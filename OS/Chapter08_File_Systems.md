# Chapter 8: File Systems | The Persistence Singularity

## The Atomic Truth
**File System = Abstraction over raw storage blocks**

---

## 8.1 File Concept

### The Path of Elegance

**File:** Named collection of related information stored on secondary storage.

**Attributes:**
- **Name:** Human-readable identifier
- **Type:** Executable, text, binary, etc.
- **Location:** Pointer to device and location on device
- **Size:** Current file size (bytes)
- **Protection:** Access-control information (read/write/execute)
- **Time stamps:** Creation, last access, last modification
- **Owner:** User ID of creator

**The Golden Pivot:** A file is a **logical unit** of storage. Physical storage details are hidden.

---

## 8.2 File Operations

### The Six Fundamental Operations

1. **Create:** Allocate space, create directory entry
2. **Open:** Load metadata into memory (file descriptor/handle)
3. **Read:** Transfer data from file to memory
4. **Write:** Transfer data from memory to file
5. **Seek:** Reposition file pointer
6. **Close:** Release file descriptor, flush buffers
7. **Delete:** Remove directory entry, free space

### Open File Table

**Per-Process Table:**
- File pointer (current position)
- Access rights

**System-Wide Table:**
- File location on disk
- Size
- Open count (how many processes have it open)

**The 2026 Trap:**

**Question:** "Can two processes write to the same file simultaneously?"

**Answer:** **Yes** (if file opened in shared mode), but **race conditions** can occur (need synchronization).

---

## 8.3 File Access Methods

### 1. Sequential Access

**Model:** Tape drive (read/write in order).

```c
read_next();   // Read next record
write_next();  // Write next record
reset();       // Rewind to beginning
```

**Use Case:** Log files, backups.

### 2. Direct (Random) Access

**Model:** Disk (jump to any record).

```c
read(n);   // Read block n
write(n);  // Write block n
seek(n);   // Position at block n
```

**Use Case:** Databases, indexed files.

**The Golden Pivot:** Direct access requires **fixed-size records** (or index structure).

---

## 8.4 Directory Structure

### Single-Level Directory

```
All files in one directory
[file1, file2, file3, ...]
```

**Problem:** Naming conflicts, no organization.

### Two-Level Directory

```
Per-user directories
User1: [file1, file2]
User2: [file1, file3]
```

**Problem:** No subdirectories, limited organization.

### Tree-Structured (Hierarchical)

```
Root
├── home
│   ├── user1
│   │   ├── docs
│   │   └── code
│   └── user2
└── etc
```

**Properties:**
- **Path:** Absolute (`/home/user1/file.txt`) or Relative (`../user2/file.txt`)
- **Current directory:** Working directory pointer

### Acyclic Graph

**Feature:** Allow **sharing** (multiple paths to same file).

**Mechanism:** **Links**
- **Hard link:** Multiple directory entries point to same inode
- **Soft link (symbolic link):** File contains path to target file

**Problem:** Deletion ambiguity (what happens when shared file deleted?).

---

## 8.5 File Allocation Methods

### 1. Contiguous Allocation

**Mechanism:** File occupies consecutive blocks on disk.

**Directory Entry:** (start block, length)

**Example:**
- File A: starts at block 10, length 5 → occupies blocks [10, 11, 12, 13, 14]

**Advantages:**
1. **Simple:** Only start and length stored
2. **Fast sequential access:** Read entire file without seeking
3. **Fast random access:** Block $n$ at address: start + $n$

**Disadvantages:**
1. **External fragmentation:** Free space scattered
2. **File growth difficult:** Cannot expand if next block occupied
3. **Needs compaction:** Expensive

**Use Case:** CD-ROMs (read-only, no growth).

### 2. Linked Allocation

**Mechanism:** Each block contains pointer to next block.

**Directory Entry:** (first block, last block)

**Example:**
```
File A: Block 5 → Block 12 → Block 9 → Block 3 → NULL
```

**Advantages:**
1. **No external fragmentation:** Any free block usable
2. **Easy file growth:** Add block to end of chain

**Disadvantages:**
1. **Slow random access:** Must traverse chain from beginning
2. **Pointer overhead:** Each block wastes space for pointer
3. **Reliability:** If one pointer corrupted, rest of file lost

**Optimization: FAT (File Allocation Table)**

**Mechanism:** Store all pointers in a **separate table** (in memory).

**Structure:**
```
Block | Next Block
------|------------
0     | -1 (free)
1     | 5
2     | -1 (free)
3     | -1 (EOF)
4     | -1 (free)
5     | 12
...
```

**Advantages:**
- Random access faster (no need to read data blocks to get pointers)
- Entire FAT can be cached in memory

**Use Case:** FAT12/16/32 file systems (DOS, Windows).

### 3. Indexed Allocation

**Mechanism:** Each file has an **index block** containing pointers to all data blocks.

**Directory Entry:** (index block address)

**Example:**
```
File A: Index block 10
Index block 10: [5, 12, 9, 3, ...]
```

**Advantages:**
1. **Fast random access:** Direct lookup in index
2. **No external fragmentation**

**Disadvantages:**
1. **Pointer overhead:** Entire index block needed even for small files
2. **Index block size limits file size**

**Solutions for Large Files:**

#### Linked Scheme
Index blocks linked together (for very large files).

#### Multilevel Index
Index block points to other index blocks (like multi-level paging).

**Example (2-level):**
```
Index Block (Level 1) → [Index Block 2, Index Block 3, ...]
Index Block 2 (Level 2) → [Data Block 1, Data Block 2, ...]
```

#### Combined Scheme (UNIX inode)

**Structure:**
```
inode:
  - Direct blocks: 12 pointers (point directly to data blocks)
  - Single indirect: 1 pointer (points to index block)
  - Double indirect: 1 pointer (points to index of index blocks)
  - Triple indirect: 1 pointer (3-level indirection)
```

**Calculation Example:**

**Given:**
- Block size: 4 KB
- Pointer size: 4 bytes
- Pointers per block: $4096 / 4 = 1024$

**Maximum file size:**
- Direct: $12 \times 4 \text{ KB} = 48 \text{ KB}$
- Single indirect: $1024 \times 4 \text{ KB} = 4 \text{ MB}$
- Double indirect: $1024 \times 1024 \times 4 \text{ KB} = 4 \text{ GB}$
- Triple indirect: $1024^3 \times 4 \text{ KB} = 4 \text{ TB}$

**Total:** $48 \text{ KB} + 4 \text{ MB} + 4 \text{ GB} + 4 \text{ TB} \approx 4 \text{ TB}$

**The 2026 Adversarial Vault:**

**Trap:** "Indexed allocation always wastes space for index block."
- **TRUE** for small files (index block overhead).
- **Mitigated** in UNIX inode (direct pointers for small files).

---

## 8.6 Free Space Management

### 1. Bit Vector (Bitmap)

**Mechanism:** One bit per block (0 = free, 1 = allocated).

**Example:**
```
Blocks: 0 1 2 3 4 5 6 7
Bitmap: 1 0 1 1 0 0 1 0
        (Block 1, 4, 5, 7 are free)
```

**Advantages:**
- Simple, fast to find free blocks (scan for 0 bits)
- Easy to find contiguous blocks

**Disadvantages:**
- **Overhead:** For 1 TB disk with 4 KB blocks, bitmap = $\frac{1 \text{ TB}}{4 \text{ KB}} \times 1 \text{ bit} = 32 \text{ MB}$

### 2. Linked List

**Mechanism:** Free blocks linked together.

**Advantages:**
- No wasted space for bitmap

**Disadvantages:**
- Slow to find contiguous blocks
- Need to traverse list

### 3. Grouping

**Mechanism:** First free block contains addresses of $n$ free blocks. The $n$-th block contains addresses of next $n$ free blocks, etc.

**Advantage:** Faster than simple linked list.

### 4. Counting

**Mechanism:** Store (first free block, count of contiguous free blocks).

**Example:**
```
Free list: [(10, 5), (20, 3), (50, 10)]
```

**Advantage:** Efficient for contiguous allocation.

---

## 8.7 File System Implementation

### Layered Structure

```
Application Programs
    ↓
Logical File System (directory management, inode)
    ↓
File-Organization Module (blocks, free space)
    ↓
Basic File System (I/O control, buffering)
    ↓
I/O Control (device drivers)
    ↓
Devices (disk, SSD)
```

### On-Disk Structures

1. **Boot Control Block:** Info to boot OS (first block)
2. **Volume Control Block:** Volume details (superblock in UNIX)
   - Number of blocks, block size, free block count
3. **Directory Structure:** File names and inode numbers
4. **Inodes / FCB (File Control Block):** File metadata
   - Permissions, timestamps, block pointers

### In-Memory Structures

1. **Mount Table:** Info about mounted volumes
2. **Directory Cache:** Recently accessed directory info
3. **System-Wide Open File Table:** Files opened by all processes
4. **Per-Process Open File Table:** Files opened by this process

---

## 8.8 Virtual File System (VFS)

### The Abstraction Layer

**Problem:** Different file systems (ext4, NTFS, FAT32) have different interfaces.

**Solution: VFS**

```
User Space: open(), read(), write(), close()
    ↓
VFS Layer: Unified interface
    ↓         ↓         ↓
  ext4      NTFS      FAT32
```

**Key Structures:**
1. **vnode (virtual inode):** File representation
2. **VFS operations:** Function pointers to FS-specific functions

**The Golden Pivot:** VFS allows multiple file systems to coexist transparently.

---

## 8.9 Efficiency and Performance

### Buffer Cache

**Mechanism:** Keep frequently accessed blocks in memory (RAM cache).

**Replacement:** LRU or similar algorithm.

**Write Strategies:**
1. **Write-through:** Write to cache and disk immediately (safe, slow)
2. **Write-back:** Write to cache, defer disk write (fast, risky)

### Read-Ahead

**Mechanism:** When block $n$ accessed, also read blocks $n+1, n+2$ (prefetch).

**Rationale:** Exploit spatial locality (sequential access common).

### Asynchronous I/O

**Mechanism:** Issue I/O request, continue execution (don't block).

**Use Case:** Overlapping computation and I/O.

---

## 8.10 Recovery and Consistency

### File System Consistency

**Problem:** Crash during write → inconsistent state.

**Example:**
- Updating file: allocate new block, update inode, update free list
- Crash after step 2 → block allocated but not in free list (leak!)

### Solutions

#### 1. Consistency Checker (fsck, chkdsk)

**Mechanism:** Scan entire file system, rebuild free list, fix inconsistencies.

**Problem:** Slow (hours for large disks).

#### 2. Journaling (Log-Structured)

**Mechanism:** Write operations to **log** (journal) before committing.

**Steps:**
1. Write intended changes to journal
2. Mark journal entry as committed
3. Apply changes to actual file system
4. Remove journal entry

**On crash:**
- Replay journal (redo committed operations)

**Advantages:**
- **Fast recovery** (only replay journal, not scan entire disk)
- **Consistency guaranteed**

**Examples:** ext3/ext4 (Linux), NTFS (Windows), APFS (macOS).

---

## 8.11 Mental Machinery for Permanent Recall

### The Bizarre Mnemonic: "The Library Warehouse"

Imagine a **library warehouse** (disk):

- **Files:** Books
- **Blocks:** Storage boxes (fixed size)
- **Directory:** Catalog (book → box mapping)
- **Contiguous:** All chapters of one book in consecutive boxes (fast to read, hard to expand)
- **Linked:** Each box has note saying "next part in box #X" (flexible, slow random access)
- **Indexed:** Master index box listing all boxes for a book (fast lookup)
- **inode:** Book's metadata card (author, size, box locations)
- **Bitmap:** Wall chart showing which boxes are full (quick glance)
- **Journaling:** Logbook of planned changes (safety net)

**The Mental Slider:**
- Left (Contiguous): Fast, rigid
- Middle (Linked): Flexible, slow random access
- Right (Indexed): Fast random access, overhead

### The 5-Second Snap-Check

**Q:** Which allocation method for which scenario?

| **Scenario** | **Method** |
|--------------|------------|
| CD-ROM (read-only) | Contiguous |
| Small disk, simple OS | Linked (FAT) |
| General-purpose OS | Indexed (inode) |

---

## 8.12 Practice Problems

### MCQ 1: File Allocation

**Q:** Which allocation method supports fast random access without external fragmentation?

(A) Contiguous  
(B) Linked  
(C) Indexed  
(D) None  

**Solution:**

- Contiguous: Fast random access, but has external fragmentation
- Linked: No external frag, but slow random access
- Indexed: Fast random access, no external frag ✓

**Answer: (C)**

---

### MCQ 2: UNIX inode

**Q:** In UNIX inode, which pointer is used for very large files?

(A) Direct  
(B) Single indirect  
(C) Double indirect  
(D) Triple indirect  

**Solution:**

Triple indirect supports files up to ~4 TB (largest).

**Answer: (D)**

---

### MCQ 3: Free Space

**Q:** For a 1 GB disk with 1 KB blocks, bitmap size = ?

(A) 128 KB  
(B) 256 KB  
(C) 512 KB  
(D) 1 MB  

**Solution:**

Blocks: $\frac{1 \text{ GB}}{1 \text{ KB}} = 1,048,576$ blocks

Bitmap: $\frac{1,048,576 \text{ bits}}{8} = 131,072 \text{ bytes} = 128 \text{ KB}$

**Answer: (A)**

---

### MCQ 4: Journaling

**Q:** What is the main advantage of journaling file systems?

(A) Faster writes  
(B) Larger file size support  
(C) Fast crash recovery  
(D) Better compression  

**Solution:**

Journaling enables fast recovery (replay log vs full scan).

**Answer: (C)**

---

### NAT 1: inode Calculation

**Q:** Block size = 2 KB, pointer size = 4 bytes. How many data blocks can a single indirect pointer reference?

**Solution:**

Pointers per block: $\frac{2048}{4} = 512$

**Answer: 512**

---

### NAT 2: Contiguous Allocation

**Q:** File A occupies blocks 10-14. File B occupies blocks 20-25. File A grows by 2 blocks. If block 15 is free but 16 is occupied, how many blocks must be relocated?

**Solution:**

File A needs blocks 10-16 (7 blocks). Block 16 is occupied, so A must be **relocated entirely** to a new contiguous area.

Blocks relocated: 5 (current blocks 10-14)

**Answer: 5**

---

### NAT 3: Linked Allocation

**Q:** Block size = 512 bytes, pointer size = 4 bytes. For a file of 10 KB, how many blocks are needed (including overhead)?

**Solution:**

Usable space per block: $512 - 4 = 508$ bytes

Blocks needed: $\lceil \frac{10 \times 1024}{508} \rceil = \lceil 20.63 \rceil = 21$ blocks

**Answer: 21**

---

### NAT 4: Maximum File Size

**Q:** UNIX inode with 10 direct pointers, block size = 4 KB, pointer size = 4 bytes. What is the maximum file size using only direct pointers (in KB)?

**Solution:**

$10 \times 4 = 40$ KB

**Answer: 40**

---

## 8.13 The Elite Formulas Summary

### 1. Bitmap Size

$$\text{Bitmap Size} = \frac{\text{Total Blocks}}{8} \text{ bytes}$$

### 2. Pointers per Block

$$N = \frac{\text{Block Size}}{\text{Pointer Size}}$$

### 3. Maximum File Size (Single Indirect)

$$\text{Max Size} = N \times \text{Block Size}$$

### 4. Maximum File Size (UNIX inode)

$$\text{Max} = D \times B + N \times B + N^2 \times B + N^3 \times B$$

where $D$ = direct pointers, $N$ = pointers per block, $B$ = block size.

---

## Logic Singularity Verified for 2026 (IIT-G Standards)

**Mastery Level:** Sovereign

**The Core Insight:**
- **Contiguous:** Fast but rigid
- **Linked:** Flexible but slow random access
- **Indexed:** Fast random access, overhead for small files
- **UNIX inode:** Hybrid (direct + indirect pointers)

**Next:** Chapter 9 dissects **Disk Management & I/O**—where you'll learn why SSTF isn't always best.

**Would you like to initiate a 'Multi-Variable Stress Test' combining file allocation with disk scheduling?**
