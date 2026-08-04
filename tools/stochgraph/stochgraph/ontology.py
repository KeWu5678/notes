"""The ontology itself — every label, every edge type, every key, with its meaning.

Single source of truth for the schema. The projection imports its edge names from
here, the loader documents itself from here, and `CONCEPTS.md` is rendered from
here, so the three cannot drift apart.

Naming note: the implication edges are called ``SUFF`` rather than ``IMPLIES``.
"A implies B" invites reading the edge as material implication between propositions;
what the edge actually records is that hypothesis A is *sufficient* to conclude B —
and, crucially, only when A is sufficient **on its own**. A hypothesis that needs
company gets ``SUFF_GIVEN``, never the bare form.

The Python constants keep their long names (``SUFFICIENT_FOR``); only the edge type
written into the graph is abbreviated, so the code stays readable while the browser
stays legible.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class LabelSpec:
    name: str
    definition: str
    examples: str = ""


@dataclass(frozen=True)
class EdgeSpec:
    name: str
    source: str
    target: str
    layer: str          # "1" statement layer · "2" concept layer
    definition: str
    keys: str = ""


# --------------------------------------------------------------------------- #
# node labels                                                                 #
# --------------------------------------------------------------------------- #

NODE_LABELS: List[LabelSpec] = [
    LabelSpec(
        "Object", "A thing that exists in the theory.",
        "Brownian motion, a filtration, M, L(M), the predictable σ-field",
    ),
    LabelSpec(
        "Property",
        "An arity-1 predicate: something a single object can satisfy.",
        "adapted, continuous, L²-bounded, progressively measurable",
    ),
    LabelSpec(
        "Relation",
        "An arity-≥2 predicate: something that holds between objects. "
        "A property is just a relation of arity 1, so the two differ only by arity.",
        "modification, indistinguishable, subset of, dense in",
    ),
    LabelSpec(
        "Statement",
        "An assertion made by the notes, carrying its verbatim text, page and "
        "provenance. This is the unit that gets cited.",
        "Proposition 1.1.4, Theorem 3.3.6, Exercise 1",
    ),
    LabelSpec(
        "Definition",
        "A statement that *introduces* a concept rather than asserting something "
        "about existing ones. Always carries `:Statement` as well — Neo4j labels "
        "are flat, so nothing is inherited automatically.",
        "Definition 1.1.1",
    ),
    LabelSpec(
        "Fact",
        "A reified assertion — a predicate applied to named arguments. Created "
        "**only** when something must point at the assertion itself, as when one "
        "statement declares two facts equivalent. Everywhere else an assertion is "
        "an edge, because an unbound fact is isomorphic to its predicate and a "
        "node would be pure indirection.",
        "\"M has a right-continuous modification\" in Theorem 1.3.12",
    ),
    LabelSpec(
        "Source", "A location in the notes: chapter and section. Provenance, not "
        "mathematics.",
        "§1.1",
    ),
]

# Second label on an `:Object`. Extensible: the stable layer is `:Object`, so adding
# a refinement never invalidates an existing query.
OBJECT_REFINEMENTS: List[LabelSpec] = [
    LabelSpec("FunctionSpace", "A space of functions or processes.", "M, L(M), L₀"),
    LabelSpec("Process", "A stochastic process.", "Brownian motion, ⟨M⟩, h·M"),
    LabelSpec("Measure", "A measure.", "Wiener measure, the Doleans measure ℙ_M"),
    LabelSpec("Map", "A map between spaces.", "the stochastic integral I: L₀ → M"),
    LabelSpec("SigmaField", "A σ-field or a family of them.",
              "the predictable σ-field, a filtration (F_t)"),
    LabelSpec("Space", "A set carrying structure — measure, topology, inner product.",
              "a probability space, a filtered probability space, a Hilbert space"),
]


# --------------------------------------------------------------------------- #
# edge types                                                                  #
# --------------------------------------------------------------------------- #

# Layer 1 — a statement to what it is about. Authored (extracted), exact.
CITES = "CITES"
REQUIRES = "REQUIRES"
CONCLUDES = "CONCLUDES"
DEFINES = "DEFINES"
ABOUT = "ABOUT"
IN = "IN"

# Layer 2 — concept to concept. Derived by projection from layer 1, never authored.
SUFFICIENT_FOR = "SUFF"
SUFFICIENT_FOR_GIVEN = "SUFF_GIVEN"
NOT_SUFFICIENT_FOR = "NOT_SUFF"
NOT_SUFFICIENT_FOR_GIVEN = "NOT_SUFF_GIVEN"
HAS_PROPERTY = "HAS_PROPERTY"
NOT_HAS_PROPERTY = "NOT_HAS_PROPERTY"

# Reified assertions (used sparingly — see the `:Fact` label).
PREDICATE = "PREDICATE"
ARG = "ARG"
EQUIVALENT = "EQUIVALENT"

EDGE_TYPES: List[EdgeSpec] = [
    EdgeSpec(
        CITES, "Statement", "Statement", "1",
        "This statement's text or proof references that one. Read mechanically "
        "from the PDF's link annotations, so it is ground truth.",
        "_via is not needed — the edge itself is the citation",
    ),
    EdgeSpec(
        REQUIRES, "Statement", "Property | Relation", "1",
        "This statement assumes that predicate. Unbound: it records *that* "
        "left-continuity is assumed, not of which object.",
    ),
    EdgeSpec(
        CONCLUDES, "Statement", "Property | Relation", "1",
        "This statement asserts that predicate.", "negated",
    ),
    EdgeSpec(
        DEFINES, "Definition", "Object | Property | Relation", "1",
        "This definition introduces that concept. The concept layer's provenance.",
    ),
    EdgeSpec(
        ABOUT, "Statement", "Object", "1",
        "The objects the statement is about — its subject.",
    ),
    EdgeSpec(IN, "Statement", "Source", "1", "Where the statement sits in the notes."),
    EdgeSpec(
        SUFFICIENT_FOR, "Property | Relation", "Property | Relation", "2",
        "The source predicate is sufficient, **on its own**, for the target. "
        "Emitted only when the statement has exactly one hypothesis, so the edge "
        "is true read in isolation.",
        "_via",
    ),
    EdgeSpec(
        SUFFICIENT_FOR_GIVEN, "Property | Relation", "Property | Relation", "2",
        "The source predicate is sufficient for the target **only together with** "
        "the conditions in `under`. Never confuse with the bare form: alone, the "
        "source does not suffice.",
        "_via, under",
    ),
    EdgeSpec(
        NOT_SUFFICIENT_FOR, "Property | Relation", "Property | Relation", "2",
        "The source is **not** sufficient for the target — the converse fails in "
        "general. First-class, because a graph that cannot say this lets an agent "
        "derive the converse.",
        "_via",
    ),
    EdgeSpec(
        NOT_SUFFICIENT_FOR_GIVEN, "Property | Relation", "Property | Relation", "2",
        "Not sufficient even together with `under`.", "_via, under",
    ),
    EdgeSpec(
        HAS_PROPERTY, "Object", "Property", "2",
        "A named object satisfies a property.", "_via, under",
    ),
    EdgeSpec(
        NOT_HAS_PROPERTY, "Object", "Property", "2",
        "A named object does not satisfy a property.", "_via, under",
    ),
    EdgeSpec(
        PREDICATE, "Fact", "Property | Relation", "1",
        "The predicate a reified assertion applies.",
    ),
    EdgeSpec(
        ARG, "Fact", "Object", "1",
        "An argument of a reified assertion; `i` is its position.", "i",
    ),
    EdgeSpec(
        EQUIVALENT, "Fact", "Fact", "2",
        "The two assertions hold under exactly the same circumstances — each is "
        "sufficient for the other. The reason `:Fact` exists: an equivalence needs "
        "assertions as endpoints, and an edge cannot end on an edge.",
        "_via, under",
    ),
    EdgeSpec(
        "«relation name»", "Object", "Object", "2",
        "One edge type per `:Relation` node, named after it — `SUBSET_OF`, "
        "`DENSE_IN`, `EQUALS`, `HAS`, and their `NOT_` forms. Generated when a "
        "statement "
        "concludes a binary relation between two *named* objects. None exist yet: "
        "the space inclusions live in chapter 4.",
        "_via, under",
    ),
]

EDGE_KEYS: List[LabelSpec] = [
    LabelSpec(
        "_via",
        "Bookkeeping. The node id of the statement that justifies this edge — "
        "every derived edge can be traced back to a citable page.",
    ),
    LabelSpec(
        "under",
        "Mathematics. The further hypotheses this edge depends on, as concept ids "
        "(never prose). A denormalization for browsing; the exact form is the "
        "statement's REQUIRES edges.",
    ),
    LabelSpec(
        "negated",
        "Mathematics. Marks a CONCLUDES edge whose assertion is a denial.",
    ),
]
