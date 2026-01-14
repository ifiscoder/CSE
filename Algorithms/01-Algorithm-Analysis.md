# Module 1: Algorithm Analysis & Complexity

## 🎯 The Atomic Truth
> **"Counting steps as input grows"**

---

## 🧠 Mental Model: The Factory Assembly Line

Imagine an algorithm as a **factory production line**:
- **Input (n)** = Number of items to manufacture
- **Time Complexity** = How production time scales with more items
- **Space Complexity** = How much warehouse space you need

[Image: Factory with conveyor belt, workers (operations), and warehouse (memory)]

---

## 📐 1. Asymptotic Notations | The Mathematical DNA

### 1.1 Big-O Notation (Upper Bound)

**The Atomic Truth:** *"At most this bad, never worse"*

$$f(n) = O(g(n)) \iff \exists \text{ constants } c > 0, n_0 > 0 \text{ such that } f(n) \leq c \cdot g(n), \forall n \geq n_0$$

**Intuition:** Big-O captures the **worst-case ceiling**. If $f(n) = O(n^2)$, your algorithm will *never* take more than roughly $n^2$ steps (up to a constant factor) for large inputs.

#### Example: Proving $3n^2 + 5n + 7 = O(n^2)$

**Step-by-step derivation:**
1. We need: $3n^2 + 5n + 7 \leq c \cdot n^2$
2. Divide by $n^2$: $3 + \frac{5}{n} + \frac{7}{n^2} \leq c$
3. For $n \geq 1$: $3 + 5 + 7 = 15 \leq c$
4. Choose $c = 15, n_0 = 1$ ✓

**🎯 GATE Trick:** Any polynomial $a_kn^k + a_{k-1}n^{k-1} + ... + a_0 = O(n^k)$

---

### 1.2 Big-Ω Notation (Lower Bound)

**The Atomic Truth:** *"At least this much, possibly more"*

$$f(n) = \Omega(g(n)) \iff \exists \text{ constants } c > 0, n_0 > 0 \text{ such that } f(n) \geq c \cdot g(n), \forall n \geq n_0$$

**Intuition:** Big-Ω captures the **best-case floor**. If sorting takes $\Omega(n \log n)$ comparisons, no comparison-based sort can do better.

---

### 1.3 Big-Θ Notation (Tight Bound)

**The Atomic Truth:** *"Exactly this class, sandwiched precisely"*

$$f(n) = \Theta(g(n)) \iff f(n) = O(g(n)) \text{ AND } f(n) = \Omega(g(n))$$

**Intuition:** When both upper and lower bounds match, we have the **exact growth rate**.

#### The Sandwich Inequality
$$c_1 \cdot g(n) \leq f(n) \leq c_2 \cdot g(n), \forall n \geq n_0$$

---

### 1.4 Little-o and Little-ω (Strict Bounds)

| Notation | Meaning | Mathematical Definition |
|----------|---------|------------------------|
| $f(n) = o(g(n))$ | Strictly less than | $\lim_{n \to \infty} \frac{f(n)}{g(n)} = 0$ |
| $f(n) = \omega(g(n))$ | Strictly greater than | $\lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty$ |

**🎯 GATE Trap Alert:** 
- $n = O(n^2)$ ✓ (correct)
- $n = o(n^2)$ ✓ (correct - strictly less)
- $n^2 = O(n^2)$ ✓ (correct)
- $n^2 = o(n^2)$ ✗ (wrong - not strictly less)

---

## 📊 2. Complexity Hierarchy

### 2.1 The Growth Rate Ladder

$$O(1) < O(\log \log n) < O(\log n) < O(\sqrt{n}) < O(n) < O(n \log n) < O(n^2) < O(n^3) < O(2^n) < O(n!) < O(n^n)$$

### 2.2 Numerical Intuition Table

| n | log n | n | n log n | n² | 2ⁿ | n! |
|---|-------|---|---------|-----|-----|-----|
| 10 | 3.3 | 10 | 33 | 100 | 1024 | 3.6M |
| 100 | 6.6 | 100 | 664 | 10⁴ | 10³⁰ | ∞ |
| 1000 | 10 | 1000 | 10⁴ | 10⁶ | 10³⁰¹ | ∞ |

**🧠 Memory Mnemonic:** **"CALL SNOOPY"**
- **C**onstant
- **A**lgorithmic (log)
- **L**inear
- **L**inearithmic (n log n)
- **S**quare
- **N**cubic
- **O**ther polynomials
- **O**exponential (2ⁿ)
- **P**ermutation (n!)
- **Y**ikes (nⁿ)

---

## 🔄 3. Recurrence Relations | The Heart of Algorithm Analysis

### 3.1 Why Recurrences?

Most efficient algorithms use **recursion** → leads to **recurrence relations** for time complexity.

**General Form:** $T(n) = aT(n/b) + f(n)$

Where:
- $a$ = number of subproblems
- $n/b$ = size of each subproblem
- $f(n)$ = work done at current level (divide + combine)

---

### 3.2 Method 1: Substitution Method (Guess & Verify)

**Steps:**
1. Guess the solution form
2. Use mathematical induction to prove
3. Determine constants

#### Example: $T(n) = 2T(n/2) + n$, $T(1) = 1$

**Guess:** $T(n) = O(n \log n)$, so $T(n) \leq cn \log n$

**Inductive Proof:**
Assume $T(k) \leq ck \log k$ for all $k < n$

$$T(n) = 2T(n/2) + n$$
$$\leq 2 \cdot c(n/2)\log(n/2) + n$$
$$= cn(\log n - 1) + n$$
$$= cn \log n - cn + n$$
$$= cn \log n - (c-1)n$$
$$\leq cn \log n \text{ (for } c \geq 1\text{)}$$

**Result:** $T(n) = O(n \log n)$ ✓

---

### 3.3 Method 2: Recursion Tree Method (Visual)

**The Atomic Truth:** *"Draw the tree, sum the levels"*

#### Example: $T(n) = 2T(n/2) + n$

```
Level 0:           n                    Work: n
                  / \
Level 1:       n/2   n/2                Work: 2(n/2) = n
               /\     /\
Level 2:     n/4 n/4 n/4 n/4           Work: 4(n/4) = n
               ...
Level k:     1  1  1  ...  1            Work: 2^k · (n/2^k) = n
```

**Total Levels:** $\log_2 n$ (since $n/2^k = 1 \Rightarrow k = \log n$)

**Total Work:** $n \times \log n = O(n \log n)$

---

### 3.4 Method 3: Master Theorem ⭐ (Most Important for GATE)

**For recurrences of form:** $T(n) = aT(n/b) + f(n)$

**Critical Value:** $\log_b a$ (determines which term dominates)

**Compare $f(n)$ with $n^{\log_b a}$:**

| Case | Condition | Result |
|------|-----------|--------|
| **Case 1** | $f(n) = O(n^{\log_b a - \epsilon})$ for some $\epsilon > 0$ | $T(n) = \Theta(n^{\log_b a})$ |
| **Case 2** | $f(n) = \Theta(n^{\log_b a})$ | $T(n) = \Theta(n^{\log_b a} \log n)$ |
| **Case 3** | $f(n) = \Omega(n^{\log_b a + \epsilon})$ for some $\epsilon > 0$ AND $af(n/b) \leq cf(n)$ for $c < 1$ | $T(n) = \Theta(f(n))$ |

#### 🎯 Visual Memory: "The Arm Wrestling Match"

[Image: Two wrestlers - "Leaves" ($n^{\log_b a}$) vs "Root Work" ($f(n)$)]

- **Case 1:** Leaves dominate → Answer is leaf work
- **Case 2:** Perfect tie → Multiply by $\log n$
- **Case 3:** Root dominates → Answer is root work

---

### 3.5 Master Theorem Examples

#### Example 1: $T(n) = 2T(n/2) + n$
- $a = 2, b = 2, f(n) = n$
- $\log_b a = \log_2 2 = 1$
- $f(n) = n = \Theta(n^1)$
- **Case 2:** $T(n) = \Theta(n \log n)$ ✓

#### Example 2: $T(n) = 4T(n/2) + n$
- $a = 4, b = 2, f(n) = n$
- $\log_b a = \log_2 4 = 2$
- $f(n) = n = O(n^{2-1}) = O(n^1)$ where $\epsilon = 1$
- **Case 1:** $T(n) = \Theta(n^2)$ ✓

#### Example 3: $T(n) = 4T(n/2) + n^3$
- $a = 4, b = 2, f(n) = n^3$
- $\log_b a = 2$
- $f(n) = n^3 = \Omega(n^{2+1})$ where $\epsilon = 1$
- Check regularity: $4(n/2)^3 = n^3/2 \leq cn^3$ for $c = 1/2$ ✓
- **Case 3:** $T(n) = \Theta(n^3)$ ✓

---

### 3.6 Extended Master Theorem (For $f(n) = n^{\log_b a} \log^k n$)

When $f(n) = \Theta(n^{\log_b a} \log^k n)$:

$$T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$$

#### Example: $T(n) = 2T(n/2) + n \log n$
- $\log_b a = 1$, $f(n) = n \log n = n^1 \cdot \log^1 n$
- Here $k = 1$
- **Result:** $T(n) = \Theta(n \log^2 n)$

---

### 3.7 Master Theorem Doesn't Apply? 

**Cases where Master Theorem fails:**

1. **Non-polynomial gap:** $T(n) = 2T(n/2) + \frac{n}{\log n}$
   - $f(n) = n/\log n$ is not polynomially smaller than $n$
   - Use **Akra-Bazzi method** instead

2. **Variable $a$ or $b$:** $T(n) = T(n/2) + T(n/3) + n$
   - Use recursion tree or substitution

3. **Non-constant recursion:** $T(n) = T(\sqrt{n}) + 1$
   - Substitute $m = \log n$, solve, then back-substitute

---

### 3.8 Special Recurrences for GATE

| Recurrence | Solution | Algorithm Example |
|------------|----------|-------------------|
| $T(n) = T(n-1) + 1$ | $\Theta(n)$ | Linear search |
| $T(n) = T(n-1) + n$ | $\Theta(n^2)$ | Selection sort |
| $T(n) = 2T(n-1) + 1$ | $\Theta(2^n)$ | Tower of Hanoi |
| $T(n) = T(n/2) + 1$ | $\Theta(\log n)$ | Binary search |
| $T(n) = T(n/2) + n$ | $\Theta(n)$ | Finding median |
| $T(n) = 2T(n/2) + 1$ | $\Theta(n)$ | Tree traversal |
| $T(n) = 2T(n/2) + n$ | $\Theta(n \log n)$ | Merge sort |
| $T(n) = 2T(n/2) + n^2$ | $\Theta(n^2)$ | - |
| $T(n) = T(\sqrt{n}) + 1$ | $\Theta(\log \log n)$ | - |

---

## 🔢 4. Counting Operations | Loop Analysis

### 4.1 Simple Loops

```
for i = 1 to n:
    // constant time operation
```
**Complexity:** $O(n)$

---

### 4.2 Nested Loops

```
for i = 1 to n:
    for j = 1 to n:
        // constant time
```
**Complexity:** $n \times n = O(n^2)$

---

### 4.3 Dependent Nested Loops

#### Type 1: j depends on i
```
for i = 1 to n:
    for j = 1 to i:
        // constant time
```
**Count:** $1 + 2 + 3 + ... + n = \frac{n(n+1)}{2} = O(n^2)$

#### Type 2: Upper triangular
```
for i = 1 to n:
    for j = i to n:
        // constant time
```
**Count:** $n + (n-1) + ... + 1 = \frac{n(n+1)}{2} = O(n^2)$

---

### 4.4 Logarithmic Loops

```
for i = 1; i <= n; i = i * 2:
    // constant time
```
**Iterations:** $i = 1, 2, 4, 8, ..., 2^k$ where $2^k \leq n$
**Count:** $k = \lfloor \log_2 n \rfloor + 1 = O(\log n)$

```
for i = n; i >= 1; i = i / 2:
    // constant time
```
**Same:** $O(\log n)$

---

### 4.5 Nested with Log

```
for i = 1 to n:
    for j = 1; j <= n; j = j * 2:
        // constant time
```
**Complexity:** $n \times \log n = O(n \log n)$

---

### 4.6 Tricky Loop Patterns

#### Pattern 1: Sum pattern
```
for i = 1 to n:
    for j = 1; j <= i; j = j * 2:
        // constant time
```
**Inner loop runs:** $\log i$ times
**Total:** $\sum_{i=1}^{n} \log i = \log(n!) = \Theta(n \log n)$

**Using Stirling's Approximation:** $\log(n!) = n \log n - n \log e + O(\log n) = \Theta(n \log n)$

---

#### Pattern 2: While loops
```
i = n
while i > 0:
    for j = 0 to i:
        // constant time
    i = i / 2
```
**Work per iteration:** $n + n/2 + n/4 + ... + 1$
**Total:** $n(1 + 1/2 + 1/4 + ...) \leq 2n = O(n)$

---

## 🎯 5. Space Complexity

### 5.1 What Counts as Space?

1. **Input space** - Often not counted (auxiliary space focus)
2. **Auxiliary space** - Extra space used by algorithm
3. **Stack space** - For recursive calls

---

### 5.2 Recursion Stack Space

For recursion with depth $d$ and frame size $c$:
$$\text{Space} = O(d \times c)$$

#### Example: Merge Sort
- Recursion depth: $\log n$
- Array copy: $n$
- **Total:** $O(n)$ (auxiliary array dominates)

#### Example: Quick Sort
- Best case depth: $O(\log n)$
- Worst case depth: $O(n)$
- **Space:** $O(\log n)$ to $O(n)$

---

## 🧪 6. Amortized Analysis

### 6.1 What is Amortized Analysis?

**The Atomic Truth:** *"Average cost over sequence of operations"*

Not the same as average case! Amortized gives **guaranteed average** per operation in worst-case sequence.

---

### 6.2 Aggregate Method

**Calculate:** Total cost of $n$ operations / $n$

#### Example: Dynamic Array (ArrayList)

When array is full, double the size:
- Copy $n$ elements to new array
- Insertions: $1, 1, 1, 2, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 8, ...$
- Expensive operations at powers of 2

**Total cost for $n$ insertions:**
$$n + (1 + 2 + 4 + ... + n) \leq n + 2n = 3n$$

**Amortized cost:** $3n/n = O(1)$ per insertion ✓

---

### 6.3 Accounting Method

**Idea:** Assign "credits" to operations. Cheap operations pay for expensive ones.

#### Example: Stack with multipop

Operations: PUSH, POP, MULTIPOP(k)

- Assign each PUSH cost = 2 (1 for push, 1 stored as credit)
- POP uses 1 credit
- MULTIPOP(k) uses k credits

Each element pushed stores 1 credit → always enough to pop
**Amortized cost:** $O(1)$ per operation

---

### 6.4 Potential Method

**Define potential function $\Phi$:**
$$\hat{c}_i = c_i + \Phi(D_i) - \Phi(D_{i-1})$$

**Amortized cost = Actual cost + Change in potential**

#### Example: Binary Counter

State: $k$-bit counter
Potential: $\Phi$ = number of 1s in counter

- Increment flips bits: some 1→0, one 0→1
- If $t$ bits flip from 1→0: actual cost = $t+1$
- Change in potential = $1 - t$
- **Amortized cost:** $(t+1) + (1-t) = 2 = O(1)$ ✓

---

## 🎓 7. GATE Pattern Problems

### Problem Type 1: Find Complexity of Code

```
for i = 1 to n:
    j = 1
    while j < n:
        j = j + i
```

**Analysis:**
- Outer loop: $n$ iterations
- Inner loop: For fixed $i$, $j$ takes values $1, 1+i, 1+2i, ...$
- Iterations of inner: $\lceil n/i \rceil$

**Total:** $\sum_{i=1}^{n} \frac{n}{i} = n \sum_{i=1}^{n} \frac{1}{i} = n \cdot H_n = n \cdot O(\log n) = O(n \log n)$

---

### Problem Type 2: Solve Recurrence

$T(n) = 3T(n/4) + n \log n$

**Master Theorem:**
- $a = 3, b = 4$
- $\log_b a = \log_4 3 \approx 0.79$
- $f(n) = n \log n = \Omega(n^{0.79 + \epsilon})$ for $\epsilon = 0.2$
- Check: $3 \cdot \frac{n}{4} \log \frac{n}{4} \leq c \cdot n \log n$ for $c = 3/4$ ✓

**Case 3:** $T(n) = \Theta(n \log n)$

---

### Problem Type 3: Compare Functions

Which grows faster: $n^{\log n}$ or $(\log n)^n$?

**Take logarithm:**
- $\log(n^{\log n}) = \log n \cdot \log n = (\log n)^2$
- $\log((\log n)^n) = n \cdot \log(\log n)$

For large $n$: $n \cdot \log(\log n) >> (\log n)^2$

**Answer:** $(\log n)^n$ grows faster

---

## 🚨 8. Common GATE Traps

### Trap 1: Confusing O, Ω, Θ

**Wrong:** "The time complexity is $O(n^2)$" (when asking for tight bound)
**Right:** "The time complexity is $\Theta(n^2)$"

### Trap 2: Master Theorem Misapplication

$T(n) = 2T(n/2) + n/\log n$

Cannot apply Master Theorem! Gap is not polynomial.
Use integration or recursion tree.

### Trap 3: Forgetting Base Case

$T(1) = 1$ matters for substitution method!

### Trap 4: Log Base Confusion

$\log_2 n$ vs $\log_{10} n$ vs $\ln n$

All differ by constant factor: $\log_a n = \frac{\log_b n}{\log_b a}$

**For Big-O:** Base doesn't matter! $O(\log n)$ is same for any base.

---

## 📝 9. Practice Problems

### Problem 1 [NAT]
Find the tight bound for $T(n) = 9T(n/3) + n^2$

<details>
<summary>Solution</summary>

$a = 9, b = 3, \log_b a = 2$
$f(n) = n^2 = \Theta(n^2)$
**Case 2:** $T(n) = \Theta(n^2 \log n)$

**Answer:** $n^2 \log n$
</details>

---

### Problem 2 [MSQ]
Which of the following are TRUE?

A. $n^2 = O(n^3)$
B. $n^3 = O(n^2)$  
C. $2^n = O(3^n)$
D. $\log n = O(n)$

<details>
<summary>Solution</summary>

A. TRUE (n² grows slower than n³)
B. FALSE (n³ grows faster than n²)
C. TRUE (2ⁿ grows slower than 3ⁿ since 2 < 3)
D. TRUE (log n grows slower than n)

**Answer:** A, C, D
</details>

---

### Problem 3 [MCQ]
What is the complexity of:
```
for i = 1; i*i <= n; i++:
    // constant time
```

A. O(n)
B. O(√n)
C. O(log n)
D. O(n log n)

<details>
<summary>Solution</summary>

Loop runs while $i^2 \leq n$, i.e., $i \leq \sqrt{n}$
**Answer:** B. O(√n)
</details>

---

## 🧠 Memory Anchors

### The Mental Slider: Complexity Dial

[Image: Dial with complexity classes from O(1) to O(n!)]

Turn the dial mentally:
- Each notch = 10x harder problem
- O(n²) at n=1000 = 1 million operations
- O(2ⁿ) at n=1000 = universe lifetime operations

### The Bizarre Mnemonic: "Master Theorem Arm Wrestling"

Two giant arms wrestling:
- Left arm: LEAVES ($n^{\log_b a}$) - represents all recursive calls
- Right arm: ROOT WORK ($f(n)$) - represents work at each level

**Case 1:** Left arm pins right → Leaves win → $\Theta(n^{\log_b a})$
**Case 2:** Perfect stalemate → Multiply by $\log n$ referee
**Case 3:** Right arm pins left → Root wins → $\Theta(f(n))$

### 5-Second Sanity Check

1. Is the answer at least O(n)? (Must read input at least once)
2. Is the answer at most O(n!)? (Cannot be worse than trying all permutations)
3. Does recursion depth match log factor?

---

## ⚡ Quick Formulas

| Sum | Closed Form |
|-----|-------------|
| $1 + 2 + ... + n$ | $\frac{n(n+1)}{2}$ |
| $1^2 + 2^2 + ... + n^2$ | $\frac{n(n+1)(2n+1)}{6}$ |
| $1 + 2 + 4 + ... + 2^k$ | $2^{k+1} - 1$ |
| $1 + 1/2 + 1/4 + ...$ | $2$ |
| $1 + 1/2 + 1/3 + ... + 1/n$ | $\ln n + \gamma \approx \ln n + 0.577$ |
| $\log(n!)$ | $\Theta(n \log n)$ |

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

**Next Module:** [Searching Algorithms →](02-Searching-Algorithms.md)
