# Simple Interest & Compound Interest — Complete Mastery Guide

> **Target Exams:** GATE · ESE · PSU · BANK (IBPS/SBI/RBI)
>
> **Philosophy:** Every formula is *derived*, not memorized. You will understand the *why* behind each equation so deeply that forgetting becomes impossible.

---

## Table of Contents

1. [The Atomic Idea — What Is Interest?](#1-the-atomic-idea--what-is-interest)
2. [Simple Interest (SI) — From Scratch](#2-simple-interest-si--from-scratch)
3. [Compound Interest (CI) — From Scratch](#3-compound-interest-ci--from-scratch)
4. [SI vs CI — The Core Relationship](#4-si-vs-ci--the-core-relationship)
5. [Installments (EMI)](#5-installments-emi)
6. [Population & Depreciation (CI Applications)](#6-population--depreciation-ci-applications)
7. [Effective Rate of Interest](#7-effective-rate-of-interest)
8. [Exam-Grade Shortcuts & Tricks](#8-exam-grade-shortcuts--tricks)
9. [Edge Cases & Examiner Traps](#9-edge-cases--examiner-traps)
10. [Worked Examples — All Exam Types](#10-worked-examples--all-exam-types)
11. [Mnemonics & Quick-Recall](#11-mnemonics--quick-recall)
12. [Practice Problem Bank](#12-practice-problem-bank)

---

## 1. The Atomic Idea — What Is Interest?

**Interest = The rent you pay for using someone else's money.**

> **Analogy:** You borrow your friend's bicycle for a week. You return the bicycle (the *Principal*) **plus** a chocolate bar as a thank-you (the *Interest*). The chocolate bar is the "cost of borrowing."

### Core Variables

| Symbol | Meaning | Unit |
|--------|---------|------|
| $P$ | **Principal** — the original amount borrowed/invested | ₹ (currency) |
| $R$ | **Rate of interest** per unit time | % per annum (p.a.) |
| $T$ | **Time** period | Years (default) |
| $I$ | **Interest** earned/paid | ₹ |
| $A$ | **Amount** = Principal + Interest | ₹ |

**The Universal Equation:**

$$A = P + I$$

This is always true — for SI, CI, or any system. The *only* difference between SI and CI is **how $I$ is calculated**.

---

## 2. Simple Interest (SI) — From Scratch

### 2.1 The "Why" — How the Formula Comes Up

> **Question:** If I lend ₹100 at 10% per year, how much interest do I earn each year?

**Year 1:** 10% of ₹100 = ₹10
**Year 2:** 10% of ₹100 = ₹10 (still on the *original* ₹100, not on ₹110)
**Year 3:** 10% of ₹100 = ₹10

After 3 years, total interest = ₹10 + ₹10 + ₹10 = ₹30.

**Pattern:** Interest each year = $P \times \frac{R}{100}$

After $T$ years:

$$\boxed{SI = \frac{P \times R \times T}{100}}$$

**Why the 100?** Because $R$ is a *percentage*. Writing $R = 10$ means $\frac{10}{100} = 0.10$ of the principal.

### 2.2 The Amount Formula

$$A = P + SI = P + \frac{P \times R \times T}{100} = P\left(1 + \frac{R \times T}{100}\right)$$

### 2.3 Rearranged Forms (Exam-Critical)

From $SI = \frac{PRT}{100}$, isolate any variable:

| Find | Formula |
|------|---------|
| $P$ | $P = \frac{SI \times 100}{R \times T}$ |
| $R$ | $R = \frac{SI \times 100}{P \times T}$ |
| $T$ | $T = \frac{SI \times 100}{P \times R}$ |

> **Trick:** All four rearrangements use the same three numbers in the numerator and denominator — just move the unknown to the left side.

### 2.4 When Time Is in Months or Days

The formula assumes $T$ is in **years** (since $R$ is usually per annum).

- If time is in **months**: $T = \frac{\text{months}}{12}$
- If time is in **days**: $T = \frac{\text{days}}{365}$ (or 366 for leap year)

> **Banking Convention:** Many bank/financial exams use a **360-day commercial year** instead of 365. Always check the question. If unspecified in a BANK exam, assume 360 days. If unspecified in GATE/ESE, assume 365 days.

**Example:** $P = ₹5000$, $R = 12\%$ p.a., $T = 9$ months.

$$SI = \frac{5000 \times 12 \times \frac{9}{12}}{100} = \frac{5000 \times 12 \times 9}{100 \times 12} = \frac{5000 \times 9}{100} = ₹450$$

> **Shortcut insight:** When $T$ is in months, the 12 in the numerator ($R$ contribution) and denominator (time conversion) often cancel. Look for this.

### 2.5 SI is LINEAR

**Key insight:** Simple Interest grows **linearly** with time.

```
Interest
  |          /
  |        /
  |      /       ← straight line (constant slope = P×R/100)
  |    /
  |  /
  |/_____________ Time
```

This means:
- **Doubling time = halving rate** (if other variables constant)
- If SI for 5 years is ₹500, SI for 1 year is exactly ₹100

---

## 3. Compound Interest (CI) — From Scratch

### 3.1 The "Why" — How CI Differs

> **The key difference:** In CI, interest is calculated on **Principal + previously accumulated interest**. Interest earns interest.

**Example:** $P = ₹100$, $R = 10\%$ p.a., compounded annually.

| Year | Principal at Start | Interest This Year | Amount at End |
|------|-------------------|-------------------|---------------|
| 1 | ₹100 | 10% of 100 = ₹10 | ₹110 |
| 2 | ₹110 | 10% of 110 = ₹11 | ₹121 |
| 3 | ₹121 | 10% of 121 = ₹12.10 | ₹133.10 |

Compare with SI after 3 years: $100 + 30 = ₹130$. CI gives ₹133.10 — the extra ₹3.10 is "interest on interest."

### 3.2 Derivation of the CI Formula

**Year 1:**
$$A_1 = P + P \cdot \frac{R}{100} = P\left(1 + \frac{R}{100}\right)$$

**Year 2:** (interest is now on $A_1$, not $P$)
$$A_2 = A_1\left(1 + \frac{R}{100}\right) = P\left(1 + \frac{R}{100}\right)^2$$

**Year 3:**
$$A_3 = A_2\left(1 + \frac{R}{100}\right) = P\left(1 + \frac{R}{100}\right)^3$$

**General (after $T$ years, compounded annually):**

$$\boxed{A = P\left(1 + \frac{R}{100}\right)^T}$$

$$\boxed{CI = A - P = P\left[\left(1 + \frac{R}{100}\right)^T - 1\right]}$$

> **"Aha" Moment:** The factor $\left(1 + \frac{R}{100}\right)$ is a **multiplier**. Each year, the amount gets *multiplied* by this factor. That is why CI is *exponential* — it is repeated multiplication, not repeated addition (which is what SI does).

### 3.3 Compounding More Than Once a Year

If interest is compounded $n$ times per year:

$$A = P\left(1 + \frac{R}{100n}\right)^{nT}$$

| Compounding | $n$ |
|-------------|-----|
| Annually | 1 |
| Semi-annually (half-yearly) | 2 |
| Quarterly | 4 |
| Monthly | 12 |
| Daily | 365 |

**How this formula comes up:**
- If compounded semi-annually at 10% p.a., each half gets **5%** interest for **2 periods per year**.
- Rate per period = $\frac{R}{n}$, Number of periods = $n \times T$.
- Substituting into the annual CI formula gives the general formula above.

**Example:** $P = ₹10000$, $R = 8\%$ p.a., compounded quarterly, $T = 1$ year.

$$A = 10000\left(1 + \frac{8}{100 \times 4}\right)^{4 \times 1} = 10000\left(1 + 0.02\right)^4 = 10000 \times (1.02)^4$$

$(1.02)^4 = 1.08243216$

$$A = ₹10824.32$$

CI = ₹824.32 (vs SI of ₹800). The extra ₹24.32 comes from intra-year compounding.

### 3.4 CI is EXPONENTIAL

```
Amount
  |            *
  |          *
  |        *       ← exponential curve (gets steeper)
  |      *
  |    *
  |  *
  |*______________ Time
```

**Key consequence:** For the same $P$, $R$, $T$:
- CI ≥ SI always (equality only when $T = 1$ year with annual compounding, or $T = 0$)
- The gap between CI and SI **widens** as $T$ increases

---

## 4. SI vs CI — The Core Relationship

### 4.1 Difference Between CI and SI for 2 Years

This is an **extremely high-frequency exam question**.

$$SI_{2} = \frac{P \times R \times 2}{100} = \frac{2PR}{100}$$

$$CI_{2} = P\left(1+\frac{R}{100}\right)^2 - P = P\left[\left(1+\frac{R}{100}\right)^2 - 1\right]$$

Expand $\left(1 + \frac{R}{100}\right)^2 = 1 + \frac{2R}{100} + \frac{R^2}{10000}$

$$CI_2 = P\left[\frac{2R}{100} + \frac{R^2}{10000}\right] = \frac{2PR}{100} + \frac{PR^2}{10000}$$

$$\boxed{CI_2 - SI_2 = \frac{PR^2}{10000} = P\left(\frac{R}{100}\right)^2}$$

> **"Aha" Moment:** The difference between CI and SI for 2 years is simply **SI on 1 year's SI**:
>
> $CI_2 - SI_2 = \frac{R}{100} \times \frac{PR}{100} = \frac{R}{100} \times SI_1$
>
> This makes intuitive sense: in the second year, CI charges interest on the first year's interest — that extra "interest on interest" is exactly this difference.

### 4.2 Difference Between CI and SI for 3 Years

$$\boxed{CI_3 - SI_3 = \frac{PR^2(300 + R)}{100^3} = P\left(\frac{R}{100}\right)^2\left(3 + \frac{R}{100}\right)}$$

**Derivation sketch:**

$CI_3 = P\left[\left(1 + \frac{R}{100}\right)^3 - 1\right]$

Expand $(1+x)^3 = 1 + 3x + 3x^2 + x^3$ where $x = \frac{R}{100}$:

$CI_3 = P[3x + 3x^2 + x^3]$

$SI_3 = P \cdot 3x$

$CI_3 - SI_3 = P[3x^2 + x^3] = Px^2(3 + x) = P\left(\frac{R}{100}\right)^2\left(3 + \frac{R}{100}\right)$

### 4.3 The Ratio Method (Successive Years in CI)

In CI (compounded annually), each year's amount is the previous year's multiplied by $\left(1 + \frac{R}{100}\right)$.

Therefore, **interest in successive years** forms a geometric progression:

$$\frac{I_2}{I_1} = \frac{I_3}{I_2} = 1 + \frac{R}{100}$$

> **Exam Power Move:** If CI in year 2 is ₹550 and CI in year 1 is ₹500:
>
> $\frac{550}{500} = 1 + \frac{R}{100} \implies \frac{R}{100} = \frac{50}{500} = 0.10 \implies R = 10\%$

---

## 5. Installments (EMI)

### 5.1 Equal Annual Installment Under SI

If a sum $P$ is borrowed and repaid in $n$ equal annual installments of ₹$x$ each at $R\%$ SI:

$$\boxed{P = \frac{x \cdot n}{1 + \frac{R}{100} \cdot \frac{(n-1)}{2}}}$$

**Why?** Each installment of ₹$x$ reduces the outstanding principal. The $k$-th installment (paid at end of year $k$) effectively "saves" interest for the remaining $(n - k)$ years.

Total amount repaid = $n \times x$

The principal with interest for $n$ years = $P + \frac{PRn}{100}$

But each installment $x$ paid at end of year $k$ also stops interest on itself for $(n - k)$ years. The total interest "saved" by early payments:

$$\frac{xR}{100}\left[1 + 2 + \cdots + (n-1)\right] = \frac{xR}{100} \cdot \frac{n(n-1)}{2}$$

Setting total amount repaid = principal + net interest:

$$nx = P + \frac{PRn}{100} - \frac{xR \cdot n(n-1)}{200}$$

Solving for $P$:

$$P = \frac{x \cdot n}{1 + \frac{Rn}{100}} \times \left(1 + \frac{R(n-1)}{200}\right) = \frac{x \cdot n}{1 + \frac{R(n-1)}{200}}$$

### 5.2 Equal Annual Installment Under CI

$$\boxed{x = \frac{P \cdot r \cdot (1+r)^n}{(1+r)^n - 1}} \quad \text{where } r = \frac{R}{100}$$

**Derivation:** The present value of $n$ future payments of ₹$x$ each must equal $P$:

$$P = \frac{x}{(1+r)} + \frac{x}{(1+r)^2} + \cdots + \frac{x}{(1+r)^n}$$

This is a geometric series with first term $\frac{x}{1+r}$ and ratio $\frac{1}{1+r}$:

$$P = x \cdot \frac{1 - (1+r)^{-n}}{r}$$

Solving for $x$ gives the EMI formula.

---

## 6. Population & Depreciation (CI Applications)

### 6.1 Population Growth

Population follows compound interest logic — each year's growth is on the *current* population, not the original.

$$\boxed{P_{\text{after}} = P_{\text{now}}\left(1 + \frac{R}{100}\right)^T}$$

**Example:** City population = 50,000. Growth rate = 5% p.a. Population after 3 years?

$P = 50000 \times (1.05)^3 = 50000 \times 1.157625 = 57881.25 \approx 57881$

### 6.2 Depreciation (Decay)

Value of a machine/asset **decreases** each year:

$$\boxed{V_{\text{after}} = V_{\text{now}}\left(1 - \frac{R}{100}\right)^T}$$

> **Key:** Notice the **minus** sign inside the bracket. This is the only change from the growth formula.

**Example:** Machine value = ₹1,00,000. Depreciation = 10% p.a. Value after 2 years?

$V = 100000 \times (0.9)^2 = 100000 \times 0.81 = ₹81,000$

### 6.3 Mixed Growth Rates (Different Rates Each Year)

$$\boxed{A = P\left(1 + \frac{R_1}{100}\right)\left(1 + \frac{R_2}{100}\right)\left(1 + \frac{R_3}{100}\right)}$$

When growth rates change year-to-year, simply multiply the individual factors. No single "average" rate trick — you must use each rate separately.

---

## 7. Effective Rate of Interest

### 7.1 Concept

If interest is compounded more than once a year, the **effective annual rate** is higher than the stated (nominal) rate.

$$\boxed{R_{\text{eff}} = \left(1 + \frac{R}{100n}\right)^n - 1} \quad \text{(expressed as a fraction; multiply by 100 for %)}$$

**Example:** Nominal rate = 12% p.a. compounded monthly.

$R_{\text{eff}} = \left(1 + \frac{0.12}{12}\right)^{12} - 1 = (1.01)^{12} - 1 \approx 0.12683 = 12.683\%$

> **Exam Takeaway:** For BANK exams, they often give the nominal rate and ask for effective rate, or vice versa. The formula above is the bridge.

### 7.2 Quick Effective Rate for 2 Half-Years

If nominal rate is $R\%$ compounded semi-annually:

$$R_{\text{eff}} = R + \frac{R^2}{400}\%$$

**Derivation:** $\left(1 + \frac{R}{200}\right)^2 = 1 + \frac{R}{100} + \frac{R^2}{40000}$

Effective rate = $\frac{R}{100} + \frac{R^2}{40000} = \frac{R + R^2/400}{100}$

So $R_{\text{eff}}\% = R + \frac{R^2}{400}$

---

## 8. Exam-Grade Shortcuts & Tricks

### Trick 1: The Rule of 72 (Doubling Time)

**Approximate** number of years to double your money at $R\%$ compound interest:

$$\boxed{T_{\text{double}} \approx \frac{72}{R}}$$

| Rate | Doubling Time (Rule of 72) | Exact |
|------|---------------------------|-------|
| 6% | 12 years | 11.9 years |
| 8% | 9 years | 9.01 years |
| 10% | 7.2 years | 7.27 years |
| 12% | 6 years | 6.12 years |

> **Why 72?** The exact formula gives $T = \frac{\ln 2}{\ln(1 + R/100)}$. For small $R$, $\ln(1+x) \approx x$, so $T \approx \frac{0.693}{R/100} = \frac{69.3}{R}$. The number 72 is used instead of 69.3 because it has more divisors (1,2,3,4,6,8,9,12…) making mental math easier.

### Trick 2: SI Doubling Time

For Simple Interest, the amount doubles when $SI = P$:

$$P = \frac{P \times R \times T}{100} \implies T = \frac{100}{R}$$

**To triple:** $SI = 2P \implies T = \frac{200}{R}$

**General:** To become $n$ times: $T = \frac{(n-1) \times 100}{R}$

### Trick 3: Finding SI/CI Quickly Using Fractions

When $R$ is a "nice" fraction:

| Rate | Fraction | Mental Math |
|------|----------|-------------|
| 5% | 1/20 | Divide by 20 |
| 10% | 1/10 | Divide by 10 |
| 12.5% | 1/8 | Divide by 8 |
| 20% | 1/5 | Divide by 5 |
| 25% | 1/4 | Divide by 4 |
| 33⅓% | 1/3 | Divide by 3 |
| 50% | 1/2 | Divide by 2 |

**Example:** CI on ₹8000 at 12.5% for 2 years (compounded annually).

$12.5\% = \frac{1}{8}$. Multiplier = $1 + \frac{1}{8} = \frac{9}{8}$

$A = 8000 \times \frac{9}{8} \times \frac{9}{8} = 8000 \times \frac{81}{64} = ₹10125$

CI = $10125 - 8000 = ₹2125$

> No calculator needed — pure fraction arithmetic.

### Trick 4: Half-Yearly to Annual Conversion

If given: "$R\%$ compounded semi-annually for $T$ years"

Convert to: Rate = $\frac{R}{2}\%$, Time = $2T$ periods, then use standard CI formula.

**Example:** 10% p.a. compounded semi-annually for 2 years = 5% for 4 periods.

$A = P \times (1.05)^4$

### Trick 5: The "Successive Interest" Method for 2 Years

For CI over 2 years at rate $R\%$:

$$\text{Effective 2-year rate} = R + R + \frac{R \times R}{100} = 2R + \frac{R^2}{100}$$

**Example:** $R = 10\%$. Effective 2-year CI rate = $10 + 10 + \frac{10 \times 10}{100} = 21\%$

So CI on ₹5000 for 2 years at 10% = $5000 \times \frac{21}{100} = ₹1050$

> **Why this works:** $(1+0.1)^2 = 1.21$, so the total percentage gain over 2 years is 21%.

### Trick 6: Finding the Rate When CI and SI Are Given

For 2 years:

$$R = \frac{(CI - SI) \times 2 \times 100}{SI}\%$$

**Derivation:** $CI_2 - SI_2 = \frac{PR^2}{10000}$ and $SI_2 = \frac{2PR}{100}$

$$\frac{CI_2 - SI_2}{SI_2} = \frac{PR^2/10000}{2PR/100} = \frac{R}{200}$$

$$R = \frac{200(CI_2 - SI_2)}{SI_2}$$

### Trick 7: Principal from Amounts at CI

If Amount after $n$ years = $A_n$ and after $(n+1)$ years = $A_{n+1}$:

$$R = \frac{A_{n+1} - A_n}{A_n} \times 100\%$$

$$P = \frac{A_n}{(1 + R/100)^n}$$

---

## 9. Edge Cases & Examiner Traps

### Trap 1: Time Units Mismatch

> **Problem:** "SI on ₹4000 at 6% for 2 years and 3 months."

Many students use $T = 2.3$ (wrong!) instead of $T = 2 + \frac{3}{12} = 2.25$ years.

$$SI = \frac{4000 \times 6 \times 2.25}{100} = ₹540$$

### Trap 2: CI with Fractional Years

When CI involves a fractional year like $2\frac{1}{2}$ years:

**Method:** Compound for the whole years, then apply SI for the fractional part.

$A = P\left(1 + \frac{R}{100}\right)^2 \times \left(1 + \frac{R \times \frac{1}{2}}{100}\right)$

> **Warning:** Some questions compound for fractional periods too. Read the question carefully — if it says "compounded annually," use SI for the fractional part. If it says "compounded half-yearly," treat the half as one more compounding period.

### Trap 3: "Per Annum" vs "For the Period"

If the question says "8% for 6 months" (without saying "per annum"), it means 8% is the rate for 6 months itself — not 8% p.a.

### Trap 4: CI-SI Difference Is NOT Always $\frac{PR^2}{10000}$

That formula works only for **2 years**. For 3+ years, use the expanded formula from Section 4.2.

### Trap 5: Confusing Amount with Interest

$A = P + I$. Many students calculate $A$ but report it as if it were $I$ (or vice versa).

> **5-Second Sanity Check:** Interest should be **less than** the principal for reasonable rates and time periods. If your interest exceeds the principal at 10% for 3 years, something is wrong.

### Trap 6: SI = CI for $T = 1$ Year (Annual Compounding Only)

For 1 year with annual compounding, SI = CI. But if compounded semi-annually/quarterly/monthly for 1 year, CI > SI.

### Trap 7: The "Sum of Money" Trick in BANK Exams

> "A sum becomes 3 times in 8 years at SI. In how many years will it become 5 times?"

$3P = P + SI_8 \implies SI_8 = 2P$

Rate: $\frac{2P \times 100}{P \times 8} = 25\%$

For $5P$: $4P = \frac{P \times 25 \times T}{100} \implies T = 16$ years.

**Shortcut:** $\frac{T_2}{T_1} = \frac{n_2 - 1}{n_1 - 1} \implies T_2 = 8 \times \frac{4}{2} = 16$ years.

### Trap 8: NAT Precision (GATE Specific)

In GATE NAT questions, answers are typically matched to **2 decimal places**. Be precise:
- $(1.05)^3 = 1.157625$, not $1.16$
- Use exact fractions where possible and convert only at the final step
- Round only the final answer, never intermediate values

---

## 10. Worked Examples — All Exam Types

### Example 1 — Basic SI (BANK Level)

> **Q:** Find the SI on ₹6000 at 8% p.a. for 3 years.

$$SI = \frac{6000 \times 8 \times 3}{100} = \frac{144000}{100} = ₹1440$$

$A = 6000 + 1440 = ₹7440$

---

### Example 2 — Find Rate (BANK/SSC)

> **Q:** A sum of ₹4000 amounts to ₹5200 in 4 years at SI. Find the rate.

$SI = 5200 - 4000 = ₹1200$

$R = \frac{1200 \times 100}{4000 \times 4} = \frac{120000}{16000} = 7.5\%$

---

### Example 3 — CI Computation (GATE/ESE)

> **Q:** Find CI on ₹15000 at 10% p.a. for 2 years, compounded annually.

$$A = 15000\left(1 + \frac{10}{100}\right)^2 = 15000 \times (1.1)^2 = 15000 \times 1.21 = ₹18150$$

$CI = 18150 - 15000 = ₹3150$

**Verification using the successive rate trick:** Effective 2-year rate = $10 + 10 + 1 = 21\%$

$CI = 15000 \times 0.21 = ₹3150$ ✓

---

### Example 4 — CI-SI Difference (High Frequency)

> **Q:** The difference between CI and SI on a sum at 5% p.a. for 2 years is ₹20. Find the sum.

$$CI_2 - SI_2 = P\left(\frac{R}{100}\right)^2$$

$$20 = P\left(\frac{5}{100}\right)^2 = P \times \frac{1}{400}$$

$$P = 20 \times 400 = ₹8000$$

---

### Example 5 — Half-Yearly Compounding (BANK/GATE)

> **Q:** CI on ₹20000 at 10% p.a. compounded semi-annually for 1 year.

Rate per period = 5%, Periods = 2

$A = 20000 \times (1.05)^2 = 20000 \times 1.1025 = ₹22050$

$CI = ₹2050$

Compare: SI for same = $\frac{20000 \times 10 \times 1}{100} = ₹2000$. Extra ₹50 from compounding.

---

### Example 6 — Population Problem (GATE/ESE)

> **Q:** A town has 50,000 people. Population grows at 4% in year 1, 5% in year 2, and 8% in year 3. Find population after 3 years.

$$P_3 = 50000 \times 1.04 \times 1.05 \times 1.08$$

$= 50000 \times 1.04 \times 1.05 \times 1.08$

$= 50000 \times 1.092 \times 1.08$ (since $1.04 \times 1.05 = 1.092$)

$= 50000 \times 1.17936 = 58968$

---

### Example 7 — Doubling at CI (GATE NAT)

> **Q:** At what rate of CI does money double in 5 years? (Use Rule of 72)

$R \approx \frac{72}{5} = 14.4\%$

Exact: $2 = (1 + r)^5 \implies r = 2^{1/5} - 1 = 1.14870 - 1 = 0.14870 = 14.87\%$

> For GATE NAT, if the question asks for approximate, use Rule of 72. If exact, use the logarithmic formula.

---

### Example 8 — Installment (BANK/SSC)

> **Q:** A man borrows ₹10000 at 10% CI and repays in 2 equal annual installments. Find each installment.

$r = 0.10, n = 2$

$$x = \frac{10000 \times 0.10 \times (1.10)^2}{(1.10)^2 - 1} = \frac{10000 \times 0.10 \times 1.21}{0.21} = \frac{1210}{0.21} = ₹5761.90$$

**Verification:** After year 1: $10000 \times 1.10 - 5761.90 = 11000 - 5761.90 = ₹5238.10$

After year 2: $5238.10 \times 1.10 - 5761.90 = 5761.91 - 5761.90 = ₹0.01 \approx ₹0$ ✓ (rounding)

---

### Example 9 — SI Sum Becomes $n$ Times (BANK/SSC)

> **Q:** A sum triples in 10 years at SI. In how many years will it become 6 times?

Using the shortcut: $T_2 = T_1 \times \frac{n_2 - 1}{n_1 - 1} = 10 \times \frac{5}{2} = 25$ years.

---

### Example 10 — Finding Principal from Year-wise CI

> **Q:** CI on a sum for the 2nd year is ₹1100 and for the 3rd year is ₹1210. Find the sum and rate.

$$\frac{I_3}{I_2} = 1 + \frac{R}{100} = \frac{1210}{1100} = 1.10 \implies R = 10\%$$

$I_2 = P \times (1.1)^2 - P \times 1.1 = P \times 1.1 \times 0.1 = 0.11P$

$0.11P = 1100 \implies P = ₹10000$

---

## 11. Mnemonics & Quick-Recall

### The "SMART" Mnemonic for SI

| Letter | Meaning | Formula |
|--------|---------|---------|
| **S** | Simple Interest result | $SI = \frac{PRT}{100}$ |
| **M** | Money (Principal) to find | $P = \frac{100 \times SI}{RT}$ |
| **A** | Annual Rate to find | $R = \frac{100 \times SI}{PT}$ |
| **R** | Remaining unknown = Time | $T = \frac{100 \times SI}{PR}$ |
| **T** | Total Amount | $A = P + SI$ |

> **Recall trick:** "SMART money uses Simple Interest" — S, M, A, R, T maps to SI, P, R, T, A formulas.

### The "Power Tower" for CI

> Visualize a building where each floor is **taller** than the last (exponential growth). Floor 1 = $P \times (1 + r)$, Floor 2 = Floor 1 × $(1 + r)$, and so on. The building height after $n$ floors = $P(1+r)^n$.

### The "72 Door" Mnemonic

> Imagine a vault with the number **72** on the door. To open it, you divide 72 by the interest rate — the result is how many years until your money doubles.

### 5-Second Snap-Checks

1. **SI sanity:** SI for 1 year at 10% should be exactly 10% of principal. Scale linearly.
2. **CI sanity:** CI for 2 years at 10% should be 21% of principal (not 20%).
3. **CI > SI:** Always, for $T > 1$ year (annual compounding). If your CI < SI, you made an error.
4. **Difference check:** $CI_2 - SI_2$ should be a small number compared to either CI or SI. If it is larger, recompute.

---

## 12. Practice Problem Bank

### Level 1 — Foundation (BANK/SSC)

**Q1.** Find the SI on ₹12000 at 6% p.a. for 4 years.
<details><summary>Answer</summary>

$SI = \frac{12000 \times 6 \times 4}{100} = ₹2880$
</details>

**Q2.** At what rate of SI will ₹5000 become ₹6500 in 5 years?
<details><summary>Answer</summary>

$SI = 1500$, $R = \frac{1500 \times 100}{5000 \times 5} = 6\%$
</details>

**Q3.** In how many years will ₹8000 yield ₹2400 as SI at 10% p.a.?
<details><summary>Answer</summary>

$T = \frac{2400 \times 100}{8000 \times 10} = 3$ years
</details>

**Q4.** A sum becomes double in 5 years at SI. Find the rate.
<details><summary>Answer</summary>

$SI = P$, $R = \frac{P \times 100}{P \times 5} = 20\%$
</details>

### Level 2 — Intermediate (BANK PO / GATE)

**Q5.** Find the CI on ₹25000 at 12% p.a. for 2 years, compounded annually.
<details><summary>Answer</summary>

$A = 25000 \times (1.12)^2 = 25000 \times 1.2544 = ₹31360$. CI = ₹6360.
</details>

**Q6.** The difference between CI and SI on a sum for 2 years at 8% p.a. is ₹128. Find the principal.
<details><summary>Answer</summary>

$P = \frac{128}{(8/100)^2} = \frac{128}{0.0064} = ₹20000$
</details>

**Q7.** CI on ₹10000 at 10% p.a. for 2 years, compounded half-yearly.
<details><summary>Answer</summary>

Rate per period = 5%, periods = 4. $A = 10000 \times (1.05)^4 = 10000 \times 1.21550625 = ₹12155.06$. CI = ₹2155.06.
</details>

**Q8.** A machine costing ₹2,00,000 depreciates at 15% p.a. Find its value after 3 years.
<details><summary>Answer</summary>

$V = 200000 \times (0.85)^3 = 200000 \times 0.614125 = ₹1,22,825$
</details>

### Level 3 — Advanced (GATE / ESE)

**Q9.** The CI on a sum for 3 years at 10% p.a. exceeds the SI by ₹620. Find the sum.
<details><summary>Answer</summary>

$CI_3 - SI_3 = P\left(\frac{R}{100}\right)^2\left(3 + \frac{R}{100}\right) = P \times 0.01 \times 3.1 = 0.031P$

$0.031P = 620 \implies P = ₹20000$
</details>

**Q10.** Find the effective annual rate equivalent to 16% p.a. compounded quarterly.
<details><summary>Answer</summary>

$R_{\text{eff}} = \left(1 + \frac{0.16}{4}\right)^4 - 1 = (1.04)^4 - 1 = 1.16985856 - 1 = 0.16986 = 16.99\%$
</details>

**Q11.** A sum of money amounts to ₹7260 in 2 years and ₹7986 in 3 years at CI compounded annually. Find the rate and the principal.
<details><summary>Answer</summary>

$R = \frac{7986 - 7260}{7260} \times 100 = \frac{726}{7260} \times 100 = 10\%$

$P = \frac{7260}{(1.10)^2} = \frac{7260}{1.21} = ₹6000$
</details>

**Q12.** A person invests ₹P at $R\%$ CI. If the interest for the 4th year is ₹1464.10, and the interest for the 5th year is ₹1610.51, find $R$ and $P$.
<details><summary>Answer</summary>

$\frac{I_5}{I_4} = \frac{1610.51}{1464.10} = 1.10 \implies R = 10\%$

$I_4 = P[(1.1)^4 - (1.1)^3] = P \times (1.1)^3 \times 0.1 = 0.1331P$

$0.1331P = 1464.10 \implies P = ₹11000$
</details>

---

## Quick Reference Card

| Concept | Formula |
|---------|---------|
| Simple Interest | $SI = \frac{PRT}{100}$ |
| SI Amount | $A = P\left(1 + \frac{RT}{100}\right)$ |
| CI Amount (annual) | $A = P\left(1 + \frac{R}{100}\right)^T$ |
| CI Amount (n times/year) | $A = P\left(1 + \frac{R}{100n}\right)^{nT}$ |
| $CI_2 - SI_2$ | $P\left(\frac{R}{100}\right)^2$ |
| $CI_3 - SI_3$ | $P\left(\frac{R}{100}\right)^2\left(3 + \frac{R}{100}\right)$ |
| Doubling (SI) | $T = \frac{100}{R}$ |
| Doubling (CI, approx) | $T \approx \frac{72}{R}$ |
| Effective Rate (semi-annual) | $R_{\text{eff}} = R + \frac{R^2}{400}\%$ |
| Depreciation | $V = V_0\left(1 - \frac{R}{100}\right)^T$ |
| EMI (CI) | $x = \frac{Pr(1+r)^n}{(1+r)^n - 1}$ |
| $n$-times at SI | $T = \frac{(n-1) \times 100}{R}$ |
| Successive year CI ratio | $\frac{I_{k+1}}{I_k} = 1 + \frac{R}{100}$ |

---

*End of SI & CI Complete Study Material*
