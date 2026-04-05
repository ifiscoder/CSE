# Permutation and Combination Aptitude Study Material (GATE/ESE/PSU/BANK)

## 0) Exam Framing: Why This Topic Decides Rank

Permutation and Combination appears simple, but in competitive exams it has a high error rate because:

- candidates mix **order matters** vs **order does not matter**
- repeated objects and constraints are hidden in wording
- over-application of formulas without counting model checks

For exam speed, this chapter is not about memorizing many formulas. It is about selecting the right **counting model** in seconds.

---

## 1) The Atomic Truth (Aha Core)

**Count outcomes by constructing choice steps.**

Everything in this chapter comes from:

- Rule of Product (multiplication principle)
- Rule of Sum (addition principle)
- divide by overcount when identical arrangements are counted multiple times

---

## 2) First Principles Derivation of Core Formulas

### 2.1 Factorial and Why It Appears

Number of ways to arrange \(n\) distinct objects in a line:

\[
n\times(n-1)\times(n-2)\times\cdots\times1=n!
\]

with \(0!=1\) (empty arrangement convention, needed for consistency).

### 2.2 Permutations \(^{n}P_r\)

Choose and arrange \(r\) positions from \(n\) distinct objects:

\[
^{n}P_r=n(n-1)\cdots(n-r+1)=\frac{n!}{(n-r)!}
\]

### 2.3 Combinations \(^{n}C_r\)

First count ordered selections \(^{n}P_r\).  
Each unordered group of \(r\) is counted \(r!\) times due to internal rearrangements.

\[
^{n}C_r=\frac{^{n}P_r}{r!}=\frac{n!}{r!(n-r)!}
\]

### 2.4 Relation Between Them

\[
^{n}P_r=\,^{n}C_r\cdot r!
\]

This is one of the fastest conversion identities in exam solving.

### 2.5 Symmetry of Combinations

\[
^{n}C_r=\,^{n}C_{n-r}
\]

Reason: choosing \(r\) to include is equivalent to choosing \(n-r\) to exclude.

---

## 3) Decision Engine: Which Model to Use in 5 Seconds

1. Are we **arranging**? (positions matter) \(\Rightarrow\) permutation.
2. Are we **selecting/grouping**? (positions ignored) \(\Rightarrow\) combination.
3. Are objects identical? \(\Rightarrow\) divide by factorial(s) of identical counts.
4. Any restrictions (together, apart, no adjacency, fixed ends, at least/at most)?  
   \(\Rightarrow\) use casework/complement/gap method.

---

## 4) Complete Formula Vault with Derivations/Use Cases

### 4.1 Arrangements of \(n\) Distinct in a Line

\[
n!
\]

Use: seating in a row, ranking, code ordering.

### 4.2 Arrangements of \(n\) Distinct in a Circle

If only relative rotations are same:

\[
(n-1)!
\]

Reason: fix one object as anchor; arrange remaining \(n-1\).

If clockwise and anticlockwise also considered same (necklace-type mirror equivalence for all distinct):

\[
\frac{(n-1)!}{2}
\]

### 4.3 Permutations with Repetition Allowed (length \(r\), \(n\) choices each slot)

\[
n^r
\]

Use: passwords, strings, digit sequences with reuse.

### 4.4 Permutations of Multiset (Repeated Objects)

For total \(n\) with counts \(a,b,c,\dots\), \(a+b+c+\cdots=n\):

\[
\frac{n!}{a!\,b!\,c!\cdots}
\]

Reason: divide by internal swaps among identical items.

### 4.5 Combination with Repetition (Stars and Bars)

Number of nonnegative integer solutions to:

\[
x_1+x_2+\cdots+x_k=n
\]

is

\[
{n+k-1 \choose k-1}
\]

Derivation: \(n\) stars + \(k-1\) bars; choose bar positions among \(n+k-1\).

### 4.6 Positive Integer Solutions

For

\[
x_1+\cdots+x_k=n,\quad x_i\ge1
\]

set \(y_i=x_i-1\), then \(y_i\ge0\), \(\sum y_i=n-k\):

\[
{n-1 \choose k-1}
\]

### 4.7 Inclusion-Exclusion (At Least One Condition)

\[
|A\cup B|=|A|+|B|-|A\cap B|
\]

\[
|A\cup B\cup C|=\sum|A_i|-\sum|A_i\cap A_j|+|A\cap B\cap C|
\]

Use for “contains at least one vowel”, “divisible by 2 or 3”, etc.

---

## 5) High-Value Exam Patterns (with Worked Examples)

## Pattern A: Order vs Selection

**Q:** From 8 students, choose captain and vice-captain.  
**Ans:** \(^{8}P_2=8\times7=56\)

**Q:** From 8 students, choose 2 representatives.  
**Ans:** \(^{8}C_2=28\)

Key: titles imply order.

## Pattern B: “Together” Constraint

**Q:** In how many ways can A, B, C, D, E be arranged if A and B are together?

Treat \(AB\) as one block: objects = \((AB),C,D,E\) \(\Rightarrow 4!\)  
Inside block: \(AB\) or \(BA\) \(\Rightarrow 2\)

\[
4!\cdot2=48
\]

## Pattern C: “Not Together”

Total arrangements \(=5!=120\)  
Together \(=48\)  
Not together:

\[
120-48=72
\]

Complement is fastest.

## Pattern D: No Two Specific Items Adjacent (Gap Method)

Arrange non-targets first, place targets in gaps.

Example: arrange A, B, C, D, E, F with A and B not adjacent.

Total: \(6!=720\)  
Adjacent: treat AB block \(\Rightarrow 5!\cdot2=240\)  
Not adjacent:

\[
720-240=480
\]

## Pattern E: Repeated Letters

**Q:** Arrangements of “BALLOON”.

Letters: 7 total, \(L\) repeated 2, \(O\) repeated 2.

\[
\frac{7!}{2!\,2!}=1260
\]

## Pattern F: Circular Seating

**Q:** 6 persons around a round table:

\[
(6-1)!=120
\]

If two seatings that are mirror images are same (rare unless explicitly stated):

\[
\frac{120}{2}=60
\]

## Pattern G: Distribution with No Upper Bound

**Q:** Number of ways to distribute 10 identical balls among 4 boxes:

\[
x_1+x_2+x_3+x_4=10,\ x_i\ge0
\]

\[
{10+4-1 \choose 4-1}={13 \choose 3}=286
\]

## Pattern H: Each Box At Least One

\[
x_1+x_2+x_3+x_4=10,\ x_i\ge1
\Rightarrow {9 \choose 3}=84
\]

---

## 6) Advanced Techniques for Speed

### 6.1 Complement Counting

For “at least one” / “none” style statements:

\[
\text{required}=\text{total}-\text{forbidden}
\]

Usually 2–5x faster than direct casework.

### 6.2 Slot/Gap Method

To avoid adjacency, arrange base objects first and then choose gaps.

If \(m\) base objects in a row, gaps = \(m+1\).

### 6.3 Block Method

Items together \(\Rightarrow\) convert many objects into one super-object.

### 6.4 Symmetry Shortcuts

\[
^{n}C_r=\,^{n}C_{n-r}
\]

Compute with smaller \(r\) for speed and fewer arithmetic mistakes.

### 6.5 Ratio/Cancel Early

Avoid huge factorial expansion:

\[
{20 \choose 3}=\frac{20\cdot19\cdot18}{3\cdot2\cdot1}=1140
\]

not full \(20!\) expansions.

---

## 7) Edge Cases (Frequently Ignored, Mark-Losing)

1. \(0!=1\), \(^{n}C_0=1\), \(^{n}P_0=1\)
2. \(^{n}C_r=0\) for \(r>n\)
3. \(^{n}P_r=0\) for \(r>n\) when repetition not allowed
4. Repetition allowed vs not allowed must be checked from statement
5. Circular problems: verify if reflections are distinct or not
6. Identical objects cannot be treated as distinct placeholders

---

## 8) Common Traps (Adversarial Examiner View)

1. **Trap:** Using \(^{n}C_r\) where order matters (captain/vice-captain).  
   **Fix:** if roles differ, use permutation.

2. **Trap:** Forgetting divide by repeats in words with repeated letters.  
   **Fix:** map multiplicities first.

3. **Trap:** Circular arrangement solved as \(n!\).  
   **Fix:** use \((n-1)!\) unless one seat fixed externally.

4. **Trap:** “At least one” done by long case splits.  
   **Fix:** complement first.

5. **Trap:** distribution of identical items solved by permutation formulas.  
   **Fix:** stars and bars.

---

## 9) NAT/MSQ Precision and Consistency Strategy

### NAT (Numerical Answer Type)

- Keep exact integer/fraction form till final step.
- If decimal needed, round only at end as instructed.
- Common loss boundary: values like \(0.4999\) vs \(0.500\) due to early rounding.

### MSQ (Multi-Select Questions)

Validate each option independently with quick logic:

- dimensional/feasibility check (e.g., \(r>n\) impossible without repetition)
- edge checks (\(r=0\), \(r=n\))
- relation checks (\(^{n}P_r=^{n}C_r\cdot r!\))

Never assume only one option unless explicitly MSQ/SQ specified.

---

## 10) Ultra-Compact Concept Map

- **Permutation:** arrangement
- **Combination:** selection
- **Repeated objects:** divide by repeated factorials
- **Repetition allowed:** powers/stars-bars
- **Together:** block
- **Not together:** complement/gaps
- **At least one:** complement + inclusion-exclusion

---

## 11) Pythonic Validation Snippets (for Concept Self-Check)

Use these for personal verification of formulas on small values.

```python
import math
from itertools import permutations, combinations, product

def nPr(n, r):
    return math.factorial(n)//math.factorial(n-r) if 0 <= r <= n else 0

def nCr(n, r):
    return math.comb(n, r) if 0 <= r <= n else 0

# Validate nPr and nCr against brute force for small n, r
for n in range(0, 8):
    items = list(range(n))
    for r in range(0, n+1):
        assert len(set(permutations(items, r))) == nPr(n, r)
        assert len(set(combinations(items, r))) == nCr(n, r)

# Validate repetition-allowed count n^r
for n in range(0, 6):
    for r in range(0, 6):
        assert len(list(product(range(n), repeat=r))) == n**r

print("All checks passed")
```

For stars and bars, brute-force validate small \(n,k\):

```python
import math

def nonnegative_solutions(n, k):
    # count x1+...+xk=n, xi>=0
    ans = 0
    def dfs(i, rem):
        nonlocal ans
        if i == k-1:
            ans += 1
            return
        for x in range(rem+1):
            dfs(i+1, rem-x)
    dfs(0, n)
    return ans

for n in range(0, 8):
    for k in range(1, 6):
        assert nonnegative_solutions(n, k) == math.comb(n+k-1, k-1)

print("Stars-bars validated")
```

---

## 12) 30-Second Question Attack Framework

1. Identify object type: distinct/identical.
2. Identify action: arrange/select/distribute.
3. Mark constraints: together/apart/at least/at most/fixed positions.
4. Pick core model.
5. Run one quick sanity check (magnitude + edge case).

---

## 13) Practice Set (Exam-Style with Final Answers)

1. Number of 4-letter arrangements from 9 distinct letters (no repetition):  
   \[
   ^9P_4=3024
   \]

2. Number of committees of 4 from 10 persons:  
   \[
   ^{10}C_4=210
   \]

3. Arrangements of “MISSISSIPPI”: letters counts \(M=1,I=4,S=4,P=2\):  
   \[
   \frac{11!}{4!\,4!\,2!}=34650
   \]

4. Circular seating of 8 persons where A and B sit together:  
   block AB + 6 others \(\Rightarrow 7\) entities circular:
   \[
   (7-1)!\cdot2=1440
   \]

5. Number of nonnegative solutions of \(x+y+z=12\):  
   \[
   {14\choose2}=91
   \]

6. Number of positive solutions of \(x+y+z=12\):  
   \[
   {11\choose2}=55
   \]

---

## 14) Memory Anchors for Permanent Recall

- **Permutation = podium** (positions are different heights)
- **Combination = basket** (selection only, no order)
- **Repeated letters = photocopies** (swapping copies changes nothing)
- **Stars and Bars = chocolates and separators**
- **Circular = pin one person and spin**

Mental slider:

- move from “all distinct linear” \(\rightarrow\) “add constraints” \(\rightarrow\) “identical items” \(\rightarrow\) “distribution equations”.  
One slider, many question types.

5-second snap-check:

- If answer for “selection” is larger than corresponding “arrangement” in same \(n,r\), it is wrong.
- If “not together” \(>\) total, wrong.
- If repeated objects present and you did not divide, likely wrong.

---

## 15) Final Master Table

| Situation | Formula |
|---|---|
| Arrange \(n\) distinct linearly | \(n!\) |
| Arrange \(r\) from \(n\) distinct | \(^{n}P_r=\frac{n!}{(n-r)!}\) |
| Select \(r\) from \(n\) distinct | \(^{n}C_r=\frac{n!}{r!(n-r)!}\) |
| Relation | \(^{n}P_r=\,^{n}C_r\cdot r!\) |
| Repetition allowed (length \(r\), \(n\) symbols) | \(n^r\) |
| Repeated objects \(a,b,c,\dots\) | \(\frac{n!}{a!b!c!\cdots}\) |
| Circular distinct | \((n-1)!\) |
| Nonnegative solutions \(\sum_{i=1}^{k}x_i=n\) | \({n+k-1\choose k-1}\) |
| Positive solutions \(\sum_{i=1}^{k}x_i=n\) | \({n-1\choose k-1}\) |

---

You now have a complete, non-redundant, exam-grade toolkit for Permutation and Combination from first principles to advanced traps and verification.
