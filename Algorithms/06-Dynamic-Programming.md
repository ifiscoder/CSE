# Module 6: Dynamic Programming

## 🎯 The Atomic Truth
> **"Remember past solutions—avoid recomputation"**

---

## 🧠 Mental Model: The Smart Student

[Image: Student with notebook of solved problems, looking up past solutions]

Instead of solving the same sub-problem repeatedly, **store solutions** and **look them up**.

---

## 📐 1. The DP Paradigm

### 1.1 Two Key Properties

**1. Optimal Substructure:**
Optimal solution contains optimal solutions to subproblems.

**2. Overlapping Subproblems:**
Same subproblems are solved multiple times in recursion.

### 1.2 DP vs Divide and Conquer

| Aspect | D&C | DP |
|--------|-----|-----|
| Subproblems | Independent | Overlapping |
| Approach | Top-down | Top-down or Bottom-up |
| Storage | No memoization | Memoization/Tabulation |
| Example | Merge Sort | Fibonacci |

### 1.3 Two Approaches

**Top-Down (Memoization):**
- Start with original problem
- Recursively solve subproblems
- Store results in memo table

**Bottom-Up (Tabulation):**
- Start with smallest subproblems
- Build up to original problem
- Fill table iteratively

---

## 🔢 2. Fibonacci Numbers | The Gateway Example

### 2.1 Naive Recursion

```python
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)
```

**Complexity:** $T(n) = T(n-1) + T(n-2) + O(1) \approx O(2^n)$

### 2.2 Memoization (Top-Down)

```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]
```

**Complexity:** O(n) time, O(n) space

### 2.3 Tabulation (Bottom-Up)

```python
def fib_tab(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]
```

**Complexity:** O(n) time, O(n) space

### 2.4 Space Optimization

```python
def fib_optimized(n):
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    
    return prev1
```

**Complexity:** O(n) time, O(1) space

### 2.5 Matrix Exponentiation

$$\begin{bmatrix} F_n \\ F_{n-1} \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}^{n-1} \begin{bmatrix} F_1 \\ F_0 \end{bmatrix}$$

**Complexity:** O(log n) using fast matrix exponentiation!

---

## 📦 3. 0/1 Knapsack Problem

### 3.1 Problem Statement

Given n items with weights $w_i$ and values $v_i$, and knapsack capacity W, maximize value without exceeding capacity. **No fractions allowed.**

### 3.2 Recurrence

Let $dp[i][w]$ = maximum value using items 1 to i with capacity w.

$$dp[i][w] = \begin{cases} 
dp[i-1][w] & \text{if } w_i > w \text{ (can't include)} \\
\max(dp[i-1][w], dp[i-1][w-w_i] + v_i) & \text{otherwise}
\end{cases}$$

**Base Case:** $dp[0][w] = 0$ for all w

### 3.3 Implementation

```python
def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't include item i
            dp[i][w] = dp[i - 1][w]
            
            # Include item i (if possible)
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], 
                              dp[i - 1][w - weights[i - 1]] + values[i - 1])
    
    return dp[n][capacity]
```

### 3.4 Example

```
Items: weights = [2, 3, 4, 5], values = [3, 4, 5, 6]
Capacity: 5

DP Table:
     w=0  1  2  3  4  5
i=0   0  0  0  0  0  0
i=1   0  0  3  3  3  3
i=2   0  0  3  4  4  7
i=3   0  0  3  4  5  7
i=4   0  0  3  4  5  7

Answer: 7 (items 1 and 2)
```

### 3.5 Space Optimization

Since we only need previous row:

```python
def knapsack_01_optimized(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        # Traverse right to left to avoid using updated values
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]
```

**🎯 GATE Point:** Right-to-left traversal is crucial! Left-to-right would allow multiple uses of same item.

### 3.6 Complexity

- Time: O(n × W)
- Space: O(W) optimized

### 3.7 Reconstructing Solution

```python
def knapsack_with_items(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Fill DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], 
                              dp[i - 1][w - weights[i - 1]] + values[i - 1])
    
    # Backtrack to find items
    items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items.append(i - 1)
            w -= weights[i - 1]
    
    return dp[n][capacity], items
```

---

## 📏 4. Longest Common Subsequence (LCS)

### 4.1 Problem Statement

Find longest subsequence common to two sequences.

**Subsequence:** Not necessarily contiguous, but order preserved.

### 4.2 Recurrence

Let $dp[i][j]$ = LCS length of first i chars of X and first j chars of Y.

$$dp[i][j] = \begin{cases}
0 & \text{if } i = 0 \text{ or } j = 0 \\
dp[i-1][j-1] + 1 & \text{if } X[i] = Y[j] \\
\max(dp[i-1][j], dp[i][j-1]) & \text{otherwise}
\end{cases}$$

### 4.3 Implementation

```python
def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]
```

### 4.4 Example

```
X = "ABCDGH", Y = "AEDFHR"

DP Table:
      ""  A  E  D  F  H  R
  ""   0  0  0  0  0  0  0
  A    0  1  1  1  1  1  1
  B    0  1  1  1  1  1  1
  C    0  1  1  1  1  1  1
  D    0  1  1  2  2  2  2
  G    0  1  1  2  2  2  2
  H    0  1  1  2  2  3  3

LCS = "ADH" (length 3)
```

### 4.5 Reconstructing LCS

```python
def lcs_string(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Backtrack
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))
```

### 4.6 Complexity

- Time: O(m × n)
- Space: O(m × n), can be O(min(m, n)) for length only

### 4.7 🎯 GATE Applications

**Shortest Common Supersequence (SCS):**
$$|SCS| = m + n - |LCS|$$

**Edit Distance:** Related but different recurrence.

---

## ✏️ 5. Edit Distance (Levenshtein)

### 5.1 Problem Statement

Minimum operations (insert, delete, replace) to convert string X to Y.

### 5.2 Recurrence

$$dp[i][j] = \begin{cases}
j & \text{if } i = 0 \\
i & \text{if } j = 0 \\
dp[i-1][j-1] & \text{if } X[i] = Y[j] \\
1 + \min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) & \text{otherwise}
\end{cases}$$

Where:
- $dp[i-1][j] + 1$: Delete from X
- $dp[i][j-1] + 1$: Insert into X
- $dp[i-1][j-1] + 1$: Replace in X

### 5.3 Implementation

```python
def edit_distance(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # Delete
                                  dp[i][j - 1],      # Insert
                                  dp[i - 1][j - 1])  # Replace
    
    return dp[m][n]
```

### 5.4 Example

```
X = "sunday", Y = "saturday"

DP Table:
      ""  s  a  t  u  r  d  a  y
  ""   0  1  2  3  4  5  6  7  8
  s    1  0  1  2  3  4  5  6  7
  u    2  1  1  2  2  3  4  5  6
  n    3  2  2  2  3  3  4  5  6
  d    4  3  3  3  3  4  3  4  5
  a    5  4  3  4  4  4  4  3  4
  y    6  5  4  4  5  5  5  4  3

Edit Distance: 3
```

### 5.5 Complexity

- Time: O(m × n)
- Space: O(m × n), can be O(min(m, n))

---

## ⛓️ 6. Matrix Chain Multiplication

### 6.1 Problem Statement

Given matrices $A_1, A_2, ..., A_n$ with dimensions $p_0 \times p_1, p_1 \times p_2, ..., p_{n-1} \times p_n$, find parenthesization that minimizes scalar multiplications.

### 6.2 Recurrence

Let $dp[i][j]$ = minimum cost to multiply $A_i$ through $A_j$.

$$dp[i][j] = \begin{cases}
0 & \text{if } i = j \\
\min_{i \leq k < j} \{dp[i][k] + dp[k+1][j] + p_{i-1} \cdot p_k \cdot p_j\} & \text{otherwise}
\end{cases}$$

### 6.3 Implementation

```python
def matrix_chain(dims):
    n = len(dims) - 1  # Number of matrices
    dp = [[0] * n for _ in range(n)]
    
    # l is chain length
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1]
```

### 6.4 Example

```
Matrices: A(10×30), B(30×5), C(5×60)
dims = [10, 30, 5, 60]

Options:
(AB)C: (10×30×5) + (10×5×60) = 1500 + 3000 = 4500
A(BC): (30×5×60) + (10×30×60) = 9000 + 18000 = 27000

Optimal: 4500
```

### 6.5 Complexity

- Time: O(n³)
- Space: O(n²)

### 6.6 🎯 GATE Point: Number of Parenthesizations

For n matrices, number of ways = Catalan number $C_{n-1}$

$$C_n = \frac{1}{n+1}\binom{2n}{n} = \frac{(2n)!}{(n+1)!n!}$$

| n | Parenthesizations |
|---|-------------------|
| 2 | 1 |
| 3 | 2 |
| 4 | 5 |
| 5 | 14 |

---

## 📈 7. Longest Increasing Subsequence (LIS)

### 7.1 Problem Statement

Find length of longest strictly increasing subsequence.

### 7.2 O(n²) DP Solution

```python
def lis_n2(arr):
    n = len(arr)
    dp = [1] * n  # dp[i] = LIS ending at i
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
```

### 7.3 O(n log n) Binary Search Solution

```python
import bisect

def lis_nlogn(arr):
    # tails[i] = smallest ending element for LIS of length i+1
    tails = []
    
    for num in arr:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    
    return len(tails)
```

### 7.4 Example

```
arr = [10, 9, 2, 5, 3, 7, 101, 18]

Processing:
10 → tails = [10]
9  → tails = [9]
2  → tails = [2]
5  → tails = [2, 5]
3  → tails = [2, 3]
7  → tails = [2, 3, 7]
101→ tails = [2, 3, 7, 101]
18 → tails = [2, 3, 7, 18]

LIS length = 4
```

### 7.5 Complexity

- O(n²): Simple DP
- O(n log n): Binary search optimization

### 7.6 🎯 Applications

- Longest Chain of Pairs
- Box Stacking Problem
- Maximum Sum Increasing Subsequence

---

## 💰 8. Coin Change Variants

### 8.1 Minimum Coins

```python
def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
    
    return dp[amount] if dp[amount] != float('inf') else -1
```

### 8.2 Number of Ways

```python
def count_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]
```

### 8.3 🎯 Order Matters!

**Combinations (order doesn't matter):** Iterate coins first (as above)
**Permutations (order matters):** Iterate amounts first

```python
def count_permutations(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] += dp[i - coin]
    
    return dp[amount]
```

---

## 🌳 9. Optimal Binary Search Tree

### 9.1 Problem Statement

Given keys with access probabilities, construct BST minimizing expected search cost.

### 9.2 Recurrence

Let $dp[i][j]$ = minimum cost for keys $k_i$ to $k_j$.
Let $w[i][j]$ = sum of probabilities from $k_i$ to $k_j$.

$$dp[i][j] = \min_{i \leq r \leq j} \{dp[i][r-1] + dp[r+1][j] + w[i][j]\}$$

### 9.3 Implementation

```python
def optimal_bst(keys, freq):
    n = len(keys)
    
    # Cost table
    dp = [[0] * n for _ in range(n)]
    
    # Base case: single keys
    for i in range(n):
        dp[i][i] = freq[i]
    
    # Fill for increasing lengths
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            # Sum of frequencies
            w = sum(freq[i:j + 1])
            
            # Try each key as root
            for r in range(i, j + 1):
                left = dp[i][r - 1] if r > i else 0
                right = dp[r + 1][j] if r < j else 0
                cost = left + right + w
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1]
```

### 9.4 Complexity

- Time: O(n³)
- Space: O(n²)
- With Knuth's optimization: O(n²)

---

## 📊 10. DP on Trees

### 10.1 Maximum Independent Set

```python
def max_independent_set(root):
    # Returns (include_root, exclude_root)
    if not root:
        return (0, 0)
    
    total_include = root.value
    total_exclude = 0
    
    for child in root.children:
        include_child, exclude_child = max_independent_set(child)
        total_include += exclude_child  # Can't include adjacent
        total_exclude += max(include_child, exclude_child)
    
    return (total_include, total_exclude)
```

### 10.2 Tree Diameter

```python
def tree_diameter(root):
    diameter = [0]
    
    def height(node):
        if not node:
            return 0
        
        heights = sorted([height(child) for child in node.children], reverse=True)
        
        # Diameter through this node
        if len(heights) >= 2:
            diameter[0] = max(diameter[0], heights[0] + heights[1])
        elif len(heights) == 1:
            diameter[0] = max(diameter[0], heights[0])
        
        return 1 + (heights[0] if heights else 0)
    
    height(root)
    return diameter[0]
```

---

## 🔲 11. DP on Grids

### 11.1 Unique Paths

```python
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    return dp[m - 1][n - 1]
```

**Formula:** $\binom{m+n-2}{m-1}$ (Combinatorics!)

### 11.2 Minimum Path Sum

```python
def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                grid[i][j] += grid[i][j - 1]
            elif j == 0:
                grid[i][j] += grid[i - 1][j]
            else:
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
    
    return grid[m - 1][n - 1]
```

---

## 🎓 12. GATE Pattern Problems

### Problem Type 1: Recurrence Identification

**Q:** What's the recurrence for LCS?

**Answer:**
$$dp[i][j] = \begin{cases}
dp[i-1][j-1] + 1 & \text{if } X[i] = Y[j] \\
\max(dp[i-1][j], dp[i][j-1]) & \text{otherwise}
\end{cases}$$

---

### Problem Type 2: Complexity Analysis

**Q:** Time complexity of matrix chain multiplication for n matrices?

**Solution:**
- Two loops: O(n²) subproblems
- Each subproblem: O(n) choices

**Answer: O(n³)**

---

### Problem Type 3: DP Table Filling

**Q:** For strings "ABC" and "AC", fill LCS table.

**Solution:**
```
      ""  A  C
  ""   0  0  0
  A    0  1  1
  B    0  1  1
  C    0  1  2

LCS = 2 ("AC")
```

---

## 🚨 13. Common GATE Traps

### Trap 1: Wrong Base Case

Always handle edge cases: empty strings, capacity 0, etc.

### Trap 2: Off-by-One Indexing

Be consistent: 0-indexed or 1-indexed?

### Trap 3: Confusing Subsequence vs Substring

- **Subsequence:** Not contiguous (LCS)
- **Substring:** Contiguous (Longest Common Substring)

### Trap 4: Direction of Traversal

- 0/1 Knapsack: Right-to-left for space optimization
- Unbounded Knapsack: Left-to-right

### Trap 5: Counting vs Optimization

- Counting: Add paths/ways
- Optimization: Take min/max

---

## 📝 14. Practice Problems

### Problem 1 [NAT]
LCS of "AGGTAB" and "GXTXAYB"?

<details>
<summary>Solution</summary>

LCS = "GTAB" (length 4)

**Answer: 4**
</details>

---

### Problem 2 [MCQ]
0/1 Knapsack with n=4, W=5. Space complexity with optimization?

A. O(n × W)
B. O(W)
C. O(n)
D. O(1)

<details>
<summary>Solution</summary>

With single array optimization: O(W)

**Answer:** B
</details>

---

### Problem 3 [MSQ]
Which have O(n²) DP solution?

A. LCS
B. LIS (basic)
C. Matrix Chain Multiplication
D. Fibonacci

<details>
<summary>Solution</summary>

A. TRUE - O(m×n) = O(n²) for equal length strings
B. TRUE - Basic DP is O(n²)
C. FALSE - O(n³)
D. FALSE - O(n)

**Answer:** A, B
</details>

---

## 🧠 Memory Anchors

### The DP Recipe (SROBT)

1. **S**ubproblem: Define what dp[i] or dp[i][j] represents
2. **R**ecurrence: Write relation between subproblems
3. **O**rder: Determine computation order (dependencies)
4. **B**ase: Set base cases
5. **T**able: Fill and return answer

### The Bizarre Mnemonic: "Robot Climbing Stairs"

Imagine a robot on a grid:
- **Unique Paths:** Robot counts ways to reach goal
- **Min Path Sum:** Robot finds cheapest route
- **LCS:** Two robots finding common path
- **Edit Distance:** Robot transforming one path to another

### 5-Second Sanity Check

1. Did I define what dp[i] means?
2. Are base cases correct?
3. Is computation order respecting dependencies?
4. Is final answer in dp[n] or dp[n-1]?

---

## ⚡ Quick Reference

| Problem | Recurrence Type | Time | Space |
|---------|-----------------|------|-------|
| Fibonacci | dp[i] = dp[i-1] + dp[i-2] | O(n) | O(1) |
| 0/1 Knapsack | dp[i][w] | O(nW) | O(W) |
| LCS | dp[i][j] | O(mn) | O(min(m,n)) |
| Edit Distance | dp[i][j] | O(mn) | O(min(m,n)) |
| Matrix Chain | dp[i][j] with k loop | O(n³) | O(n²) |
| LIS | dp[i] = max{dp[j]+1} | O(n²) / O(n log n) | O(n) |
| Coin Change | dp[i] | O(nS) | O(S) |
| Optimal BST | dp[i][j] with r loop | O(n³) / O(n²) | O(n²) |

---

**✅ Module Complete | Ready for GATE 2026**

**Next Module:** [Graph Algorithms →](07-Graph-Algorithms.md)
