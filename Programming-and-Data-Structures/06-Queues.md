# Part 6: Queues

> **The Atomic Truth:** *Queue = FIFO: First In, First Out.*

---

## 6.1 Queue Concept & Operations

A queue is a linear data structure where insertion happens at the **rear** and deletion at the **front**.

**Analogy:** A queue at a ticket counter — first person in line gets served first.

### Core Operations — All $O(1)$

| Operation | Description |
|-----------|------------|
| `enqueue(x)` | Insert element at rear |
| `dequeue()` | Remove and return front element |
| `front()/peek()` | Return front element without removing |
| `isEmpty()` | Check if queue is empty |
| `isFull()` | Check if queue is full |

---

## 6.2 Array Implementation (Linear Queue)

```c
#define MAX 100
struct Queue {
    int arr[MAX];
    int front, rear;
};

void init(struct Queue *q) { q->front = q->rear = -1; }

int isEmpty(struct Queue *q) { return q->front == -1; }

int isFull(struct Queue *q) { return q->rear == MAX - 1; }

void enqueue(struct Queue *q, int x) {
    if (isFull(q)) { printf("Overflow\n"); return; }
    if (q->front == -1) q->front = 0;
    q->arr[++(q->rear)] = x;
}

int dequeue(struct Queue *q) {
    if (isEmpty(q)) { printf("Underflow\n"); return -1; }
    int val = q->arr[q->front];
    if (q->front == q->rear)
        q->front = q->rear = -1;  // Queue became empty
    else
        q->front++;
    return val;
}
```

**Problem with linear queue:** Even after dequeuing, the front space is wasted. After several enqueue/dequeue operations, the queue appears full but has unused space at the front.

**Solution:** Circular Queue.

---

## 6.3 Circular Queue

### The Key Idea

Use modular arithmetic to wrap around:

$$\text{next position} = (\text{current} + 1) \bmod \text{MAX}$$

```c
struct CircularQueue {
    int arr[MAX];
    int front, rear;
    int size;  // Track number of elements
};

void init(struct CircularQueue *q) {
    q->front = 0;
    q->rear = -1;
    q->size = 0;
}

int isEmpty(struct CircularQueue *q) { return q->size == 0; }

int isFull(struct CircularQueue *q) { return q->size == MAX; }

void enqueue(struct CircularQueue *q, int x) {
    if (isFull(q)) { printf("Overflow\n"); return; }
    q->rear = (q->rear + 1) % MAX;
    q->arr[q->rear] = x;
    q->size++;
}

int dequeue(struct CircularQueue *q) {
    if (isEmpty(q)) { printf("Underflow\n"); return -1; }
    int val = q->arr[q->front];
    q->front = (q->front + 1) % MAX;
    q->size--;
    return val;
}
```

### Alternative: Without Size Variable

Without a separate `size` counter, we sacrifice **one slot** to distinguish full from empty:

- **Empty:** `front == (rear + 1) % MAX` (or use a flag)
- **Full:** `(rear + 2) % MAX == front` → wastes one slot

OR more commonly:
- **Empty:** `front == rear` (both point to same empty slot)
- **Full:** `(rear + 1) % MAX == front`
- **Capacity:** $\text{MAX} - 1$ elements (one slot wasted)

### 🔴 GATE Trap: Circular Queue Conditions

| Method | Empty Condition | Full Condition | Max Elements |
|--------|----------------|----------------|-------------|
| With size counter | `size == 0` | `size == MAX` | MAX |
| Without (waste 1 slot) | `front == rear` | `(rear + 1) % MAX == front` | MAX - 1 |

**GATE commonly asks:** "In a circular queue of size $n$, what is the maximum number of elements?" → $n - 1$ (if no size counter) or $n$ (with size counter).

### Number of Elements in Circular Queue

$$\text{count} = (\text{rear} - \text{front} + \text{MAX}) \bmod \text{MAX}$$

(When front = 0 and rear points to last element. Exact formula depends on implementation convention.)

---

## 6.4 Linked List Implementation

```c
struct Node {
    int data;
    struct Node *next;
};

struct Queue {
    struct Node *front, *rear;
};

void init(struct Queue *q) { q->front = q->rear = NULL; }

void enqueue(struct Queue *q, int data) {
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    if (q->rear == NULL) {
        q->front = q->rear = newNode;
        return;
    }
    q->rear->next = newNode;
    q->rear = newNode;
}

int dequeue(struct Queue *q) {
    if (q->front == NULL) { printf("Underflow\n"); return -1; }
    struct Node *temp = q->front;
    int data = temp->data;
    q->front = q->front->next;
    if (q->front == NULL)
        q->rear = NULL;  // Queue became empty
    free(temp);
    return data;
}
```

---

## 6.5 Double-Ended Queue (Deque)

A deque allows insertion and deletion at **both ends**.

### Types

| Type | Insert Front | Insert Rear | Delete Front | Delete Rear |
|------|-------------|-------------|-------------|-------------|
| **Input-restricted deque** | ❌ | ✅ | ✅ | ✅ |
| **Output-restricted deque** | ✅ | ✅ | ✅ | ❌ |
| **General deque** | ✅ | ✅ | ✅ | ✅ |

**Key fact:** A deque can implement both a stack AND a queue:
- As a stack: insert and delete from the same end
- As a queue: insert at one end, delete at the other

---

## 6.6 Priority Queue

Elements have **priorities**. Dequeue always removes the element with the **highest priority** (or lowest, depending on convention).

### Implementations

| Implementation | Enqueue | Dequeue (remove min/max) |
|---------------|---------|--------------------------|
| Unsorted array | $O(1)$ | $O(n)$ |
| Sorted array | $O(n)$ | $O(1)$ |
| Unsorted linked list | $O(1)$ | $O(n)$ |
| Sorted linked list | $O(n)$ | $O(1)$ |
| **Binary Heap** | $O(\log n)$ | $O(\log n)$ |
| **Balanced BST** | $O(\log n)$ | $O(\log n)$ |

**Binary Heap is the standard implementation** — both operations in $O(\log n)$.

(Detailed in Trees chapter.)

---

## 6.7 Queue Using Two Stacks

### Method 1: Make Enqueue Costly — $O(n)$ enqueue, $O(1)$ dequeue

```c
// Enqueue: move all from s1 to s2, push to s1, move all back
void enqueue(Stack *s1, Stack *s2, int x) {
    while (!isEmpty(s1))
        push(s2, pop(s1));
    push(s1, x);
    while (!isEmpty(s2))
        push(s1, pop(s2));
}

int dequeue(Stack *s1) {
    return pop(s1);
}
```

### Method 2: Make Dequeue Costly — $O(1)$ enqueue, Amortized $O(1)$ dequeue

```c
void enqueue(Stack *s1, int x) {
    push(s1, x);  // Always push to s1
}

int dequeue(Stack *s1, Stack *s2) {
    if (isEmpty(s2)) {
        while (!isEmpty(s1))
            push(s2, pop(s1));  // Transfer only when s2 is empty
    }
    return pop(s2);
}
```

**Why amortized $O(1)$?** Each element is pushed and popped from each stack **at most once**. Over $n$ operations, total work = $O(n)$, so per-operation = $O(1)$ amortized.

### 🔴 GATE Trap: Stack Using Two Queues

Push: $O(n)$ or $O(1)$ depending on method.

**Method (make push costly):**
```c
void push(Queue *q1, Queue *q2, int x) {
    enqueue(q2, x);
    while (!isEmpty(q1))
        enqueue(q2, dequeue(q1));
    // Swap q1 and q2
    Queue *temp = q1; q1 = q2; q2 = temp;
}

int pop(Queue *q1) {
    return dequeue(q1);
}
```

---

## 6.8 Queue Applications

1. **BFS (Breadth-First Search)** — level-order traversal of graphs and trees
2. **CPU Scheduling** — Round Robin uses a circular queue
3. **Print queue** — jobs processed in order
4. **Sliding window maximum** — use deque
5. **Cache implementation (LRU)** — queue + hash map

### Sliding Window Maximum (using Deque)

For each window of size $k$, find the maximum element.

```c
// Store indices in deque, maintaining decreasing order of values
void slidingMax(int arr[], int n, int k) {
    Deque dq;
    init(&dq);
    
    for (int i = 0; i < n; i++) {
        // Remove elements outside window
        while (!isEmpty(&dq) && front(&dq) <= i - k)
            removeFront(&dq);
        
        // Remove smaller elements from rear (they'll never be max)
        while (!isEmpty(&dq) && arr[rear(&dq)] <= arr[i])
            removeRear(&dq);
        
        insertRear(&dq, i);
        
        if (i >= k - 1)
            printf("%d ", arr[front(&dq)]);
    }
}
// Time: O(n), Space: O(k)
```

---

## 6.9 Generating Binary Numbers 1 to $n$

**Elegant queue application:**

```c
void generateBinary(int n) {
    Queue q;
    init(&q);
    enqueue(&q, "1");
    
    for (int i = 0; i < n; i++) {
        char *front = dequeue(&q);
        printf("%s\n", front);
        enqueue(&q, concat(front, "0"));
        enqueue(&q, concat(front, "1"));
    }
}
// Output for n=5: 1, 10, 11, 100, 101
```

**Why it works:** Each number generates two children by appending 0 and 1. This is essentially a level-order traversal of a binary tree.

---

## Summary: Quick-Fire GATE Facts for Queues

1. Queue = FIFO. Enqueue at rear, dequeue at front.
2. Circular queue: next position = $(i + 1) \bmod n$.
3. Circular queue (no size counter): max elements = $n - 1$.
4. Queue using 2 stacks: amortized $O(1)$ for both operations (Method 2).
5. Deque can simulate both stack and queue.
6. Priority queue best implemented with a **binary heap**.
7. BFS uses a queue; DFS uses a stack.
8. Input-restricted deque: no front insertion. Output-restricted: no rear deletion.

---

> **5-Second Snap-Check for Queue Questions:**
> 1. Is it circular? → Remember modular arithmetic and the "one slot waste" issue
> 2. Is it about implementation using stacks? → Method 2 gives amortized $O(1)$
> 3. Is it a deque? → Check which operations are restricted
> 4. Priority queue implementation? → Binary heap = $O(\log n)$ both operations
