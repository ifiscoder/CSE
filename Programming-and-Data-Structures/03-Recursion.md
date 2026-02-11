# Part 3: Recursion

> **The Atomic Truth:** *Recursion = self-similar subproblem + base case.*

---

## 3.1 How Recursion Works — The Stack Frame Model

Every function call creates a **stack frame** (activation record) containing:
- Return address
- Parameters
- Local variables
- Saved registers

```c
int factorial(int n) {
    if (n <= 1) return 1;       // Base case
    return n * factorial(n - 1); // Recursive case
}
```

**Stack visualization for `factorial(4)`:**

```
Call Stack (grows downward):
┌─────────────────┐
│ factorial(4)     │ ← waiting for factorial(3)
├─────────────────┤
│ factorial(3)     │ ← waiting for factorial(2)
├─────────────────┤
│ factorial(2)     │ ← waiting for factorial(1)
├─────────────────┤
│ factorial(1)     │ ← returns 1 (base case hit)
└─────────────────┘

Unwinding:
factorial(1) = 1
factorial(2) = 2 × 1 = 2
factorial(3) = 3 × 2 = 6
factorial(4) = 4 × 6 = 24
```

**Key Insight:** Each call is **independent** — it has its own copy of `n`. The function doesn't "remember" other calls; it waits for the return value.

**Analogy:** Recursion is like a chain of managers. The CEO asks VP, VP asks Director, Director asks Manager... the Manager (base case) actually does the work, and results flow back up the chain.

---

## 3.2 Recurrence Relations — Solving for Time Complexity

### Setting Up Recurrences

| Code Pattern | Recurrence | Solution |
|-------------|-----------|----------|
| `f(n) = f(n-1) + O(1)` | $T(n) = T(n-1) + c$ | $O(n)$ |
| `f(n) = f(n-1) + O(n)` | $T(n) = T(n-1) + cn$ | $O(n^2)$ |
| `f(n) = 2·f(n/2) + O(n)` | $T(n) = 2T(n/2) + cn$ | $O(n \log n)$ |
| `f(n) = 2·f(n-1) + O(1)` | $T(n) = 2T(n-1) + c$ | $O(2^n)$ |
| `f(n) = f(n/2) + O(1)` | $T(n) = T(n/2) + c$ | $O(\log n)$ |

### Master Theorem — The Swiss Army Knife

For recurrences of the form:

$$T(n) = aT(n/b) + \Theta(n^k \log^p n)$$

where $a \geq 1$, $b > 1$:

Compare $\log_b a$ with $k$:

| Case | Condition | Result |
|------|-----------|--------|
| 1 | $\log_b a > k$ | $T(n) = \Theta(n^{\log_b a})$ |
| 2 | $\log_b a = k$ and $p > -1$ | $T(n) = \Theta(n^k \log^{p+1} n)$ |
| 2' | $\log_b a = k$ and $p = -1$ | $T(n) = \Theta(n^k \log \log n)$ |
| 2'' | $\log_b a = k$ and $p < -1$ | $T(n) = \Theta(n^k)$ |
| 3 | $\log_b a < k$ | $T(n) = \Theta(n^k \log^p n)$ |

**How the Master Theorem works (intuition):**

The recursion tree has:
- **Height** = $\log_b n$
- **Branching factor** = $a$ (each node has $a$ children)
- **Work at level $i$** = $a^i \times f(n/b^i)$
- Total leaves = $a^{\log_b n} = n^{\log_b a}$

The theorem simply asks: **Who wins — the leaves (splitting work) or the per-level work (combining work)?**

### Example Applications

**Merge Sort:** $T(n) = 2T(n/2) + \Theta(n)$
- $a = 2$, $b = 2$, $k = 1$, $p = 0$
- $\log_b a = \log_2 2 = 1 = k$ → Case 2 with $p = 0 > -1$
- $T(n) = \Theta(n \log n)$ ✓

**Binary Search:** $T(n) = T(n/2) + \Theta(1)$
- $a = 1$, $b = 2$, $k = 0$, $p = 0$
- $\log_b a = 0 = k$ → Case 2
- $T(n) = \Theta(\log n)$ ✓

**Strassen's Matrix Multiplication:** $T(n) = 7T(n/2) + \Theta(n^2)$
- $a = 7$, $b = 2$, $k = 2$
- $\log_b a = \log_2 7 \approx 2.807 > 2 = k$ → Case 1
- $T(n) = \Theta(n^{\log_2 7}) \approx \Theta(n^{2.807})$ ✓

### Substitution Method (for non-standard recurrences)

**Example:** $T(n) = T(\sqrt{n}) + 1$

**Trick:** Let $n = 2^m$, so $\sqrt{n} = 2^{m/2}$

$$T(2^m) = T(2^{m/2}) + 1$$

Let $S(m) = T(2^m)$:

$$S(m) = S(m/2) + 1$$

By Master Theorem: $S(m) = \Theta(\log m)$

So $T(n) = \Theta(\log \log n)$ ✓

### Recursion Tree Method

For $T(n) = 3T(n/4) + cn^2$:

```
Level 0:           cn²                          Total = cn²
Level 1:    c(n/4)²  c(n/4)²  c(n/4)²          Total = 3c(n/4)² = (3/16)cn²
Level 2:    ... 9 nodes of c(n/16)² each         Total = (3/16)²cn²
...
Level i:    3^i nodes of c(n/4^i)² each          Total = (3/16)^i × cn²
```

Total = $cn^2 \sum_{i=0}^{\log_4 n} (3/16)^i = cn^2 \times \frac{1}{1 - 3/16} = \frac{16}{13} cn^2 = \Theta(n^2)$

Since $3/16 < 1$, the geometric series converges. Root dominates → $\Theta(n^2)$.

---

## 3.3 Types of Recursion

### 1. Tail Recursion

The recursive call is the **last operation** — nothing happens after it returns.

```c
// Tail recursive factorial
int factorial_tail(int n, int acc) {
    if (n <= 1) return acc;
    return factorial_tail(n - 1, n * acc);  // Last operation
}
// Call: factorial_tail(5, 1) → 120
```

**Why it matters:** Tail recursion can be optimized by the compiler into a **loop** (tail call optimization), using $O(1)$ stack space instead of $O(n)$.

### 2. Head Recursion

The recursive call happens **before** any processing.

```c
void head(int n) {
    if (n == 0) return;
    head(n - 1);      // Call first
    printf("%d ", n);  // Process after
}
// head(3) → prints: 1 2 3
```

### 3. Tree Recursion

Function calls itself **multiple times** per invocation.

```c
int fib(int n) {
    if (n <= 1) return n;
    return fib(n-1) + fib(n-2);  // TWO recursive calls
}
```

**Time complexity:** $T(n) = T(n-1) + T(n-2) + O(1)$

This gives $T(n) = O(2^n)$ (roughly). More precisely, $T(n) = O(\phi^n)$ where $\phi = \frac{1+\sqrt{5}}{2} \approx 1.618$.

**Space complexity:** $O(n)$ — the maximum depth of the call stack.

### 🔴 GATE Trap: Number of function calls in Fibonacci

For `fib(n)`, total calls = $2 \times F(n+1) - 1$ where $F(k)$ is the $k$-th Fibonacci number.

```
fib(5) makes these calls:
fib(5) → fib(4) + fib(3)
fib(4) → fib(3) + fib(2)
fib(3) → fib(2) + fib(1)     [called twice!]
fib(2) → fib(1) + fib(0)     [called three times!]

Total calls for fib(5) = 15
```

### 4. Indirect Recursion

Functions call each other in a cycle.

```c
void funcA(int n) {
    if (n <= 0) return;
    printf("%d ", n);
    funcB(n - 1);
}

void funcB(int n) {
    if (n <= 0) return;
    printf("%d ", n);
    funcA(n - 2);
}
// funcA(5) → 5 4 2 1
```

---

## 3.4 Classic Recursive Problems

### Tower of Hanoi

**Problem:** Move $n$ disks from source to destination using auxiliary peg. Rules: move one disk at a time, never place larger on smaller.

```c
void hanoi(int n, char src, char aux, char dest) {
    if (n == 0) return;
    hanoi(n - 1, src, dest, aux);    // Move n-1 disks to auxiliary
    printf("Move disk %d: %c → %c\n", n, src, dest);  // Move largest
    hanoi(n - 1, aux, src, dest);    // Move n-1 disks to destination
}
```

**Number of moves:**

$$T(n) = 2T(n-1) + 1, \quad T(0) = 0$$

Solving: $T(n) = 2^n - 1$

**Derivation:**
$$T(n) = 2T(n-1) + 1 = 2[2T(n-2) + 1] + 1 = 4T(n-2) + 3$$
$$= 8T(n-3) + 7 = \ldots = 2^k T(n-k) + (2^k - 1)$$

At $k = n$: $T(n) = 2^n \cdot T(0) + 2^n - 1 = 0 + 2^n - 1 = 2^n - 1$

**Mnemonic:** "Hanoi = $2^n - 1$" — think of it as a binary counter counting from 0 to $2^n - 1$.

### Power Function

```c
// Naive: O(n)
int power(int x, int n) {
    if (n == 0) return 1;
    return x * power(x, n - 1);
}

// Fast (binary exponentiation): O(log n)
int fast_power(int x, int n) {
    if (n == 0) return 1;
    int half = fast_power(x, n / 2);
    if (n % 2 == 0)
        return half * half;
    else
        return x * half * half;
}
```

**Recurrence for fast power:** $T(n) = T(n/2) + O(1) = O(\log n)$

### GCD (Euclid's Algorithm)

```c
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
```

**Why it works:** $\gcd(a, b) = \gcd(b, a \bmod b)$ because any common divisor of $a$ and $b$ also divides $a \bmod b$.

**Time complexity:** $O(\log(\min(a, b)))$ — each step reduces the larger number by at least half.

---

## 3.5 Recursion vs Iteration

| Aspect | Recursion | Iteration |
|--------|----------|-----------|
| Space | $O(n)$ stack frames (unless tail-optimized) | $O(1)$ typically |
| Overhead | Function call overhead per recursion | Loop overhead (minimal) |
| Readability | Often cleaner for tree/divide-and-conquer | Cleaner for linear processes |
| Termination | Base case | Loop condition |
| Stack overflow | Possible for deep recursion | Not an issue |

**Key theorem:** Every recursive algorithm can be converted to an iterative one using an explicit stack.

---

## 3.6 Tracing Recursive Functions — GATE Technique

### Step-by-Step Tracing

```c
int mystery(int n) {
    if (n == 0) return 0;
    return mystery(n / 2) + n % 2;
}
// What does mystery(11) return?
```

**Trace:**
```
mystery(11) = mystery(5) + 11%2 = mystery(5) + 1
mystery(5)  = mystery(2) + 5%2  = mystery(2) + 1
mystery(2)  = mystery(1) + 2%2  = mystery(1) + 0
mystery(1)  = mystery(0) + 1%2  = 0 + 1 = 1

Unwinding: 1 + 0 + 1 + 1 = 3
```

**The function counts the number of 1-bits** in the binary representation of $n$! ($11 = 1011_2$ → three 1s)

### 🔴 GATE Trap: Static Variable in Recursion

```c
int fun(int n) {
    static int x = 0;
    if (n <= 0) return x;
    x++;
    return fun(n - 1) + x;  // x is shared across ALL calls!
}
```

**Trap:** `static` variables maintain state across recursive calls. The value of `x` is the **final value** when used in expressions that are evaluated during unwinding, not the value at the time of the call.

### Output Prediction: Print Before vs After Recursion

```c
void before(int n) {
    if (n == 0) return;
    printf("%d ", n);
    before(n - 1);
}
// before(3) → 3 2 1 (prints on the way DOWN)

void after(int n) {
    if (n == 0) return;
    after(n - 1);
    printf("%d ", n);
}
// after(3) → 1 2 3 (prints on the way UP / unwinding)
```

**Mnemonic:** Print BEFORE recursive call = descending order. Print AFTER = ascending order.

---

## 3.7 Backtracking (Brief Intro)

Backtracking uses recursion to explore all possibilities and "undo" choices that don't lead to a solution.

**Template:**
```c
void backtrack(State state, ...) {
    if (isSolution(state)) {
        processSolution(state);
        return;
    }
    for (each choice c) {
        if (isValid(c, state)) {
            makeChoice(c, state);       // Choose
            backtrack(newState, ...);    // Explore
            undoChoice(c, state);        // Un-choose (backtrack)
        }
    }
}
```

**Classic examples:** N-Queens, Subset Sum, Permutations, Maze solving.

---

## 3.8 Stack Space of Recursive Functions

**Formula:** Stack space = Maximum depth of recursion × Size of each frame

| Function | Max Depth | Stack Space |
|----------|-----------|-------------|
| `factorial(n)` | $n$ | $O(n)$ |
| `fib(n)` (naive) | $n$ | $O(n)$ |
| `binary_search(n)` | $\log n$ | $O(\log n)$ |
| `merge_sort(n)` | $\log n$ | $O(\log n)$ + $O(n)$ for merge |
| `quick_sort(n)` worst | $n$ | $O(n)$ |
| `quick_sort(n)` best | $\log n$ | $O(\log n)$ |

---

## Summary: Quick-Fire GATE Facts for Recursion

1. Every recursion needs a **base case** and **progress toward it**.
2. Tail recursion → can be optimized to $O(1)$ space.
3. Tree recursion (like naive Fibonacci) → exponential time.
4. Hanoi: $2^n - 1$ moves.
5. `static` variables in recursion are **shared** across all calls.
6. Print before call → descending. Print after call → ascending.
7. Master Theorem: compare $\log_b a$ with $k$.
8. Any recursion can be converted to iteration with an explicit stack.

---

> **5-Second Snap-Check for Recursion Questions:**
> 1. Write the recurrence relation first.
> 2. Check: is it tail recursive? (last operation = recursive call)
> 3. For output tracing: identify if `static` variables exist.
> 4. For complexity: try Master Theorem first, then substitution.
