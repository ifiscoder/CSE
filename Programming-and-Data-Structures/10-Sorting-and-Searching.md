# Part 10: Sorting & Searching

> **The Atomic Truth:** *Sorting = ordering elements; comparison-based lower bound = $\Omega(n \log n)$.*

---

## 10.1 Searching Algorithms

### Linear Search — $O(n)$

```c
int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++)
        if (arr[i] == key)
            return i;
    return -1;
}
```

**Best:** $O(1)$ (first element). **Average:** $O(n/2)$. **Worst:** $O(n)$.

### Binary Search — $O(\log n)$

**Prerequisite:** Array must be **sorted**.

```c
int binarySearch(int arr[], int n, int key) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;  // Avoid overflow!
        if (arr[mid] == key)
            return mid;
        else if (arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}
```

**Why `low + (high - low)/2` instead of `(low + high)/2`?** To prevent integer overflow when `low + high > INT_MAX`.

### Binary Search — Number of Comparisons

For $n$ elements:

$$\text{Max comparisons} = \lfloor \log_2 n \rfloor + 1$$

**Why?** Each comparison halves the search space. After $k$ comparisons, remaining elements ≤ $n/2^k$. Search ends when $n/2^k < 1$, i.e., $k > \log_2 n$.

### 🔴 GATE Trap: Binary Search Variants

Finding **first occurrence** of a key:
```c
int firstOccurrence(int arr[], int n, int key) {
    int low = 0, high = n - 1, result = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == key) {
            result = mid;
            high = mid - 1;  // Keep searching left
        } else if (arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return result;
}
```

Finding **last occurrence:** Change `high = mid - 1` to `low = mid + 1` in the equality case.

---

## 10.2 Sorting Algorithms — The Complete Picture

### The Master Comparison Table

| Algorithm | Best | Average | Worst | Space | Stable? | Method |
|-----------|------|---------|-------|-------|---------|--------|
| Bubble Sort | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ✅ | Comparison |
| Selection Sort | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ❌ | Comparison |
| Insertion Sort | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ✅ | Comparison |
| Merge Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | ✅ | Divide & Conquer |
| Quick Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | ❌ | Divide & Conquer |
| Heap Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | ❌ | Selection (Heap) |
| Counting Sort | $O(n + k)$ | $O(n + k)$ | $O(n + k)$ | $O(k)$ | ✅ | Non-comparison |
| Radix Sort | $O(d(n + k))$ | $O(d(n + k))$ | $O(d(n + k))$ | $O(n + k)$ | ✅ | Non-comparison |
| Bucket Sort | $O(n + k)$ | $O(n + k)$ | $O(n^2)$ | $O(n + k)$ | ✅ | Distribution |

Where $k$ = range of values, $d$ = number of digits.

---

## 10.3 Bubble Sort

```c
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int swapped = 0;
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
                swapped = 1;
            }
        }
        if (!swapped) break;  // Optimization: stop if no swaps
    }
}
```

**Key facts:**
- After $i$-th pass, the $i$-th largest element is in its final position
- Minimum passes to detect sorted array: **1** (with `swapped` flag)
- Number of swaps = number of **inversions** in the array

### What is an Inversion?

A pair $(i, j)$ where $i < j$ but $arr[i] > arr[j]$.

**Maximum inversions** (reverse sorted): $\frac{n(n-1)}{2}$

**Bubble sort swaps = inversions.** This is true for any adjacent-swap-based sort.

---

## 10.4 Selection Sort

```c
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++)
            if (arr[j] < arr[minIdx])
                minIdx = j;
        swap(&arr[i], &arr[minIdx]);
    }
}
```

**Key facts:**
- Always makes exactly $\frac{n(n-1)}{2}$ comparisons (regardless of input)
- Number of swaps: at most $n - 1$ (one per pass)
- **NOT stable** — can change relative order of equal elements

**Why not stable?** Example: `[5a, 5b, 2]`. First pass swaps `5a` with `2` → `[2, 5b, 5a]`. Order of equal 5s changed.

---

## 10.5 Insertion Sort

```c
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
```

**Key facts:**
- **Best for nearly sorted data**: $O(n)$ when array is already sorted or has few inversions
- **Best for small arrays**: used as subroutine in optimized quicksort/mergesort
- **Online algorithm**: can sort as elements arrive
- Comparisons = inversions + $(n - 1)$
- **Stable** — equal elements maintain relative order

### 🔴 GATE Trap: Insertion Sort Comparisons

"How many comparisons does insertion sort make on `[3, 1, 2, 5, 4]`?"

```
Pass 1: Insert 1. Compare with 3. Shift 3. Place 1. [1,3,2,5,4] — 1 comparison
Pass 2: Insert 2. Compare with 3. Shift 3. Compare with 1. Place 2. [1,2,3,5,4] — 2 comparisons
Pass 3: Insert 5. Compare with 3. In place. [1,2,3,5,4] — 1 comparison
Pass 4: Insert 4. Compare with 5. Shift 5. Compare with 3. Place 4. [1,2,3,4,5] — 2 comparisons
Total: 1 + 2 + 1 + 2 = 6 comparisons
```

---

## 10.6 Merge Sort

```c
void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1, n2 = r - m;
    int L[n1], R[n2];
    
    for (int i = 0; i < n1; i++) L[i] = arr[l + i];
    for (int j = 0; j < n2; j++) R[j] = arr[m + 1 + j];
    
    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j])     // <= makes it stable
            arr[k++] = L[i++];
        else
            arr[k++] = R[j++];
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSort(int arr[], int l, int r) {
    if (l >= r) return;
    int m = l + (r - l) / 2;
    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);
    merge(arr, l, m, r);
}
```

**Recurrence:** $T(n) = 2T(n/2) + \Theta(n) = \Theta(n \log n)$

**Key facts:**
- **Always** $O(n \log n)$ — best, average, and worst
- Requires $O(n)$ extra space (auxiliary array)
- **Stable**
- Preferred for **linked lists** (no random access needed, $O(1)$ extra space)

### Number of Comparisons in Merge Sort

**Minimum comparisons** to merge two arrays of size $m$ and $n$: $\min(m, n)$ (one array exhausted immediately)

**Maximum comparisons:** $m + n - 1$ (interleaved elements)

**Total comparisons for merge sort of $n$ elements:**
- Best: $\frac{n}{2} \log_2 n$ (approximately)
- Worst: $n \log_2 n - n + 1$

---

## 10.7 Quick Sort

```c
int partition(int arr[], int low, int high) {
    int pivot = arr[high];  // Last element as pivot
    int i = low - 1;
    
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
```

### Complexity Analysis

**Best/Average case:** Pivot divides array roughly in half.

$$T(n) = 2T(n/2) + \Theta(n) = \Theta(n \log n)$$

**Worst case:** Pivot is always min or max (sorted/reverse-sorted input with first/last element pivot).

$$T(n) = T(n-1) + \Theta(n) = \Theta(n^2)$$

### Randomized Quick Sort

Choose pivot **randomly** → expected time $O(n \log n)$ regardless of input.

### 🔴 GATE Trap: Quick Sort Comparisons

"How many comparisons does Quick Sort make in the worst case with $n$ elements?"

Worst case: $n-1 + n-2 + \ldots + 1 = \frac{n(n-1)}{2}$

"What input causes worst case with last-element pivot?"

**Already sorted array.** Pivot = last element = maximum. Partitions into $n-1$ and $0$ elements.

### Quick Sort vs Merge Sort

| Aspect | Quick Sort | Merge Sort |
|--------|-----------|------------|
| Average time | $O(n \log n)$ | $O(n \log n)$ |
| Worst time | $O(n^2)$ | $O(n \log n)$ |
| Extra space | $O(\log n)$ stack | $O(n)$ |
| Stable | ❌ | ✅ |
| Cache performance | ✅ (in-place, good locality) | ❌ |
| In practice | Faster (smaller constants) | Guaranteed performance |

---

## 10.8 Heap Sort

(Covered in Trees chapter. Key recap here.)

```c
void heapSort(int arr[], int n) {
    // Build max-heap: O(n)
    for (int i = n/2 - 1; i >= 0; i--)
        heapify(arr, n, i);
    
    // Extract elements: O(n log n)
    for (int i = n-1; i > 0; i--) {
        swap(&arr[0], &arr[i]);
        heapify(arr, i, 0);
    }
}
```

**Key facts:**
- $O(n \log n)$ in ALL cases
- In-place ($O(1)$ extra space)
- **NOT stable**
- Slower in practice than Quick Sort (poor cache performance)

---

## 10.9 Counting Sort — $O(n + k)$

**Non-comparison based.** Works when range of values $k$ is not significantly larger than $n$.

```c
void countingSort(int arr[], int n) {
    int max = findMax(arr, n);
    int count[max + 1];
    memset(count, 0, sizeof(count));
    
    // Count occurrences
    for (int i = 0; i < n; i++)
        count[arr[i]]++;
    
    // Cumulative count (for stability)
    for (int i = 1; i <= max; i++)
        count[i] += count[i - 1];
    
    // Build output (traverse input in reverse for stability)
    int output[n];
    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }
    
    // Copy back
    for (int i = 0; i < n; i++)
        arr[i] = output[i];
}
```

**When to use:** Elements are integers in a known, small range.

**Stable:** Yes (with the reverse-traversal technique).

---

## 10.10 Radix Sort — $O(d(n + k))$

Sorts digit by digit, from **least significant to most significant**, using a **stable** sub-sort (typically counting sort).

```
Input:  170, 045, 075, 090, 002, 024, 802, 066

Sort by ones digit:  170, 090, 002, 802, 024, 045, 075, 066
Sort by tens digit:  002, 802, 024, 045, 066, 170, 075, 090
Sort by hundreds:    002, 024, 045, 066, 075, 090, 170, 802
```

**Why LSD (Least Significant Digit) first?** Because each pass uses a **stable** sort, earlier digits' ordering is preserved when later digits are equal.

**Time:** $O(d \times (n + k))$ where $d$ = digits, $k$ = base (10 for decimal).

---

## 10.11 Bucket Sort — $O(n)$ Average

1. Divide range into $n$ buckets
2. Distribute elements into buckets
3. Sort each bucket (using insertion sort)
4. Concatenate

**Best for:** Uniformly distributed floating-point numbers in $[0, 1)$.

**Average:** $O(n)$ (if distribution is uniform).  
**Worst:** $O(n^2)$ (all elements in one bucket).

---

## 10.12 Comparison-Based Sorting Lower Bound

### The $\Omega(n \log n)$ Proof

Any comparison-based sorting algorithm can be modeled as a **decision tree**.

- Each internal node = one comparison
- Each leaf = one permutation (possible output)
- Number of leaves ≥ $n!$ (all $n!$ permutations must be reachable)

**Height of tree** = worst-case comparisons.

For a binary tree with $L$ leaves: $\text{height} \geq \lceil \log_2 L \rceil$

$$\text{Min comparisons} \geq \lceil \log_2(n!) \rceil$$

By Stirling's approximation: $\log_2(n!) = n \log_2 n - n \log_2 e + O(\log n) = \Theta(n \log n)$

$$\boxed{\text{Comparison-based sorting} = \Omega(n \log n)}$$

**This means:** No comparison-based sort can do better than $O(n \log n)$ in the worst case.

**Non-comparison sorts** (counting, radix, bucket) bypass this limit by using element properties.

---

## 10.13 Stability in Sorting

A sorting algorithm is **stable** if elements with equal keys maintain their relative order from the input.

**Stable:** Bubble, Insertion, Merge, Counting, Radix, Bucket

**Unstable:** Selection, Quick, Heap

### 🔴 GATE Trap: Making Unstable Sorts Stable

Any sort can be made stable by using the original index as a **secondary key**. But this may change the time/space complexity.

**Why is Quick Sort unstable?** The partition step can swap non-adjacent elements, disrupting relative order of equal keys.

---

## 10.14 Order Statistics — $k$-th Smallest Element

### Naive: Sort then access $O(n \log n)$

### Using Min-Heap: $O(n + k \log n)$

Build heap $O(n)$, then extract-min $k$ times $O(k \log n)$.

### QuickSelect (Randomized) — $O(n)$ Average

Partition-based, like QuickSort but only recurse on ONE side.

```c
int quickSelect(int arr[], int low, int high, int k) {
    if (low == high) return arr[low];
    
    int pi = partition(arr, low, high);
    
    if (pi == k)
        return arr[pi];
    else if (pi > k)
        return quickSelect(arr, low, pi - 1, k);
    else
        return quickSelect(arr, pi + 1, high, k);
}
```

**Average:** $O(n)$. **Worst:** $O(n^2)$.

### Median of Medians — $O(n)$ Worst Case

Guaranteed linear-time selection. Uses median of groups of 5 as pivot.

$$T(n) = T(n/5) + T(7n/10) + O(n) = O(n)$$

---

## 10.15 Inversions

An **inversion** is a pair $(i, j)$ where $i < j$ and $arr[i] > arr[j]$.

**Count inversions using modified merge sort:** $O(n \log n)$

During merge, when right element is chosen before left elements, count all remaining left elements as inversions.

---

## Summary: Quick-Fire GATE Facts for Sorting & Searching

1. Comparison-based lower bound: $\Omega(n \log n)$.
2. Binary search: $\lfloor \log_2 n \rfloor + 1$ max comparisons. Array must be sorted.
3. **Merge sort:** Always $O(n \log n)$, $O(n)$ space, stable.
4. **Quick sort:** Average $O(n \log n)$, worst $O(n^2)$, in-place, unstable. Worst case on sorted input with bad pivot.
5. **Heap sort:** Always $O(n \log n)$, in-place, unstable.
6. Counting sort: $O(n + k)$, stable, non-comparison.
7. Radix sort: $O(d(n+k))$, uses stable sub-sort, LSD first.
8. Stable sorts: Bubble, Insertion, Merge, Counting, Radix.
9. Inversions = bubble sort swaps = merge sort inversion count.
10. QuickSelect: $O(n)$ average for $k$-th smallest.
11. Insertion sort is best for nearly sorted / small arrays.
12. Selection sort: always $\frac{n(n-1)}{2}$ comparisons, max $n-1$ swaps.

---

> **5-Second Snap-Check for Sorting Questions:**
> 1. "Best sorting algorithm?" → Depends on constraints (stable? space? guaranteed?)
> 2. Counting comparisons? → Trace through the algorithm
> 3. "Can you sort in $O(n)$?" → Only with non-comparison sort + bounded range
> 4. Worst case of Quick Sort → sorted input with bad pivot choice
> 5. Stable? → "**B**ubble **I**nsertion **M**erge **C**ounting **R**adix" = **BIMCR**
