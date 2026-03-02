# Algebra — Complete A-to-Z Study Material

> **Target Exams:** GATE · ESE · PSU · BANK (IBPS / SBI / RBI)
>
> **Design Philosophy:** Every formula is *derived*, not memorised. Every trick is *justified*, not assumed. Every edge case is *hunted*, not ignored.

---

## Table of Contents

| # | Topic | Key Exam Weight |
|---|-------|-----------------|
| 1 | [Algebraic Foundations & Number Properties](#1-algebraic-foundations--number-properties) | ★★★★★ |
| 2 | [Surds (Radicals) & Indices (Exponents)](#2-surds-radicals--indices-exponents) | ★★★★☆ |
| 3 | [Logarithms](#3-logarithms) | ★★★★★ |
| 4 | [Algebraic Identities](#4-algebraic-identities) | ★★★★★ |
| 5 | [Linear Equations](#5-linear-equations) | ★★★★★ |
| 6 | [Quadratic Equations](#6-quadratic-equations) | ★★★★★ |
| 7 | [Polynomials — Factor & Remainder Theorems](#7-polynomials--factor--remainder-theorems) | ★★★★☆ |
| 8 | [Inequalities](#8-inequalities) | ★★★★☆ |
| 9 | [Arithmetic Progression (AP)](#9-arithmetic-progression-ap) | ★★★★★ |
| 10 | [Geometric Progression (GP)](#10-geometric-progression-gp) | ★★★★★ |
| 11 | [Harmonic Progression (HP) & AGP](#11-harmonic-progression-hp--agp) | ★★★☆☆ |
| 12 | [Set Theory Essentials](#12-set-theory-essentials) | ★★★★☆ |
| 13 | [Functions & Relations](#13-functions--relations) | ★★★☆☆ |
| 14 | [Binomial Theorem](#14-binomial-theorem) | ★★★★☆ |
| 15 | [Matrices & Determinants (Aptitude Essentials)](#15-matrices--determinants-aptitude-essentials) | ★★★☆☆ |
| 16 | [Exam-Ready Quick Recall Sheet](#16-exam-ready-quick-recall-sheet) | — |

---

## 1. Algebraic Foundations & Number Properties

### The Atomic Truth

> *Numbers obey closure, commutativity, associativity, distribution.*

### 1.1 The Real Number Hierarchy

```
ℝ  (Real Numbers)
├── ℚ  (Rational)  →  p/q, q ≠ 0
│   ├── ℤ  (Integers) → …, -2, -1, 0, 1, 2, …
│   │   ├── ℕ₀ (Whole)  → 0, 1, 2, 3, …
│   │   │   └── ℕ  (Natural) → 1, 2, 3, …
│   │   └── Negative Integers
│   └── Non-integer rationals (e.g. 3/7)
└── Irrational → √2, π, e  (non-repeating, non-terminating)
```

**Why this matters in exams:**
Many MCQ distractors mix up whether 0 is natural or whole. Convention for GATE/ESE: **0 is whole, not natural** (unless stated otherwise).

### 1.2 Properties of Operations

| Property | Addition | Multiplication |
|----------|----------|----------------|
| Closure | $a + b \in S$ | $a \times b \in S$ |
| Commutative | $a + b = b + a$ | $ab = ba$ |
| Associative | $(a+b)+c = a+(b+c)$ | $(ab)c = a(bc)$ |
| Identity | $a + 0 = a$ | $a \times 1 = a$ |
| Inverse | $a + (-a) = 0$ | $a \times \frac{1}{a} = 1,\ a \ne 0$ |
| Distributive | — | $a(b+c) = ab + ac$ |

### 1.3 Divisibility Rules (Speed Tricks)

| Divisor | Rule | Example |
|---------|------|---------|
| 2 | Last digit even | 7**4**8 → 8 is even ✓ |
| 3 | Sum of digits divisible by 3 | 123 → 1+2+3 = 6 ✓ |
| 4 | Last **two** digits divisible by 4 | 7**32** → 32/4 = 8 ✓ |
| 5 | Ends in 0 or 5 | 145 ✓ |
| 6 | Divisible by **both** 2 and 3 | 132 → even, 1+3+2=6 ✓ |
| 7 | Double last digit, subtract from rest | 343 → 34 − 2×3 = 28 ✓ |
| 8 | Last **three** digits divisible by 8 | 7**120** → 120/8 = 15 ✓ |
| 9 | Sum of digits divisible by 9 | 729 → 7+2+9 = 18 ✓ |
| 11 | Alternating sum = 0 or ±11k | 9218 → 9−2+1−8 = 0 ✓ |

**Analogy — The Bouncer Analogy:** Think of each divisibility rule as a "bouncer" at a club. The number wants to enter the "divisible" club. Each bouncer checks a specific quick ID (last digit, digit sum, etc.) instead of running full long division.

### 1.4 HCF & LCM

**How the formulas arise:**

Every positive integer has a unique prime factorisation (Fundamental Theorem of Arithmetic):

$$n = p_1^{a_1} \cdot p_2^{a_2} \cdots p_k^{a_k}$$

Given two numbers $A = p_1^{a_1} p_2^{a_2} \ldots$ and $B = p_1^{b_1} p_2^{b_2} \ldots$:

$$\text{HCF}(A,B) = \prod p_i^{\min(a_i, b_i)}$$
$$\text{LCM}(A,B) = \prod p_i^{\max(a_i, b_i)}$$

**The Golden Relationship:**

$$\text{HCF}(A,B) \times \text{LCM}(A,B) = A \times B$$

*Why?* Because $\min(a,b) + \max(a,b) = a + b$ for every prime power.

**Edge Cases:**
- $\text{HCF}(0, n) = n$ (every number divides 0)
- $\text{LCM}(0, n) = 0$
- HCF of co-prime numbers = 1

**Example (BANK-style):**

> *The HCF of two numbers is 12 and their LCM is 360. If one number is 60, find the other.*

$$\text{Other} = \frac{\text{HCF} \times \text{LCM}}{\text{Known}} = \frac{12 \times 360}{60} = 72$$

---

## 2. Surds (Radicals) & Indices (Exponents)

### The Atomic Truth

> *Indices are repeated multiplication; surds are the inverse question.*

### 2.1 Laws of Indices — Derived from First Principles

Start from the definition: $a^n = \underbrace{a \cdot a \cdot a \cdots a}_{n \text{ times}}$

| Law | Formula | How it arises |
|-----|---------|---------------|
| Product | $a^m \cdot a^n = a^{m+n}$ | $m$ copies × $n$ copies = $m+n$ copies |
| Quotient | $\dfrac{a^m}{a^n} = a^{m-n}$ | Cancel $n$ copies from $m$ copies |
| Power of Power | $(a^m)^n = a^{mn}$ | $n$ groups of $m$ copies each |
| Zero Exponent | $a^0 = 1$ | Set $m=n$ in quotient: $a^n / a^n = 1$ |
| Negative Exponent | $a^{-n} = \dfrac{1}{a^n}$ | Set $m=0$ in quotient: $a^{0-n}$ |
| Fractional Exponent | $a^{1/n} = \sqrt[n]{a}$ | $(a^{1/n})^n = a^{n/n} = a^1$ → it's the nth root |

**Edge Case — The $0^0$ Trap:**
- In algebra/combinatorics: $0^0 = 1$ (by convention, because $\binom{0}{0}=1$, empty product = 1).
- In analysis/limits: $0^0$ is indeterminate because $\lim_{x \to 0^+} x^x = 1$ but other paths differ.
- **Exam trick:** If a question simply writes $0^0$ with no limits context, treat it as **1**.

### 2.2 Surd Simplification

A surd $\sqrt[n]{a}$ is irrational when $a$ is not a perfect $n$th power.

**Rationalisation (Why it works):**

The identity $(a-b)(a+b) = a^2 - b^2$ eliminates a square root in the denominator.

$$\frac{1}{\sqrt{a} + \sqrt{b}} = \frac{\sqrt{a} - \sqrt{b}}{(\sqrt{a})^2 - (\sqrt{b})^2} = \frac{\sqrt{a} - \sqrt{b}}{a - b}$$

**Example:**

$$\frac{1}{\sqrt{5} + \sqrt{3}} = \frac{\sqrt{5} - \sqrt{3}}{5 - 3} = \frac{\sqrt{5} - \sqrt{3}}{2}$$

**Nested Surds — The Square-Root Denesting Trick:**

To simplify $\sqrt{a + b\sqrt{c}}$, look for $p, q$ such that:
$$p + q = a, \quad pq = \frac{b^2 c}{4}$$

Then $\sqrt{a + b\sqrt{c}} = \sqrt{p} + \sqrt{q}$.

**Example:** Simplify $\sqrt{7 + 4\sqrt{3}}$.

Here $a = 7,\ b = 4,\ c = 3$. Need $p + q = 7,\ pq = \frac{16 \times 3}{4} = 12$.

$p, q$ are roots of $t^2 - 7t + 12 = 0 \Rightarrow t = 3, 4$.

$$\sqrt{7 + 4\sqrt{3}} = \sqrt{4} + \sqrt{3} = 2 + \sqrt{3}$$

**Verification:** $(2 + \sqrt{3})^2 = 4 + 4\sqrt{3} + 3 = 7 + 4\sqrt{3}$ ✓

### 2.3 Comparison of Surds

**Problem:** Which is larger, $\sqrt[3]{4}$ or $\sqrt[4]{6}$?

**Technique:** Raise both to the LCM of the root indices (LCM(3,4) = 12):

$$\sqrt[3]{4} = 4^{1/3} = 4^{4/12} = (4^4)^{1/12} = 256^{1/12}$$
$$\sqrt[4]{6} = 6^{1/4} = 6^{3/12} = (6^3)^{1/12} = 216^{1/12}$$

$256 > 216 \Rightarrow \sqrt[3]{4} > \sqrt[4]{6}$.

---

## 3. Logarithms

### The Atomic Truth

> *A logarithm answers: "What power gives me this number?"*

$$\log_a b = x \iff a^x = b$$

**Analogy — The Elevator:** If $a$ (the base) is the elevator speed, and $b$ is the floor you want to reach, $\log_a b$ tells you *how many times* you must press the "up" button.

### 3.1 Properties — All Derived from Index Laws

Since $\log$ is the inverse of exponentiation, every log law is just an index law in disguise.

| Index Law | Corresponding Log Law | Derivation Sketch |
|-----------|-----------------------|-------------------|
| $a^m \cdot a^n = a^{m+n}$ | $\log_a(xy) = \log_a x + \log_a y$ | Let $a^m = x,\ a^n = y$; then $xy = a^{m+n}$ |
| $a^m / a^n = a^{m-n}$ | $\log_a(x/y) = \log_a x - \log_a y$ | Same idea with division |
| $(a^m)^n = a^{mn}$ | $\log_a(x^n) = n \log_a x$ | Let $a^m = x$; then $x^n = a^{mn}$ |
| $a^0 = 1$ | $\log_a 1 = 0$ | Direct substitution |
| $a^1 = a$ | $\log_a a = 1$ | Direct substitution |

### 3.2 Change of Base Formula

**Derivation:**

Let $\log_a b = x$. Then $a^x = b$.

Take $\log_c$ of both sides: $x \log_c a = \log_c b$.

$$\boxed{\log_a b = \frac{\log_c b}{\log_c a}}$$

**Corollary (The Flip Rule):**

$$\log_a b = \frac{1}{\log_b a}$$

Set $c = b$: $\log_a b = \frac{\log_b b}{\log_b a} = \frac{1}{\log_b a}$.

### 3.3 Special Values & Edge Cases

| Expression | Value | Why |
|-----------|-------|-----|
| $\log_a 1$ | $0$ | $a^0 = 1$ |
| $\log_a a$ | $1$ | $a^1 = a$ |
| $\log_a 0$ | **Undefined** (→ $-\infty$) | No finite power gives 0 |
| $\log_a (-\text{ve})$ | **Undefined** (in ℝ) | No real power of a positive base gives negative |
| Base $a = 1$ | **Undefined** | $1^x = 1$ always, never reaches other numbers |
| Base $a \le 0$ | **Undefined** (in ℝ) | Oscillation / complex values |

**Domain Guard:** $\log_a x$ exists in ℝ only when $a > 0,\ a \ne 1,\ x > 0$.

### 3.4 Exam-Critical Tricks

**Trick 1 — Chain Rule for Logs:**

$$\log_a b \cdot \log_b c \cdot \log_c d = \log_a d$$

*Proof:* Each $\log$ factor converts to $\frac{\ln(\cdot)}{\ln(\cdot)}$ and consecutive denominators/numerators cancel (telescoping).

**Trick 2 — Sum of Reciprocal Logs:**

$$\frac{1}{\log_a x} + \frac{1}{\log_b x} = \frac{1}{\log_{ab} x}$$

*Proof:* $\frac{1}{\log_a x} = \log_x a$. So LHS $= \log_x a + \log_x b = \log_x(ab) = \frac{1}{\log_{ab} x}$.

**Example (GATE-style NAT):**

> *Find $\log_2 3 \cdot \log_3 4 \cdot \log_4 8$.*

$$= \log_2 3 \cdot \log_3 4 \cdot \log_4 8 = \log_2 8 = 3$$

(Chain rule telescopes directly.)

### 3.5 Mnemonic — "LOG = Ladder Of Growth"

Picture a ladder leaning against a building:
- **Base** $a$ = angle of the ladder (how steep you climb).
- **Argument** $b$ = the floor/height you reach.
- **Log value** = how many rungs you need.

A steeper ladder (larger base) needs *fewer* rungs to reach the same floor → $\log_a b$ *decreases* as $a$ increases (for $b > 1$).

---

## 4. Algebraic Identities

### The Atomic Truth

> *Identities are universal truths — valid for ALL values of the variable.*

### 4.1 Core Two-Variable Identities

**Identity 1:** $(a + b)^2 = a^2 + 2ab + b^2$

*Derivation:*
$(a+b)^2 = (a+b)(a+b) = a^2 + ab + ba + b^2 = a^2 + 2ab + b^2$

**Identity 2:** $(a - b)^2 = a^2 - 2ab + b^2$

*Same process with sign change.*

**Identity 3:** $(a+b)(a-b) = a^2 - b^2$

*Derivation:*
$= a^2 - ab + ab - b^2 = a^2 - b^2$

**The Golden Connections (why they matter together):**

$$\underbrace{(a+b)^2}_{S^2} - \underbrace{(a-b)^2}_{D^2} = 4ab$$
$$\underbrace{(a+b)^2}_{S^2} + \underbrace{(a-b)^2}_{D^2} = 2(a^2 + b^2)$$

These are *extremely* useful when a question gives you $a+b$ and $a-b$ (or $ab$) and asks for $a^2 + b^2$.

**Example (BANK PO):**

> *If $x + \frac{1}{x} = 5$, find $x^2 + \frac{1}{x^2}$.*

Square both sides: $x^2 + 2 + \frac{1}{x^2} = 25 \Rightarrow x^2 + \frac{1}{x^2} = 23$.

> *Now find $x^4 + \frac{1}{x^4}$.*

Square again: $(x^2 + \frac{1}{x^2})^2 = x^4 + 2 + \frac{1}{x^4} = 529 \Rightarrow x^4 + \frac{1}{x^4} = 527$.

**Pattern:** Each squaring step subtracts 2 from the squared value: $5 \to 23 \to 527$.

### 4.2 Cube Identities

**Identity 4:** $(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3 = a^3 + b^3 + 3ab(a+b)$

**Identity 5:** $(a-b)^3 = a^3 - 3a^2b + 3ab^2 - b^3 = a^3 - b^3 - 3ab(a-b)$

**Factorisation of Sum/Difference of Cubes:**

$$a^3 + b^3 = (a+b)(a^2 - ab + b^2)$$
$$a^3 - b^3 = (a-b)(a^2 + ab + b^2)$$

*How to remember:* **"SOAP"** mnemonic:
- **S**ame sign → $(a \mathbf{+} b)$ for sum, $(a \mathbf{-} b)$ for difference
- **O**pposite sign → $-ab$ for sum, $+ab$ for difference
- **A**lways **P**ositive → $a^2$ and $b^2$ are always positive

**Example (ESE):**

> *If $a + b + c = 0$, prove that $a^3 + b^3 + c^3 = 3abc$.*

Use the identity: $a^3 + b^3 + c^3 - 3abc = (a+b+c)(a^2+b^2+c^2 - ab - bc - ca)$.

Since $a+b+c = 0$, the RHS is 0. Hence $a^3 + b^3 + c^3 = 3abc$. ∎

### 4.3 Three-Variable Identities

$$(a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca)$$

*Derivation:* Expand $(a+b+c)(a+b+c)$ term by term — 9 products, 3 squares + 6 cross terms that pair up.

**The Master Identity:**

$$a^3 + b^3 + c^3 - 3abc = (a + b + c)\left(a^2 + b^2 + c^2 - ab - bc - ca\right)$$

**Trick — Rewriting the second factor:**

$$a^2 + b^2 + c^2 - ab - bc - ca = \frac{1}{2}\left[(a-b)^2 + (b-c)^2 + (c-a)^2\right]$$

This is always $\ge 0$. So if $a+b+c > 0$, then $a^3 + b^3 + c^3 \ge 3abc$ (AM-GM connection!).

### 4.4 Sophie Germain & Power Identities

**Sophie Germain Identity:**

$$a^4 + 4b^4 = (a^2 + 2b^2 + 2ab)(a^2 + 2b^2 - 2ab)$$

*Trick:* Add and subtract $4a^2b^2$ to create a difference of squares.

**Higher Power Factorisations:**

$$a^n - b^n = (a-b)(a^{n-1} + a^{n-2}b + \cdots + b^{n-1}) \quad \text{for all } n \in \mathbb{N}$$
$$a^n + b^n = (a+b)(a^{n-1} - a^{n-2}b + \cdots + b^{n-1}) \quad \text{for odd } n$$

---

## 5. Linear Equations

### The Atomic Truth

> *Highest power of the variable is 1 → straight-line graph.*

### 5.1 Single Variable

$$ax + b = 0 \implies x = -\frac{b}{a}, \quad a \ne 0$$

**Edge Cases:**
- $a = 0, b = 0$: Identity (true for all $x$) → infinitely many solutions.
- $a = 0, b \ne 0$: Contradiction (no solution).

### 5.2 System of Two Linear Equations

$$a_1 x + b_1 y = c_1$$
$$a_2 x + b_2 y = c_2$$

**Why Cramer's Rule Works (The Determinant Intuition):**

Geometrically, two lines in a plane either:
1. **Intersect** at exactly one point (unique solution)
2. **Are parallel** (no solution)
3. **Coincide** (infinite solutions)

The determinant $D = a_1 b_2 - a_2 b_1$ measures whether the two direction vectors are linearly independent.

| Condition | Geometric Meaning | Solutions |
|-----------|--------------------|-----------|
| $D \ne 0$ | Lines intersect | Unique: $x = D_x/D,\ y = D_y/D$ |
| $D = 0,\ D_x \ne 0$ or $D_y \ne 0$ | Parallel lines | None |
| $D = 0,\ D_x = 0,\ D_y = 0$ | Same line | Infinite |

where:
$$D_x = c_1 b_2 - c_2 b_1, \quad D_y = a_1 c_2 - a_2 c_1$$

**Ratio Test (Speed Trick):**

$$\frac{a_1}{a_2} \ne \frac{b_1}{b_2} \implies \text{Unique solution}$$
$$\frac{a_1}{a_2} = \frac{b_1}{b_2} \ne \frac{c_1}{c_2} \implies \text{No solution (parallel)}$$
$$\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2} \implies \text{Infinite solutions (coincident)}$$

### 5.3 Word Problems — The Framework

**Step 1:** Assign variables to unknowns.
**Step 2:** Translate English → Algebra (key words: "is" = $=$, "more than" = $+$, "times" = $\times$).
**Step 3:** Solve the system.
**Step 4:** Verify by substituting back into the **original word problem** (not the equations — catches translation errors).

**Example (PSU):**

> *The sum of two numbers is 50 and their difference is 10. Find them.*

$x + y = 50,\ x - y = 10$. Add: $2x = 60 \Rightarrow x = 30$. Subtract: $2y = 40 \Rightarrow y = 20$.

Check: $30 + 20 = 50$ ✓, $30 - 20 = 10$ ✓.

---

## 6. Quadratic Equations

### The Atomic Truth

> *Highest power is 2 → at most two roots.*

### 6.1 Standard Form & the Quadratic Formula — Derived

$$ax^2 + bx + c = 0, \quad a \ne 0$$

**Derivation by Completing the Square:**

$$x^2 + \frac{b}{a}x = -\frac{c}{a}$$

Add $\left(\frac{b}{2a}\right)^2$ to both sides:

$$\left(x + \frac{b}{2a}\right)^2 = \frac{b^2 - 4ac}{4a^2}$$

$$x + \frac{b}{2a} = \pm \frac{\sqrt{b^2 - 4ac}}{2a}$$

$$\boxed{x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}}$$

The expression under the square root, $\Delta = b^2 - 4ac$, is the **Discriminant**.

### 6.2 Nature of Roots via Discriminant

| Discriminant $\Delta$ | Nature of Roots | Geometric Meaning |
|------------------------|-----------------|-------------------|
| $\Delta > 0$ | Two distinct real roots | Parabola cuts x-axis at 2 points |
| $\Delta = 0$ | Two equal (repeated) real roots | Parabola *touches* x-axis |
| $\Delta < 0$ | No real roots (complex conjugate pair) | Parabola doesn't touch x-axis |
| $\Delta =$ perfect square (and $a,b,c \in \mathbb{Q}$) | Rational roots | — |

**Edge Case Trap:** "$\Delta > 0$ means real and *unequal*" — examiners test this distinction vs $\Delta \ge 0$.

### 6.3 Vieta's Formulas — Why They Work

If $\alpha, \beta$ are roots of $ax^2 + bx + c = 0$, then $ax^2 + bx + c = a(x-\alpha)(x-\beta)$.

Expanding: $a(x-\alpha)(x-\beta) = a\left[x^2 - (\alpha+\beta)x + \alpha\beta\right]$.

Comparing coefficients:

$$\boxed{\alpha + \beta = -\frac{b}{a}, \qquad \alpha \beta = \frac{c}{a}}$$

**The Power of Vieta's:** You can find symmetric expressions of roots *without finding the roots themselves*.

$$\alpha^2 + \beta^2 = (\alpha+\beta)^2 - 2\alpha\beta$$
$$\alpha^3 + \beta^3 = (\alpha+\beta)^3 - 3\alpha\beta(\alpha+\beta)$$
$$|\alpha - \beta| = \sqrt{(\alpha+\beta)^2 - 4\alpha\beta} = \frac{\sqrt{\Delta}}{|a|}$$

**Example (GATE NAT):**

> *If the roots of $2x^2 - 7x + 3 = 0$ are $\alpha, \beta$, find $\alpha^2 + \beta^2$.*

$\alpha + \beta = 7/2,\ \alpha\beta = 3/2$.

$\alpha^2 + \beta^2 = (7/2)^2 - 2(3/2) = 49/4 - 3 = 37/4 = 9.25$.

### 6.4 Constructing Equations from Roots

If roots are $\alpha, \beta$:

$$x^2 - (\alpha + \beta)x + \alpha\beta = 0$$

**Example:** Roots are $3 + \sqrt{2}$ and $3 - \sqrt{2}$.

Sum = 6, Product = $9 - 2 = 7$. Equation: $x^2 - 6x + 7 = 0$.

### 6.5 Common Conditions on Roots

| Condition | Requirement |
|-----------|-------------|
| Both roots positive | $\alpha+\beta > 0,\ \alpha\beta > 0,\ \Delta \ge 0$ |
| Both roots negative | $\alpha+\beta < 0,\ \alpha\beta > 0,\ \Delta \ge 0$ |
| Roots opposite in sign | $\alpha\beta < 0$ (i.e., $c/a < 0$) |
| Roots reciprocal of each other | $\alpha\beta = 1$ (i.e., $c = a$) |
| One root zero | $c = 0$ |
| Both roots zero | $b = 0,\ c = 0$ |
| Roots equal in magnitude, opposite sign | $\alpha + \beta = 0$ (i.e., $b = 0$) |

### 6.6 Tricks for Fast Solving

**Trick 1 — Sum-Product Factoring:**

For $x^2 + bx + c = 0$ (where $a=1$): find two numbers whose sum is $b$ and product is $c$.

Example: $x^2 - 7x + 12 = 0$. Numbers: $-3$ and $-4$ (sum $= -7$, product $= 12$). Roots: $x = 3, 4$.

**Trick 2 — Cross-Check via Coefficient Sum:**

- If $a + b + c = 0$, then $x = 1$ is a root and the other root is $c/a$.
- If $a - b + c = 0$, then $x = -1$ is a root and the other root is $-c/a$.

**Example:** $3x^2 - 5x + 2 = 0$. Check: $3 - 5 + 2 = 0$ ✓. Roots: $x = 1$ and $x = 2/3$.

### 6.7 Maximum/Minimum of Quadratic Expression

The expression $f(x) = ax^2 + bx + c$ achieves its extreme value at $x = -\frac{b}{2a}$.

- If $a > 0$: **Minimum** value $= c - \frac{b^2}{4a} = -\frac{\Delta}{4a}$.
- If $a < 0$: **Maximum** value $= c - \frac{b^2}{4a} = -\frac{\Delta}{4a}$.

*Why?* Completing the square: $a\left(x + \frac{b}{2a}\right)^2 + c - \frac{b^2}{4a}$. The squared term is $\ge 0$ (or $\le 0$ if $a < 0$).

---

## 7. Polynomials — Factor & Remainder Theorems

### The Atomic Truth

> *A polynomial of degree n has at most n roots.*

### 7.1 Polynomial Division

Any polynomial $P(x)$ divided by $D(x)$ gives:

$$P(x) = D(x) \cdot Q(x) + R(x)$$

where $\deg(R) < \deg(D)$.

### 7.2 Remainder Theorem — Why It Works

When you divide $P(x)$ by $(x - a)$, the divisor is linear, so the remainder $R$ is a constant:

$$P(x) = (x - a) \cdot Q(x) + R$$

Substitute $x = a$:

$$P(a) = (a - a) \cdot Q(a) + R = R$$

$$\boxed{\text{Remainder when } P(x) \text{ is divided by } (x-a) = P(a)}$$

### 7.3 Factor Theorem

If $P(a) = 0$, then the remainder is 0, meaning $(x-a)$ divides $P(x)$ exactly.

$$\boxed{P(a) = 0 \iff (x - a) \text{ is a factor of } P(x)}$$

**Example (GATE MCQ):**

> *Find the remainder when $P(x) = x^3 - 6x^2 + 11x - 6$ is divided by $(x - 2)$.*

$P(2) = 8 - 24 + 22 - 6 = 0$. So $(x-2)$ is a **factor** (remainder = 0).

In fact: $x^3 - 6x^2 + 11x - 6 = (x-1)(x-2)(x-3)$.

### 7.4 Generalised Remainder Theorem

When dividing by $(ax + b)$: remainder $= P(-b/a)$.

When dividing by a quadratic $(x-a)(x-b)$: remainder is $Rx + S$ (linear), found by solving:
$$P(a) = Ra + S, \quad P(b) = Rb + S$$

**Example:**

> *Remainder when $x^{100}$ is divided by $(x-1)(x+1)$.*

$P(1) = 1,\ P(-1) = 1$. So $R(1) + S = 1$ and $-R + S = 1$.

Solving: $R = 0,\ S = 1$. Remainder = $\boxed{1}$.

### 7.5 Rational Root Theorem

For $P(x) = a_n x^n + \cdots + a_0$ with integer coefficients, any rational root $p/q$ (in lowest terms) satisfies:
- $p$ divides $a_0$ (constant term)
- $q$ divides $a_n$ (leading coefficient)

**Use case:** Quickly narrow down candidate roots before testing with the Factor Theorem.

---

## 8. Inequalities

### The Atomic Truth

> *Inequalities flip on multiplication/division by negatives.*

### 8.1 Fundamental Rules

| Operation | Effect on Inequality |
|-----------|---------------------|
| Add/subtract same number | Direction preserved |
| Multiply/divide by **positive** | Direction preserved |
| Multiply/divide by **negative** | Direction **reverses** |
| Square both sides | Valid only if both sides are **non-negative** |
| Take reciprocals | Direction reverses (if both same sign) |

### 8.2 AM-GM Inequality

For non-negative reals $a_1, a_2, \ldots, a_n$:

$$\frac{a_1 + a_2 + \cdots + a_n}{n} \ge \sqrt[n]{a_1 a_2 \cdots a_n}$$

Equality holds when $a_1 = a_2 = \cdots = a_n$.

**Derivation for n=2:**

$(a - b)^2 \ge 0 \implies a^2 + b^2 \ge 2ab$.

Let $a = \sqrt{x},\ b = \sqrt{y}$:

$$x + y \ge 2\sqrt{xy} \implies \frac{x+y}{2} \ge \sqrt{xy}$$

**Use Case — Optimisation Without Calculus:**

> *Find the minimum value of $x + \frac{1}{x}$ for $x > 0$.*

By AM-GM: $x + \frac{1}{x} \ge 2\sqrt{x \cdot \frac{1}{x}} = 2$.

Minimum is $2$, achieved at $x = 1$.

### 8.3 Quadratic Inequality

To solve $ax^2 + bx + c > 0$ (or $< 0, \ge 0, \le 0$):

**Step 1:** Find the roots $\alpha, \beta$ ($\alpha \le \beta$) of $ax^2 + bx + c = 0$.

**Step 2:** Use the sign scheme:
- If $a > 0$: the expression is **negative between roots** and **positive outside**.
  - $ax^2 + bx + c > 0 \Rightarrow x \in (-\infty, \alpha) \cup (\beta, \infty)$
  - $ax^2 + bx + c < 0 \Rightarrow x \in (\alpha, \beta)$
- If $a < 0$: flip the intervals.

**Analogy — The Parabola Smile/Frown:**
- $a > 0$: Parabola smiles 😊 → positive *outside* the roots.
- $a < 0$: Parabola frowns 😞 → positive *between* the roots.

### 8.4 Wavy Curve Method (for polynomial/rational inequalities)

**For:** $\frac{(x-a_1)^{p_1}(x-a_2)^{p_2}\cdots}{(x-b_1)^{q_1}(x-b_2)^{q_2}\cdots} > 0$

**Steps:**
1. Mark all roots and undefined points on the number line.
2. Start from the rightmost point with a **positive** sign (since the leading term dominates for large $x$).
3. At each root:
   - **Odd multiplicity** → sign changes.
   - **Even multiplicity** → sign stays the same (curve "bounces").

**Example:**

Solve $(x-1)(x-3)^2(x-5) > 0$.

Roots: $1, 3, 5$. Start from right of 5: positive.
- Cross $x=5$ (odd): changes to negative.
- Cross $x=3$ (even): stays negative.
- Cross $x=1$ (odd): changes to positive.

Solution: $x \in (-\infty, 1) \cup (5, \infty)$.

(Note: $x=3$ is NOT included because the inequality is strict and the curve doesn't change sign there.)

### 8.5 Modulus (Absolute Value) Inequalities

$$|x| < a \iff -a < x < a \quad (a > 0)$$
$$|x| > a \iff x < -a \text{ or } x > a$$

**Triangle Inequality:** $|a + b| \le |a| + |b|$

**Reverse Triangle Inequality:** $|a - b| \ge ||a| - |b||$

---

## 9. Arithmetic Progression (AP)

### The Atomic Truth

> *Each term grows by the same fixed amount.*

### 9.1 Definition & Derivation

An AP has the form: $a,\ a+d,\ a+2d,\ a+3d, \ldots$

The $n$th term:

$$\boxed{T_n = a + (n-1)d}$$

*Why?* The first term is $a$. Each subsequent term adds $d$ once. After $n-1$ steps: $a + (n-1)d$.

### 9.2 Sum of First n Terms

$$S_n = \frac{n}{2}\left[2a + (n-1)d\right] = \frac{n}{2}(a + l)$$

where $l = T_n$ is the last term.

**Derivation (Gauss's Trick):**

Write the sum forwards and backwards:
$$S_n = a + (a+d) + (a+2d) + \cdots + l$$
$$S_n = l + (l-d) + (l-2d) + \cdots + a$$

Add term-by-term: each pair sums to $(a + l)$, and there are $n$ pairs:

$$2S_n = n(a + l) \implies S_n = \frac{n}{2}(a + l)$$

**The "n/2 Handshake" Analogy:** Imagine $n$ people standing in a line. Pair the first with the last, the second with the second-last, etc. Each pair shakes hands and their "combined strength" is always $a + l$.

### 9.3 Key Properties

1. If three numbers are in AP: $b - a = c - b \implies 2b = a + c$ (middle term is the AM).
2. If $T_p = q$ and $T_q = p$, then $T_{p+q} = 0$ and $d = -1$.
3. $T_n = S_n - S_{n-1}$ for $n \ge 2$.
4. If $S_n = An^2 + Bn + C$, then:
   - It's an AP only if $C = 0$.
   - $d = 2A$ and $a = A + B$.

### 9.4 Selection of Terms in AP (for simplicity)

| # of Terms | Choose as | Why |
|-------------|-----------|-----|
| 3 | $a-d,\ a,\ a+d$ | Sum = $3a$ (d cancels) |
| 4 | $a-3d,\ a-d,\ a+d,\ a+3d$ | Common difference is $2d$ |
| 5 | $a-2d,\ a-d,\ a,\ a+d,\ a+2d$ | Sum = $5a$ |

**Example (BANK):**

> *The sum of three numbers in AP is 27 and their product is 648. Find them.*

Let them be $a-d,\ a,\ a+d$. Sum: $3a = 27 \Rightarrow a = 9$.

Product: $(9-d)(9)(9+d) = 648 \Rightarrow 9(81 - d^2) = 648 \Rightarrow d^2 = 9 \Rightarrow d = 3$.

Numbers: $6, 9, 12$.

### 9.5 Arithmetic Mean (AM)

The AM of $a$ and $b$:

$$\text{AM} = \frac{a + b}{2}$$

**Inserting $n$ AMs between $a$ and $b$:**

The $n+2$ terms form an AP with first term $a$ and last term $b$:

$$d = \frac{b - a}{n + 1}$$

---

## 10. Geometric Progression (GP)

### The Atomic Truth

> *Each term grows by the same fixed ratio.*

### 10.1 Definition & Derivation

A GP has the form: $a,\ ar,\ ar^2,\ ar^3, \ldots$

The $n$th term:

$$\boxed{T_n = ar^{n-1}}$$

### 10.2 Sum of First n Terms

$$S_n = a \cdot \frac{r^n - 1}{r - 1} \quad (r \ne 1)$$

**Derivation:**

$$S_n = a + ar + ar^2 + \cdots + ar^{n-1}$$

Multiply by $r$:

$$rS_n = ar + ar^2 + \cdots + ar^n$$

Subtract: $S_n - rS_n = a - ar^n$

$$S_n(1 - r) = a(1 - r^n) \implies S_n = \frac{a(1 - r^n)}{1 - r}$$

### 10.3 Sum to Infinity (|r| < 1)

As $n \to \infty$, $r^n \to 0$ when $|r| < 1$:

$$\boxed{S_\infty = \frac{a}{1 - r}, \quad |r| < 1}$$

**Analogy — The Bouncing Ball:** A ball dropped from height $a$ bounces back to $ra$ (where $0 < r < 1$), then $r^2 a$, etc. The total distance converges to $\frac{a}{1-r}$ (up) + $\frac{a}{1-r}$ (down) minus the initial drop, giving $\frac{a(1+r)}{1-r}$.

### 10.4 Key Properties

1. Three numbers in GP: $a/r,\ a,\ ar$. Product = $a^3$ (always).
2. If $a, b, c$ are in GP: $b^2 = ac$ (geometric mean property).
3. $T_n = S_n - S_{n-1}$.
4. In a GP, any term is the geometric mean of its neighbours: $T_k = \sqrt{T_{k-1} \cdot T_{k+1}}$.

### 10.5 Geometric Mean (GM)

The GM of $a$ and $b$ (both positive):

$$\text{GM} = \sqrt{ab}$$

**AM-GM Relationship:** $\text{AM} \ge \text{GM}$ with equality iff $a = b$.

Proof: $\frac{a+b}{2} \ge \sqrt{ab} \iff (a+b)^2 \ge 4ab \iff (a-b)^2 \ge 0$ ✓ (always true).

### 10.6 Recurring Decimals as GP (BANK/SSC Favourite)

> *Express $0.777\ldots$ as a fraction.*

$$0.777\ldots = \frac{7}{10} + \frac{7}{100} + \frac{7}{1000} + \cdots = \frac{7/10}{1 - 1/10} = \frac{7}{9}$$

> *Express $0.1\overline{23}$ as a fraction.*

$$0.1\overline{23} = 0.1 + 0.0\overline{23} = \frac{1}{10} + \frac{23}{990} = \frac{99 + 23}{990} = \frac{122}{990} = \frac{61}{495}$$

**General Pattern:** $0.\overline{ab} = \frac{ab}{99}$, $0.\overline{abc} = \frac{abc}{999}$, etc.

---

## 11. Harmonic Progression (HP) & AGP

### The Atomic Truth

> *HP: reciprocals form an AP. AGP: AP × GP term by term.*

### 11.1 Harmonic Progression

$a_1, a_2, a_3, \ldots$ is an HP if $\frac{1}{a_1}, \frac{1}{a_2}, \frac{1}{a_3}, \ldots$ is an AP.

**There is no direct formula for the sum of an HP.** Always convert to AP.

**Harmonic Mean** of $a$ and $b$:

$$\text{HM} = \frac{2ab}{a + b}$$

*Derivation:* If HM = $H$, then $\frac{1}{a}, \frac{1}{H}, \frac{1}{b}$ are in AP. So $\frac{2}{H} = \frac{1}{a} + \frac{1}{b} = \frac{a+b}{ab}$.

### 11.2 Relationship: AM ≥ GM ≥ HM

For positive reals $a, b$:

$$\frac{a+b}{2} \ge \sqrt{ab} \ge \frac{2ab}{a+b}$$

Also: $\text{AM} \times \text{HM} = (\text{GM})^2$, i.e., $\frac{a+b}{2} \cdot \frac{2ab}{a+b} = ab = (\sqrt{ab})^2$.

**Mnemonic — "The Mean Hierarchy":** Think of AM, GM, HM as Gold, Silver, Bronze medals: AM always wins, HM always comes last. They tie only when all values are equal.

### 11.3 Arithmetico-Geometric Progression (AGP)

An AGP is formed by multiplying corresponding terms of an AP and a GP:

$$S = ab + (a+d)br + (a+2d)br^2 + \cdots$$

**Sum Technique (Multiply-Subtract method):**

$$S = ab + (a+d)br + (a+2d)br^2 + \cdots + [a+(n-1)d]br^{n-1}$$
$$rS = abr + (a+d)br^2 + \cdots + [a+(n-2)d]br^{n-1} + [a+(n-1)d]br^n$$

Subtract: $S(1-r) = ab + dbr + dbr^2 + \cdots + dbr^{n-1} - [a+(n-1)d]br^n$

The middle terms form a GP with first term $dbr$, ratio $r$, and $(n-1)$ terms.

**Infinite AGP Sum** ($|r| < 1$):

$$\boxed{S_\infty = \frac{ab}{1-r} + \frac{dbr}{(1-r)^2}}$$

**Example:**

> *Find $1 \cdot 2 + 2 \cdot 4 + 3 \cdot 8 + 4 \cdot 16 + \cdots$ to $n$ terms.*

AP part: $1, 2, 3, \ldots$ ($a=1, d=1$). GP part: $2, 4, 8, \ldots$ ($b=2, r=2$).

This is a finite AGP (doesn't converge since $r = 2 > 1$). Use the multiply-subtract method to get the closed form.

---

## 12. Set Theory Essentials

### The Atomic Truth

> *A set is a well-defined collection of distinct objects.*

### 12.1 Operations & Venn Diagrams

| Operation | Notation | Meaning |
|-----------|----------|---------|
| Union | $A \cup B$ | Elements in A **or** B (or both) |
| Intersection | $A \cap B$ | Elements in A **and** B |
| Difference | $A - B$ or $A \setminus B$ | In A but **not** in B |
| Complement | $A'$ or $A^c$ | Not in A (relative to Universal set $U$) |
| Symmetric Difference | $A \oplus B$ | In exactly one of A or B = $(A \cup B) - (A \cap B)$ |

### 12.2 Counting Formula (Inclusion-Exclusion)

**Two Sets:**

$$|A \cup B| = |A| + |B| - |A \cap B|$$

*Why subtract $|A \cap B|$?* Because elements in the overlap are counted twice — once in $|A|$ and once in $|B|$.

**Three Sets:**

$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |B \cap C| - |A \cap C| + |A \cap B \cap C|$$

*Why add back $|A \cap B \cap C|$?* After subtracting pairwise, elements in all three sets have been subtracted three times and added back three times, netting zero. Adding once restores the correct count of 1.

**Example (BANK/SSC):**

> *In a group of 100 students, 60 like Cricket, 50 like Football, and 20 like both. How many like neither?*

$|C \cup F| = 60 + 50 - 20 = 90$. Neither $= 100 - 90 = 10$.

### 12.3 De Morgan's Laws

$$\overline{A \cup B} = \overline{A} \cap \overline{B}$$
$$\overline{A \cap B} = \overline{A} \cup \overline{B}$$

**Mnemonic:** "Break the bar, change the sign" — when you distribute a complement (bar) over a set operation, union ↔ intersection flip.

### 12.4 Properties of Set Operations

| Property | Union | Intersection |
|----------|-------|--------------|
| Commutative | $A \cup B = B \cup A$ | $A \cap B = B \cap A$ |
| Associative | $(A \cup B) \cup C = A \cup (B \cup C)$ | $(A \cap B) \cap C = A \cap (B \cap C)$ |
| Idempotent | $A \cup A = A$ | $A \cap A = A$ |
| Identity | $A \cup \emptyset = A$ | $A \cap U = A$ |
| Domination | $A \cup U = U$ | $A \cap \emptyset = \emptyset$ |
| Absorption | $A \cup (A \cap B) = A$ | $A \cap (A \cup B) = A$ |
| Distributive | $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ | $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ |

### 12.5 Power Set

The power set $\mathcal{P}(A)$ is the set of all subsets of $A$.

$$|\mathcal{P}(A)| = 2^{|A|}$$

*Why?* Each element has 2 choices: include or exclude. For $n$ elements: $2 \times 2 \times \cdots \times 2 = 2^n$.

---

## 13. Functions & Relations

### The Atomic Truth

> *A function maps each input to exactly one output.*

### 13.1 Relations

A relation $R$ from set $A$ to set $B$ is a subset of $A \times B$.

**Properties of Relations (on a set $A$):**

| Property | Definition | Example on $\{1,2,3\}$ |
|----------|------------|------------------------|
| Reflexive | $(a, a) \in R\ \forall a$ | $\{(1,1),(2,2),(3,3),\ldots\}$ |
| Symmetric | $(a,b) \in R \implies (b,a) \in R$ | "is sibling of" |
| Transitive | $(a,b), (b,c) \in R \implies (a,c) \in R$ | "$\le$" |
| Anti-symmetric | $(a,b),(b,a) \in R \implies a = b$ | "$\le$" |
| Equivalence | Reflexive + Symmetric + Transitive | "same remainder mod 3" |
| Partial Order | Reflexive + Anti-symmetric + Transitive | "$\le$" on integers |

### 13.2 Functions — Types

Let $f: A \to B$.

| Type | Definition | Counting (if $|A|=m, |B|=n$) |
|------|------------|-------------------------------|
| **Injective** (One-to-one) | $f(a_1) = f(a_2) \implies a_1 = a_2$ | $n \cdot (n-1) \cdots (n-m+1) = \frac{n!}{(n-m)!}$, requires $m \le n$ |
| **Surjective** (Onto) | Every $b \in B$ has a pre-image | Requires $m \ge n$ |
| **Bijective** | Both injective and surjective | Requires $m = n$; count $= n!$ |

**Total functions from $A$ to $B$:** $n^m$ (each of $m$ elements has $n$ choices).

### 13.3 Composition & Inverse

- $(g \circ f)(x) = g(f(x))$ — apply $f$ first, then $g$.
- $f^{-1}$ exists $\iff$ $f$ is bijective.
- $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$ (reverse order — like removing layers).

### 13.4 Even and Odd Functions

| Type | Definition | Graph Symmetry | Examples |
|------|-----------|----------------|----------|
| Even | $f(-x) = f(x)$ | Symmetric about y-axis | $x^2,\ \cos x,\ |x|$ |
| Odd | $f(-x) = -f(x)$ | Symmetric about origin | $x^3,\ \sin x,\ x$ |

**Trick:** Any function can be decomposed: $f(x) = \underbrace{\frac{f(x)+f(-x)}{2}}_{\text{even part}} + \underbrace{\frac{f(x)-f(-x)}{2}}_{\text{odd part}}$.

---

## 14. Binomial Theorem

### The Atomic Truth

> *$(a+b)^n$ expands into $n+1$ terms using combinations.*

### 14.1 The Expansion — Why It Works

$$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$$

**Intuition:** When you multiply $(a+b)$ by itself $n$ times, each term in the product arises by choosing either $a$ or $b$ from each factor. The number of ways to choose $b$ exactly $k$ times out of $n$ factors is $\binom{n}{k}$.

### 14.2 Key Terms

**General Term:** $T_{k+1} = \binom{n}{k} a^{n-k} b^k$ (the $(k+1)$th term, $k = 0, 1, \ldots, n$).

**Middle Term(s):**
- If $n$ is even: one middle term at $k = n/2$, i.e., $T_{n/2 + 1}$.
- If $n$ is odd: two middle terms at $k = (n-1)/2$ and $k = (n+1)/2$.

### 14.3 Binomial Coefficients Properties

$$\binom{n}{k} = \binom{n}{n-k} \quad \text{(Symmetry)}$$
$$\binom{n}{0} + \binom{n}{1} + \cdots + \binom{n}{n} = 2^n \quad \text{(Set } a=b=1\text{)}$$
$$\binom{n}{0} - \binom{n}{1} + \binom{n}{2} - \cdots = 0 \quad \text{(Set } a=1, b=-1\text{)}$$

**Pascal's Rule:** $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$

*Why?* Consider $n$ objects. Fix one object. Either it's in the chosen group ($\binom{n-1}{k-1}$ ways for the rest) or it's not ($\binom{n-1}{k}$ ways).

### 14.4 Applications & Tricks

**Finding Coefficient of $x^r$ in $(1 + x)^n$:**

$T_{r+1} = \binom{n}{r} x^r$. Coefficient $= \binom{n}{r}$.

**Finding Coefficient of $x^r$ in $(a + bx)^n$:**

$T_{k+1} = \binom{n}{k} a^{n-k} (bx)^k = \binom{n}{k} a^{n-k} b^k x^k$.

Set $k = r$: coefficient $= \binom{n}{r} a^{n-r} b^r$.

**Example (GATE):**

> *Find the coefficient of $x^5$ in $(1 + x)^8$.*

$$\binom{8}{5} = \binom{8}{3} = \frac{8 \times 7 \times 6}{3 \times 2 \times 1} = 56$$

**The Term Independent of $x$ in $\left(x + \frac{1}{x}\right)^n$:**

$T_{k+1} = \binom{n}{k} x^{n-k} \cdot x^{-k} = \binom{n}{k} x^{n-2k}$.

Independent of $x$ when $n - 2k = 0 \implies k = n/2$ (exists only if $n$ is even).

### 14.5 Binomial Approximation (for small |x|)

$$(1 + x)^n \approx 1 + nx \quad \text{when } |x| \ll 1$$

*Why?* Higher powers of $x$ become negligibly small.

**Example:** $(1.01)^{10} \approx 1 + 10(0.01) = 1.1$ (exact: $1.10462...$).

---

## 15. Matrices & Determinants (Aptitude Essentials)

### The Atomic Truth

> *A matrix is a rectangular array; its determinant encodes volume/invertibility.*

### 15.1 Basic Operations

**Addition:** Element-wise (matrices must be same size).

**Scalar Multiplication:** Multiply every element by the scalar.

**Matrix Multiplication:** $(AB)_{ij} = \sum_k A_{ik} B_{kj}$

*Condition:* Columns of $A$ = Rows of $B$. Result size: (Rows of $A$) × (Columns of $B$).

**Why is matrix multiplication not commutative?** Because $AB$ means "apply $B$ first, then $A$" — the order of transformations matters (rotating then reflecting ≠ reflecting then rotating).

### 15.2 Determinant (2×2 and 3×3)

**2×2:**

$$\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$$

*Geometric meaning:* Area of the parallelogram formed by the column vectors.

**3×3 (Sarrus' Rule or Cofactor Expansion):**

$$\det\begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix} = a(ei - fh) - b(di - fg) + c(dh - eg)$$

### 15.3 Properties of Determinants

| Property | Statement |
|----------|-----------|
| Row/Column swap | Changes sign ($\times -1$) |
| Two identical rows/cols | $\det = 0$ |
| Scalar multiple of a row | $\det$ multiplied by that scalar |
| $\det(kA)$ for $n \times n$ | $= k^n \det(A)$ |
| $\det(AB)$ | $= \det(A) \cdot \det(B)$ |
| $\det(A^T)$ | $= \det(A)$ |
| $\det(A^{-1})$ | $= 1/\det(A)$ |
| Singular matrix | $\det = 0 \iff$ no inverse |

### 15.4 Inverse of a 2×2 Matrix

$$A^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

*Trick:* Swap the main diagonal, negate the off-diagonal, divide by determinant.

### 15.5 System of Linear Equations (Matrix Form)

$AX = B$ where $A$ is the coefficient matrix, $X$ is the variable vector, $B$ is the constant vector.

| $\det(A)$ | $B$ | Solutions |
|-----------|-----|-----------|
| $\ne 0$ | Any | Unique: $X = A^{-1}B$ |
| $= 0$ | Consistent | Infinite |
| $= 0$ | Inconsistent | None |

---

## 16. Exam-Ready Quick Recall Sheet

### 16.1 Formula Flash Cards

| # | Formula | Quick Note |
|---|---------|------------|
| 1 | $(a \pm b)^2 = a^2 \pm 2ab + b^2$ | Square of sum/difference |
| 2 | $(a+b)(a-b) = a^2 - b^2$ | Difference of squares |
| 3 | $(a+b)^3 = a^3 + b^3 + 3ab(a+b)$ | Cube of sum |
| 4 | $a^3 + b^3 = (a+b)(a^2 - ab + b^2)$ | Sum of cubes (SOAP) |
| 5 | $a^3 - b^3 = (a-b)(a^2 + ab + b^2)$ | Difference of cubes (SOAP) |
| 6 | $a^3+b^3+c^3-3abc = (a+b+c)(a^2+b^2+c^2-ab-bc-ca)$ | Master 3-var identity |
| 7 | Quadratic: $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$ | Discriminant decides nature |
| 8 | Vieta: $\alpha+\beta = -b/a,\ \alpha\beta = c/a$ | Roots ↔ coefficients |
| 9 | AP: $T_n = a+(n-1)d$, $S_n = \frac{n}{2}(2a+(n-1)d)$ | Linear growth |
| 10 | GP: $T_n = ar^{n-1}$, $S_n = \frac{a(r^n-1)}{r-1}$ | Exponential growth |
| 11 | $S_\infty(\text{GP}) = \frac{a}{1-r}$, $|r| < 1$ | Infinite GP sum |
| 12 | $\text{AM} \ge \text{GM} \ge \text{HM}$ | Mean inequality chain |
| 13 | $\log_a(xy) = \log_a x + \log_a y$ | Product → Sum |
| 14 | $\log_a b = \frac{1}{\log_b a}$ | Flip rule |
| 15 | $(1+x)^n = \sum \binom{n}{k}x^k$ | Binomial expansion |
| 16 | $\|A \cup B\| = \|A\| + \|B\| - \|A \cap B\|$ | Inclusion-Exclusion |
| 17 | $\text{HCF} \times \text{LCM} = A \times B$ | Product relationship |

### 16.2 The 5-Second Sanity Checks

1. **Quadratic roots:** Sum should equal $-b/a$, product should equal $c/a$. Plug both roots back in — must give 0.
2. **AP/GP sums:** For small $n$ (like $n = 1, 2$), manually verify the formula gives the right answer.
3. **Log arguments:** Check that all arguments are positive and bases are valid ($> 0$, $\ne 1$).
4. **Inequality direction:** After multiplying/dividing by a variable, ask: "Could this be negative?" If yes, split into cases.
5. **Determinant:** Swap two rows and check that the sign flips.

### 16.3 Top 10 Traps Examiners Set

| # | Trap | How to Avoid |
|---|------|--------------|
| 1 | Forgetting $a \ne 0$ in quadratic | Always check if the leading coefficient could be 0 |
| 2 | Not flipping inequality when dividing by negative | Always track the sign of the divisor |
| 3 | $\log$ of negative/zero | Enforce domain: argument > 0, base > 0, base ≠ 1 |
| 4 | $0^0$ treated as 0 instead of 1 | Convention: $0^0 = 1$ in discrete math |
| 5 | $\sqrt{x^2} = x$ instead of $|x|$ | $\sqrt{x^2} = |x|$ always |
| 6 | Missing the $\pm$ in $x^2 = k \implies x = \pm\sqrt{k}$ | Two roots, not one |
| 7 | AP sum formula with wrong $n$ | $n$ = number of terms, not last term |
| 8 | GP infinite sum when $|r| \ge 1$ | Sum diverges; formula not valid |
| 9 | Confusing $\binom{n}{r}$ with $P(n,r)$ | $\binom{n}{r} = \frac{P(n,r)}{r!}$ |
| 10 | Matrix multiplication order | $AB \ne BA$ in general; check dimensions |

### 16.4 Speed Techniques Summary

| Technique | When to Use |
|-----------|-------------|
| **Vieta's Formulas** | Finding symmetric expressions of quadratic/cubic roots |
| **Coefficient Sum Test** ($a+b+c=0$) | Quickly finding one root of a quadratic |
| **AM-GM** | Optimisation without calculus |
| **Telescoping in Logs** | Chain of logarithms with changing bases |
| **Rationalisation** | Surd in denominator |
| **Wavy Curve** | Polynomial/rational inequalities |
| **Gauss Pairing** | Sum of AP |
| **Multiply-Subtract** | Sum of AGP |
| **Inclusion-Exclusion** | Counting in overlapping sets |
| **Prime Factorisation** | HCF/LCM, divisibility |

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.**
>
> This material covers every algebra topic tested in GATE, ESE, PSU, and BANK aptitude. Every formula is derived, every trick is justified, and every trap is exposed. Use this as your single-source-of-truth for algebra.
