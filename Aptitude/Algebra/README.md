# Algebra for Aptitude — GATE | ESE | PSU | BANK

> **Complete A-Z Study Material** — Concepts · Derivations · Tricks · Edge Cases · Solved Examples

---

## Table of Contents

| # | Topic | Link |
|---|-------|------|
| 1 | [Fundamentals of Algebra](#1-fundamentals-of-algebra) | Variables, Expressions, Identities |
| 2 | [Indices (Exponents) & Surds](#2-indices-exponents--surds) | Laws, Rationalization |
| 3 | [Logarithms](#3-logarithms) | Properties, Equations |
| 4 | [Polynomials](#4-polynomials) | Factoring, Remainder & Factor Theorem |
| 5 | [Linear Equations](#5-linear-equations) | Single & Simultaneous |
| 6 | [Quadratic Equations](#6-quadratic-equations) | Roots, Discriminant, Vieta's |
| 7 | [Inequalities](#7-inequalities) | Linear, Quadratic, Modulus |
| 8 | [Absolute Value (Modulus)](#8-absolute-value-modulus) | Properties, Equations |
| 9 | [Progressions & Series](#9-progressions--series) | AP, GP, HP, AGP, Special Sums |
| 10 | [Binomial Theorem](#10-binomial-theorem) | Expansion, General Term |
| 11 | [Set Theory (Aptitude)](#11-set-theory-aptitude) | Venn Diagrams, Operations |
| 12 | [Functions (Aptitude)](#12-functions-aptitude) | Domain, Range, Composition |
| 13 | [Matrices & Determinants (Aptitude)](#13-matrices--determinants-aptitude) | Operations, Cramer's Rule |
| 14 | [Exam Strategy & Shortcut Vault](#14-exam-strategy--shortcut-vault) | Speed Tricks, Edge Cases |

---

## 1. Fundamentals of Algebra

### 1.1 What Is Algebra?

Algebra is arithmetic with **unknowns**. Instead of saying "some number plus 3 equals 7", we write:

$$x + 3 = 7$$

**Analogy:** Think of $x$ as an empty box. Algebra is the art of figuring out what goes inside that box using the clues (equations) you're given.

### 1.2 Core Building Blocks

| Term | Meaning | Example |
|------|---------|---------|
| **Variable** | An unknown quantity | $x, y, z$ |
| **Constant** | A fixed value | $3, -7, \pi$ |
| **Coefficient** | Number multiplying a variable | In $5x$, coefficient = 5 |
| **Expression** | Combination using $+, -, \times, \div$ | $3x^2 + 2x - 5$ |
| **Equation** | Expression = Expression | $3x + 2 = 11$ |
| **Identity** | True for ALL values of the variable | $(a+b)^2 = a^2 + 2ab + b^2$ |

> **Key distinction (exam trap):**
> An **equation** is true for specific values; an **identity** is true for **every** value.

### 1.3 Fundamental Algebraic Identities

These identities appear everywhere — in simplification, factoring, and shortcut calculations.

#### How the identities are derived

**Identity 1:** $(a + b)^2 = a^2 + 2ab + b^2$

*Derivation:*
$$
(a+b)^2 = (a+b)(a+b) = a \cdot a + a \cdot b + b \cdot a + b \cdot b = a^2 + 2ab + b^2
$$

**Why it works:** We're computing the area of a square with side $(a+b)$. The four rectangles inside have areas $a^2$, $ab$, $ab$, $b^2$.

---

**Identity 2:** $(a - b)^2 = a^2 - 2ab + b^2$

*Derivation:*
$$
(a-b)^2 = (a-b)(a-b) = a^2 - ab - ab + b^2 = a^2 - 2ab + b^2
$$

---

**Identity 3:** $(a + b)(a - b) = a^2 - b^2$

*Derivation:*
$$
(a+b)(a-b) = a^2 - ab + ab - b^2 = a^2 - b^2
$$

**Use case (fast mental math):** $103 \times 97 = (100+3)(100-3) = 10000 - 9 = 9991$

---

**Identity 4:** $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3 = a^3 + b^3 + 3ab(a+b)$

*Derivation:*
$$
(a+b)^3 = (a+b)(a+b)^2 = (a+b)(a^2+2ab+b^2)
$$
$$
= a^3 + 2a^2b + ab^2 + a^2b + 2ab^2 + b^3 = a^3 + 3a^2b + 3ab^2 + b^3
$$

---

**Identity 5:** $(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3 = a^3 - b^3 - 3ab(a-b)$

---

**Identity 6:** $a^3 + b^3 = (a+b)(a^2 - ab + b^2)$

*Derivation (from Identity 4):*
$$
(a+b)^3 = a^3 + b^3 + 3ab(a+b)
$$
$$
a^3 + b^3 = (a+b)^3 - 3ab(a+b) = (a+b)\left[(a+b)^2 - 3ab\right] = (a+b)(a^2 - ab + b^2)
$$

---

**Identity 7:** $a^3 - b^3 = (a-b)(a^2 + ab + b^2)$

---

#### Extended Identities (Exam Favourites)

| Identity | Formula |
|----------|---------|
| $(a+b+c)^2$ | $a^2 + b^2 + c^2 + 2ab + 2bc + 2ca$ |
| $a^3+b^3+c^3-3abc$ | $(a+b+c)(a^2+b^2+c^2-ab-bc-ca)$ |
| **Special case** | If $a+b+c=0$, then $a^3+b^3+c^3 = 3abc$ |
| $a^2+b^2$ | $(a+b)^2 - 2ab$ or $(a-b)^2 + 2ab$ |
| $(a+b)^2 - (a-b)^2$ | $4ab$ |
| $(a+b)^2 + (a-b)^2$ | $2(a^2+b^2)$ |

### 1.4 Solved Examples

**Example 1:** If $x + \frac{1}{x} = 5$, find $x^2 + \frac{1}{x^2}$.

*Solution:*
$$
\left(x + \frac{1}{x}\right)^2 = x^2 + 2 + \frac{1}{x^2}
$$
$$
25 = x^2 + \frac{1}{x^2} + 2 \implies x^2 + \frac{1}{x^2} = 23
$$

**The trick:** Never solve for $x$ directly. Use the identity to "level up" from $x + 1/x$ to $x^2 + 1/x^2$.

---

**Example 2:** If $a + b + c = 0$, find $\frac{a^3 + b^3 + c^3}{abc}$.

*Solution:* When $a + b + c = 0$, we know $a^3 + b^3 + c^3 = 3abc$.
$$
\frac{3abc}{abc} = 3
$$

**Edge case:** This fails if $abc = 0$, i.e., at least one variable is zero.

---

**Example 3:** Find $97^2$ mentally.

*Solution:*
$$
97^2 = (100 - 3)^2 = 10000 - 600 + 9 = 9409
$$

---

## 2. Indices (Exponents) & Surds

### 2.1 The Atomic Truth

> Exponents count repeated multiplication. Surds are irrational roots that refuse to simplify.

### 2.2 Laws of Indices — With Derivation

**Why does $a^m \times a^n = a^{m+n}$?**

$$
a^m \times a^n = \underbrace{a \cdot a \cdots a}_{m} \times \underbrace{a \cdot a \cdots a}_{n} = \underbrace{a \cdot a \cdots a}_{m+n} = a^{m+n}
$$

The full set of laws:

| Law | Formula | Why |
|-----|---------|-----|
| Product | $a^m \cdot a^n = a^{m+n}$ | Counting total factors |
| Quotient | $\frac{a^m}{a^n} = a^{m-n}$ | Cancelling common factors |
| Power of Power | $(a^m)^n = a^{mn}$ | Repeating "m factors" n times |
| Zero Exponent | $a^0 = 1$ $(a \ne 0)$ | $a^n / a^n = a^{n-n} = a^0 = 1$ |
| Negative Exponent | $a^{-n} = \frac{1}{a^n}$ | From $a^0 / a^n = a^{-n}$ |
| Fractional Exponent | $a^{1/n} = \sqrt[n]{a}$ | The number whose $n$-th power is $a$ |
| Distribution | $(ab)^n = a^n b^n$ | Each factor raised independently |

**Edge case:** $0^0$ is conventionally taken as $1$ in combinatorics/algebra but is **indeterminate** in analysis. GATE usually avoids this.

### 2.3 Surds

A **surd** is a root that cannot be simplified to a rational number: $\sqrt{2}, \sqrt{3}, \sqrt[3]{5}$.

**Rationalisation:** Remove the surd from the denominator.

$$
\frac{1}{\sqrt{a} + \sqrt{b}} = \frac{\sqrt{a} - \sqrt{b}}{(\sqrt{a}+\sqrt{b})(\sqrt{a}-\sqrt{b})} = \frac{\sqrt{a} - \sqrt{b}}{a - b}
$$

**Why this works:** We use the identity $(x+y)(x-y) = x^2 - y^2$. Since $(\sqrt{a})^2 = a$, the surds vanish from the denominator.

### 2.4 Comparison of Surds

To compare $\sqrt[3]{4}$ and $\sqrt{3}$:

1. Find LCM of indices: LCM(3, 2) = 6
2. $\sqrt[3]{4} = 4^{1/3} = 4^{2/6} = (16)^{1/6}$
3. $\sqrt{3} = 3^{1/2} = 3^{3/6} = (27)^{1/6}$
4. Since $27 > 16$, we get $\sqrt{3} > \sqrt[3]{4}$.

### 2.5 Solved Examples

**Example 1:** Simplify $\frac{2^{n+4} - 2 \cdot 2^n}{2 \cdot 2^{n+3}}$.

$$
= \frac{2^n \cdot 2^4 - 2^{n+1}}{2^{n+4}} = \frac{2^n(16 - 2)}{2^{n+4}} = \frac{14 \cdot 2^n}{2^n \cdot 16} = \frac{14}{16} = \frac{7}{8}
$$

**Trick:** Factor out the smallest power of the common base.

---

**Example 2:** If $2^a = 3^b = 6^c$, prove that $c = \frac{ab}{a+b}$.

Let $2^a = 3^b = 6^c = k$.
Then $2 = k^{1/a}$, $3 = k^{1/b}$, $6 = k^{1/c}$.
Since $6 = 2 \times 3$: $k^{1/c} = k^{1/a} \cdot k^{1/b} = k^{1/a + 1/b}$

$$
\frac{1}{c} = \frac{1}{a} + \frac{1}{b} = \frac{a+b}{ab} \implies c = \frac{ab}{a+b}
$$

---

## 3. Logarithms

### 3.1 The Atomic Truth

> A logarithm answers: "What power do I raise the base to, to get this number?"

$$
\log_b a = x \iff b^x = a
$$

**Analogy:** If exponentiation is a question ("2 raised to what gives 8?"), the logarithm is the answer ($\log_2 8 = 3$).

### 3.2 Properties — With Derivation

Let $\log_b M = p$ and $\log_b N = q$, so $M = b^p$ and $N = b^q$.

**Product Rule:** $\log_b(MN) = \log_b M + \log_b N$

*Derivation:*
$$
MN = b^p \cdot b^q = b^{p+q} \implies \log_b(MN) = p + q = \log_b M + \log_b N
$$

**Quotient Rule:** $\log_b\left(\frac{M}{N}\right) = \log_b M - \log_b N$

*Derivation:*
$$
\frac{M}{N} = \frac{b^p}{b^q} = b^{p-q} \implies \log_b\left(\frac{M}{N}\right) = p - q
$$

**Power Rule:** $\log_b(M^k) = k \log_b M$

*Derivation:*
$$
M^k = (b^p)^k = b^{pk} \implies \log_b(M^k) = pk = k \log_b M
$$

**Change of Base:** $\log_b a = \frac{\log_c a}{\log_c b}$

*Derivation:*
Let $\log_b a = x$, so $b^x = a$. Taking $\log_c$ of both sides:
$$
x \log_c b = \log_c a \implies x = \frac{\log_c a}{\log_c b}
$$

### 3.3 Complete Property Table

| Property | Formula | Edge Case |
|----------|---------|-----------|
| Definition | $\log_b a = x \iff b^x = a$ | $a > 0, b > 0, b \ne 1$ |
| $\log_b 1$ | $= 0$ | Always |
| $\log_b b$ | $= 1$ | Always |
| $\log_b(b^x)$ | $= x$ | Always |
| $b^{\log_b x}$ | $= x$ | $x > 0$ |
| Product | $\log_b(MN) = \log_b M + \log_b N$ | $M, N > 0$ |
| Quotient | $\log_b(M/N) = \log_b M - \log_b N$ | $M, N > 0$ |
| Power | $\log_b(M^k) = k\log_b M$ | $M > 0$ |
| Change of base | $\log_b a = \frac{\log_c a}{\log_c b}$ | — |
| Reciprocal | $\log_b a = \frac{1}{\log_a b}$ | — |
| Chain | $\log_a b \cdot \log_b c = \log_a c$ | — |

### 3.4 Solved Examples

**Example 1:** Find $\log_2 \log_2 \log_2 (2^{2^{2^2}})$.

Work inside out:
- $2^2 = 4$
- $2^4 = 16$
- $2^{16} = 65536$
- $\log_2(65536) = 16$
- $\log_2(16) = 4$
- $\log_2(4) = 2$

**Answer: 2**

---

**Example 2:** If $\log_{10} 2 = 0.3010$, find the number of digits in $2^{64}$.

Number of digits = $\lfloor \log_{10}(2^{64}) \rfloor + 1 = \lfloor 64 \times 0.3010 \rfloor + 1 = \lfloor 19.264 \rfloor + 1 = 19 + 1 = 20$

**Trick:** Number of digits in $N$ = $\lfloor \log_{10} N \rfloor + 1$.

---

**Example 3:** If $\log_x 0.1 = -\frac{1}{3}$, find $x$.

$$
x^{-1/3} = 0.1 = 10^{-1} \implies x^{1/3} = 10 \implies x = 10^3 = 1000
$$

---

## 4. Polynomials

### 4.1 The Atomic Truth

> A polynomial is a sum of terms, each being a coefficient times a variable raised to a non-negative integer power.

$$
P(x) = a_n x^n + a_{n-1}x^{n-1} + \cdots + a_1 x + a_0
$$

**Degree** = highest power of $x$ with a non-zero coefficient.

### 4.2 Remainder Theorem

**Statement:** When polynomial $P(x)$ is divided by $(x - a)$, the remainder is $P(a)$.

**Why it works:**
$$
P(x) = (x - a) \cdot Q(x) + R
$$
Put $x = a$: $P(a) = 0 \cdot Q(a) + R = R$.

### 4.3 Factor Theorem

**Statement:** $(x - a)$ is a factor of $P(x)$ if and only if $P(a) = 0$.

This is a direct consequence of the Remainder Theorem: if the remainder is 0, then $(x-a)$ divides $P(x)$ exactly.

### 4.4 Factorisation Techniques

| Method | When to Use | Example |
|--------|-------------|---------|
| Common factor | All terms share a factor | $6x^2 + 9x = 3x(2x+3)$ |
| Grouping | 4 terms, pair-wise common factors | $ax + ay + bx + by = (a+b)(x+y)$ |
| Identity | Recognise $a^2-b^2$, perfect squares, etc. | $x^2-9 = (x+3)(x-3)$ |
| Trial (Factor Theorem) | Test integer roots via $P(a)=0$ | For $x^3-6x^2+11x-6$, try $x=1,2,3$ |
| Splitting middle term | Quadratic $ax^2+bx+c$ | Find two numbers with product $ac$ and sum $b$ |

### 4.5 Solved Examples

**Example 1:** Find the remainder when $x^{100}$ is divided by $x^2 - 3x + 2$.

$x^2 - 3x + 2 = (x-1)(x-2)$, which is degree 2, so remainder is at most degree 1: $R(x) = ax + b$.

$$
x^{100} = (x-1)(x-2) \cdot Q(x) + ax + b
$$

Put $x = 1$: $1 = a + b$
Put $x = 2$: $2^{100} = 2a + b$

Subtracting: $a = 2^{100} - 1$, $b = 1 - a = 2 - 2^{100}$.

$$R(x) = (2^{100} - 1)x + (2 - 2^{100})$$

---

**Example 2:** If $(x+2)$ is a factor of $x^3 + kx^2 + 4x + 12$, find $k$.

$P(-2) = 0$: $-8 + 4k - 8 + 12 = 0 \implies 4k - 4 = 0 \implies k = 1$.

---

## 5. Linear Equations

### 5.1 Single Variable

$$ax + b = 0 \implies x = -\frac{b}{a} \quad (a \ne 0)$$

### 5.2 System of Two Variables

$$
a_1x + b_1y = c_1 \\
a_2x + b_2y = c_2
$$

**Methods:** Substitution, Elimination, Cross-multiplication, Determinants (Cramer's Rule).

**Cross-Multiplication Formula:**

$$
\frac{x}{b_1c_2 - b_2c_1} = \frac{y}{c_1a_2 - c_2a_1} = \frac{1}{a_1b_2 - a_2b_1}
$$

**Condition Analysis:**

| Condition | Meaning | Graphically |
|-----------|---------|-------------|
| $\frac{a_1}{a_2} \ne \frac{b_1}{b_2}$ | Unique solution | Lines intersect |
| $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$ | Infinite solutions | Lines coincide |
| $\frac{a_1}{a_2} = \frac{b_1}{b_2} \ne \frac{c_1}{c_2}$ | No solution | Lines are parallel |

### 5.3 Solved Examples

**Example 1:** A two-digit number is 7 times the sum of its digits. The number obtained by reversing digits is 27 less than the original. Find the number.

Let digits be $x$ (tens) and $y$ (units). Number = $10x + y$.

$$10x + y = 7(x + y) \implies 3x = 6y \implies x = 2y$$
$$10x + y - (10y + x) = 27 \implies 9x - 9y = 27 \implies x - y = 3$$

From $x = 2y$ and $x - y = 3$: $2y - y = 3 \implies y = 3, x = 6$.

**Number = 63.** Check: $63 = 7 \times 9$ ✓, $63 - 36 = 27$ ✓.

---

## 6. Quadratic Equations

### 6.1 The Atomic Truth

> A quadratic is a polynomial of degree 2. Its graph is a parabola. It has at most 2 roots.

$$ax^2 + bx + c = 0 \quad (a \ne 0)$$

### 6.2 The Quadratic Formula — Derivation

Starting from $ax^2 + bx + c = 0$:

$$
x^2 + \frac{b}{a}x + \frac{c}{a} = 0
$$

Complete the square:

$$
\left(x + \frac{b}{2a}\right)^2 - \frac{b^2}{4a^2} + \frac{c}{a} = 0
$$

$$
\left(x + \frac{b}{2a}\right)^2 = \frac{b^2 - 4ac}{4a^2}
$$

$$
x + \frac{b}{2a} = \pm \frac{\sqrt{b^2 - 4ac}}{2a}
$$

$$
\boxed{x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}}
$$

### 6.3 Discriminant ($D = b^2 - 4ac$)

| Value of $D$ | Nature of Roots | Example |
|--------------|-----------------|---------|
| $D > 0$, perfect square | Real, rational, unequal | $x^2 - 5x + 6 = 0$, $D=1$ |
| $D > 0$, not perfect square | Real, irrational, unequal | $x^2 - 3x + 1 = 0$, $D=5$ |
| $D = 0$ | Real, rational, equal | $x^2 - 6x + 9 = 0$ |
| $D < 0$ | Complex (no real roots) | $x^2 + x + 1 = 0$, $D=-3$ |

**Exam trap:** If coefficients are rational and one root is $p + \sqrt{q}$, the other root **must** be $p - \sqrt{q}$. (Irrational roots come in conjugate pairs for rational-coefficient polynomials.)

### 6.4 Vieta's Formulas (Relation Between Roots & Coefficients)

If $\alpha, \beta$ are roots of $ax^2 + bx + c = 0$:

$$
\alpha + \beta = -\frac{b}{a}, \qquad \alpha \beta = \frac{c}{a}
$$

**Why?** Since $ax^2 + bx + c = a(x - \alpha)(x - \beta) = a\left[x^2 - (\alpha+\beta)x + \alpha\beta\right]$:

Comparing coefficients: $-(\alpha+\beta) = b/a$ and $\alpha\beta = c/a$.

**Building new equations from old roots:**

To find the equation whose roots are $f(\alpha)$ and $f(\beta)$, express the sum and product of the new roots in terms of $\alpha+\beta$ and $\alpha\beta$.

| If new roots are | Sum | Product |
|------------------|-----|---------|
| $\alpha^2, \beta^2$ | $(\alpha+\beta)^2 - 2\alpha\beta$ | $(\alpha\beta)^2$ |
| $1/\alpha, 1/\beta$ | $\frac{\alpha+\beta}{\alpha\beta}$ | $\frac{1}{\alpha\beta}$ |
| $\alpha+k, \beta+k$ | $(\alpha+\beta)+2k$ | $\alpha\beta + k(\alpha+\beta) + k^2$ |

### 6.5 Solved Examples

**Example 1:** If the roots of $x^2 - 6x + k = 0$ are in the ratio 2:1, find $k$.

Let roots be $2m$ and $m$.
- Sum: $2m + m = 6 \implies m = 2$
- Product: $2m \cdot m = k \implies 2(4) = 8$

**$k = 8$.**

---

**Example 2:** For what values of $k$ does $x^2 + 2(k-1)x + (k+5) = 0$ have equal roots?

$D = 0$: $4(k-1)^2 - 4(k+5) = 0$

$$
(k-1)^2 = k+5 \implies k^2 - 2k + 1 = k + 5 \implies k^2 - 3k - 4 = 0 \implies (k-4)(k+1) = 0
$$

**$k = 4$ or $k = -1$.**

---

**Example 3:** If $\alpha, \beta$ are roots of $2x^2 - 3x + 1 = 0$, find $\alpha^3 + \beta^3$.

$\alpha + \beta = 3/2$, $\alpha\beta = 1/2$.

$$
\alpha^3 + \beta^3 = (\alpha+\beta)^3 - 3\alpha\beta(\alpha+\beta) = \frac{27}{8} - 3 \cdot \frac{1}{2} \cdot \frac{3}{2} = \frac{27}{8} - \frac{9}{4} = \frac{27 - 18}{8} = \frac{9}{8}
$$

---

## 7. Inequalities

### 7.1 The Atomic Truth

> An inequality states that one expression is larger or smaller than another. The key rule: **multiplying/dividing by a negative number flips the sign**.

### 7.2 Properties of Inequalities

| Property | Rule |
|----------|------|
| Addition | $a > b \implies a + c > b + c$ |
| Subtraction | $a > b \implies a - c > b - c$ |
| Positive multiplication | $a > b, c > 0 \implies ac > bc$ |
| Negative multiplication | $a > b, c < 0 \implies ac < bc$ ⚠️ **flips** |
| Reciprocal (same sign) | $0 < a < b \implies \frac{1}{a} > \frac{1}{b}$ ⚠️ **flips** |
| Squaring (both positive) | $0 < a < b \implies a^2 < b^2$ |

### 7.3 Linear Inequalities

Solve like equations, but **flip the sign when multiplying/dividing by negative**.

**Example:** $-3x + 5 \ge 2$
$$-3x \ge -3 \implies x \le 1 \quad \text{(sign flipped)}$$

### 7.4 Quadratic Inequalities

To solve $ax^2 + bx + c > 0$ (with $a > 0$):

1. Find roots $\alpha, \beta$ (with $\alpha < \beta$).
2. The parabola opens upward (since $a > 0$).
3. $ax^2 + bx + c > 0$ when $x < \alpha$ or $x > \beta$.
4. $ax^2 + bx + c < 0$ when $\alpha < x < \beta$.

**Mnemonic: The Wavy Curve Method**

For a product like $(x - a_1)(x - a_2)\cdots(x - a_n) > 0$:

1. Mark roots $a_1 < a_2 < \cdots < a_n$ on a number line.
2. Start from the rightmost interval with a **+** sign.
3. Alternate signs as you cross each root (for single-multiplicity roots).

### 7.5 Important Algebraic Inequalities

**AM-GM Inequality:**
$$
\frac{a + b}{2} \ge \sqrt{ab} \quad (a, b > 0)
$$

*Derivation:*
$$
(\sqrt{a} - \sqrt{b})^2 \ge 0 \implies a - 2\sqrt{ab} + b \ge 0 \implies \frac{a+b}{2} \ge \sqrt{ab}
$$

Equality holds when $a = b$.

**Use case in exams:** To find the minimum of $x + \frac{1}{x}$ (for $x > 0$):
$$
x + \frac{1}{x} \ge 2\sqrt{x \cdot \frac{1}{x}} = 2
$$

Minimum value is **2** at $x = 1$.

### 7.6 Solved Examples

**Example 1:** Find the range of $x$ for $x^2 - 5x + 6 < 0$.

Roots: $(x-2)(x-3) = 0 \implies x = 2, 3$.

Since the parabola opens upward and we want the negative region: $2 < x < 3$.

---

**Example 2:** Find the minimum value of $a^2 + b^2$ given $a + b = 10$, $a, b > 0$.

By QM-AM (or Cauchy-Schwarz):
$$
\frac{a^2 + b^2}{2} \ge \left(\frac{a+b}{2}\right)^2 = 25 \implies a^2 + b^2 \ge 50
$$

Minimum is **50** when $a = b = 5$.

**Alternative (identity):** $a^2 + b^2 = (a+b)^2 - 2ab = 100 - 2ab$. This is minimised when $ab$ is maximised. By AM-GM, $ab \le (a+b)^2/4 = 25$, so $a^2+b^2 \ge 100 - 50 = 50$.

---

## 8. Absolute Value (Modulus)

### 8.1 Definition

$$
|x| = \begin{cases} x & \text{if } x \ge 0 \\ -x & \text{if } x < 0 \end{cases}
$$

**Analogy:** $|x|$ is the distance of $x$ from 0 on the number line. It's always non-negative.

### 8.2 Key Properties

| Property | Formula |
|----------|---------|
| Non-negativity | $\|x\| \ge 0$ |
| Definiteness | $\|x\| = 0 \iff x = 0$ |
| Symmetry | $\|-x\| = \|x\|$ |
| Product | $\|xy\| = \|x\| \cdot \|y\|$ |
| Quotient | $\|x/y\| = \|x\|/\|y\|$ $(y \ne 0)$ |
| Triangle Inequality | $\|x + y\| \le \|x\| + \|y\|$ |
| Reverse Triangle | $\lvert \|x\| - \|y\| \rvert \le \|x - y\|$ |
| Square | $\|x\|^2 = x^2$ |

### 8.3 Solving Modulus Equations

**Type 1:** $|f(x)| = a$ (where $a > 0$)
$$f(x) = a \quad \text{or} \quad f(x) = -a$$

**Type 2:** $|f(x)| = |g(x)|$
$$f(x) = g(x) \quad \text{or} \quad f(x) = -g(x)$$

**Type 3:** $|f(x)| = f(x)$ — This means $f(x) \ge 0$.

### 8.4 Solving Modulus Inequalities

| Inequality | Solution |
|------------|----------|
| $\|x\| < a$ $(a > 0)$ | $-a < x < a$ |
| $\|x\| > a$ $(a > 0)$ | $x < -a$ or $x > a$ |
| $\|x\| \le a$ $(a > 0)$ | $-a \le x \le a$ |
| $\|x\| \ge a$ $(a > 0)$ | $x \le -a$ or $x \ge a$ |

**Mnemonic:** "Less than → between, Greater than → outside."

### 8.5 Solved Example

**Example:** Solve $|2x - 3| < 5$.

$$
-5 < 2x - 3 < 5 \implies -2 < 2x < 8 \implies -1 < x < 4
$$

---

## 9. Progressions & Series

### 9.1 Arithmetic Progression (AP)

A sequence where the difference between consecutive terms is constant.

$$a, a+d, a+2d, \ldots$$

| Formula | Expression |
|---------|------------|
| $n$-th term | $a_n = a + (n-1)d$ |
| Sum of $n$ terms | $S_n = \frac{n}{2}[2a + (n-1)d] = \frac{n}{2}(a + l)$ |
| Common difference | $d = a_n - a_{n-1}$ |
| $n$-th term from sum | $a_n = S_n - S_{n-1}$ (for $n \ge 2$) |

**Derivation of $S_n$:**

Write the sum forwards and backwards:
$$
S_n = a + (a+d) + (a+2d) + \cdots + l
$$
$$
S_n = l + (l-d) + (l-2d) + \cdots + a
$$

Adding: $2S_n = n(a + l)$, so $S_n = \frac{n}{2}(a+l)$.

**Key Properties:**
- If $a, b, c$ are in AP: $2b = a + c$ (middle term = average of neighbours)
- Arithmetic mean of $a$ and $b$: $AM = \frac{a+b}{2}$
- Choosing terms wisely: 3 terms → $a-d, a, a+d$; 4 terms → $a-3d, a-d, a+d, a+3d$

### 9.2 Geometric Progression (GP)

A sequence where the ratio of consecutive terms is constant.

$$a, ar, ar^2, \ldots$$

| Formula | Expression |
|---------|------------|
| $n$-th term | $a_n = ar^{n-1}$ |
| Sum of $n$ terms | $S_n = a\cdot\frac{r^n - 1}{r - 1}$ $(r \ne 1)$ |
| Sum to infinity | $S_\infty = \frac{a}{1-r}$ $(\lvert r \rvert < 1)$ |

**Derivation of $S_n$:**

$$S_n = a + ar + ar^2 + \cdots + ar^{n-1}$$
$$rS_n = ar + ar^2 + \cdots + ar^n$$

Subtracting: $S_n - rS_n = a - ar^n$

$$S_n(1 - r) = a(1 - r^n) \implies S_n = \frac{a(1 - r^n)}{1 - r} = \frac{a(r^n - 1)}{r - 1}$$

**Key Properties:**
- If $a, b, c$ are in GP: $b^2 = ac$
- Geometric mean of $a$ and $b$: $GM = \sqrt{ab}$
- $AM \ge GM$ always (for positive numbers)
- Choosing terms wisely: 3 terms → $a/r, a, ar$

### 9.3 Harmonic Progression (HP)

A sequence is in HP if the reciprocals are in AP.

$$\frac{1}{a}, \frac{1}{a+d}, \frac{1}{a+2d}, \ldots$$

- **No direct formula for sum.** Convert to AP using reciprocals.
- Harmonic mean of $a$ and $b$: $HM = \frac{2ab}{a+b}$
- Relationship: $AM \ge GM \ge HM$ and $GM^2 = AM \times HM$ (for two positive numbers)

**Derivation of $GM^2 = AM \times HM$:**

$$
AM \times HM = \frac{a+b}{2} \times \frac{2ab}{a+b} = ab = (\sqrt{ab})^2 = GM^2
$$

### 9.4 Arithmetico-Geometric Progression (AGP)

A series where each term is the product of corresponding AP and GP terms.

$$S = ab + (a+d)br + (a+2d)br^2 + \cdots$$

**Method to find sum:** Multiply $S$ by $r$, subtract, and reduce to a GP.

**Example:** Find the sum to infinity of $1 + 3x + 5x^2 + 7x^3 + \cdots$ $(|x| < 1)$.

$$S = 1 + 3x + 5x^2 + 7x^3 + \cdots$$
$$xS = x + 3x^2 + 5x^3 + \cdots$$
$$S - xS = 1 + 2x + 2x^2 + 2x^3 + \cdots = 1 + \frac{2x}{1-x} = \frac{1+x}{1-x}$$
$$S = \frac{1+x}{(1-x)^2}$$

### 9.5 Special Series & Summation Formulas

| Sum | Formula | Derivation Hint |
|-----|---------|----------------|
| $\sum_{k=1}^{n} k$ | $\frac{n(n+1)}{2}$ | AP sum with $a=1, d=1$ |
| $\sum_{k=1}^{n} k^2$ | $\frac{n(n+1)(2n+1)}{6}$ | Telescoping via $(k+1)^3 - k^3$ |
| $\sum_{k=1}^{n} k^3$ | $\left[\frac{n(n+1)}{2}\right]^2$ | Sum of cubes = square of sum of naturals |

**Derivation of $\sum k^2$:**

Use the identity $(k+1)^3 - k^3 = 3k^2 + 3k + 1$.

Sum from $k=1$ to $n$:
$$
(n+1)^3 - 1 = 3\sum k^2 + 3\sum k + n
$$
$$
n^3 + 3n^2 + 3n = 3\sum k^2 + \frac{3n(n+1)}{2} + n
$$
$$
3\sum k^2 = n^3 + 3n^2 + 2n - \frac{3n(n+1)}{2} = \frac{2n^3 + 6n^2 + 4n - 3n^2 - 3n}{2} = \frac{2n^3 + 3n^2 + n}{2}
$$
$$
\sum k^2 = \frac{n(n+1)(2n+1)}{6}
$$

### 9.6 Solved Examples

**Example 1:** The sum of an AP is 150. It has 10 terms, first term is 1. Find $d$.

$$
S_{10} = \frac{10}{2}[2(1) + 9d] = 5(2 + 9d) = 150 \implies 2 + 9d = 30 \implies d = \frac{28}{9}
$$

---

**Example 2:** Find the sum $1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots$ to infinity.

GP with $a = 1, r = 1/2$:
$$S_\infty = \frac{1}{1 - 1/2} = 2$$

---

**Example 3:** If the 4th and 7th terms of a GP are 24 and 192, find the GP.

$a r^3 = 24$ and $ar^6 = 192$. Dividing: $r^3 = 8 \implies r = 2$.
Then $a \cdot 8 = 24 \implies a = 3$.

**GP: 3, 6, 12, 24, 48, 96, 192, ...**

---

## 10. Binomial Theorem

### 10.1 The Atomic Truth

> The Binomial Theorem expands $(a+b)^n$ into a sum of terms involving $\binom{n}{k}$.

$$
(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k
$$

where $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ is the binomial coefficient.

### 10.2 Why It Works

Consider $(a+b)^n = (a+b)(a+b)\cdots(a+b)$ ($n$ times).

When you expand, each term picks either $a$ or $b$ from each factor. A term $a^{n-k}b^k$ appears whenever you pick $b$ from exactly $k$ of the $n$ factors. The number of ways to choose those $k$ factors is $\binom{n}{k}$.

### 10.3 Key Components

| Component | Formula |
|-----------|---------|
| General term ($T_{r+1}$) | $\binom{n}{r} a^{n-r} b^r$ |
| Number of terms | $n + 1$ |
| Middle term (n even) | $T_{n/2 + 1}$ |
| Middle terms (n odd) | $T_{(n+1)/2}$ and $T_{(n+3)/2}$ |
| Sum of coefficients | Put $a=b=1$: $(1+1)^n = 2^n$ |
| Sum of even-index coefficients | $2^{n-1}$ |
| Sum of odd-index coefficients | $2^{n-1}$ |

### 10.4 Properties of Binomial Coefficients

$$
\binom{n}{0} + \binom{n}{1} + \binom{n}{2} + \cdots + \binom{n}{n} = 2^n
$$

$$
\binom{n}{0} - \binom{n}{1} + \binom{n}{2} - \cdots = 0
$$

$$
\binom{n}{r} = \binom{n}{n-r} \quad \text{(symmetry)}
$$

$$
\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r} \quad \text{(Pascal's Rule)}
$$

### 10.5 Solved Examples

**Example 1:** Find the coefficient of $x^5$ in $(1 + x)^8$.

$$
T_{r+1} = \binom{8}{r} x^r \implies r = 5 \implies \binom{8}{5} = 56
$$

---

**Example 2:** Find the term independent of $x$ in $\left(x + \frac{1}{x^2}\right)^9$.

$$
T_{r+1} = \binom{9}{r} x^{9-r} \cdot x^{-2r} = \binom{9}{r} x^{9 - 3r}
$$

For term independent of $x$: $9 - 3r = 0 \implies r = 3$.

$$T_4 = \binom{9}{3} = 84$$

---

**Example 3:** Find the last digit of $7^{100}$.

$7^{100} = (7^2)^{50} = 49^{50} = (50 - 1)^{50}$.

$$
(50 - 1)^{50} = \sum_{k=0}^{50} \binom{50}{k} 50^k (-1)^{50-k}
$$

Only the last term ($k=0$) contributes to the last digit: $(-1)^{50} = 1$.

All other terms contain $50$ as a factor, hence end in $0$.

**Last digit = 1.**

**Shortcut:** Powers of 7 cycle: $7, 9, 3, 1, 7, 9, 3, 1, \ldots$ (cycle of 4). $100 \div 4 = 25$ remainder $0$, so last digit = $7^4$'s last digit = $1$.

---

## 11. Set Theory (Aptitude)

### 11.1 The Atomic Truth

> A set is a well-defined collection of distinct objects.

### 11.2 Operations

| Operation | Notation | Meaning |
|-----------|----------|---------|
| Union | $A \cup B$ | Elements in $A$ or $B$ (or both) |
| Intersection | $A \cap B$ | Elements in both $A$ and $B$ |
| Difference | $A - B$ | Elements in $A$ but not in $B$ |
| Complement | $A'$ or $\bar{A}$ | Elements not in $A$ (relative to universal set) |
| Symmetric Difference | $A \Delta B$ | $(A - B) \cup (B - A)$ |

### 11.3 Key Formulas

**Two sets:**
$$
|A \cup B| = |A| + |B| - |A \cap B|
$$

**Why?** When we add $|A|$ and $|B|$, the elements in $A \cap B$ get counted twice. So we subtract once.

**Three sets:**
$$
|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |B \cap C| - |A \cap C| + |A \cap B \cap C|
$$

**De Morgan's Laws:**
$$
(A \cup B)' = A' \cap B' \qquad (A \cap B)' = A' \cup B'
$$

**Mnemonic:** "Break the bar, change the sign." The complement of a union is the intersection of complements, and vice versa.

### 11.4 Solved Example

**Example:** In a group of 100 students, 50 like Maths, 40 like Physics, 30 like Chemistry. 15 like both Maths & Physics, 10 like both Physics & Chemistry, 20 like both Maths & Chemistry, 5 like all three. How many like none?

$$
|M \cup P \cup C| = 50 + 40 + 30 - 15 - 10 - 20 + 5 = 80
$$

Students liking none = $100 - 80 = 20$.

---

## 12. Functions (Aptitude)

### 12.1 The Atomic Truth

> A function assigns exactly one output to each input. $f: A \to B$ maps each element of $A$ to a unique element of $B$.

### 12.2 Domain & Range

- **Domain:** Set of all valid inputs.
- **Range (Codomain Image):** Set of all actual outputs.

**Edge cases for domain:**
- $\frac{1}{x-2}$: Domain = $\mathbb{R} \setminus \{2\}$ (denominator ≠ 0)
- $\sqrt{x-3}$: Domain = $[3, \infty)$ (expression under root ≥ 0)
- $\log(x-1)$: Domain = $(1, \infty)$ (argument > 0)

### 12.3 Types of Functions

| Type | Definition | Test |
|------|-----------|------|
| **One-to-one (Injective)** | Different inputs → different outputs | $f(a) = f(b) \implies a = b$ |
| **Onto (Surjective)** | Every element of codomain is hit | Range = Codomain |
| **Bijective** | Both one-to-one and onto | Invertible |
| **Even** | $f(-x) = f(x)$ | Symmetric about y-axis |
| **Odd** | $f(-x) = -f(x)$ | Symmetric about origin |

### 12.4 Composition & Inverse

- $(f \circ g)(x) = f(g(x))$: Apply $g$ first, then $f$.
- $f^{-1}$ exists only if $f$ is bijective.
- $f(f^{-1}(x)) = x$ and $f^{-1}(f(x)) = x$.

### 12.5 Solved Example

**Example:** If $f(x) = 2x + 3$ and $g(x) = x^2 - 1$, find $(f \circ g)(2)$ and $(g \circ f)(2)$.

$(f \circ g)(2) = f(g(2)) = f(4-1) = f(3) = 9$

$(g \circ f)(2) = g(f(2)) = g(7) = 49 - 1 = 48$

**Key insight:** $f \circ g \ne g \circ f$ in general. Composition is **not commutative**.

---

## 13. Matrices & Determinants (Aptitude)

### 13.1 The Atomic Truth

> A matrix is a rectangular array of numbers. A determinant is a single number computed from a square matrix that encodes whether the matrix is invertible.

### 13.2 Matrix Operations

| Operation | Rule |
|-----------|------|
| Addition | $(A+B)_{ij} = A_{ij} + B_{ij}$ (same dimensions) |
| Scalar multiplication | $(kA)_{ij} = k \cdot A_{ij}$ |
| Multiplication | $(AB)_{ij} = \sum_k A_{ik} B_{kj}$ |
| Transpose | $(A^T)_{ij} = A_{ji}$ |

**Critical exam fact:** $AB \ne BA$ in general. Matrix multiplication is **not commutative**.

### 13.3 Determinant of 2×2 Matrix

$$
\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc
$$

**Why?** The determinant gives the signed area of the parallelogram formed by the row vectors. If it's zero, the rows are parallel (linearly dependent) → no inverse.

### 13.4 Determinant of 3×3 Matrix (Sarrus' Rule)

$$
\det\begin{pmatrix} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \\ a_3 & b_3 & c_3 \end{pmatrix} = a_1(b_2c_3 - b_3c_2) - b_1(a_2c_3 - a_3c_2) + c_1(a_2b_3 - a_3b_2)
$$

### 13.5 Cramer's Rule (2 Variables)

For $a_1x + b_1y = c_1$ and $a_2x + b_2y = c_2$:

$$
x = \frac{\begin{vmatrix} c_1 & b_1 \\ c_2 & b_2 \end{vmatrix}}{\begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix}}, \qquad
y = \frac{\begin{vmatrix} a_1 & c_1 \\ a_2 & c_2 \end{vmatrix}}{\begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix}}
$$

### 13.6 Key Properties of Determinants

| Property | Statement |
|----------|-----------|
| Row/Column swap | Changes sign of determinant |
| Row/Column of zeros | Determinant = 0 |
| Two identical rows/columns | Determinant = 0 |
| Scalar multiple of row | Determinant multiplied by that scalar |
| Row addition | Determinant unchanged |
| $\det(AB)$ | $= \det(A) \cdot \det(B)$ |
| $\det(A^T)$ | $= \det(A)$ |
| $\det(kA)$ for $n \times n$ | $= k^n \det(A)$ |
| $A$ invertible | $\iff \det(A) \ne 0$ |

### 13.7 Solved Example

**Example:** Solve using Cramer's rule: $2x + 3y = 7$, $3x - 2y = 4$.

$$
D = \begin{vmatrix} 2 & 3 \\ 3 & -2 \end{vmatrix} = -4 - 9 = -13
$$

$$
D_x = \begin{vmatrix} 7 & 3 \\ 4 & -2 \end{vmatrix} = -14 - 12 = -26 \implies x = \frac{-26}{-13} = 2
$$

$$
D_y = \begin{vmatrix} 2 & 7 \\ 3 & 4 \end{vmatrix} = 8 - 21 = -13 \implies y = \frac{-13}{-13} = 1
$$

**Solution:** $x = 2, y = 1$.

---

## 14. Exam Strategy & Shortcut Vault

### 14.1 Speed Tricks for Competitive Exams

#### Trick 1: Component Ratio (Allegation)

When two quantities of average values $A_1$ and $A_2$ are mixed to get average $A$:

$$
\frac{n_1}{n_2} = \frac{A_2 - A}{A - A_1}
$$

#### Trick 2: Symmetric Expression Shortcuts

If you know $x + y$ and $xy$, you can find **any** symmetric expression of $x$ and $y$:

| Expression | In terms of $s = x+y$, $p = xy$ |
|------------|----------------------------------|
| $x^2 + y^2$ | $s^2 - 2p$ |
| $x^3 + y^3$ | $s^3 - 3sp$ |
| $x^2 - y^2$ | $s \cdot \sqrt{s^2 - 4p}$ (if $x > y$) |
| $(x - y)^2$ | $s^2 - 4p$ |
| $x^4 + y^4$ | $(s^2 - 2p)^2 - 2p^2$ |

#### Trick 3: Last Digit Patterns

| Base | Cycle of last digits | Period |
|------|---------------------|--------|
| 2 | 2, 4, 8, 6 | 4 |
| 3 | 3, 9, 7, 1 | 4 |
| 4 | 4, 6 | 2 |
| 5 | 5 | 1 |
| 6 | 6 | 1 |
| 7 | 7, 9, 3, 1 | 4 |
| 8 | 8, 4, 2, 6 | 4 |
| 9 | 9, 1 | 2 |

**Method:** Divide exponent by cycle length. Remainder tells you the position in the cycle (remainder 0 → last position).

#### Trick 4: Remainder Shortcuts

- $\frac{a^n}{a-1}$: Remainder is always **1** (since $a \equiv 1 \pmod{a-1}$)
- $\frac{a^n}{a+1}$: Remainder is **1** if $n$ is even, **$a$** (or equivalently $-1$) if $n$ is odd.

#### Trick 5: Sum of Digits Divisibility

| Divisor | Quick Test |
|---------|------------|
| 3 | Sum of digits divisible by 3 |
| 9 | Sum of digits divisible by 9 |
| 11 | Alternating sum of digits divisible by 11 |

#### Trick 6: Number of Factors

If $N = p_1^{a_1} \cdot p_2^{a_2} \cdots p_k^{a_k}$, then:

- Number of factors: $(a_1+1)(a_2+1)\cdots(a_k+1)$
- Sum of factors: $\frac{p_1^{a_1+1}-1}{p_1-1} \cdot \frac{p_2^{a_2+1}-1}{p_2-1} \cdots$

### 14.2 Common Exam Traps

| Trap | What Goes Wrong | Prevention |
|------|----------------|------------|
| Sign flip in inequality | Forgetting to flip when multiplying by negative | Always check the sign of the multiplier |
| $\log$ domain | Taking $\log$ of zero or negative number | Verify argument > 0 |
| $(a+b)^n \ne a^n + b^n$ | Applying power distributively over addition | Only valid for $n=1$ |
| $\sqrt{x^2} = \|x\|$, not $x$ | Assuming the root is always positive and equal to $x$ | Use modulus for even roots |
| AM-GM with negative numbers | Applying AM ≥ GM when terms are negative | AM-GM requires **positive** terms |
| Series sum formula confusion | Using GP sum when $r = 1$ | $r=1 \implies S_n = na$ |
| Modulus equation missing cases | Not checking both $+$ and $-$ branches | Always split into cases |
| Confusing $f \circ g$ with $g \circ f$ | Applying in wrong order | "Fog": $f$ is outer, $g$ is inner |

### 14.3 Edge Cases Checklist

Before submitting any answer, verify:

- [ ] Did you check $n = 0$ and $n = 1$ special cases?
- [ ] Did you verify the domain (no division by zero, no log of non-positive, no even root of negative)?
- [ ] Did you handle the equality condition in inequalities?
- [ ] For modulus equations, did you check all branches?
- [ ] For GP problems, did you handle $r = 1$ separately?
- [ ] For quadratic problems, did you verify that $a \ne 0$?
- [ ] Did you cross-check by substituting back into the original equation?

### 14.4 The 5-Second Sanity Checks

1. **Dimensional analysis:** Does the answer have the right "shape"? (e.g., sum of positive terms should be positive)
2. **Extreme value test:** Plug in $0$, $1$, or $\infty$ to quickly verify.
3. **Parity check:** If all inputs are even, is the output even?
4. **Magnitude check:** Is the answer roughly the right size?
5. **Symmetry check:** If the problem is symmetric in $a$ and $b$, the answer should be too.

---

## Quick Reference Card

### Must-Know Identities

$$
(a+b)^2 = a^2 + 2ab + b^2
$$
$$
(a-b)^2 = a^2 - 2ab + b^2
$$
$$
a^2 - b^2 = (a+b)(a-b)
$$
$$
a^3 + b^3 = (a+b)(a^2-ab+b^2)
$$
$$
a^3 - b^3 = (a-b)(a^2+ab+b^2)
$$
$$
\text{If } a+b+c = 0, \text{ then } a^3+b^3+c^3 = 3abc
$$

### Must-Know Series

$$
\sum_{k=1}^n k = \frac{n(n+1)}{2}, \quad \sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}, \quad \sum_{k=1}^n k^3 = \left(\frac{n(n+1)}{2}\right)^2
$$

### Must-Know Logarithm Results

$$
\log_b(MN) = \log_b M + \log_b N, \quad \log_b(M^k) = k\log_b M, \quad \log_b a = \frac{1}{\log_a b}
$$

### Must-Know Inequality

$$
AM \ge GM \ge HM \quad \text{(for positive reals)}
$$

---

*End of Algebra Study Material — GATE | ESE | PSU | BANK*
