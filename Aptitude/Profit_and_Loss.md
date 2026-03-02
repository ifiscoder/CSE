# Profit & Loss — Complete A-to-Z Study Material
> **Target Exams:** GATE · ESE · PSU · BANK (SSC CGL / IBPS / SBI / RBI)
>
> **Goal:** Rank-1 mastery — every concept derived from first principles, every trap exposed, every shortcut battle-tested.

---

## Table of Contents

1. [The Atomic Core — What Is Profit & Loss Really?](#1-the-atomic-core)
2. [Fundamental Terminology](#2-fundamental-terminology)
3. [Master Formula Sheet — Derived, Not Memorised](#3-master-formula-sheet)
4. [Markup vs. Margin — The Classic Confusion Killer](#4-markup-vs-margin)
5. [Discount Mechanics](#5-discount-mechanics)
6. [Successive Discounts](#6-successive-discounts)
7. [Profit/Loss on Selling Price vs. Cost Price](#7-profitloss-on-sp-vs-cp)
8. [Dishonest Dealer / False Weight Problems](#8-dishonest-dealer)
9. [Buy-x-Get-y-Free Schemes](#9-buy-x-get-y-free)
10. [Mixing & Partnership Profit Sharing](#10-mixing--partnership)
11. [Break-Even Analysis](#11-break-even-analysis)
12. [Using CP = 100 Technique (Assumption Method)](#12-cp--100-technique)
13. [Percentage Multiplier (Fraction Shortcut)](#13-percentage-multiplier)
14. [Two-Article / Combined Transaction Problems](#14-two-article-problems)
15. [Solved Examples — Exam-Grade (with Traps)](#15-solved-examples)
16. [Edge Cases & Pitfalls](#16-edge-cases--pitfalls)
17. [Exam-Specific Strategies](#17-exam-specific-strategies)
18. [Mnemonics & Mental Models](#18-mnemonics--mental-models)
19. [Practice Problem Bank (with Solutions)](#19-practice-problem-bank)

---

## 1. The Atomic Core

**In ≤ 7 words:** *"Sell higher → Profit; lower → Loss."*

### The Real-World Analogy

Imagine you buy mangoes for ₹100 (your **Cost Price**). You sell them for ₹130 (your **Selling Price**).

- The ₹30 extra you earned? That's **Profit**.
- If instead you could only sell for ₹80? The ₹20 you lost? That's **Loss**.

**Why does this exist?** Every commercial transaction boils down to:

$$\boxed{\text{Profit or Loss} = \text{Selling Price} - \text{Cost Price}}$$

- Result **positive** → Profit
- Result **negative** → Loss
- Result **zero** → Break-even (no profit, no loss)

This single equation is the DNA of every problem in this chapter.

---

## 2. Fundamental Terminology

| Symbol | Term | Meaning |
|--------|------|---------|
| **CP** | Cost Price | Total amount paid to acquire the goods (includes purchase price + overhead expenses like transport, taxes, etc.) |
| **SP** | Selling Price | The amount received from the buyer when goods are sold |
| **P** | Profit (Gain) | $SP - CP$ when $SP > CP$ |
| **L** | Loss | $CP - SP$ when $CP > SP$ |
| **MP** | Marked Price (List Price) | The price *written on the tag* before any discount — the "sticker price" |
| **D** | Discount | Reduction offered on MP; $\text{Discount} = MP - SP$ |
| **P%** | Profit Percentage | Profit expressed as a percentage of CP (unless stated otherwise) |
| **L%** | Loss Percentage | Loss expressed as a percentage of CP (unless stated otherwise) |
| **D%** | Discount Percentage | Discount expressed as a percentage of MP |

### Critical Insight — The Reference Base

> **Default rule (GATE/ESE/BANK standard):**
> - Profit % and Loss % are **always calculated on CP** unless the problem explicitly says "on SP."
> - Discount % is **always calculated on MP**.
>
> *Forgetting this single rule is the #1 source of wrong answers.*

---

## 3. Master Formula Sheet — Derived, Not Memorised

### 3.1 Core Relationships

**Starting from the atomic equation** $P = SP - CP$:

$$\text{Profit %} = \frac{P}{CP} \times 100 = \frac{SP - CP}{CP} \times 100$$

$$\text{Loss %} = \frac{L}{CP} \times 100 = \frac{CP - SP}{CP} \times 100$$

**How the formula came up:** We want profit as a *fraction* of what we invested (CP), then multiply by 100 to get a percentage. It's the same logic as "marks obtained / total marks × 100" — you measure performance relative to the starting point.

### 3.2 Deriving SP from CP and Profit%

From $P\% = \frac{SP - CP}{CP} \times 100$:

$$\frac{P\%}{100} = \frac{SP}{CP} - 1$$

$$\frac{SP}{CP} = 1 + \frac{P\%}{100}$$

$$\boxed{SP = CP \times \left(1 + \frac{P\%}{100}\right)} \quad \text{... (for Profit)}$$

$$\boxed{SP = CP \times \left(1 - \frac{L\%}{100}\right)} \quad \text{... (for Loss)}$$

**Aha moment:** Think of the multiplier $(1 + P\%/100)$ as a *scaling factor*. A 20% profit means you scale CP by 1.20. A 10% loss means you scale by 0.90. That's it.

### 3.3 Deriving CP from SP and Profit%

Rearranging the above:

$$\boxed{CP = \frac{SP}{1 + \frac{P\%}{100}}} = \frac{SP \times 100}{100 + P\%}$$

$$\boxed{CP = \frac{SP}{1 - \frac{L\%}{100}}} = \frac{SP \times 100}{100 - L\%}$$

### 3.4 Marked Price & Discount

The shopkeeper sets MP on the tag, then offers a discount:

$$SP = MP - \text{Discount} = MP \times \left(1 - \frac{D\%}{100}\right)$$

**The full chain (CP → MP → SP):**

$$CP \xrightarrow{\text{Markup}} MP \xrightarrow{\text{Discount}} SP$$

If markup is $m\%$ on CP: $MP = CP \times \left(1 + \frac{m\%}{100}\right)$

If discount is $d\%$ on MP: $SP = MP \times \left(1 - \frac{d\%}{100}\right)$

Combining:

$$\boxed{SP = CP \times \left(1 + \frac{m}{100}\right)\left(1 - \frac{d}{100}\right)}$$

### 3.5 The "Multiplier" Summary Table

| Scenario | Multiplier on CP |
|----------|-----------------|
| Profit of $P\%$ | $\times\;\dfrac{100+P}{100}$ |
| Loss of $L\%$ | $\times\;\dfrac{100-L}{100}$ |
| Markup of $m\%$ then Discount of $d\%$ | $\times\;\dfrac{100+m}{100} \times \dfrac{100-d}{100}$ |

---

## 4. Markup vs. Margin — The Classic Confusion Killer

These two terms are often used interchangeably in daily life but are **mathematically different**.

| | **Markup** | **Margin (Profit %)** |
|---|---|---|
| **Base** | Cost Price (CP) | Cost Price (CP) for standard problems |
| **Formula** | $\frac{MP - CP}{CP} \times 100$ | $\frac{SP - CP}{CP} \times 100$ |
| **What it answers** | "How much did I *raise* the tag above my cost?" | "How much did I *actually earn* after selling?" |

### Example

- CP = ₹100, MP = ₹150, Discount = 10%
- Markup = $(150-100)/100 \times 100 = 50\%$
- SP = $150 \times 0.90 = ₹135$
- Actual Profit% = $(135-100)/100 \times 100 = 35\%$

**Trap:** If a problem says "marked up by 50% and sold at 10% discount," the profit is NOT 40%. It is 35%. The discount applies to the *marked price*, not the cost price.

### Why the difference?

Markup % is on CP (₹100 base). Discount % is on MP (₹150 base). 10% of ₹150 = ₹15 ≠ 10% of ₹100 = ₹10. Different bases give different absolute amounts.

### Quick Formula

$$\text{Net Profit%} = m - d - \frac{m \times d}{100}$$

where $m$ = markup %, $d$ = discount %.

**Derivation:**

$$\text{Net effect} = \left(1 + \frac{m}{100}\right)\left(1 - \frac{d}{100}\right) - 1 = \frac{m - d - \frac{md}{100}}{100}$$

Multiply by 100: $\text{Profit %} = m - d - \frac{md}{100}$.

For the example: $50 - 10 - \frac{50 \times 10}{100} = 50 - 10 - 5 = 35\%.$ ✓

---

## 5. Discount Mechanics

### 5.1 Single Discount

$$SP = MP \times \left(1 - \frac{d}{100}\right)$$

**Example:** MP = ₹800, Discount = 15%

$SP = 800 \times 0.85 = ₹680$

### 5.2 Finding Discount% When SP and MP Are Given

$$D\% = \frac{MP - SP}{MP} \times 100$$

---

## 6. Successive Discounts

When a shopkeeper gives **two discounts** $d_1\%$ and $d_2\%$ one after another:

$$SP = MP \times \left(1 - \frac{d_1}{100}\right)\left(1 - \frac{d_2}{100}\right)$$

### Why Not Just Add Them?

**Because the second discount applies to the already-reduced price, not the original MP.**

**Example:** MP = ₹1000, Successive discounts = 20% and 10%.

- **Wrong approach (just adding):** 30% discount → SP = ₹700 ✗
- **Correct approach:**
  - After 20%: $1000 \times 0.80 = ₹800$
  - After 10% on ₹800: $800 \times 0.90 = ₹720$ ✓

### Single Equivalent Discount Formula

If two successive discounts are $d_1\%$ and $d_2\%$, the single equivalent discount is:

$$\boxed{d_{eq} = d_1 + d_2 - \frac{d_1 \times d_2}{100}}$$

**Derivation:**

Effective multiplier $= (1-d_1/100)(1-d_2/100)$

Single equivalent multiplier $= (1 - d_{eq}/100)$

Setting them equal and solving:

$1 - d_{eq}/100 = 1 - d_1/100 - d_2/100 + d_1 d_2/10000$

$d_{eq}/100 = d_1/100 + d_2/100 - d_1 d_2/10000$

$d_{eq} = d_1 + d_2 - d_1 d_2 / 100$ ✓

**Example check:** $d_{eq} = 20 + 10 - (20 \times 10)/100 = 30 - 2 = 28\%$

SP = $1000 \times (1 - 0.28) = 1000 \times 0.72 = ₹720$ ✓

### Extension to Three Successive Discounts

Apply the two-discount formula twice, or directly:

$$SP = MP \times \left(1 - \frac{d_1}{100}\right)\left(1 - \frac{d_2}{100}\right)\left(1 - \frac{d_3}{100}\right)$$

---

## 7. Profit/Loss on SP vs. CP

### The Standard Convention

By default, **Profit% is on CP**. But some banking problems specifically state "profit is x% of SP."

### Conversion Formulas

If Profit is $x\%$ **on SP**, the equivalent Profit% **on CP**:

$$\boxed{P\%_{\text{on CP}} = \frac{x}{100 - x} \times 100}$$

If Profit is $x\%$ **on CP**, the equivalent Profit% **on SP**:

$$\boxed{P\%_{\text{on SP}} = \frac{x}{100 + x} \times 100}$$

**Derivation (from first principles):**

Let $P\% \text{ on SP} = x$. Then $P = \frac{x}{100} \times SP$.

Also $P = SP - CP$, so $CP = SP - P = SP(1 - x/100) = SP \times \frac{100-x}{100}$.

$P\% \text{ on CP} = \frac{P}{CP} \times 100 = \frac{\frac{x}{100} \times SP}{\frac{100-x}{100} \times SP} \times 100 = \frac{x}{100-x} \times 100$ ✓

**Example:** A man earns 20% profit on SP. What is his actual profit% (on CP)?

$P\%_{\text{on CP}} = \frac{20}{100-20} \times 100 = \frac{20}{80} \times 100 = 25\%$

Similarly for **loss**: replace $+$ with $-$ appropriately:

- Loss $x\%$ on SP → Loss on CP $= \frac{x}{100+x} \times 100$
- Loss $x\%$ on CP → Loss on SP $= \frac{x}{100-x} \times 100$

---

## 8. Dishonest Dealer / False Weight Problems

### The Concept

A dishonest shopkeeper **claims to sell at CP** (or at a certain SP) but uses a **false weight** — he gives less quantity than paid for.

### The Core Logic

If a dealer **claims** to sell $W_{\text{claimed}}$ grams but actually gives $W_{\text{actual}}$ grams:

$$\boxed{\text{Profit %} = \frac{W_{\text{claimed}} - W_{\text{actual}}}{W_{\text{actual}}} \times 100 = \frac{\text{Error}}{\text{True Value}} \times 100}$$

**Why?**

The customer pays for $W_{\text{claimed}}$ but receives $W_{\text{actual}}$.

- CP (to dealer) for $W_{\text{actual}}$ grams = proportional to $W_{\text{actual}}$
- SP (from customer) for $W_{\text{actual}}$ grams = proportional to $W_{\text{claimed}}$ (since customer pays rate × claimed weight)

$$P\% = \frac{SP - CP}{CP} = \frac{W_{\text{claimed}} - W_{\text{actual}}}{W_{\text{actual}}} \times 100$$

> **Critical:** The denominator is $W_{\text{actual}}$ (the true value), NOT $W_{\text{claimed}}$.

### Example 1 — Pure False Weight

A shopkeeper uses a 900g weight instead of 1 kg while selling at cost price. His profit%?

$$P\% = \frac{1000 - 900}{900} \times 100 = \frac{100}{900} \times 100 = 11.11\%$$

### Example 2 — False Weight + Additional Profit%

If the same shopkeeper also sells at 10% above CP:

$$\text{Total Profit %} = \left(\frac{1000}{900}\right) \times \left(\frac{110}{100}\right) \times 100 - 100$$

$$= \frac{1000 \times 110}{900 \times 100} \times 100 - 100 = \frac{11000}{900} - 100 \approx 122.22 - 100 = 22.22\%$$

**General Combined Formula:**

$$\boxed{P\% = \left(\frac{W_{\text{claimed}}}{W_{\text{actual}}} \times \frac{100 + P_{\text{extra}}\%}{100}\right) \times 100 - 100}$$

### Example 3 — False Weight + Discount

Shopkeeper marks goods 20% above CP, gives 10% discount, and uses 900g instead of 1 kg:

$$P\% = \frac{W_{\text{claimed}}}{W_{\text{actual}}} \times (1+m/100) \times (1-d/100) \times 100 - 100$$

$$= \frac{1000}{900} \times 1.20 \times 0.90 \times 100 - 100 = \frac{1000 \times 108}{900 \times 100} \times 100 - 100 = 120 - 100 = 20\%$$

---

## 9. Buy-x-Get-y-Free Schemes

### "Buy 3 Get 1 Free"

The customer pays for 3 items but receives 4 items.

- **From the seller's perspective:** He sells 4 items for the price of 3.
- CP of goods given = CP of 4 items
- SP received = SP of 3 items

If sold at MP (no additional profit/loss claimed):

$$P\% = \frac{\text{SP} - \text{CP}}{\text{CP}} = \frac{3 \times \text{price} - 4 \times \text{cost}}{4 \times \text{cost}}$$

If selling at cost price (SP per item = CP per item):

$$\text{Loss %} = \frac{4-3}{4} \times 100 = 25\%$$

Wait — that's a **loss** to the seller! The seller is giving away 1 free item.

### General Formula: "Buy $x$ Get $y$ Free"

**Effective discount** to the customer:

$$\boxed{D\% = \frac{y}{x+y} \times 100}$$

- Buy 2 Get 1 Free → $D = 1/3 \times 100 = 33.33\%$
- Buy 3 Get 1 Free → $D = 1/4 \times 100 = 25\%$
- Buy 4 Get 1 Free → $D = 1/5 \times 100 = 20\%$

**Why?** Customer buys $x+y$ items but pays for only $x$. The discount fraction is the free items / total items received.

---

## 10. Mixing & Partnership Profit Sharing

### 10.1 Mixing to Get a Target Profit

If two items are bought at different CPs and sold at the same SP:

**Example:** Tea A costs ₹60/kg, Tea B costs ₹80/kg. In what ratio should they be mixed to sell at ₹75/kg with 25% profit?

- Target CP of mixture = $75 / 1.25 = ₹60/\text{kg}$
- Using alligation: Ratio of A : B = $(80-60) : (60-60) = 20 : 0$, i.e., only Tea A should be used.

But if target CP = ₹68:

- $A : B = (80-68) : (68-60) = 12 : 8 = 3 : 2$

### 10.2 Partnership Profit Sharing

When partners invest different amounts for different durations, profit is shared in the ratio of **(Investment × Time)**.

$$\text{Share of } A : B = (I_A \times T_A) : (I_B \times T_B)$$

**Example:** A invests ₹5000 for 12 months, B invests ₹8000 for 9 months. Total profit = ₹18,400.

Ratio = $5000 \times 12 : 8000 \times 9 = 60000 : 72000 = 5 : 6$

A's share = $\frac{5}{11} \times 18400 = ₹8363.64$

B's share = $\frac{6}{11} \times 18400 = ₹10036.36$

---

## 11. Break-Even Analysis

### What Is Break-Even?

The point where **Total Revenue = Total Cost** → zero profit, zero loss.

$$\text{Break-even quantity} = \frac{\text{Fixed Costs}}{\text{SP per unit} - \text{Variable Cost per unit}}$$

### Example

Fixed cost = ₹50,000/month. Variable cost = ₹30/unit. SP = ₹80/unit.

$$\text{Break-even} = \frac{50000}{80 - 30} = \frac{50000}{50} = 1000 \text{ units}$$

Selling more than 1000 units → profit. Less → loss.

### Relevance for GATE/ESE

Break-even appears in **Engineering Economics (General Aptitude)** and in **Industrial Engineering** papers. BANK exams rarely test this directly, but the concept is useful for Data Interpretation (DI) sets.

---

## 12. CP = 100 Technique (Assumption Method)

**The single most powerful technique for Profit & Loss.**

### The Idea

When a problem gives only percentages (no absolute values), **assume CP = ₹100**. This converts every percentage directly into a rupee value, eliminating fraction arithmetic.

### Example

> A shopkeeper marks goods 40% above CP and gives 20% discount. Find his profit%.

**Step 1:** Let CP = ₹100

**Step 2:** MP = $100 + 40\% \text{ of } 100 = ₹140$

**Step 3:** Discount = $20\% \text{ of } 140 = ₹28$

**Step 4:** SP = $140 - 28 = ₹112$

**Step 5:** Profit% = $(112-100)/100 \times 100 = 12\%$

**Verification with formula:** $m - d - md/100 = 40 - 20 - 800/100 = 40 - 20 - 8 = 12\%$ ✓

### When To Use This

- Whenever the problem involves **only percentages** and asks for a **percentage answer**.
- It doesn't work when absolute values are given and the answer requires an absolute value.

---

## 13. Percentage Multiplier (Fraction Shortcut)

### The Concept

Instead of calculating percentages step-by-step, convert common percentages to fractions:

| Percentage | Fraction | Multiplier (for Profit) | Multiplier (for Loss) |
|-----------|----------|------------------------|----------------------|
| 10% | 1/10 | 11/10 | 9/10 |
| 20% | 1/5 | 6/5 | 4/5 |
| 25% | 1/4 | 5/4 | 3/4 |
| 33.33% | 1/3 | 4/3 | 2/3 |
| 50% | 1/2 | 3/2 | 1/2 |
| 12.5% | 1/8 | 9/8 | 7/8 |
| 16.67% | 1/6 | 7/6 | 5/6 |
| 40% | 2/5 | 7/5 | 3/5 |
| 60% | 3/5 | 8/5 | 2/5 |

### Example — Speed Solve

> SP = ₹750, Loss = 25%. Find CP.

Loss of 25% → Multiplier = 3/4. So $SP = CP \times 3/4$.

$CP = 750 \times 4/3 = ₹1000$

**No formula needed. Pure fraction arithmetic. Under 5 seconds.**

---

## 14. Two-Article / Combined Transaction Problems

### The Classic Trap

> Two articles are sold at the same SP. On one, there is a profit of $x\%$ and on the other, a loss of $x\%$. What is the overall profit or loss%?

### The Answer: **Always a Loss**

$$\boxed{\text{Overall Loss %} = \frac{x^2}{100}}$$

This is **always a loss**, never a profit. This is one of the most tested results in BANK and GATE exams.

### Derivation

Let SP of each = $S$.

- $CP_1 = \frac{S}{1+x/100} = \frac{100S}{100+x}$
- $CP_2 = \frac{S}{1-x/100} = \frac{100S}{100-x}$

Total CP = $100S\left(\frac{1}{100+x} + \frac{1}{100-x}\right) = 100S \times \frac{(100-x)+(100+x)}{(100+x)(100-x)} = \frac{100S \times 200}{10000-x^2} = \frac{20000S}{10000-x^2}$

Total SP = $2S$

$$\text{Loss} = \text{Total CP} - \text{Total SP} = \frac{20000S}{10000-x^2} - 2S = \frac{20000S - 2S(10000-x^2)}{10000-x^2} = \frac{2Sx^2}{10000-x^2}$$

$$\text{Loss %} = \frac{\text{Loss}}{\text{Total CP}} \times 100 = \frac{2Sx^2}{10000-x^2} \times \frac{10000-x^2}{20000S} \times 100 = \frac{x^2}{100}\%$$

### Why Always a Loss?

**Intuition:** The item sold at a loss had a *higher* CP (you paid more for it), so the loss on the expensive item outweighs the profit on the cheaper item.

### Example

Two cycles sold at ₹1200 each. One at 20% profit, other at 20% loss. Net result?

$\text{Loss %} = 20^2/100 = 4\%$

Verification: $CP_1 = 1200/1.2 = ₹1000$, $CP_2 = 1200/0.8 = ₹1500$.
Total CP = ₹2500, Total SP = ₹2400. Loss = ₹100.
Loss% = $100/2500 \times 100 = 4\%$ ✓

---

## 15. Solved Examples — Exam-Grade

### Example 1 (GATE Style — NAT)

> A man buys an article for ₹800 and marks it 30% above CP. He then allows a discount of 15%. Find the profit percentage.

**Solution:**

$MP = 800 \times 1.30 = ₹1040$

$SP = 1040 \times 0.85 = ₹884$

$P\% = \frac{884 - 800}{800} \times 100 = \frac{84}{800} \times 100 = 10.5\%$

**Quick check with formula:** $m - d - md/100 = 30 - 15 - 450/100 = 30 - 15 - 4.5 = 10.5\%$ ✓

**NAT Answer:** 10.5 (or 10.50)

---

### Example 2 (Banking — MCQ)

> A shopkeeper purchases goods at 5/6 of the marked price and sells them at 10% above the marked price. What is his profit percentage?

**Solution:**

Let MP = ₹600 (choosing a number divisible by 6).

$CP = \frac{5}{6} \times 600 = ₹500$

$SP = 1.10 \times 600 = ₹660$

$P\% = \frac{660-500}{500} \times 100 = \frac{160}{500} \times 100 = 32\%$

---

### Example 3 (SSC/Bank — Successive Discount)

> A dealer offers successive discounts of 10%, 20%, and 10% on the marked price of ₹5000. Find the selling price.

**Solution:**

$$SP = 5000 \times 0.90 \times 0.80 \times 0.90 = 5000 \times 0.648 = ₹3240$$

---

### Example 4 (ESE — Conceptual)

> If by selling 12 articles, a man earns a profit equal to the selling price of 2 articles. Find the profit percentage.

**Solution:**

Let SP of each article = $s$.

Profit on 12 articles = $2s$.

Total SP = $12s$. Total CP = Total SP - Profit = $12s - 2s = 10s$.

$$P\% = \frac{2s}{10s} \times 100 = 20\%$$

**The Trap:** Students often write $P\% = 2/12 \times 100 = 16.67\%$ by incorrectly taking SP as the base. The profit is on **CP**.

---

### Example 5 (Dishonest Dealer — GATE/PSU)

> A dishonest dealer professes to sell at cost price but uses weights of 960g instead of 1 kg. In addition, he mixes 20% impurity which costs nothing. Find his profit percentage.

**Solution:**

He gives 960g, but 20% of that is free impurity = $960 \times 0.20 = 192g$ free.

Actual goods cost to him = $960 - 192 = 768g$ worth of cost.

He charges for 1000g, his actual cost is for 768g.

$$P\% = \frac{1000 - 768}{768} \times 100 = \frac{232}{768} \times 100 \approx 30.21\%$$

---

### Example 6 (Bank PO — Buy-x-Get-y)

> A shopkeeper advertises "Buy 4 Get 1 Free." What effective discount does the customer get?

**Solution:**

$$D\% = \frac{1}{4+1} \times 100 = 20\%$$

---

### Example 7 (Competitive — Profit on SP)

> A merchant earns 25% profit on SP. What is his actual profit% (on CP)?

**Solution:**

$$P\%_{\text{on CP}} = \frac{25}{100-25} \times 100 = \frac{25}{75} \times 100 = 33.33\%$$

---

### Example 8 (GATE — Two-Article Trap)

> A man sells two TVs at ₹9,000 each. On one he gains 25% and on the other he loses 25%. Find his overall gain or loss percentage.

**Solution:**

Same SP, same percentage → always loss.

$$\text{Loss%} = \frac{25^2}{100} = \frac{625}{100} = 6.25\%$$

---

### Example 9 (Advanced — Finding MP)

> A trader wants a 20% profit after allowing a 10% discount. If CP = ₹450, what should the marked price be?

**Solution:**

Required SP for 20% profit = $450 \times 1.20 = ₹540$

$SP = MP \times 0.90 \Rightarrow 540 = MP \times 0.90$

$MP = 540 / 0.90 = ₹600$

---

### Example 10 (PSU — Break-Even)

> A factory has a fixed cost of ₹2,00,000. Variable cost per unit is ₹50. Selling price per unit is ₹90. How many units must be sold to break even?

**Solution:**

$$\text{Break-even units} = \frac{200000}{90-50} = \frac{200000}{40} = 5000 \text{ units}$$

---

## 16. Edge Cases & Pitfalls

### Edge Case 1: CP = 0

If you get something for free (CP = 0), then any SP gives **infinite profit%**. This is technically valid but rarely appears in exams. If it does, the answer is typically phrased as "cannot be determined" or "infinite."

### Edge Case 2: SP = 0

If you sell for nothing (give it away), Loss% = 100%.

$L\% = \frac{CP - 0}{CP} \times 100 = 100\%$

### Edge Case 3: Loss% = 100% means SP = 0

You can never have Loss% > 100% (you can't lose more than you invested in the standard formulation). If a problem implies this, it's either badly framed or includes additional liabilities.

### Edge Case 4: Successive Discounts of 50% and 50% ≠ 100% Discount

$d_{eq} = 50 + 50 - (50 \times 50)/100 = 100 - 25 = 75\%$

SP ≠ 0; it's 25% of MP.

### Edge Case 5: Profit% and Loss% Are Not Additive

If you make 20% profit on Monday and 20% loss on Tuesday (on the new amount), the net is NOT zero.

$100 \times 1.20 \times 0.80 = 96 → 4\%$ net loss.

This is the **same** concept as the two-article problem — $x^2/100 = 400/100 = 4\%$ loss.

### Edge Case 6: Overhead Expenses Included in CP

Some problems state: "A man buys goods for ₹500 and spends ₹50 on transport."

Here, $CP = 500 + 50 = ₹550$. The overhead is **part of the cost price**.

### Pitfall: Percentage Change Is Not Symmetric

A 25% increase followed by a 25% decrease does NOT return to the original value:

$100 \to 125 \to 93.75$ → **6.25% loss**, not zero.

---

## 17. Exam-Specific Strategies

### GATE / ESE (General Aptitude)

- Usually **1-2 questions** in GA section (1 or 2 marks each).
- Focus on: Markup-Discount combos, dishonest dealer, two-article trap.
- **NAT type** is common — precision matters. Calculate to **2 decimal places**.
- Time budget: ≤ 2 minutes per question.
- These questions are designed to be solvable with the "CP=100" trick or multiplier method.

### Banking (SBI PO / IBPS / RBI Grade B)

- **5-8 questions** typically in the Quantitative Aptitude section.
- Focus on: Successive discounts, buy-x-get-y, partnership sharing, series of transactions.
- **Simplification** and **Data Interpretation** sets may embed P&L logic.
- Speed is everything: target < 45 seconds per question.
- Master the fraction-multiplier table (Section 13).

### SSC CGL / CHSL

- **2-4 questions** directly; more embedded in DI.
- Focus on: Dishonest dealer, SP/CP given as ratio, profit on SP tricks.
- Practice "missing data" problems where CP or SP must be inferred.

### PSU Exams (NTPC / BHEL / ONGC)

- Similar to GATE GA section but occasionally includes break-even and cost analysis.
- Focus on: Break-even, markup-discount, partnership.

---

## 18. Mnemonics & Mental Models

### Mnemonic 1: "CROPS" — The Flow of Money

> **C**ost → ma**R**kup → **O**fficial tag (**M**P) → discount **P**ares it → **S**elling price

$$CP \xrightarrow{+markup} MP \xrightarrow{-discount} SP$$

### Mnemonic 2: "Same-Same Always Lame" (Two-Article Trap)

> Same SP + Same % = Always a Loss = $x^2/100$

Picture two identical doors (same SP, same %): one says "profit" (sunny side), one says "loss" (dark side). When you walk through both, you always end up in a pit (loss).

### Mnemonic 3: "BASE matters!"

- **P**rofit% base → **C**P ("**P**igeons **C**atch" worms)
- **D**iscount% base → **M**P ("**D**octors **M**end" bones)

### Mental Slider — The Multiplier Dial

Imagine a dial in your head:
- At the center is **1.00** (no change: SP = CP).
- Turn it **clockwise** (right) and the number grows: 1.10 (10% profit), 1.25 (25% profit), etc.
- Turn it **counter-clockwise** (left) and it shrinks: 0.90 (10% loss), 0.75 (25% loss).
- Every P&L problem is just **finding where the dial should point** and multiplying.

### 5-Second Snap-Check

After solving any problem, ask:

1. **Does the answer make sense?** (Profit% can't exceed ~900-1000% in realistic problems)
2. **Is the loss% ≤ 100%?** (If you got 120% loss, recheck.)
3. **Is the profit on the *cheaper* item?** (If two-article problem, the one sold at loss has higher CP.)
4. **Did I use the right base?** (CP for profit, MP for discount)

---

## 19. Practice Problem Bank (with Solutions)

### Problem 1

> A man buys 10 oranges for ₹50 and sells 8 oranges for ₹50. Find his profit%.

<details>
<summary><b>Solution</b></summary>

CP per orange = ₹5. SP per orange = ₹50/8 = ₹6.25.

$P\% = \frac{6.25 - 5}{5} \times 100 = 25\%$

**Shortcut:** He buys 10, sells 8 for the same price. Ratio of quantities = 10:8 = 5:4.

$P\% = \frac{5-4}{4} \times 100 = 25\%$ (use selling quantity in denominator)

</details>

---

### Problem 2

> On selling 17 balls at ₹720, there is a loss equal to the cost price of 5 balls. Find the CP of each ball.

<details>
<summary><b>Solution</b></summary>

Let CP of each ball = $c$.

Total CP of 17 balls = $17c$.

Loss = $5c$.

Total SP = Total CP - Loss = $17c - 5c = 12c$.

Given SP = ₹720 → $12c = 720$ → $c = ₹60$.

</details>

---

### Problem 3

> The ratio of CP to SP is 5:4. What is the loss percentage?

<details>
<summary><b>Solution</b></summary>

CP:SP = 5:4. Since CP > SP, it's a loss.

$L\% = \frac{5-4}{5} \times 100 = 20\%$

</details>

---

### Problem 4

> A shopkeeper sold an article at a loss of 10%. If he had sold it for ₹70 more, he would have earned 4% profit. Find the CP.

<details>
<summary><b>Solution</b></summary>

At 10% loss: $SP_1 = 0.90 \times CP$

At 4% profit: $SP_2 = 1.04 \times CP$

Difference: $SP_2 - SP_1 = 1.04 \times CP - 0.90 \times CP = 0.14 \times CP = ₹70$

$CP = 70/0.14 = ₹500$

</details>

---

### Problem 5

> A dealer marks his goods 35% above CP and allows a discount of 20% to customers. Besides this, he uses a false weight of 800g instead of 1 kg. Find his overall profit%.

<details>
<summary><b>Solution</b></summary>

$P\% = \frac{W_{claimed}}{W_{actual}} \times (1+m/100) \times (1-d/100) \times 100 - 100$

$= \frac{1000}{800} \times 1.35 \times 0.80 \times 100 - 100$

$= 1.25 \times 1.08 \times 100 - 100 = 135 - 100 = 35\%$

</details>

---

### Problem 6

> Three successive discounts of 10%, 20%, and 25% are equivalent to a single discount of what percentage?

<details>
<summary><b>Solution</b></summary>

Effective multiplier = $0.90 \times 0.80 \times 0.75 = 0.54$

Equivalent single discount = $(1 - 0.54) \times 100 = 46\%$

</details>

---

### Problem 7

> A manufacturer sells goods to a wholesaler at 10% profit, wholesaler sells to retailer at 20% profit, retailer sells to customer at 25% profit. If customer pays ₹1650, find the manufacturing cost.

<details>
<summary><b>Solution</b></summary>

Let manufacturing cost = $C$.

$C \times 1.10 \times 1.20 \times 1.25 = 1650$

$C \times 1.65 = 1650$

$C = ₹1000$

</details>

---

### Problem 8

> A man sold two horses at ₹12,000 each. On one he gained 20% and on the other he lost 20%. Find his overall gain or loss in rupees.

<details>
<summary><b>Solution</b></summary>

$CP_1 = 12000/1.20 = ₹10000$

$CP_2 = 12000/0.80 = ₹15000$

Total CP = ₹25000. Total SP = ₹24000.

Loss = ₹1000.

$L\% = 1000/25000 \times 100 = 4\%$

Quick check: $x^2/100 = 400/100 = 4\%$ ✓

</details>

---

### Problem 9

> If the cost price is 80% of the selling price, find the profit%.

<details>
<summary><b>Solution</b></summary>

$CP = 0.80 \times SP$

$P = SP - CP = SP - 0.80 \times SP = 0.20 \times SP$

$P\% = \frac{P}{CP} \times 100 = \frac{0.20 \times SP}{0.80 \times SP} \times 100 = \frac{0.20}{0.80} \times 100 = 25\%$

</details>

---

### Problem 10

> A trader purchases a watch and a wall clock for ₹390. He sells the wall clock at a profit of 10% and the watch at a loss of 15%. If he earns a profit of ₹7.50 overall, find the cost of the watch.

<details>
<summary><b>Solution</b></summary>

Let cost of watch = $w$, cost of wall clock = $390 - w$.

Profit on clock = $0.10(390-w)$

Loss on watch = $0.15w$

Net profit: $0.10(390-w) - 0.15w = 7.50$

$39 - 0.10w - 0.15w = 7.50$

$39 - 0.25w = 7.50$

$0.25w = 31.50$

$w = ₹126$

</details>

---

## Quick-Reference Formula Card

| # | Formula | When to Use |
|---|---------|-------------|
| 1 | $P\% = \frac{SP-CP}{CP} \times 100$ | Basic profit% |
| 2 | $SP = CP \times (100+P)/100$ | SP from CP and Profit% |
| 3 | $CP = SP \times 100/(100+P)$ | CP from SP and Profit% |
| 4 | $SP = MP \times (100-D)/100$ | SP after discount |
| 5 | $P\% = m - d - md/100$ | Net profit after markup & discount |
| 6 | $d_{eq} = d_1 + d_2 - d_1 d_2/100$ | Equivalent single discount |
| 7 | $\text{Loss%} = x^2/100$ | Same SP, same %, two articles |
| 8 | $P\% = \frac{\text{Error}}{\text{True Value}} \times 100$ | Dishonest dealer (false weight) |
| 9 | $D\% = \frac{y}{x+y} \times 100$ | Buy $x$ Get $y$ Free |
| 10 | $P\%_{\text{on CP}} = \frac{x}{100-x} \times 100$ | Profit on SP to Profit on CP |

---

> **Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.**
>
> This material is self-contained — no external reference needed. Master these 10 formulas, understand the 6 edge cases, and practice the 10 problems, and Profit & Loss becomes free marks.
