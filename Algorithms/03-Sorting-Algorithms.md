# Module 3: Sorting Algorithms

## 🎯 The Atomic Truth
> **"Order brings efficiency to chaos"**

---

## 🧠 Mental Model: Arranging Books on a Shelf

[Image: Messy bookshelf → Organized by height/alphabet]

Different strategies for organizing:
- **Bubble Sort:** Compare neighbors, swap if wrong
- **Selection Sort:** Find smallest, place at beginning
- **Insertion Sort:** Pick one, insert in right place
- **Merge Sort:** Split, sort halves, merge
- **Quick Sort:** Pick pivot, partition around it

---

## 📊 Master Comparison Table

| Algorithm | Best | Average | Worst | Space | Stable | In-place |
|-----------|------|---------|-------|-------|--------|----------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | ❌ | ✅ |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ | ❌ |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ | ✅ |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ | ✅ |
| Counting | O(n+k) | O(n+k) | O(n+k) | O(k) | ✅ | ❌ |
| Radix | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | O(n+k) | ✅ | ❌ |
| Bucket | O(n+k) | O(n+k) | O(n²) | O(n) | ✅ | ❌ |

---

## 🫧 1. Bubble Sort | The Naive Approach

### 1.1 The Atomic Truth
> **"Bubbles rise—largest element floats to end"**

### 1.2 Algorithm

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):  # Last i elements are sorted
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Optimization: already sorted
            break
    return arr
```

### 1.3 Visualization

```
Pass 1: [5, 3, 8, 4, 2] → [3, 5, 4, 2, 8]  (8 bubbles to end)
Pass 2: [3, 5, 4, 2, 8] → [3, 4, 2, 5, 8]  (5 bubbles to position)
Pass 3: [3, 4, 2, 5, 8] → [3, 2, 4, 5, 8]  (4 is in place)
Pass 4: [3, 2, 4, 5, 8] → [2, 3, 4, 5, 8]  (Done!)
```

### 1.4 Analysis

**Number of comparisons:** $\frac{n(n-1)}{2} = O(n^2)$

**Number of swaps:**
- Best: 0 (already sorted)
- Worst: $\frac{n(n-1)}{2}$ (reverse sorted)
- Average: $\frac{n(n-1)}{4}$

### 1.5 Properties
- ✅ **Stable:** Equal elements maintain relative order
- ✅ **In-place:** O(1) extra space
- ✅ **Adaptive:** O(n) on nearly sorted data

### 1.6 🎯 GATE Insight: Inversion Count

Each swap removes exactly ONE inversion.
Total swaps = Number of inversions

**Inversion:** Pair (i, j) where i < j but arr[i] > arr[j]

---

## 🎯 2. Selection Sort | Find the Minimum

### 2.1 The Atomic Truth
> **"Select minimum, place at front"**

### 2.2 Algorithm

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

### 2.3 Visualization

```
[64, 25, 12, 22, 11]  → Find min (11) → [11, 25, 12, 22, 64]
[11, 25, 12, 22, 64]  → Find min (12) → [11, 12, 25, 22, 64]
[11, 12, 25, 22, 64]  → Find min (22) → [11, 12, 22, 25, 64]
[11, 12, 22, 25, 64]  → Find min (25) → [11, 12, 22, 25, 64]
```

### 2.4 Analysis

**Comparisons:** Always $\frac{n(n-1)}{2}$ (regardless of input)

**Swaps:** Exactly $n - 1$ (one per pass)

| Case | Comparisons | Swaps |
|------|-------------|-------|
| Best | O(n²) | O(n) |
| Worst | O(n²) | O(n) |

### 2.5 Properties
- ❌ **NOT Stable:** Can swap equal elements out of order
- ✅ **In-place:** O(1) extra space
- ❌ **NOT Adaptive:** Always O(n²) comparisons

### 2.6 When to Use
- When **swap cost is high** (large records)
- Memory write is expensive (flash memory)

---

## 📥 3. Insertion Sort | The Card Player

### 3.1 The Atomic Truth
> **"Insert each card in its proper position"**

### 3.2 Algorithm

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift right
            j -= 1
        arr[j + 1] = key  # Insert
    return arr
```

### 3.3 Visualization

```
[5, 2, 4, 6, 1, 3]
Insert 2: [2, 5, 4, 6, 1, 3]
Insert 4: [2, 4, 5, 6, 1, 3]
Insert 6: [2, 4, 5, 6, 1, 3]  (no movement)
Insert 1: [1, 2, 4, 5, 6, 3]
Insert 3: [1, 2, 3, 4, 5, 6]
```

### 3.4 Analysis

| Case | Condition | Comparisons | Shifts |
|------|-----------|-------------|--------|
| Best | Already sorted | n - 1 = O(n) | 0 |
| Worst | Reverse sorted | n(n-1)/2 = O(n²) | n(n-1)/2 |
| Average | Random | n²/4 = O(n²) | n²/4 |

### 3.5 Properties
- ✅ **Stable:** Equal elements stay in order
- ✅ **In-place:** O(1) space
- ✅ **Adaptive:** O(n) on nearly sorted data
- ✅ **Online:** Can sort as data arrives

### 3.6 When to Use
- Small arrays (n < 50)
- Nearly sorted data (few inversions)
- Online sorting (streaming data)
- Used as base case in hybrid sorts

### 3.7 Binary Insertion Sort

Use binary search to find insertion position.

**Comparisons:** O(n log n)
**Shifts:** Still O(n²)
**Total:** O(n²) - doesn't help overall

---

## 🔀 4. Merge Sort | Divide and Conquer

### 4.1 The Atomic Truth
> **"Split, sort halves, merge—guaranteed O(n log n)"**

### 4.2 Algorithm

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # <= for stability
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### 4.3 Visualization

```
[38, 27, 43, 3, 9, 82, 10]
        /              \
[38, 27, 43, 3]    [9, 82, 10]
    /      \          /     \
[38, 27]  [43, 3]  [9, 82]  [10]
  /  \      /  \     /  \
[38][27]  [43][3]  [9][82] [10]

Merge up:
[27, 38]  [3, 43]  [9, 82]  [10]
   \      /           \      /
[3, 27, 38, 43]    [9, 10, 82]
        \            /
[3, 9, 10, 27, 38, 43, 82]
```

### 4.4 Recurrence Analysis

$$T(n) = 2T(n/2) + O(n)$$

Using Master Theorem:
- $a = 2, b = 2, f(n) = n$
- $\log_b a = 1$
- $f(n) = \Theta(n^1)$
- **Case 2:** $T(n) = \Theta(n \log n)$

### 4.5 Detailed Analysis

| Metric | Value |
|--------|-------|
| Comparisons | $n \log n - n + 1$ (approximately) |
| Maximum comparisons | $n \log n$ |
| Minimum comparisons | $\frac{n \log n}{2}$ |
| Moves | $2n \log n$ |

### 4.6 Properties
- ✅ **Stable:** When merging, equal left element comes first
- ❌ **NOT In-place:** O(n) extra space
- ❌ **NOT Adaptive:** Always O(n log n)
- ✅ **Parallelizable:** Independent subproblems

### 4.7 When to Use
- Need guaranteed O(n log n)
- Stability required
- Sorting linked lists (O(1) space for lists!)
- External sorting (large files)

### 4.8 Space-Optimized Merge Sort

For linked lists: O(1) space possible using pointer manipulation.

---

## ⚡ 5. Quick Sort | The Practical Champion

### 5.1 The Atomic Truth
> **"Pivot in place—smaller left, larger right"**

### 5.2 Algorithm

```python
def quick_sort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Rightmost as pivot
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

### 5.3 Partition Visualization (Lomuto Scheme)

```
arr = [10, 7, 8, 9, 1, 5], pivot = 5

i = -1
j = 0: arr[0]=10 > 5, no swap
j = 1: arr[1]=7 > 5, no swap
j = 2: arr[2]=8 > 5, no swap
j = 3: arr[3]=9 > 5, no swap
j = 4: arr[4]=1 ≤ 5, i=0, swap → [1, 7, 8, 9, 10, 5]

Swap pivot: [1, 5, 8, 9, 10, 7]
                ↑ pivot at index 1
```

### 5.4 Hoare's Partition (More Efficient)

```python
def hoare_partition(arr, low, high):
    pivot = arr[low]
    i, j = low - 1, high + 1
    
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        
        j -= 1
        while arr[j] > pivot:
            j -= 1
        
        if i >= j:
            return j
        
        arr[i], arr[j] = arr[j], arr[i]
```

**Hoare's does 3x fewer swaps on average!**

### 5.5 Recurrence Analysis

**Best/Average Case:** Balanced partitions
$$T(n) = 2T(n/2) + O(n) = O(n \log n)$$

**Worst Case:** Unbalanced partitions (sorted/reverse sorted)
$$T(n) = T(n-1) + O(n) = O(n^2)$$

### 5.6 Pivot Selection Strategies

| Strategy | Description | Worst Case Probability |
|----------|-------------|----------------------|
| First/Last | Always pick first/last | High for sorted data |
| Random | Pick random element | 1/n! (very low) |
| Median-of-3 | Median of first, mid, last | Low |
| Median-of-medians | True median | Impossible (O(n) guaranteed) |

### 5.7 Properties
- ❌ **NOT Stable:** Partitioning can swap equal elements
- ✅ **In-place:** O(log n) stack space
- ❌ **NOT Adaptive:** No benefit from sorted data

### 5.8 Why Quick Sort is Often Fastest

1. **Cache efficiency:** Sequential access pattern
2. **Low overhead:** Simple inner loop
3. **In-place:** No memory allocation
4. **Tail recursion:** Can optimize smaller recursion

### 5.9 Tail-Call Optimization

```python
def quick_sort_optimized(arr, low, high):
    while low < high:
        pivot_idx = partition(arr, low, high)
        
        # Recurse on smaller partition
        if pivot_idx - low < high - pivot_idx:
            quick_sort_optimized(arr, low, pivot_idx - 1)
            low = pivot_idx + 1
        else:
            quick_sort_optimized(arr, pivot_idx + 1, high)
            high = pivot_idx - 1
```

**Stack space:** Guaranteed O(log n) even in worst case!

### 5.10 3-Way Quick Sort (For Duplicates)

```python
def quick_sort_3way(arr, low, high):
    if low >= high:
        return
    
    pivot = arr[low]
    lt, gt = low, high
    i = low
    
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else:
            i += 1
    
    quick_sort_3way(arr, low, lt - 1)
    quick_sort_3way(arr, gt + 1, high)
```

**Complexity:** O(n) for all equal elements!

---

## 🏔️ 6. Heap Sort | Priority Queue Based

### 6.1 The Atomic Truth
> **"Build max-heap, extract max repeatedly"**

### 6.2 Heap Property

**Max-Heap:** Parent ≥ Children
**Min-Heap:** Parent ≤ Children

Array representation:
- Parent of i: (i-1)/2
- Left child of i: 2i + 1
- Right child of i: 2i + 2

### 6.3 Heapify (Restore Heap Property)

```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

### 6.4 Build Heap

```python
def build_heap(arr):
    n = len(arr)
    # Start from last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
```

**Why start from n/2 - 1?**
Leaves (from n/2 to n-1) are trivially heaps.

**Build Heap Complexity:** O(n) (NOT O(n log n)!)

**Proof:**
$$\sum_{h=0}^{\log n} \frac{n}{2^{h+1}} \cdot O(h) = O(n \sum_{h=0}^{\infty} \frac{h}{2^h}) = O(n)$$

### 6.5 Heap Sort Algorithm

```python
def heap_sort(arr):
    n = len(arr)
    
    # Build max-heap
    build_heap(arr)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move max to end
        heapify(arr, i, 0)  # Heapify reduced heap
    
    return arr
```

### 6.6 Analysis

| Metric | Complexity |
|--------|------------|
| Build heap | O(n) |
| n extractions | O(n log n) |
| **Total** | **O(n log n)** |
| Space | O(1) |

### 6.7 Properties
- ❌ **NOT Stable:** Heap operations can reorder equal elements
- ✅ **In-place:** O(1) extra space
- ❌ **NOT Adaptive:** Always O(n log n)

### 6.8 Heap Sort vs Quick Sort

| Aspect | Heap Sort | Quick Sort |
|--------|-----------|------------|
| Worst case | O(n log n) | O(n²) |
| Average case | O(n log n) | O(n log n) |
| Cache performance | Poor | Excellent |
| Stability | No | No |
| In-place | Yes | Yes |
| Practical speed | Slower | Faster |

---

## 🔢 7. Counting Sort | When Values are Small

### 7.1 The Atomic Truth
> **"Count occurrences, calculate positions"**

### 7.2 Prerequisites
- Elements are integers in range [0, k]
- k = O(n) for linear time

### 7.3 Algorithm

```python
def counting_sort(arr, k):
    n = len(arr)
    count = [0] * (k + 1)
    output = [0] * n
    
    # Count occurrences
    for x in arr:
        count[x] += 1
    
    # Cumulative count (positions)
    for i in range(1, k + 1):
        count[i] += count[i - 1]
    
    # Build output (stable: go right to left)
    for i in range(n - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    
    return output
```

### 7.4 Visualization

```
arr = [4, 2, 2, 8, 3, 3, 1], k = 8

Count:   [0, 1, 2, 2, 1, 0, 0, 0, 1]
          0  1  2  3  4  5  6  7  8

Cumulative: [0, 1, 3, 5, 6, 6, 6, 6, 7]
             0  1  2  3  4  5  6  7  8

Output: [1, 2, 2, 3, 3, 4, 8]
```

### 7.5 Analysis

| Metric | Complexity |
|--------|------------|
| Time | O(n + k) |
| Space | O(n + k) |

When k = O(n): **Linear time sorting!**

### 7.6 Properties
- ✅ **Stable:** Right-to-left pass preserves order
- ❌ **NOT In-place:** O(n + k) space
- ❌ **NOT Comparison-based:** Can beat O(n log n)

---

## 🔤 8. Radix Sort | Digit by Digit

### 8.1 The Atomic Truth
> **"Sort by each digit, from least to most significant"**

### 8.2 Algorithm

```python
def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for x in arr:
        digit = (x // exp) % 10
        count[digit] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
    
    for i in range(n):
        arr[i] = output[i]
```

### 8.3 Visualization

```
arr = [170, 45, 75, 90, 802, 24, 2, 66]

Sort by 1s digit: [170, 90, 802, 2, 24, 45, 75, 66]
Sort by 10s digit: [802, 2, 24, 45, 66, 170, 75, 90]
Sort by 100s digit: [2, 24, 45, 66, 75, 90, 170, 802]
```

### 8.4 Analysis

If numbers have d digits and each digit has k possible values:

$$T(n) = d \cdot O(n + k) = O(d(n + k))$$

For n numbers with maximum value M:
- d = log_k(M) digits
- Total: O(n log M) or O(n · d)

### 8.5 When is Radix Sort Better?

**Radix vs Comparison Sort:**

Radix: O(d · n) where d = log_k(max)
Quick Sort: O(n log n)

Radix is better when: $d < \log n$, i.e., $\max < n^{constant}$

### 8.6 Properties
- ✅ **Stable:** Uses stable counting sort
- ❌ **NOT In-place:** O(n) extra space
- ❌ **NOT Comparison-based**

---

## 🪣 9. Bucket Sort | Distribute and Conquer

### 9.1 The Atomic Truth
> **"Distribute to buckets, sort each, concatenate"**

### 9.2 Algorithm

```python
def bucket_sort(arr, num_buckets=10):
    if not arr:
        return arr
    
    min_val, max_val = min(arr), max(arr)
    bucket_range = (max_val - min_val) / num_buckets + 1
    
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribute elements
    for x in arr:
        idx = int((x - min_val) / bucket_range)
        buckets[idx].append(x)
    
    # Sort each bucket and concatenate
    result = []
    for bucket in buckets:
        insertion_sort(bucket)  # Or any stable sort
        result.extend(bucket)
    
    return result
```

### 9.3 Analysis

**Best/Average (uniform distribution):**
- n elements into n buckets → 1 element per bucket
- O(n) to distribute + O(n) to concatenate
- **Total: O(n)**

**Worst (all in one bucket):**
- Degrades to underlying sort
- **O(n²)** if using insertion sort

### 9.4 Properties
- ✅ **Stable:** If underlying sort is stable
- ❌ **NOT In-place:** O(n) extra space

---

## 📉 10. Comparison-Based Lower Bound

### 10.1 The Atomic Truth
> **"Decision tree height = minimum comparisons"**

### 10.2 Theorem

Any comparison-based sorting algorithm requires **Ω(n log n)** comparisons in the worst case.

### 10.3 Proof

A comparison-based algorithm is a decision tree:
- Internal nodes: comparisons
- Leaves: permutations (outputs)
- Number of leaves ≥ n! (all permutations possible)

For binary tree with L leaves:
$$\text{Height} \geq \log_2 L \geq \log_2(n!)$$

Using Stirling's approximation:
$$\log_2(n!) = n \log_2 n - n \log_2 e + O(\log n) = \Theta(n \log n)$$

**Therefore:** Minimum comparisons = Ω(n log n)

### 10.4 🎯 Key GATE Point

- Merge Sort, Heap Sort achieve O(n log n) → **Optimal** among comparison sorts
- Counting Sort, Radix Sort can do O(n) → NOT comparison-based (use element values directly)

---

## 🔄 11. Stability in Sorting

### 11.1 What is Stability?

**Stable Sort:** Equal elements maintain their relative order from input.

```
Input:  [(A,1), (B,2), (C,1)]  (sort by number)
Stable:  [(A,1), (C,1), (B,2)]  ← A before C (original order)
Unstable: [(C,1), (A,1), (B,2)]  ← Order changed
```

### 11.2 Why Stability Matters

1. **Multi-key sorting:** Sort by name, then by age → Stable sort preserves name order within same age
2. **Preserving previous order:** Multiple sort passes should respect earlier criteria

### 11.3 Making Unstable Sorts Stable

Add original index as secondary key:
```python
# For any comparison, use (key, original_index)
stable_arr = [(arr[i], i) for i in range(len(arr))]
unstable_sort(stable_arr)
```

Cost: O(n) extra space for indices

---

## 🎓 12. GATE Pattern Problems

### Problem Type 1: Count Operations

**Q:** How many swaps for Bubble Sort on [5, 1, 4, 2, 8]?

**Solution:** Count inversions = swaps
- (5,1), (5,4), (5,2), (4,2) = 4 inversions
- **Answer: 4 swaps**

---

### Problem Type 2: Best Case Identification

**Q:** Which sort has O(n) best case and O(n²) worst case?

**Solution:**
- Bubble: O(n) best (optimized), O(n²) worst ✓
- Insertion: O(n) best, O(n²) worst ✓
- Selection: O(n²) always ✗

**Answer: Bubble Sort, Insertion Sort**

---

### Problem Type 3: Stability Question

**Q:** Make Selection Sort stable. What changes?

**Solution:**
Instead of swapping, **shift elements right** and insert minimum at position.
```python
# Instead of swap:
min_val = arr[min_idx]
for j in range(min_idx, i, -1):
    arr[j] = arr[j-1]
arr[i] = min_val
```

Cost: O(n²) shifts instead of O(n) swaps

---

### Problem Type 4: Recurrence for Quick Sort

**Q:** If Quick Sort always partitions in ratio 1:9, what is complexity?

**Solution:**
$$T(n) = T(n/10) + T(9n/10) + O(n)$$

Recursion tree: Each level has total work O(n).
Depth determined by larger partition: $\log_{10/9} n = O(\log n)$

**Answer: O(n log n)** (constant ratio still gives log depth)

---

### Problem Type 5: External Sorting

**Q:** 1 GB file, 100 MB RAM. How many passes for external merge sort?

**Solution:**
- Initial runs: 1000 MB / 100 MB = 10 runs
- k-way merge with 100 MB: k = 10 (10 buffers of 10 MB each)
- Passes: $\lceil \log_{10} 10 \rceil = 1$

**Total: 1 creation pass + 1 merge pass = 2 passes**

---

## 🚨 13. Common GATE Traps

### Trap 1: Quick Sort Average vs Worst

**Question says "Quick Sort complexity"**
- If asking generally → O(n log n) average
- If given sorted input → O(n²) worst
- Read carefully!

### Trap 2: Build Heap Complexity

**WRONG:** Build heap is O(n log n)
**RIGHT:** Build heap is O(n)

### Trap 3: Counting Sort Space

Don't forget: O(n + k), not just O(k)

### Trap 4: Selection Sort Swaps

Selection Sort: Always n-1 swaps
Bubble Sort: Can be 0 to n(n-1)/2 swaps

### Trap 5: Radix Sort with Floating Points

Radix sort doesn't work directly on floating-point numbers!

---

## 📝 14. Practice Problems

### Problem 1 [NAT]
Minimum number of comparisons to merge two sorted arrays of sizes 3 and 5?

<details>
<summary>Solution</summary>

Minimum: max(3, 5) = 5 (when one array exhausts early)
Maximum: 3 + 5 - 1 = 7 (alternating elements)

**Answer:** Minimum = 5, Maximum = 7
</details>

---

### Problem 2 [MCQ]
Which sorting algorithm is best for nearly sorted data?

A. Quick Sort
B. Merge Sort
C. Insertion Sort
D. Heap Sort

<details>
<summary>Solution</summary>

Insertion Sort: O(n) on nearly sorted data (few inversions)
Others: Still O(n log n)

**Answer:** C
</details>

---

### Problem 3 [MSQ]
Which are TRUE for n elements in range [0, n²-1]?

A. Counting sort: O(n²)
B. Radix sort: O(n)
C. Quick sort: O(n log n) average
D. Bucket sort: O(n) average with uniform distribution

<details>
<summary>Solution</summary>

A. TRUE - k = n², so O(n + n²) = O(n²)
B. TRUE - d = 2 digits in base n, O(2n) = O(n)
C. TRUE - Always O(n log n) average
D. TRUE - With uniform distribution

**Answer:** A, B, C, D
</details>

---

## 🧠 Memory Anchors

### The Mental Slider: Sorting Selector

[Image: Decision tree for choosing sort algorithm]

```
Need guaranteed O(n log n)? → Merge/Heap Sort
Small array (n < 50)? → Insertion Sort
Nearly sorted? → Insertion Sort
Need stability? → Merge Sort
Integer range [0, k]? → Counting Sort (if k = O(n))
In-place required? → Quick/Heap Sort
External sorting? → Merge Sort variants
```

### The Bizarre Mnemonic: "SHIM BQ CRB"

**S**table sorts: **S**election? NO. **H**eap? NO. **I**nsertion? YES. **M**erge? YES. **B**ubble? YES. **Q**uick? NO.

**S**table = **I**nsertion, **M**erge, **B**ubble (and **C**ounting, **R**adix, **B**ucket)

Remember: "**I M B**ecause **C**lever **R**abbits **B**ounce" = Stable sorts

### 5-Second Sanity Check

1. Comparison sort → At least O(n log n)
2. In-place → O(log n) to O(n) stack space okay
3. Stable → Check: will equal elements stay ordered?

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

**Next Module:** [Divide and Conquer →](04-Divide-and-Conquer.md)
