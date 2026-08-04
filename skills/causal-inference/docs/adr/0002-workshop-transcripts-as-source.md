# 0002 — Workshop transcripts as a second source tier

Date: 2026-07-28
Status: accepted
Amends: [0001](./0001-deck-only-sourcing.md)

## Context

ADR 0001 restricted every failure mode to the seven lecture PDFs, and listed the
cost: bad control and near-instrument depletion absent, steps 2 and 5 thin,
"practitioner traps missing — tuning before rather than inside cross-fitting,
covariate selection under high-dimensional $X$, trimming threshold choice". It
closed by saying that if the rule were relaxed it should be relaxed in one
deliberate pass over all nine skills, with a second tier of `src:` tags.

Two transcripts of the workshop itself have since been added to the vault:

- `Causal Inference Workshop Auto1 Day1 — transcript.md` (27 Feb 2026)
- `Causal Inference Workshop Auto1 Day2 — transcript.md` (6 Mar 2026)

plus the Gemini summary notes for each day. These are not new material of a
different kind — they are the presenters talking through the same seven decks,
in the same sessions, answering questions from the room. Most of the caveats
0001 wanted are in them, spoken:

- an instrument-like covariate — a strong predictor of $D$ that does not affect
  $Y$ — "could increase variance of your estimation" (`[D1] 01:54`), the exact
  mechanism 0001 recorded as absent
- interference between units, and which way it biases the estimate
  (`[D2] 02:37–02:38`)
- covariate selection by feature importance is invalid, with the Lasso
  omitted-variable mechanism (`[D2] 00:05–00:11, 00:43`)
- learner choice by out-of-sample nuisance error rather than by the estimate,
  and why the disagreement is a finite-sample phenomenon (`[D2] 00:40, 00:46`)
- hyperparameters tuned per cross-fitting fold — "really not a good idea"
  (`[D1] 02:13`)
- the package returns an estimate whether or not the identification assumption
  holds (`[D2] 02:45–02:46`)

## Decision

**Two source tiers, both traceable.** Failure modes may cite either:

| Tier | Keys | Locator |
|---|---|---|
| Lecture decks | `[Intro]` `[Recap]` `[Sens]` `[DiD]` `[Tune]` `[Het]` `[Closing]` | slide page — `[Sens] p.35` |
| Workshop transcripts | `[D1]` `[D2]` | timestamp — `[D2] 02:37` |

Timestamps refer to the nearest preceding `### hh:mm:ss` heading in the
transcript file; a range spans several.

Everything else stays excluded, unchanged from 0001: not the notebooks, not the
reference papers, not this vault's own notes, not agent-supplied practitioner
knowledge. **Gaps are still silent.** Skills are still **stateless**.

**Transcripts are cited for substance, never quoted verbatim.** Both files carry
"This transcript was computer generated and might contain errors", and the
speech is disfluent. A `src: [D1] hh:mm` claims *this point was made here*, not
*these were the words*.

## Consequences

- The sharpest omission named in 0001 — the near-instrument variance inflation —
  is now in step 1, sourced. So is interference, which neither the decks nor 0001
  covered at all.
- **The trust surface widens from edited slides to unedited speech.** A slide was
  written to be defensible; an answer to a question in the room was not. Several
  new entries are explicitly hedged by the speaker ("I would say", "usually",
  "rule of thumb"), and are recorded at `[WARNING]` or `[NOTE]` rather than
  `[BLOCKER]` for that reason.
- **Timestamps are a weaker locator than page numbers.** A slide citation can be
  checked in seconds; a timestamp needs a paragraph read around it.
- Steps 0, 1 and 8 gained the most; step 5 stayed thin, because the transcripts
  say little about it that the decks do not.
- The Gemini summary notes are *not* a source. They paraphrase the transcripts
  and would add a third layer of lossy restatement for nothing. Cite the
  transcript.

## Revisiting

The next candidate tier is the three notebooks, which 0001 also excluded. They
differ from both current tiers in being executable rather than said, so admitting
them raises a question these two tiers do not: whether a behaviour observed in a
notebook run is a claim about DoubleML or about that dataset. Decide that before
adding a `[NB]` key.
