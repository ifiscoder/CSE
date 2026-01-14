# Module 9: String Algorithms

## 🎯 The Atomic Truth
> **"Pattern in text—find it fast"**

---

## 🧠 Mental Model: Finding a Phrase in a Book

[Image: Magnifying glass over book pages, highlighting matching words]

- **Naive:** Read every word, compare letter by letter
- **KMP:** Remember what you've learned from mismatches
- **Rabin-Karp:** Use fingerprints (hashes) for quick rejection
- **Suffix structures:** Pre-process text for instant lookup

---

## 📐 1. Pattern Matching Fundamentals

### 1.1 Problem Statement

Given text T (length n) and pattern P (length m), find all occurrences of P in T.

### 1.2 Terminology

- **Text:** String to search in (length n)
- **Pattern:** String to find (length m)
- **Match:** Pattern found at position i if T[i:i+m] == P

---

## 🐌 2. Naive Pattern Matching

### 2.1 Algorithm

```python
def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    matches = []
    
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            matches.append(i)
    
    return matches
```

### 2.2 Complexity

| Case | Complexity | Example |
|------|------------|---------|
| Best | O(n) | Pattern not in text (first char mismatch) |
| Worst | O(nm) | Text: "AAAAAAA", Pattern: "AAAB" |
| Average | O(n) | Random text and pattern |

### 2.3 When Naive is Okay

- Short patterns (m is small constant)
- One-time search
- Patterns with unique characters

---

## ⚡ 3. KMP Algorithm (Knuth-Morris-Pratt)

### 3.1 The Atomic Truth
> **"Never re-compare what you've already seen"**

### 3.2 Key Insight

When mismatch occurs at position j in pattern:
- We've already matched P[0:j]
- Find longest proper prefix of P[0:j] that's also a suffix
- Shift pattern to align this prefix with matched text

### 3.3 Failure Function (LPS Array)

**LPS[i]** = Length of longest proper prefix of P[0:i+1] that's also a suffix.

```python
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0  # Length of previous longest prefix suffix
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  # Try shorter prefix
            else:
                lps[i] = 0
                i += 1
    
    return lps
```

### 3.4 Example: LPS Computation

```
Pattern: "ABABCABAB"
Index:    0 1 2 3 4 5 6 7 8

i=0: LPS[0] = 0 (single char, no proper prefix)
i=1: A vs B, no match, LPS[1] = 0
i=2: AB, A matches A, LPS[2] = 1
i=3: ABA, AB matches AB, LPS[3] = 2
i=4: ABAB vs ABAB, C vs A, length=2, try length=LPS[1]=0, LPS[4] = 0
i=5: A matches A, LPS[5] = 1
i=6: AB matches AB, LPS[6] = 2
i=7: ABA matches ABA, LPS[7] = 3
i=8: ABAB matches ABAB, LPS[8] = 4

LPS = [0, 0, 1, 2, 0, 1, 2, 3, 4]
```

### 3.5 KMP Search Algorithm

```python
def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    matches = []
    
    i = 0  # Index in text
    j = 0  # Index in pattern
    
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            
            if j == m:  # Pattern found
                matches.append(i - j)
                j = lps[j - 1]  # Continue searching
        else:
            if j != 0:
                j = lps[j - 1]  # Use failure function
            else:
                i += 1
    
    return matches
```

### 3.6 Visualization

```
Text:    ABABDABACDABABCABAB
Pattern: ABABCABAB

Step 1: ABAB matches, then D vs C mismatch
        j = lps[3] = 2, continue from position 2 in pattern

Step 2: AB matches, then D vs A mismatch
        j = lps[1] = 0, continue from position 0

... Eventually finds match at position 10
```

### 3.7 Complexity

| Metric | Complexity |
|--------|------------|
| LPS computation | O(m) |
| Search | O(n) |
| **Total** | **O(n + m)** |
| Space | O(m) |

### 3.8 🎯 GATE Points

1. **No character is compared more than 2m times**
2. **Total comparisons ≤ 2n**
3. **Works for any alphabet**

---

## #️⃣ 4. Rabin-Karp Algorithm

### 4.1 The Atomic Truth
> **"Hash first, compare only if hashes match"**

### 4.2 Key Insight

Use rolling hash to compute hash of each window in O(1) after initial O(m) computation.

### 4.3 Rolling Hash Formula

For pattern/window of length m with base d and modulo q:

$$H = \sum_{i=0}^{m-1} \text{char}[i] \cdot d^{m-1-i} \mod q$$

**Rolling update:**
$$H_{new} = (d \cdot (H_{old} - \text{char}_{removed} \cdot d^{m-1}) + \text{char}_{new}) \mod q$$

### 4.4 Algorithm

```python
def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    d = 256  # Number of characters in alphabet
    q = 101  # A prime number
    matches = []
    
    if m > n:
        return matches
    
    # Compute d^(m-1) mod q
    h = pow(d, m - 1, q)
    
    # Compute initial hashes
    p_hash = 0  # Pattern hash
    t_hash = 0  # Text window hash
    
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q
    
    # Slide pattern over text
    for i in range(n - m + 1):
        # If hashes match, verify character by character
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                matches.append(i)
        
        # Compute hash for next window
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if t_hash < 0:
                t_hash += q
    
    return matches
```

### 4.5 Complexity

| Case | Complexity | Reason |
|------|------------|--------|
| Average | O(n + m) | Few hash collisions |
| Worst | O(nm) | All hashes match (need verification) |

### 4.6 Use Cases

1. **Multiple pattern search** - Compute all pattern hashes, check each window
2. **2D pattern matching** - Hash rows, then hash column of row hashes
3. **Plagiarism detection**

### 4.7 🎯 Choosing Prime q

- Should be large to minimize collisions
- Should fit in word size to avoid overflow
- Common choice: largest prime < 2³¹

---

## 🌳 5. Trie (Prefix Tree)

### 5.1 The Atomic Truth
> **"Tree of prefixes—fast prefix lookup"**

### 5.2 Structure

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0  # Optional: count of words

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.count += 1
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

### 5.3 Visualization

```
Words: ["cat", "car", "card", "care", "dog"]

       root
      /    \
     c      d
     |      |
     a      o
    /|\     |
   t r d    g
     |\
     d e

Ends marked: cat, car, card, care, dog
```

### 5.4 Operations

| Operation | Complexity |
|-----------|------------|
| Insert | O(m) |
| Search | O(m) |
| Prefix search | O(m) |
| Space | O(n × m × alphabet_size) worst case |

Where m = length of word/pattern, n = number of words.

### 5.5 Applications

1. **Autocomplete**
2. **Spell checker**
3. **IP routing (longest prefix match)**
4. **T9 predictive text**

---

## 🔀 6. Z-Algorithm

### 6.1 The Atomic Truth
> **"Z[i] = longest substring starting from i that matches prefix"**

### 6.2 Z-Array Definition

Z[i] = length of longest substring starting at i that is also a prefix of string.

### 6.3 Algorithm

```python
def z_function(s):
    n = len(s)
    z = [0] * n
    z[0] = n  # Entire string matches itself
    
    l, r = 0, 0  # Z-box boundaries
    
    for i in range(1, n):
        if i < r:
            # Use previously computed values
            z[i] = min(r - i, z[i - l])
        
        # Extend manually
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        
        # Update Z-box
        if i + z[i] > r:
            l, r = i, i + z[i]
    
    return z
```

### 6.4 Pattern Matching using Z-Algorithm

```python
def z_search(text, pattern):
    combined = pattern + "$" + text
    z = z_function(combined)
    m = len(pattern)
    
    matches = []
    for i in range(m + 1, len(combined)):
        if z[i] == m:
            matches.append(i - m - 1)
    
    return matches
```

### 6.5 Example

```
String: "aabxaabxcaabxaabxay"
Z:      [19, 1, 0, 0, 4, 1, 0, 0, 0, 8, 1, 0, 0, 5, 1, 0, 0, 1, 0]

For pattern matching:
Pattern: "aabx"
Combined: "aabx$aabxaabxcaabxaabxay"

Z values ≥ 4 indicate matches.
```

### 6.6 Complexity

O(n) time, O(n) space

---

## 🏗️ 7. Suffix Array

### 7.1 The Atomic Truth
> **"Sorted array of all suffixes—powerful for substring queries"**

### 7.2 Definition

For string S of length n:
- Suffix i = S[i:n]
- Suffix Array = sorted indices of all suffixes

### 7.3 Simple Construction (O(n² log n))

```python
def suffix_array_simple(s):
    n = len(s)
    suffixes = [(s[i:], i) for i in range(n)]
    suffixes.sort()
    return [idx for _, idx in suffixes]
```

### 7.4 Efficient Construction (O(n log n))

```python
def suffix_array_efficient(s):
    n = len(s)
    s = s + chr(0)  # Append character smaller than all
    n += 1
    
    # Initial ranking based on single characters
    rank = [ord(c) for c in s]
    sa = list(range(n))
    
    k = 1
    while k < n:
        # Sort by (rank[i], rank[i+k])
        def key(i):
            return (rank[i], rank[i + k] if i + k < n else -1)
        
        sa.sort(key=key)
        
        # Update ranks
        new_rank = [0] * n
        for i in range(1, n):
            new_rank[sa[i]] = new_rank[sa[i-1]]
            if key(sa[i]) != key(sa[i-1]):
                new_rank[sa[i]] += 1
        
        rank = new_rank
        k *= 2
    
    return sa[1:]  # Remove the added character's suffix
```

### 7.5 Example

```
String: "banana"
Suffixes:
0: banana
1: anana
2: nana
3: ana
4: na
5: a

Sorted: a(5), ana(3), anana(1), banana(0), na(4), nana(2)
Suffix Array: [5, 3, 1, 0, 4, 2]
```

### 7.6 LCP Array (Longest Common Prefix)

```python
def lcp_array(s, sa):
    n = len(s)
    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i
    
    lcp = [0] * n
    k = 0
    
    for i in range(n):
        if rank[i] == 0:
            k = 0
            continue
        
        j = sa[rank[i] - 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        
        lcp[rank[i]] = k
        k = max(0, k - 1)  # Kasai's algorithm optimization
    
    return lcp
```

### 7.7 Applications

1. **Pattern search in O(m log n)**
2. **Longest repeated substring**
3. **Number of distinct substrings**
4. **Longest common substring of two strings**

---

## 🏛️ 8. Suffix Tree

### 8.1 The Atomic Truth
> **"Compressed trie of all suffixes—O(m) pattern search"**

### 8.2 Properties

- Every path from root to leaf = one suffix
- Every internal node has ≥ 2 children
- Edges labeled with non-empty substrings
- No two edges from same node start with same character

### 8.3 Construction

Ukkonen's Algorithm: O(n) time, O(n) space

(Complex implementation - typically use library or suffix array instead)

### 8.4 Applications

1. **Exact pattern matching: O(m)**
2. **Longest repeated substring**
3. **Longest common substring**
4. **Palindrome detection**

---

## ↔️ 9. Longest Palindromic Substring

### 9.1 Expand Around Center (O(n²))

```python
def longest_palindrome(s):
    n = len(s)
    if n == 0:
        return ""
    
    start, max_len = 0, 1
    
    def expand(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    for i in range(n):
        len1 = expand(i, i)      # Odd length
        len2 = expand(i, i + 1)  # Even length
        
        length = max(len1, len2)
        if length > max_len:
            max_len = length
            start = i - (length - 1) // 2
    
    return s[start:start + max_len]
```

### 9.2 Manacher's Algorithm (O(n))

```python
def manacher(s):
    # Transform: "abc" -> "^#a#b#c#$"
    t = "^#" + "#".join(s) + "#$"
    n = len(t)
    p = [0] * n  # Palindrome radius
    
    center, right = 0, 0
    
    for i in range(1, n - 1):
        if i < right:
            mirror = 2 * center - i
            p[i] = min(right - i, p[mirror])
        
        # Expand
        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1
        
        # Update center and right boundary
        if i + p[i] > right:
            center, right = i, i + p[i]
    
    # Find maximum
    max_len, max_center = max((p[i], i) for i in range(1, n - 1))
    
    start = (max_center - max_len) // 2
    return s[start:start + max_len]
```

---

## 🔧 10. String Hashing

### 10.1 Polynomial Rolling Hash

```python
class StringHash:
    def __init__(self, s, base=31, mod=10**9 + 9):
        self.n = len(s)
        self.base = base
        self.mod = mod
        
        # Precompute prefix hashes
        self.h = [0] * (self.n + 1)
        self.pw = [1] * (self.n + 1)
        
        for i in range(self.n):
            self.h[i + 1] = (self.h[i] * base + ord(s[i]) - ord('a') + 1) % mod
            self.pw[i + 1] = (self.pw[i] * base) % mod
    
    def get_hash(self, l, r):
        """Get hash of substring s[l:r+1]"""
        return (self.h[r + 1] - self.h[l] * self.pw[r - l + 1] % self.mod + self.mod) % self.mod
```

### 10.2 Double Hashing (Reduce Collisions)

Use two different (base, mod) pairs. Match only if both hashes match.

### 10.3 Applications

1. **Comparing substrings in O(1)**
2. **Rabin-Karp pattern matching**
3. **Longest common prefix (binary search + hashing)**
4. **Palindrome checking**

---

## 🎓 11. GATE Pattern Problems

### Problem Type 1: LPS Array

**Q:** Compute LPS for "AABAACAABAA"

**Solution:**
```
A A B A A C A A B A  A
0 1 0 1 2 0 1 2 3 4  5
```

**Answer:** [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]

---

### Problem Type 2: Comparisons in KMP

**Q:** Maximum comparisons in KMP for text of length n and pattern of length m?

**Answer:** 2n (each text character compared at most twice)

---

### Problem Type 3: Rabin-Karp Hash

**Q:** Rolling hash for "abcd" with d=10, q=13. Next hash after sliding to "bcde"?

**Solution:**
```
H(abcd) = 1×10³ + 2×10² + 3×10 + 4 = 1234
H(bcde) = (10×(1234 - 1×10³) + 5) mod 13
        = (10×234 + 5) mod 13
        = 2345 mod 13 = 5
```

---

## 🚨 12. Common GATE Traps

### Trap 1: LPS vs Z-Array

- LPS[i]: Longest **proper** prefix of P[0:i+1] that's also suffix
- Z[i]: Longest substring starting at i matching prefix

### Trap 2: KMP Shift Amount

Shift = j - LPS[j-1], NOT LPS[j]

### Trap 3: Rabin-Karp Modular Arithmetic

Handle negative numbers: `(hash + mod) % mod`

### Trap 4: Suffix Array 0-indexing

Suffix i starts at index i, not position i+1.

---

## 📝 13. Practice Problems

### Problem 1 [NAT]
LPS[6] for pattern "AABAAAB"?

<details>
<summary>Solution</summary>

Pattern: A A B A A A B
LPS:     0 1 0 1 2 2 3

**Answer: 3**
</details>

---

### Problem 2 [MCQ]
Which algorithm has O(n+m) worst case for pattern matching?

A. Naive
B. Rabin-Karp
C. KMP
D. All of above

<details>
<summary>Solution</summary>

- Naive: O(nm) worst
- Rabin-Karp: O(nm) worst (hash collisions)
- KMP: O(n+m) guaranteed

**Answer:** C
</details>

---

### Problem 3 [MSQ]
Which use suffix structures?

A. Longest repeated substring
B. Longest common substring
C. Pattern counting
D. All substrings enumeration

<details>
<summary>Solution</summary>

All can be efficiently solved using suffix arrays/trees.

**Answer:** A, B, C, D
</details>

---

## 🧠 Memory Anchors

### The Algorithm Selector

```
Pattern Matching:
├── Single pattern, text → KMP or Z-Algorithm
├── Multiple patterns → Aho-Corasick or Rabin-Karp
├── Prefix queries → Trie
└── Substring queries → Suffix Array/Tree

Preprocessing vs Query:
├── O(m) preprocess, O(n) search → KMP
├── O(n) preprocess, O(m) search → Suffix structures
└── O(m) preprocess, O(n) average → Rabin-Karp
```

### The Bizarre Mnemonic: "Detective Finding Clues"

- **Naive:** Check every spot manually
- **KMP:** Remember patterns from failures
- **Rabin-Karp:** Use fingerprints for quick elimination
- **Suffix Array:** Sort all clues alphabetically for binary search

### 5-Second Sanity Check

1. What's being preprocessed - pattern or text?
2. What's the worst-case guarantee needed?
3. Single pattern or multiple?

---

## ⚡ Quick Reference

| Algorithm | Preprocessing | Search | Space | Best For |
|-----------|---------------|--------|-------|----------|
| Naive | - | O(nm) | O(1) | Short patterns |
| KMP | O(m) | O(n) | O(m) | Single pattern |
| Rabin-Karp | O(m) | O(n) avg | O(1) | Multiple patterns |
| Z-Algorithm | O(n+m) | - | O(n+m) | Many applications |
| Trie | O(total chars) | O(m) | O(alphabet × total) | Prefix queries |
| Suffix Array | O(n log n) | O(m log n) | O(n) | Substring queries |

---

**✅ Module Complete | Ready for GATE 2026**

**Next Module:** [Advanced Topics & NP-Completeness →](10-Advanced-Topics.md)
