# Part 9: Hashing

> **The Atomic Truth:** *Hashing = key → index mapping for $O(1)$ average access.*

---

## 9.1 The Hashing Concept

**Problem:** Given a key, find its value in $O(1)$ time.

**Solution:** Use a **hash function** $h(k)$ to map keys to array indices.

```
Key → h(key) → Index → Array[index] = Value
```

**Analogy:** A hash table is like a library where each book's shelf position is determined by a formula applied to its ISBN. No need to search — compute the position directly.

### Hash Table Components

1. **Hash function** $h: K \rightarrow \{0, 1, \ldots, m-1\}$ where $m$ = table size
2. **Array** of size $m$
3. **Collision resolution** strategy

---

## 9.2 Hash Functions

### 1. Division Method

$$h(k) = k \bmod m$$

**Best practice:** Choose $m$ as a **prime number** not close to a power of 2.

**Why prime?** A prime $m$ distributes keys more uniformly because it doesn't share factors with common patterns in key data.

**Why not power of 2?** $k \bmod 2^p$ only looks at the last $p$ bits, ignoring higher-order bits.

### 2. Multiplication Method

$$h(k) = \lfloor m \times (k \times A \bmod 1) \rfloor$$

where $0 < A < 1$. Knuth suggests $A \approx (\sqrt{5} - 1)/2 \approx 0.6180$.

**Advantage:** Choice of $m$ is not critical (works well with any $m$, even powers of 2).

### 3. Mid-Square Method

1. Square the key
2. Extract middle digits
3. Use as hash value

**Example:** Key = 4321, Square = 18671041, Middle 2 digits = 71, so $h(4321) = 71$

### 4. Folding Method

Divide key into parts, add them up.

**Example:** Key = 123456789, Fold into 3-digit parts: 123 + 456 + 789 = 1368, take last 3 digits: 368

---

## 9.3 Properties of Good Hash Functions

1. **Uniform distribution:** Keys should be spread evenly across the table
2. **Deterministic:** Same key always produces same hash
3. **Efficient:** $O(1)$ to compute
4. **Minimize collisions:** Different keys should (ideally) map to different indices

---

## 9.4 Collisions

A **collision** occurs when two distinct keys map to the same index: $h(k_1) = h(k_2)$ but $k_1 \neq k_2$.

**Pigeonhole Principle:** If $|K| > m$ (more possible keys than table slots), collisions are **inevitable**.

### Resolution Methods

Two major categories:
1. **Closed Addressing (Chaining)** — store multiple elements at same index
2. **Open Addressing** — find another slot in the table

---

## 9.5 Collision Resolution: Chaining (Separate Chaining)

Each table slot contains a **linked list** of elements that hash to that index.

```
Index 0: → [10] → [20] → NULL
Index 1: → [31] → NULL
Index 2: → [NULL]
Index 3: → [13] → [43] → [73] → NULL
...
```

### Operations

```c
void insert(HashTable *ht, int key) {
    int index = key % ht->size;
    // Insert at head of linked list at ht->table[index]
    insertFront(&ht->table[index], key);
}

int search(HashTable *ht, int key) {
    int index = key % ht->size;
    // Search linked list at ht->table[index]
    return searchList(ht->table[index], key);
}
```

### Performance Analysis

**Load factor:** $\alpha = n/m$ where $n$ = number of keys, $m$ = table size.

With chaining, $\alpha$ can be **> 1** (more elements than slots).

| Operation | Average (successful) | Average (unsuccessful) | Worst |
|-----------|---------------------|----------------------|-------|
| Search | $O(1 + \alpha/2)$ | $O(1 + \alpha)$ | $O(n)$ |
| Insert | $O(1)$ (insert at head) | — | $O(1)$ |
| Delete | $O(1 + \alpha/2)$ | $O(1 + \alpha)$ | $O(n)$ |

**Why?** Average chain length = $\alpha$. Successful search examines about half the chain on average.

---

## 9.6 Collision Resolution: Open Addressing

All elements stored in the table itself. On collision, **probe** for the next empty slot.

**General probe sequence:** $h(k, i) = (h'(k) + f(i)) \bmod m$ for $i = 0, 1, 2, \ldots$

### 1. Linear Probing

$$h(k, i) = (h'(k) + i) \bmod m$$

Check slots: $h'(k), h'(k)+1, h'(k)+2, \ldots$ (wrapping around).

**Problem: Primary Clustering** — long runs of occupied slots form, causing new insertions to cluster further.

**Expected probes (successful):** $\frac{1}{2}\left(1 + \frac{1}{1-\alpha}\right)$

**Expected probes (unsuccessful):** $\frac{1}{2}\left(1 + \frac{1}{(1-\alpha)^2}\right)$

### 2. Quadratic Probing

$$h(k, i) = (h'(k) + c_1 i + c_2 i^2) \bmod m$$

Common choice: $h(k, i) = (h'(k) + i^2) \bmod m$

Check slots: $h'(k), h'(k)+1, h'(k)+4, h'(k)+9, \ldots$

**Solves primary clustering** but causes **secondary clustering** (keys hashing to same initial slot follow same probe sequence).

**Guarantee:** If $m$ is prime and $\alpha < 0.5$, quadratic probing will find an empty slot.

### 3. Double Hashing

$$h(k, i) = (h_1(k) + i \times h_2(k)) \bmod m$$

Two different hash functions. The probe step size depends on the key itself.

**Best choice for $h_2$:** $h_2(k) = R - (k \bmod R)$ where $R$ is a prime < $m$.

**Eliminates both primary and secondary clustering.**

**Expected probes (successful):** $\frac{1}{\alpha} \ln\left(\frac{1}{1-\alpha}\right)$

**Expected probes (unsuccessful):** $\frac{1}{1-\alpha}$

### 🔴 GATE Trap: $h_2(k)$ Must Never Be 0

If $h_2(k) = 0$, the probe sequence gets stuck at the same slot. Ensure $h_2(k) \neq 0$ for all keys.

### Comparison of Probing Methods

| Method | Clustering | Probe Computation | Table Size Constraint |
|--------|-----------|-------------------|----------------------|
| Linear | Primary clustering | $O(1)$ | Any |
| Quadratic | Secondary clustering | $O(1)$ | $m$ should be prime |
| Double Hashing | No clustering | $O(1)$ (two hash functions) | $m$ should be prime, $h_2 \neq 0$ |

---

## 9.7 Open Addressing: Load Factor Constraint

In open addressing, $\alpha \leq 1$ (can't store more elements than slots).

**Practical threshold:** Keep $\alpha \leq 0.7$ for good performance.

### Performance Comparison at Various Load Factors

| $\alpha$ | Linear (unsucc.) | Quadratic (unsucc.) | Double Hash (unsucc.) | Chaining (unsucc.) |
|----------|-----------------|--------------------|-----------------------|-------------------|
| 0.5 | 2.5 probes | ~2 probes | 2 probes | 1.5 probes |
| 0.75 | 8.5 probes | ~4 probes | 4 probes | 1.75 probes |
| 0.9 | 50.5 probes | ~10 probes | 10 probes | 1.9 probes |

---

## 9.8 Deletion in Open Addressing

**Problem:** You can't simply empty a slot — it might break probe sequences for other keys.

**Solution:** Use a **DELETED marker** (tombstone). During search, skip DELETED slots. During insert, can reuse DELETED slots.

**Disadvantage:** Table degrades over time with many tombstones. Periodically rebuild.

---

## 9.9 Rehashing

When $\alpha$ exceeds a threshold:
1. Create a new larger table (typically $2 \times m$, then find next prime)
2. Re-insert all elements using the new hash function
3. Free old table

**Time:** $O(n)$ per rehashing, but **amortized $O(1)$** per insertion.

---

## 9.10 Universal Hashing

Choose hash function **randomly** from a family of hash functions at runtime.

For any two distinct keys $k_1, k_2$:

$$\Pr[h(k_1) = h(k_2)] \leq \frac{1}{m}$$

**Why?** Prevents adversarial inputs from causing worst-case behavior.

**Example family:** $h_{a,b}(k) = ((ak + b) \bmod p) \bmod m$ where $p$ is a prime ≥ |universe|.

---

## 9.11 Perfect Hashing

Achieves $O(1)$ **worst-case** lookup for a **static** set of keys.

### Cuckoo Hashing

Uses two hash functions and two tables. Each key has exactly two possible positions.

On collision: evict the existing element, which tries its alternate position. If a cycle occurs, rehash with new functions.

**Lookup:** $O(1)$ worst-case (check exactly 2 positions).  
**Insert:** $O(1)$ amortized.

---

## 9.12 GATE Problem Patterns

### Pattern 1: Finding Number of Probes

"Insert keys 10, 22, 31, 4, 15, 28, 17, 88, 59 into a hash table of size 11 using $h(k) = k \bmod 11$ with linear probing."

```
10 → h(10) = 10  → slot 10 ✓
22 → h(22) = 0   → slot 0 ✓
31 → h(31) = 9   → slot 9 ✓
4  → h(4)  = 4   → slot 4 ✓
15 → h(15) = 4   → collision → try 5 ✓
28 → h(28) = 6   → slot 6 ✓
17 → h(17) = 6   → collision → try 7 ✓
88 → h(88) = 0   → collision → try 1 ✓
59 → h(59) = 4   → collision → try 5 → 6 → 7 → 8 ✓ (4 probes)
```

### Pattern 2: Average Probes Calculation

Average successful search probes = (sum of probes for each key) / n

From above: (1+1+1+1+2+1+2+2+5)/9 = 16/9 ≈ 1.78

### Pattern 3: Load Factor Questions

"Given a hash table of size 100 with 70 elements, what is the expected number of probes for unsuccessful search with linear probing?"

$\alpha = 70/100 = 0.7$

Expected probes = $\frac{1}{2}\left(1 + \frac{1}{(1-0.7)^2}\right) = \frac{1}{2}\left(1 + \frac{1}{0.09}\right) = \frac{1}{2}(1 + 11.11) = 6.06$

---

## Summary: Quick-Fire GATE Facts for Hashing

1. Hash function maps key → index. Division method: $k \bmod m$ ($m$ = prime).
2. Load factor $\alpha = n/m$. Chaining allows $\alpha > 1$; open addressing requires $\alpha \leq 1$.
3. **Chaining:** average search = $O(1 + \alpha)$. **Open addressing:** depends on probing method.
4. Linear probing → primary clustering. Quadratic → secondary clustering. Double hashing → no clustering.
5. Open addressing deletion: use **tombstones** (DELETED markers).
6. Build heap is $O(n)$; rehashing is $O(n)$ but amortized $O(1)$ per insert.
7. $h_2(k)$ in double hashing must **never be 0**.
8. For GATE NAT: count probes carefully — every collision counts as one extra probe.
9. Average probes formula: sum of individual probes divided by number of keys.

---

> **5-Second Snap-Check for Hashing Questions:**
> 1. Open addressing or chaining? → Check the problem statement
> 2. Load factor given? → Use the appropriate expected-probes formula
> 3. Counting probes? → Simulate step by step; first probe counts as 1
> 4. Double hashing? → Verify $h_2(k) \neq 0$
