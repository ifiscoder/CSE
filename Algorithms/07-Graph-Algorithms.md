# Module 7: Graph Algorithms

## 🎯 The Atomic Truth
> **"Vertices connected by edges—traverse, optimize, detect"**

---

## 🧠 Mental Model: City Map Navigation

[Image: Cities (vertices) connected by roads (edges)]

- **BFS:** Explore level by level (like ripples in water)
- **DFS:** Go deep, then backtrack (like a maze solver)
- **Dijkstra:** Find shortest route (GPS navigation)
- **MST:** Connect all cities with minimum road cost

---

## 📐 1. Graph Representations

### 1.1 Adjacency Matrix

```python
# For graph with n vertices
adj_matrix = [[0] * n for _ in range(n)]
# adj_matrix[i][j] = 1 if edge exists, weight if weighted
```

| Aspect | Complexity |
|--------|------------|
| Space | O(V²) |
| Check edge (u,v) | O(1) |
| Find all neighbors | O(V) |
| Add edge | O(1) |

**Best for:** Dense graphs, frequent edge queries

### 1.2 Adjacency List

```python
# Using dictionary of lists
adj_list = {v: [] for v in range(n)}
# adj_list[u].append(v) for edge u→v
# adj_list[u].append((v, weight)) for weighted
```

| Aspect | Complexity |
|--------|------------|
| Space | O(V + E) |
| Check edge (u,v) | O(degree(u)) |
| Find all neighbors | O(degree(u)) |
| Add edge | O(1) |

**Best for:** Sparse graphs, traversals

### 1.3 Edge List

```python
edges = [(u, v, weight), ...]
```

**Best for:** Kruskal's algorithm, simple storage

---

## 🌊 2. Breadth-First Search (BFS)

### 2.1 The Atomic Truth
> **"Explore all neighbors before going deeper"**

### 2.2 Algorithm

```python
from collections import deque

def bfs(adj, start):
    n = len(adj)
    visited = [False] * n
    distance = [-1] * n
    parent = [-1] * n
    
    queue = deque([start])
    visited[start] = True
    distance[start] = 0
    
    while queue:
        u = queue.popleft()
        
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u
                queue.append(v)
    
    return distance, parent
```

### 2.3 Visualization

```
Graph:       BFS from 0:
0 — 1        Level 0: [0]
|   |        Level 1: [1, 2]
2 — 3        Level 2: [3]

Order: 0 → 1 → 2 → 3
```

### 2.4 Complexity

| Metric | Complexity |
|--------|------------|
| Time | O(V + E) |
| Space | O(V) |

### 2.5 Applications

1. **Shortest path in unweighted graph**
2. **Connected components**
3. **Bipartiteness check**
4. **Level order traversal**
5. **Finding all nodes within distance k**

### 2.6 BFS for Shortest Path

```python
def shortest_path(adj, start, end):
    distance, parent = bfs(adj, start)
    
    if distance[end] == -1:
        return None  # No path
    
    # Reconstruct path
    path = []
    current = end
    while current != -1:
        path.append(current)
        current = parent[current]
    
    return path[::-1]
```

---

## 🕳️ 3. Depth-First Search (DFS)

### 3.1 The Atomic Truth
> **"Go as deep as possible, then backtrack"**

### 3.2 Recursive Implementation

```python
def dfs(adj, start):
    n = len(adj)
    visited = [False] * n
    discovery = [-1] * n
    finish = [-1] * n
    time = [0]
    
    def dfs_visit(u):
        visited[u] = True
        time[0] += 1
        discovery[u] = time[0]
        
        for v in adj[u]:
            if not visited[v]:
                dfs_visit(v)
        
        time[0] += 1
        finish[u] = time[0]
    
    dfs_visit(start)
    return discovery, finish
```

### 3.3 Iterative Implementation

```python
def dfs_iterative(adj, start):
    n = len(adj)
    visited = [False] * n
    order = []
    stack = [start]
    
    while stack:
        u = stack.pop()
        
        if not visited[u]:
            visited[u] = True
            order.append(u)
            
            for v in reversed(adj[u]):  # Reverse for same order as recursive
                if not visited[v]:
                    stack.append(v)
    
    return order
```

### 3.4 Complexity

| Metric | Complexity |
|--------|------------|
| Time | O(V + E) |
| Space | O(V) |

### 3.5 Edge Classification

During DFS, edges are classified as:

| Edge Type | Condition | Meaning |
|-----------|-----------|---------|
| **Tree edge** | v not visited | Part of DFS tree |
| **Back edge** | v is ancestor | Indicates cycle |
| **Forward edge** | v is descendant (non-tree) | Skip in undirected |
| **Cross edge** | v is neither | Between subtrees |

**🎯 GATE Point:**
- Undirected graph: Only tree edges and back edges
- Back edge exists ⟺ Cycle exists

### 3.6 Applications

1. **Cycle detection**
2. **Topological sort**
3. **Strongly connected components**
4. **Articulation points and bridges**
5. **Solving mazes**

---

## 🔄 4. Cycle Detection

### 4.1 Undirected Graph

```python
def has_cycle_undirected(adj, n):
    visited = [False] * n
    
    def dfs(u, parent):
        visited[u] = True
        
        for v in adj[u]:
            if not visited[v]:
                if dfs(v, u):
                    return True
            elif v != parent:  # Back edge found
                return True
        
        return False
    
    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                return True
    
    return False
```

### 4.2 Directed Graph

```python
def has_cycle_directed(adj, n):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    
    def dfs(u):
        color[u] = GRAY  # Being processed
        
        for v in adj[u]:
            if color[v] == GRAY:  # Back edge
                return True
            if color[v] == WHITE and dfs(v):
                return True
        
        color[u] = BLACK  # Finished
        return False
    
    for i in range(n):
        if color[i] == WHITE:
            if dfs(i):
                return True
    
    return False
```

### 4.3 🎯 GATE Insight

**Color Interpretation:**
- WHITE: Not visited
- GRAY: In current DFS path (on stack)
- BLACK: Completely processed

**Cycle exists in directed graph ⟺ Edge to GRAY vertex during DFS**

---

## 📊 5. Topological Sort

### 5.1 The Atomic Truth
> **"Order vertices so all edges go forward"**

Only possible for **DAGs** (Directed Acyclic Graphs).

### 5.2 DFS-based Algorithm

```python
def topological_sort_dfs(adj, n):
    visited = [False] * n
    stack = []
    
    def dfs(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
        stack.append(u)  # Add after all descendants
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    return stack[::-1]
```

### 5.3 Kahn's Algorithm (BFS-based)

```python
from collections import deque

def topological_sort_kahn(adj, n):
    in_degree = [0] * n
    for u in range(n):
        for v in adj[u]:
            in_degree[v] += 1
    
    queue = deque([u for u in range(n) if in_degree[u] == 0])
    order = []
    
    while queue:
        u = queue.popleft()
        order.append(u)
        
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    if len(order) != n:
        return None  # Cycle exists
    
    return order
```

### 5.4 Properties

- Topological order is **not unique** (unless graph is a chain)
- Number of topological orderings can be exponential

### 5.5 Applications

1. **Task scheduling** with dependencies
2. **Build systems** (Makefiles)
3. **Course prerequisites**
4. **Symbol resolution** in linkers

---

## 🏝️ 6. Connected Components

### 6.1 Undirected: BFS/DFS

```python
def connected_components(adj, n):
    visited = [False] * n
    components = []
    
    def bfs(start):
        component = []
        queue = deque([start])
        visited[start] = True
        
        while queue:
            u = queue.popleft()
            component.append(u)
            
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        
        return component
    
    for i in range(n):
        if not visited[i]:
            components.append(bfs(i))
    
    return components
```

### 6.2 Directed: Strongly Connected Components (SCC)

**Kosaraju's Algorithm:**

```python
def kosaraju(adj, n):
    # Step 1: Fill order by finish times
    visited = [False] * n
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(n):
        if not visited[i]:
            dfs1(i)
    
    # Step 2: Create transpose graph
    adj_t = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            adj_t[v].append(u)
    
    # Step 3: DFS on transpose in reverse order
    visited = [False] * n
    sccs = []
    
    def dfs2(u, scc):
        visited[u] = True
        scc.append(u)
        for v in adj_t[u]:
            if not visited[v]:
                dfs2(v, scc)
    
    for u in reversed(order):
        if not visited[u]:
            scc = []
            dfs2(u, scc)
            sccs.append(scc)
    
    return sccs
```

### 6.3 Tarjan's Algorithm

Single DFS using low-link values:

```python
def tarjan_scc(adj, n):
    index = [0]
    indices = [-1] * n
    low_link = [0] * n
    on_stack = [False] * n
    stack = []
    sccs = []
    
    def strong_connect(u):
        indices[u] = index[0]
        low_link[u] = index[0]
        index[0] += 1
        stack.append(u)
        on_stack[u] = True
        
        for v in adj[u]:
            if indices[v] == -1:
                strong_connect(v)
                low_link[u] = min(low_link[u], low_link[v])
            elif on_stack[v]:
                low_link[u] = min(low_link[u], indices[v])
        
        # Root of SCC
        if low_link[u] == indices[u]:
            scc = []
            while True:
                v = stack.pop()
                on_stack[v] = False
                scc.append(v)
                if v == u:
                    break
            sccs.append(scc)
    
    for i in range(n):
        if indices[i] == -1:
            strong_connect(i)
    
    return sccs
```

### 6.4 Complexity

Both algorithms: O(V + E)

---

## 🛤️ 7. Shortest Paths

### 7.1 Single Source: Dijkstra (Non-negative weights)

```python
import heapq

def dijkstra(adj, n, source):
    dist = [float('inf')] * n
    dist[source] = 0
    pq = [(0, source)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
        
        for weight, v in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    
    return dist
```

**Complexity:**
- Binary heap: O((V + E) log V)
- Fibonacci heap: O(E + V log V)

### 7.2 Single Source: Bellman-Ford (Handles negative weights)

```python
def bellman_ford(edges, n, source):
    dist = [float('inf')] * n
    dist[source] = 0
    
    # Relax all edges V-1 times
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    # Check for negative cycle
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None  # Negative cycle exists
    
    return dist
```

**Complexity:** O(VE)

### 7.3 All Pairs: Floyd-Warshall

```python
def floyd_warshall(adj_matrix, n):
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Initialize
    for i in range(n):
        dist[i][i] = 0
        for j, w in adj_matrix[i]:
            dist[i][j] = w
    
    # DP: Consider each vertex as intermediate
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist
```

**Complexity:** O(V³)

### 7.4 Comparison

| Algorithm | Weights | Complexity | Use Case |
|-----------|---------|------------|----------|
| BFS | Unweighted | O(V+E) | Unit weights |
| Dijkstra | Non-negative | O(E log V) | Single source |
| Bellman-Ford | Any | O(VE) | Negative weights |
| Floyd-Warshall | Any | O(V³) | All pairs, dense |
| Johnson's | Any | O(VE log V) | All pairs, sparse |

### 7.5 🎯 GATE Traps

1. **Dijkstra fails with negative weights** - even one negative edge can break it
2. **Bellman-Ford detects negative cycles** - important for arbitrage detection
3. **Floyd-Warshall diagonal** - negative value indicates negative cycle

---

## 🌲 8. Minimum Spanning Tree (MST)

### 8.1 Kruskal's Algorithm

```python
def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # Sort by weight
    
    parent = list(range(n))
    rank = [0] * n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True
    
    mst = []
    mst_weight = 0
    
    for u, v, w in edges:
        if union(u, v):
            mst.append((u, v, w))
            mst_weight += w
            if len(mst) == n - 1:
                break
    
    return mst, mst_weight
```

### 8.2 Prim's Algorithm

```python
import heapq

def prim(adj, n):
    visited = [False] * n
    mst = []
    mst_weight = 0
    pq = [(0, 0, -1)]  # (weight, vertex, parent)
    
    while pq and len(mst) < n:
        w, u, parent = heapq.heappop(pq)
        
        if visited[u]:
            continue
        
        visited[u] = True
        mst_weight += w
        if parent != -1:
            mst.append((parent, u, w))
        
        for weight, v in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (weight, v, u))
    
    return mst, mst_weight
```

### 8.3 MST Properties

1. **Cut Property:** Min weight edge crossing any cut is in MST
2. **Cycle Property:** Max weight edge in any cycle is NOT in MST
3. **Unique MST:** If all edge weights are distinct
4. **MST edges:** Exactly V-1 for connected graph

---

## 🔗 9. Articulation Points and Bridges

### 9.1 Definitions

- **Articulation Point (Cut Vertex):** Removing it disconnects graph
- **Bridge (Cut Edge):** Removing it disconnects graph

### 9.2 Algorithm using DFS

```python
def find_articulation_points_bridges(adj, n):
    discovery = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    articulation = [False] * n
    bridges = []
    time = [0]
    
    def dfs(u):
        children = 0
        discovery[u] = low[u] = time[0]
        time[0] += 1
        
        for v in adj[u]:
            if discovery[v] == -1:  # Tree edge
                children += 1
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])
                
                # Articulation point conditions
                if parent[u] == -1 and children > 1:
                    articulation[u] = True
                if parent[u] != -1 and low[v] >= discovery[u]:
                    articulation[u] = True
                
                # Bridge condition
                if low[v] > discovery[u]:
                    bridges.append((u, v))
            
            elif v != parent[u]:  # Back edge
                low[u] = min(low[u], discovery[v])
    
    for i in range(n):
        if discovery[i] == -1:
            dfs(i)
    
    return [i for i in range(n) if articulation[i]], bridges
```

### 9.3 Key Concepts

**Low-link value:** Minimum discovery time reachable from subtree.

**Articulation Point u:**
- Root with ≥2 children, OR
- Non-root where child v has low[v] ≥ discovery[u]

**Bridge (u,v):**
- low[v] > discovery[u] (no way back to u's ancestors)

---

## 🔢 10. Bipartite Graph

### 10.1 Check Bipartiteness

```python
def is_bipartite(adj, n):
    color = [-1] * n
    
    def bfs(start):
        queue = deque([start])
        color[start] = 0
        
        while queue:
            u = queue.popleft()
            
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
        
        return True
    
    for i in range(n):
        if color[i] == -1:
            if not bfs(i):
                return False
    
    return True
```

### 10.2 🎯 GATE Point

**Graph is bipartite ⟺ No odd-length cycle**

---

## 🌊 11. Network Flow

### 11.1 Max Flow: Ford-Fulkerson (Edmonds-Karp)

```python
from collections import deque

def max_flow(capacity, source, sink):
    n = len(capacity)
    
    def bfs():
        visited = [-1] * n
        visited[source] = source
        queue = deque([source])
        
        while queue:
            u = queue.popleft()
            
            for v in range(n):
                if visited[v] == -1 and capacity[u][v] > 0:
                    visited[v] = u
                    queue.append(v)
                    if v == sink:
                        return visited
        
        return None
    
    flow = 0
    
    while True:
        parent = bfs()
        if parent is None:
            break
        
        # Find min capacity along path
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v])
            v = u
        
        # Update capacities
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = u
        
        flow += path_flow
    
    return flow
```

### 11.2 Complexity

| Method | Complexity |
|--------|------------|
| Ford-Fulkerson (DFS) | O(E × max_flow) |
| Edmonds-Karp (BFS) | O(VE²) |
| Dinic's | O(V²E) |

### 11.3 Min Cut = Max Flow

By Max-Flow Min-Cut theorem, the maximum flow equals the minimum cut capacity.

---

## 🎓 12. GATE Pattern Problems

### Problem Type 1: BFS/DFS Order

**Q:** BFS order from vertex A in graph A-B-C-D (path)?

**Answer:** A → B → C → D

---

### Problem Type 2: Shortest Path

**Q:** Shortest path from A to E with negative weights?

**Answer:** Use Bellman-Ford, not Dijkstra!

---

### Problem Type 3: SCC Count

**Q:** How many SCCs in graph with edges 1→2, 2→3, 3→1, 3→4?

**Solution:**
- SCC1: {1, 2, 3} (cycle)
- SCC2: {4} (single vertex)

**Answer: 2**

---

## 🚨 13. Common GATE Traps

### Trap 1: Dijkstra with Negative Weights
Always fails! Use Bellman-Ford.

### Trap 2: Topological Sort on Cyclic Graph
Impossible! Return error or detect cycle.

### Trap 3: MST vs Shortest Path
MST minimizes total edge weight, NOT individual path lengths.

### Trap 4: BFS vs DFS Space
Both O(V), but BFS can be O(width) at worst.

---

## 📝 14. Practice Problems

### Problem 1 [NAT]
Complete graph K₅. How many edges in MST?

<details>
<summary>Solution</summary>

MST always has V-1 edges.

**Answer: 4**
</details>

---

### Problem 2 [MCQ]
Which detects negative cycles?

A. Dijkstra
B. BFS
C. Bellman-Ford
D. Prim

<details>
<summary>Solution</summary>

**Answer:** C
</details>

---

### Problem 3 [MSQ]
Which are O(V+E)?

A. BFS
B. DFS
C. Dijkstra
D. Topological Sort

<details>
<summary>Solution</summary>

A. TRUE
B. TRUE
C. FALSE - O(E log V)
D. TRUE

**Answer:** A, B, D
</details>

---

## 🧠 Memory Anchors

### The Mental Slider: Graph Algorithm Selector

```
Shortest Path?
├── Unweighted → BFS
├── Non-negative → Dijkstra
├── Negative possible → Bellman-Ford
└── All pairs → Floyd-Warshall

Cycle Detection?
├── Undirected → DFS (back edge to non-parent)
└── Directed → DFS (gray node)

Components?
├── Undirected → BFS/DFS
└── Directed (SCC) → Kosaraju/Tarjan
```

### 5-Second Sanity Check

1. Is graph directed or undirected?
2. Are weights positive, negative, or absent?
3. Is traversal single-source or all-pairs?

---

## ⚡ Quick Reference

| Algorithm | Time | Space | Use Case |
|-----------|------|-------|----------|
| BFS | O(V+E) | O(V) | Shortest path (unweighted) |
| DFS | O(V+E) | O(V) | Cycle detection, topo sort |
| Dijkstra | O(E log V) | O(V) | SSSP (non-negative) |
| Bellman-Ford | O(VE) | O(V) | SSSP (any weights) |
| Floyd-Warshall | O(V³) | O(V²) | APSP |
| Kruskal | O(E log E) | O(V) | MST (sparse) |
| Prim | O(E log V) | O(V) | MST (dense) |
| Kosaraju | O(V+E) | O(V) | SCC |
| Tarjan | O(V+E) | O(V) | SCC, articulation |

---

**✅ Module Complete | Ready for GATE 2026**

**Next Module:** [Backtracking →](08-Backtracking.md)
