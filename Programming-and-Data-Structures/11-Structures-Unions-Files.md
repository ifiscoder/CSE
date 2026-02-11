# Part 11: Structures, Unions & File Handling

> **The Atomic Truth:** *struct groups different types; union overlaps them.*

---

## 11.1 Structures (`struct`)

### Definition & Declaration

```c
struct Student {
    int id;         // 4 bytes
    char name[20];  // 20 bytes
    float gpa;      // 4 bytes
};

// Declaration
struct Student s1 = {101, "Alice", 9.5};

// Access
printf("%d %s %.1f", s1.id, s1.name, s1.gpa);
```

### Memory Layout & Padding

**Structure padding:** The compiler inserts **padding bytes** to align members on their natural boundaries (for performance).

**Alignment rule:** Each member is aligned to an address that is a multiple of its size (or the platform's alignment requirement).

```c
struct Example {
    char a;     // 1 byte + 3 padding bytes
    int b;      // 4 bytes (aligned to 4-byte boundary)
    char c;     // 1 byte + 3 padding bytes (struct padded to multiple of max alignment)
};
// sizeof(struct Example) = 12 (NOT 6!)
```

**Why padding?** CPU accesses aligned data faster. Unaligned access may require two memory reads.

### Minimizing Padding — Order Members by Size

```c
struct Optimized {
    int b;      // 4 bytes
    char a;     // 1 byte
    char c;     // 1 byte + 2 padding bytes
};
// sizeof(struct Optimized) = 8 (saved 4 bytes!)
```

**Rule of thumb:** Declare members in **decreasing order of size** to minimize padding.

### 🔴 GATE Trap: `sizeof` with Structures

```c
struct A {
    char c;     // 1 + 7 padding (to align double)
    double d;   // 8
    int i;      // 4 + 4 padding (total struct aligned to 8)
};
// sizeof(struct A) = 24 (on 64-bit system)

struct B {
    double d;   // 8
    int i;      // 4
    char c;     // 1 + 3 padding (total struct aligned to 8)
};
// sizeof(struct B) = 16
```

**Same members, different order, different size!** GATE frequently tests this.

### Bit Fields

```c
struct Flags {
    unsigned int bold   : 1;  // 1 bit
    unsigned int italic : 1;  // 1 bit
    unsigned int underl : 1;  // 1 bit
    unsigned int size   : 5;  // 5 bits (values 0-31)
};
// Total: 8 bits = 1 byte (but may be padded to 4 bytes)
```

**Rules for bit fields:**
1. Cannot take address of bit field (`&` operator is illegal)
2. Cannot create arrays of bit fields
3. Total bits can't exceed the declared type's width
4. Unnamed bit fields (`: 0`) force alignment to next unit boundary

---

## 11.2 Nested Structures & Self-Referential Structures

### Nested Structures

```c
struct Date {
    int day, month, year;
};

struct Employee {
    char name[50];
    struct Date dob;      // Nested structure
    struct Date joining;
};

struct Employee e1 = {"Bob", {15, 3, 1990}, {1, 6, 2020}};
printf("%d", e1.dob.year);  // 1990
```

### Self-Referential Structure (Used in Linked Lists, Trees)

```c
struct Node {
    int data;
    struct Node *next;  // Pointer to same type (OK)
    // struct Node next; // ERROR: incomplete type (infinite size)
};
```

**Why pointer works but value doesn't?** A pointer has a fixed size (8 bytes on 64-bit), regardless of what it points to. A value would require knowing the full size, which creates infinite recursion.

---

## 11.3 `typedef` with Structures

```c
typedef struct Node {
    int data;
    struct Node *next;  // Must use "struct Node" inside definition
} Node;

// Now can use:
Node *head = NULL;  // Instead of "struct Node *head"
```

### 🔴 GATE Trap: Forward Declaration

```c
typedef struct {
    int data;
    // Node *next;       // ERROR: "Node" not yet defined at this point!
    struct Node *next;   // This would be a DIFFERENT type!
} Node;
```

**Safe pattern:** Always use the struct tag for self-references:
```c
typedef struct Node {
    int data;
    struct Node *next;  // Uses the struct tag, not the typedef
} Node;
```

---

## 11.4 Unions

### Definition

A union allocates memory for the **largest member only**. All members share the same memory.

```c
union Data {
    int i;      // 4 bytes
    float f;    // 4 bytes
    char str[20]; // 20 bytes
};
// sizeof(union Data) = 20 (size of largest member)

union Data d;
d.i = 42;
printf("%d", d.i);    // 42
d.f = 3.14;
printf("%d", d.i);    // Garbage! (memory reinterpreted)
```

**Analogy:** A union is like a **hotel room** that can be configured as a single, double, or suite — but only one configuration at a time. A struct is like **three separate rooms** booked simultaneously.

### Union vs Structure

| Feature | `struct` | `union` |
|---------|----------|---------|
| Memory | Sum of all members (+ padding) | Size of largest member |
| Members | All exist simultaneously | Only one active at a time |
| Accessing | Any member anytime | Only last-written member is valid |
| Use case | Group related data | Memory-efficient variant types |

### 🔴 GATE Trap: Type Punning with Unions

```c
union IntFloat {
    int i;
    float f;
};

union IntFloat u;
u.f = 3.14f;
printf("%d", u.i);  // Prints the bit pattern of 3.14 interpreted as int
                     // (1078523331 on most systems)
```

**This is a common GATE question type:** "What is the output?" The answer requires understanding how the same bits are interpreted differently by different types.

### Checking Endianness Using Union

```c
union Endian {
    int i;
    char c;
};

union Endian e;
e.i = 1;
if (e.c == 1)
    printf("Little Endian");  // LSB stored at lowest address
else
    printf("Big Endian");
```

---

## 11.5 Enumerations (`enum`)

```c
enum Color { RED, GREEN, BLUE };        // RED=0, GREEN=1, BLUE=2
enum Color c = GREEN;
printf("%d", c);                         // 1

enum Priority { LOW = 1, MEDIUM = 5, HIGH = 10 };
printf("%d", HIGH);                      // 10
```

**Key facts:**
1. Enum values are **integers** (type `int`)
2. Default: first = 0, subsequent = previous + 1
3. Can assign explicit values
4. Duplicate values are allowed
5. `sizeof(enum)` = `sizeof(int)` (typically 4)

---

## 11.6 File Handling in C

### File Operations Overview

```c
#include <stdio.h>

FILE *fp;

// Open
fp = fopen("file.txt", "r");   // Open for reading
if (fp == NULL) {
    perror("Error opening file");
    return 1;
}

// Read/Write operations...

// Close
fclose(fp);
```

### File Opening Modes

| Mode | Description | File exists | File doesn't exist |
|------|------------|------------|-------------------|
| `"r"` | Read | Opens | Returns NULL |
| `"w"` | Write | **Truncates** | Creates |
| `"a"` | Append | Opens (writes at end) | Creates |
| `"r+"` | Read + Write | Opens | Returns NULL |
| `"w+"` | Read + Write | **Truncates** | Creates |
| `"a+"` | Read + Append | Opens | Creates |

Add `"b"` suffix for binary mode: `"rb"`, `"wb"`, etc.

### 🔴 GATE Trap: `"w"` Mode Destroys Existing Content

```c
fp = fopen("data.txt", "w");  // If data.txt exists, its content is ERASED!
```

This is a very common mistake. If you want to add content without erasing, use `"a"` (append).

### Character I/O

```c
// Write
fputc('A', fp);

// Read
int ch = fgetc(fp);  // Returns int (to accommodate EOF)
// EOF is typically -1
```

**Why `fgetc` returns `int`, not `char`?** To distinguish `EOF` (-1) from a valid character (especially `0xFF` which as `char` would be -1 on signed-char systems).

### String I/O

```c
// Write
fputs("Hello\n", fp);

// Read (reads until newline or n-1 characters)
char buffer[100];
fgets(buffer, 100, fp);  // Safe: reads at most 99 chars + '\0'
```

### Formatted I/O

```c
// Write
fprintf(fp, "Name: %s, Age: %d\n", name, age);

// Read
fscanf(fp, "%s %d", name, &age);
```

### Binary I/O

```c
// Write n elements of size sizeof(int) from array to file
fwrite(arr, sizeof(int), n, fp);

// Read n elements of size sizeof(int) from file to array
size_t count = fread(arr, sizeof(int), n, fp);
```

**`fread` returns** the number of items successfully read (may be less than $n$ if EOF reached).

### File Positioning

```c
fseek(fp, offset, origin);
// origin: SEEK_SET (beginning), SEEK_CUR (current), SEEK_END (end)

long pos = ftell(fp);  // Current position

rewind(fp);  // Reset to beginning (equivalent to fseek(fp, 0, SEEK_SET))
```

### 🔴 GATE Trap: File Size Calculation

```c
fseek(fp, 0, SEEK_END);
long size = ftell(fp);
rewind(fp);
printf("File size: %ld bytes", size);
```

"How many records of type `struct Student` (size 48 bytes) can be stored in a file of 1000 bytes?"

Answer: $\lfloor 1000 / 48 \rfloor = 20$ records (with 40 bytes unused).

---

## 11.7 Dynamic Memory Allocation

### The Four Functions (from `<stdlib.h>`)

| Function | Purpose | Returns |
|----------|---------|---------|
| `malloc(size)` | Allocate `size` bytes (uninitialized) | `void *` or NULL |
| `calloc(n, size)` | Allocate `n × size` bytes (**zero-initialized**) | `void *` or NULL |
| `realloc(ptr, new_size)` | Resize previously allocated block | `void *` or NULL |
| `free(ptr)` | Deallocate memory | void |

```c
// malloc
int *arr = (int *)malloc(n * sizeof(int));
if (arr == NULL) { /* allocation failed */ }

// calloc — all elements initialized to 0
int *arr = (int *)calloc(n, sizeof(int));

// realloc — may move the block
arr = (int *)realloc(arr, 2 * n * sizeof(int));

// free
free(arr);
arr = NULL;  // Good practice: prevent dangling pointer
```

### `malloc` vs `calloc`

| Feature | `malloc` | `calloc` |
|---------|----------|----------|
| Parameters | Total bytes | Count × size |
| Initialization | **No** (garbage) | **Yes** (zeros) |
| Speed | Slightly faster | Slightly slower (zeroing) |
| Overflow check | No | Yes (checks `n × size` overflow) |

### Common Memory Errors

| Error | Description |
|-------|------------|
| **Memory leak** | Allocated memory never freed |
| **Dangling pointer** | Pointer to freed memory |
| **Double free** | Freeing same memory twice |
| **Buffer overflow** | Writing beyond allocated bounds |
| **Use after free** | Accessing freed memory |
| **Wild pointer** | Uninitialized pointer |

### 🔴 GATE Trap: `realloc` Behavior

```c
int *p = (int *)malloc(5 * sizeof(int));
int *q = (int *)realloc(p, 10 * sizeof(int));
```

**Three possible outcomes:**
1. Block extended in place → `q == p`
2. New block allocated, old data copied, old block freed → `q != p`, `p` is now dangling
3. Allocation failed → `q == NULL`, `p` is still valid (don't lose it!)

**Safe pattern:**
```c
int *temp = realloc(p, new_size);
if (temp != NULL)
    p = temp;
else
    // Handle failure, p still valid
```

---

## 11.8 Command Line Arguments

```c
int main(int argc, char *argv[]) {
    // argc = argument count (including program name)
    // argv[0] = program name
    // argv[1], argv[2], ... = arguments
    // argv[argc] = NULL
    
    printf("Program: %s\n", argv[0]);
    for (int i = 1; i < argc; i++)
        printf("Arg %d: %s\n", i, argv[i]);
    return 0;
}
```

**Running:** `./program hello 42`

```
argc = 3
argv[0] = "./program"
argv[1] = "hello"
argv[2] = "42"
argv[3] = NULL
```

**Note:** All arguments are **strings**. Use `atoi()`, `atof()` etc. to convert.

---

## 11.9 Variable Length Arguments (`<stdarg.h>`)

```c
#include <stdarg.h>

double average(int count, ...) {
    va_list args;
    va_start(args, count);     // Initialize
    
    double sum = 0;
    for (int i = 0; i < count; i++)
        sum += va_arg(args, double);  // Get next argument
    
    va_end(args);               // Cleanup
    return sum / count;
}

// Usage:
double avg = average(3, 1.0, 2.0, 3.0);  // 2.0
```

---

## Summary: Quick-Fire GATE Facts for Structures, Unions & Files

1. `sizeof(struct)` ≥ sum of member sizes (due to **padding**).
2. Order members by decreasing size to **minimize padding**.
3. `sizeof(union)` = size of **largest member**.
4. Union: only **last written member** is valid.
5. `malloc` → garbage; `calloc` → zeros.
6. `realloc` may move the block — **always use a temp pointer**.
7. `fgetc` returns `int`, not `char` (to distinguish EOF).
8. `"w"` mode **truncates** existing files.
9. Self-referential struct: use **pointer** (not value) to same type.
10. Bit fields: cannot use `&` operator on them.
11. `sizeof` on struct with bit fields rounds up to alignment.
12. `free(NULL)` is safe (does nothing). Double `free` is **undefined**.

---

> **5-Second Snap-Check for struct/union Questions:**
> 1. `sizeof` question? → Draw memory layout with padding
> 2. Union output? → Check which member was last written
> 3. File question? → Check the mode (`"w"` destroys, `"a"` appends)
> 4. Dynamic memory? → Check for leaks, dangling pointers, double free
