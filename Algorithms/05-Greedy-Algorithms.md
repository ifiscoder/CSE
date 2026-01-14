# Module 5: Greedy Algorithms

## 🎯 The Atomic Truth
> **"Always choose locally optimal—hope globally optimal"**

---

## 🧠 Mental Model: The Hungry Traveler

[Image: Traveler at crossroads, always picking the shortest visible path]

At each step, make the choice that **seems best right now** without worrying about future consequences.

**Key Question:** Does local optimal → global optimal?

---

## 📐 1. The Greedy Paradigm

### 1.1 General Structure

```python
def greedy_algorithm(problem):
    solution = empty_set
    
    while not is_complete(solution):
        # Select best candidate by some criterion
        best = select_best(candidates)
        
        # Check if adding it maintains feasibility
        if is_feasible(solution + best):
            solution = solution + best
        
        candidates.remove(best)
    
    return solution
```

### 1.2 Greedy Choice Property

**Definition:** A globally optimal solution can be reached by making locally optimal choices.

### 1.3 Optimal Substructure

**Definition:** An optimal solution contains optimal solutions to subproblems.

### 1.4 When Greedy Works

Greedy works when:
1. **Greedy Choice Property** holds
2. **Optimal Substructure** exists

**Proving Greedy Correctness:**
- Exchange argument: Show greedy choice can replace any other choice without worsening solution
- Stay-ahead argument: Show greedy solution stays ahead at every step

---

## 📅 2. Activity Selection Problem

### 2.1 Problem Statement
Given n activities with start times $s_i$ and finish times $f_i$, select maximum number of non-overlapping activities.

### 2.2 Greedy Strategy

**Sort by finish time, always pick earliest finishing activity.**

```python
def activity_selection(activities):
    # Sort by finish time
    activities.sort(key=lambda x: x[1])
    
    selected = [activities[0]]
    last_finish = activities[0][1]
    
    for i in range(1, len(activities)):
        if activities[i][0] >= last_finish:  # Non-overlapping
            selected.append(activities[i])
            last_finish = activities[i][1]
    
    return selected
```

### 2.3 Example

```
Activities: (1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)

Sorted by finish: (1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)

Selected: (1,4) → (5,7) → (8,11) → (12,16)
Count: 4
```

### 2.4 Correctness Proof (Exchange Argument)

Let $A$ be greedy solution, $O$ be any optimal solution.

**Claim:** We can transform $O$ to $A$ without reducing size.

**Proof:**
- Let first activity in O be $o_1$
- Greedy picks $a_1$ with earliest finish time
- Since $f(a_1) \leq f(o_1)$, replacing $o_1$ with $a_1$ in O is valid
- Continue inductively...

### 2.5 Complexity

- Sorting: O(n log n)
- Selection: O(n)
- **Total: O(n log n)**

### 2.6 🎯 GATE Trap: Other Greedy Strategies

| Strategy | Works? |
|----------|--------|
| Earliest finish time | ✅ Yes |
| Earliest start time | ❌ No (long activity blocks many) |
| Shortest duration | ❌ No (might overlap) |
| Fewest conflicts | ❌ No (counterexamples exist) |

---

## 💰 3. Fractional Knapsack

### 3.1 Problem Statement
Given items with weights $w_i$ and values $v_i$, and knapsack capacity W, maximize value. **Fractions allowed.**

### 3.2 Greedy Strategy

**Sort by value-to-weight ratio, take maximum of each.**

```python
def fractional_knapsack(items, capacity):
    # Sort by value/weight ratio (descending)
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    
    total_value = 0
    remaining = capacity
    
    for weight, value in items:
        if weight <= remaining:
            # Take whole item
            total_value += value
            remaining -= weight
        else:
            # Take fraction
            total_value += value * (remaining / weight)
            break
    
    return total_value
```

### 3.3 Example

```
Items: (weight, value) = (10, 60), (20, 100), (30, 120)
Capacity: 50

Ratios: 60/10=6, 100/20=5, 120/30=4

Take: Full item 1 (weight=10, value=60)
      Full item 2 (weight=20, value=100)
      2/3 of item 3 (weight=20, value=80)

Total: 60 + 100 + 80 = 240
```

### 3.4 Complexity

O(n log n) for sorting

### 3.5 🎯 GATE Point: Fractional vs 0/1 Knapsack

| Aspect | Fractional | 0/1 |
|--------|------------|-----|
| Items | Divisible | Indivisible |
| Approach | Greedy | Dynamic Programming |
| Complexity | O(n log n) | O(nW) |

---

## 📦 4. Huffman Coding

### 4.1 Problem Statement
Given characters with frequencies, create optimal prefix-free binary encoding minimizing total bits.

### 4.2 Prefix-Free Property

No codeword is prefix of another → Unambiguous decoding.

### 4.3 Greedy Strategy

**Repeatedly combine two lowest frequency nodes.**

```python
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(char_freq):
    # Create leaf nodes and build min-heap
    heap = [Node(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)
    
    # Combine until single tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        internal = Node(None, left.freq + right.freq)
        internal.left = left
        internal.right = right
        
        heapq.heappush(heap, internal)
    
    return heap[0]  # Root of Huffman tree

def generate_codes(root, current_code="", codes={}):
    if root is None:
        return
    
    if root.char is not None:  # Leaf node
        codes[root.char] = current_code
        return
    
    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)
    
    return codes
```

### 4.4 Example

```
Characters: a(5), b(9), c(12), d(13), e(16), f(45)

Step 1: Combine a(5) + b(9) = ab(14)
Step 2: Combine c(12) + d(13) = cd(25)
Step 3: Combine ab(14) + e(16) = abe(30)
Step 4: Combine cd(25) + abe(30) = abcde(55)
Step 5: Combine f(45) + abcde(55) = root(100)

Codes:
f: 0
c: 100
d: 101
a: 1100
b: 1101
e: 111
```

### 4.5 Properties

- More frequent characters → shorter codes
- Less frequent characters → longer codes
- **Optimal:** Minimizes $\sum f_i \cdot l_i$ (weighted path length)

### 4.6 Complexity

- Building heap: O(n)
- n-1 combinations, each O(log n)
- **Total: O(n log n)**

### 4.7 🎯 GATE Formulas

**Weighted External Path Length (WEPL):**
$$WEPL = \sum_{i=1}^{n} f_i \cdot l_i$$

where $f_i$ = frequency, $l_i$ = code length

**Average code length:**
$$L_{avg} = \frac{\sum f_i \cdot l_i}{\sum f_i}$$

---

## 🔗 5. Minimum Spanning Tree (MST)

### 5.1 Problem Statement
Given connected weighted graph, find spanning tree with minimum total edge weight.

### 5.2 Cut Property

**Theorem:** For any cut (S, V-S), the minimum weight edge crossing the cut is in some MST.

### 5.3 Kruskal's Algorithm

**Strategy:** Sort edges, add smallest edge that doesn't create cycle.

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
            return False  # Already connected
        
        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def kruskal(n, edges):
    # edges: [(weight, u, v), ...]
    edges.sort()
    uf = UnionFind(n)
    mst = []
    
    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            if len(mst) == n - 1:
                break
    
    return mst
```

### 5.4 Kruskal's Complexity

- Sort edges: O(E log E)
- Union-Find operations: O(E α(V)) ≈ O(E)
- **Total: O(E log E) = O(E log V)**

### 5.5 Prim's Algorithm

**Strategy:** Grow MST from single vertex, always add minimum weight edge to tree.

```python
import heapq

def prim(n, adj):
    # adj[u] = [(weight, v), ...]
    visited = [False] * n
    mst = []
    min_heap = [(0, 0, -1)]  # (weight, vertex, parent)
    
    while min_heap and len(mst) < n:
        weight, u, parent = heapq.heappop(min_heap)
        
        if visited[u]:
            continue
        
        visited[u] = True
        if parent != -1:
            mst.append((parent, u, weight))
        
        for w, v in adj[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))
    
    return mst
```

### 5.6 Prim's Complexity

- Binary heap: O((V + E) log V)
- Fibonacci heap: O(E + V log V)

### 5.7 Kruskal vs Prim

| Aspect | Kruskal | Prim |
|--------|---------|------|
| Best for | Sparse graphs | Dense graphs |
| Data structure | Union-Find | Priority Queue |
| Edge-centric | Yes | No |
| Works on disconnected | Yes (forest) | No |

### 5.8 🎯 GATE Insights

- MST has exactly V-1 edges
- If all edge weights distinct → unique MST
- Maximum weight edge in unique cycle → not in MST
- Minimum weight edge → always in MST

---

## 🛤️ 6. Shortest Paths

### 6.1 Dijkstra's Algorithm

**Problem:** Single source shortest paths with non-negative weights.

**Strategy:** Greedily select vertex with minimum distance.

```python
import heapq

def dijkstra(n, adj, source):
    dist = [float('inf')] * n
    dist[source] = 0
    min_heap = [(0, source)]
    
    while min_heap:
        d, u = heapq.heappop(min_heap)
        
        if d > dist[u]:
            continue  # Already found shorter path
        
        for weight, v in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(min_heap, (dist[v], v))
    
    return dist
```

### 6.2 Complexity

- Binary heap: O((V + E) log V)
- Fibonacci heap: O(E + V log V)
- Array (no heap): O(V²) — better for dense graphs

### 6.3 Why Greedy Works

Once we've found shortest path to vertex u, we won't find a shorter one (non-negative weights guarantee this).

### 6.4 🎯 GATE Trap: Negative Weights

Dijkstra **FAILS** with negative edges!

Example:
```
A --1--> B --(-2)--> C
A --2--> C

Dijkstra picks A→C (cost 2)
But A→B→C costs 1 + (-2) = -1
```

Use Bellman-Ford for negative weights.

---

## ⏰ 7. Job Scheduling Problems

### 7.1 Job Sequencing with Deadlines

**Problem:** n jobs, each with deadline $d_i$ and profit $p_i$. Each job takes 1 unit time. Maximize profit.

```python
def job_sequencing(jobs):
    # jobs: [(job_id, deadline, profit), ...]
    jobs.sort(key=lambda x: x[2], reverse=True)  # Sort by profit
    
    max_deadline = max(job[1] for job in jobs)
    slots = [-1] * (max_deadline + 1)  # Time slots
    
    total_profit = 0
    jobs_done = []
    
    for job_id, deadline, profit in jobs:
        # Find latest available slot before deadline
        for t in range(min(deadline, max_deadline), 0, -1):
            if slots[t] == -1:
                slots[t] = job_id
                total_profit += profit
                jobs_done.append(job_id)
                break
    
    return total_profit, jobs_done
```

### 7.2 Example

```
Jobs: J1(d=4, p=20), J2(d=1, p=10), J3(d=1, p=40), J4(d=1, p=30)

Sorted by profit: J3(40), J4(30), J1(20), J2(10)

Scheduling:
- J3: Slot 1 ✓ (profit = 40)
- J4: Slot 1 taken, no earlier slot ✗
- J1: Slot 4 ✓ (profit = 20)
- J2: Slot 1 taken, no earlier slot ✗

Total: 40 + 20 = 60
```

### 7.3 Complexity

- Sorting: O(n log n)
- Scheduling: O(n × max_deadline) or O(n²)
- With Union-Find: O(n log n)

### 7.4 Minimize Waiting Time

**Problem:** n jobs with service times. Minimize total waiting time.

**Strategy:** Shortest Job First (SJF)

```python
def minimize_waiting_time(jobs):
    jobs.sort()  # Sort by service time
    
    total_wait = 0
    current_time = 0
    
    for job in jobs:
        total_wait += current_time
        current_time += job
    
    return total_wait
```

**Proof:** Exchange argument shows SJF is optimal.

---

## 💵 8. Coin Change (Greedy Version)

### 8.1 Problem
Given coin denominations, find minimum coins for amount.

### 8.2 Greedy Approach

```python
def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)
    count = 0
    
    for coin in coins:
        count += amount // coin
        amount %= coin
    
    return count if amount == 0 else -1
```

### 8.3 When Greedy Works

Greedy works for **canonical coin systems:**
- Standard: {1, 5, 10, 25} ✓
- Non-canonical: {1, 3, 4} ✗

**Example:** Amount = 6, coins = {1, 3, 4}
- Greedy: 4 + 1 + 1 = 3 coins
- Optimal: 3 + 3 = 2 coins ✗

### 8.4 🎯 GATE Point

**Always check if greedy works for given denominations!**

General coin change → Dynamic Programming

---

## 📊 9. Graph Coloring (Greedy Heuristic)

### 9.1 Greedy Coloring

```python
def greedy_coloring(adj, n):
    colors = [-1] * n
    
    for u in range(n):
        # Find colors of neighbors
        neighbor_colors = set()
        for v in adj[u]:
            if colors[v] != -1:
                neighbor_colors.add(colors[v])
        
        # Assign smallest available color
        color = 0
        while color in neighbor_colors:
            color += 1
        colors[u] = color
    
    return colors, max(colors) + 1
```

### 9.2 Properties

- Greedy uses at most $\Delta + 1$ colors ($\Delta$ = max degree)
- Order of vertices matters!
- Not always optimal (NP-hard problem)

---

## 🎓 10. GATE Pattern Problems

### Problem Type 1: Activity Selection

**Q:** Activities: (1,4), (3,5), (0,6), (5,7), (6,10), (8,11). Maximum activities?

**Solution:**
Sort by finish: (1,4), (3,5), (0,6), (5,7), (6,10), (8,11)
Select: (1,4) → (5,7) → (8,11)

**Answer: 3**

---

### Problem Type 2: Huffman Coding

**Q:** Characters a, b, c, d with frequencies 1, 2, 3, 4. Total bits for encoding "abcd"?

**Solution:**
Build Huffman tree:
- Combine 1+2=3 (ab)
- Combine 3+3=6 (c+ab)
- Combine 4+6=10 (d+cab)

Codes: d=0, c=10, b=110, a=111
Total: 3+3+2+1 = 9 bits

**Answer: 9**

---

### Problem Type 3: MST

**Q:** Graph with V=5, edges with unique weights 1 to 10. If edges 1,2,3,4 form a cycle, which edge is NOT in MST?

**Solution:**
Edge with maximum weight in cycle (edge 4) is NOT in MST.

**Answer: Edge 4**

---

## 🚨 11. Common GATE Traps

### Trap 1: Assuming Greedy Works

**Always verify greedy choice property!**

Counter-example for 0/1 knapsack:
- Items: (10, 60), (20, 100), (30, 120), Capacity: 50
- Greedy (by ratio): Item 1 (60) + Item 2 (100) = 160
- Optimal: Item 2 (100) + Item 3 (120) = 220 ✗

### Trap 2: Wrong Greedy Criterion

Activity Selection: **Finish time**, not start time!

### Trap 3: Dijkstra with Negative Weights

Dijkstra fails! Use Bellman-Ford.

### Trap 4: Huffman for Equal Frequencies

If all frequencies equal, any balanced tree works.

---

## 📝 12. Practice Problems

### Problem 1 [NAT]
Fractional knapsack: Items (weight, value) = (30, 120), (10, 60), (20, 100), Capacity = 50. Maximum value?

<details>
<summary>Solution</summary>

Ratios: 120/30=4, 60/10=6, 100/20=5
Sorted: Item 2 (ratio 6), Item 3 (ratio 5), Item 1 (ratio 4)

Take: Item 2 fully (10, 60), Item 3 fully (20, 100), Item 1 partially (20/30 × 120 = 80)

Total: 60 + 100 + 80 = 240

**Answer: 240**
</details>

---

### Problem 2 [MCQ]
Which is NOT correct about Huffman coding?

A. More frequent symbols have shorter codes
B. It produces optimal prefix-free codes
C. All codes have same length for equal frequencies
D. It uses greedy approach

<details>
<summary>Solution</summary>

C is NOT necessarily true. For 4 symbols with equal frequencies, codes might be 00, 01, 10, 11 (all length 2) but tree structure can vary.

Actually, C is TRUE for power-of-2 equal frequencies. But for non-power-of-2, lengths may differ.

**Answer:** C (not always same length)
</details>

---

### Problem 3 [MSQ]
Which problems have greedy optimal solutions?

A. Fractional Knapsack
B. 0/1 Knapsack
C. Activity Selection
D. Traveling Salesman

<details>
<summary>Solution</summary>

A. TRUE - Greedy by ratio
B. FALSE - Needs DP
C. TRUE - Greedy by finish time
D. FALSE - NP-hard, no known greedy solution

**Answer:** A, C
</details>

---

## 🧠 Memory Anchors

### The Mental Slider: Greedy Validity Dial

[Image: Dial from "Greedy Fails" to "Greedy Optimal"]

Check:
1. Greedy choice property? (Local → Global)
2. Optimal substructure? (After greedy choice)
3. Counterexample exists? (If yes → use DP)

### The Bizarre Mnemonic: "Greedy Goblin"

Imagine a goblin in a treasure cave:
- **Fractional Knapsack:** Goblin cuts gold bars (works!)
- **0/1 Knapsack:** Goblin can't break gems (fails!)
- **Activity Selection:** Goblin leaves party earliest (works!)
- **Huffman:** Goblin combines smallest piles first (works!)

### 5-Second Sanity Check

1. Is the problem about optimization?
2. Can we make irrevocable choices?
3. Does choosing best now hurt us later? (If yes → not greedy)

---

## ⚡ Quick Reference

| Problem | Greedy Strategy | Complexity |
|---------|-----------------|------------|
| Activity Selection | Earliest finish time | O(n log n) |
| Fractional Knapsack | Highest value/weight ratio | O(n log n) |
| Huffman Coding | Combine lowest frequencies | O(n log n) |
| Kruskal's MST | Smallest edge, no cycle | O(E log E) |
| Prim's MST | Minimum edge to tree | O(E log V) |
| Dijkstra | Minimum distance vertex | O(E log V) |
| Job Sequencing | Highest profit first | O(n log n) |
| Minimize Wait Time | Shortest job first | O(n log n) |

---

**✅ Module Complete | Ready for GATE 2026**

**Next Module:** [Dynamic Programming →](06-Dynamic-Programming.md)
