# Module 4: Divide and Conquer

## 🎯 The Atomic Truth
> **"Split problem, solve parts, combine solutions"**

---

## 🧠 Mental Model: Military Strategy

[Image: General dividing army to conquer multiple fronts, then reuniting]

**Divide:** Break the enemy line into smaller groups
**Conquer:** Defeat each group independently
**Combine:** Reunite your forces with captured territory

---

## 📐 1. The Paradigm | Core Concept

### 1.1 General Structure

```python
def divide_and_conquer(problem):
    # Base case
    if is_small_enough(problem):
        return direct_solve(problem)
    
    # Divide
    subproblems = divide(problem)
    
    # Conquer
    solutions = [divide_and_conquer(sub) for sub in subproblems]
    
    # Combine
    return combine(solutions)
```

### 1.2 Recurrence Template

$$T(n) = aT(n/b) + f(n)$$

Where:
- $a$ = number of subproblems
- $n/b$ = size of each subproblem
- $f(n)$ = cost of divide + combine

### 1.3 When to Use D&C

1. Problem can be broken into **independent** smaller subproblems
2. Subproblems are **same type** as original
3. Solutions can be **efficiently combined**
4. Subproblem solutions don't need to be **reused** (otherwise → Dynamic Programming)

---

## 🔢 2. Classic D&C Algorithms

### 2.1 Binary Search (Revisited)

**Divide:** Compare with middle element
**Conquer:** Search in one half
**Combine:** No combination needed

$$T(n) = T(n/2) + O(1) = O(\log n)$$

---

### 2.2 Merge Sort (Revisited)

**Divide:** Split array in half
**Conquer:** Sort each half recursively
**Combine:** Merge two sorted halves

$$T(n) = 2T(n/2) + O(n) = O(n \log n)$$

---

### 2.3 Quick Sort (Revisited)

**Divide:** Partition around pivot
**Conquer:** Sort partitions recursively
**Combine:** No combination (in-place)

$$T(n) = T(k) + T(n-k-1) + O(n)$$

Best/Average: O(n log n), Worst: O(n²)

---

## 🔍 3. Finding Maximum and Minimum

### 3.1 Naive Approach

```python
def find_max_min_naive(arr):
    max_val = min_val = arr[0]
    for x in arr[1:]:
        if x > max_val:
            max_val = x
        if x < min_val:
            min_val = x
    return max_val, min_val
```

**Comparisons:** 2(n-1) = 2n - 2

### 3.2 D&C Approach

```python
def find_max_min(arr, low, high):
    # Base case: single element
    if low == high:
        return arr[low], arr[low]
    
    # Base case: two elements
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[high], arr[low]
        return arr[low], arr[high]
    
    # Divide
    mid = (low + high) // 2
    
    # Conquer
    max1, min1 = find_max_min(arr, low, mid)
    max2, min2 = find_max_min(arr, mid + 1, high)
    
    # Combine
    return max(max1, max2), min(min1, min2)
```

### 3.3 Comparison Analysis

**Recurrence:**
$$T(n) = 2T(n/2) + 2$$

Solving:
$$T(n) = 2T(n/2) + 2$$
$$= 4T(n/4) + 2 \cdot 2 + 2$$
$$= 2^k T(n/2^k) + 2(2^{k-1} + 2^{k-2} + ... + 1)$$
$$= n \cdot T(1) + 2(n - 1) / 1$$

At $n = 2^k$: $T(n) = \frac{3n}{2} - 2$

**Comparisons:** $\frac{3n}{2} - 2$ vs $2n - 2$ (naive)

**🎯 GATE Point:** D&C saves ~25% comparisons!

---

## 🔢 4. Finding Kth Smallest Element

### 4.1 Problem Statement
Find the k-th smallest element in unsorted array in expected O(n) time.

### 4.2 QuickSelect Algorithm (Randomized)

```python
import random

def quick_select(arr, k):
    return quick_select_helper(arr, 0, len(arr) - 1, k - 1)

def quick_select_helper(arr, low, high, k):
    if low == high:
        return arr[low]
    
    # Random pivot selection
    pivot_idx = random.randint(low, high)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    
    pivot_idx = partition(arr, low, high)
    
    if k == pivot_idx:
        return arr[k]
    elif k < pivot_idx:
        return quick_select_helper(arr, low, pivot_idx - 1, k)
    else:
        return quick_select_helper(arr, pivot_idx + 1, high, k)

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i
```

### 4.3 Analysis

**Best/Average:** $T(n) = T(n/2) + O(n) = O(n)$

**Worst:** $T(n) = T(n-1) + O(n) = O(n^2)$

### 4.4 Median of Medians (Deterministic O(n))

```python
def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]
    
    # Divide into groups of 5
    medians = []
    for i in range(0, len(arr), 5):
        group = sorted(arr[i:i+5])
        medians.append(group[len(group) // 2])
    
    # Find median of medians
    pivot = median_of_medians(medians, len(medians) // 2)
    
    # Partition around pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]
    
    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + len(equal):
        return pivot
    else:
        return median_of_medians(high, k - len(low) - len(equal))
```

### 4.5 Why Groups of 5?

After finding median of medians:
- At least 30% elements are ≤ pivot
- At least 30% elements are ≥ pivot
- Worst case: recurse on 70% of elements

$$T(n) = T(n/5) + T(7n/10) + O(n)$$

Since $1/5 + 7/10 = 9/10 < 1$: $T(n) = O(n)$

**🎯 GATE Point:** Groups of 3 don't work (3/4 + 2/3 > 1)!

---

## ✖️ 5. Matrix Multiplication

### 5.1 Naive Algorithm

```python
def matrix_multiply_naive(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C
```

**Complexity:** $O(n^3)$ multiplications and additions

### 5.2 Simple D&C Approach

Divide n×n matrices into 4 (n/2)×(n/2) submatrices:

$$\begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix} \times \begin{bmatrix} B_{11} & B_{12} \\ B_{21} & B_{22} \end{bmatrix} = \begin{bmatrix} C_{11} & C_{12} \\ C_{21} & C_{22} \end{bmatrix}$$

Where:
$$C_{11} = A_{11}B_{11} + A_{12}B_{21}$$
$$C_{12} = A_{11}B_{12} + A_{12}B_{22}$$
$$C_{21} = A_{21}B_{11} + A_{22}B_{21}$$
$$C_{22} = A_{21}B_{12} + A_{22}B_{22}$$

**Recurrence:** $T(n) = 8T(n/2) + O(n^2)$

Using Master Theorem: $\log_2 8 = 3$, so $T(n) = O(n^3)$

**No improvement!** Still 8 multiplications.

---

### 5.3 Strassen's Algorithm ⭐

**Key Insight:** Reduce 8 multiplications to 7 using clever algebra.

Define 7 products:
$$M_1 = (A_{11} + A_{22})(B_{11} + B_{22})$$
$$M_2 = (A_{21} + A_{22})B_{11}$$
$$M_3 = A_{11}(B_{12} - B_{22})$$
$$M_4 = A_{22}(B_{21} - B_{11})$$
$$M_5 = (A_{11} + A_{12})B_{22}$$
$$M_6 = (A_{21} - A_{11})(B_{11} + B_{12})$$
$$M_7 = (A_{12} - A_{22})(B_{21} + B_{22})$$

Then:
$$C_{11} = M_1 + M_4 - M_5 + M_7$$
$$C_{12} = M_3 + M_5$$
$$C_{21} = M_2 + M_4$$
$$C_{22} = M_1 - M_2 + M_3 + M_6$$

### 5.4 Strassen Analysis

**Recurrence:** $T(n) = 7T(n/2) + O(n^2)$

Using Master Theorem:
- $a = 7, b = 2$
- $\log_2 7 \approx 2.807$
- $f(n) = n^2 = O(n^{2.807 - \epsilon})$
- **Case 1:** $T(n) = O(n^{\log_2 7}) = O(n^{2.807})$

**Improvement:** From $O(n^3)$ to $O(n^{2.807})$

### 5.5 Practical Considerations

- Strassen's has larger constants
- Better only for $n > \sim 32$
- Hybrid: Use Strassen's for large, switch to naive for small

### 5.6 Current Best

- Coppersmith-Winograd: $O(n^{2.376})$
- Current best (Williams): $O(n^{2.3728...})$
- Lower bound: $\Omega(n^2)$ (must read all entries)

---

## 📊 6. Counting Inversions

### 6.1 Problem Statement
Count pairs (i, j) where i < j but arr[i] > arr[j].

### 6.2 Application
- Measuring "sortedness" of array
- Collaborative filtering (comparing rankings)

### 6.3 D&C Algorithm (Modified Merge Sort)

```python
def count_inversions(arr):
    _, count = merge_count(arr)
    return count

def merge_count(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, left_inv = merge_count(arr[:mid])
    right, right_inv = merge_count(arr[mid:])
    merged, split_inv = merge_and_count(left, right)
    
    return merged, left_inv + right_inv + split_inv

def merge_and_count(left, right):
    result = []
    inversions = 0
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            inversions += len(left) - i  # All remaining left elements
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result, inversions
```

### 6.4 Key Insight

When merging, if right[j] is picked before left[i], then right[j] is smaller than all remaining left elements. These form inversions!

### 6.5 Analysis

Same as Merge Sort: $O(n \log n)$

**🎯 GATE Point:** Maximum inversions = $\frac{n(n-1)}{2}$ (reverse sorted array)

---

## 📏 7. Closest Pair of Points

### 7.1 Problem Statement
Given n points in 2D, find the pair with minimum Euclidean distance.

### 7.2 Naive Approach

```python
def closest_pair_naive(points):
    min_dist = float('inf')
    n = len(points)
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean(points[i], points[j])
            min_dist = min(min_dist, dist)
    
    return min_dist
```

**Complexity:** $O(n^2)$

### 7.3 D&C Algorithm

```python
def closest_pair(points):
    # Sort by x-coordinate
    points_x = sorted(points, key=lambda p: p[0])
    points_y = sorted(points, key=lambda p: p[1])
    
    return closest_pair_helper(points_x, points_y)

def closest_pair_helper(px, py):
    n = len(px)
    
    # Base case
    if n <= 3:
        return brute_force(px)
    
    # Divide
    mid = n // 2
    mid_point = px[mid]
    
    # Split py into left and right by x-coordinate
    pyl = [p for p in py if p[0] <= mid_point[0]]
    pyr = [p for p in py if p[0] > mid_point[0]]
    
    # Conquer
    dl = closest_pair_helper(px[:mid], pyl)
    dr = closest_pair_helper(px[mid:], pyr)
    d = min(dl, dr)
    
    # Combine: check strip around midline
    strip = [p for p in py if abs(p[0] - mid_point[0]) < d]
    
    return min(d, strip_closest(strip, d))

def strip_closest(strip, d):
    min_dist = d
    
    for i in range(len(strip)):
        # Only check next 7 points (provable!)
        for j in range(i + 1, min(i + 8, len(strip))):
            dist = euclidean(strip[i], strip[j])
            min_dist = min(min_dist, dist)
    
    return min_dist
```

### 7.4 Why Only 7 Points in Strip?

[Image: Grid cells in strip of width 2d]

Key insight: In a δ×δ box, at most 1 point (else distance < δ).

In strip of width 2δ:
- Divide into δ/2 × δ/2 cells
- 8 cells on each side of midline
- At most 8 points per row of height δ
- **Only need to check next 7 points!**

### 7.5 Analysis

$$T(n) = 2T(n/2) + O(n)$$

**Complexity:** $O(n \log n)$

The $O(n)$ comes from:
- Building strip: O(n)
- Checking strip: O(n) since each point checks only 7 neighbors

---

## 🔢 8. Large Integer Multiplication

### 8.1 Problem
Multiply two n-digit numbers efficiently.

### 8.2 Naive School Method

$$O(n^2)$$ digit multiplications

### 8.3 Karatsuba Algorithm

For n-digit numbers X and Y, split each:
$$X = X_1 \cdot 10^{n/2} + X_0$$
$$Y = Y_1 \cdot 10^{n/2} + Y_0$$

**Naive:** $XY = X_1Y_1 \cdot 10^n + (X_1Y_0 + X_0Y_1) \cdot 10^{n/2} + X_0Y_0$

→ 4 multiplications of n/2-digit numbers

**Karatsuba's trick:**
$$P_1 = X_1 Y_1$$
$$P_2 = X_0 Y_0$$
$$P_3 = (X_1 + X_0)(Y_1 + Y_0)$$
$$X_1Y_0 + X_0Y_1 = P_3 - P_1 - P_2$$

→ Only 3 multiplications!

### 8.4 Analysis

$$T(n) = 3T(n/2) + O(n)$$

Using Master Theorem:
$$T(n) = O(n^{\log_2 3}) = O(n^{1.585})$$

**Improvement:** From $O(n^2)$ to $O(n^{1.585})$

### 8.5 Current Best

Schönhage-Strassen: $O(n \log n \log \log n)$
Fürer: $O(n \log n \cdot 2^{O(\log^* n)})$
Harvey-Hoeven (2019): $O(n \log n)$ ← asymptotically optimal!

---

## 🏃 9. Fast Fourier Transform (FFT)

### 9.1 Problem
Multiply two polynomials of degree n in O(n log n).

Standard convolution: $O(n^2)$

### 9.2 Key Insight

**Coefficient form:** A(x) = a₀ + a₁x + ... + aₙxⁿ → O(n²) to multiply

**Point-value form:** {(x₀, A(x₀)), (x₁, A(x₁)), ...} → O(n) to multiply point-wise!

**FFT Strategy:**
1. Convert coefficients → point-values at special points (FFT)
2. Multiply point-values: O(n)
3. Convert point-values → coefficients (Inverse FFT)

### 9.3 The nth Roots of Unity

Choose evaluation points as $\omega_n^0, \omega_n^1, ..., \omega_n^{n-1}$

where $\omega_n = e^{2\pi i/n}$ (principal nth root of unity)

**Key properties:**
- $\omega_n^n = 1$
- $\omega_n^{n/2} = -1$
- $(\omega_n^k)^2 = \omega_{n/2}^k$

### 9.4 FFT Algorithm (Cooley-Tukey)

```python
import cmath

def fft(a):
    n = len(a)
    if n == 1:
        return a
    
    omega = cmath.exp(2j * cmath.pi / n)
    
    # Split into even and odd indices
    a_even = fft(a[0::2])
    a_odd = fft(a[1::2])
    
    y = [0] * n
    for k in range(n // 2):
        t = omega ** k * a_odd[k]
        y[k] = a_even[k] + t
        y[k + n // 2] = a_even[k] - t
    
    return y
```

### 9.5 Analysis

$$T(n) = 2T(n/2) + O(n) = O(n \log n)$$

### 9.6 Polynomial Multiplication using FFT

```python
def multiply_polynomials(A, B):
    n = 1
    while n < len(A) + len(B):
        n *= 2
    
    # Pad with zeros
    A = A + [0] * (n - len(A))
    B = B + [0] * (n - len(B))
    
    # FFT
    fft_A = fft(A)
    fft_B = fft(B)
    
    # Point-wise multiplication
    fft_C = [fft_A[i] * fft_B[i] for i in range(n)]
    
    # Inverse FFT
    C = ifft(fft_C)
    
    return [round(c.real) for c in C]
```

**Total complexity:** $O(n \log n)$

---

## 🎯 10. D&C Design Patterns

### 10.1 Pattern 1: Reduce Problem Size

- Binary Search: 1 subproblem of size n/2
- $T(n) = T(n/2) + O(1) = O(\log n)$

### 10.2 Pattern 2: Divide Evenly

- Merge Sort: 2 subproblems of size n/2
- $T(n) = 2T(n/2) + O(n) = O(n \log n)$

### 10.3 Pattern 3: Reduce Recursive Calls

- Strassen: 7 instead of 8 calls
- Karatsuba: 3 instead of 4 calls
- Small reduction in calls → significant asymptotic improvement

### 10.4 Pattern 4: Clever Combination

- Closest Pair: O(n) combination using geometry
- Inversion Count: O(n) combination using merge

---

## 🎓 11. GATE Pattern Problems

### Problem Type 1: Master Theorem Application

**Q:** Solve $T(n) = 4T(n/2) + n^2 \log n$

**Solution:**
- $a = 4, b = 2, \log_2 4 = 2$
- $f(n) = n^2 \log n = n^{\log_b a} \cdot \log^1 n$
- Extended Case 2: $T(n) = \Theta(n^2 \log^2 n)$

---

### Problem Type 2: Comparison Count

**Q:** Minimum comparisons to find max and min in 100 elements?

**Solution:**
Using D&C: $\frac{3n}{2} - 2 = \frac{3 \times 100}{2} - 2 = 148$

**Answer: 148**

---

### Problem Type 3: Recurrence Identification

**Q:** Which algorithm has recurrence $T(n) = 7T(n/2) + O(n^2)$?

**Solution:** Strassen's matrix multiplication

---

## 🚨 12. Common GATE Traps

### Trap 1: Not Recognizing D&C

Many problems can be solved by D&C but aren't obviously recursive.

### Trap 2: Wrong Recurrence

For QuickSelect: $T(n) = T(n/2) + O(n)$ gives O(n), but worst case is O(n²)!

### Trap 3: Strassen's Exponent

$O(n^{\log_2 7})$, NOT $O(n^{2.5})$ or $O(n^3)$

### Trap 4: Closest Pair Strip

Strip has width $2\delta$, not $\delta$. Points are sorted by y, not x, in strip.

---

## 📝 13. Practice Problems

### Problem 1 [NAT]
Using Karatsuba's algorithm, how many multiplications to multiply two 64-digit numbers? (Base case: 1-digit numbers need 1 multiplication)

<details>
<summary>Solution</summary>

$T(n) = 3T(n/2) + O(n)$

For n = 64:
- Level 0: 1 call
- Level 1: 3 calls
- Level 2: 9 calls
- ...
- Level 6: $3^6 = 729$ calls (base case: 1-digit)

**Answer: 729 multiplications**
</details>

---

### Problem 2 [MCQ]
Time complexity of finding median using D&C with deterministic pivot selection?

A. O(n²)
B. O(n log n)
C. O(n)
D. O(log n)

<details>
<summary>Solution</summary>

Median of medians gives O(n) worst case.

**Answer:** C
</details>

---

### Problem 3 [MSQ]
Which problems have O(n log n) D&C solution?

A. Finding maximum element
B. Counting inversions
C. Polynomial multiplication (FFT)
D. Finding median

<details>
<summary>Solution</summary>

A. FALSE - O(n) is sufficient
B. TRUE - Modified merge sort
C. TRUE - FFT
D. FALSE - O(n) using median of medians

**Answer:** B, C
</details>

---

## 🧠 Memory Anchors

### The Mental Slider: D&C Decision Dial

[Image: Dial showing when to use D&C vs other paradigms]

```
D&C: Independent subproblems, no overlap
DP: Overlapping subproblems
Greedy: Local optimal = Global optimal
Brute Force: When nothing else works
```

### The Bizarre Mnemonic: "Divide Kingdoms"

Imagine a king dividing his kingdom:
- **Merge Sort:** Divide land equally, let princes sort, merge territories
- **Quick Sort:** Pick a mountain (pivot), put valleys left, peaks right
- **Strassen:** Instead of 8 battles, fight 7 clever campaigns

### 5-Second Sanity Check

1. Are subproblems independent? If yes → D&C. If overlap → DP
2. Is combination efficient? If not → D&C won't help
3. Does reducing one call help? (7 vs 8 in Strassen → huge improvement)

---

## ⚡ Quick Reference

| Problem | Recurrence | Complexity |
|---------|------------|------------|
| Binary Search | T(n) = T(n/2) + O(1) | O(log n) |
| Merge Sort | T(n) = 2T(n/2) + O(n) | O(n log n) |
| Quick Sort (avg) | T(n) = 2T(n/2) + O(n) | O(n log n) |
| Max-Min | T(n) = 2T(n/2) + O(1) | O(n), 3n/2 - 2 comparisons |
| QuickSelect (avg) | T(n) = T(n/2) + O(n) | O(n) |
| Strassen | T(n) = 7T(n/2) + O(n²) | O(n^2.807) |
| Karatsuba | T(n) = 3T(n/2) + O(n) | O(n^1.585) |
| Closest Pair | T(n) = 2T(n/2) + O(n) | O(n log n) |
| FFT | T(n) = 2T(n/2) + O(n) | O(n log n) |
| Inversions | T(n) = 2T(n/2) + O(n) | O(n log n) |

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

**Next Module:** [Greedy Algorithms →](05-Greedy-Algorithms.md)
