# 📚 Ratio & Proportion — Complete Study Material

> **Target Exams:** GATE · ESE · PSU · Bank (IBPS / SBI / RBI)
> **Goal:** Master every concept from zero to Rank-1 level — no repetition, full intuition.

---

## Table of Contents

1. [What is a Ratio?](#1-what-is-a-ratio)
2. [Fundamental Properties of Ratios](#2-fundamental-properties-of-ratios)
3. [Comparison of Ratios](#3-comparison-of-ratios)
4. [Compounded Ratio & Special Ratio Types](#4-compounded-ratio--special-ratio-types)
5. [What is Proportion?](#5-what-is-proportion)
6. [Properties of Proportion](#6-properties-of-proportion)
7. [Types of Proportion](#7-types-of-proportion)
8. [Componendo & Dividendo (The Power Theorem)](#8-componendo--dividendo-the-power-theorem)
9. [k-Factor Method (The Universal Ratio Solver)](#9-k-factor-method-the-universal-ratio-solver)
10. [Variation (Direct, Inverse, Joint)](#10-variation-direct-inverse-joint)
11. [Mixture & Alligation](#11-mixture--alligation)
12. [Partnership (Ratio in Business)](#12-partnership-ratio-in-business)
13. [Solved Examples — Concept by Concept](#13-solved-examples--concept-by-concept)
14. [Tricks & Shortcuts for Competitive Exams](#14-tricks--shortcuts-for-competitive-exams)
15. [Common Traps & Edge Cases](#15-common-traps--edge-cases)
16. [Practice Problems (with Answers)](#16-practice-problems-with-answers)

---

## 1. What is a Ratio?

### The Atomic Truth

> A ratio is a **multiplicative comparison** of two quantities of the **same kind**.

When we say *the ratio of A to B is 3 : 5*, we mean:

$$\frac{A}{B} = \frac{3}{5}$$

It does **not** mean $A = 3$ or $B = 5$. It means for every 3 units of A, there are 5 units of B.

### Why "Same Kind"?

You can compare kg with kg, litres with litres, but not kg with litres. Ratio is unit-less — the units cancel out.

**Analogy:** Think of a ratio like a recipe. "2 cups flour to 1 cup sugar" tells you the *relationship*, not the absolute amounts. Whether you use 4 cups flour and 2 cups sugar, or 20 and 10, the ratio 2 : 1 holds.

### Formal Definition

If $a$ and $b$ are two quantities of the same kind ($b \neq 0$), then $a : b = \dfrac{a}{b}$.

- $a$ is the **antecedent** (first term).
- $b$ is the **consequent** (second term).

### How the Notation Works

$$a : b = \frac{a}{b}$$

This is just a fraction written differently. Everything you know about fractions applies directly to ratios.

---

## 2. Fundamental Properties of Ratios

### Property 1 — Scaling (Multiplication / Division)

$$a : b = ka : kb \quad \text{for any } k \neq 0$$

**Why?** Because $\dfrac{ka}{kb} = \dfrac{a}{b}$.

**Example:** $3 : 5 = 6 : 10 = 30 : 50$.

This is exactly like simplifying fractions.

### Property 2 — Ratio in Simplest Form

A ratio $a : b$ is in simplest form when $\gcd(a, b) = 1$.

**Example:** $12 : 18$. Since $\gcd(12, 18) = 6$, simplest form is $2 : 3$.

### Property 3 — Order Matters

$$a : b \neq b : a \quad \text{(unless } a = b\text{)}$$

$3 : 5 \neq 5 : 3$. The first compares A to B; the second compares B to A.

### Property 4 — Ratio of Three or More Quantities

$a : b : c$ means $\dfrac{a}{b}$ and $\dfrac{b}{c}$ are both defined simultaneously.

**Key:** When combining two ratios like $A : B = 2 : 3$ and $B : C = 4 : 5$, you must make $B$ common:

$$A : B = 2 : 3 = 8 : 12, \quad B : C = 4 : 5 = 12 : 15$$

$$\Rightarrow A : B : C = 8 : 12 : 15$$

**How?** Multiply the first ratio by 4 and the second by 3 so that B becomes $\text{lcm}(3, 4) = 12$ in both.

---

## 3. Comparison of Ratios

### Method 1 — Cross Multiplication

To compare $\dfrac{a}{b}$ and $\dfrac{c}{d}$:

- If $ad > bc$, then $a : b > c : d$
- If $ad = bc$, then $a : b = c : d$
- If $ad < bc$, then $a : b < c : d$

**Example:** Compare $3 : 7$ and $5 : 11$.

$3 \times 11 = 33$ vs. $7 \times 5 = 35$.

Since $33 < 35$, we get $3 : 7 < 5 : 11$.

### Method 2 — Decimal Conversion

$\dfrac{3}{7} \approx 0.4286$ and $\dfrac{5}{11} \approx 0.4545$.

So $3 : 7 < 5 : 11$. ✓

### Method 3 — Make Denominators Equal (LCM Method)

Convert both fractions to the same denominator using LCM and compare numerators.

---

## 4. Compounded Ratio & Special Ratio Types

### Compounded Ratio

If we have ratios $a : b$ and $c : d$, their **compounded ratio** is:

$$a : b \text{ compounded with } c : d = ac : bd$$

**Why?** Because $\dfrac{a}{b} \times \dfrac{c}{d} = \dfrac{ac}{bd}$.

**Example:** Compounded ratio of $2 : 3$ and $5 : 7$ is $10 : 21$.

### Duplicate Ratio

The duplicate ratio of $a : b$ is $a^2 : b^2$.

$$\text{Duplicate of } 3 : 4 = 9 : 16$$

**Where does this come from?** It is the compounded ratio of $a : b$ with itself: $\dfrac{a}{b} \times \dfrac{a}{b} = \dfrac{a^2}{b^2}$.

### Triplicate Ratio

The triplicate ratio of $a : b$ is $a^3 : b^3$.

### Sub-Duplicate Ratio

The sub-duplicate ratio of $a : b$ is $\sqrt{a} : \sqrt{b}$.

$$\text{Sub-duplicate of } 9 : 16 = 3 : 4$$

### Sub-Triplicate Ratio

The sub-triplicate ratio of $a : b$ is $\sqrt[3]{a} : \sqrt[3]{b}$.

### Reciprocal (Inverse) Ratio

The reciprocal ratio of $a : b$ is $b : a$ (equivalently $\dfrac{1}{a} : \dfrac{1}{b}$).

---

## 5. What is Proportion?

### The Atomic Truth

> A proportion is an **equation stating two ratios are equal**.

If $a : b = c : d$, we write:

$$a : b :: c : d \quad \text{or equivalently} \quad \frac{a}{b} = \frac{c}{d}$$

### Terminology

| Term | Name |
|------|------|
| $a$ | First proportional |
| $b$ | Second proportional |
| $c$ | Third proportional |
| $d$ | Fourth proportional |
| $a, d$ | **Extremes** (outer terms) |
| $b, c$ | **Means** (inner terms) |

### The Fundamental Rule of Proportion

$$a : b :: c : d \implies ad = bc$$

**Product of extremes = Product of means.**

**How does this formula come?**

Starting from:

$$\frac{a}{b} = \frac{c}{d}$$

Cross-multiply both sides by $bd$:

$$a \cdot d = b \cdot c$$

This is the single most important identity in proportion. Every other result flows from it.

**Example:** Are 2, 3, 8, 12 in proportion?

Check: $2 \times 12 = 24$ and $3 \times 8 = 24$. Yes, $24 = 24$. ✓

---

## 6. Properties of Proportion

Given $\dfrac{a}{b} = \dfrac{c}{d} = k$ (say), so $a = bk$ and $c = dk$.

### Property 1 — Invertendo

$$\frac{a}{b} = \frac{c}{d} \implies \frac{b}{a} = \frac{d}{c}$$

**Why?** Take the reciprocal of both sides.

### Property 2 — Alternendo

$$\frac{a}{b} = \frac{c}{d} \implies \frac{a}{c} = \frac{b}{d}$$

**Why?** From $ad = bc$, divide both sides by $cd$: $\dfrac{a}{c} = \dfrac{b}{d}$.

### Property 3 — Componendo

$$\frac{a}{b} = \frac{c}{d} \implies \frac{a + b}{b} = \frac{c + d}{d}$$

**Derivation:** Add 1 to both sides of $\dfrac{a}{b} = \dfrac{c}{d}$:

$$\frac{a}{b} + 1 = \frac{c}{d} + 1 \implies \frac{a + b}{b} = \frac{c + d}{d}$$

### Property 4 — Dividendo

$$\frac{a}{b} = \frac{c}{d} \implies \frac{a - b}{b} = \frac{c - d}{d}$$

**Derivation:** Subtract 1 from both sides.

### Property 5 — Componendo-Dividendo (The Crown Jewel)

$$\frac{a}{b} = \frac{c}{d} \implies \frac{a + b}{a - b} = \frac{c + d}{c - d}$$

**Full derivation in [Section 8](#8-componendo--dividendo-the-power-theorem).**

### Property 6 — Addendo

$$\frac{a}{b} = \frac{c}{d} \implies \frac{a + c}{b + d} = \frac{a}{b} = \frac{c}{d}$$

**Why?** Let $\dfrac{a}{b} = \dfrac{c}{d} = k$. Then $a = bk, c = dk$.

$$\frac{a + c}{b + d} = \frac{bk + dk}{b + d} = \frac{k(b + d)}{b + d} = k$$

### Property 7 — Subtrahendo

$$\frac{a}{b} = \frac{c}{d} \implies \frac{a - c}{b - d} = \frac{a}{b} = \frac{c}{d}$$

Same logic as addendo, using subtraction.

### Property 8 — General Form (Sum of Equal Ratios)

If $\dfrac{a_1}{b_1} = \dfrac{a_2}{b_2} = \cdots = \dfrac{a_n}{b_n} = k$, then:

$$k = \frac{a_1 + a_2 + \cdots + a_n}{b_1 + b_2 + \cdots + b_n}$$

This is the **generalized addendo** and is extremely powerful in competitive exams.

---

## 7. Types of Proportion

### 7.1 Continued Proportion

Three quantities $a, b, c$ are in continued proportion if:

$$\frac{a}{b} = \frac{b}{c}$$

This gives: $b^2 = ac \implies b = \sqrt{ac}$.

Here, $b$ is called the **mean proportional** (or geometric mean) of $a$ and $c$.

**Example:** Find the mean proportional of 4 and 16.

$$b = \sqrt{4 \times 16} = \sqrt{64} = 8$$

Check: $4 : 8 = 8 : 16 = 1 : 2$. ✓

### 7.2 Third Proportional

If $a : b = b : x$, then $x$ is the **third proportional** to $a$ and $b$.

$$x = \frac{b^2}{a}$$

**Derivation:** From $\dfrac{a}{b} = \dfrac{b}{x}$, cross-multiply: $ax = b^2 \implies x = \dfrac{b^2}{a}$.

**Example:** Third proportional to 3 and 6:

$$x = \frac{6^2}{3} = \frac{36}{3} = 12$$

Check: $3 : 6 = 6 : 12 = 1 : 2$. ✓

### 7.3 Fourth Proportional

If $a : b = c : x$, then $x$ is the **fourth proportional** to $a, b, c$.

$$x = \frac{bc}{a}$$

**Derivation:** From $\dfrac{a}{b} = \dfrac{c}{x}$, cross-multiply: $ax = bc \implies x = \dfrac{bc}{a}$.

**Example:** Fourth proportional to 2, 5, 6:

$$x = \frac{5 \times 6}{2} = 15$$

Check: $2 : 5 = 6 : 15$. $\dfrac{2}{5} = 0.4$, $\dfrac{6}{15} = 0.4$. ✓

---

## 8. Componendo & Dividendo (The Power Theorem)

### Why is this Important?

This single technique solves 30–40% of ratio-proportion problems in competitive exams. It converts complex expressions into simple ones in one step.

### The Theorem

If $\dfrac{a}{b} = \dfrac{c}{d}$, then:

$$\frac{a + b}{a - b} = \frac{c + d}{c - d}$$

### Complete Derivation

Start with $\dfrac{a}{b} = \dfrac{c}{d}$.

**Step 1 (Componendo):** Add 1 to both sides.

$$\frac{a}{b} + 1 = \frac{c}{d} + 1 \implies \frac{a + b}{b} = \frac{c + d}{d} \quad \cdots (1)$$

**Step 2 (Dividendo):** Subtract 1 from both sides.

$$\frac{a}{b} - 1 = \frac{c}{d} - 1 \implies \frac{a - b}{b} = \frac{c - d}{d} \quad \cdots (2)$$

**Step 3:** Divide equation (1) by equation (2).

$$\frac{(a + b)/b}{(a - b)/b} = \frac{(c + d)/d}{(c - d)/d}$$

The $b$'s cancel on the left, the $d$'s cancel on the right:

$$\boxed{\frac{a + b}{a - b} = \frac{c + d}{c - d}}$$

### When to Apply

Use Componendo-Dividendo when you see expressions of the form $\dfrac{\sqrt{x} + a}{\sqrt{x} - a}$ or any fraction where the numerator and denominator share a structure differing only by $+$ and $-$.

### Worked Example

**Problem:** If $\dfrac{\sqrt{x} + 3}{\sqrt{x} - 3} = \dfrac{5}{2}$, find $x$.

**Solution using C & D:**

By Componendo-Dividendo:

$$\frac{(\sqrt{x} + 3) + (\sqrt{x} - 3)}{(\sqrt{x} + 3) - (\sqrt{x} - 3)} = \frac{5 + 2}{5 - 2}$$

$$\frac{2\sqrt{x}}{6} = \frac{7}{3}$$

$$\frac{\sqrt{x}}{3} = \frac{7}{3} \implies \sqrt{x} = 7 \implies x = 49$$

**Verification:** $\dfrac{7 + 3}{7 - 3} = \dfrac{10}{4} = \dfrac{5}{2}$. ✓

---

## 9. k-Factor Method (The Universal Ratio Solver)

### The Idea

Whenever you see $A : B = m : n$, introduce a variable $k$ such that:

$$A = mk, \quad B = nk$$

Now every quantity is expressed in terms of a **single variable** $k$, and you can plug these into any equation.

### Why Does This Work?

$\dfrac{A}{B} = \dfrac{mk}{nk} = \dfrac{m}{n}$. The ratio is preserved regardless of $k$'s value.

### Example 1 — Basic

**Problem:** The ratio of ages of A and B is 4 : 7. If the sum of their ages is 55, find their ages.

**Solution:**

Let $A = 4k, B = 7k$.

$$4k + 7k = 55 \implies 11k = 55 \implies k = 5$$

$$A = 20, \quad B = 35$$

### Example 2 — With Three Quantities

**Problem:** A sum of ₹2400 is divided among A, B, C in the ratio 3 : 5 : 4. Find each share.

**Solution:**

Let shares be $3k, 5k, 4k$.

$$3k + 5k + 4k = 2400 \implies 12k = 2400 \implies k = 200$$

$$A = ₹600, \quad B = ₹1000, \quad C = ₹800$$

### Example 3 — With a Constraint

**Problem:** Two numbers are in the ratio 5 : 8. If 4 is added to each, the new ratio becomes 2 : 3. Find the numbers.

**Solution:**

Let numbers be $5k$ and $8k$.

$$\frac{5k + 4}{8k + 4} = \frac{2}{3}$$

Cross-multiply: $3(5k + 4) = 2(8k + 4)$

$15k + 12 = 16k + 8 \implies k = 4$

Numbers: $20$ and $32$.

**Verification:** $\dfrac{20 + 4}{32 + 4} = \dfrac{24}{36} = \dfrac{2}{3}$. ✓

---

## 10. Variation (Direct, Inverse, Joint)

### 10.1 Direct Variation (Direct Proportion)

$x$ is directly proportional to $y$ means:

$$x \propto y \implies x = Ky \quad (\text{for some constant } K > 0)$$

**Equivalently:** $\dfrac{x}{y} = K = \text{constant}$.

**If $y$ doubles, $x$ doubles.** The ratio stays fixed.

**Real-life analogy:** Distance and time at constant speed. If speed is 60 km/h, then $d = 60t$. Double the time, double the distance.

**Formula bridge:**

$$\frac{x_1}{y_1} = \frac{x_2}{y_2}$$

### 10.2 Inverse Variation (Inverse Proportion)

$x$ is inversely proportional to $y$ means:

$$x \propto \frac{1}{y} \implies xy = K = \text{constant}$$

**If $y$ doubles, $x$ halves.** The product stays fixed.

**Real-life analogy:** Speed and time for a fixed distance. $\text{Speed} \times \text{Time} = \text{Distance}$. Faster speed means less time.

**Formula bridge:**

$$x_1 \cdot y_1 = x_2 \cdot y_2$$

### 10.3 Joint Variation

$z$ varies jointly as $x$ and $y$:

$$z \propto xy \implies z = Kxy$$

**Example:** Area of a rectangle: $A = l \times w$. Area varies jointly with length and width.

### 10.4 Combined Variation

$z$ varies directly as $x$ and inversely as $y$:

$$z \propto \frac{x}{y} \implies z = K \cdot \frac{x}{y}$$

### Worked Example

**Problem:** If 15 workers can build a wall in 48 hours, how long will 20 workers take?

**Solution:** Workers and time are inversely proportional (more workers → less time).

$$w_1 \cdot t_1 = w_2 \cdot t_2$$

$$15 \times 48 = 20 \times t_2 \implies t_2 = \frac{720}{20} = 36 \text{ hours}$$

---

## 11. Mixture & Alligation

### 11.1 The Concept

Alligation is a technique to find the ratio in which two or more ingredients at different prices (or concentrations) must be mixed to produce a mixture at a given price (or concentration).

### 11.2 The Alligation Rule (with Derivation)

Suppose you mix two items:
- Item 1: cost/concentration = $C_1$ (cheaper)
- Item 2: cost/concentration = $C_2$ (dearer)
- Desired mixture: cost/concentration = $C_m$ (mean)

Where $C_1 < C_m < C_2$.

**The ratio of quantities:**

$$\frac{\text{Quantity of Cheaper}}{\text{Quantity of Dearer}} = \frac{C_2 - C_m}{C_m - C_1}$$

**How does this formula come?**

Let $q_1$ units of Item 1 and $q_2$ units of Item 2 be mixed.

Total cost/concentration of the mixture:

$$\frac{C_1 \cdot q_1 + C_2 \cdot q_2}{q_1 + q_2} = C_m$$

$$C_1 q_1 + C_2 q_2 = C_m q_1 + C_m q_2$$

$$C_1 q_1 - C_m q_1 = C_m q_2 - C_2 q_2$$

$$q_1(C_1 - C_m) = q_2(C_m - C_2)$$

$$\frac{q_1}{q_2} = \frac{C_m - C_2}{C_1 - C_m} = \frac{C_2 - C_m}{C_m - C_1}$$

(Signs flip because $C_1 < C_m < C_2$, making both numerator and denominator positive.)

### 11.3 The Alligation Cross (Visual Shortcut)

```
   C₁ (Cheaper)          C₂ (Dearer)
         \                 /
          \               /
           Cₘ (Mean)
          /               \
         /                 \
   (C₂ - Cₘ)          (Cₘ - C₁)

Ratio = (C₂ - Cₘ) : (Cₘ - C₁)
```

### Worked Example

**Problem:** In what ratio must rice costing ₹30/kg be mixed with rice costing ₹45/kg to get a mixture worth ₹36/kg?

**Solution:**

$C_1 = 30, \quad C_2 = 45, \quad C_m = 36$

$$\frac{q_1}{q_2} = \frac{C_2 - C_m}{C_m - C_1} = \frac{45 - 36}{36 - 30} = \frac{9}{6} = \frac{3}{2}$$

**Answer:** 3 : 2.

### 11.4 Replacement Problems (Serial Dilution)

**Scenario:** A container has $V$ litres of pure liquid. Each time, $R$ litres are removed and replaced with water. After $n$ operations:

$$\text{Quantity of pure liquid remaining} = V \left(1 - \frac{R}{V}\right)^n$$

**How does this formula come?**

After 1st operation: pure liquid left $= V - R = V\left(1 - \dfrac{R}{V}\right)$.

After 2nd operation: concentration is now $\dfrac{V - R}{V}$. When $R$ litres are removed, pure liquid removed $= R \cdot \dfrac{V - R}{V}$. Pure liquid left:

$$V\left(1 - \frac{R}{V}\right) - R \cdot \frac{V - R}{V} = (V - R)\left(1 - \frac{R}{V}\right) = V\left(1 - \frac{R}{V}\right)^2$$

By induction, after $n$ operations: $V\left(1 - \dfrac{R}{V}\right)^n$.

**Example:** A cask contains 80 litres of wine. 8 litres are drawn out and replaced with water. This is done 3 times. How much wine remains?

$$80 \left(1 - \frac{8}{80}\right)^3 = 80 \left(\frac{72}{80}\right)^3 = 80 \times \left(\frac{9}{10}\right)^3 = 80 \times \frac{729}{1000} = 58.32 \text{ litres}$$

---

## 12. Partnership (Ratio in Business)

### The Rule

When two or more partners invest capital for different time periods, profit is shared in the ratio of their **capital × time** products.

### Simple Partnership (Equal Time)

If A invests $C_A$ and B invests $C_B$ for the same duration:

$$\text{Profit ratio} = C_A : C_B$$

### Compound Partnership (Different Times)

If A invests $C_A$ for $t_A$ months and B invests $C_B$ for $t_B$ months:

$$\text{Profit ratio} = C_A \cdot t_A : C_B \cdot t_B$$

**Why?** The "effective investment" is money multiplied by time. ₹1000 for 12 months has the same weight as ₹12000 for 1 month.

### Worked Example

**Problem:** A starts a business with ₹50,000. After 3 months, B joins with ₹70,000. At the end of the year, the profit is ₹48,000. Find each person's share.

**Solution:**

A invests for 12 months, B invests for 9 months (12 − 3).

$$\text{Profit ratio} = 50000 \times 12 : 70000 \times 9 = 600000 : 630000 = 20 : 21$$

Total parts = $20 + 21 = 41$.

$$A = \frac{20}{41} \times 48000 ≈ ₹23,414.63$$

$$B = \frac{21}{41} \times 48000 ≈ ₹24,585.37$$

---

## 13. Solved Examples — Concept by Concept

### Example 1 — Combining Ratios

**Problem:** $A : B = 2 : 3$ and $B : C = 5 : 7$. Find $A : B : C$.

**Solution:** Make $B$ common.

$\text{LCM}(3, 5) = 15$.

$A : B = 2 : 3 = 10 : 15$

$B : C = 5 : 7 = 15 : 21$

$$A : B : C = 10 : 15 : 21$$

---

### Example 2 — Income and Expenditure

**Problem:** Incomes of A and B are in the ratio 5 : 4. Their expenditures are in the ratio 3 : 2. Each saves ₹2000. Find their incomes.

**Solution:**

Let incomes be $5k$ and $4k$. Let expenditures be $3m$ and $2m$.

Savings: Income − Expenditure.

$$5k - 3m = 2000 \quad \cdots (1)$$

$$4k - 2m = 2000 \quad \cdots (2)$$

From (2): $2k - m = 1000 \implies m = 2k - 1000$.

Substitute in (1): $5k - 3(2k - 1000) = 2000$

$5k - 6k + 3000 = 2000 \implies -k = -1000 \implies k = 1000$

Incomes: $A = ₹5000, \quad B = ₹4000$.

**Verification:** $m = 2(1000) - 1000 = 1000$. Expenditures: $3000$ and $2000$. Savings: $2000$ and $2000$. ✓

---

### Example 3 — Proportion with Square Roots

**Problem:** If $\dfrac{\sqrt{3a} + 2\sqrt{b}}{\sqrt{3a} - 2\sqrt{b}} = \dfrac{5}{1}$, find $\dfrac{a}{b}$.

**Solution:** Apply Componendo-Dividendo.

$$\frac{(\sqrt{3a} + 2\sqrt{b}) + (\sqrt{3a} - 2\sqrt{b})}{(\sqrt{3a} + 2\sqrt{b}) - (\sqrt{3a} - 2\sqrt{b})} = \frac{5 + 1}{5 - 1}$$

$$\frac{2\sqrt{3a}}{4\sqrt{b}} = \frac{6}{4} = \frac{3}{2}$$

$$\frac{\sqrt{3a}}{2\sqrt{b}} = \frac{3}{2}$$

$$\frac{\sqrt{3a}}{\sqrt{b}} = 3$$

Square both sides:

$$\frac{3a}{b} = 9 \implies \frac{a}{b} = 3$$

---

### Example 4 — Mean Proportional

**Problem:** Find two numbers whose mean proportional is 12 and third proportional is 96.

**Solution:**

Let the numbers be $a$ and $b$.

Mean proportional: $\sqrt{ab} = 12 \implies ab = 144 \quad \cdots (1)$

Third proportional to $a, b$ is $\dfrac{b^2}{a} = 96 \implies b^2 = 96a \quad \cdots (2)$

From (1): $a = \dfrac{144}{b}$. Substitute in (2):

$b^2 = 96 \cdot \dfrac{144}{b} \implies b^3 = 13824 \implies b = 24$

$a = \dfrac{144}{24} = 6$

**Answer:** 6 and 24.

**Check:** Mean proportional $= \sqrt{6 \times 24} = \sqrt{144} = 12$. ✓ Third proportional $= \dfrac{24^2}{6} = \dfrac{576}{6} = 96$. ✓

---

### Example 5 — Alligation with Percentages

**Problem:** How many litres of a 30% acid solution must be added to 40 litres of a 12% acid solution to make a 20% acid solution?

**Solution:**

Using alligation:

$C_1 = 12\%, \quad C_2 = 30\%, \quad C_m = 20\%$

$$\frac{q_1}{q_2} = \frac{C_2 - C_m}{C_m - C_1} = \frac{30 - 20}{20 - 12} = \frac{10}{8} = \frac{5}{4}$$

We have $q_1 = 40$ litres of the 12% solution.

$$\frac{40}{q_2} = \frac{5}{4} \implies q_2 = \frac{40 \times 4}{5} = 32 \text{ litres}$$

---

### Example 6 — Partnership with Changing Capital

**Problem:** A starts a business with ₹10,000. After 4 months, B joins with ₹15,000. After 2 more months, A withdraws ₹5000. At the end of the year, total profit is ₹25,500. Find each share.

**Solution:**

A: ₹10,000 for 6 months + ₹5,000 for 6 months $= 60000 + 30000 = 90000$

B: ₹15,000 for 8 months $= 120000$

Ratio $= 90000 : 120000 = 3 : 4$

$$A = \frac{3}{7} \times 25500 = ₹10,928.57$$

$$B = \frac{4}{7} \times 25500 = ₹14,571.43$$

---

### Example 7 — Serial Replacement

**Problem:** A vessel contains 60 litres of milk. 12 litres are drawn and replaced with water. This is done twice. Find the ratio of milk to water.

**Solution:**

Milk after 2 operations:

$$60 \left(1 - \frac{12}{60}\right)^2 = 60 \times \left(\frac{4}{5}\right)^2 = 60 \times \frac{16}{25} = 38.4 \text{ litres}$$

Water $= 60 - 38.4 = 21.6$ litres.

Milk : Water $= 38.4 : 21.6 = 384 : 216 = 16 : 9$.

---

## 14. Tricks & Shortcuts for Competitive Exams

### Trick 1 — The k-Method (Always the First Move)

When given a ratio $a : b = m : n$, immediately write $a = mk, b = nk$. This single substitution solves 80% of problems.

### Trick 2 — Direct Division via Ratio

To divide a quantity $Q$ in the ratio $a : b : c$:

$$\text{Share of first} = \frac{a}{a + b + c} \times Q$$

No need to find $k$. Just compute the fraction directly.

**Example:** Divide 360 in ratio 2 : 3 : 4.

Shares: $\dfrac{2}{9} \times 360 = 80$, $\dfrac{3}{9} \times 360 = 120$, $\dfrac{4}{9} \times 360 = 160$.

### Trick 3 — Componendo-Dividendo One-Step

Whenever you see $\dfrac{a + b}{a - b}$, think "C & D can probably be applied backwards to extract the original ratio."

### Trick 4 — Successive Ratio Change

If a ratio $a : b$ changes to $c : d$ by adding/subtracting a value $x$, set up:

$$\frac{a \cdot k \pm x}{b \cdot k \pm x} = \frac{c}{d}$$

Cross-multiply and solve for $k$. Then compute the original values.

### Trick 5 — Quick Alligation Cross

Draw the cross diagram. Subtract diagonally from the mean. The answer is the ratio of these differences. Takes 5 seconds.

### Trick 6 — For Bank Exams — Percentage to Ratio

$25\% = \dfrac{1}{4}$, so "25% more" means new ratio $= 5 : 4$ compared to old.

$33.\overline{3}\% = \dfrac{1}{3}$, so "33.33% less" means new ratio $= 2 : 3$ compared to old.

Memorize these fraction-percentage equivalences for speed.

### Trick 7 — Equal Ratio Chain

If $\dfrac{a}{b} = \dfrac{c}{d} = \dfrac{e}{f}$, then each equals $\dfrac{a + c + e}{b + d + f}$.

Use this to immediately find the value when you know one such sum.

### Trick 8 — Using Ratios to Avoid Quadratics

Many problems that appear to need quadratic equations can be solved faster by just using ratio properties and the k-method, avoiding the quadratic formula entirely.

---

## 15. Common Traps & Edge Cases

### Trap 1 — Ratio ≠ Absolute Value

$A : B = 3 : 4$ does **not** mean $A = 3, B = 4$. It means $A = 3k, B = 4k$ for some $k > 0$.

### Trap 2 — Adding the Same Quantity Changes the Ratio

If $A : B = 2 : 5$, and you add 10 to both, the ratio becomes $\dfrac{2k + 10}{5k + 10}$, which is **not** $2 : 5$ (unless $k \to \infty$).

Adding a positive number to both terms makes the ratio **closer to 1 : 1**. Subtracting moves it **further from 1 : 1** (or reverses it).

### Trap 3 — Ratios with Negative Numbers

Normally ratios deal with positive quantities. But if allowed, $(-2) : 4 = (-1) : 2$. Be careful with signs in cross-multiplication.

### Trap 4 — Misusing Componendo-Dividendo

C & D requires $a - b \neq 0$ and $c - d \neq 0$. If $a = b$, the denominator is zero and the formula fails.

### Trap 5 — Confusing "Ratio of Increase" with "New Ratio"

"A's salary increases by 20%" means the **new** value is $1.2A$, not that the ratio of increase is $20 : 100$.

If old ratio was $A : B = 5 : 4$ and A gets a 20% raise:

New $A = 1.2 \times 5k = 6k$, B stays $4k$. New ratio = $6 : 4 = 3 : 2$.

### Trap 6 — Alligation: Mean Must Be Between the Two Values

If $C_m$ is not between $C_1$ and $C_2$, the mixture is impossible (you would need a negative quantity of one ingredient).

### Trap 7 — Replacement Formula Assumes Well-Mixed

The serial dilution formula $V\left(1 - \dfrac{R}{V}\right)^n$ assumes the mixture is perfectly homogeneous before each withdrawal. This is stated in most exam problems but watch for problems that violate this.

### Trap 8 — Unit Conversion in Ratios

$A : B = 2 \text{ kg} : 500 \text{ g}$. You must convert to the same unit first:

$2 \text{ kg} = 2000 \text{ g}$, so ratio $= 2000 : 500 = 4 : 1$.

### Edge Case — Ratio with Zero

$0 : 5$ is valid (it equals 0). But $5 : 0$ is **undefined** (division by zero).

### Edge Case — Three Quantity Ratios When One Is Zero

$A : B : C = 3 : 0 : 5$ means B is zero. This is mathematically valid but check whether the problem context allows it.

---

## 16. Practice Problems (with Answers)

### Problem 1

If $\dfrac{x}{y} = \dfrac{3}{4}$, find $\dfrac{4x + 5y}{5x - 2y}$.

**Solution:**

Let $x = 3k, y = 4k$.

$$\frac{4(3k) + 5(4k)}{5(3k) - 2(4k)} = \frac{12k + 20k}{15k - 8k} = \frac{32k}{7k} = \frac{32}{7}$$

---

### Problem 2

If $a : b = 5 : 9$ and $b : c = 4 : 7$, find $a : b : c$.

**Solution:**

$\text{LCM}(9, 4) = 36$.

$a : b = 5 : 9 = 20 : 36$

$b : c = 4 : 7 = 36 : 63$

$$a : b : c = 20 : 36 : 63$$

---

### Problem 3

Divide ₹7200 among A, B, C such that A's share is twice B's share and B's share is thrice C's share.

**Solution:**

$B = 3C$, $A = 2B = 6C$.

$A : B : C = 6 : 3 : 1$. Total parts = 10.

$C = \dfrac{1}{10} \times 7200 = ₹720$, $B = ₹2160$, $A = ₹4320$.

---

### Problem 4

The present ages of A and B are in the ratio 5 : 6. After 8 years, their ages will be in the ratio 7 : 8. Find their present ages.

**Solution:**

$A = 5k, B = 6k$.

$$\frac{5k + 8}{6k + 8} = \frac{7}{8}$$

$8(5k + 8) = 7(6k + 8)$

$40k + 64 = 42k + 56 \implies 2k = 8 \implies k = 4$

$A = 20 \text{ years}, \quad B = 24 \text{ years}$.

---

### Problem 5

A mixture of milk and water in the ratio 5 : 1 weighs 78 kg. How much water must be added to make the ratio 3 : 1?

**Solution:**

Milk $= \dfrac{5}{6} \times 78 = 65$ kg, Water $= \dfrac{1}{6} \times 78 = 13$ kg.

Let $x$ kg water be added.

$$\frac{65}{13 + x} = \frac{3}{1} \implies 65 = 3(13 + x) = 39 + 3x \implies 3x = 26 \implies x = \frac{26}{3} \approx 8.67 \text{ kg}$$

---

### Problem 6

A bag contains ₹1, ₹2, and ₹5 coins in the ratio 3 : 5 : 4. If the total amount is ₹264, find the number of each type of coin.

**Solution:**

Number of coins: $3k, 5k, 4k$.

Total amount: $1(3k) + 2(5k) + 5(4k) = 3k + 10k + 20k = 33k = 264$

$k = 8$

Coins: ₹1 → 24, ₹2 → 40, ₹5 → 32.

**Verification:** $24 + 80 + 160 = 264$. ✓

---

### Problem 7

In a mixture of 45 litres, the ratio of milk to water is 4 : 1. How much water must be added to make the ratio 3 : 2?

**Solution:**

Milk $= \dfrac{4}{5} \times 45 = 36$ litres, Water $= \dfrac{1}{5} \times 45 = 9$ litres.

Let $x$ litres water be added.

$$\frac{36}{9 + x} = \frac{3}{2} \implies 72 = 3(9 + x) = 27 + 3x \implies 3x = 45 \implies x = 15$$

---

### Problem 8

If $\dfrac{a}{3} = \dfrac{b}{4} = \dfrac{c}{7}$, find $\dfrac{a + b + c}{c}$.

**Solution:**

Let each ratio $= k$. Then $a = 3k, b = 4k, c = 7k$.

$$\frac{a + b + c}{c} = \frac{3k + 4k + 7k}{7k} = \frac{14k}{7k} = 2$$

---

### Problem 9

A, B, C enter into a partnership. A invests 3 times as much as B and B invests two-thirds of what C invests. If the total profit is ₹66,000, find B's share.

**Solution:**

Let $C = x$. Then $B = \dfrac{2}{3}x$ and $A = 3B = 2x$.

$A : B : C = 2x : \dfrac{2}{3}x : x = 6 : 2 : 3$

$B = \dfrac{2}{11} \times 66000 = ₹12,000$

---

### Problem 10

The salaries of A, B, C are in the ratio 1 : 2 : 3. If the salary of B and C together is ₹6000 more than that of A, find each salary.

**Solution:**

$A = k, B = 2k, C = 3k$.

$(2k + 3k) - k = 6000 \implies 4k = 6000 \implies k = 1500$

$A = ₹1500, \quad B = ₹3000, \quad C = ₹4500$

---

## Quick Reference Card

| Concept | Formula | When to Use |
|---------|---------|-------------|
| Ratio | $a : b = \dfrac{a}{b}$ | Comparing two quantities |
| Proportion | $ad = bc$ | Verifying / solving proportions |
| Mean Proportional | $b = \sqrt{ac}$ | Finding middle term in continued proportion |
| Third Proportional | $x = \dfrac{b^2}{a}$ | $a : b = b : x$ |
| Fourth Proportional | $x = \dfrac{bc}{a}$ | $a : b = c : x$ |
| Componendo-Dividendo | $\dfrac{a+b}{a-b} = \dfrac{c+d}{c-d}$ | Expressions with $\pm$ structure |
| Direct Variation | $\dfrac{x_1}{y_1} = \dfrac{x_2}{y_2}$ | One increases, other increases proportionally |
| Inverse Variation | $x_1 y_1 = x_2 y_2$ | One increases, other decreases proportionally |
| Alligation | $\dfrac{q_1}{q_2} = \dfrac{C_2 - C_m}{C_m - C_1}$ | Mixing two items at a desired mean |
| Replacement | $V\!\left(1 - \dfrac{R}{V}\right)^n$ | Serial dilution / replacement |
| Partnership | $C_1 t_1 : C_2 t_2$ | Profit sharing with different investments/times |

---

> **Final Tip:** In any competitive exam, if a ratio-proportion question looks complex, always start with the **k-method**. Express every quantity in terms of $k$, form equations, and solve. It works universally.

---

*Study Material for GATE / ESE / PSU / Bank Examinations — Ratio & Proportion (Complete)*
