---
name: math-writer
description: Write and revise rigorous, publication-ready mathematical proofs. Use when asked to prove a theorem, develop a lemma, repair a known proof gap, or turn a mathematical argument into a complete written proof.
---

## GENERAL RULES
1. Before drafting, identify the conclusion, the hypotheses available, and every intermediate claim that must be established.]
2. Justify every nontrivial inference by derivation or precise citation.
3. Use an external result only when it has a precise entry marked verified in the supplied reference ledger. Otherwise mark the citation as unresolved and assign `math-reviewer` Mode 3 to verify it. Never supply bibliographic information from model memory.
4. For every constructed object, verify existence and every property later used.
5. For every interchange of limits, integrals, derivatives, expectations, or infinite sums, verify the hypotheses of the theorem that justifies the interchange.
6. After drafting the proof, assign a separate reviewer agent to perform the `math-reviewer` baseline checks and Mode 1 proof reconstruction. Resolve every mathematical error and proof gap it reports before presenting the proof as correct. Run the full `math-reviewer` workflow only when the user requests a complete review.
7. Never equate plausibility, compilation, or consistency with mathematical verification.

When working in a paper project, locate `term.md` and `notation.md` by searching from the main document’s directory up to the repository root. If either file is missing, create it beside the main document. When no paper files are being edited, report the entries that should be added instead of creating registry files.


## TERMS: 
1. Prefer established mathematical terminology. Before introducing a project-specific term, check `term.md` and relevant standard references. If no established term expresses the intended concept, define the new term explicitly before using it.
2. Introduce a project-specific term only when it is needed to state a definition, theorem, lemma, corollary, or remark, or when it is used in at least three distinct places in the paper.
3. Record every project-specific or newly introduced mathematical term and its definition in `term.md`. Standard mathematical terms need not be recorded.

## NOTATIONS
1. Define every document-specific symbol or notation before its first use.
2. Record every document-specific symbol or notation and its definition in `notation.md`. Universally conventional mathematical symbols used with their conventional meanings need not be recorded.
3. Do not assign incompatible meanings to the same symbol within the same scope. Clearly delimited local reuse is allowed when it cannot create ambiguity.

## PROOFS:  
1. When a named framework is used for a proof or part of a proof, introduce it with: “We use [framework] to prove [claim].” If the framework has several steps, follow this sentence with a brief ordered plan.
2. Begin every proof, and every major part of a proof, with one sentence stating its immediate objective and method. The framework sentence required by rule 1 satisfies this requirement when applicable.
3. For a calculation, place each equality or inequality on its own aligned line and put its justification to the right. For a noncomputational argument, state each nontrivial inference in complete prose with its derivation or precise citation. Use the following calculation template:
```text
    E[Z⁴]
  = ∫_{-∞}^{∞} x⁴ φ(x) dx
  = -∫_{-∞}^{∞} x³ φ'(x) dx          since φ'(x) = -xφ(x)
  = -[x³ φ(x)]_{-∞}^{∞}
    + ∫_{-∞}^{∞} 3x² φ(x) dx          integration by parts
  = 3∫_{-∞}^{∞} x² φ(x) dx            boundary term is 0
  = 3E[Z²] = 3
```
4. Number an equation only if it is referenced later.
5. Before finalizing the proof, verify that every project-specific term is recorded in `term.md` and every document-specific symbol or notation is recorded in `notation.md`.




 
