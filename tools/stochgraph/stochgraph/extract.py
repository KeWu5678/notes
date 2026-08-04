"""Stage 0 — mechanical extraction of the statement layer from StochAna.pdf.

No LLM, no inference: every node and edge produced here is read directly off the
PDF, so the whole output carries provenance tier ``verbatim``.

Two views of the PDF are combined, because neither alone is enough:

* ``pdftotext -layout`` gives clean text in reading order. Statement prose comes
  out word-for-word; only symbols flatten (``M_t^2`` -> ``Mt2``).
* ``pdftohtml -xml`` gives per-run font families, positions and — the reason we
  need it — the internal link annotations that encode every cross-reference.

The xml alone cannot supply the text: runs are fragmented by font (a statement
body arrives as a dozen interleaved italic/math runs) and baselines are not
monotonic, so "Proof:" can sort ahead of the line it introduces.

Structure is recovered from three typographic signals, all exact:

* a declaration is a run in the bold font (``CMBX``) whose text opens with an
  environment keyword — 273 across the book, with no in-text reference
  misread as a declaration;
* a statement body runs until its proof, the next declaration, or a heading;
* ``◻`` closes a proof, which bounds the region a citation is attributed to.
"""

from __future__ import annotations

import re
import subprocess
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterator, List, Optional, Tuple

# Environment keywords as they appear in the notes. `Definition` is the only one
# that is ontologically distinct (it introduces rather than asserts); the rest
# are a rhetorical distinction and are kept only as the `_kind` bookkeeping key.
ENV_KEYWORDS = (
    "Definition", "Theorem", "Proposition", "Lemma", "Corollary",
    "Remark", "Example", "Exercise", "Assumption",
)
ENV_RE = re.compile(
    r"^(?P<kind>" + "|".join(ENV_KEYWORDS) + r")\s+(?P<ref>\d+(?:\.\d+)*)\.?"
    # Some results carry their classical name in the bold header itself
    # ("Lemma 1.3.15 (Backwards martingale convergence)"); others put it in the
    # italic body. Accepting it here is what keeps those declarations from being
    # missed altogether. The closing parenthesis is optional because a name
    # containing an accent or math ("Arzela-Ascoli", "Tightness in C([0,1],R)")
    # is split across runs by poppler, leaving the bracket unbalanced.
    r"\s*(?P<name>\(.*)?$"
)

BOLD_FAMILY = "CMBX"          # theorem-header font
ROW_TOLERANCE = 10            # px; sub/superscripts sit a few px off baseline
QED = "◻"

# A section heading in the text layer: "4.2.1    The space M".
SECTION_RE = re.compile(r"^\s*(?P<num>\d+(?:\.\d+){1,2})\s{2,}(?P<title>\S.*)$")
CHAPTER_RE = re.compile(r"^\s*Chapter\s+(?P<num>\d+)\s*$")
PROOF_RE = re.compile(r"^\s*Proof\s*[:.]", re.IGNORECASE)

# Anchor text of a cross-reference link: "3.3.6", "(2.5)", "39", "25(i)".
ANCHOR_REF_RE = re.compile(r"^\(?(?P<ref>\d+(?:\.\d+)*)\)?")

# The notes run to six chapters and about seventy exercises. A ref outside those
# shapes is a poppler artefact, not a citation: an anchor split mid-number
# ("2.3.10." breaking after "2.3.1") leaves a fragment like "0." behind. Such a
# ref is rejected and reported rather than turned into an edge, because a wrong
# edge in the verbatim tier is worse than a missing one.
MAX_CHAPTER = 6
MAX_EXERCISE = 70


def plausible_ref(ref: str) -> bool:
    parts = ref.split(".")
    if len(parts) == 1:
        return 1 <= int(parts[0]) <= MAX_EXERCISE
    return 1 <= int(parts[0]) <= MAX_CHAPTER and all(int(p) >= 1 for p in parts[1:])


@dataclass
class Run:
    """One positioned text run from the xml layer."""
    page: int
    top: int
    left: int
    family: str
    text: str

    @property
    def bold(self) -> bool:
        return BOLD_FAMILY in self.family


@dataclass
class Link:
    """An internal cross-reference link annotation."""
    page: int
    top: int
    target_page: int
    anchor: str
    left: int = 0

    @property
    def ref(self) -> Optional[str]:
        m = ANCHOR_REF_RE.match(self.anchor.strip())
        return m.group("ref") if m else None

    @property
    def is_equation(self) -> bool:
        """Numbered display equations are cited parenthesised: "(2.5)".

        The distinction is load-bearing: equation (2.5) and Proposition 2.5 are
        different objects, and dropping the parentheses would forge an edge
        between unrelated nodes.
        """
        return self.anchor.strip().startswith("(")


@dataclass
class Declaration:
    """A numbered environment, located by the bold header run."""
    kind: str
    ref: str
    page: int
    top: int
    name: str = ""      # classical name, when the header carries one


@dataclass
class Statement:
    """One node of the statement layer."""
    ref: str
    kind: str
    page: int
    top: int
    text: str
    name: str
    chapter: int
    section: str
    proved_here: bool
    end_page: int
    end_top: int
    cites: List[str] = field(default_factory=list)
    cites_equations: List[str] = field(default_factory=list)

    @property
    def is_definition(self) -> bool:
        return self.kind == "Definition"

    @property
    def node_id(self) -> str:
        prefix = "ex" if self.kind == "Exercise" else "s"
        return f"{prefix}/{self.ref}"


# --------------------------------------------------------------------------- #
# PDF readers                                                                 #
# --------------------------------------------------------------------------- #

def read_text_pages(pdf: Path) -> Dict[int, List[str]]:
    """Page number -> lines, via ``pdftotext -layout``.

    Page numbering matches the printed page numbers of these notes (the cover is
    page 1), so no offset correction is needed.
    """
    out = subprocess.run(
        ["pdftotext", "-layout", str(pdf), "-"],
        check=True, capture_output=True, text=True,
    ).stdout
    return {i: page.splitlines() for i, page in enumerate(out.split("\f"), start=1)}


def read_xml(pdf: Path) -> Tuple[List[Run], List[Link]]:
    """Positioned runs and link annotations, via ``pdftohtml -xml``.

    ``fontspec`` elements are declared on first use rather than on every page, so
    the id -> family map is accumulated across the document.
    """
    raw = subprocess.run(
        ["pdftohtml", "-xml", "-stdout", str(pdf)],
        check=True, capture_output=True, text=True,
    ).stdout
    root = ET.fromstring(raw)

    families: Dict[str, str] = {}
    runs: List[Run] = []
    links: List[Link] = []

    for page_el in root.findall("page"):
        page = int(page_el.get("number", "0"))
        for spec in page_el.findall("fontspec"):
            families[spec.get("id", "")] = spec.get("family", "")
        for el in page_el.findall("text"):
            top, left = int(el.get("top", "0")), int(el.get("left", "0"))
            family = families.get(el.get("font", ""), "")
            text = "".join(el.itertext())
            if text.strip():
                runs.append(Run(page, top, left, family, text))
            for a in el.findall("a"):
                href = a.get("href", "")
                if "#" not in href:
                    continue
                try:
                    target = int(href.rsplit("#", 1)[1])
                except ValueError:
                    continue
                links.append(
                    Link(page, top, target, "".join(a.itertext()), left)
                )

    return runs, merge_link_fragments(links)


def merge_link_fragments(links: List[Link]) -> List[Link]:
    """Rejoin one reference that poppler split across runs.

    A reference whose text changes font mid-way ("2.3.10." breaking after
    "2.3.1") arrives as two link annotations on the same row pointing at the same
    page. Left as-is they yield a nonsense ref ("0") and therefore a wrong edge,
    so fragments sharing a row and a target are concatenated in reading order.
    """
    buckets: Dict[Tuple[int, int, int], List[Link]] = {}
    for link in links:
        key = (link.page, link.top // ROW_TOLERANCE, link.target_page)
        buckets.setdefault(key, []).append(link)

    merged: List[Link] = []
    for parts in buckets.values():
        parts.sort(key=lambda l: l.left)
        first = parts[0]
        merged.append(
            Link(
                first.page, first.top, first.target_page,
                "".join(p.anchor for p in parts), first.left,
            )
        )
    merged.sort(key=lambda l: (l.page, l.top, l.left))
    return merged


# --------------------------------------------------------------------------- #
# Structure                                                                    #
# --------------------------------------------------------------------------- #

def find_declarations(runs: List[Run]) -> List[Declaration]:
    """Bold runs opening with an environment keyword.

    The bold font is used for nothing else, so this is exact: an in-text
    "…follows from Theorem 4.2.2" sits in the roman body font and is skipped.
    """
    decls: List[Declaration] = []
    for run in runs:
        if not run.bold:
            continue
        m = ENV_RE.match(run.text.strip())
        if m:
            name = (m.group("name") or "").strip().lstrip("(").rstrip(")").strip()
            decls.append(
                Declaration(m.group("kind"), m.group("ref"), run.page, run.top, name)
            )
    decls.sort(key=lambda d: (d.page, d.top))
    return decls


def find_qed_marks(runs: List[Run]) -> List[Tuple[int, int]]:
    """(page, top) of every QED box — the end of a proof."""
    marks = [(r.page, r.top) for r in runs if QED in r.text]
    marks.sort()
    return marks


def section_index(pages: Dict[int, List[str]]) -> Dict[int, List[Tuple[int, str, str]]]:
    """page -> [(line_no, section number, title)] for section headings."""
    index: Dict[int, List[Tuple[int, str, str]]] = {}
    for page, lines in pages.items():
        found = []
        for i, line in enumerate(lines):
            m = SECTION_RE.match(line)
            if m and not line.strip().endswith("."):
                found.append((i, m.group("num"), m.group("title").strip()))
        if found:
            index[page] = found
    return index


def _dehyphenate(lines: List[str]) -> str:
    """Join wrapped lines, healing words split across a line break."""
    out = ""
    for line in lines:
        piece = line.strip()
        if not piece:
            continue
        if out.endswith("-"):
            out = out[:-1] + piece
        elif out:
            out += " " + piece
        else:
            out = piece
    return re.sub(r"\s+", " ", out).strip()


def _header_line(lines: List[str], kind: str, ref: str) -> Optional[int]:
    """Index of the line declaring ``kind ref`` on this page."""
    needle = f"{kind} {ref}"
    for i, line in enumerate(lines):
        if line.lstrip().startswith(needle):
            return i
    return None


def build_rows(runs: List[Run]) -> Dict[int, List[Tuple[int, List[Run]]]]:
    """page -> [(top, runs)], one entry per visual row.

    Runs are clustered by baseline because poppler emits a separate run per font
    change, so a single printed line arrives as many runs at near-equal ``top``.
    """
    by_page: Dict[int, List[Run]] = {}
    for run in runs:
        by_page.setdefault(run.page, []).append(run)

    rows: Dict[int, List[Tuple[int, List[Run]]]] = {}
    for page, page_runs in by_page.items():
        clustered: List[Tuple[int, List[Run]]] = []
        for run in sorted(page_runs, key=lambda r: (r.top, r.left)):
            if clustered and run.top - clustered[-1][0] <= ROW_TOLERANCE:
                clustered[-1][1].append(run)
            else:
                clustered.append((run.top, [run]))
        rows[page] = clustered
    return rows


def _is_italic_row(row: List[Run]) -> bool:
    return any("CMTI" in r.family for r in row)


# Roman body text: CMR10 is the running prose face, CMCSC10 sets "Proof:".
# CMR7/CMR5 are the small sizes used for sub- and superscripts, so they are not
# evidence of prose.
BODY_ROMAN = ("CMR10", "CMCSC10")


def _has_roman_prose(row: List[Run]) -> bool:
    """Does this row contain actual roman *words*?

    A displayed formula ends up with stray CMR10 runs for its numerals ("1", "0"),
    so the presence of the face alone does not mean prose. Requiring several
    letters in one run distinguishes narrative from a numbered display, which is
    what lets a statement keep a formula that trails its final clause.
    """
    for run in row:
        if any(fam in run.family for fam in BODY_ROMAN):
            if sum(c.isalpha() for c in run.text) >= 4:
                return True
    return False


HEAD_MARGIN = 130  # px; body text starts below the running head


def _is_running_head(top: int) -> bool:
    """The repeated chapter line and page number at the top of every page.

    Detected by position, not by font: the slanted family ``CMSL`` also sets the
    *defined term* inside a definition ("…have the same finite dimensional
    distributions"), so a font test would swallow definition headers.
    """
    return top < HEAD_MARGIN


def _starts_declaration(row: List[Run]) -> bool:
    return any(r.bold and ENV_RE.match(r.text.strip()) for r in row)


def statement_row_span(
    rows: Dict[int, List[Tuple[int, List[Run]]]],
    decl: Declaration,
    max_rows: int = 30,
) -> Tuple[int, int, int, bool]:
    """(row count, end page, end top, proof follows) for a declaration's statement.

    The notes set statement bodies in italic and everything else — narrative,
    proofs, headings — in roman. So the statement is exactly the header row plus
    the following italic rows, and the first non-italic row terminates it. This
    is what makes multi-part statements ("i) … ii) …", displayed formulas inside
    a hypothesis) come out whole rather than truncating at the first blank line.
    """
    page = decl.page
    page_rows = rows.get(page, [])
    # Locate by content, not by ``top``: a neighbouring run (a superscript a few
    # pixels higher) can seed the cluster, so the row's top need not equal the
    # header run's top.
    start = next(
        (
            i for i, (_, row) in enumerate(page_rows)
            if any(
                r.bold and (m := ENV_RE.match(r.text.strip()))
                and m.group("ref") == decl.ref and m.group("kind") == decl.kind
                for r in row
            )
        ),
        None,
    )
    if start is None:
        return 0, decl.page, decl.top, False

    count = 0
    end_page, end_top = page, decl.top
    i = start

    while count < max_rows:
        page_rows = rows.get(page, [])
        if i >= len(page_rows):
            # Continue onto the next page only if the statement is still running.
            if page + 1 not in rows:
                break
            page, i = page + 1, 0
            continue

        top, row = page_rows[i]
        if _is_running_head(top):
            i += 1
            continue
        if count and _starts_declaration(row):
            break
        if count and not _is_italic_row(row) and _has_roman_prose(row):
            text = " ".join(r.text for r in row)
            return count, end_page, end_top, "Proof" in text

        count += 1
        end_page, end_top = page, top
        i += 1

    return count, end_page, end_top, False


def _looks_like_running_head(line: str) -> bool:
    """The chapter/section line reprinted at the top of each page in the text layer."""
    stripped = re.sub(r"^\s*[\d.]*\s*", "", line).strip()
    stripped = re.sub(r"\s*\d+\s*$", "", stripped)
    letters = [c for c in stripped if c.isascii() and c.isalpha()]
    if len(letters) <= 8:
        return False
    # Ratio rather than "all upper": these heads carry Greek lowercase
    # ("σ-FIELDS AND STOPPING TIMES"), which no all-caps test would pass.
    return sum(c.isupper() for c in letters) / len(letters) >= 0.9


def extract_statement_text(
    pages: Dict[int, List[str]],
    decl: Declaration,
    n_rows: int,
) -> str:
    """The statement's verbatim text: ``n_rows`` non-blank lines from the header.

    The row count comes from the xml layer (which knows the typography) while the
    text comes from ``pdftotext`` (which knows the reading order) — neither layer
    can do both.
    """
    start = _header_line(pages.get(decl.page, []), decl.kind, decl.ref)
    if start is None or n_rows <= 0:
        return ""

    collected: List[str] = []
    page, i = decl.page, start
    while len(collected) < n_rows:
        lines = pages.get(page, [])
        if i >= len(lines):
            if page + 1 not in pages:
                break
            page, i = page + 1, 0
            continue
        line = lines[i]
        stripped = line.strip()
        # Hard boundary, independent of the row count: a statement can never
        # contain the next declaration's header. The row count is derived from
        # typography and can over-count when a footnote sits at the foot of the
        # page, so this guard is what stops the over-run reaching the next result.
        if collected and ENV_RE.match(stripped.split("  ")[0].strip()):
            break
        if collected and re.match(
            r"^(" + "|".join(ENV_KEYWORDS) + r")\s+\d+(\.\d+)*\b", stripped
        ):
            break
        if collected and CHAPTER_RE.match(line):
            break
        if stripped and not _looks_like_running_head(line):
            collected.append(line)
        i += 1

    text = _dehyphenate(collected)
    return re.sub(
        rf"^{decl.kind}\s+{re.escape(decl.ref)}\.?\s*", "", text
    ).strip()


def statement_regions(
    decls: List[Declaration],
    qed: List[Tuple[int, int]],
    last_page: int,
) -> List[Tuple[int, int]]:
    """End position (page, top) of each declaration's statement+proof region.

    A citation inside a proof is a real dependency of the statement it proves, so
    the region deliberately spans the proof: it ends at the QED box that closes
    the proof, or at the next declaration, whichever comes first.
    """
    ends: List[Tuple[int, int]] = []
    for i, decl in enumerate(decls):
        nxt = decls[i + 1] if i + 1 < len(decls) else None
        limit = (nxt.page, nxt.top) if nxt else (last_page + 1, 0)
        here = (decl.page, decl.top)
        closing = next((m for m in qed if here < m <= limit), None)
        ends.append(closing if closing else limit)
    return ends


def build_statements(
    pages: Dict[int, List[str]],
    runs: List[Run],
    links: List[Link],
    first_page: int,
    last_page: int,
) -> Tuple[List[Statement], List[Dict[str, str]]]:
    """Assemble the statement layer for the given printed page range."""
    decls = find_declarations(runs)
    qed = find_qed_marks(runs)
    ends = statement_regions(decls, qed, max(pages))
    sections = section_index(pages)

    # Running section context, tracked across the whole document so a statement
    # on a page with no heading still knows which section it is in.
    current_section = ""
    section_at: Dict[Tuple[int, int], str] = {}
    for page in sorted(pages):
        headings = sections.get(page, [])
        idx = 0
        for i, _line in enumerate(pages[page]):
            while idx < len(headings) and headings[idx][0] <= i:
                current_section = headings[idx][1]
                idx += 1
            section_at[(page, i)] = current_section

    rows = build_rows(runs)

    statements: List[Statement] = []
    for i, decl in enumerate(decls):
        if not (first_page <= decl.page <= last_page):
            continue
        n_rows, _, _, proved_here = statement_row_span(rows, decl)
        text = extract_statement_text(pages, decl, n_rows)

        header_line = _header_line(pages.get(decl.page, []), decl.kind, decl.ref)
        section = section_at.get((decl.page, header_line or 0), "")
        # A chapter's opening definition precedes its first numbered section
        # heading, so the running section context would still name the previous
        # chapter. The ref is authoritative about which chapter a result is in.
        if "." in decl.ref and section:
            if decl.ref.split(".")[0] != section.split(".")[0]:
                section = ""
        # An exercise's ref carries no chapter; take it from the section.
        chapter = int(decl.ref.split(".")[0]) if "." in decl.ref else (
            int(section.split(".")[0]) if section else 0
        )

        end_page, end_top = ends[i]
        statements.append(
            Statement(
                ref=decl.ref, kind=decl.kind, page=decl.page, top=decl.top,
                text=text, name=decl.name, chapter=chapter, section=section,
                proved_here=proved_here, end_page=end_page, end_top=end_top,
            )
        )

    rejected = attach_citations(statements, decls, ends, links)
    return statements, rejected


def attach_citations(
    statements: List[Statement],
    decls: List[Declaration],
    ends: List[Tuple[int, int]],
    links: List[Link],
) -> List[Dict[str, str]]:
    """Assign each link annotation to the statement whose region contains it.

    Returns the rejected anchors so they surface in the manifest for review.
    """
    rejected: List[Dict[str, str]] = []
    regions = [
        ((d.page, d.top), ends[i], d.ref, d.kind) for i, d in enumerate(decls)
    ]
    by_ref = {(s.ref, s.kind): s for s in statements}

    for link in links:
        pos = (link.page, link.top)
        ref = link.ref
        if not ref or not plausible_ref(ref):
            rejected.append(
                {"page": str(link.page), "anchor": link.anchor.strip()}
            )
            continue
        for start, end, owner_ref, owner_kind in regions:
            if start <= pos <= end:
                stmt = by_ref.get((owner_ref, owner_kind))
                if not stmt:
                    break
                bucket = stmt.cites_equations if link.is_equation else stmt.cites
                # Self-references (a proof pointing back at its own statement)
                # and duplicates carry no information.
                if (link.is_equation or ref != stmt.ref) and ref not in bucket:
                    bucket.append(ref)
                break

    return rejected


def load(
    pdf: Path, first_page: int, last_page: int
) -> Tuple[List[Statement], List[Dict[str, str]]]:
    """Run stage 0 over a printed page range.

    Returns the statements and the anchors that could not be resolved to a
    citation, which the manifest reports for review.
    """
    pages = read_text_pages(pdf)
    runs, links = read_xml(pdf)
    return build_statements(pages, runs, links, first_page, last_page)
