# Percentage — Complete A-Z Study Material

> **Target Exams:** GATE · ESE · PSU · Banking Exams (SSC CGL, IBPS, SBI, RBI)
> **Objective:** Master every concept, trick, and edge case so that no percentage question can surprise you.

---

## Table of Contents

1. [What is a Percentage?](#1-what-is-a-percentage)
2. [Where Does the Formula Come From?](#2-where-does-the-formula-come-from)
3. [Fraction ↔ Percentage Conversion Table](#3-fraction--percentage-conversion-table)
4. [Core Operations](#4-core-operations)
5. [Percentage Change (Increase / Decrease)](#5-percentage-change-increase--decrease)
6. [Successive Percentage Changes](#6-successive-percentage-changes)
7. [Reverse Percentage (Finding the Original)](#7-reverse-percentage-finding-the-original)
8. [Percentage Comparison — "A is what % more/less than B"](#8-percentage-comparison--a-is-what--moreless-than-b)
9. [Population Growth & Depreciation (Compound Application)](#9-population-growth--depreciation-compound-application)
10. [Profit, Loss & Discount — Percentage Bridge](#10-profit-loss--discount--percentage-bridge)
11. [Elections & Voting](#11-elections--voting)
12. [Mixture & Alligation with Percentages](#12-mixture--alligation-with-percentages)
13. [Data Interpretation — Percentage in Tables & Charts](#13-data-interpretation--percentage-in-tables--charts)
14. [Exam-Specific Patterns & Shortcuts](#14-exam-specific-patterns--shortcuts)
15. [Edge Cases & Common Traps](#15-edge-cases--common-traps)
16. [Practice Problem Bank with Solutions](#16-practice-problem-bank-with-solutions)
17. [Quick-Revision Cheat Sheet](#17-quick-revision-cheat-sheet)

---

## 1. What is a Percentage?

**The Atomic Truth:** *A fraction with denominator 100.*

**Why do we need it?**

Imagine comparing two cricket batsmen:
- Batsman A scored 45 out of 60.
- Batsman B scored 38 out of 50.

Who performed better? You cannot compare directly because the bases (60 and 50) are different. Percentage **normalises everything to a common base of 100**, making comparison instant.

- A: (45/60) × 100 = 75%
- B: (38/50) × 100 = 76%

Batsman B is better — something not obvious without percentages.

**Formal Definition:**

$$
\text{Percentage} = \frac{\text{Part}}{\text{Whole}} \times 100
$$

The word comes from Latin *per centum* — "for every hundred."

**Analogy — The Universal Translator:**
Think of percentage as a universal currency converter. Just as you convert rupees, dollars, and euros into one currency to compare prices, you convert fractions with different denominators into a single system (base 100) to compare quantities.

---

## 2. Where Does the Formula Come From?

### 2.1 Deriving "x% of y"

Start from the meaning: *x percent* = *x per hundred* = x/100.

So "x% of y" literally means "x parts out of every 100 parts of y":

$$
x\% \text{ of } y = \frac{x}{100} \times y
$$

**Example:** 20% of 350
$$
= \frac{20}{100} \times 350 = \frac{1}{5} \times 350 = 70
$$

### 2.2 Deriving "What percentage is A of B?"

We need to find a number $p$ such that:
$$
p\% \text{ of } B = A
$$
$$
\frac{p}{100} \times B = A
$$
$$
p = \frac{A}{B} \times 100
$$

**Example:** What percentage is 45 of 180?
$$
p = \frac{45}{180} \times 100 = \frac{1}{4} \times 100 = 25\%
$$

### 2.3 Deriving "Percentage Change"

If a quantity goes from **Old** to **New**:

$$
\text{Change} = \text{New} - \text{Old}
$$
$$
\text{Percentage Change} = \frac{\text{Change}}{\text{Old}} \times 100 = \frac{\text{New} - \text{Old}}{\text{Old}} \times 100
$$

**Why divide by Old (not New)?** Because we measure *how much it changed relative to where it started*. The starting point is the reference — just like speed is measured relative to the starting position.

---

## 3. Fraction ↔ Percentage Conversion Table

Memorise these — they are the **speed multipliers** for competitive exams.

| Fraction | Percentage | Fraction | Percentage |
|----------|-----------|----------|-----------|
| 1/2 | 50% | 1/9 | 11.11% |
| 1/3 | 33.33% | 1/10 | 10% |
| 2/3 | 66.67% | 1/11 | 9.09% |
| 1/4 | 25% | 1/12 | 8.33% |
| 3/4 | 75% | 1/13 | 7.69% |
| 1/5 | 20% | 1/14 | 7.14% |
| 2/5 | 40% | 1/15 | 6.67% |
| 3/5 | 60% | 1/16 | 6.25% |
| 4/5 | 80% | 1/20 | 5% |
| 1/6 | 16.67% | 1/25 | 4% |
| 5/6 | 83.33% | 1/50 | 2% |
| 1/7 | 14.28% | 1/100 | 1% |
| 1/8 | 12.5% | 2/7 | 28.57% |

**Trick to remember 1/7 family:**

1/7 = 14.2857... — the cycle **142857** repeats.
- 2/7 = 28.5714...
- 3/7 = 42.8571...

All six cyclic permutations of **142857**.

**Trick for 1/11 family:** Multiply by 9.09:
- 2/11 = 18.18%, 3/11 = 27.27%, ... each step adds 9.09.

---

## 4. Core Operations

### 4.1 Finding x% of a Number

$$
x\% \text{ of } N = \frac{x}{100} \times N
$$

**Speed Technique — Break & Combine:**

Find 17.5% of 400:
- 10% of 400 = 40
- 5% of 400 = 20 (half of 10%)
- 2.5% of 400 = 10 (half of 5%)
- 17.5% = 40 + 20 + 10 = **70**

**Why this works:** Percentage is a linear operator — $a\%$ of $N$ + $b\%$ of $N$ = $(a+b)\%$ of $N$. You can decompose any percentage into powers-of-two-like chunks of 10%, 5%, 2.5%, 1%.

### 4.2 Finding the Whole When a Part is Given

If $x\%$ of some number = $A$, find the number.

$$
\text{Number} = \frac{A \times 100}{x} = \frac{A}{x} \times 100
$$

**Example:** 35% of a number is 280. Find the number.
$$
\text{Number} = \frac{280}{35} \times 100 = 8 \times 100 = 800
$$

### 4.3 What Percentage is A of B?

$$
\frac{A}{B} \times 100\%
$$

**Example:** Express 64 as a percentage of 256.
$$
\frac{64}{256} \times 100 = \frac{1}{4} \times 100 = 25\%
$$

---

## 5. Percentage Change (Increase / Decrease)

### 5.1 Absolute Formula

$$
\%\ \text{Change} = \frac{\text{New} - \text{Old}}{\text{Old}} \times 100
$$

- Positive result → **Increase**
- Negative result → **Decrease**

**Example:** A shirt's price goes from ₹800 to ₹920.
$$
\%\ \text{Increase} = \frac{920 - 800}{800} \times 100 = \frac{120}{800} \times 100 = 15\%
$$

### 5.2 Multiplier Method (The Power Technique)

Instead of calculating change, convert the percentage directly into a **multiplier**:

| Scenario | Multiplier |
|----------|-----------|
| Increase by $x\%$ | $\times\left(1 + \frac{x}{100}\right)$ |
| Decrease by $x\%$ | $\times\left(1 - \frac{x}{100}\right)$ |

**Example:** Increase 500 by 20%.
$$
500 \times 1.20 = 600
$$

Decrease 500 by 20%.
$$
500 \times 0.80 = 400
$$

**Why use multipliers?** When multiple percentage changes are applied in sequence (successive changes), multipliers chain together by multiplication — far faster than computing each change separately.

### 5.3 Fraction Shortcut for Common Changes

| Change | Fraction Multiplier |
|--------|-------------------|
| +10% | × 11/10 |
| −10% | × 9/10 |
| +20% | × 6/5 |
| −20% | × 4/5 |
| +25% | × 5/4 |
| −25% | × 3/4 |
| +33.33% | × 4/3 |
| −33.33% | × 2/3 |
| +50% | × 3/2 |
| −50% | × 1/2 |

---

## 6. Successive Percentage Changes

### 6.1 The Problem

If a quantity increases by $a\%$ and then by $b\%$, what is the **net single percentage change**?

### 6.2 Derivation

Let original value = 100.

After $a\%$ increase: $100 \times \left(1 + \frac{a}{100}\right)$

After another $b\%$ increase on the new value:
$$
100 \times \left(1 + \frac{a}{100}\right)\left(1 + \frac{b}{100}\right)
$$

Expand:
$$
= 100\left[1 + \frac{a}{100} + \frac{b}{100} + \frac{ab}{10000}\right]
$$

Net change from 100:
$$
= a + b + \frac{ab}{100}
$$

$$
\boxed{\text{Net Change} = a + b + \frac{ab}{100}\ \%}
$$

### 6.3 Intuition — Why the Extra Term?

When you increase by $a\%$ first, the base itself grows. The second increase $b\%$ acts on this **enlarged base**. The extra term $\frac{ab}{100}$ captures the "interest on interest" — the percentage of the percentage.

**Analogy:** Think of painting a wall. First coat covers area $a$. Second coat covers area $b$ on the original wall PLUS a thin overlap on the area $a$ already painted. That overlap is $\frac{ab}{100}$.

### 6.4 Worked Examples

**Example 1:** A price increases by 20% then decreases by 10%.
$$
\text{Net} = 20 + (-10) + \frac{20 \times (-10)}{100} = 10 - 2 = 8\%\ \text{increase}
$$

**Example 2 (Trap):** Increase by 25% then decrease by 20%. Is the net change +5%? Let's check.
$$
\text{Net} = 25 + (-20) + \frac{25 \times (-20)}{100} = 5 - 5 = 0\%
$$

No change at all! This is because 25% up = ×5/4, then 20% down = ×4/5, and (5/4)(4/5) = 1.

**Example 3:** Two successive discounts of 20% and 30%.
$$
\text{Net discount} = -20 + (-30) + \frac{(-20)(-30)}{100} = -50 + 6 = -44\%
$$

Effective discount is 44%, not 50%.

### 6.5 Three or More Successive Changes

For three changes $a\%$, $b\%$, $c\%$:
1. First combine $a$ and $b$ using the formula to get a net change $d$.
2. Then combine $d$ and $c$.

Or use the multiplier approach directly:

$$
\text{Final} = \text{Original} \times \left(1+\frac{a}{100}\right)\left(1+\frac{b}{100}\right)\left(1+\frac{c}{100}\right)
$$

---

## 7. Reverse Percentage (Finding the Original)

### 7.1 The Concept

"After a 20% increase, the new value is 600. Find the original."

**Common Mistake:** Taking 20% of 600 and subtracting → 600 − 120 = 480. ❌

**Why is this wrong?** The 20% was applied on the **original**, not on 600. You are removing 20% of the wrong base.

### 7.2 The Correct Approach

$$
\text{Original} \times 1.20 = 600
$$
$$
\text{Original} = \frac{600}{1.20} = 500
$$

**General Rule:**

$$
\text{Original} = \frac{\text{New Value}}{\text{Multiplier}}
$$

### 7.3 Worked Examples

**Example 1:** After a 25% discount, a TV costs ₹9,000. What was the original price?

Multiplier for 25% decrease = 0.75
$$
\text{Original} = \frac{9000}{0.75} = 12000
$$

**Example 2:** After two successive increases of 10% and 20%, the population becomes 66,000. Find original.
$$
\text{Multiplier} = 1.10 \times 1.20 = 1.32
$$
$$
\text{Original} = \frac{66000}{1.32} = 50000
$$

**Example 3:** A number is first increased by 20% and then decreased by $x\%$, giving back the original. Find $x$.

$$
\left(1 + \frac{20}{100}\right)\left(1 - \frac{x}{100}\right) = 1
$$
$$
1.20 \times \left(1 - \frac{x}{100}\right) = 1
$$
$$
1 - \frac{x}{100} = \frac{1}{1.20} = \frac{5}{6}
$$
$$
\frac{x}{100} = \frac{1}{6} \implies x = 16.\overline{6}\%
$$

### 7.4 The Reversal Pairs (Must Memorise)

If you increase by $x\%$, the decrease needed to return to original:

| Increase | Required Decrease |
|----------|------------------|
| 10% | 9.09% (1/11) |
| 20% | 16.67% (1/6) |
| 25% | 20% (1/5) |
| 33.33% | 25% (1/4) |
| 50% | 33.33% (1/3) |
| 100% | 50% (1/2) |

**Pattern:** If increase = $\frac{n}{d}$, then the decrease = $\frac{n}{d+n}$.

**Why?** If the multiplier up is $\frac{d+n}{d}$, the multiplier down must be $\frac{d}{d+n}$, which is a decrease of $\frac{n}{d+n}$.

---

## 8. Percentage Comparison — "A is what % more/less than B"

### 8.1 The Formula

"$A$ is what percent more than $B$?" → The **base** is $B$.

$$
\frac{A - B}{B} \times 100\%
$$

"$A$ is what percent less than $B$?" → Same formula, result will be negative (or use $\frac{B-A}{B}\times100$).

### 8.2 The Critical Trap

> "A is 25% more than B" does **NOT** mean "B is 25% less than A."

**Proof:** Let $B = 100$. Then $A = 125$.

$A$ is 25% more than $B$: $\frac{125-100}{100} \times 100 = 25\%$ ✓

$B$ is what % less than $A$: $\frac{125-100}{125} \times 100 = 20\%$

The base changes! When comparing A to B, the base is B. When comparing B to A, the base is A.

### 8.3 Shortcut

If $A$ is $x\%$ more than $B$, then $B$ is less than $A$ by:

$$
\frac{x}{100+x} \times 100\%
$$

If $A$ is $x\%$ less than $B$, then $B$ is more than $A$ by:

$$
\frac{x}{100-x} \times 100\%
$$

**Example:** If A's salary is 20% more than B's, then B's salary is less than A's by:
$$
\frac{20}{120} \times 100 = 16.67\%
$$

### 8.4 Three-Way Comparison

If $A$ is 20% more than $B$, and $B$ is 30% more than $C$, then $A$ as a percentage of $C$:

$$
A = 1.20 \times B = 1.20 \times 1.30 \times C = 1.56C
$$

So $A$ is 56% more than $C$.

---

## 9. Population Growth & Depreciation (Compound Application)

### 9.1 Compound Growth Formula

$$
P_n = P_0 \left(1 + \frac{r}{100}\right)^n
$$

Where:
- $P_0$ = initial population/value
- $r$ = rate of growth per period (use negative $r$ for depreciation)
- $n$ = number of periods
- $P_n$ = population/value after $n$ periods

### 9.2 Derivation

Year 1: $P_1 = P_0 + P_0 \times \frac{r}{100} = P_0\left(1+\frac{r}{100}\right)$

Year 2: $P_2 = P_1\left(1+\frac{r}{100}\right) = P_0\left(1+\frac{r}{100}\right)^2$

By induction, after $n$ years: $P_n = P_0\left(1+\frac{r}{100}\right)^n$

This is identical to compound interest because the **percentage acts on the new accumulated base each period**, not the original.

### 9.3 Depreciation

A machine loses value at $r\%$ per year:

$$
V_n = V_0\left(1 - \frac{r}{100}\right)^n
$$

**Example:** A car worth ₹5,00,000 depreciates at 15% per year. Value after 3 years:
$$
V_3 = 500000 \times (0.85)^3 = 500000 \times 0.614125 = ₹3,07,062.50
$$

### 9.4 Different Rates in Different Years

If the rate is $r_1\%$ in year 1, $r_2\%$ in year 2, $r_3\%$ in year 3:
$$
P_3 = P_0\left(1+\frac{r_1}{100}\right)\left(1+\frac{r_2}{100}\right)\left(1+\frac{r_3}{100}\right)
$$

**Example:** Population 10,000 grows by 10% in year 1, 20% in year 2, decreases by 5% in year 3.
$$
P_3 = 10000 \times 1.10 \times 1.20 \times 0.95 = 10000 \times 1.254 = 12540
$$

### 9.5 Finding Rate or Time

**Finding rate:** $P_n$ and $P_0$ known, $n$ known.
$$
\left(1+\frac{r}{100}\right)^n = \frac{P_n}{P_0} \implies 1+\frac{r}{100} = \left(\frac{P_n}{P_0}\right)^{1/n}
$$

**Finding time:** Use logarithms or trial with common values in exam context.

**Exam Shortcut (Doubling Time):**

At $r\%$ growth, the quantity doubles in approximately $\frac{72}{r}$ years. (Rule of 72)

- At 10%: doubles in ≈ 7.2 years
- At 12%: doubles in ≈ 6 years

---

## 10. Profit, Loss & Discount — Percentage Bridge

### 10.1 Core Definitions

| Term | Formula |
|------|---------|
| Profit % | $\frac{\text{SP} - \text{CP}}{\text{CP}} \times 100$ |
| Loss % | $\frac{\text{CP} - \text{SP}}{\text{CP}} \times 100$ |
| Discount % | $\frac{\text{MP} - \text{SP}}{\text{MP}} \times 100$ |

Where CP = Cost Price, SP = Selling Price, MP = Marked Price.

**Key insight:** Profit/Loss % is always on **CP**. Discount % is always on **MP**. Never mix the bases.

### 10.2 Multiplier Chain

$$
\text{CP} \xrightarrow{\text{Markup}} \text{MP} \xrightarrow{\text{Discount}} \text{SP}
$$

$$
\text{SP} = \text{CP} \times \left(1 + \frac{\text{Markup}\%}{100}\right) \times \left(1 - \frac{\text{Discount}\%}{100}\right)
$$

$$
\text{Net Profit/Loss Factor} = \left(1 + \frac{m}{100}\right)\left(1 - \frac{d}{100}\right)
$$

If the result > 1 → profit. If < 1 → loss.

**Example:** An item is marked up 40% above CP and then a 25% discount is offered.
$$
\text{Factor} = 1.40 \times 0.75 = 1.05
$$
Net profit = 5%.

### 10.3 Successive Discounts

Two discounts of $d_1\%$ and $d_2\%$:
$$
\text{Effective SP} = \text{MP} \times \left(1 - \frac{d_1}{100}\right)\left(1 - \frac{d_2}{100}\right)
$$

Single equivalent discount:
$$
d_{\text{eq}} = d_1 + d_2 - \frac{d_1 \times d_2}{100}
$$

**Example:** Successive discounts of 20% and 10%.
$$
d_{\text{eq}} = 20 + 10 - \frac{200}{100} = 28\%
$$

Not 30% — a classic exam trap.

### 10.4 False Weight / Cheating Shopkeeper

A shopkeeper uses a weight of $w$ grams instead of 1000 grams.
$$
\text{Profit}\% = \frac{1000 - w}{w} \times 100
$$

**Example:** A shopkeeper uses 800 g instead of 1 kg.
$$
\text{Profit}\% = \frac{200}{800} \times 100 = 25\%
$$

---

## 11. Elections & Voting

### 11.1 Standard Election Problem

Two candidates. Winner gets $x\%$ of total votes. Winning margin = $M$ votes.

$$
\text{Winner votes} = x\% \text{ of Total}
$$
$$
\text{Loser votes} = (100-x)\% \text{ of Total}
$$
$$
\text{Margin} = (2x - 100)\% \text{ of Total} = M
$$
$$
\text{Total Votes} = \frac{M \times 100}{2x - 100}
$$

**Example:** A wins with 60% of votes. Winning margin = 1200 votes.
$$
\text{Total} = \frac{1200 \times 100}{2(60) - 100} = \frac{120000}{20} = 6000
$$

### 11.2 With Invalid / Spoilt Votes

If $s\%$ of total votes are invalid:
$$
\text{Valid votes} = (100-s)\% \text{ of Total Votes Cast}
$$

Then apply the winner's percentage on **valid votes**, not total.

**Example:** 80,000 votes cast. 20% invalid. Winner gets 65% of valid votes.
- Valid = 80,000 × 0.80 = 64,000
- Winner = 64,000 × 0.65 = 41,600
- Loser = 64,000 × 0.35 = 22,400
- Margin = 19,200

---

## 12. Mixture & Alligation with Percentages

### 12.1 Basic Mixture Problem

A solution has $x\%$ concentration. If you add pure substance or solvent, how does the percentage change?

**Key Principle:** Amount of pure substance = Concentration% × Total Volume.

**Example:** 50 litres of 30% salt solution. How much salt to add to make it 40%?

Salt currently = 50 × 0.30 = 15 litres.
Let $s$ litres of salt be added.

$$
\frac{15 + s}{50 + s} = 0.40
$$
$$
15 + s = 20 + 0.4s
$$
$$
0.6s = 5 \implies s = 8.33 \text{ litres}
$$

### 12.2 Replacement Formula

If a container has $V$ litres of pure liquid and $x$ litres are removed and replaced with water, repeated $n$ times:

$$
\text{Pure liquid remaining} = V\left(1 - \frac{x}{V}\right)^n
$$

**Concentration after $n$ operations:**
$$
\text{Concentration} = \left(1 - \frac{x}{V}\right)^n \times 100\%
$$

**Example:** A 20-litre container of milk. 4 litres removed and replaced with water, done 3 times.
$$
\text{Milk remaining} = 20\left(1 - \frac{4}{20}\right)^3 = 20\left(\frac{4}{5}\right)^3 = 20 \times 0.512 = 10.24 \text{ litres}
$$
$$
\text{Concentration} = \frac{10.24}{20} \times 100 = 51.2\%
$$

### 12.3 Alligation Rule

When mixing two solutions of concentrations $c_1$ and $c_2$ to get concentration $c_m$:

$$
\frac{Q_1}{Q_2} = \frac{c_2 - c_m}{c_m - c_1}
$$

where $Q_1$, $Q_2$ are the quantities of the two solutions.

**Visual Representation:**
```
    c₁                c₂
      \              /
       \            /
         c_m (mean)
       /            \
      /              \
 (c₂ - c_m)    (c_m - c₁)
```

The ratio of quantities = ratio of differences from the mean, **cross-wise**.

---

## 13. Data Interpretation — Percentage in Tables & Charts

### 13.1 Percentage Share

$$
\text{Share of } A = \frac{\text{Value of } A}{\text{Total}} \times 100\%
$$

### 13.2 Year-on-Year (YoY) Growth

$$
\text{YoY Growth} = \frac{\text{Value}_{\text{current}} - \text{Value}_{\text{previous}}}{\text{Value}_{\text{previous}}} \times 100\%
$$

### 13.3 CAGR (Compound Annual Growth Rate)

$$
\text{CAGR} = \left[\left(\frac{V_f}{V_i}\right)^{1/n} - 1\right] \times 100\%
$$

### 13.4 Speed Tricks for DI

1. **Approximation First:** In competitive exams, answer choices are usually spread apart. Approximate to the nearest 5% or 10%.

2. **Percentage of a Percentage:** If you need 23% of 847, compute 25% (= 211.75) and subtract 2% (= 16.94) → ≈ 194.8.

3. **Ratio to Percentage Conversion:** If a pie chart shows a sector and you know the total, convert the sector angle: $\text{Percentage} = \frac{\theta}{360} \times 100$.

---

## 14. Exam-Specific Patterns & Shortcuts

### 14.1 GATE / ESE Patterns

GATE and ESE typically test percentage in the context of:
- **Data Interpretation** sets (pie charts, bar graphs)
- **Profit/Loss** word problems with multiple percentage changes
- **Engineering applications** — error percentage, efficiency percentage

**Key technique:** Use the **multiplier chain method** — convert every percentage change to a decimal multiplier and multiply all at once.

### 14.2 Banking Exam Patterns

Banking exams (IBPS PO/Clerk, SBI PO) focus on:
- **Simplification:** Rapid calculation of x% of y
- **DI sets** with 5 questions on one data set
- **Comparison-based questions:** "By what percent is X more than Y?"

**Key technique:** Master the **fraction table** (Section 3). Convert every percentage to its simplest fraction before computing.

**Speed Hack:** For 16.67%, use 1/6. For 14.28%, use 1/7. This converts multiplication into simple division.

### 14.3 SSC CGL / PSU Patterns

Typically involve:
- **Election problems**
- **Population growth**
- **Income-expenditure-savings** percentage chains

**Key technique:** Set the unknown as 100 (or LCM of denominators) and work with whole numbers.

### 14.4 The "Income → Expenditure → Savings" Template

If income increases by $a\%$ and expenditure increases by $b\%$, find the % change in savings.

$$
\text{Savings} = \text{Income} - \text{Expenditure}
$$

Let Income = $I$, Expenditure = $E$, Savings = $S = I - E$.

New Savings = $I(1 + a/100) - E(1 + b/100)$

$$
\%\ \text{change in Savings} = \frac{I \cdot a/100 - E \cdot b/100}{I - E} \times 100
$$

$$
= \frac{Ia - Eb}{I - E}\ \%
$$

**Example:** A person earns ₹10,000 and spends ₹7,000. Income rises by 20%, expenditure by 30%.

Old Savings = 3,000.
New Income = 12,000. New Expenditure = 9,100. New Savings = 2,900.

$$
\%\ \text{change} = \frac{2900 - 3000}{3000} \times 100 = -3.33\%
$$

Savings **decreased** by 3.33% despite income rising by 20%.

### 14.5 The "Students Passed/Failed" Template

If $x\%$ of boys and $y\%$ of girls pass an exam, and the ratio of boys to girls is $m : n$:

$$
\text{Overall pass } \% = \frac{mx + ny}{m + n}\ \%
$$

This is the **weighted average** of percentages.

**Example:** 60% of 200 boys and 80% of 300 girls pass.
$$
\text{Pass}\% = \frac{200 \times 60 + 300 \times 80}{200 + 300} = \frac{12000 + 24000}{500} = 72\%
$$

---

## 15. Edge Cases & Common Traps

### Trap 1: "Percentage OF" vs "Percentage MORE THAN"

"A is 150% of B" → $A = 1.5B$

"A is 150% more than B" → $A = B + 1.5B = 2.5B$

These are completely different. Read the question word by word.

### Trap 2: Base Confusion

"If A is 25% more than B, then B is ___% less than A?"

Students often answer 25%. The correct answer is 20% (see Section 8).

### Trap 3: Successive ≠ Additive

Two successive increases of 10% ≠ 20% increase.

$$
\text{Net} = 10 + 10 + \frac{10 \times 10}{100} = 21\%
$$

### Trap 4: Percentage of Decrease Then Increase

"A price drops by 20% and then increases by 20%. Is it back to original?"

No. Net change = $20 + (-20) + \frac{20 \times (-20)}{100} = -4\%$. The price is **4% less** than original.

**General Rule:** An $x\%$ increase followed by an $x\%$ decrease (or vice versa) always results in a **net decrease** of $\frac{x^2}{100}\%$.

### Trap 5: Percentage Change of a Ratio

If both numerator and denominator change, you cannot simply add/subtract the percentage changes.

If $R = A/B$, $A$ increases by $a\%$ and $B$ increases by $b\%$:

$$
R_{\text{new}} = R \times \frac{1 + a/100}{1 + b/100}
$$

$$
\%\ \text{change in } R = \left(\frac{1 + a/100}{1 + b/100} - 1\right) \times 100 = \frac{a - b}{100 + b} \times 100\%
$$

**Example:** If price increases by 20% and quantity consumed decreases by 10%, % change in expenditure:
$$
\text{Exp} = P \times Q \implies \text{New Exp} = 1.20P \times 0.90Q = 1.08PQ
$$
Expenditure increases by 8%.

### Trap 6: Percentage Change When Original is Zero

If the original value is 0, percentage change is **undefined** (division by zero). Exam questions avoid this, but if you see it in DI data, flag it as "not calculable" or "infinite."

### Trap 7: Confusing Percentage Points with Percentage Change

"Market share went from 20% to 25%."
- Change = 5 **percentage points**
- Percentage change = $\frac{5}{20} \times 100 = 25\%$ increase

These are different metrics. Read what the question asks.

---

## 16. Practice Problem Bank with Solutions

### Problem 1 (Basic — Banking)
If 35% of a number is 175, find 50% of that number.

**Solution:**
$$
35\% = 175 \implies \text{Number} = \frac{175}{0.35} = 500
$$
$$
50\% \text{ of } 500 = 250
$$

**Shortcut:** $\frac{50\%}{35\%} = \frac{50}{35} = \frac{10}{7}$. So answer $= 175 \times \frac{10}{7} = 250$.

---

### Problem 2 (Percentage Change — SSC)
A's income is 60% more than B's. By what percent is B's income less than A's?

**Solution:**
$$
\frac{60}{100 + 60} \times 100 = \frac{60}{160} \times 100 = 37.5\%
$$

---

### Problem 3 (Successive Change — GATE DI)
The production of a factory increased by 10% in 2022, decreased by 5% in 2023, and increased by 20% in 2024 over the respective previous years. What is the overall percentage change from 2021 to 2024?

**Solution:**
$$
\text{Multiplier} = 1.10 \times 0.95 \times 1.20 = 1.254
$$
$$
\text{Overall change} = (1.254 - 1) \times 100 = 25.4\%\ \text{increase}
$$

---

### Problem 4 (Population — PSU)
The population of a city was 2,00,000 in 2020. It grows at 5% per annum. What is the population in 2023?

**Solution:**
$$
P = 200000 \times (1.05)^3 = 200000 \times 1.157625 = 2,31,525
$$

---

### Problem 5 (Election — Banking)
In an election between two candidates, 15% of votes were declared invalid. The winner got 60% of valid votes and won by 5,100 votes. Find total votes cast.

**Solution:**
Valid votes = 85% of Total.
Winner = 60%, Loser = 40% of valid.
Margin = 20% of valid = 5,100.
$$
\text{Valid} = \frac{5100}{0.20} = 25500
$$
$$
\text{Total} = \frac{25500}{0.85} = 30000
$$

---

### Problem 6 (Income-Expenditure — SSC CGL)
Ravi's income is ₹15,000 and expenditure is ₹12,000. His income increases by 20% and expenditure by 25%. Find the percentage change in savings.

**Solution:**
Old Savings = 15000 − 12000 = 3000.
New Income = 15000 × 1.20 = 18000.
New Expenditure = 12000 × 1.25 = 15000.
New Savings = 18000 − 15000 = 3000.

$$
\%\ \text{change} = \frac{3000 - 3000}{3000} \times 100 = 0\%
$$

No change in savings — income went up but so did expenditure proportionally relative to savings.

---

### Problem 7 (Mixture — Banking)
A 60-litre mixture contains milk and water in 2:1 ratio. How much water must be added so that the milk concentration becomes 40%?

**Solution:**
Milk = 40 litres. Water = 20 litres.
After adding $w$ litres of water:
$$
\frac{40}{60 + w} = 0.40
$$
$$
40 = 24 + 0.4w
$$
$$
0.4w = 16 \implies w = 40
$$

Wait — let me recompute:
$$
40 = 0.40 \times (60 + w)
$$
$$
40 = 24 + 0.4w
$$

That gives $0.4w = 16$, so $w = 40$ litres of water must be added.

Verification: New total = 100 litres. Milk = 40 litres = 40%. ✓

---

### Problem 8 (Multi-Step — GATE)
A shopkeeper marks his goods 30% above the cost price and offers two successive discounts of 10% and 10%. Find the profit or loss percentage.

**Solution:**
$$
\text{SP} = \text{CP} \times 1.30 \times 0.90 \times 0.90
$$
$$
= \text{CP} \times 1.30 \times 0.81 = \text{CP} \times 1.053
$$
$$
\text{Profit} = 5.3\%
$$

---

### Problem 9 (Expenditure Change — ESE)
If the price of rice rises by 25%, by what percentage must a family reduce consumption to keep the expenditure the same?

**Solution:**
Expenditure = Price × Quantity.

New Price = 1.25P. We need new expenditure = old expenditure.
$$
1.25P \times Q_{\text{new}} = P \times Q
$$
$$
Q_{\text{new}} = \frac{Q}{1.25} = 0.8Q
$$
$$
\text{Reduction} = 20\%
$$

**Shortcut:** $\frac{25}{125} \times 100 = 20\%$. (Use $\frac{x}{100+x}$ for the required decrease.)

---

### Problem 10 (Reverse Percentage — Banking)
After spending 65% of his income and donating 10% of the remainder, a person saves ₹6,300. Find his income.

**Solution:**
After spending 65%, remainder = 35% of Income.
Donation = 10% of remainder. Savings = 90% of remainder.
$$
0.90 \times 0.35 \times \text{Income} = 6300
$$
$$
0.315 \times \text{Income} = 6300
$$
$$
\text{Income} = \frac{6300}{0.315} = 20000
$$

---

## 17. Quick-Revision Cheat Sheet

### Formulae at a Glance

| # | Formula | Use Case |
|---|---------|----------|
| 1 | $x\%$ of $N = \frac{xN}{100}$ | Basic percentage |
| 2 | $\frac{A}{B} \times 100\%$ | A is what % of B |
| 3 | $\frac{\text{New}-\text{Old}}{\text{Old}} \times 100$ | Percentage change |
| 4 | $a + b + \frac{ab}{100}$ | Two successive changes |
| 5 | $\frac{\text{New Value}}{\text{Multiplier}}$ | Finding original |
| 6 | $\frac{x}{100+x} \times 100$ | Reversal: more→less |
| 7 | $\frac{x}{100-x} \times 100$ | Reversal: less→more |
| 8 | $P_0(1+r/100)^n$ | Population/compound growth |
| 9 | $V_0(1-r/100)^n$ | Depreciation |
| 10 | $V(1-x/V)^n$ | Repeated replacement |
| 11 | $\frac{mx+ny}{m+n}$ | Weighted average % |
| 12 | $d_1+d_2-\frac{d_1 d_2}{100}$ | Equivalent single discount |

### 5-Second Sanity Checks

1. **If both changes are equal and opposite, net is always a loss.** $x\%$ up then $x\%$ down → net loss of $\frac{x^2}{100}\%$.

2. **Successive discounts always total less than sum.** 20% + 30% discount ≠ 50%. It's 44%.

3. **For reversal**: increase of 1/n requires decrease of 1/(n+1). Quick fraction check.

4. **Weighted average lies between the two values.** If your answer is outside the range of the individual percentages, it's wrong.

5. **Multiplier must be positive.** If your multiplier goes negative, recheck — you may have subtracted more than 100%.

### Memory Anchors

**"SUDDS" for successive changes:** **S**tart × **U**p-multiplier × **D**own-multiplier = **D**one. **S**implify.

**"BASE matters":** Always ask — percentage OF WHAT? The denominator in the percentage formula is the **base**. Wrong base = wrong answer.

**"72 Rule":** Doubling time ≈ 72 / rate%. Works for growth, population, money.

---

> **End of Percentage Study Material.**
>
> This material covers every concept, formula derivation, trick, edge case, and exam pattern needed for GATE, ESE, PSU, and Banking examinations. Each formula is derived from first principles with the "why" explained. Practice the 10 problems until each can be solved in under 60 seconds.
