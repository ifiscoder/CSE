# Module 2: Searching Algorithms

## 🎯 The Atomic Truth
> **"Finding needle in haystack—smartly"**

---

## 🧠 Mental Model: The Library Search

Imagine finding a book in a library:
- **Linear Search** = Walking shelf by shelf
- **Binary Search** = Using the catalog, jumping to section
- **Hash-based** = Having exact shelf coordinates

[Image: Library with organized shelves, a person with a catalog, and GPS coordinates]

---

## 📚 1. Linear Search | The Brute Force

### 1.1 Algorithm

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

### 1.2 Analysis

| Case | Complexity | When |
|------|------------|------|
| Best | O(1) | Target at first position |
| Average | O(n/2) = O(n) | Target uniformly distributed |
| Worst | O(n) | Target at last or not present |
| Space | O(1) | No extra space |

### 1.3 When to Use
- Unsorted or small arrays
- One-time search (sorting overhead > linear scan)
- Linked lists (no random access)

---

## 🎯 2. Binary Search | The Divide-and-Conquer Genius

### 2.1 The Atomic Truth
> **"Halve the search space each step"**

### 2.2 Prerequisites
- Array must be **SORTED**
- Random access (array, not linked list)

### 2.3 Algorithm: Iterative

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = low + (high - low) // 2  # Prevents overflow!
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1
```

### 2.4 Algorithm: Recursive

```python
def binary_search_rec(arr, target, low, high):
    if low > high:
        return -1
    
    mid = low + (high - low) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_rec(arr, target, mid + 1, high)
    else:
        return binary_search_rec(arr, target, low, mid - 1)
```

### 2.5 Complexity Analysis

**Recurrence:** $T(n) = T(n/2) + O(1)$

Using Master Theorem:
- $a = 1, b = 2, f(n) = 1$
- $\log_b a = 0$, $f(n) = \Theta(n^0) = \Theta(1)$
- **Case 2:** $T(n) = \Theta(\log n)$

| Case | Complexity |
|------|------------|
| Best | O(1) |
| Average | O(log n) |
| Worst | O(log n) |
| Space (iterative) | O(1) |
| Space (recursive) | O(log n) - stack |

### 2.6 🎯 Critical: Mid Calculation

**Wrong:** `mid = (low + high) / 2`
- Causes **integer overflow** when low + high > INT_MAX

**Right:** `mid = low + (high - low) / 2`
- Safe from overflow

### 2.7 Number of Comparisons

Maximum comparisons: $\lfloor \log_2 n \rfloor + 1$

| n | Max Comparisons |
|---|-----------------|
| 1 | 1 |
| 7 | 3 |
| 15 | 4 |
| 1023 | 10 |
| 1,000,000 | 20 |

**🧠 Intuition:** $2^{20} = 1,048,576 \approx 10^6$

---

## 🔧 3. Binary Search Variants | The GATE Favorites

### 3.1 Find First Occurrence

```python
def first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            result = mid       # Found, but keep looking left
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return result
```

### 3.2 Find Last Occurrence

```python
def last_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            result = mid       # Found, but keep looking right
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return result
```

### 3.3 Count Occurrences

```python
def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    if first == -1:
        return 0
    last = last_occurrence(arr, target)
    return last - first + 1
```

**Complexity:** O(log n) - Two binary searches

---

### 3.4 Lower Bound (≥ target)

Find smallest element ≥ target (C++ `lower_bound`)

```python
def lower_bound(arr, target):
    low, high = 0, len(arr)
    
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    
    return low  # Index of first element ≥ target
```

### 3.5 Upper Bound (> target)

Find smallest element > target (C++ `upper_bound`)

```python
def upper_bound(arr, target):
    low, high = 0, len(arr)
    
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid
    
    return low  # Index of first element > target
```

### 3.6 🎯 GATE Trick: lower_bound - upper_bound = count

```python
count = upper_bound(arr, x) - lower_bound(arr, x)
```

---

## 🌀 4. Search in Rotated Sorted Array

### 4.1 Problem
Array was sorted but rotated k times. Find element in O(log n).

Example: `[4, 5, 6, 7, 0, 1, 2]` (rotation of `[0, 1, 2, 4, 5, 6, 7]`)

### 4.2 Algorithm

```python
def search_rotated(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            return mid
        
        # Left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return -1
```

### 4.3 Key Insight

At least one half (left or right of mid) is **always sorted**.
- If `arr[low] <= arr[mid]`: Left half is sorted
- Otherwise: Right half is sorted

**Complexity:** O(log n)

---

## 🔢 5. Binary Search on Answer | Powerful Technique

### 5.1 The Atomic Truth
> **"Don't search for element, search for answer"**

### 5.2 When to Use
- Answer lies in a range [low, high]
- Checking if answer = x is possible in O(f(n))
- Answers form a **monotonic** sequence (all NO then all YES, or vice versa)

### 5.3 Template

```python
def binary_search_on_answer(low, high, is_valid):
    result = -1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if is_valid(mid):
            result = mid
            high = mid - 1  # Find smaller valid answer
            # OR low = mid + 1 for larger valid answer
        else:
            low = mid + 1
    
    return result
```

### 5.4 Example: Square Root (Integer)

```python
def integer_sqrt(n):
    if n < 2:
        return n
    
    low, high = 1, n // 2
    
    while low <= high:
        mid = low + (high - low) // 2
        square = mid * mid
        
        if square == n:
            return mid
        elif square < n:
            low = mid + 1
        else:
            high = mid - 1
    
    return high  # Floor of sqrt
```

### 5.5 Example: Minimum Pages (Allocate Books)

Given `n` books with pages `[p1, p2, ..., pn]`, allocate to `m` students such that maximum pages assigned to any student is minimized.

```python
def is_valid(pages, m, max_pages):
    students = 1
    current = 0
    
    for p in pages:
        if p > max_pages:  # Single book too large
            return False
        if current + p > max_pages:
            students += 1
            current = p
        else:
            current += p
    
    return students <= m

def min_pages(pages, m):
    low = max(pages)          # At least largest book
    high = sum(pages)         # At most all books to one person
    result = high
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if is_valid(pages, m, mid):
            result = mid
            high = mid - 1    # Try for smaller maximum
        else:
            low = mid + 1
    
    return result
```

---

## 🎲 6. Ternary Search

### 6.1 When to Use
- Finding maximum/minimum of **unimodal** function
- Function first increases then decreases (or vice versa)

### 6.2 Algorithm

```python
def ternary_search(f, low, high, eps=1e-9):
    while high - low > eps:
        mid1 = low + (high - low) / 3
        mid2 = high - (high - low) / 3
        
        if f(mid1) < f(mid2):
            low = mid1
        else:
            high = mid2
    
    return (low + high) / 2
```

### 6.3 Complexity

Each iteration reduces search space by 1/3.

$$T(n) = T(2n/3) + O(1) = O(\log_{3/2} n) = O(\log n)$$

### 6.4 Binary vs Ternary Search

| Aspect | Binary | Ternary |
|--------|--------|---------|
| Comparisons per iteration | 1-2 | 2 |
| Reduction factor | 1/2 | 1/3 |
| Total comparisons | log₂ n | 2 log₁.₅ n ≈ 1.6 log₂ n |
| Winner | ✓ | ✗ |

**🎯 GATE Trap:** Ternary search seems faster (dividing by 3) but needs 2 comparisons per step, making it **slower** than binary search!

---

## 🧮 7. Exponential Search

### 7.1 When to Use
- Unbounded/infinite arrays
- Element likely near beginning

### 7.2 Algorithm

```python
def exponential_search(arr, target):
    n = len(arr)
    
    if arr[0] == target:
        return 0
    
    # Find range [i/2, i] where element lies
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    
    # Binary search in that range
    return binary_search(arr, target, i // 2, min(i, n - 1))
```

### 7.3 Complexity

- Finding range: O(log k) where k is position
- Binary search in range: O(log k)
- **Total:** O(log k)

Useful when element is at position k << n.

---

## 🏃 8. Jump Search

### 8.1 Algorithm

Jump by fixed steps, then linear search.

```python
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # Optimal jump size
    
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Linear search in block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[prev] == target:
        return prev
    
    return -1
```

### 8.2 Optimal Jump Size

If jump size = $m$, worst case comparisons:
$$\frac{n}{m} + m - 1$$

Minimize: $\frac{d}{dm}\left(\frac{n}{m} + m\right) = 0$
$$-\frac{n}{m^2} + 1 = 0 \implies m = \sqrt{n}$$

**Optimal complexity:** $O(\sqrt{n})$

### 8.3 Use Case
- When backward traversal is costly (tape storage)
- Binary search requires O(log n) backward jumps

---

## 📊 9. Interpolation Search

### 9.1 The Atomic Truth
> **"Guess position based on value"**

### 9.2 Algorithm

```python
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high and arr[low] <= target <= arr[high]:
        if arr[low] == arr[high]:
            if arr[low] == target:
                return low
            return -1
        
        # Interpolation formula
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    
    return -1
```

### 9.3 Complexity

| Distribution | Complexity |
|--------------|------------|
| Uniform | O(log log n) |
| Non-uniform | O(n) worst case |

### 9.4 When to Use
- Uniformly distributed sorted data
- Large datasets where O(log log n) matters

---

## 🔗 10. Searching in Special Structures

### 10.1 Search in 2D Sorted Matrix

**Row-wise and column-wise sorted matrix:**

```
1   4   7   11
2   5   8   12
3   6   9   16
10  13  14  17
```

```python
def search_2d_matrix(matrix, target):
    if not matrix:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1  # Start from top-right
    
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    
    return False
```

**Complexity:** O(m + n) where m = rows, n = columns

### 10.2 Search in Row-Major Sorted 2D Array

**Entire matrix sorted when flattened:**

```
1   3   5
7   9   11
13  15  17
```

```python
def search_sorted_2d(matrix, target):
    if not matrix:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        row, col = mid // cols, mid % cols
        
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False
```

**Complexity:** O(log(mn))

---

## 🎯 11. GATE Pattern Problems

### Problem Type 1: Minimum Comparisons

**Q:** What is the minimum number of comparisons to find an element in a sorted array of 1000 elements?

**Solution:**
- Binary search: $\lfloor \log_2 1000 \rfloor + 1 = 10$ comparisons
- Answer: **10**

---

### Problem Type 2: Failed Search Comparisons

**Q:** In unsuccessful search in binary search, how many comparisons for n = 15?

**Solution:**
- Search ends when range is empty
- Depth of decision tree = $\lfloor \log_2 15 \rfloor + 1 = 4$
- Answer: **4**

---

### Problem Type 3: Average Comparisons

**Q:** For successful binary search in array of size n, what is the average number of comparisons?

**Solution:**
The internal path length of binary search tree with n nodes.

$$C_{avg} = \frac{1}{n}\sum_{i=1}^{n}(\text{comparisons to find element } i)$$

For complete binary tree:
$$C_{avg} \approx \log_2 n - 1$$

More precisely:
$$C_{avg} = \frac{(n+1)\lfloor\log_2 n\rfloor + 2(n+1) - 2^{\lfloor\log_2 n\rfloor + 1}}{n}$$

---

## 🚨 12. Common GATE Traps

### Trap 1: Unsorted Array Binary Search
Binary search **REQUIRES** sorted array. If not sorted, answer is O(n).

### Trap 2: Integer Overflow
```c
int mid = (low + high) / 2;  // WRONG - can overflow
int mid = low + (high - low) / 2;  // CORRECT
```

### Trap 3: Infinite Loop in Binary Search
```c
// WRONG
while (low < high) {
    mid = (low + high) / 2;
    if (arr[mid] < target)
        low = mid;  // Should be mid + 1
}
```

### Trap 4: Off-by-One Errors
- `low <= high` vs `low < high`
- `mid + 1` vs `mid`
- `high = mid - 1` vs `high = mid`

### Trap 5: Ternary Search Complexity
Ternary search is **NOT** faster than binary search (constant factor difference in log).

---

## 📝 13. Practice Problems

### Problem 1 [NAT]
An array has 1023 elements. What is the maximum number of comparisons to find an element using binary search?

<details>
<summary>Solution</summary>

$\lfloor \log_2 1023 \rfloor + 1 = 9 + 1 = 10$

**Answer:** 10
</details>

---

### Problem 2 [MCQ]
Time complexity of binary search on a doubly linked list of n sorted elements?

A. O(log n)
B. O(n log n)
C. O(n)
D. O(1)

<details>
<summary>Solution</summary>

Linked list has no random access. Finding mid takes O(n/2).
Total: T(n) = T(n/2) + O(n) = O(n)

**Answer:** C
</details>

---

### Problem 3 [MSQ]
Which of the following is/are TRUE about interpolation search?

A. Works on sorted arrays only
B. O(log log n) for uniformly distributed data
C. O(n) worst case
D. Always faster than binary search

<details>
<summary>Solution</summary>

A. TRUE - Requires sorted data
B. TRUE - For uniform distribution
C. TRUE - For skewed distribution
D. FALSE - Only faster for uniform data

**Answer:** A, B, C
</details>

---

### Problem 4 [MCQ]
In a rotated sorted array of distinct elements, what is the time complexity to find the minimum element?

A. O(n)
B. O(log n)
C. O(n log n)
D. O(1)

<details>
<summary>Solution</summary>

Modified binary search can find the pivot (minimum) in O(log n).

**Answer:** B
</details>

---

## 🧠 Memory Anchors

### The Mental Slider: Search Efficiency Dial

[Image: Dial showing search algorithms from Linear to Hash]

- **O(n):** Walking step by step
- **O(√n):** Jumping then walking
- **O(log n):** Halving each step
- **O(log log n):** Intelligent jumping
- **O(1):** Direct access

### The Bizarre Mnemonic: "Binary Search as Guessing Game"

You're guessing a number 1-100. After each guess, you get "higher" or "lower".

**Genius Strategy:** Always guess the middle.
- 100 → 50 → 25 → 12 → 6 → 3 → 1
- Maximum 7 guesses for 1-100 (log₂ 100 ≈ 7)

### 5-Second Sanity Check

1. Is array sorted? No → Binary search won't work
2. Maximum comparisons ≈ log₂ n + 1
3. For n = 10⁶, binary search needs ~20 comparisons (2²⁰ ≈ 10⁶)

---

## ⚡ Quick Reference

| Algorithm | Time | Space | Sorted? | Best For |
|-----------|------|-------|---------|----------|
| Linear | O(n) | O(1) | No | Small/unsorted |
| Binary | O(log n) | O(1) | Yes | General sorted |
| Jump | O(√n) | O(1) | Yes | Sequential storage |
| Interpolation | O(log log n) | O(1) | Yes | Uniform data |
| Exponential | O(log k) | O(1) | Yes | Unknown bounds |
| Ternary | O(log n) | O(1) | - | Unimodal functions |

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

**Next Module:** [Sorting Algorithms →](03-Sorting-Algorithms.md)
