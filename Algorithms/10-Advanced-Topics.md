# Module 10: Advanced Topics & NP-Completeness

## 🎯 The Atomic Truth
> **"Some problems are computationally hard—recognize and handle them"**

---

## 🧠 Mental Model: The Computational Zoo

[Image: Zoo with different complexity classes as enclosures]

- **P Zoo:** Problems solved quickly (polynomial time)
- **NP Zoo:** Solutions verified quickly (polynomial time)
- **NP-Complete:** Hardest in NP—if one is easy, all are
- **NP-Hard:** At least as hard as NP-Complete

---

## 📐 1. Complexity Classes

### 1.1 Class P

**Definition:** Problems solvable in polynomial time by a deterministic Turing machine.

$$P = \bigcup_{k \geq 1} \text{TIME}(n^k)$$

**Examples:**
- Sorting: O(n log n)
- Shortest path: O(V² or E log V)
- Maximum matching: O(V³)
- Primality testing: O(log⁶ n)

### 1.2 Class NP

**Definition:** Problems whose solutions can be **verified** in polynomial time.

**Equivalently:** Problems solvable in polynomial time by a **non-deterministic** Turing machine.

**Examples:**
- SAT (Boolean Satisfiability)
- Hamiltonian Cycle
- Graph Coloring
- Subset Sum

### 1.3 P vs NP

**The Million Dollar Question:** Is P = NP?

```
If P = NP:
- Every problem with quickly verifiable solution is quickly solvable
- Cryptography breaks
- Optimization becomes easy

Current belief: P ≠ NP (unproven)
```

### 1.4 Class NP-Complete

**Definition:** A problem X is NP-Complete if:
1. X ∈ NP (solutions verifiable in polynomial time)
2. Every problem in NP can be reduced to X in polynomial time

**Significance:** If ANY NP-Complete problem has polynomial solution, then P = NP.

### 1.5 Class NP-Hard

**Definition:** Problems at least as hard as NP-Complete, but not necessarily in NP.

**Examples:**
- Halting Problem (undecidable, not in NP)
- Optimization versions of NP-Complete problems

### 1.6 Relationship Diagram

```
┌─────────────────────────────────────┐
│              NP-Hard                │
│  ┌───────────────────────────────┐  │
│  │           NP                  │  │
│  │  ┌─────────────────────────┐  │  │
│  │  │     NP-Complete         │  │  │
│  │  │  ┌───────────────────┐  │  │  │
│  │  │  │        P          │  │  │  │
│  │  │  │                   │  │  │  │
│  │  │  └───────────────────┘  │  │  │
│  │  └─────────────────────────┘  │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
(Assuming P ≠ NP)
```

---

## 🔄 2. Polynomial-Time Reductions

### 2.1 Definition

Problem A reduces to problem B (A ≤ₚ B) if:
- There exists a polynomial-time function f such that
- x ∈ A ⟺ f(x) ∈ B

**Meaning:** If we can solve B, we can solve A.

### 2.2 Reduction Properties

1. If A ≤ₚ B and B ∈ P, then A ∈ P
2. If A ≤ₚ B and A is NP-Complete, then B is NP-Hard
3. Transitivity: If A ≤ₚ B and B ≤ₚ C, then A ≤ₚ C

### 2.3 Proving NP-Completeness

To prove problem X is NP-Complete:
1. Show X ∈ NP (give polynomial verifier)
2. Show known NP-Complete problem Y ≤ₚ X

---

## 📚 3. Classic NP-Complete Problems

### 3.1 SAT (Boolean Satisfiability)

**Problem:** Given boolean formula, is there an assignment that makes it TRUE?

**Cook-Levin Theorem (1971):** SAT is NP-Complete (the first one!)

### 3.2 3-SAT

**Problem:** SAT where each clause has exactly 3 literals.

**Example:**
$$(\bar{x}_1 \vee x_2 \vee x_3) \wedge (x_1 \vee \bar{x}_2 \vee x_4) \wedge ...$$

**Reduction:** SAT ≤ₚ 3-SAT

### 3.3 Clique

**Problem:** Does graph G have a clique of size k?

**Clique:** Complete subgraph (every pair connected).

**Reduction:** 3-SAT ≤ₚ Clique

### 3.4 Vertex Cover

**Problem:** Is there a set of k vertices that covers all edges?

**Reduction:** Clique ≤ₚ Vertex Cover

**Key:** G has clique of size k ⟺ Ḡ (complement) has vertex cover of size n-k

### 3.5 Independent Set

**Problem:** Is there a set of k vertices with no edges between them?

**Relation:** Independent set in G ⟺ Clique in Ḡ

### 3.6 Hamiltonian Cycle

**Problem:** Does graph have a cycle visiting each vertex exactly once?

**Reduction:** 3-SAT ≤ₚ Hamiltonian Cycle (complex gadget construction)

### 3.7 Traveling Salesman (TSP)

**Problem:** Find shortest tour visiting all cities exactly once.

**Decision version:** Is there a tour of length ≤ k?

**Reduction:** Hamiltonian Cycle ≤ₚ TSP

### 3.8 Graph Coloring

**Problem:** Can graph be colored with k colors such that no adjacent vertices share a color?

**Note:** 2-coloring is in P (bipartiteness check), but k-coloring for k ≥ 3 is NP-Complete.

### 3.9 Subset Sum

**Problem:** Given set S and target T, is there a subset summing to T?

**Reduction:** 3-SAT ≤ₚ Subset Sum

### 3.10 Partition Problem

**Problem:** Can set S be partitioned into two subsets with equal sum?

**Reduction:** Subset Sum ≤ₚ Partition

### 3.11 0/1 Knapsack (Decision)

**Problem:** Can we achieve value ≥ V with weight ≤ W?

**Note:** Optimization is NP-Hard, decision is NP-Complete.

---

## 🔗 4. Reduction Examples

### 4.1 Independent Set to Clique

**Reduction:** G has IS of size k ⟺ Ḡ has Clique of size k

```python
def independent_set_to_clique(G, k):
    # Construct complement graph
    G_complement = complement_graph(G)
    return has_clique(G_complement, k)
```

### 4.2 Vertex Cover to Independent Set

**Relation:** S is vertex cover ⟺ V - S is independent set

If G has n vertices:
- G has VC of size k ⟺ G has IS of size n-k

### 4.3 3-SAT to Clique

**Construction:**
1. For formula with m clauses, create 3m nodes (one per literal per clause)
2. Connect nodes if:
   - From different clauses AND
   - Not complementary (xᵢ and x̄ᵢ not connected)
3. Formula is satisfiable ⟺ Graph has clique of size m

### 4.4 Hamiltonian Cycle to TSP

**Reduction:**
1. Given graph G, create complete graph with distances:
   - d(u,v) = 1 if edge (u,v) exists in G
   - d(u,v) = 2 otherwise
2. G has Hamiltonian Cycle ⟺ TSP has tour of length n

---

## ⚙️ 5. Approximation Algorithms

### 5.1 Concept

Since NP-Hard problems can't be solved optimally in polynomial time (unless P=NP), we settle for **approximate** solutions.

**Approximation Ratio:**
$$\rho = \frac{\text{Approximate Solution}}{\text{Optimal Solution}}$$

For minimization: ρ ≥ 1
For maximization: ρ ≤ 1

### 5.2 Vertex Cover: 2-Approximation

```python
def vertex_cover_approx(graph):
    cover = set()
    edges = list(graph.edges())
    
    while edges:
        u, v = edges.pop()
        cover.add(u)
        cover.add(v)
        
        # Remove edges covered by u or v
        edges = [(a, b) for (a, b) in edges if a not in {u, v} and b not in {u, v}]
    
    return cover
```

**Guarantee:** Returns cover at most 2× optimal size.

**Proof:** Each edge picked contributes 2 vertices. Optimal must have at least 1 vertex per picked edge.

### 5.3 TSP: Christofides' Algorithm

For metric TSP (triangle inequality): 1.5-approximation

1. Find MST
2. Find minimum weight matching on odd-degree vertices
3. Find Eulerian circuit
4. Shortcut to get Hamiltonian cycle

### 5.4 Knapsack: FPTAS

**Fully Polynomial-Time Approximation Scheme (FPTAS):**

For any ε > 0, find solution within (1-ε) of optimal in time O(n/ε).

```python
def knapsack_fptas(weights, values, capacity, epsilon):
    n = len(values)
    max_val = max(values)
    
    # Scale values
    k = epsilon * max_val / n
    scaled_values = [int(v / k) for v in values]
    
    # Solve with scaled values (smaller range)
    # ... DP solution ...
    
    return result
```

### 5.5 Set Cover: Greedy

**Greedy:** Repeatedly pick set covering most uncovered elements.

**Approximation ratio:** O(log n)

---

## 🎲 6. Randomized Algorithms

### 6.1 Las Vegas Algorithms

- Always correct
- Running time is random
- Example: Randomized QuickSort

### 6.2 Monte Carlo Algorithms

- Running time is fixed
- Answer may be incorrect with small probability
- Example: Miller-Rabin primality test

### 6.3 Randomized QuickSort

```python
import random

def randomized_quicksort(arr, low, high):
    if low < high:
        # Random pivot selection
        pivot_idx = random.randint(low, high)
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
        
        p = partition(arr, low, high)
        randomized_quicksort(arr, low, p - 1)
        randomized_quicksort(arr, p + 1, high)
```

**Expected complexity:** O(n log n)

### 6.4 Randomized Min-Cut (Karger's Algorithm)

```python
def karger_min_cut(graph):
    while num_vertices(graph) > 2:
        # Pick random edge
        u, v = random_edge(graph)
        # Contract edge
        merge_vertices(graph, u, v)
    
    return count_edges_between_remaining_vertices(graph)
```

**Success probability:** ≥ 2/n²
**Running with n²log(n) repetitions:** High probability of finding min-cut

---

## 🏃 7. Parameterized Complexity

### 7.1 Fixed-Parameter Tractability (FPT)

Problem is FPT if solvable in time O(f(k) · n^c) where:
- k is a parameter (not input size)
- c is a constant
- f is any function of k

### 7.2 Examples

**Vertex Cover (parameterized by solution size k):**
- Brute force: O(n^k)
- FPT algorithm: O(2^k · n)

```python
def vertex_cover_fpt(graph, k):
    if k < 0:
        return False
    if no_edges(graph):
        return True
    
    # Pick any edge (u, v)
    u, v = pick_edge(graph)
    
    # Either u or v must be in cover
    return (vertex_cover_fpt(graph - u, k - 1) or
            vertex_cover_fpt(graph - v, k - 1))
```

### 7.3 Kernelization

Reduce problem to equivalent instance of size bounded by function of k.

**Vertex Cover Kernelization:**
- Remove isolated vertices
- If vertex v has degree > k, v must be in cover
- Resulting kernel has ≤ k² edges

---

## 📊 8. Amortized Analysis Revisited

### 8.1 Dynamic Array

| Operation | Worst Case | Amortized |
|-----------|------------|-----------|
| Insert | O(n) | O(1) |
| Delete | O(n) | O(1) |

### 8.2 Splay Trees

Self-adjusting BST with O(log n) amortized operations.

**Key Property:** Recently accessed elements are near root.

### 8.3 Fibonacci Heaps

| Operation | Binary Heap | Fibonacci Heap (Amortized) |
|-----------|-------------|---------------------------|
| Insert | O(log n) | O(1) |
| Find-min | O(1) | O(1) |
| Delete-min | O(log n) | O(log n) |
| Decrease-key | O(log n) | O(1) |
| Merge | O(n) | O(1) |

---

## 🔧 9. Advanced Data Structures

### 9.1 Union-Find with Path Compression

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
```

**Amortized complexity:** O(α(n)) per operation, where α is inverse Ackermann function (practically constant).

### 9.2 Segment Trees

```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return (self.query(2 * node + 1, start, mid, l, r) +
                self.query(2 * node + 2, mid + 1, end, l, r))
    
    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(2 * node + 1, start, mid, idx, val)
            else:
                self.update(2 * node + 2, mid + 1, end, idx, val)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
```

**Complexity:** O(log n) for query and update

### 9.3 Fenwick Tree (Binary Indexed Tree)

```python
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)  # Add last set bit
    
    def prefix_sum(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)  # Remove last set bit
        return total
    
    def range_sum(self, l, r):
        return self.prefix_sum(r) - self.prefix_sum(l - 1)
```

**Complexity:** O(log n) for update and query

---

## 🎓 10. GATE Pattern Problems

### Problem Type 1: Complexity Class

**Q:** Which is in P?
A. SAT
B. 2-SAT
C. 3-SAT
D. Hamiltonian Cycle

**Answer:** B (2-SAT is in P, solvable by implication graph)

---

### Problem Type 2: Reduction Direction

**Q:** If A ≤ₚ B and B ∈ P, what can we conclude?

**Answer:** A ∈ P

---

### Problem Type 3: NP-Completeness Proof

**Q:** To prove problem X is NP-Complete:

1. Show X ∈ NP (polynomial verifier)
2. Reduce known NP-Complete problem to X

---

## 🚨 11. Common GATE Traps

### Trap 1: Reduction Direction

"A ≤ₚ B" means A reduces TO B, not B to A.

If A is NP-Complete and A ≤ₚ B, then B is NP-Hard (not B reduces to A).

### Trap 2: NP vs NP-Complete

NP-Complete is a subset of NP. All problems in P are also in NP.

### Trap 3: Decision vs Optimization

Decision versions are typically NP-Complete.
Optimization versions are NP-Hard.

### Trap 4: Pseudo-Polynomial

Subset Sum has O(nS) algorithm. This is **pseudo-polynomial** (exponential in input size if S is exponential in bits).

---

## 📝 12. Practice Problems

### Problem 1 [MCQ]
Which is NOT NP-Complete?

A. Vertex Cover
B. Shortest Path
C. Graph Coloring (k≥3)
D. Clique

<details>
<summary>Solution</summary>

Shortest path is in P (Dijkstra/Bellman-Ford).

**Answer:** B
</details>

---

### Problem 2 [NAT]
If G has n vertices and a clique of size k, what size independent set does Ḡ (complement) have?

<details>
<summary>Solution</summary>

Clique in G = Independent set in Ḡ of same size.

**Answer:** k
</details>

---

### Problem 3 [MSQ]
Which are in NP?

A. Subset Sum
B. Halting Problem
C. Hamiltonian Cycle
D. Satisfiability

<details>
<summary>Solution</summary>

- A: Yes (verify by checking subset sum)
- B: No (undecidable, not in NP)
- C: Yes (verify by checking cycle)
- D: Yes (verify by checking assignment)

**Answer:** A, C, D
</details>

---

## 🧠 Memory Anchors

### Complexity Class Hierarchy

```
           NP-Hard
          /       \
         /         \
   NP-Complete    (Not in NP)
        |          Example: Halting
        |
       NP
        |
        P
```

### The Bizarre Mnemonic: "Complexity Zoo"

- **P Animals:** Easy to catch (solve quickly)
- **NP Animals:** Easy to verify if caught (check quickly)
- **NP-Complete Animals:** If you catch one easily, all are easy
- **NP-Hard Animals:** At least as hard to catch as NP-Complete

### Reduction Mnemonic: "Uphill Flow"

Reduction flows FROM easier TO harder:
- A ≤ₚ B means "A is at most as hard as B"
- Hardness flows upward in the reduction chain

### 5-Second Sanity Check

1. Can solutions be verified quickly? → NP
2. Can it be solved quickly? → P
3. Is it among the hardest in NP? → NP-Complete
4. Harder than everything in NP? → NP-Hard

---

## ⚡ Quick Reference

### NP-Complete Problems Relationships

```
       SAT
        |
      3-SAT
     /  |  \
Clique  |   Subset Sum
   |    |       |
   V.C  Ham.    Partition
   |    Cycle
   I.S    |
         TSP
```

### Key Reductions

| From | To | Key Idea |
|------|-----|----------|
| 3-SAT | Clique | Literal nodes, consistent edges |
| Clique | Vertex Cover | Complement graph |
| Clique | Independent Set | Complement graph |
| Hamiltonian | TSP | Distance 1 for edges, 2 otherwise |
| Subset Sum | Partition | Target = Total/2 |

### Approximation Ratios

| Problem | Approximation | Algorithm |
|---------|---------------|-----------|
| Vertex Cover | 2 | Maximal matching |
| TSP (metric) | 1.5 | Christofides |
| Set Cover | O(log n) | Greedy |
| Max-Cut | 0.878 | SDP relaxation |
| Knapsack | 1-ε | FPTAS |

---

## 📖 Final Exam Strategy

### Time Allocation
1. **Easy (30%):** P problems, basic reductions
2. **Medium (50%):** Complexity proofs, approximations
3. **Hard (20%):** Novel reductions, parameterized complexity

### Common Question Types
1. Identify complexity class
2. Prove NP-Completeness
3. Design approximation algorithm
4. Analyze reduction correctness

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

---

## 🎓 Course Completion

Congratulations! You have completed the comprehensive Algorithms course covering:

1. ✅ Algorithm Analysis & Complexity
2. ✅ Searching Algorithms
3. ✅ Sorting Algorithms
4. ✅ Divide and Conquer
5. ✅ Greedy Algorithms
6. ✅ Dynamic Programming
7. ✅ Graph Algorithms
8. ✅ Backtracking
9. ✅ String Algorithms
10. ✅ Advanced Topics & NP-Completeness

**You are now equipped to ace GATE, ESE, PSU, and BANK examinations!**

---

**Would you like to initiate a 'Multi-Variable Stress Test' combining multiple topics for a Rank-1 simulation?**
