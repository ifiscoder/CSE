# Part 8: Graphs

> **The Atomic Truth:** *Graph = vertices + edges; models relationships.*

---

## 8.1 Graph Terminology

| Term | Definition |
|------|-----------|
| **Graph** $G = (V, E)$ | Set of vertices $V$ and edges $E$ |
| **Directed graph (digraph)** | Edges have direction: $(u, v) \neq (v, u)$ |
| **Undirected graph** | Edges are unordered: $\{u, v\} = \{v, u\}$ |
| **Weighted graph** | Edges have associated weights/costs |
| **Degree** | Number of edges incident to a vertex |
| **In-degree** | (Directed) Number of incoming edges |
| **Out-degree** | (Directed) Number of outgoing edges |
| **Path** | Sequence of vertices connected by edges |
| **Cycle** | Path that starts and ends at the same vertex |
| **Connected graph** | Path exists between every pair of vertices (undirected) |
| **Strongly connected** | Path exists between every pair in both directions (directed) |
| **Complete graph** $K_n$ | Edge between every pair of vertices |

### Key Formulas

**Handshaking Theorem (Undirected):**

$$\sum_{v \in V} \deg(v) = 2|E|$$

**Why?** Each edge contributes 1 to the degree of each of its two endpoints.

**Consequence:** Sum of degrees is always even → number of odd-degree vertices is even.

**For directed graphs:**

$$\sum_{v \in V} \text{in-deg}(v) = \sum_{v \in V} \text{out-deg}(v) = |E|$$

**Complete graph edges:**
$$|E(K_n)| = \binom{n}{2} = \frac{n(n-1)}{2}$$

**Maximum edges in directed graph:** $n(n-1)$ (with self-loops: $n^2$)

**Maximum edges in simple undirected graph:** $\frac{n(n-1)}{2}$

---

## 8.2 Graph Representations

### Adjacency Matrix

A $|V| \times |V|$ matrix where $M[i][j] = 1$ if edge $(i, j)$ exists.

```
Graph:  0 — 1       Adjacency Matrix:
        |   |         0  1  2  3
        3 — 2       0 [0  1  0  1]
                    1 [1  0  1  0]
                    2 [0  1  0  1]
                    3 [1  0  1  0]
```

| Aspect | Value |
|--------|-------|
| Space | $O(V^2)$ |
| Check edge existence | $O(1)$ |
| Find all neighbors | $O(V)$ |
| Add edge | $O(1)$ |
| Best for | Dense graphs ($E \approx V^2$) |

### Adjacency List

Array of linked lists (or dynamic arrays). Each vertex stores a list of its neighbors.

```
0 → [1, 3]
1 → [0, 2]
2 → [1, 3]
3 → [0, 2]
```

| Aspect | Value |
|--------|-------|
| Space | $O(V + E)$ |
| Check edge existence | $O(\text{degree})$ |
| Find all neighbors | $O(\text{degree})$ |
| Add edge | $O(1)$ |
| Best for | Sparse graphs ($E \ll V^2$) |

### 🔴 GATE Trap: Space Comparison

For an undirected graph with adjacency list: each edge is stored **twice** (once for each endpoint). Total space for edges = $2|E|$ entries in the lists.

For a directed graph: each edge stored **once**. Total space for edges = $|E|$.

---

## 8.3 Breadth-First Search (BFS)

Explores all vertices at distance $d$ before distance $d+1$. Uses a **queue**.

```c
void BFS(int adj[][MAX], int V, int start) {
    int visited[MAX] = {0};
    Queue q;
    init(&q);
    
    visited[start] = 1;
    enqueue(&q, start);
    
    while (!isEmpty(&q)) {
        int v = dequeue(&q);
        printf("%d ", v);
        
        for (int u = 0; u < V; u++) {
            if (adj[v][u] && !visited[u]) {
                visited[u] = 1;
                enqueue(&q, u);
            }
        }
    }
}
```

### BFS Properties

| Property | Value |
|----------|-------|
| Time (adj. matrix) | $O(V^2)$ |
| Time (adj. list) | $O(V + E)$ |
| Space | $O(V)$ |
| Shortest path (unweighted) | ✅ Yes |
| Works for disconnected? | Need to run from all unvisited vertices |

**Why BFS finds shortest paths (unweighted)?** It processes vertices in order of their distance from the source. When a vertex is first discovered, it's via the shortest path.

---

## 8.4 Depth-First Search (DFS)

Explores as deep as possible along each branch. Uses a **stack** (or recursion).

```c
void DFS(int adj[][MAX], int V, int start, int visited[]) {
    visited[start] = 1;
    printf("%d ", start);
    
    for (int u = 0; u < V; u++) {
        if (adj[start][u] && !visited[u])
            DFS(adj, V, u, visited);
    }
}
```

### DFS Properties

| Property | Value |
|----------|-------|
| Time (adj. matrix) | $O(V^2)$ |
| Time (adj. list) | $O(V + E)$ |
| Space | $O(V)$ (recursion stack) |
| Shortest path | ❌ No |
| Cycle detection | ✅ Yes |

### DFS Edge Classification (Directed Graphs)

During DFS, edges are classified based on discovery/finish times:

| Edge Type | Definition | Indicates |
|-----------|-----------|-----------|
| **Tree edge** | Edge to undiscovered vertex | Part of DFS tree |
| **Back edge** | Edge to ancestor in DFS tree | **Cycle exists** |
| **Forward edge** | Edge to descendant (not tree edge) | Shortcut to descendant |
| **Cross edge** | Edge to neither ancestor nor descendant | Between different branches |

**Key fact:** A directed graph has a cycle ↔ DFS finds a **back edge**.

**For undirected graphs:** Only tree edges and back edges exist. A back edge = cycle.

### 🔴 GATE Trap: BFS vs DFS for Applications

| Application | Use BFS? | Use DFS? |
|------------|---------|---------|
| Shortest path (unweighted) | ✅ | ❌ |
| Cycle detection | ✅ | ✅ |
| Topological sort | ❌ | ✅ |
| Connected components | ✅ | ✅ |
| Bipartiteness check | ✅ | ✅ |
| Finding bridges/articulation points | ❌ | ✅ |
| Strongly connected components | ❌ | ✅ |

---

## 8.5 Topological Sort

A **linear ordering** of vertices such that for every directed edge $(u, v)$, $u$ comes before $v$.

**Exists only for DAGs** (Directed Acyclic Graphs).

### DFS-Based (Reverse Post-Order)

```c
void topoDFS(int adj[][MAX], int V, int v, int visited[], Stack *s) {
    visited[v] = 1;
    for (int u = 0; u < V; u++)
        if (adj[v][u] && !visited[u])
            topoDFS(adj, V, u, visited, s);
    push(s, v);  // Push AFTER all descendants processed
}

void topologicalSort(int adj[][MAX], int V) {
    int visited[MAX] = {0};
    Stack s;
    init(&s);
    
    for (int i = 0; i < V; i++)
        if (!visited[i])
            topoDFS(adj, V, i, visited, &s);
    
    while (!isEmpty(&s))
        printf("%d ", pop(&s));
}
```

### Kahn's Algorithm (BFS-Based)

```c
void kahnTopSort(int adj[][MAX], int V) {
    int inDegree[MAX] = {0};
    Queue q;
    init(&q);
    
    // Calculate in-degrees
    for (int i = 0; i < V; i++)
        for (int j = 0; j < V; j++)
            if (adj[i][j]) inDegree[j]++;
    
    // Enqueue vertices with in-degree 0
    for (int i = 0; i < V; i++)
        if (inDegree[i] == 0) enqueue(&q, i);
    
    int count = 0;
    while (!isEmpty(&q)) {
        int v = dequeue(&q);
        printf("%d ", v);
        count++;
        
        for (int u = 0; u < V; u++) {
            if (adj[v][u]) {
                inDegree[u]--;
                if (inDegree[u] == 0)
                    enqueue(&q, u);
            }
        }
    }
    
    if (count != V) printf("Cycle exists!");
}
```

**Bonus:** Kahn's algorithm also detects cycles (if count ≠ V).

**Number of possible topological orderings** depends on the DAG structure. Multiple valid orderings may exist.

---

## 8.6 Minimum Spanning Tree (MST)

A spanning tree with the **minimum total edge weight** that connects all vertices.

### Kruskal's Algorithm (Greedy — Edge-based)

1. Sort all edges by weight
2. Pick the smallest edge. If it doesn't form a cycle, include it
3. Repeat until $V - 1$ edges are included

**Cycle detection:** Use **Union-Find (Disjoint Set Union)**.

**Time:** $O(E \log E)$ — dominated by sorting. With Union-Find path compression: nearly $O(E \log E)$.

### Prim's Algorithm (Greedy — Vertex-based)

1. Start from any vertex
2. Always add the **minimum weight edge** connecting a visited vertex to an unvisited one
3. Repeat until all vertices are visited

**Time:**
- With adjacency matrix: $O(V^2)$
- With binary heap + adjacency list: $O(E \log V)$
- With Fibonacci heap: $O(E + V \log V)$

### When to Use Which?

| Algorithm | Better for |
|----------|-----------|
| Kruskal's | Sparse graphs ($E \ll V^2$) |
| Prim's (matrix) | Dense graphs ($E \approx V^2$) |

### MST Properties

1. **Cut Property:** The minimum weight edge crossing any cut must be in the MST.
2. **Cycle Property:** The maximum weight edge in any cycle is NOT in the MST.
3. A graph may have **multiple MSTs** (when equal-weight edges exist), but the total weight is unique.
4. Number of edges in MST = $V - 1$.
5. If all edge weights are distinct, MST is **unique**.

---

## 8.7 Shortest Path Algorithms

### Dijkstra's Algorithm (Single Source, Non-negative Weights)

Finds shortest path from source to all vertices.

**Time:**
- With adjacency matrix: $O(V^2)$
- With binary heap: $O((V + E) \log V)$

**Does NOT work with negative edges.**

### Bellman-Ford Algorithm (Single Source, Handles Negative Weights)

Relaxes all edges $V - 1$ times.

**Time:** $O(VE)$

**Can detect negative weight cycles** (if any distance decreases in the $V$-th iteration).

### Floyd-Warshall Algorithm (All Pairs)

Dynamic programming approach. Considers all vertices as intermediate vertices.

```c
for (int k = 0; k < V; k++)
    for (int i = 0; i < V; i++)
        for (int j = 0; j < V; j++)
            if (dist[i][k] + dist[k][j] < dist[i][j])
                dist[i][j] = dist[i][k] + dist[k][j];
```

**Time:** $O(V^3)$, **Space:** $O(V^2)$

**Negative cycle detection:** If `dist[i][i] < 0` for any $i$.

### Comparison

| Algorithm | Type | Negative Weights | Time |
|-----------|------|-----------------|------|
| Dijkstra | Single source | ❌ | $O(V^2)$ or $O((V+E)\log V)$ |
| Bellman-Ford | Single source | ✅ (detects neg. cycles) | $O(VE)$ |
| Floyd-Warshall | All pairs | ✅ (detects neg. cycles) | $O(V^3)$ |
| BFS | Single source (unweighted) | N/A | $O(V + E)$ |

### 🔴 GATE Trap: Dijkstra with Negative Edges

```
A → B (weight 1)
A → C (weight 5)
B → C (weight -10)
```

Dijkstra would finalize C's distance through A as 5, missing the shorter path A→B→C = 1 + (-10) = -9. **Dijkstra fails with negative edges** because it assumes finalized distances won't decrease.

---

## 8.8 Graph Properties & Special Graphs

### Bipartite Graph

A graph whose vertices can be divided into two disjoint sets such that every edge connects a vertex in one set to a vertex in the other.

**Test:** A graph is bipartite ↔ it has **no odd-length cycle** ↔ BFS 2-coloring succeeds.

### Euler Path/Circuit

- **Euler path:** visits every **edge** exactly once
- **Euler circuit:** Euler path that returns to starting vertex

| Graph Type | Euler Path Exists | Euler Circuit Exists |
|-----------|-------------------|---------------------|
| Undirected | Exactly 0 or 2 odd-degree vertices | All vertices have even degree |
| Directed | At most 1 vertex with out-in=1, at most 1 with in-out=1 | in-degree = out-degree for all |

### Hamiltonian Path/Circuit

- **Hamiltonian path:** visits every **vertex** exactly once
- **Hamiltonian circuit:** Hamiltonian path returning to start

**No efficient algorithm** (NP-complete).

### Connected Components

- **Undirected:** Run BFS/DFS from unvisited vertices. Each run = one component.
- **Directed (strongly connected):** Use **Kosaraju's** or **Tarjan's** algorithm. Both $O(V + E)$.

---

## 8.9 Important Graph Counting Formulas

| Property | Formula |
|----------|---------|
| Max edges in simple undirected graph | $\frac{n(n-1)}{2}$ |
| Max edges in simple directed graph | $n(n-1)$ |
| Edges in complete bipartite $K_{m,n}$ | $m \times n$ |
| Number of spanning trees of $K_n$ | $n^{n-2}$ (Cayley's formula) |
| Edges in a tree | $n - 1$ |
| Min edges to connect $n$ vertices | $n - 1$ (tree) |
| Min edges to make complete graph | $\frac{n(n-1)}{2}$ |

---

## Summary: Quick-Fire GATE Facts for Graphs

1. Handshaking: $\sum \deg = 2|E|$.
2. BFS = Queue + shortest path (unweighted). DFS = Stack + cycle detection.
3. Time: $O(V + E)$ with adjacency list for both BFS and DFS.
4. Back edge in DFS → **cycle**.
5. Topological sort: only for DAGs. DFS (reverse post-order) or Kahn's (BFS with in-degree).
6. MST edges = $V - 1$. Kruskal: sort edges. Prim: grow from vertex.
7. Dijkstra: no negative edges. Bellman-Ford: handles negatives.
8. Floyd-Warshall: all pairs, $O(V^3)$.
9. Bipartite ↔ no odd cycle ↔ 2-colorable.
10. Euler circuit: all even degrees (undirected).
11. Spanning trees of $K_n = n^{n-2}$.

---

> **5-Second Snap-Check for Graph Questions:**
> 1. Shortest path? → Unweighted = BFS, Non-negative = Dijkstra, Negative = Bellman-Ford, All pairs = Floyd-Warshall
> 2. MST? → Kruskal (sparse), Prim (dense)
> 3. Topological sort? → Must be DAG
> 4. Cycle? → Back edge in DFS
> 5. Euler? → Check degree conditions
