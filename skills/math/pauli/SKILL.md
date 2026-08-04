---
name: pauli
description: answering style for terminal readability; set the answering style. Use when the user asks a math question
---

## answering style:  
1. Keep anwssers clean and concise. Use the bold or underline text for separation or highlighting important parts.  
2. output math style: 
The terminal shows LaTeX source instead of rendered formulas, so write math with Unicode symbols (`∫ ∞ √ π φ σ μ Δ ≤ ≥ → ∈ ∑ ² ³`), not LaTeX commands like `\int` or `\frac`. Use LaTeX only if explicitly asked.

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

AVOID:
1. Stating a variable without defining. 
2. Invent terms. Search for established definition first. If not available, always inform the user the term is defined by agents and give the precise definition. 

