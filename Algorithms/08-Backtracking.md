# Module 8: Backtracking

## 🎯 The Atomic Truth
> **"Try, fail, undo, try again—systematically"**

---

## 🧠 Mental Model: Maze Explorer with Breadcrumbs

[Image: Explorer in maze, leaving trail, hitting dead end, backtracking]

- Try a path
- If dead end → backtrack (undo last choice)
- Try next option
- Continue until solution or all options exhausted

---

## 📐 1. The Backtracking Paradigm

### 1.1 General Structure

```python
def backtrack(state, choices):
    if is_solution(state):
        record_solution(state)
        return
    
    for choice in choices:
        if is_valid(state, choice):
            make_choice(state, choice)      # Do
            backtrack(state, new_choices)    # Recurse
            undo_choice(state, choice)       # Undo
```

### 1.2 Key Components

1. **State:** Current partial solution
2. **Choices:** Available options at current step
3. **Constraints:** Rules to filter invalid choices
4. **Goal:** When to stop (found solution)

### 1.3 Backtracking vs Brute Force

| Aspect | Brute Force | Backtracking |
|--------|-------------|--------------|
| Exploration | All combinations | Prunes invalid paths |
| Efficiency | Slow | Faster (with good pruning) |
| Space | Often higher | Lower (recursive stack) |

### 1.4 When to Use Backtracking

- **Constraint Satisfaction Problems**
- **Combinatorial Problems**
- **Optimization with constraints**
- **Puzzle solving**

---

## 👑 2. N-Queens Problem

### 2.1 Problem Statement

Place N queens on N×N chessboard such that no two queens attack each other.

### 2.2 Constraints

Queens attack:
- Same row ✗
- Same column ✗
- Same diagonal ✗

### 2.3 Algorithm

```python
def solve_n_queens(n):
    solutions = []
    board = [-1] * n  # board[row] = column of queen in that row
    
    def is_safe(row, col):
        for prev_row in range(row):
            prev_col = board[prev_row]
            # Same column or diagonal check
            if prev_col == col or abs(prev_col - col) == abs(prev_row - row):
                return False
        return True
    
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Undo
    
    backtrack(0)
    return solutions

def print_solution(board):
    n = len(board)
    for row in range(n):
        line = ['.' if c != board[row] else 'Q' for c in range(n)]
        print(' '.join(line))
    print()
```

### 2.4 Visualization (4-Queens)

```
Solution 1:        Solution 2:
. Q . .            . . Q .
. . . Q            Q . . .
Q . . .            . . . Q
. . Q .            . Q . .
```

### 2.5 Optimized with Sets

```python
def solve_n_queens_optimized(n):
    solutions = []
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col
    board = []
    
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            board.append(col)
            
            backtrack(row + 1)
            
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
            board.pop()
    
    backtrack(0)
    return solutions
```

### 2.6 Complexity

- Time: O(N!) in worst case, but pruning reduces significantly
- Space: O(N) for recursion stack

### 2.7 🎯 GATE Point: Number of Solutions

| N | Solutions |
|---|-----------|
| 1 | 1 |
| 2 | 0 |
| 3 | 0 |
| 4 | 2 |
| 5 | 10 |
| 6 | 4 |
| 7 | 40 |
| 8 | 92 |

---

## 🧩 3. Sudoku Solver

### 3.1 Problem Statement

Fill 9×9 grid with digits 1-9 such that each row, column, and 3×3 box contains all digits.

### 3.2 Algorithm

```python
def solve_sudoku(board):
    def is_valid(row, col, num):
        # Check row
        if num in board[row]:
            return False
        
        # Check column
        for r in range(9):
            if board[r][col] == num:
                return False
        
        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if board[r][c] == num:
                    return False
        
        return True
    
    def find_empty():
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    return (r, c)
        return None
    
    def backtrack():
        cell = find_empty()
        if cell is None:
            return True  # Solved!
        
        row, col = cell
        
        for num in range(1, 10):
            if is_valid(row, col, num):
                board[row][col] = num
                
                if backtrack():
                    return True
                
                board[row][col] = 0  # Undo
        
        return False  # No valid number found
    
    backtrack()
    return board
```

### 3.3 Optimization: Constraint Propagation

```python
def solve_sudoku_optimized(board):
    # Precompute available numbers for each cell
    rows = [set(range(1, 10)) for _ in range(9)]
    cols = [set(range(1, 10)) for _ in range(9)]
    boxes = [set(range(1, 10)) for _ in range(9)]
    
    empty = []
    
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                empty.append((r, c))
            else:
                num = board[r][c]
                rows[r].discard(num)
                cols[c].discard(num)
                boxes[3 * (r // 3) + c // 3].discard(num)
    
    def backtrack(idx):
        if idx == len(empty):
            return True
        
        r, c = empty[idx]
        box_idx = 3 * (r // 3) + c // 3
        
        for num in rows[r] & cols[c] & boxes[box_idx]:
            board[r][c] = num
            rows[r].remove(num)
            cols[c].remove(num)
            boxes[box_idx].remove(num)
            
            if backtrack(idx + 1):
                return True
            
            board[r][c] = 0
            rows[r].add(num)
            cols[c].add(num)
            boxes[box_idx].add(num)
        
        return False
    
    backtrack(0)
    return board
```

### 3.4 Complexity

- Worst case: O(9^81) without pruning
- With constraints: Much faster in practice

---

## 🎯 4. Subset Sum Problem

### 4.1 Problem Statement

Given set of numbers and target sum, find if subset exists with that sum.

### 4.2 Backtracking Solution

```python
def subset_sum(nums, target):
    def backtrack(index, current_sum):
        if current_sum == target:
            return True
        if index >= len(nums) or current_sum > target:
            return False
        
        # Include current element
        if backtrack(index + 1, current_sum + nums[index]):
            return True
        
        # Exclude current element
        return backtrack(index + 1, current_sum)
    
    return backtrack(0, 0)
```

### 4.3 Finding All Subsets

```python
def all_subsets_with_sum(nums, target):
    results = []
    
    def backtrack(index, current, current_sum):
        if current_sum == target:
            results.append(current[:])
            return
        if index >= len(nums) or current_sum > target:
            return
        
        # Include
        current.append(nums[index])
        backtrack(index + 1, current, current_sum + nums[index])
        current.pop()
        
        # Exclude
        backtrack(index + 1, current, current_sum)
    
    backtrack(0, [], 0)
    return results
```

### 4.4 Complexity

- Time: O(2^n) in worst case
- Space: O(n) recursion depth

### 4.5 🎯 GATE: Backtracking vs DP

| Aspect | Backtracking | DP |
|--------|--------------|-----|
| Goal | Find one/all solutions | Count/optimize |
| Overlapping | Avoids re-computation by pruning | Stores subproblem results |
| Use | When searching for feasible solutions | When counting/optimizing |

---

## 🔡 5. Permutations

### 5.1 Generate All Permutations

```python
def permutations(nums):
    results = []
    
    def backtrack(start):
        if start == len(nums):
            results.append(nums[:])
            return
        
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]  # Swap
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]  # Undo
    
    backtrack(0)
    return results
```

### 5.2 Permutations with Duplicates

```python
def unique_permutations(nums):
    results = []
    nums.sort()
    used = [False] * len(nums)
    
    def backtrack(current):
        if len(current) == len(nums):
            results.append(current[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            # Skip duplicates
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            
            used[i] = True
            current.append(nums[i])
            backtrack(current)
            current.pop()
            used[i] = False
    
    backtrack([])
    return results
```

### 5.3 Complexity

- Time: O(n × n!)
- Space: O(n)

---

## 📦 6. Combinations

### 6.1 Generate C(n, k)

```python
def combinations(n, k):
    results = []
    
    def backtrack(start, current):
        if len(current) == k:
            results.append(current[:])
            return
        
        # Pruning: not enough elements left
        if len(current) + (n - start) < k:
            return
        
        for i in range(start, n):
            current.append(i + 1)
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return results
```

### 6.2 Combination Sum

Find all combinations that sum to target (can reuse elements).

```python
def combination_sum(candidates, target):
    results = []
    candidates.sort()
    
    def backtrack(start, current, remaining):
        if remaining == 0:
            results.append(current[:])
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break  # Pruning
            
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])  # i, not i+1 (can reuse)
            current.pop()
    
    backtrack(0, [], target)
    return results
```

### 6.3 Complexity

- C(n,k): O(C(n,k) × k) to generate all
- Combination Sum: Exponential but pruned

---

## 🗺️ 7. Graph Coloring

### 7.1 Problem Statement

Color vertices of graph with m colors such that no two adjacent vertices have same color.

### 7.2 Algorithm

```python
def graph_coloring(adj, m):
    n = len(adj)
    colors = [0] * n
    
    def is_safe(vertex, color):
        for neighbor in adj[vertex]:
            if colors[neighbor] == color:
                return False
        return True
    
    def backtrack(vertex):
        if vertex == n:
            return True  # All vertices colored
        
        for color in range(1, m + 1):
            if is_safe(vertex, color):
                colors[vertex] = color
                
                if backtrack(vertex + 1):
                    return True
                
                colors[vertex] = 0  # Undo
        
        return False  # No valid coloring
    
    if backtrack(0):
        return colors
    return None
```

### 7.3 Chromatic Number

Minimum colors needed to color graph = **Chromatic Number χ(G)**

### 7.4 🎯 GATE Points

- Complete graph Kₙ: χ = n
- Bipartite graph: χ = 2
- Tree (n > 1): χ = 2
- Cycle (even length): χ = 2
- Cycle (odd length): χ = 3

---

## 🛤️ 8. Hamiltonian Path/Cycle

### 8.1 Definitions

- **Hamiltonian Path:** Visits every vertex exactly once
- **Hamiltonian Cycle:** Path that returns to start

### 8.2 Algorithm

```python
def hamiltonian_cycle(adj, n):
    path = [0]  # Start from vertex 0
    visited = [False] * n
    visited[0] = True
    
    def is_valid(v, pos):
        # Must be adjacent to previous vertex
        if path[pos - 1] not in adj[v]:
            return False
        # Not already visited
        if visited[v]:
            return False
        return True
    
    def backtrack(pos):
        if pos == n:
            # Check if cycle (last connects to first)
            return 0 in adj[path[-1]]
        
        for v in range(1, n):
            if is_valid(v, pos):
                path.append(v)
                visited[v] = True
                
                if backtrack(pos + 1):
                    return True
                
                path.pop()
                visited[v] = False
        
        return False
    
    if backtrack(1):
        return path
    return None
```

### 8.3 Complexity

- Time: O(n!) in worst case
- NP-complete problem

### 8.4 🎯 Hamiltonian vs Eulerian

| Property | Hamiltonian | Eulerian |
|----------|-------------|----------|
| Visits | Each vertex once | Each edge once |
| Condition | NP-complete to check | Polynomial time |
| Existence | No easy condition | All vertices even degree |

---

## 🧠 9. Maze Solving

### 9.1 Rat in a Maze

```python
def solve_maze(maze):
    n = len(maze)
    solution = [[0] * n for _ in range(n)]
    
    def is_safe(x, y):
        return 0 <= x < n and 0 <= y < n and maze[x][y] == 1
    
    def backtrack(x, y):
        if x == n - 1 and y == n - 1:
            solution[x][y] = 1
            return True
        
        if is_safe(x, y):
            solution[x][y] = 1
            
            # Try moving down
            if backtrack(x + 1, y):
                return True
            
            # Try moving right
            if backtrack(x, y + 1):
                return True
            
            # Backtrack
            solution[x][y] = 0
        
        return False
    
    if backtrack(0, 0):
        return solution
    return None
```

### 9.2 All Paths

```python
def all_paths_maze(maze):
    n = len(maze)
    paths = []
    
    def backtrack(x, y, path):
        if x == n - 1 and y == n - 1:
            paths.append(path[:])
            return
        
        # Try all 4 directions
        directions = [(1, 0, 'D'), (0, 1, 'R'), (-1, 0, 'U'), (0, -1, 'L')]
        
        for dx, dy, direction in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] == 1:
                maze[x][y] = 0  # Mark visited
                path.append(direction)
                backtrack(nx, ny, path)
                path.pop()
                maze[x][y] = 1  # Unmark
    
    maze[0][0] = 0  # Mark start as visited
    backtrack(0, 0, [])
    maze[0][0] = 1  # Restore
    
    return paths
```

---

## 🔧 10. Pruning Techniques

### 10.1 Constraint Propagation

Check constraints early to reduce search space.

```python
# Instead of:
if is_complete(state) and is_valid(state):
    ...

# Use:
if not is_valid_partial(state):
    return  # Prune early
```

### 10.2 Ordering Heuristics

**Most Constrained Variable (MCV):** Choose variable with fewest remaining values.

**Least Constraining Value (LCV):** Choose value that rules out fewest options for neighbors.

### 10.3 Symmetry Breaking

Avoid exploring symmetric solutions.

Example in N-Queens: First queen in first half of first row only.

### 10.4 Bound-based Pruning

For optimization, track best solution and prune paths that can't improve.

```python
def backtrack_with_bound(state, current_cost, best_cost):
    if current_cost >= best_cost[0]:
        return  # Can't improve
    
    if is_solution(state):
        best_cost[0] = current_cost
        return
    
    # Continue exploration...
```

---

## 🎓 11. GATE Pattern Problems

### Problem Type 1: N-Queens Count

**Q:** How many solutions for 4-Queens?

**Answer:** 2

---

### Problem Type 2: Complexity Analysis

**Q:** Time complexity of brute force vs backtracking for N-Queens?

**Answer:**
- Brute force: O(N^N) - try all positions
- Backtracking: O(N!) with pruning - much better

---

### Problem Type 3: Backtracking vs DP

**Q:** When to use backtracking over DP?

**Answer:**
- Finding all solutions (not just count)
- Constraint satisfaction
- When overlapping subproblems are few

---

## 🚨 12. Common GATE Traps

### Trap 1: Forgetting to Undo

```python
# WRONG
make_choice(state, choice)
backtrack(state)
# Missing: undo_choice(state, choice)
```

### Trap 2: Modifying Iteration Variable

```python
# WRONG
for i in range(len(items)):
    items.remove(items[i])  # Modifying while iterating!
```

### Trap 3: Premature Termination

Ensure you explore all branches if finding ALL solutions.

### Trap 4: Inefficient Validity Check

```python
# WRONG: O(n²) check every time
def is_safe(board, row, col):
    for i in range(n):
        for j in range(n):
            # Full board scan

# RIGHT: O(n) check using sets or targeted check
```

---

## 📝 13. Practice Problems

### Problem 1 [NAT]
N-Queens for N=5. How many solutions?

<details>
<summary>Solution</summary>

**Answer: 10**
</details>

---

### Problem 2 [MCQ]
Which is NOT typically solved by backtracking?

A. Sudoku
B. Graph Coloring
C. Shortest Path
D. Subset Sum

<details>
<summary>Solution</summary>

Shortest Path uses BFS/Dijkstra, not backtracking.

**Answer:** C
</details>

---

### Problem 3 [MSQ]
Which improve backtracking efficiency?

A. Pruning invalid paths early
B. Variable ordering heuristics
C. Using more memory for memoization
D. Symmetry breaking

<details>
<summary>Solution</summary>

All except C (memoization is more DP-related).

**Answer:** A, B, D
</details>

---

## 🧠 Memory Anchors

### The Backtracking Template (DRU)

1. **D**ecide: Make a choice
2. **R**ecurse: Explore with that choice
3. **U**ndo: Revert the choice

### The Bizarre Mnemonic: "Explorer in a Maze"

- **Make choice:** Take a path
- **Hit wall:** Can't continue
- **Backtrack:** Go back to last junction
- **Try next:** Take different path
- **Find exit:** Solution found!

### 5-Second Sanity Check

1. Is the problem about finding valid configurations?
2. Can partial solutions be validated?
3. Can we undo choices easily?
4. If all yes → Backtracking!

---

## ⚡ Quick Reference

| Problem | Time Complexity | Key Pruning |
|---------|-----------------|-------------|
| N-Queens | O(N!) | Diagonal checks |
| Sudoku | O(9^81) worst | Constraint propagation |
| Subset Sum | O(2^n) | Sum exceeds target |
| Permutations | O(n × n!) | Used array |
| Graph Coloring | O(m^n) | Adjacent color check |
| Hamiltonian | O(n!) | Visited check |

---

**✅ Module Complete | Ready for GATE 2026**

**Next Module:** [String Algorithms →](09-String-Algorithms.md)
