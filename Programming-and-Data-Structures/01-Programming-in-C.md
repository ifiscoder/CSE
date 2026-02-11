# Part 1: Programming in C — Foundations

> **The Atomic Truth:** *C is typed memory manipulation through pointers.*

---

## 1.1 Data Types & Storage Sizes

### Fundamental Types

| Type | Size (typical 64-bit) | Range | Format Specifier |
|------|----------------------|-------|-----------------|
| `char` | 1 byte | $-128$ to $127$ (signed) or $0$ to $255$ (unsigned) | `%c`, `%d` (as int) |
| `short` | 2 bytes | $-2^{15}$ to $2^{15}-1$ | `%hd` |
| `int` | 4 bytes | $-2^{31}$ to $2^{31}-1$ | `%d` |
| `long` | 8 bytes (64-bit) / 4 bytes (32-bit) | varies | `%ld` |
| `long long` | 8 bytes | $-2^{63}$ to $2^{63}-1$ | `%lld` |
| `float` | 4 bytes | ~$\pm 3.4 \times 10^{38}$ (6-7 sig digits) | `%f` |
| `double` | 8 bytes | ~$\pm 1.7 \times 10^{308}$ (15-16 sig digits) | `%lf` |

### Why These Sizes?

The formula for the range of an $n$-bit signed integer (2's complement):

$$\text{Range} = [-2^{n-1}, \; 2^{n-1} - 1]$$

**Derivation:** With $n$ bits, total patterns = $2^n$. One bit is the sign bit. The negative side gets one extra value because $0$ is counted as positive. So negatives: $2^{n-1}$ values (from $-1$ to $-2^{n-1}$), non-negatives: $2^{n-1}$ values (from $0$ to $2^{n-1}-1$).

For unsigned: Range = $[0, \; 2^n - 1]$

**Example:**
```c
unsigned char x = 255;  // Max value: 2^8 - 1 = 255
x = x + 1;             // Wraps around to 0 (modular arithmetic)
printf("%d", x);        // Output: 0
```

### 🔴 GATE Trap: Overflow Behavior

```c
int x = 2147483647;  // INT_MAX = 2^31 - 1
x = x + 1;           // UNDEFINED BEHAVIOR for signed!
```

**Key Rule:** Signed overflow is **undefined behavior** in C. Unsigned overflow is **well-defined** (wraps modulo $2^n$).

> **5-Second Snap-Check:** If a question involves incrementing `INT_MAX` → answer is "undefined behavior" (not a specific value).

---

## 1.2 Operators — Precedence & Associativity

### Precedence Table (Top = Highest)

| Level | Operators | Associativity |
|-------|----------|---------------|
| 1 | `()` `[]` `->` `.` | Left to Right |
| 2 | `!` `~` `++` `--` `+` `-` `*` `&` `(type)` `sizeof` | **Right to Left** |
| 3 | `*` `/` `%` | Left to Right |
| 4 | `+` `-` | Left to Right |
| 5 | `<<` `>>` | Left to Right |
| 6 | `<` `<=` `>` `>=` | Left to Right |
| 7 | `==` `!=` | Left to Right |
| 8 | `&` (bitwise AND) | Left to Right |
| 9 | `^` (XOR) | Left to Right |
| 10 | `\|` (OR) | Left to Right |
| 11 | `&&` | Left to Right |
| 12 | `\|\|` | Left to Right |
| 13 | `?:` | **Right to Left** |
| 14 | `=` `+=` `-=` etc. | **Right to Left** |
| 15 | `,` | Left to Right |

### 🧠 Mnemonic: "**Please Excuse My Dear Aunt Sally Became Extremely Lazy After Cozy Teatime**"

**P**ostfix → **E**xclamation(Unary) → **M**ultiply → **D**ivide-Add → **A**rrows(Shift) → **S**maller(Relational) → **B**oth-equal(Equality) → **E**lectric(&) → **L**ightning(^) → **A**lternate(|) → **C**ombined(&&) → **T**ogether(||)

### 🔴 GATE Trap: Associativity of Unary vs Assignment

```c
int a = 5, b;
b = a++ + ++a;  // UNDEFINED BEHAVIOR!
```

**Why?** The variable `a` is modified more than once between two sequence points. The C standard says this is **undefined**. GATE loves asking this — the answer is NOT a specific number.

### Short-Circuit Evaluation

```c
int a = 0, b = 5;
if (a && (b = 10)) { }
printf("%d", b);  // Output: 5 (b=10 never executes!)
```

**Rule:** In `&&`, if the left operand is 0 (false), the right operand is **never evaluated**. In `||`, if the left operand is non-zero (true), the right operand is **never evaluated**.

**Analogy:** Think of `&&` as a lazy security guard — if the first ID check fails, he doesn't bother checking the second.

---

## 1.3 Control Flow

### The `switch` Statement — Edge Cases

```c
int x = 2;
switch(x) {
    case 1: printf("A");
    case 2: printf("B");
    case 3: printf("C");
    default: printf("D");
}
// Output: BCD (fall-through!)
```

**Key Rule:** Without `break`, execution **falls through** all subsequent cases. This is the #1 trap in switch questions.

### 🔴 GATE Trap: `switch` with expressions

```c
switch(x) {
    case 1+1: printf("Two");   // Valid: constant expression
    case 'A':  printf("65");   // Valid: 'A' = 65
    // case y:                  // INVALID: variable not allowed
    // case 1.5:                // INVALID: must be integer
}
```

**Rules for `case` labels:**
1. Must be **integer constant expressions** (evaluated at compile time)
2. No duplicates allowed
3. No floating-point values
4. No variables

### Loop Analysis — Counting Iterations

**Formula for `for(i = a; i < b; i += c)`:**

$$\text{Iterations} = \left\lceil \frac{b - a}{c} \right\rceil$$

**Example:**
```c
for (int i = 3; i < 20; i += 4)
    // Iterations = ceil((20-3)/4) = ceil(4.25) = 5
    // Values: 3, 7, 11, 15, 19
```

**For nested loops:**
```c
for (int i = 1; i <= n; i++)
    for (int j = 1; j <= i; j++)
        count++;
// Total = 1 + 2 + 3 + ... + n = n(n+1)/2
```

$$\text{Total iterations} = \sum_{i=1}^{n} i = \frac{n(n+1)}{2}$$

### Common Loop Patterns & Their Counts

| Loop Pattern | Iterations |
|-------------|-----------|
| `for(i=1; i<=n; i*=2)` | $\lfloor \log_2 n \rfloor + 1$ |
| `for(i=n; i>=1; i/=2)` | $\lfloor \log_2 n \rfloor + 1$ |
| `for(i=1; i<=n; i*=c)` | $\lfloor \log_c n \rfloor + 1$ |
| `for(i=1; i*i<=n; i++)` | $\lfloor \sqrt{n} \rfloor$ |
| Nested: `i: 1→n`, `j: 1→i` | $\frac{n(n+1)}{2}$ |
| Nested: `i: 1→n`, `j: i→n` | $\frac{n(n+1)}{2}$ |
| Nested: `i: 1→n (×2)`, `j: 1→i` | $2n - 1$ (Geometric sum) |

**Why `i*=2` gives $\lfloor \log_2 n \rfloor + 1$:**

After $k$ iterations, $i = 2^k$. Loop stops when $2^k > n$, i.e., $k > \log_2 n$. The smallest such $k$ is $\lfloor \log_2 n \rfloor + 1$.

---

## 1.4 Functions

### Parameter Passing

C uses **pass by value** exclusively. There is NO pass by reference in C (that's C++).

```c
void swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    int x = 5, y = 10;
    swap(x, y);
    printf("%d %d", x, y);  // Output: 5 10 (unchanged!)
}
```

**To simulate pass by reference, use pointers:**

```c
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 5, y = 10;
    swap(&x, &y);
    printf("%d %d", x, y);  // Output: 10 5
}
```

**Analogy:** Pass by value is like giving someone a **photocopy** of your document — they can scribble on it, but your original is unchanged. Pass by pointer is giving them your **home address** — they can come and rearrange your furniture.

### Function Pointer Syntax

```c
int add(int a, int b) { return a + b; }

int main() {
    int (*fptr)(int, int) = &add;  // & is optional
    printf("%d", fptr(3, 4));      // Output: 7
    printf("%d", (*fptr)(3, 4));   // Also valid: 7
}
```

**Reading function pointer declarations (Right-Left Rule):**
`int (*fptr)(int, int)` → "fptr is a pointer to a function taking two ints, returning int"

### 🔴 GATE Trap: Array Decay in Function Parameters

```c
void foo(int arr[]) {
    printf("%zu", sizeof(arr));  // Output: 8 (pointer size, NOT array size!)
}

int main() {
    int arr[10];
    printf("%zu", sizeof(arr));  // Output: 40 (10 × 4 bytes)
    foo(arr);
}
```

**Rule:** When an array is passed to a function, it **decays to a pointer**. `sizeof` inside the function gives pointer size, not array size.

---

## 1.5 Pointers — The Master Key

### Pointer Arithmetic

If `p` is a pointer to type `T`, then:
- `p + 1` advances by `sizeof(T)` bytes
- `p + n` advances by `n × sizeof(T)` bytes
- `p2 - p1` gives the number of **elements** between them (not bytes)

```c
int arr[] = {10, 20, 30, 40, 50};
int *p = arr;

printf("%d", *(p + 2));    // 30 (arr[2])
printf("%d", *(arr + 3));  // 40 (arr[3])
printf("%d", 2[arr]);      // 30 (same as arr[2], because a[i] = *(a+i) = *(i+a) = i[a])
```

**Why `2[arr]` works:** The `[]` operator is defined as `a[b] ≡ *(a + b)`. Since addition is commutative: `*(a + b) = *(b + a) = b[a]`.

### Pointer to Array vs Array of Pointers

```c
int (*p)[5];    // Pointer to an array of 5 ints
int *p[5];      // Array of 5 pointers to int
```

**Mnemonic:** `[]` binds tighter than `*`. So `int *p[5]` → `p` is first an array `[5]`, then pointers `*`. Parentheses `(*p)` force `p` to be a pointer first.

### Double Pointers

```c
int x = 10;
int *p = &x;
int **pp = &p;

printf("%d", **pp);  // 10
// **pp → *(*pp) → *(p) → x → 10
```

**Use case:** Modifying a pointer inside a function requires a pointer-to-pointer:

```c
void allocate(int **pp) {
    *pp = (int *)malloc(sizeof(int));
    **pp = 42;
}

int main() {
    int *p = NULL;
    allocate(&p);
    printf("%d", *p);  // 42
    free(p);
}
```

### `const` with Pointers — Four Combinations

| Declaration | Read as | Pointer mutable? | Data mutable? |
|------------|---------|-------------------|---------------|
| `int *p` | pointer to int | ✅ | ✅ |
| `const int *p` | pointer to const int | ✅ | ❌ |
| `int *const p` | const pointer to int | ❌ | ✅ |
| `const int *const p` | const pointer to const int | ❌ | ❌ |

**Mnemonic:** Read right-to-left from the variable name. Whatever is to the left of `*` is what's constant about the **data**. `const` to the right of `*` (between `*` and name) makes the **pointer** constant.

### 🔴 GATE Trap: Dangling Pointer

```c
int *foo() {
    int x = 10;
    return &x;  // WARNING: returning address of local variable!
}

int main() {
    int *p = foo();
    printf("%d", *p);  // UNDEFINED BEHAVIOR (dangling pointer)
}
```

**Rule:** Local variables are destroyed when the function returns. Their addresses become **dangling pointers**.

### Void Pointer

```c
void *vp;
int x = 10;
vp = &x;

// printf("%d", *vp);        // ERROR: can't dereference void*
printf("%d", *(int *)vp);    // OK: cast first, then dereference
```

**Rules for `void *`:**
1. Can hold address of any type
2. Cannot be dereferenced without casting
3. Pointer arithmetic on `void *` is **undefined** in standard C (GCC allows it, treating size as 1)

### NULL Pointer

```c
int *p = NULL;  // p points to address 0 (typically)
if (p) { }     // false — NULL is falsy
// *p           // SEGMENTATION FAULT (dereferencing NULL)
```

---

## 1.6 Storage Classes

| Storage Class | Scope | Lifetime | Default Init | Stored In |
|--------------|-------|----------|-------------|-----------|
| `auto` | Block | Block execution | Garbage | Stack |
| `register` | Block | Block execution | Garbage | CPU Register (hint) |
| `static` (local) | Block | **Entire program** | 0 | Data Segment |
| `static` (global) | File | Entire program | 0 | Data Segment |
| `extern` | Global | Entire program | 0 | Data Segment |

### The `static` Local Variable Trick

```c
void counter() {
    static int count = 0;  // Initialized ONCE, persists across calls
    count++;
    printf("%d ", count);
}

int main() {
    counter();  // 1
    counter();  // 2
    counter();  // 3
}
```

**Why?** `static` local variables are allocated in the **data segment** (not stack), so they survive function return. But their **scope** is still limited to the function block.

### 🔴 GATE Trap: Static vs Global

```c
// file1.c
static int x = 5;  // Visible ONLY in file1.c

// file2.c
extern int x;       // Linker ERROR: x has internal linkage
```

**Rule:** `static` at file scope gives **internal linkage** (file-private). `extern` gives **external linkage** (visible across files).

### `register` — The Misleading Keyword

```c
register int x = 10;
// int *p = &x;  // ERROR: cannot take address of register variable
```

**Key fact:** `register` is only a **hint** — the compiler may ignore it. The only guaranteed effect: you **cannot take its address** with `&`.

---

## 1.7 Preprocessor Directives

### Macro Pitfalls

```c
#define SQUARE(x) x*x
printf("%d", SQUARE(3+1));
// Expands to: 3+1*3+1 = 3+3+1 = 7 (NOT 16!)
```

**Fix:**
```c
#define SQUARE(x) ((x)*(x))
printf("%d", SQUARE(3+1));
// Expands to: ((3+1)*(3+1)) = 16
```

**Rule:** Always **parenthesize** every parameter AND the entire expression in macros.

### 🔴 GATE Trap: Macro Side Effects

```c
#define MAX(a, b) ((a) > (b) ? (a) : (b))
int x = 5, y = 3;
int z = MAX(x++, y++);
// Expands to: ((x++) > (y++) ? (x++) : (y++))
// x gets incremented TWICE if x > y!
printf("%d %d %d", x, y, z);  // 7 4 6
```

**Why?** Macros are **text substitution**, not function calls. Arguments with side effects get evaluated multiple times.

### `#` and `##` Operators

```c
#define STRINGIFY(x) #x
printf("%s", STRINGIFY(hello));  // Output: "hello"

#define CONCAT(a, b) a##b
int xy = 100;
printf("%d", CONCAT(x, y));     // Output: 100 (becomes variable xy)
```

### Conditional Compilation

```c
#ifdef DEBUG
    printf("Debug mode\n");
#endif

#ifndef HEADER_H
#define HEADER_H
// Header content (include guard)
#endif
```

---

## 1.8 Type Casting & Promotion

### Implicit Type Promotion Rules

In an expression with mixed types, C promotes to the **wider** type:

$$\text{char/short} \rightarrow \text{int} \rightarrow \text{unsigned int} \rightarrow \text{long} \rightarrow \text{float} \rightarrow \text{double}$$

```c
char c = 'A';        // c = 65
int result = c + 1;  // char promoted to int: 65 + 1 = 66
printf("%c", result); // Output: 'B'
```

### 🔴 GATE Trap: Signed vs Unsigned Comparison

```c
int a = -1;
unsigned int b = 1;
if (a > b)
    printf("Greater");  // This PRINTS! Because -1 is converted to
                         // unsigned (becomes very large: 4294967295)
```

**Rule:** When signed and unsigned are compared, the signed value is **implicitly converted to unsigned**. $-1$ in 2's complement = all 1s = $2^{32} - 1 = 4294967295$ as unsigned.

### Integer Division Truncation

```c
printf("%d", 7/2);      // 3 (truncated toward zero)
printf("%d", -7/2);     // -3 (truncated toward zero, C99+)
printf("%f", 7.0/2);    // 3.500000
printf("%f", (float)7/2); // 3.500000
```

---

## 1.9 `sizeof` Operator — Key Facts

```c
printf("%zu", sizeof(char));       // Always 1 (by definition)
printf("%zu", sizeof(int));        // 4 (typically)
printf("%zu", sizeof(int *));      // 8 (64-bit) or 4 (32-bit)
printf("%zu", sizeof(char *));     // 8 (same as above — all pointers same size)
printf("%zu", sizeof(void *));     // 8 (same)
```

**Critical GATE fact:** `sizeof` is a **compile-time** operator (except for VLAs). The expression inside is **never evaluated**:

```c
int x = 5;
printf("%zu", sizeof(x++));  // x is still 5! sizeof doesn't evaluate x++
printf("%d", x);             // Output: 5
```

---

## 1.10 Bitwise Operations

### Operations Table

| Op | Symbol | Example (8-bit) | Result |
|----|--------|-----------------|--------|
| AND | `&` | `0b1100 & 0b1010` | `0b1000` (8) |
| OR | `\|` | `0b1100 \| 0b1010` | `0b1110` (14) |
| XOR | `^` | `0b1100 ^ 0b1010` | `0b0110` (6) |
| NOT | `~` | `~0b00001100` | `0b11110011` (-13 in signed) |
| Left Shift | `<<` | `5 << 2` | `20` ($5 \times 2^2$) |
| Right Shift | `>>` | `20 >> 2` | `5` ($20 / 2^2$) |

### Key Bit Manipulation Formulas

$$x \ll k = x \times 2^k$$
$$x \gg k = \lfloor x / 2^k \rfloor \quad \text{(for unsigned or positive values)}$$

### Useful Bit Tricks

| Task | Expression | Why it works |
|------|-----------|-------------|
| Check if $n$ is even | `n & 1 == 0` | Last bit = 0 → even |
| Check if $n$ is power of 2 | `n > 0 && (n & (n-1)) == 0` | Power of 2 has exactly one set bit |
| Get $i$-th bit | `(n >> i) & 1` | Shift bit to position 0, mask others |
| Set $i$-th bit | `n \| (1 << i)` | OR with mask having only bit $i$ set |
| Clear $i$-th bit | `n & ~(1 << i)` | AND with mask having only bit $i$ cleared |
| Toggle $i$-th bit | `n ^ (1 << i)` | XOR flips the target bit |
| Count set bits | Brian Kernighan: `while(n) { n &= (n-1); count++; }` | Each iteration clears the lowest set bit |
| Swap without temp | `a ^= b; b ^= a; a ^= b;` | XOR is self-inverse |

### 🔴 GATE Trap: Right Shift of Negative Numbers

```c
int x = -8;
printf("%d", x >> 1);  // Implementation-defined! Could be -4 (arithmetic) or large positive (logical)
```

**Rule:** Right shift of negative signed integers is **implementation-defined**. Most compilers use **arithmetic shift** (preserves sign bit), but don't count on it in GATE unless specified.

---

## 1.11 `typedef` vs `#define`

```c
typedef int* IntPtr;
IntPtr a, b;          // Both a and b are int*

#define INTPTR int*
INTPTR a, b;          // Only a is int*, b is just int!
// Expands to: int *a, b;
```

**Rule:** `typedef` is a proper type alias (handled by compiler). `#define` is text substitution (handled by preprocessor). Always prefer `typedef` for type aliases.

---

## 1.12 `volatile` Keyword

```c
volatile int flag = 0;  // Tell compiler: this value can change unexpectedly
```

**Use case:** Hardware registers, signal handlers, multi-threaded shared variables. The compiler **will not optimize away** reads/writes to `volatile` variables.

**GATE context:** If asked "which keyword prevents compiler optimization of a variable?" → Answer: `volatile`.

---

## Summary: Quick-Fire GATE Facts for C Programming

1. `sizeof(char)` is **always 1** by definition.
2. All pointer types have the **same size** on a given platform.
3. `sizeof` does **not evaluate** its operand (except VLAs).
4. Signed integer overflow is **undefined behavior**.
5. Array passed to function **decays to pointer**.
6. `static` local: block scope + program lifetime.
7. Macros: always parenthesize parameters.
8. `switch` falls through without `break`.
9. `&&` and `||` are **short-circuit** evaluated.
10. `a[i]` is identical to `*(a + i)` is identical to `i[a]`.

---

> **5-Second Snap-Check for Output Questions:**
> 1. Is there undefined behavior? (sequence points, overflow) → UB
> 2. Is there a macro? → mentally expand it first
> 3. Is there pointer arithmetic? → multiply by `sizeof(type)`
> 4. Is there `sizeof`? → check if array decayed to pointer
