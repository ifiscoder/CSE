# Module 2: Digital Logic & Boolean Algebra | The Singularity

> **The Atomic Truth:** *"All logic reduces to AND, OR, NOT."*

---

## 🎯 The Path of Elegance (Root Derivation)

### 2.1 Boolean Algebra | The Mathematical Foundation

**The Golden Pivot:** Every Boolean expression can be reduced to two canonical forms.

### Fundamental Postulates (Huntington's Postulates)

| Postulate | OR Form | AND Form |
|-----------|---------|----------|
| Identity | $A + 0 = A$ | $A \cdot 1 = A$ |
| Null | $A + 1 = 1$ | $A \cdot 0 = 0$ |
| Idempotent | $A + A = A$ | $A \cdot A = A$ |
| Complement | $A + A' = 1$ | $A \cdot A' = 0$ |
| Commutative | $A + B = B + A$ | $A \cdot B = B \cdot A$ |
| Associative | $(A+B)+C = A+(B+C)$ | $(A \cdot B) \cdot C = A \cdot (B \cdot C)$ |
| Distributive | $A+(B \cdot C) = (A+B)(A+C)$ | $A \cdot (B+C) = AB + AC$ |

### DeMorgan's Theorems | The Duality Engines

$$\overline{A + B} = \bar{A} \cdot \bar{B}$$
$$\overline{A \cdot B} = \bar{A} + \bar{B}$$

**The Mental Slider:**
```
[3D Dial: Break the bar, change the sign]
LONG BAR → BREAK IT → CHANGE OPERATOR
```

---

## 🔲 2.2 Logic Gates | The Building Blocks

```
[Image of Universal Gate Hierarchy]
         NAND / NOR (Universal)
              ↓
    AND, OR, NOT (Basic)
              ↓
    XOR, XNOR (Arithmetic)
```

### Truth Table Reference

| A | B | AND | OR | NAND | NOR | XOR | XNOR |
|---|---|-----|----|----- |-----|-----|------|
| 0 | 0 |  0  | 0  |  1   |  1  |  0  |  1   |
| 0 | 1 |  0  | 1  |  1   |  0  |  1  |  0   |
| 1 | 0 |  0  | 1  |  1   |  0  |  1  |  0   |
| 1 | 1 |  1  | 1  |  0   |  0  |  0  |  1   |

### ⚡ The GATE Shortcut: Counting 1s

| Gate | Number of 1s in output |
|------|------------------------|
| AND (n inputs) | $1$ (all 1s case) |
| OR (n inputs) | $2^n - 1$ (all except all 0s) |
| XOR (n inputs) | $2^{n-1}$ (odd number of 1s) |
| NAND (n inputs) | $2^n - 1$ |
| NOR (n inputs) | $1$ |

---

## 📐 2.3 Canonical Forms | SOP & POS

### Sum of Products (SOP) | Minterms

$$F = \sum m(i, j, k, ...)$$

**Minterm:** Product term where each variable appears exactly once (complemented or uncomplemented).

For 3 variables (A, B, C):
| Minterm | Binary | Term |
|---------|--------|------|
| $m_0$ | 000 | $\bar{A}\bar{B}\bar{C}$ |
| $m_1$ | 001 | $\bar{A}\bar{B}C$ |
| $m_2$ | 010 | $\bar{A}B\bar{C}$ |
| $m_3$ | 011 | $\bar{A}BC$ |
| $m_4$ | 100 | $A\bar{B}\bar{C}$ |
| $m_5$ | 101 | $A\bar{B}C$ |
| $m_6$ | 110 | $AB\bar{C}$ |
| $m_7$ | 111 | $ABC$ |

### Product of Sums (POS) | Maxterms

$$F = \prod M(i, j, k, ...)$$

**Maxterm:** Sum term where each variable appears exactly once.

**The Duality Rule:**
$$F = \sum m(i, j, ...) \Leftrightarrow F' = \prod M(i, j, ...)$$
$$F = \prod M(p, q, ...) \Leftrightarrow F' = \sum m(p, q, ...)$$

---

## 🗺️ 2.4 Karnaugh Maps (K-Maps) | Visual Minimization

### The K-Map Anatomy

**2-Variable K-Map:**
```
      B
    0   1
A ┌───┬───┐
0 │ 0 │ 1 │
  ├───┼───┤
1 │ 2 │ 3 │
  └───┴───┘
```

**3-Variable K-Map:**
```
        BC
      00  01  11  10
A  ┌────┬────┬────┬────┐
0  │ 0  │ 1  │ 3  │ 2  │
   ├────┼────┼────┼────┤
1  │ 4  │ 5  │ 7  │ 6  │
   └────┴────┴────┴────┘
```

**4-Variable K-Map:**
```
          CD
       00   01   11   10
AB ┌─────┬─────┬─────┬─────┐
00 │  0  │  1  │  3  │  2  │
   ├─────┼─────┼─────┼─────┤
01 │  4  │  5  │  7  │  6  │
   ├─────┼─────┼─────┼─────┤
11 │ 12  │ 13  │ 15  │ 14  │
   ├─────┼─────┼─────┼─────┤
10 │  8  │  9  │ 11  │ 10  │
   └─────┴─────┴─────┴─────┘
```

### ⚡ K-Map Grouping Rules

1. **Group sizes:** $1, 2, 4, 8, 16, ...$ (powers of 2)
2. **Wraparound:** Edges connect (left↔right, top↔bottom)
3. **Overlap allowed:** One cell can be in multiple groups
4. **Largest groups first:** Minimize terms
5. **Don't cares (X):** Can be 0 or 1 as needed

### The Grouping → Expression Formula

| Group Size | Variables Eliminated |
|------------|---------------------|
| 1 | 0 |
| 2 | 1 |
| 4 | 2 |
| 8 | 3 |
| $2^k$ | $k$ |

---

## 🔧 2.5 Combinational Circuits

### Multiplexer (MUX) | The Universal Selector

```
[Image of 4:1 MUX]
        ┌─────────┐
   I₀ ──┤         │
   I₁ ──┤  4:1    ├── Y
   I₂ ──┤  MUX    │
   I₃ ──┤         │
        └────┬────┘
           S₁ S₀
```

**The Golden Formula:**
$$Y = \bar{S_1}\bar{S_0}I_0 + \bar{S_1}S_0I_1 + S_1\bar{S_0}I_2 + S_1S_0I_3$$

**GATE Shortcut:** $2^n:1$ MUX can implement ANY n-variable Boolean function!

### Implementing Functions with MUX

**Example:** Implement $F(A,B,C) = \sum m(1,2,6,7)$ using 4:1 MUX

1. Use A, B as select lines
2. Express F in terms of C:
   - $(A,B) = (0,0)$: $m_0=0, m_1=1$ → Output = $C$
   - $(A,B) = (0,1)$: $m_2=1, m_3=0$ → Output = $\bar{C}$
   - $(A,B) = (1,0)$: $m_4=0, m_5=0$ → Output = $0$
   - $(A,B) = (1,1)$: $m_6=1, m_7=1$ → Output = $1$

| Select (A,B) | I input |
|--------------|---------|
| 00 | C |
| 01 | $\bar{C}$ |
| 10 | 0 |
| 11 | 1 |

### Decoder | The Address Translator

**$n:2^n$ Decoder:** Activates exactly ONE of $2^n$ outputs.

```
[Image of 2:4 Decoder]
      ┌──────────┐
 A ───┤          ├─── D₀ = Ā·B̄
 B ───┤  2:4     ├─── D₁ = Ā·B
      │ Decoder  ├─── D₂ = A·B̄
      │          ├─── D₃ = A·B
      └──────────┘
```

**GATE Shortcut:** Decoder + OR gates = ANY Boolean function!

### Encoder | The Priority Resolver

**Priority Encoder:** When multiple inputs are 1, highest priority wins.

| Input (I₃I₂I₁I₀) | Output (Y₁Y₀) | Valid |
|------------------|---------------|-------|
| 0001 | 00 | 1 |
| 001X | 01 | 1 |
| 01XX | 10 | 1 |
| 1XXX | 11 | 1 |

---

## ⚡ 2.6 Arithmetic Circuits

### Half Adder

$$S = A \oplus B$$
$$C = A \cdot B$$

### Full Adder

$$S = A \oplus B \oplus C_{in}$$
$$C_{out} = AB + C_{in}(A \oplus B) = AB + BC_{in} + AC_{in}$$

```
[Image of Full Adder Block]
  A ──┬──────┐
      │      ▼
  B ──┼───►[XOR]─── S
      │   ↓
Cᵢₙ──┴──►[Carry]── Cₒᵤₜ
```

### Ripple Carry Adder | The Serial Path

**Critical Path Delay:** $T = (n-1) \cdot T_{carry} + T_{sum}$

Where $T_{carry} = 2$ gate delays (for AND-OR path)

**For n-bit RCA:** Total delay ≈ $2n$ gate delays

### Carry Look-Ahead Adder (CLA) | The Parallel Speedup

**Generate:** $G_i = A_i \cdot B_i$ (carry generated internally)
**Propagate:** $P_i = A_i \oplus B_i$ (carry propagated through)

$$C_1 = G_0 + P_0C_0$$
$$C_2 = G_1 + P_1G_0 + P_1P_0C_0$$
$$C_3 = G_2 + P_2G_1 + P_2P_1G_0 + P_2P_1P_0C_0$$

**CLA Delay:** $O(\log n)$ instead of $O(n)$

---

## 🔄 2.7 Sequential Circuits | State Machines

### Flip-Flops | The Memory Elements

| Type | Characteristic Equation | Excitation Table |
|------|------------------------|------------------|
| SR | $Q^+ = S + \bar{R}Q$ | See below |
| JK | $Q^+ = J\bar{Q} + \bar{K}Q$ | See below |
| D | $Q^+ = D$ | $D = Q^+$ |
| T | $Q^+ = T \oplus Q$ | $T = Q \oplus Q^+$ |

### Excitation Tables | The Reverse Engineering

**SR Flip-Flop:**
| $Q$ | $Q^+$ | $S$ | $R$ |
|-----|-------|-----|-----|
| 0 | 0 | 0 | X |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | X | 0 |

**JK Flip-Flop:**
| $Q$ | $Q^+$ | $J$ | $K$ |
|-----|-------|-----|-----|
| 0 | 0 | 0 | X |
| 0 | 1 | 1 | X |
| 1 | 0 | X | 1 |
| 1 | 1 | X | 0 |

### Counter Design | State Machine Approach

**Modulo-N Counter:** Counts from 0 to N-1, then resets.

**Number of Flip-Flops Required:** $\lceil \log_2 N \rceil$

---

## 🎭 The Bizarre Mnemonic | "The K-Map Dance"

*"Gray code is a WALTZ: only ONE bit changes per step. In K-Maps, adjacent cells are dance partners—they differ by exactly one variable, making simplification a choreographed elimination!"*

---

## 🏆 The 2026 Adversarial Vault

### Trap 1: The K-Map Wraparound Trap
**Question Pattern:** "Minimize $F = \sum m(0, 2, 8, 10)$ for 4 variables."
**Anti-Solution:** Students miss the corner grouping.
**Truth:** All four corners form ONE group! Result: $\bar{B}\bar{D}$

### Trap 2: The Don't Care Exploitation
**Question Pattern:** Given don't cares, find minimum SOP.
**Anti-Solution:** Students either ignore don't cares OR use all of them.
**Truth:** Use don't cares ONLY to enlarge groups, NEVER as required outputs.

### Trap 3: The Universal Gate Count
**Question Pattern:** "Implement XOR using minimum NAND gates."
**Anti-Solution:** Students derive from scratch.
**Truth:** XOR = 4 NAND gates (memorize this!)

### Trap 4: The Decoder Output Miscount
**Question Pattern:** "How many 2:4 decoders to build a 4:16 decoder?"
**Anti-Solution:** Students say 4.
**Truth:** 5 decoders (1 for enable + 4 for outputs).

### MSQ Logic Gate | Elimination Rules
1. MUX select lines = $\log_2(\text{data inputs})$
2. Decoder outputs = $2^{\text{inputs}}$
3. Priority encoder needs a VALID output signal
4. Minimum gates for XOR: 4 NAND or 5 NOR

---

## 📊 GATE PYQ Pattern Analysis

| Year | Topic | Marks | Trap Type |
|------|-------|-------|-----------|
| 2023 | K-Map Minimization | 2 | Don't care usage |
| 2022 | MUX Implementation | 2 | Function fitting |
| 2021 | CLA Carry Calculation | 2 | G and P confusion |
| 2020 | Flip-Flop Excitation | 1 | Wrong table |

---

## ⚡ The 5-Second Snap-Checks

| Check | Rule |
|-------|------|
| K-Map group size | Power of 2 only |
| MUX select lines | $\log_2(\text{inputs})$ |
| Decoder outputs | $2^n$ for n inputs |
| FF next state | Apply characteristic equation |

---

**Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: [Sovereign].**

*Would you like to initiate a **'Multi-Variable Stress Test'** combining Digital Logic with Pipelining Hazards for a Rank-1 simulation?*

---
[← Previous: Number Systems](./01-Number-Systems-Data-Representation.md) | [Back to Index](./README.md) | [Next: CPU Architecture →](./03-CPU-Architecture-Instruction-Set.md)
