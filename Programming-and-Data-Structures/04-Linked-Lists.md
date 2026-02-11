# Part 4: Linked Lists

> **The Atomic Truth:** *Linked list = nodes connected by pointers; non-contiguous memory.*

---

## 4.1 Why Linked Lists?

| Feature | Array | Linked List |
|---------|-------|-------------|
| Memory | Contiguous, fixed at creation | Non-contiguous, dynamic |
| Access | $O(1)$ random access | $O(n)$ sequential access |
| Insert at beginning | $O(n)$ (shift all) | $O(1)$ |
| Insert at end | $O(1)$ (if space) / $O(n)$ (if resize) | $O(n)$ or $O(1)$ with tail pointer |
| Delete by value | $O(n)$ | $O(n)$ search + $O(1)$ delete |
| Memory overhead | None | Extra pointer per node |
| Cache performance | Excellent (locality) | Poor (scattered memory) |

**Analogy:** An array is like apartments in a building — numbered sequentially, easy to find by number. A linked list is like a treasure hunt — each clue tells you where the next one is.

---

## 4.2 Singly Linked List

### Node Structure

```c
struct Node {
    int data;
    struct Node *next;
};
```

**Memory layout:**
```
head → [10 | •→] → [20 | •→] → [30 | NULL]
```

### Core Operations

**Create a node:**
```c
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}
```

**Insert at beginning — $O(1)$:**
```c
void insertFront(struct Node **head, int data) {
    struct Node *newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
}
```

**Why double pointer (`**head`)?** Because we need to modify the `head` pointer itself. A single pointer would only modify a local copy.

**Insert at end — $O(n)$:**
```c
void insertEnd(struct Node **head, int data) {
    struct Node *newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    struct Node *temp = *head;
    while (temp->next != NULL)
        temp = temp->next;
    temp->next = newNode;
}
```

**Delete a node with given key — $O(n)$:**
```c
void deleteNode(struct Node **head, int key) {
    struct Node *temp = *head, *prev = NULL;
    
    // Head node holds the key
    if (temp != NULL && temp->data == key) {
        *head = temp->next;
        free(temp);
        return;
    }
    
    // Search for key
    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }
    
    if (temp == NULL) return;  // Key not found
    
    prev->next = temp->next;
    free(temp);
}
```

**Traverse — $O(n)$:**
```c
void printList(struct Node *head) {
    while (head != NULL) {
        printf("%d → ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}
```

### 🔴 GATE Trap: Counting Operations for Insert/Delete

To insert at position $k$ in a singly linked list:
- Pointer movements needed: $k - 1$ (to reach the node before position $k$)
- Pointer changes: **2** (newNode->next and prev->next)

To delete at position $k$:
- Pointer movements: $k - 1$
- Pointer changes: **1** (prev->next)
- Don't forget: `free()` the deleted node

---

## 4.3 Doubly Linked List

### Node Structure

```c
struct DNode {
    int data;
    struct DNode *prev;
    struct DNode *next;
};
```

**Memory layout:**
```
NULL ←[•|10|•→] ←→ [•|20|•→] ←→ [•|30|•]→ NULL
```

### Advantages over Singly Linked List

1. **Bidirectional traversal** — can go forward and backward
2. **$O(1)$ delete given a pointer** to the node (no need to find previous node)
3. **Easier reversal** — just swap prev and next pointers

### Delete Given Node Pointer — $O(1)$

```c
void deleteNode(struct DNode **head, struct DNode *del) {
    if (*head == del)
        *head = del->next;
    if (del->next != NULL)
        del->next->prev = del->prev;
    if (del->prev != NULL)
        del->prev->next = del->next;
    free(del);
}
```

**Key insight:** In a DLL, given a pointer to any node, you can delete it in $O(1)$ because you have access to both neighbors. In an SLL, you need $O(n)$ to find the previous node.

---

## 4.4 Circular Linked List

### Singly Circular

```c
// Last node points back to head
head → [10|•→] → [20|•→] → [30|•→] ──┐
  ↑                                     │
  └─────────────────────────────────────┘
```

**Detection of last node:** `temp->next == head` (not NULL)

### Doubly Circular

Every node has both prev and next pointers, and the list forms a complete circle in both directions.

### Use Cases

- **Round-robin scheduling** — processes arranged in a circle
- **Circular buffer** — media players, real-time data streams
- **Josephus problem**

### Josephus Problem

$n$ people in a circle, every $k$-th person is eliminated. Find the survivor.

**Recursive formula:**

$$J(n, k) = (J(n-1, k) + k) \bmod n$$

with $J(1, k) = 0$ (0-indexed).

```c
int josephus(int n, int k) {
    if (n == 1) return 0;
    return (josephus(n - 1, k) + k) % n;
}
// Add 1 for 1-indexed result
```

---

## 4.5 Classic Linked List Problems

### Reverse a Singly Linked List — Iterative $O(n)$

```c
struct Node* reverse(struct Node *head) {
    struct Node *prev = NULL, *curr = head, *next = NULL;
    while (curr != NULL) {
        next = curr->next;     // Save next
        curr->next = prev;     // Reverse link
        prev = curr;           // Advance prev
        curr = next;           // Advance curr
    }
    return prev;  // New head
}
```

**Mnemonic for the 3 steps:** "**S**ave, **R**everse, **A**dvance" — SRA (like a camera)

### Reverse — Recursive

```c
struct Node* reverseRecursive(struct Node *head) {
    if (head == NULL || head->next == NULL)
        return head;
    struct Node *rest = reverseRecursive(head->next);
    head->next->next = head;  // Make next node point back to current
    head->next = NULL;         // Remove forward link
    return rest;
}
```

### Detect Cycle — Floyd's Algorithm (Tortoise & Hare)

```c
int hasCycle(struct Node *head) {
    struct Node *slow = head, *fast = head;
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;         // Move 1 step
        fast = fast->next->next;   // Move 2 steps
        if (slow == fast) return 1; // Cycle detected
    }
    return 0;  // No cycle
}
```

**Why it works:** If there's a cycle, the fast pointer will eventually "lap" the slow pointer inside the cycle. If no cycle, fast hits NULL.

**Mathematical proof:** Once both are in the cycle of length $L$, the gap between them decreases by 1 each step. So they must meet within $L$ steps.

### Find Cycle Start Point

```c
struct Node* findCycleStart(struct Node *head) {
    struct Node *slow = head, *fast = head;
    
    // Phase 1: Detect cycle
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) break;
    }
    if (!fast || !fast->next) return NULL;  // No cycle
    
    // Phase 2: Find start
    slow = head;  // Reset slow to head
    while (slow != fast) {
        slow = slow->next;
        fast = fast->next;  // Both move 1 step
    }
    return slow;  // Meeting point = cycle start
}
```

**Why Phase 2 works (the math):**

Let:
- Distance from head to cycle start = $m$
- Distance from cycle start to meeting point = $k$
- Cycle length = $L$

At meeting: slow traveled $m + k$, fast traveled $m + k + nL$ (for some $n$).

Since fast moves 2× speed: $2(m + k) = m + k + nL$

$$m + k = nL \implies m = nL - k$$

So if we start one pointer at head and another at the meeting point, both moving 1 step at a time, they meet at the cycle start after $m$ steps.

### Merge Two Sorted Lists

```c
struct Node* mergeSorted(struct Node *a, struct Node *b) {
    if (!a) return b;
    if (!b) return a;
    
    if (a->data <= b->data) {
        a->next = mergeSorted(a->next, b);
        return a;
    } else {
        b->next = mergeSorted(a, b->next);
        return b;
    }
}
```

### Find Middle Element

```c
struct Node* findMiddle(struct Node *head) {
    struct Node *slow = head, *fast = head;
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;  // For even length: upper middle
}
```

**When fast reaches end, slow is at middle** (fast moves 2×, so slow covers half the distance).

### Find $n$-th Node from End

```c
struct Node* nthFromEnd(struct Node *head, int n) {
    struct Node *fast = head, *slow = head;
    for (int i = 0; i < n; i++)
        fast = fast->next;       // Move fast n steps ahead
    while (fast != NULL) {
        slow = slow->next;
        fast = fast->next;
    }
    return slow;
}
```

**Why it works:** Fast is $n$ steps ahead. When fast hits NULL, slow is $n$ steps behind NULL = $n$-th from end.

---

## 4.6 Linked List Sorting

### Merge Sort on Linked List — $O(n \log n)$

Preferred over Quick Sort for linked lists because:
1. No random access needed (merge sort only uses sequential access)
2. No extra space needed (unlike array merge sort which needs $O(n)$ auxiliary)

```c
struct Node* mergeSort(struct Node *head) {
    if (!head || !head->next) return head;
    
    struct Node *middle = findMiddle_prev(head);  // Find middle
    struct Node *secondHalf = middle->next;
    middle->next = NULL;  // Split
    
    struct Node *left = mergeSort(head);
    struct Node *right = mergeSort(secondHalf);
    
    return mergeSorted(left, right);
}
```

---

## 4.7 Memory & Pointer Questions — GATE Patterns

### Number of Pointer Changes

| Operation | SLL | DLL |
|----------|-----|-----|
| Insert at front | 2 changes | 3 changes |
| Insert at end | 2 changes | 3 changes |
| Insert after given node | 2 changes | 4 changes |
| Delete given node (pointer given) | Need prev → $O(n)$ | $O(1)$, 2-3 changes |

### Memory per Node

- **SLL node:** `sizeof(data) + sizeof(pointer)` = e.g., $4 + 8 = 12$ bytes (with padding maybe 16)
- **DLL node:** `sizeof(data) + 2 × sizeof(pointer)` = e.g., $4 + 16 = 20$ bytes (with padding maybe 24)

### 🔴 GATE Trap: XOR Linked List

A memory-efficient doubly linked list where each node stores `prev XOR next` instead of separate prev and next pointers.

```
npx(A) = NULL XOR addr(B) = addr(B)
npx(B) = addr(A) XOR addr(C)
npx(C) = addr(B) XOR addr(D)
```

To traverse forward from A→B→C: `next = npx(B) XOR addr(A) = addr(A) XOR addr(C) XOR addr(A) = addr(C)`

**Space:** One pointer per node instead of two.

---

## Summary: Quick-Fire GATE Facts for Linked Lists

1. SLL insert at front: $O(1)$, at end: $O(n)$ (without tail pointer).
2. DLL delete given node pointer: $O(1)$.
3. Floyd's cycle detection: slow (1 step) + fast (2 steps).
4. Cycle start: reset slow to head, move both by 1.
5. Finding middle: slow-fast pointer technique.
6. Merge Sort is preferred over Quick Sort for linked lists.
7. Reverse SLL needs 3 pointers: prev, curr, next.
8. Double pointer (`**head`) needed when head itself might change.
9. Josephus: $J(n,k) = (J(n-1,k) + k) \bmod n$.
10. XOR linked list: one pointer field, stores prev⊕next.

---

> **5-Second Snap-Check for Linked List Questions:**
> 1. Does the operation change head? → Need double pointer
> 2. Is it about cycle detection? → Floyd's (tortoise & hare)
> 3. Is it about finding position? → Two-pointer technique
> 4. Count pointer changes, not just time complexity
