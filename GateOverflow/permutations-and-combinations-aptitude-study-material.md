# Permutations and Combinations — Complete Study Material

> **Target Exams:** GATE · ESE · PSU · BANK (SSC CGL, IBPS PO/Clerk, SBI, RBI)
>
> **Philosophy:** Every formula is derived from scratch. No rote memorization — only understanding.

---

## Table of Contents

1. [Fundamental Counting Principle](#1-fundamental-counting-principle)
2. [Factorials](#2-factorials)
3. [Permutations (Arrangements)](#3-permutations-arrangements)
4. [Combinations (Selections)](#4-combinations-selections)
5. [Relationship Between $P$ and $C$](#5-relationship-between-p-and-c)
6. [Permutations with Repetition](#6-permutations-with-repetition)
7. [Permutations of Objects with Identical Items](#7-permutations-of-objects-with-identical-items)
8. [Circular Permutations](#8-circular-permutations)
9. [Combinations with Repetition](#9-combinations-with-repetition)
10. [Division and Distribution](#10-division-and-distribution)
11. [Derangements](#11-derangements)
12. [The Inclusion–Exclusion Principle](#12-the-inclusionexclusion-principle)
13. [Geometrical Applications](#13-geometrical-applications)
14. [Rank of a Word (Lexicographic Order)](#14-rank-of-a-word-lexicographic-order)
15. [Summation Identities & Properties of $\binom{n}{r}$](#15-summation-identities--properties-of-binomnr)
16. [Tricks, Shortcuts & Exam Heuristics](#16-tricks-shortcuts--exam-heuristics)
17. [GATE / ESE / PSU — Solved Problems](#17-gate--ese--psu--solved-problems)
18. [Banking Exam — Solved Problems](#18-banking-exam--solved-problems)
19. [Common Traps & Edge Cases](#19-common-traps--edge-cases)
20. [Quick-Revision Cheat Sheet](#20-quick-revision-cheat-sheet)

---

## 1. Fundamental Counting Principle

### 1.1 Multiplication Principle (AND-rule)

> **Atomic Truth:** Independent successive choices **multiply**.

If task $A$ can be done in $m$ ways **AND** task $B$ can be done in $n$ ways, then doing both $A$ **then** $B$ can be done in $m \times n$ ways.

**Why does it work?**
Think of a tree. Every branch of $A$ spawns $n$ sub-branches for $B$. Total leaves = $m \times n$.

**Analogy — The Outfit Problem:**
You own 4 shirts and 3 trousers. Each shirt can pair with each trouser independently.
Total outfits = $4 \times 3 = 12$.

> **Generalization:** If there are $k$ sequential tasks with $n_1, n_2, \ldots, n_k$ choices respectively, total ways = $n_1 \times n_2 \times \cdots \times n_k$.

### 1.2 Addition Principle (OR-rule)

> If task $A$ can be done in $m$ ways **OR** task $B$ can be done in $n$ ways (mutually exclusive), then doing **either** gives $m + n$ ways.

**When to add?** When the choices are **alternatives** (you pick one path, not both).

**Example:** Travel from Delhi to Mumbai by **train** (5 options) **or flight** (3 options).
Total = $5 + 3 = 8$ ways.

### 1.3 How to Decide: Multiply or Add?

| Keyword / Situation | Rule | Operation |
|---|---|---|
| "and", "then", "followed by" | Multiplication | $\times$ |
| "or", "either … or", "alternatively" | Addition | $+$ |

**Edge Case:** If alternatives are NOT mutually exclusive, use Inclusion–Exclusion (Section 12).

---

## 2. Factorials

### 2.1 Definition

$$n! = n \times (n-1) \times (n-2) \times \cdots \times 2 \times 1$$

$n!$ counts the number of ways to **arrange $n$ distinct objects in a row**.

### 2.2 Why $0! = 1$

There is exactly **1 way** to arrange zero objects — do nothing. This is the empty arrangement.

Formally, the recurrence $n! = n \times (n-1)!$ at $n = 1$ gives $1! = 1 \times 0!$, so $0! = 1$.

### 2.3 Key Factorial Values

| $n$ | $n!$ |
|---|---|
| 0 | 1 |
| 1 | 1 |
| 2 | 2 |
| 3 | 6 |
| 4 | 24 |
| 5 | 120 |
| 6 | 720 |
| 7 | 5040 |
| 8 | 40320 |
| 9 | 362880 |
| 10 | 3628800 |

**Trick:** Memorize up to $7! = 5040$. Beyond that, compute from $7!$.

### 2.4 Useful Properties

- $n! = n \times (n-1)!$
- $\frac{n!}{(n-k)!} = n(n-1)(n-2)\cdots(n-k+1)$ → a **falling product** of $k$ terms.

---

## 3. Permutations (Arrangements)

### 3.1 What is a Permutation?

> A permutation is an **ordered arrangement** of objects. **Order matters.**

"AB" and "BA" are **different** permutations.

### 3.2 Deriving ${}^nP_r$

**Problem:** From $n$ distinct objects, arrange $r$ objects in a row.

- 1st position: $n$ choices
- 2nd position: $n - 1$ choices
- 3rd position: $n - 2$ choices
- …
- $r$-th position: $n - r + 1$ choices

By the multiplication principle:

$${}^nP_r = n(n-1)(n-2) \cdots (n-r+1)$$

This is a product of **$r$ consecutive descending integers** starting from $n$.

**Closed form:** Multiply and divide by $(n-r)!$:

$${}^nP_r = \frac{n!}{(n-r)!}$$

### 3.3 Special Cases

| Case | Formula | Why |
|---|---|---|
| Arrange all $n$ objects | ${}^nP_n = n!$ | $(n - n)! = 0! = 1$ |
| Choose 0 objects | ${}^nP_0 = 1$ | Do nothing → 1 way |
| Choose 1 object | ${}^nP_1 = n$ | Just pick one |

### 3.4 Worked Example

**Q:** How many 3-letter "words" can be formed from {A, B, C, D, E} without repetition?

**Solution:**
$${}^5P_3 = \frac{5!}{(5-3)!} = \frac{120}{2} = 60$$

Or directly: $5 \times 4 \times 3 = 60$.

---

## 4. Combinations (Selections)

### 4.1 What is a Combination?

> A combination is a **selection** of objects where **order does NOT matter**.

{A, B} and {B, A} are the **same** combination.

### 4.2 Deriving ${}^nC_r$ (The Aha Moment)

**Key Insight:** Every **combination** of $r$ objects can be **arranged** in $r!$ ways.

So:

$$\text{(Permutations)} = \text{(Combinations)} \times r!$$

$${}^nP_r = {}^nC_r \times r!$$

$$\boxed{{}^nC_r = \frac{n!}{r!(n-r)!}}$$

**Analogy — The Committee Problem:**
Choosing a committee of 3 from 5 people is a combination.
Assigning them as President, VP, Secretary is a permutation.
$${}^5C_3 = \frac{{}^5P_3}{3!} = \frac{60}{6} = 10$$

### 4.3 Special Cases & Properties

| Property | Formula | Intuition |
|---|---|---|
| Symmetry | ${}^nC_r = {}^nC_{n-r}$ | Choosing $r$ to include = choosing $n - r$ to exclude |
| All or none | ${}^nC_0 = {}^nC_n = 1$ | One way to pick nothing / everything |
| Pick one | ${}^nC_1 = n$ | Just select one item |
| Pascal's Identity | ${}^nC_r = {}^{n-1}C_{r-1} + {}^{n-1}C_r$ | Either a specific item is chosen, or it is not |

### 4.4 Pascal's Identity — Why It Works

Consider a specific element $x$ in a set of $n$ elements. When choosing $r$ items:

- **Case 1 — $x$ is chosen:** Choose remaining $r-1$ from the other $n-1$ → ${}^{n-1}C_{r-1}$
- **Case 2 — $x$ is NOT chosen:** Choose all $r$ from the other $n-1$ → ${}^{n-1}C_r$

These are mutually exclusive and exhaustive:

$${}^nC_r = {}^{n-1}C_{r-1} + {}^{n-1}C_r$$

### 4.5 Worked Example

**Q:** From 8 players, select a team of 5.

$${}^8C_5 = {}^8C_3 = \frac{8 \times 7 \times 6}{3 \times 2 \times 1} = 56$$

**Trick applied:** ${}^8C_5 = {}^8C_3$ (use the smaller of $r$ and $n - r$ to reduce computation).

---

## 5. Relationship Between $P$ and $C$

$${}^nP_r = {}^nC_r \times r!$$

| Concept | Order | Formula |
|---|---|---|
| Permutation | Matters | $\frac{n!}{(n-r)!}$ |
| Combination | Does NOT matter | $\frac{n!}{r!(n-r)!}$ |

**The Golden Pivot:** *Ask yourself — does the order of selection matter?*

- **Yes → Permutation** (arranging books on a shelf)
- **No → Combination** (choosing books to carry)

---

## 6. Permutations with Repetition

### 6.1 The Setup

From $n$ distinct objects, arrange $r$ objects **where repetition is allowed**.

- 1st position: $n$ choices
- 2nd position: $n$ choices (repetition allowed)
- …
- $r$-th position: $n$ choices

$$\text{Total} = n^r$$

### 6.2 Example

**Q:** How many 4-digit PINs can be formed using digits {0–9}?

$$10^4 = 10{,}000$$

**Q:** Number of 3-letter codes from {A, B, C} with repetition?

$$3^3 = 27$$

### 6.3 Combinations with Repetition (Preview)

Selecting $r$ items from $n$ types with repetition (order irrelevant):

$${}^{n+r-1}C_r = \frac{(n+r-1)!}{r!(n-1)!}$$

(Detailed derivation in Section 9.)

---

## 7. Permutations of Objects with Identical Items

### 7.1 The Problem

Arrange $n$ objects where some are identical.

If there are $p$ identical objects of type 1, $q$ of type 2, $r$ of type 3, etc.:

$$\text{Arrangements} = \frac{n!}{p! \cdot q! \cdot r! \cdots}$$

### 7.2 Why This Works (The Derivation)

Consider the word "MISSISSIPPI" (11 letters):
- M: 1, I: 4, S: 4, P: 2

If all letters were distinct, arrangements = $11!$.

But swapping the 4 identical I's among themselves ($4!$ ways) gives the **same** word. Similarly for S ($4!$) and P ($2!$).

We **over-count** by a factor of $4! \times 4! \times 2!$.

$$\text{Distinct arrangements} = \frac{11!}{1! \cdot 4! \cdot 4! \cdot 2!} = \frac{39916800}{1 \times 24 \times 24 \times 2} = 34650$$

### 7.3 Quick-Check Template

| Word | Letters | Repetitions | Arrangements |
|---|---|---|---|
| APPLE | 5 | P×2 | $\frac{5!}{2!} = 60$ |
| BANANA | 6 | A×3, N×2 | $\frac{6!}{3! \cdot 2!} = 60$ |
| SUCCESS | 7 | S×3, C×2 | $\frac{7!}{3! \cdot 2!} = 420$ |

---

## 8. Circular Permutations

### 8.1 Why Circular is Different

In a **line**, ABCD and BCDA are different.
In a **circle**, ABCD and BCDA are the **same** (just a rotation).

A circular arrangement of $n$ objects has $n$ rotations that look identical. So we divide by $n$:

$$\text{Circular permutations of } n \text{ distinct objects} = \frac{n!}{n} = (n-1)!$$

### 8.2 Why $(n-1)!$? — The Fix-One Trick

**Fix** one person's position (to remove rotational symmetry). Then arrange the remaining $(n-1)$ people in $(n-1)!$ ways.

**Example:** Seat 6 people around a circular table.
$$= (6-1)! = 5! = 120$$

### 8.3 Necklace / Bracelet (Reflections Also Identical)

If the arrangement can be **flipped** (like a necklace), then clockwise and anticlockwise are the same:

$$\text{Necklace arrangements} = \frac{(n-1)!}{2}$$

**Example:** Arrange 6 beads on a necklace:
$$= \frac{5!}{2} = 60$$

### 8.4 Edge Cases

| Scenario | Formula |
|---|---|
| $n$ people at a round table | $(n-1)!$ |
| $n$ beads on a necklace (flippable) | $\frac{(n-1)!}{2}$ |
| $n$ keys on a keyring (flippable) | $\frac{(n-1)!}{2}$ |
| $n$ people in a line | $n!$ |

---

## 9. Combinations with Repetition (Stars and Bars)

### 9.1 The Problem

Select $r$ items from $n$ types, **repetition allowed**, **order irrelevant**.

**Example:** Buy 5 fruits from {Apple, Banana, Cherry}. How many different selections?

### 9.2 The Stars-and-Bars Derivation

Represent each selected item as a **star** ($\star$) and use **bars** ($|$) to separate types.

For 5 fruits from 3 types, one purchase might be:
- 2 Apples, 0 Bananas, 3 Cherries → $\star \star | \, | \star \star \star$

We need $r = 5$ stars and $n - 1 = 2$ bars. Total symbols = $r + n - 1 = 7$.

We choose positions for the bars (or equivalently the stars):

$$\boxed{{}^{n+r-1}C_r = {}^{n+r-1}C_{n-1}}$$

**Example answer:** ${}^{3+5-1}C_5 = {}^7C_5 = {}^7C_2 = 21$

### 9.3 The Stars-and-Bars Variants

| Problem Type | Formula |
|---|---|
| $x_1 + x_2 + \cdots + x_n = r$, $x_i \geq 0$ | ${}^{n+r-1}C_{r}$ |
| $x_1 + x_2 + \cdots + x_n = r$, $x_i \geq 1$ | ${}^{r-1}C_{n-1}$ (substitute $y_i = x_i - 1$) |

### 9.4 Example with Lower Bounds

**Q:** Distribute 10 identical balls into 4 distinct boxes, each box having at least 2 balls.

**Step 1:** Place 2 balls in each box → $4 \times 2 = 8$ balls used. Remaining = 2.

**Step 2:** Distribute 2 remaining balls into 4 boxes (no restrictions):
$${}^{4+2-1}C_2 = {}^5C_2 = 10$$

---

## 10. Division and Distribution

### 10.1 Distributing Distinct Objects into Distinct Groups

Distribute $n$ distinct objects into $r$ distinct groups of sizes $n_1, n_2, \ldots, n_r$ where $n_1 + n_2 + \cdots + n_r = n$:

$$\frac{n!}{n_1! \cdot n_2! \cdots n_r!}$$

This is the **multinomial coefficient**.

**Example:** Divide 10 students into groups of 5, 3, and 2:
$$\frac{10!}{5! \cdot 3! \cdot 2!} = \frac{3628800}{120 \times 6 \times 2} = 2520$$

### 10.2 Dividing into Equal-Sized Groups (Groups are Indistinguishable)

Divide $mn$ objects into $m$ **equal** groups of size $n$. If groups are **unlabeled**:

$$\frac{(mn)!}{(n!)^m \cdot m!}$$

The extra $m!$ in the denominator removes the ordering of the groups themselves.

**Example:** Divide 12 players into 3 equal teams of 4:
$$\frac{12!}{(4!)^3 \cdot 3!} = \frac{479001600}{13824 \times 6} = 5775$$

### 10.3 Distributing Identical Objects into Distinct Groups

This is the **stars-and-bars** problem (Section 9).

$$x_1 + x_2 + \cdots + x_r = n, \quad x_i \geq 0 \implies {}^{n+r-1}C_{r-1}$$

---

## 11. Derangements

### 11.1 What is a Derangement?

> A derangement is a permutation where **no element appears in its original position**.

**Analogy — The Hat Problem:** $n$ people throw their hats into a pile. Each picks a random hat. A derangement means nobody gets their own hat.

### 11.2 Formula Derivation (via Inclusion–Exclusion)

Let $A_i$ = event that person $i$ gets their own hat.

We want $|A_1^c \cap A_2^c \cap \cdots \cap A_n^c|$ (nobody in their original position).

By Inclusion–Exclusion:

$$D_n = n! \left[1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \cdots + (-1)^n \frac{1}{n!}\right]$$

$$\boxed{D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}}$$

### 11.3 Key Values

| $n$ | $D_n$ | $D_n / n!$ |
|---|---|---|
| 1 | 0 | 0 |
| 2 | 1 | 0.5 |
| 3 | 2 | 0.333 |
| 4 | 9 | 0.375 |
| 5 | 44 | 0.367 |
| 6 | 265 | 0.368 |

**Key Observation:** As $n \to \infty$, $D_n / n! \to 1/e \approx 0.3679$.

### 11.4 Recurrence Relation

$$D_n = (n-1)(D_{n-1} + D_{n-2})$$

**Why?** Person 1's hat goes to person $j$ ($n-1$ choices). Then either:
- Person $j$ takes person 1's hat → remaining is $D_{n-2}$, or
- Person $j$ does NOT take person 1's hat → remaining is $D_{n-1}$.

### 11.5 Worked Example

**Q:** How many derangements of {1, 2, 3, 4}?

$$D_4 = 4!\left(\frac{1}{0!} - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \frac{1}{4!}\right)$$
$$= 24\left(1 - 1 + \frac{1}{2} - \frac{1}{6} + \frac{1}{24}\right) = 24 \times \frac{9}{24} = 9$$

**Verification via recurrence:** $D_1 = 0, D_2 = 1$, $D_3 = 2(1+0) = 2$, $D_4 = 3(2+1) = 9$. ✓

---

## 12. The Inclusion–Exclusion Principle

### 12.1 The Formula

For two sets:
$$|A \cup B| = |A| + |B| - |A \cap B|$$

For three sets:
$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$$

**General:**
$$\left|\bigcup_{i=1}^n A_i\right| = \sum|A_i| - \sum|A_i \cap A_j| + \sum|A_i \cap A_j \cap A_k| - \cdots$$

### 12.2 "At least one" ↔ "Total minus none"

$$|A \cup B| = |U| - |A^c \cap B^c|$$

This is the **complementary counting** technique — often the fastest approach.

### 12.3 Classic Application — Euler's Totient

$\phi(n)$ = count of integers from 1 to $n$ that are coprime to $n$.

If $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$:

$$\phi(n) = n\left(1 - \frac{1}{p_1}\right)\left(1 - \frac{1}{p_2}\right)\cdots\left(1 - \frac{1}{p_k}\right)$$

This is Inclusion–Exclusion applied to multiples of each prime factor.

### 12.4 Worked Example

**Q:** How many integers from 1 to 100 are divisible by 2 or 3?

- $|A|$ = multiples of 2 = $\lfloor 100/2 \rfloor = 50$
- $|B|$ = multiples of 3 = $\lfloor 100/3 \rfloor = 33$
- $|A \cap B|$ = multiples of 6 = $\lfloor 100/6 \rfloor = 16$
- $|A \cup B| = 50 + 33 - 16 = 67$

---

## 13. Geometrical Applications

### 13.1 Lines, Triangles, Diagonals from Points

Given $n$ points, **no three collinear**:

| Shape | Formula | Why |
|---|---|---|
| Lines (straight) | ${}^nC_2$ | Any 2 points determine a line |
| Triangles | ${}^nC_3$ | Any 3 non-collinear points determine a triangle |

### 13.2 If $m$ Points are Collinear

- **Lines:** ${}^nC_2 - {}^mC_2 + 1$ (the $m$ collinear points form just 1 line, not ${}^mC_2$)
- **Triangles:** ${}^nC_3 - {}^mC_3$ (3 collinear points cannot form a triangle)

### 13.3 Diagonals of a Polygon

An $n$-sided polygon:
- Total lines from vertices: ${}^nC_2$
- Sides: $n$

$$\text{Diagonals} = {}^nC_2 - n = \frac{n(n-1)}{2} - n = \frac{n(n-3)}{2}$$

**Quick values:**

| Polygon | $n$ | Diagonals |
|---|---|---|
| Triangle | 3 | 0 |
| Quadrilateral | 4 | 2 |
| Pentagon | 5 | 5 |
| Hexagon | 6 | 9 |
| Decagon | 10 | 35 |

### 13.4 Rectangles and Squares in a Grid

In a grid with $m$ horizontal and $n$ vertical lines:

$$\text{Rectangles} = {}^mC_2 \times {}^nC_2$$

**Why?** A rectangle is uniquely determined by choosing 2 horizontal lines and 2 vertical lines.

### 13.5 Intersection Points

$n$ lines in general position (no two parallel, no three concurrent):

$$\text{Intersection points} = {}^nC_2$$

---

## 14. Rank of a Word (Lexicographic Order)

### 14.1 The Technique

To find the **rank** (dictionary position) of a word among all permutations of its letters:

1. Count all arrangements that come **before** the given word alphabetically.
2. Fix letters from left to right; for each position, count how many smaller letters could go there, and multiply by permutations of the remaining positions.

### 14.2 Worked Example — Rank of "GATE"

Letters in alphabetical order: A, E, G, T

**Position 1 (G):**
Letters smaller than G: A, E → 2 letters.
Each can lead to $3!$ arrangements: $2 \times 3! = 12$

**Position 2 (A):**
Fix G in position 1. Letters remaining: {A, E, T}. Letters smaller than A: none → 0.

**Position 3 (T):**
Fix G, A in positions 1, 2. Remaining: {E, T}. Letters smaller than T: E → 1.
$1 \times 1! = 1$

**Position 4 (E):**
Only one letter left. → 0

$$\text{Rank} = 12 + 0 + 1 + 0 + 1 = 14$$

(The $+1$ at the end counts the word "GATE" itself.)

### 14.3 With Repeated Letters

If the word has repeated letters, replace $k!$ with $\frac{k!}{\text{product of factorials of repetitions among remaining letters}}$.

**Example — Rank of "BALL":**
Letters sorted: A, B, L, L

Words starting with A: $\frac{3!}{2!} = 3$ (since L repeats twice in remaining)

Words starting with BA: fix B, A. Remaining: {L, L}. Letters before L among remaining: none → 0.

Words starting with BAL: fix B, A, L. Remaining: {L}. Only 1 arrangement → count it.

$$\text{Rank} = 3 + 0 + 1 = 4$$

Verification: ALL L, ABLL, ALBL, BALL → Rank 4 ✓ (wait, let's recount)

Alphabetical permutations of {A, B, L, L}:
1. ABLL
2. ALBL
3. ALLB
4. BALL ✓

---

## 15. Summation Identities & Properties of $\binom{n}{r}$

### 15.1 Core Identities

| Identity | Formula |
|---|---|
| Sum of a row | $\sum_{r=0}^{n} \binom{n}{r} = 2^n$ |
| Alternating sum | $\sum_{r=0}^{n} (-1)^r \binom{n}{r} = 0$ |
| Sum of first halves | $\binom{n}{0} + \binom{n}{1} + \cdots + \binom{n}{n} = 2^n$ |
| Vandermonde's Identity | $\binom{m+n}{r} = \sum_{k=0}^{r} \binom{m}{k}\binom{n}{r-k}$ |
| Hockey Stick | $\binom{r}{r} + \binom{r+1}{r} + \cdots + \binom{n}{r} = \binom{n+1}{r+1}$ |
| Weighted sum | $\sum_{r=0}^{n} r \binom{n}{r} = n \cdot 2^{n-1}$ |

### 15.2 Why $\sum \binom{n}{r} = 2^n$?

Each element is either **in** or **out** of a subset → $2^n$ total subsets.
The left side counts subsets by size: subsets of size 0, 1, 2, …, $n$.

### 15.3 Why $\sum (-1)^r \binom{n}{r} = 0$?

Set $x = -1$ in $(1+x)^n = \sum \binom{n}{r} x^r$.
$(1 + (-1))^n = 0^n = 0$ (for $n \geq 1$).

### 15.4 Vandermonde's Identity — Intuition

Choose $r$ items from a group of $m$ men and $n$ women.
Left side: directly choose $r$ from $m+n$.
Right side: choose $k$ men and $r - k$ women, summed over all valid $k$.

---

## 16. Tricks, Shortcuts & Exam Heuristics

### 16.1 The Complement Trick

> **"At least one" = Total − None**

**Example:** From a standard deck, how many 5-card hands have at least one ace?

Total 5-card hands: ${}^{52}C_5$
Hands with **no** ace: ${}^{48}C_5$
Answer: ${}^{52}C_5 - {}^{48}C_5$

### 16.2 The Gap Method (No Two Adjacent)

> To select $r$ non-adjacent items from $n$ items in a line:

$${}^{n-r+1}C_r$$

**Derivation:** Place $r$ selected items and create $r - 1$ mandatory gaps. Remaining $n - r$ items fill $r + 1$ possible gaps (before, between, after).

**Example:** Choose 3 non-adjacent seats from 10 in a row:
$${}^{10-3+1}C_3 = {}^8C_3 = 56$$

**Circular version:** $n$ items in a circle, select $r$ non-adjacent:
$$\frac{n}{n-r} \cdot {}^{n-r}C_r$$

### 16.3 Fix-and-Count for Constraints

When objects **must be together**: Treat the group as a **single unit**, arrange units, then arrange within the group.

When objects **must NOT be together**: Total arrangements − arrangements where they ARE together.

**Example:** Arrange 7 people such that A and B are always together.

- Treat {A, B} as one unit → 6 units → $6!$ arrangements.
- A and B can swap within the unit → $\times 2!$

$$= 6! \times 2! = 720 \times 2 = 1440$$

### 16.4 The Bijection Trick

Convert a hard counting problem into an equivalent easy one.

**Classic bijection:** "Number of non-negative integer solutions to $x_1 + x_2 + x_3 = 10$" is the same as "distributing 10 identical balls into 3 distinct boxes" → Stars and Bars.

### 16.5 Symmetry Shortcut for ${}^nC_r$

Always compute ${}^nC_r$ using $\min(r, n-r)$:

$${}^{100}C_{98} = {}^{100}C_2 = \frac{100 \times 99}{2} = 4950$$

### 16.6 The "Choose Then Arrange" Framework

For complex problems, break into:
1. **Selection** (combination) — who/what is chosen?
2. **Arrangement** (permutation) — in what order?

Multiply the two counts.

---

## 17. GATE / ESE / PSU — Solved Problems

### Problem 1 — Divisors (GATE-style NAT)

**Q:** How many positive divisors does $N = 2^3 \times 3^2 \times 5^1$ have?

**Solution:** Each divisor is of the form $2^a \times 3^b \times 5^c$ where:
- $0 \le a \le 3$ → 4 choices
- $0 \le b \le 2$ → 3 choices
- $0 \le c \le 1$ → 2 choices

$$\text{Divisors} = (3+1)(2+1)(1+1) = 4 \times 3 \times 2 = 24$$

---

### Problem 2 — Committee Formation (GATE MCQ)

**Q:** A committee of 5 is to be formed from 6 men and 4 women such that at least 2 women are included. How many ways?

**Solution:** "At least 2 women" → 2W, 3W, or 4W:

| Women | Men | Ways |
|---|---|---|
| 2 | 3 | ${}^4C_2 \times {}^6C_3 = 6 \times 20 = 120$ |
| 3 | 2 | ${}^4C_3 \times {}^6C_2 = 4 \times 15 = 60$ |
| 4 | 1 | ${}^4C_4 \times {}^6C_1 = 1 \times 6 = 6$ |

$$\text{Total} = 120 + 60 + 6 = 186$$

---

### Problem 3 — Arrangements with Constraints (ESE-style)

**Q:** In how many ways can the letters of "ENGINEERING" be arranged?

**Letters (11 total):** E-3, N-3, G-2, I-1, R-1 (wait, let's recount)

E-N-G-I-N-E-E-R-I-N-G → E:3, N:3, G:2, I:2, R:1 → total = 11

$$\frac{11!}{3! \cdot 3! \cdot 2! \cdot 2! \cdot 1!} = \frac{39916800}{6 \times 6 \times 2 \times 2 \times 1} = \frac{39916800}{144} = 277200$$

---

### Problem 4 — Circular Arrangement (GATE)

**Q:** In how many ways can 8 people be seated at a round table if 2 specific people must sit together?

**Solution:**
- Treat the 2 people as 1 unit → 7 units at a round table → $(7-1)! = 6!$
- The 2 people can swap → $\times 2!$

$$= 6! \times 2 = 720 \times 2 = 1440$$

---

### Problem 5 — Distribution (GATE NAT)

**Q:** Number of ways to distribute 12 identical balls into 4 distinct boxes such that no box is empty?

**Solution:** Each box must have $\geq 1$ ball. Use stars-and-bars with $x_i \geq 1$:

Substitute $y_i = x_i - 1$, then $y_1 + y_2 + y_3 + y_4 = 8$, $y_i \geq 0$:

$${}^{8+4-1}C_{4-1} = {}^{11}C_3 = \frac{11 \times 10 \times 9}{6} = 165$$

---

### Problem 6 — Functions (GATE CS)

**Q:** Number of onto functions from a set of 4 elements to a set of 3 elements?

**Solution:** By Inclusion–Exclusion, the number of onto (surjective) functions from $|A| = m$ to $|B| = n$:

$$\text{Onto} = \sum_{k=0}^{n} (-1)^k \binom{n}{k}(n-k)^m$$

Here $m=4, n=3$:
$$= \binom{3}{0}3^4 - \binom{3}{1}2^4 + \binom{3}{2}1^4 - \binom{3}{3}0^4$$
$$= 81 - 48 + 3 - 0 = 36$$

---

### Problem 7 — Derangements (GATE)

**Q:** 5 letters are placed in 5 addressed envelopes at random. What is the probability that no letter goes into its correct envelope?

$$P = \frac{D_5}{5!} = \frac{44}{120} = \frac{11}{30}$$

$D_5 = 5!(1 - 1 + 1/2 - 1/6 + 1/24 - 1/120) = 120 \times (44/120) = 44$

---

### Problem 8 — Grid Paths (GATE CS / IT)

**Q:** Number of shortest paths from $(0,0)$ to $(m,n)$ on a grid (moving only right or up)?

Each path consists of $m$ Right moves and $n$ Up moves → total $m + n$ moves.

$$\text{Paths} = \binom{m+n}{m} = \binom{m+n}{n}$$

**Example:** $(0,0)$ to $(4,3)$: $\binom{7}{3} = 35$

---

## 18. Banking Exam — Solved Problems

### Problem 1 — Word Formation

**Q:** How many words (meaningful or not) can be formed using all letters of "EQUATION" such that all vowels are together?

**Vowels:** E, U, A, I, O (5 vowels) | **Consonants:** Q, T, N (3 consonants)

- Treat 5 vowels as one unit → 4 units → $4!$ arrangements
- Vowels within the unit: $5!$ arrangements

$$= 4! \times 5! = 24 \times 120 = 2880$$

---

### Problem 2 — Selection with Restrictions

**Q:** From 7 consonants and 5 vowels, form words with 3 consonants and 2 vowels. How many words?

**Step 1 — Select:** ${}^7C_3 \times {}^5C_2 = 35 \times 10 = 350$ selections.

**Step 2 — Arrange:** Each selection of 5 letters can be arranged in $5! = 120$ ways.

$$= 350 \times 120 = 42000$$

---

### Problem 3 — Seating Arrangements

**Q:** 4 boys and 3 girls sit in a row such that no two girls sit together. How many ways?

**Step 1:** Arrange 4 boys: $4! = 24$ ways.

**Step 2:** This creates 5 gaps: _ B _ B _ B _ B _

**Step 3:** Place 3 girls in 5 gaps: ${}^5P_3 = 60$ ways.

$$= 24 \times 60 = 1440$$

---

### Problem 4 — Number Formation

**Q:** How many 4-digit numbers can be formed using {1, 2, 3, 4, 5} (no repetition) that are divisible by 4?

A number is divisible by 4 if its **last two digits** form a number divisible by 4.

**Two-digit endings divisible by 4 from {1,2,3,4,5}:** 12, 24, 32, 52 → 4 valid endings.

For each valid ending, remaining 2 positions from 3 remaining digits: ${}^3P_2 = 6$.

$$= 4 \times 6 = 24$$

---

### Problem 5 — Probability with Combinations

**Q:** A bag contains 5 red, 4 blue, and 3 green balls. If 3 balls are drawn at random, what is the probability that all are of different colors?

$$P = \frac{{}^5C_1 \times {}^4C_1 \times {}^3C_1}{{}^{12}C_3} = \frac{5 \times 4 \times 3}{220} = \frac{60}{220} = \frac{3}{11}$$

---

## 19. Common Traps & Edge Cases

### Trap 1: Forgetting "Order Matters vs. Doesn't"

The single biggest source of errors. Always ask: **"If I swap two selected items, do I get a different outcome?"**
- Forming a committee → NO → Combination
- Assigning roles (President, VP) → YES → Permutation

### Trap 2: Overcounting in Identical Groups

When dividing $2n$ objects into 2 equal groups:
$$\frac{(2n)!}{(n!)^2 \times 2!} \neq \frac{(2n)!}{(n!)^2}$$

The $2!$ removes the ordering of the two groups (Group 1 and Group 2 are interchangeable if unlabeled).

### Trap 3: Circular vs. Linear

Students often forget to use $(n-1)!$ for circular. **Test:** Are rotations considered the same?

### Trap 4: "At Least" Problems

Never enumerate cases from "at least 1" upward when complement is simpler.

$$P(\text{at least 1}) = 1 - P(\text{none})$$

### Trap 5: Stars-and-Bars with Upper Bounds

Stars and Bars directly handles $x_i \geq 0$ or $x_i \geq c_i$. For **upper bounds** ($x_i \leq M$), use Inclusion–Exclusion on top of Stars-and-Bars.

### Trap 6: Confusing ${}^nP_r$ and $n^r$

- ${}^nP_r$: arrangement **without** repetition
- $n^r$: arrangement **with** repetition

A PIN of 4 digits with repetition = $10^4$, NOT ${}^{10}P_4$.

### Trap 7: Necklace vs. Circular Table

- Round table: $(n-1)!$ (only rotations are same)
- Necklace: $\frac{(n-1)!}{2}$ (rotations AND reflections are same)

### Trap 8: Zero in Number-Formation Problems

When forming numbers, **0 cannot be the leading digit**.

**Example:** 4-digit numbers from {0,1,2,3,4}:
- First digit: 4 choices (1,2,3,4 — not 0)
- Remaining digits: ${}^4P_3 = 24$ (if no repetition)
- Total: $4 \times 24 = 96$ (NOT ${}^5P_4 = 120$)

### Trap 9: "Exactly $k$" via Inclusion–Exclusion

For "exactly $k$ items have property $P$":

$$\text{Exactly } k = \binom{n}{k} D_{n-k} \text{ (for derangement-type problems)}$$

Or use $P(\text{exactly } k) = \binom{n}{k} p^k (1-p)^{n-k}$ for independent Bernoulli trials.

### Trap 10: Double-Counting in Geometry

When counting rectangles in a grid, each rectangle is determined by **2 horizontal + 2 vertical** lines. Don't count individual unit rectangles and then try to combine.

---

## 20. Quick-Revision Cheat Sheet

### Core Formulas at a Glance

| Concept | Formula | When to Use |
|---|---|---|
| **Permutation** (no rep.) | $\frac{n!}{(n-r)!}$ | Ordered selection from distinct items |
| **Permutation** (with rep.) | $n^r$ | Ordered selection, repetition allowed |
| **Permutation** (identical items) | $\frac{n!}{p! q! r! \cdots}$ | Arranging with duplicates |
| **Combination** (no rep.) | $\frac{n!}{r!(n-r)!}$ | Unordered selection from distinct items |
| **Combination** (with rep.) | $\binom{n+r-1}{r}$ | Unordered selection, repetition allowed |
| **Circular Permutation** | $(n-1)!$ | Circular arrangement |
| **Necklace** | $\frac{(n-1)!}{2}$ | Circular + flippable |
| **Derangement** | $n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}$ | No element in original position |
| **Stars & Bars** ($x_i \geq 0$) | $\binom{n+r-1}{r}$ | Identical items into distinct bins |
| **Stars & Bars** ($x_i \geq 1$) | $\binom{r-1}{n-1}$ | Same, each bin non-empty |
| **Multinomial** | $\frac{n!}{n_1! n_2! \cdots n_k!}$ | Division into groups of known sizes |
| **Diagonals** | $\frac{n(n-3)}{2}$ | Diagonals of $n$-gon |
| **Grid Paths** | $\binom{m+n}{m}$ | Shortest paths in an $m \times n$ grid |
| **Onto Functions** | $\sum_{k=0}^{n}(-1)^k\binom{n}{k}(n-k)^m$ | Surjections from $m$-set to $n$-set |
| **Rectangles in Grid** | $\binom{m}{2}\binom{n}{2}$ | $m$ horizontal, $n$ vertical lines |

### Decision Flowchart

```
Start
  │
  ├─ Is ORDER important?
  │    ├─ YES → PERMUTATION
  │    │    ├─ Repetition allowed? → n^r
  │    │    ├─ Identical items? → n! / (p!q!r!…)
  │    │    ├─ Circular? → (n-1)!
  │    │    └─ Standard → nPr = n!/(n-r)!
  │    │
  │    └─ NO → COMBINATION
  │         ├─ Repetition allowed? → C(n+r-1, r)
  │         └─ Standard → nCr = n! / (r!(n-r)!)
  │
  ├─ Is it "at least" / "at most"?
  │    └─ Use COMPLEMENT: Total − Unwanted
  │
  ├─ Is it a DISTRIBUTION problem?
  │    ├─ Identical objects → Stars & Bars
  │    └─ Distinct objects → Multinomial
  │
  └─ Does it involve RESTRICTIONS (together / apart)?
       ├─ Together → Bundle them as one unit
       └─ Apart → Total − Together, or Gap method
```

### 5-Second Sanity Checks

1. **Does my answer exceed $n!$?** If arranging $n$ objects, the answer can't exceed $n!$.
2. **Is my answer negative or fractional?** Combinatorial answers are always non-negative integers.
3. **Symmetry check:** ${}^nC_r = {}^nC_{n-r}$. If $r > n/2$, rewrite using the complement.
4. **Small case verification:** Test with $n = 2$ or $n = 3$ and manually list all possibilities.
5. **Boundary check:** What happens when $r = 0$ or $r = n$? The answer should be 1.

### Bizarre Mnemonic — "The Party of n!"

> Imagine $n$ eccentric guests arriving at a party. $n!$ is the total chaos of all possible seating orders. The **bouncer** $r!$ at the door says "I don't care about your internal order" — he divides out the chaos to give you calm **Combinations**. If you want a **circular** party, nail one guest's chair to the floor (fix one position) → $(n-1)!$ remaining chaos.

---

*End of Study Material*

> **Coverage:** Fundamental Counting → Factorials → Permutations → Combinations → Repetition → Identical Objects → Circular → Stars-and-Bars → Distribution → Derangements → Inclusion-Exclusion → Geometry → Lexicographic Rank → Binomial Identities → Tricks → GATE/ESE Problems → Banking Problems → Traps → Cheat Sheet.
