# Part 2: Arrays & Strings

> **The Atomic Truth:** *Array = contiguous memory; name = base address.*

---

## 2.1 Array Fundamentals

### Memory Layout

An array `int arr[5] = {10, 20, 30, 40, 50}` with base address 1000:

```
Address:  1000    1004    1008    1012    1016
Value:    [10]    [20]    [30]    [40]    [50]
Index:     0       1       2       3       4
```

**Formula for address of `arr[i]`:**

$$\text{Address}(arr[i]) = \text{Base} + i \times \text{sizeof(element)}$$

**Why?** Elements are stored contiguously. The $i$-th element is $i$ elements away from the base, each occupying `sizeof(element)` bytes.

### Array Declaration & Initialization

```c
int arr[5] = {1, 2, 3};       // arr = {1, 2, 3, 0, 0} (remaining = 0)
int arr[] = {1, 2, 3, 4, 5};  // Size inferred = 5
int arr[5] = {0};              // All zeros
int arr[5];                    // GARBAGE values (if local)
```

**GATE fact:** Partially initialized arrays have remaining elements set to **0** (not garbage).

### Array Name vs Pointer

```c
int arr[5];
int *p = arr;

// Similarities:
arr[2] == *(arr + 2) == *(p + 2) == p[2]  // All equivalent

// Differences:
sizeof(arr) == 20  // Total array size (5 × 4)
sizeof(p) == 8     // Pointer size

// arr++;    // ERROR: array name is NOT a modifiable lvalue
p++;         // OK: pointer can be modified
```

**Analogy:** An array name is like your **home address printed on a legal document** — it refers to a location but you can't change it. A pointer is like a **GPS coordinate on your phone** — you can point it anywhere.

---

## 2.2 2-D Arrays

### Memory Layout (Row-Major Order — C default)

For `int arr[3][4]`:

$$\text{Address}(arr[i][j]) = \text{Base} + (i \times \text{cols} + j) \times \text{sizeof(element)}$$

**Derivation:** In row-major, elements are stored row by row. To reach row $i$, skip $i$ complete rows (each has `cols` elements). Then add $j$ for the column offset.

```
Logical View:          Memory Layout (row-major):
[0][0] [0][1] [0][2] [0][3]    → [0][0] [0][1] [0][2] [0][3] [1][0] [1][1] ...
[1][0] [1][1] [1][2] [1][3]
[2][0] [2][1] [2][2] [2][3]
```

### Column-Major Order (Fortran style — asked in GATE)

$$\text{Address}(arr[i][j]) = \text{Base} + (j \times \text{rows} + i) \times \text{sizeof(element)}$$

### General n-D Array Address (Row-Major)

For array $A[d_1][d_2]...[d_n]$, element $A[i_1][i_2]...[i_n]$:

$$\text{Address} = \text{Base} + \left(\sum_{k=1}^{n} i_k \times \prod_{m=k+1}^{n} d_m\right) \times \text{sizeof(element)}$$

### 🔴 GATE Trap: 2-D Array and Pointers

```c
int arr[3][4];
```

| Expression | Type | Value |
|-----------|------|-------|
| `arr` | `int (*)[4]` (pointer to array of 4 ints) | Base address |
| `arr[0]` | `int *` (pointer to int) | Base address |
| `arr[0][0]` | `int` | First element |
| `&arr` | `int (*)[3][4]` (pointer to entire 2D array) | Base address |
| `arr + 1` | `int (*)[4]` | Base + 16 (skips one row of 4 ints) |
| `arr[0] + 1` | `int *` | Base + 4 (skips one int) |

**Key insight:** `arr`, `arr[0]`, and `&arr` all have the **same numeric value** (the base address), but they have **different types**, so pointer arithmetic on them moves by different amounts.

**Example:**
```c
int arr[3][4];  // Base = 1000
// arr + 1     → 1000 + 1×(4×4) = 1016  (moves by one row)
// arr[0] + 1  → 1000 + 1×4 = 1004      (moves by one element)
// &arr + 1    → 1000 + 1×(3×4×4) = 1048 (moves by entire array)
```

### Passing 2-D Arrays to Functions

```c
// Method 1: Specify column size
void func(int arr[][4], int rows) { }

// Method 2: Pointer to array
void func(int (*arr)[4], int rows) { }

// Method 3: VLA (C99)
void func(int rows, int cols, int arr[rows][cols]) { }
```

**Rule:** When passing a 2-D array, you **must specify all dimensions except the first**.

---

## 2.3 Strings in C

### String = char array + null terminator `'\0'`

```c
char str1[] = "Hello";          // Size = 6 (5 chars + '\0')
char str2[] = {'H','e','l','l','o','\0'};  // Same as above
char str3[5] = "Hello";         // NO '\0'! NOT a valid string!
char *str4 = "Hello";           // String literal (read-only memory)
```

**Critical distinction:**
```c
char arr[] = "Hello";   // Array on stack — MODIFIABLE
char *ptr = "Hello";    // Pointer to string literal — READ-ONLY
arr[0] = 'J';           // OK: "Jello"
// ptr[0] = 'J';        // UNDEFINED BEHAVIOR (modifying read-only memory)
```

### Standard String Functions (from `<string.h>`)

| Function | Purpose | Returns | Edge Case |
|----------|---------|---------|-----------|
| `strlen(s)` | Length (excluding `'\0'`) | `size_t` | Empty string → 0 |
| `strcpy(dest, src)` | Copy src to dest | dest pointer | No bounds check! |
| `strncpy(dest, src, n)` | Copy at most n chars | dest pointer | May NOT null-terminate |
| `strcat(dest, src)` | Append src to dest | dest pointer | dest must have space |
| `strcmp(s1, s2)` | Compare lexicographically | <0, 0, >0 | Case-sensitive |
| `strchr(s, c)` | Find first occurrence of c | pointer or NULL | `'\0'` is valid to search |
| `strstr(s, sub)` | Find substring | pointer or NULL | Empty sub → returns s |

### 🔴 GATE Trap: `strlen` vs `sizeof`

```c
char str[] = "Hello";
printf("%zu", strlen(str));   // 5 (doesn't count '\0')
printf("%zu", sizeof(str));   // 6 (counts '\0')

char *ptr = "Hello";
printf("%zu", strlen(ptr));   // 5
printf("%zu", sizeof(ptr));   // 8 (pointer size, NOT string length!)
```

### String to Number Conversions

```c
#include <stdlib.h>
int n = atoi("123");        // n = 123
double d = atof("3.14");    // d = 3.14
long l = strtol("FF", NULL, 16);  // l = 255 (hex to long)
```

---

## 2.4 Pointer Arithmetic with Arrays — Deep Dive

### The `arr[i]` Identity

$$arr[i] \equiv *(arr + i) \equiv *(i + arr) \equiv i[arr]$$

This is because `[]` is defined as: `E1[E2] ≡ *((E1) + (E2))`

```c
int arr[] = {10, 20, 30, 40, 50};
printf("%d", 3[arr]);  // 40 — perfectly valid C!
```

### Pointer Subtraction

```c
int arr[] = {10, 20, 30, 40, 50};
int *p1 = &arr[1];
int *p2 = &arr[4];
printf("%ld", p2 - p1);  // 3 (number of elements, NOT bytes)
```

**Formula:** If `p1` and `p2` point into the same array:

$$p2 - p1 = \frac{\text{address}(p2) - \text{address}(p1)}{\text{sizeof(element)}}$$

### 🔴 GATE Trap: Pointer to Array Arithmetic

```c
int arr[5] = {1, 2, 3, 4, 5};
int (*p)[5] = &arr;        // p is pointer to entire array of 5 ints
printf("%d", *(*p + 2));   // 3

// p + 1 moves by sizeof(int[5]) = 20 bytes!
// *p gives you the base of the array (type int*)
// *p + 2 moves by 2*sizeof(int) = 8 bytes
```

---

## 2.5 Common Array Algorithms for GATE

### Finding Duplicates

```c
// In array of n numbers where elements are in range [0, n-1]
// Time: O(n), Space: O(1)
for (int i = 0; i < n; i++) {
    int idx = abs(arr[i]);
    if (arr[idx] < 0)
        printf("Duplicate: %d\n", idx);
    else
        arr[idx] = -arr[idx];
}
```

**Why it works:** Use the array itself as a hash table. Mark visited indices by negating. If already negative → duplicate.

### Kadane's Algorithm (Maximum Subarray Sum)

```c
int maxSubarraySum(int arr[], int n) {
    int max_ending = 0, max_so_far = INT_MIN;
    for (int i = 0; i < n; i++) {
        max_ending += arr[i];
        if (max_ending > max_so_far)
            max_so_far = max_ending;
        if (max_ending < 0)
            max_ending = 0;
    }
    return max_so_far;
}
// Time: O(n), Space: O(1)
```

**Intuition:** Keep a running sum. If it goes negative, reset — no point carrying negative baggage into future sums.

---

## 2.6 Matrix Operations — Quick Reference

### Transpose

```c
for (int i = 0; i < n; i++)
    for (int j = i + 1; j < n; j++)  // j starts from i+1 (upper triangle only)
        swap(&arr[i][j], &arr[j][i]);
```

### Spiral Order Traversal

Direction pattern: Right → Down → Left → Up → repeat

Maintain 4 boundaries: `top`, `bottom`, `left`, `right`.

---

## Summary: Quick-Fire GATE Facts for Arrays & Strings

1. Array name is a **constant pointer** to the first element (not a variable).
2. 2-D array address (row-major): $\text{Base} + (i \times \text{cols} + j) \times \text{sizeof(element)}$
3. `arr`, `&arr[0]`, `&arr` — same address, **different types**.
4. `strlen` excludes `'\0'`; `sizeof` includes it (for char arrays).
5. `char *s = "hello"` → string literal is **read-only**.
6. Pointer subtraction gives **element count**, not byte count.
7. Partially initialized array: remaining elements = **0**.
8. `strncpy` may **NOT** null-terminate the destination.

---

> **5-Second Snap-Check for Array Questions:**
> 1. Is the question about address? → Use address formula, check row-major vs column-major
> 2. Is `sizeof` involved? → Check if array decayed to pointer
> 3. Is it a string literal via pointer? → It's read-only
> 4. Pointer arithmetic → multiply offset by sizeof(type)
