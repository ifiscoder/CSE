# Part 7: Trees

> **The Atomic Truth:** *Tree = hierarchical structure; each node has at most one parent.*

---

## 7.1 Tree Fundamentals

### Terminology

| Term | Definition |
|------|-----------|
| **Root** | The topmost node (no parent) |
| **Leaf** | A node with no children (degree 0) |
| **Internal node** | A node with at least one child |
| **Depth of node** | Number of edges from root to that node |
| **Height of tree** | Maximum depth of any node (or edges on longest root-to-leaf path) |
| **Level** | Depth + 1 (sometimes used interchangeably with depth) |
| **Degree of node** | Number of children |
| **Degree of tree** | Maximum degree among all nodes |
| **Siblings** | Nodes sharing the same parent |
| **Ancestor** | Any node on the path from root to that node |
| **Descendant** | Any node in the subtree rooted at that node |

### Key Properties

For a tree with $n$ nodes:
- **Number of edges** = $n - 1$

**Why?** Every node except the root has exactly one incoming edge from its parent. So edges = nodes − 1.

---

## 7.2 Binary Tree

A tree where each node has **at most 2 children** (left and right).

### Node Structure

```c
struct Node {
    int data;
    struct Node *left;
    struct Node *right;
};
```

### Types of Binary Trees

| Type | Definition | Properties |
|------|-----------|-----------|
| **Full (Strictly) Binary Tree** | Every node has 0 or 2 children | Internal nodes + 1 = Leaves |
| **Complete Binary Tree** | All levels full except possibly last, which is filled left to right | Used in heaps |
| **Perfect Binary Tree** | All internal nodes have 2 children, all leaves at same level | Nodes = $2^{h+1} - 1$ |
| **Skewed Binary Tree** | Every node has at most 1 child | Essentially a linked list |
| **Balanced Binary Tree** | Height of left and right subtrees differ by ≤ 1 | AVL trees are balanced |

### Critical Formulas

Let $h$ = height, $n$ = total nodes, $n_0$ = leaves, $n_1$ = nodes with 1 child, $n_2$ = nodes with 2 children.

**For any binary tree:**

$$n = n_0 + n_1 + n_2$$

$$\text{Edges} = n - 1 = n_1 + 2n_2$$

**From these two:**

$$\boxed{n_0 = n_2 + 1}$$

**Derivation:** $n_0 + n_1 + n_2 - 1 = n_1 + 2n_2 \implies n_0 = n_2 + 1$

**This is one of the most important formulas in GATE.** Leaves = internal nodes (with 2 children) + 1.

**For full binary tree** ($n_1 = 0$):
- $n = 2n_0 - 1$ (odd number of nodes)
- With $n$ nodes: $n_0 = (n+1)/2$, $n_2 = (n-1)/2$

**Height bounds:**
- Minimum height (complete tree): $h = \lfloor \log_2 n \rfloor$
- Maximum height (skewed tree): $h = n - 1$

**Node count bounds at height $h$:**
- Minimum nodes: $h + 1$ (skewed)
- Maximum nodes: $2^{h+1} - 1$ (perfect)

**For perfect binary tree:**
- Nodes at level $i$: $2^i$ (root at level 0)
- Total nodes: $\sum_{i=0}^{h} 2^i = 2^{h+1} - 1$
- Leaves: $2^h$
- Internal nodes: $2^h - 1$

### 🔴 GATE Trap: Minimum/Maximum Height Questions

"A binary tree has 31 nodes. What is the minimum height?"

$h = \lfloor \log_2 31 \rfloor = 4$

Verify: perfect tree of height 4 has $2^5 - 1 = 31$ nodes ✓

"A binary tree has 20 leaves. What is the minimum number of nodes?"

In a full binary tree (minimum nodes for given leaves): $n = 2 \times 20 - 1 = 39$

---

## 7.3 Binary Tree Traversals

### The Big Three + Level Order

```c
// Inorder (Left, Root, Right) — LNR
void inorder(struct Node *root) {
    if (root == NULL) return;
    inorder(root->left);
    printf("%d ", root->data);
    inorder(root->right);
}

// Preorder (Root, Left, Right) — NLR
void preorder(struct Node *root) {
    if (root == NULL) return;
    printf("%d ", root->data);
    preorder(root->left);
    preorder(root->right);
}

// Postorder (Left, Right, Root) — LRN
void postorder(struct Node *root) {
    if (root == NULL) return;
    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->data);
}

// Level Order (BFS) — uses queue
void levelOrder(struct Node *root) {
    if (root == NULL) return;
    Queue q;
    enqueue(&q, root);
    while (!isEmpty(&q)) {
        struct Node *curr = dequeue(&q);
        printf("%d ", curr->data);
        if (curr->left) enqueue(&q, curr->left);
        if (curr->right) enqueue(&q, curr->right);
    }
}
```

### 🧠 Mnemonic

- **In**order = **In**side the sandwich (Left **Node** Right)
- **Pre**order = Node comes **Pre**-first (Node Left Right)
- **Post**order = Node comes **Post**-last (Left Right Node)

### Constructing Tree from Traversals

| Given | Can construct unique tree? |
|-------|---------------------------|
| Inorder + Preorder | ✅ Yes |
| Inorder + Postorder | ✅ Yes |
| Inorder + Level order | ✅ Yes |
| Preorder + Postorder | ❌ No (unless full binary tree) |
| Preorder only | ❌ No |
| Postorder only | ❌ No |

**Key rule:** **Inorder is required** (unless tree is a full binary tree with pre+post).

**Why?** Inorder separates left and right subtrees. Without it, you can't determine the partition.

**Algorithm (Inorder + Preorder):**
1. First element of preorder = root
2. Find root in inorder → elements left of it = left subtree, right = right subtree
3. Recurse on left and right subtrees

**Example:**
```
Preorder: F B A D C E G I H
Inorder:  A B C D E F G H I

Root = F (first in preorder)
In inorder: Left of F = {A,B,C,D,E}, Right of F = {G,H,I}

Left subtree preorder: B A D C E
Left subtree inorder:  A B C D E
Root = B, Left = {A}, Right = {C,D,E}
... and so on
```

### Iterative Inorder (Morris Traversal — $O(1)$ space)

Uses **threaded binary tree** concept — temporarily modifies tree structure.

```c
void morrisInorder(struct Node *root) {
    struct Node *curr = root;
    while (curr != NULL) {
        if (curr->left == NULL) {
            printf("%d ", curr->data);
            curr = curr->right;
        } else {
            // Find inorder predecessor
            struct Node *pred = curr->left;
            while (pred->right != NULL && pred->right != curr)
                pred = pred->right;
            
            if (pred->right == NULL) {
                pred->right = curr;  // Create thread
                curr = curr->left;
            } else {
                pred->right = NULL;  // Remove thread
                printf("%d ", curr->data);
                curr = curr->right;
            }
        }
    }
}
```

**Time:** $O(n)$, **Space:** $O(1)$ — no recursion stack needed.

---

## 7.4 Binary Search Tree (BST)

### Property

For every node:
- All values in **left subtree < node value**
- All values in **right subtree > node value**

**Consequence:** **Inorder traversal of BST gives sorted order.**

### Operations

**Search — $O(h)$:**
```c
struct Node* search(struct Node *root, int key) {
    if (root == NULL || root->data == key)
        return root;
    if (key < root->data)
        return search(root->left, key);
    return search(root->right, key);
}
```

**Insert — $O(h)$:**
```c
struct Node* insert(struct Node *root, int key) {
    if (root == NULL)
        return createNode(key);
    if (key < root->data)
        root->left = insert(root->left, key);
    else if (key > root->data)
        root->right = insert(root->right, key);
    return root;
}
```

**Delete — $O(h)$ (Three cases):**

1. **Leaf node:** Simply remove it
2. **One child:** Replace node with its child
3. **Two children:** Replace with **inorder successor** (smallest in right subtree) or **inorder predecessor** (largest in left subtree), then delete that successor/predecessor

```c
struct Node* findMin(struct Node *root) {
    while (root->left != NULL)
        root = root->left;
    return root;
}

struct Node* deleteNode(struct Node *root, int key) {
    if (root == NULL) return NULL;
    
    if (key < root->data)
        root->left = deleteNode(root->left, key);
    else if (key > root->data)
        root->right = deleteNode(root->right, key);
    else {
        // Node found
        if (root->left == NULL) {
            struct Node *temp = root->right;
            free(root);
            return temp;
        }
        if (root->right == NULL) {
            struct Node *temp = root->left;
            free(root);
            return temp;
        }
        // Two children: get inorder successor
        struct Node *succ = findMin(root->right);
        root->data = succ->data;
        root->right = deleteNode(root->right, succ->data);
    }
    return root;
}
```

### BST Complexity

| Operation | Average | Worst (skewed) |
|-----------|---------|----------------|
| Search | $O(\log n)$ | $O(n)$ |
| Insert | $O(\log n)$ | $O(n)$ |
| Delete | $O(\log n)$ | $O(n)$ |

### Number of Structurally Unique BSTs with $n$ keys

$$C_n = \frac{1}{n+1}\binom{2n}{n} = \text{Catalan number}$$

**Example:** $n = 3$ → $C_3 = 5$ distinct BSTs.

### Number of BSTs vs Number of Binary Trees

- Structurally unique binary trees with $n$ nodes = $C_n$
- BSTs with $n$ distinct keys = $C_n$ (each structure corresponds to exactly one BST for a given set of keys, but the count of structures is the same)
- Unlabeled binary trees = $C_n$
- Labeled binary trees = $C_n \times n!$

### 🔴 GATE Trap: BST from Preorder

Given only preorder traversal, we can reconstruct a **unique** BST (unlike general binary trees).

**Why?** BST property constrains the structure. Each element's position is determined by comparing with ancestors.

---

## 7.5 AVL Tree (Self-Balancing BST)

### Balance Factor

$$\text{BF}(node) = \text{height}(left) - \text{height}(right)$$

For AVL: $\text{BF} \in \{-1, 0, 1\}$ for every node.

### Rotations

| Imbalance Type | Detected When | Rotation |
|---------------|--------------|----------|
| LL (Left-Left) | BF = +2 and left child BF = +1 or 0 | Right rotation |
| RR (Right-Right) | BF = -2 and right child BF = -1 or 0 | Left rotation |
| LR (Left-Right) | BF = +2 and left child BF = -1 | Left rotate left child, then right rotate node |
| RL (Right-Left) | BF = -2 and right child BF = +1 | Right rotate right child, then left rotate node |

**Right Rotation (for LL):**
```
    z                y
   / \             /   \
  y   T4   →     x      z
 / \            / \    / \
x   T3         T1  T2 T3  T4
/ \
T1  T2
```

**Left Rotation (for RR):** Mirror of above.

### Minimum Nodes for AVL of Height $h$

$$N(h) = N(h-1) + N(h-2) + 1$$

with $N(0) = 1$, $N(1) = 2$

| Height | Min Nodes | Max Nodes |
|--------|-----------|-----------|
| 0 | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 4 | 7 |
| 3 | 7 | 15 |
| 4 | 12 | 31 |
| 5 | 20 | 63 |

**Why?** Minimum nodes = Fibonacci-like. One subtree has height $h-1$, other has $h-2$ (minimum possible while maintaining balance).

**Maximum height of AVL with $n$ nodes:** $O(\log n)$ — specifically $\approx 1.44 \log_2 n$.

---

## 7.6 Binary Heap

### Min-Heap Property

For every node: **parent ≤ children**. Root = minimum element.

### Max-Heap Property

For every node: **parent ≥ children**. Root = maximum element.

### Array Representation

A heap is a **complete binary tree**, stored in an array (0-indexed):

| Relation | Formula (0-indexed) | Formula (1-indexed) |
|----------|--------------------|--------------------|
| Parent of $i$ | $\lfloor (i-1)/2 \rfloor$ | $\lfloor i/2 \rfloor$ |
| Left child of $i$ | $2i + 1$ | $2i$ |
| Right child of $i$ | $2i + 2$ | $2i + 1$ |

### Heap Operations

**Insert (Heapify Up) — $O(\log n)$:**
```c
void insert(int heap[], int *size, int val) {
    heap[(*size)++] = val;
    int i = *size - 1;
    // Bubble up
    while (i > 0 && heap[(i-1)/2] > heap[i]) {
        swap(&heap[(i-1)/2], &heap[i]);
        i = (i - 1) / 2;
    }
}
```

**Extract Min (Heapify Down) — $O(\log n)$:**
```c
int extractMin(int heap[], int *size) {
    int min = heap[0];
    heap[0] = heap[--(*size)];
    // Sift down
    int i = 0;
    while (1) {
        int smallest = i;
        int left = 2*i + 1, right = 2*i + 2;
        if (left < *size && heap[left] < heap[smallest])
            smallest = left;
        if (right < *size && heap[right] < heap[smallest])
            smallest = right;
        if (smallest == i) break;
        swap(&heap[i], &heap[smallest]);
        i = smallest;
    }
    return min;
}
```

### Build Heap — $O(n)$ (NOT $O(n \log n)$!)

```c
void buildHeap(int arr[], int n) {
    for (int i = n/2 - 1; i >= 0; i--)
        heapifyDown(arr, n, i);
}
```

**Why $O(n)$ and not $O(n \log n)$?**

At height $h$, there are at most $\lceil n/2^{h+1} \rceil$ nodes. Each node at height $h$ requires $O(h)$ work.

$$\text{Total work} = \sum_{h=0}^{\lfloor \log n \rfloor} \left\lceil \frac{n}{2^{h+1}} \right\rceil \cdot O(h) = O\left(n \sum_{h=0}^{\infty} \frac{h}{2^h}\right) = O(n \cdot 2) = O(n)$$

The series $\sum_{h=0}^{\infty} h/2^h = 2$ (a standard result).

### Heap Sort — $O(n \log n)$

```c
void heapSort(int arr[], int n) {
    buildHeap(arr, n);           // O(n)
    for (int i = n-1; i > 0; i--) {
        swap(&arr[0], &arr[i]);  // Move max to end
        heapifyDown(arr, i, 0);  // O(log n) per element
    }
}
```

**Total:** $O(n) + O(n \log n) = O(n \log n)$

### 🔴 GATE Trap: Height of Heap

A heap with $n$ elements has height $\lfloor \log_2 n \rfloor$ (since it's a complete binary tree).

**Number of elements in a heap of height $h$:** Between $2^h$ and $2^{h+1} - 1$.

---

## 7.7 B-Trees and B+ Trees

### B-Tree of Order $m$

| Property | Value |
|----------|-------|
| Max children per node | $m$ |
| Max keys per node | $m - 1$ |
| Min children (non-root internal) | $\lceil m/2 \rceil$ |
| Min keys (non-root) | $\lceil m/2 \rceil - 1$ |
| Root | At least 2 children (if not leaf), or 1 key |
| All leaves | Same level |

**Why B-Trees?** Designed for **disk access**. Each node = one disk block. Minimize disk I/O by maximizing branching factor.

**Search in B-Tree:** $O(\log_m n)$ disk accesses = $O(\log n / \log m)$

### B+ Tree — Key Differences

| Feature | B-Tree | B+ Tree |
|---------|--------|---------|
| Data stored in | All nodes | **Only leaf nodes** |
| Leaves linked | No | **Yes (linked list)** |
| Internal nodes | Keys + data + child pointers | **Keys + child pointers only** |
| Range queries | Slow (need traversal) | **Fast (follow leaf links)** |
| Duplicate keys | No | Internal keys are duplicated as separators |

**Why B+ Tree is preferred for databases:**
1. Internal nodes have more keys (no data → more branching → shorter tree)
2. Range queries are efficient via linked leaves
3. All accesses touch the same number of levels (all data at leaves)

### 🔴 GATE Trap: B-Tree Key Counts

"In a B-tree of order 5 with $n$ keys, what is the maximum height?"

Min keys per non-root node = $\lceil 5/2 \rceil - 1 = 2$
Min children per non-root internal = $\lceil 5/2 \rceil = 3$
Root has at least 2 children.

At height $h$: min nodes at level $i$ = $2 \times 3^{i-1}$ (for $i \geq 1$)
Min keys = $1 + \sum_{i=1}^{h} 2 \times 3^{i-1} \times 2 = 1 + 4(3^h - 1)/2$

Actually, minimum keys in B-tree of order $m$ and height $h$:

$$n_{\min} = 2\left\lceil \frac{m}{2} \right\rceil^h - 1$$

For order 5, height $h$: $n_{\min} = 2 \times 3^h - 1$

So maximum height for $n$ keys: $h \leq \log_{\lceil m/2 \rceil}\left(\frac{n+1}{2}\right)$

---

## 7.8 Huffman Coding

A **greedy** algorithm for **prefix-free, variable-length** encoding.

### Algorithm

1. Create a leaf node for each character with its frequency
2. Build a min-heap of all leaf nodes
3. Repeat until heap has one node:
   - Extract two minimums ($a$, $b$)
   - Create new internal node with frequency $a + b$
   - Insert back to heap
4. The remaining node is the root of the Huffman tree

### Example

Characters: A(5), B(9), C(12), D(13), E(16), F(45)

```
Step 1: Combine A(5) + B(9) = AB(14)
Step 2: Combine C(12) + D(13) = CD(25)
Step 3: Combine AB(14) + E(16) = ABE(30)
Step 4: Combine CD(25) + ABE(30) = CDABE(55)
Step 5: Combine F(45) + CDABE(55) = Root(100)
```

**Result:**
```
        (100)
       /     \
     F(45)  (55)
           /    \
        (25)    (30)
       /   \   /    \
    C(12) D(13) (14) E(16)
               /   \
             A(5)  B(9)
```

Codes: F=0, C=100, D=101, A=1100, B=1101, E=111

### Properties

1. **Prefix-free:** No code is a prefix of another
2. **Optimal** for symbol-by-symbol coding
3. Minimum weighted external path length
4. More frequent characters → shorter codes

### Weighted External Path Length

$$\text{WEPL} = \sum_i f_i \times d_i$$

where $f_i$ = frequency and $d_i$ = depth of character $i$.

### 🔴 GATE Trap: Number of Bits

"How many bits are needed to encode a message?"

Total bits = $\sum_i f_i \times \text{len}(code_i)$

For the example above:
$= 45 \times 1 + 12 \times 3 + 13 \times 3 + 5 \times 4 + 9 \times 4 + 16 \times 3$
$= 45 + 36 + 39 + 20 + 36 + 48 = 224$ bits

---

## 7.9 Threaded Binary Tree

In a binary tree with $n$ nodes, there are $n + 1$ NULL pointers (out of $2n$ total pointers). **Threaded trees** use these NULL pointers to store **inorder successor/predecessor** pointers.

**Types:**
- **Single threaded:** NULL right pointers → inorder successor
- **Double threaded:** Both NULL pointers → predecessor and successor

**Advantage:** Inorder traversal without recursion or stack ($O(1)$ space).

---

## Summary: Quick-Fire GATE Facts for Trees

1. Edges = $n - 1$ for a tree with $n$ nodes.
2. **$n_0 = n_2 + 1$** (leaves = 2-child nodes + 1) — THE most tested formula.
3. Complete binary tree height: $\lfloor \log_2 n \rfloor$.
4. Perfect binary tree nodes: $2^{h+1} - 1$.
5. BST inorder = sorted order.
6. Unique BSTs with $n$ keys = Catalan number.
7. AVL min nodes: $N(h) = N(h-1) + N(h-2) + 1$.
8. Build heap = $O(n)$, not $O(n \log n)$.
9. Heap parent: $\lfloor (i-1)/2 \rfloor$ (0-indexed).
10. Inorder + (Preorder or Postorder) → unique tree.
11. Preorder + Postorder → unique tree only for **full** binary trees.
12. B-Tree of order $m$: min $\lceil m/2 \rceil - 1$ keys per non-root node.
13. Huffman: greedy, prefix-free, optimal symbol-by-symbol coding.
14. Threaded tree uses $n+1$ NULL pointers for efficient traversal.

---

> **5-Second Snap-Check for Tree Questions:**
> 1. Formula question? → Remember $n_0 = n_2 + 1$
> 2. Traversal construction? → You need inorder (usually)
> 3. BST question? → Think sorted order, search = $O(h)$
> 4. Heap question? → Complete binary tree, array representation
> 5. B-tree? → Check min/max keys per node, all leaves same level
