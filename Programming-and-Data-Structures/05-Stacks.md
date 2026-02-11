# Part 5: Stacks

> **The Atomic Truth:** *Stack = LIFO: Last In, First Out.*

---

## 5.1 Stack Concept & Operations

A stack is a linear data structure where insertion (push) and deletion (pop) happen at the **same end** (called the **top**).

**Analogy:** A stack of plates — you can only add or remove from the top. Trying to pull from the middle collapses everything.

### Core Operations — All $O(1)$

| Operation | Description |
|-----------|------------|
| `push(x)` | Insert element `x` at the top |
| `pop()` | Remove and return the top element |
| `peek()/top()` | Return top element without removing |
| `isEmpty()` | Check if stack is empty |
| `isFull()` | Check if stack is full (array-based) |

---

## 5.2 Array Implementation

```c
#define MAX 100
struct Stack {
    int arr[MAX];
    int top;
};

void init(struct Stack *s) { s->top = -1; }

int isEmpty(struct Stack *s) { return s->top == -1; }

int isFull(struct Stack *s) { return s->top == MAX - 1; }

void push(struct Stack *s, int x) {
    if (isFull(s)) { printf("Overflow\n"); return; }
    s->arr[++(s->top)] = x;
}

int pop(struct Stack *s) {
    if (isEmpty(s)) { printf("Underflow\n"); return -1; }
    return s->arr[(s->top)--];
}

int peek(struct Stack *s) {
    if (isEmpty(s)) return -1;
    return s->arr[s->top];
}
```

**Key details:**
- `top = -1` means empty stack
- `top = MAX - 1` means full stack
- Number of elements = `top + 1`
- Push: increment top first, then store
- Pop: read first, then decrement top

---

## 5.3 Linked List Implementation

```c
struct Node {
    int data;
    struct Node *next;
};

void push(struct Node **top, int data) {
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = *top;
    *top = newNode;
}

int pop(struct Node **top) {
    if (*top == NULL) { printf("Underflow\n"); return -1; }
    struct Node *temp = *top;
    int data = temp->data;
    *top = temp->next;
    free(temp);
    return data;
}
```

**Advantage:** No fixed size limit (limited only by memory).  
**Disadvantage:** Extra memory per element (pointer overhead).

---

## 5.4 Infix, Prefix, and Postfix Expressions

### Definitions

| Notation | Example | Operator Position |
|----------|---------|-------------------|
| **Infix** | `A + B` | Between operands |
| **Prefix** (Polish) | `+ A B` | Before operands |
| **Postfix** (Reverse Polish) | `A B +` | After operands |

### Why Postfix/Prefix?

- **No parentheses needed** — operator precedence is embedded in the expression
- **Easy to evaluate** using a stack
- **No ambiguity** — one-pass evaluation

### Conversion Rules

**Infix → Postfix (Shunting-Yard Algorithm):**

1. Scan left to right
2. **Operand** → output directly
3. **`(`** → push to stack
4. **`)`** → pop to output until `(` found, discard both parentheses
5. **Operator** → pop operators with **≥ precedence** (for left-associative) to output, then push current operator
6. At end → pop all remaining operators to output

**Example:** `A + B * C - D`

```
Token   Action                          Stack       Output
A       Output A                        []          A
+       Push +                          [+]         A
B       Output B                        [+]         A B
*       * > +, push *                   [+, *]      A B
C       Output C                        [+, *]      A B C
-       Pop * (≥ -), pop + (≥ -), push -  [-]       A B C * +
D       Output D                        [-]         A B C * + D
End     Pop all                         []          A B C * + D -
```

Result: `A B C * + D -`

### 🔴 GATE Trap: Right-to-Left Associativity

For **right-associative** operators (like `^`), pop only operators with **strictly greater** precedence (not equal).

**Example:** `A ^ B ^ C` → Postfix: `A B C ^ ^` (NOT `A B ^ C ^`)

Because `^` is right-associative: `A ^ (B ^ C)`.

### Postfix Evaluation Algorithm

```c
int evaluatePostfix(char *exp) {
    struct Stack s;
    init(&s);
    
    for (int i = 0; exp[i]; i++) {
        if (isdigit(exp[i])) {
            push(&s, exp[i] - '0');
        } else {
            int b = pop(&s);  // Second operand popped first!
            int a = pop(&s);  // First operand
            switch (exp[i]) {
                case '+': push(&s, a + b); break;
                case '-': push(&s, a - b); break;
                case '*': push(&s, a * b); break;
                case '/': push(&s, a / b); break;
            }
        }
    }
    return pop(&s);
}
```

**Critical:** Pop order matters for non-commutative operators (`-`, `/`). The first popped value is the **second operand**.

### Prefix Evaluation

Scan **right to left**, same algorithm as postfix but reversed.

Or equivalently: reverse the prefix expression, evaluate as postfix (swapping operand order for non-commutative operations).

### Infix → Prefix

**Method:** Reverse the infix → convert to postfix (swapping `(` and `)`) → reverse the result.

### Quick Conversion Table

| Infix | Postfix | Prefix |
|-------|---------|--------|
| `A + B` | `A B +` | `+ A B` |
| `A + B * C` | `A B C * +` | `+ A * B C` |
| `(A + B) * C` | `A B + C *` | `* + A B C` |
| `A + B * C - D / E` | `A B C * + D E / -` | `- + A * B C / D E` |
| `A ^ B ^ C` | `A B C ^ ^` | `^ A ^ B C` |

---

## 5.5 Parentheses Matching

```c
int isBalanced(char *exp) {
    struct Stack s;
    init(&s);
    
    for (int i = 0; exp[i]; i++) {
        if (exp[i] == '(' || exp[i] == '{' || exp[i] == '[')
            push(&s, exp[i]);
        else if (exp[i] == ')' || exp[i] == '}' || exp[i] == ']') {
            if (isEmpty(&s)) return 0;
            char top = pop(&s);
            if ((exp[i] == ')' && top != '(') ||
                (exp[i] == '}' && top != '{') ||
                (exp[i] == ']' && top != '['))
                return 0;
        }
    }
    return isEmpty(&s);  // Must be empty at end
}
```

**Edge cases:**
- Empty string → balanced
- Only closing brackets → unbalanced
- Only opening brackets → unbalanced
- Correct nesting but wrong type → unbalanced

---

## 5.6 Multiple Stacks in a Single Array

### Two Stacks

```c
// Stack 1 grows from left (index 0 →)
// Stack 2 grows from right (← index MAX-1)

struct TwoStacks {
    int arr[MAX];
    int top1, top2;
};

void init(struct TwoStacks *ts) {
    ts->top1 = -1;
    ts->top2 = MAX;
}

void push1(struct TwoStacks *ts, int x) {
    if (ts->top1 + 1 == ts->top2) { printf("Overflow\n"); return; }
    ts->arr[++(ts->top1)] = x;
}

void push2(struct TwoStacks *ts, int x) {
    if (ts->top2 - 1 == ts->top1) { printf("Overflow\n"); return; }
    ts->arr[--(ts->top2)] = x;
}
```

**Overflow condition:** `top1 + 1 == top2` — the stacks have met.

### $k$ Stacks in One Array

Use an auxiliary array to maintain free list:
- `top[k]` — top index for each stack
- `next[MAX]` — next element in the same stack, or next free slot

---

## 5.7 Stack Applications

### 1. Function Call Stack

Every function call pushes an activation record. Return pops it. This is why recursion uses $O(n)$ space — $n$ frames on the stack.

### 2. Undo/Redo Operations

- **Undo stack:** push every action; pop to undo
- **Redo stack:** push undone actions; pop to redo

### 3. Browser History

- **Back stack:** push current page when navigating
- **Forward stack:** push current page when going back

### 4. Stock Span Problem

For each day, find how many consecutive previous days had stock price ≤ today's price.

```c
void stockSpan(int price[], int span[], int n) {
    struct Stack s;
    init(&s);
    
    for (int i = 0; i < n; i++) {
        while (!isEmpty(&s) && price[peek(&s)] <= price[i])
            pop(&s);
        span[i] = isEmpty(&s) ? (i + 1) : (i - peek(&s));
        push(&s, i);  // Push index, not value
    }
}
```

### 5. Next Greater Element

For each element, find the nearest greater element to its right.

```c
void nextGreater(int arr[], int result[], int n) {
    struct Stack s;
    init(&s);
    
    for (int i = n - 1; i >= 0; i--) {
        while (!isEmpty(&s) && peek(&s) <= arr[i])
            pop(&s);
        result[i] = isEmpty(&s) ? -1 : peek(&s);
        push(&s, arr[i]);
    }
}
```

---

## 5.8 Stack Permutations

**Question type:** Given input sequence $1, 2, \ldots, n$, which output permutations are possible using a single stack?

**Rule:** A permutation is **stack-sortable** if and only if it avoids the pattern **231**.

**Meaning:** There is no subsequence where a larger element comes before a medium element, which comes before a smaller element, where the larger was pushed before the medium.

**Number of valid permutations** with $n$ elements:

$$C_n = \frac{1}{n+1}\binom{2n}{n} = \frac{(2n)!}{(n+1)! \cdot n!}$$

This is the **$n$-th Catalan number**.

**Example:** For $n = 3$: $C_3 = \frac{1}{4}\binom{6}{3} = \frac{20}{4} = 5$

The 5 valid permutations: {1,2,3}, {1,3,2}, {2,1,3}, {2,3,1}, {3,2,1}

The invalid one: **{3,1,2}** — cannot be produced.

### 🔴 GATE Trap: Checking a Specific Permutation

To check if a permutation is achievable:
1. Simulate: push input elements in order
2. Whenever the top of stack matches the next desired output, pop
3. If you can produce the entire output → valid

**Example:** Can we produce `3 2 1` from `1 2 3`?

```
Push 1, Push 2, Push 3 → Stack: [1, 2, 3]
Pop 3 ✓, Pop 2 ✓, Pop 1 ✓
Result: 3 2 1 → VALID
```

**Example:** Can we produce `3 1 2` from `1 2 3`?

```
Push 1, Push 2, Push 3 → Pop 3 ✓
Need 1, but top is 2 → must pop 2 first, but 2 comes after 1 in output → INVALID
```

---

## 5.9 Minimum Element in $O(1)$

### Method 1: Auxiliary Stack

```c
struct MinStack {
    struct Stack main;
    struct Stack minStack;  // Tracks minimum at each level
};

void push(struct MinStack *ms, int x) {
    push_stack(&ms->main, x);
    if (isEmpty(&ms->minStack) || x <= peek(&ms->minStack))
        push_stack(&ms->minStack, x);
}

int pop(struct MinStack *ms) {
    int val = pop_stack(&ms->main);
    if (val == peek(&ms->minStack))
        pop_stack(&ms->minStack);
    return val;
}

int getMin(struct MinStack *ms) {
    return peek(&ms->minStack);
}
```

### Method 2: Without Extra Space (Encoding trick)

```c
// Store: 2*x - min when pushing a new minimum
void push(int x) {
    if (isEmpty()) {
        push_actual(x);
        min = x;
    } else if (x < min) {
        push_actual(2 * x - min);  // Encoded value (will be < min)
        min = x;
    } else {
        push_actual(x);
    }
}
```

---

## Summary: Quick-Fire GATE Facts for Stacks

1. Stack = LIFO. All operations at one end.
2. Push/Pop/Peek = $O(1)$.
3. `top = -1` → empty; `top = MAX-1` → full (array-based).
4. Postfix evaluation: operands → push; operator → pop two, compute, push result.
5. **Pop order matters** for `-` and `/` in postfix.
6. Infix → Postfix: operators with ≥ precedence are popped (for left-associative).
7. For right-associative (`^`): only pop **strictly greater** precedence.
8. Valid stack permutations = Catalan number: $C_n = \frac{1}{n+1}\binom{2n}{n}$.
9. Invalid permutation pattern: avoids **231**.
10. Two stacks in one array: grow from opposite ends.

---

> **5-Second Snap-Check for Stack Questions:**
> 1. Is it about expression conversion? → Apply precedence rules carefully
> 2. Is it a permutation question? → Check for 231 pattern or simulate
> 3. Is it about minimum? → Think auxiliary stack or encoding
> 4. Number of valid permutations → Catalan number
