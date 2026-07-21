---
name: p-math
description: Format mathematical explanations for terminal readability; set the answering style. Use when the user asks a math question, requests a derivation, asks for intuition, or discusses probability, stochastic analysis, calculus, linear algebra, statistics, or related mathematical notation, especially when raw LaTeX would be hard to read.
---

# Preferred Math Formatting

The terminal shows LaTeX source instead of rendered formulas, so write math with Unicode symbols (`∫ ∞ √ π φ σ μ Δ ≤ ≥ → ∈ ∑ ² ³`), not LaTeX commands like `\int` or `\frac`. Use LaTeX only if explicitly asked.

**Shape the answer:** lead with the intuition in a few sentences, then the derivation. Keep prose between steps short — explain what each step does without burying the formulas.

**Display derivations** in aligned code blocks, with the justification for each step set off to the right:

```text
    E[Z⁴]
  = ∫_{-∞}^{∞} x⁴ φ(x) dx
  = -∫_{-∞}^{∞} x³ φ'(x) dx          since φ'(x) = -xφ(x)
  = -[x³ φ(x)]_{-∞}^{∞}
    + ∫_{-∞}^{∞} 3x² φ(x) dx          integration by parts
  = 3∫_{-∞}^{∞} x² φ(x) dx            boundary term is 0
  = 3E[Z²] = 3
```

Use inline backticks for short formulas. Match the user's notation when they've set one.

# Answring style

**answering style**:  
1. Keep anwssers clean and concise. Use the bold or underline text for separation or highlighting important parts.  
2. Never stating a variable without defining. 
3. DON'T INVENT terms. Search for established definition first. If not available, always inform the user the term is defined by me and give the precise definition. 
