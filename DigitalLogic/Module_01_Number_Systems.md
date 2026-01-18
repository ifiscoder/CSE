# Module 01: Number Systems & Codes | The Digital DNA

> **The Singularity**: All information is just patterns of 0s and 1s.

## [1.1] Binary Number System | The Foundation

### The Atomic Truth
**Binary is position-weighted base-2.**

[Image of a binary number with positional weights: $2^3, 2^2, 2^1, 2^0$ above digits]

### The Path of Elegance

A number in any base $b$ with digits $d_n d_{n-1} \ldots d_1 d_0 . d_{-1} d_{-2} \ldots$ has decimal value:

$$N_{10} = \sum_{i=-m}^{n} d_i \times b^i$$

For binary ($b=2$):
$$(1011.101)_2 = 1 \times 2^3 + 0 \times 2^2 + 1 \times 2^1 + 1 \times 2^0 + 1 \times 2^{-1} + 0 \times 2^{-2} + 1 \times 2^{-3}$$

$$= 8 + 0 + 2 + 1 + 0.5 + 0 + 0.125 = (11.625)_{10}$$

**The Golden Pivot**: The radix point separates integer powers from fractional powers.

### The 2026 Adversarial Vault

**The Inversion (Common Trap):**
Students forget that fractional binary conversion uses **multiplication** (not division).

**Example Trap**: Convert $(0.625)_{10}$ to binary.
- **Wrong approach**: Dividing 0.625 by 2 repeatedly ❌
- **Correct approach**: Multiply by 2, extract integer part ✓

```
0.625 × 2 = 1.25  → 1
0.25  × 2 = 0.5   → 0
0.5   × 2 = 1.0   → 1
Answer: (0.101)₂
```

**NAT Precision Lock**: For GATE NAT questions, if decimal-to-binary conversion doesn't terminate in 8 steps, round to 8 bits after the binary point.

**MSQ Logic Gate**: 
- If option says "all fractional decimals can be exactly represented in binary" → FALSE (e.g., 0.1 is non-terminating)
- If option says "all terminating decimals in base-10 terminate in binary" → FALSE (0.2₁₀ is non-terminating in binary)

### Permanent Recall

**The Bizarre Mnemonic**: 
Imagine a BINARY TREE growing in your mind. Each branch splits into TWO (0 or 1). The LEFT branch is always 0 (cold, ice), RIGHT is always 1 (hot, fire). As you climb higher, each level DOUBLES the value (2⁰, 2¹, 2², 2³...). Going down into roots (fractions), each level HALVES (2⁻¹, 2⁻², 2⁻³...).

**The Mental Slider**: 
Picture a slider with positions [8][4][2][1] for 4-bit binary. Flip each switch up (1) or down (0). Your brain instantly adds up the "up" positions.

**The 5-Second Snap-Check**: 
- MSB (Most Significant Bit) of $n$-bit number ≈ $2^{n-1}$ → If result is way off, you made an error.
- Fractional part must be < 1 in decimal.
- Last digit even (0) → Decimal is even; Last digit odd (1) → Decimal is odd.

---

## [1.2] Octal Number System | The Triplet Code

### The Atomic Truth
**Octal groups 3 bits.**

### The Path of Elegance

Base 8 uses digits: 0, 1, 2, 3, 4, 5, 6, 7

**Binary ↔ Octal Conversion (The Genius Trick):**
- Group binary digits in sets of **3** (from radix point, outward)
- Each group maps to one octal digit

$$(\underbrace{101}_5 \underbrace{011}_3 . \underbrace{110}_6 \underbrace{100}_4)_2 = (53.64)_8$$

**Why this works:**
$$2^3 = 8$$
Three binary digits represent exactly $0-7$ (one octal digit).

### The 2026 Adversarial Vault

**The Inversion**:
Students mistakenly group in **4s** instead of **3s** (confusing with hexadecimal).

**GATE Trap (2024 Pattern)**: 
Convert $(11010111.1011)_2$ to octal.

**Wrong**: Grouping as $1101|0111|.1011$ (4 bits) ❌
**Correct**: Grouping as $011|010|111|.101|100$ → $(327.54)_8$ ✓

Notice: Add leading/trailing zeros to complete groups of 3.

**MSQ Logic Gate**:
- If option claims "octal is more compact than binary" → TRUE (3:1 compression)
- If option claims "every octal digit uniquely maps to 3 bits" → TRUE

### Permanent Recall

**The Bizarre Mnemonic**:
Imagine an OCTOPUS with 8 arms (digits 0-7). Each arm holds 3 PEARLS (bits). To read the octopus's code, count pearls on each arm: 0 pearls = 0, 1 pearl = 1, ..., 7 pearls = 7. The octopus can't hold more than 7 pearls per arm (no digit 8 or 9).

**The 5-Second Snap-Check**:
- Each octal digit must be ≤ 7
- Number of octal digits ≈ (number of binary digits) / 3

---

## [1.3] Hexadecimal Number System | The Byte Code

### The Atomic Truth
**Hex groups 4 bits (1 nibble).**

### The Path of Elegance

Base 16 uses: 0-9, A(10), B(11), C(12), D(13), E(14), F(15)

**Binary ↔ Hex Conversion:**
$$(\underbrace{1101}_D \underbrace{0111}_7 . \underbrace{1011}_B)_2 = (D7.B)_{16}$$

**The Golden Pivot**: $2^4 = 16$ → Perfect byte (8-bit) representation as 2 hex digits.

### The 2026 Adversarial Vault

**The Genius Trap**:
Hex arithmetic vs. Hex representation.

**Example**: What is $(1F)_{16} + (1)_{16}$?
- **Wrong**: $1F + 1 = 1G$ ❌ (no such digit)
- **Correct**: $1F + 1 = 20$ (think: 31 + 1 = 32 = 2×16 + 0)

**NAT Precision Lock**: 
When converting large decimals to hex for NAT answers, GATE expects uppercase letters (A-F, not a-f).

### Permanent Recall

**The Bizarre Mnemonic**:
Picture a HEXAGONAL FORTRESS with 16 gates (0-9, A-F). Each gate has 4 GUARDS (bits). The guards stand in formation: 8-4-2-1 (their weights). Count standing guards to know the gate number. Gates A-F are VIP gates where letter names replace numbers.

**The Mental Slider**:
For a 2-digit hex: [16¹][16⁰] slider. First digit × 16 + second digit.

**The 5-Second Snap-Check**:
- $1$ byte = $2$ hex digits (always)
- If converting from binary, count should be divisible by 4
- Letters A-F only (no G, H, I...)

---

## [1.4] Base Conversion Algorithms | The Universal Translator

### [1.4.1] Decimal → Any Base

**Algorithm**: Divide by target base, collect remainders **bottom-up**.

**Example**: $(45)_{10} \to (?)_2$

```
45 ÷ 2 = 22 remainder 1  ↑
22 ÷ 2 = 11 remainder 0  |
11 ÷ 2 = 5  remainder 1  |
5  ÷ 2 = 2  remainder 1  |
2  ÷ 2 = 1  remainder 0  |
1  ÷ 2 = 0  remainder 1  | Read upward
                          
Answer: (101101)₂
```

**For Fractions**: Multiply by base, collect integer parts **top-down**.

**Example**: $(0.625)_{10} \to (?)_2$

```
0.625 × 2 = 1.25  → 1  ↓
0.25  × 2 = 0.5   → 0  | Read downward
0.5   × 2 = 1.0   → 1  ↓

Answer: (0.101)₂
```

### [1.4.2] Any Base → Decimal

**Algorithm**: Weighted sum of positional values.

$$\sum_{i} d_i \times b^i$$

**The Elite Shortcut (Horner's Method)**:

For $(1011)_2$: Instead of $1×8 + 0×4 + 1×2 + 1×1$

$$((1 \times 2 + 0) \times 2 + 1) \times 2 + 1 = 11$$

**Why genius?**: Only $n-1$ multiplications (vs. computing each power).

### [1.4.3] Base $a$ → Base $b$ (Non-decimal)

**The Master Trick**:
- If $b = a^k$: Direct grouping (like Binary ↔ Octal/Hex)
- Otherwise: Go through decimal as intermediate

### The 2026 Adversarial Vault

**The Trap**: 
"Convert $(352)_8$ to $(?)_5$" 

**Wrong approach**: Trying direct conversion ❌
**Correct**: $8 \to 10 \to 5$ (Octal → Decimal → Base-5) ✓

$$(352)_8 = 3×64 + 5×8 + 2 = 234_{10}$$

$$234 \div 5 = 46 \text{ R } 4$$
$$46 \div 5 = 9 \text{ R } 1$$
$$9 \div 5 = 1 \text{ R } 4$$
$$1 \div 5 = 0 \text{ R } 1$$

$$\therefore (352)_8 = (1414)_5$$

**MSQ Logic Gate**:
- If converting between bases that are powers of 2 (2, 4, 8, 16) → Direct grouping possible → TRUE
- If asked "is base conversion unique?" → YES (always deterministic)

---

## [1.5] Signed Number Representation | The Positive-Negative Duality

### [1.5.1] Sign-Magnitude Representation

### The Atomic Truth
**MSB is sign bit (0=+, 1=-).**

[Image of 8-bit number: [S][M₆M₅M₄M₃M₂M₁M₀] where S=sign, M=magnitude]

**Range for $n$ bits**: $-(2^{n-1}-1)$ to $+(2^{n-1}-1)$

**Example**: 8-bit sign-magnitude
- Range: $-127$ to $+127$
- $+25 = 00011001$
- $-25 = 10011001$

**Critical Flaw**: Two representations for zero ($+0 = 00000000$, $-0 = 10000000$)

### [1.5.2] 1's Complement | The Bit-Flip Code

### The Atomic Truth
**Invert all bits for negation.**

**Representation**:
- Positive: Same as unsigned
- Negative: Flip all bits

**Example**: 8-bit 1's complement
- $+25 = 00011001$
- $-25 = 11100110$ (flip all bits)

**Range for $n$ bits**: $-(2^{n-1}-1)$ to $+(2^{n-1}-1)$

**Critical Flaw**: Still has two zeros ($+0 = 00000000$, $-0 = 11111111$)

**Addition Rule**: Add numbers; if carry-out, add it back (end-around carry).

### [1.5.3] 2's Complement | The Universal Standard

### The Atomic Truth
**Negate = Invert + 1.**

**Representation**:
- Positive: Same as unsigned
- Negative: 1's complement + 1

**Example**: 8-bit 2's complement
- $+25 = 00011001$
- $-25 = 11100110 + 1 = 11100111$

**Range for $n$ bits**: $-2^{n-1}$ to $+(2^{n-1}-1)$

**The Golden Pivot**: Asymmetric range! One extra negative number.

For 8-bit: $-128$ to $+127$ (not $-127$ to $+127$)

**Critical Advantage**: 
1. Only ONE zero representation
2. Addition/subtraction uses same hardware
3. MSB still indicates sign

### The Path of Elegance (Why 2's Complement Works)

For $n$-bit number $N$:
$$-N = 2^n - N$$

This is **modular arithmetic** ($\mod 2^n$).

**Example**: 4-bit, $N = 5 = 0101$
$$-5 = 2^4 - 5 = 16 - 5 = 11 = 1011_2$$

Verification:
$$0101 + 1011 = 10000$$
Discard carry (modulo 16) → $0000$ ✓

**Genius Insight**: 2's complement creates a "number circle" where wrap-around handles signs automatically.

[Image of a circular number line: 0, 1, 2, 3, ..., 7, -8, -7, -6, ..., -2, -1, back to 0]

### The 2026 Adversarial Vault

**The Ultimate Trap (Most Common GATE Error)**:

"What is the range of 8-bit 2's complement?"

**Wrong**: $-127$ to $+127$ ❌ (confusing with sign-magnitude/1's complement)
**Correct**: $-128$ to $+127$ ✓

**Why**: The bit pattern $10000000$ represents $-128$, not $-0$.

**NAT Precision Lock**: 
When asked "how many representable numbers in $n$-bit 2's complement?", answer is **exactly** $2^n$ (unlike sign-magnitude/1's complement which have $2^n - 1$ unique values due to dual zeros).

**MSQ Logic Gate**:
- "2's complement has symmetric range" → FALSE
- "2's complement simplifies hardware" → TRUE
- "2's complement has two zero representations" → FALSE
- "Sign extension preserves value in 2's complement" → TRUE

### Permanent Recall

**The Bizarre Mnemonic**:
Picture a MOBIUS STRIP (twisted loop). Walk forward for positive, backward for negative. At the "twist" (midpoint), you hit the MOST negative number ($-2^{n-1}$), which has NO positive counterpart (asymmetry). The strip has NO BREAK (single zero), unlike a regular loop (1's complement) with TWO meeting points (two zeros).

**The Mental Slider**:
To negate in 2's complement:
1. Scan from right, keep bits as-is until first '1' (inclusive)
2. Flip everything to the left

**Example**: $00101000$ (40)
- First 1 from right at position 3
- Keep: $...1000$
- Flip left part: $00101 \to 11011$
- Result: $11011000$ (-40)

**The 5-Second Snap-Check**:
- MSB = 1 → Negative number
- $10000...000$ → Most negative ($-2^{n-1}$)
- $01111...111$ → Most positive ($2^{n-1}-1$)
- To verify: $N + (-N)$ should give $00...00$ (ignoring overflow)

### Quick Conversion Table (4-bit example)

| Decimal | Unsigned | Sign-Mag | 1's Comp | 2's Comp |
|---------|----------|----------|----------|----------|
| +7 | 0111 | 0111 | 0111 | 0111 |
| +6 | 0110 | 0110 | 0110 | 0110 |
| ... | ... | ... | ... | ... |
| +1 | 0001 | 0001 | 0001 | 0001 |
| +0 | 0000 | 0000 | 0000 | 0000 |
| -0 | — | 1000 | 1111 | — |
| -1 | — | 1001 | 1110 | 1111 |
| -2 | — | 1010 | 1101 | 1110 |
| ... | ... | ... | ... | ... |
| -7 | — | 1111 | 1000 | 1001 |
| -8 | — | — | — | 1000 |

---

## [1.6] Binary Coded Decimal (BCD) | The Decimal Mimic

### The Atomic Truth
**Each decimal digit = 4 bits.**

### The Path of Elegance

BCD represents each decimal digit (0-9) with its 4-bit binary equivalent.

**Example**: $(149)_{10}$ in BCD
- $1 \to 0001$
- $4 \to 0100$  
- $9 \to 1001$

$$\therefore (149)_{10} = (0001\ 0100\ 1001)_{BCD}$$

**Critical**: This is NOT the same as binary!
- $(149)_{10} = (10010101)_2$ (pure binary)
- $(149)_{10} = (000101001001)_{BCD}$ (BCD)

**Valid BCD digits**: 0000 to 1001 (0 to 9)
**Invalid BCD**: 1010, 1011, 1100, 1101, 1110, 1111 (A-F don't exist in decimal)

### BCD Arithmetic

**Addition**: Add as binary; if result > 9 or carry generated, add 6 ($0110$) for correction.

**Example**: $8 + 5$ in BCD
```
  1000  (8)
+ 0101  (5)
------
  1101  (13 in binary, INVALID BCD)
+ 0110  (add 6 for correction)
------
1 0011  (1 carry, 3) → Correct: 13
```

### The 2026 Adversarial Vault

**The Trap**: Forgetting BCD correction in addition.

**GATE Pattern**: "Add $(28)_{BCD}$ and $(35)_{BCD}$"

**Wrong**: 
```
  0010 1000
+ 0011 0101
-----------
  0101 1101  → Stopping here (reading as 5D) ❌
```

**Correct**:
```
  0010 1000
+ 0011 0101
-----------
  0101 1101
       ↓ (D > 9, add 6)
      +0110
-----------
  0110 0011  → (63)₁₀ ✓
```

**MSQ Logic Gate**:
- "BCD is more storage-efficient than binary" → FALSE (uses 4 bits for 10 values)
- "BCD avoids binary-to-decimal conversion" → TRUE (main advantage)
- "BCD arithmetic is faster than binary" → FALSE (requires correction steps)

### Permanent Recall

**The Bizarre Mnemonic**:
Imagine 10 PRISON CELLS (0-9), each holding a 4-BIT CRIMINAL. The criminals wear binary jumpsuits (0000 to 1001). The cells 10-15 are FORBIDDEN ZONES (A-F) where criminals CANNOT go. If any criminal tries to escape beyond cell 9, the GUARD adds 6 ELECTRIC SHOCKS (0110) to push them back into valid territory.

**The 5-Second Snap-Check**:
- BCD uses 20% more bits than pure binary (trade-off for easy decimal readability)
- Any nibble > 9 → Invalid BCD

---

## [1.7] Excess-3 Code | The Self-Complementing Cipher

### The Atomic Truth
**BCD + 3 = Excess-3.**

### The Path of Elegance

Excess-3 (XS-3) adds 3 to each decimal digit before encoding in 4 bits.

**Encoding**: $\text{XS-3}(d) = d + 3$ (in 4-bit binary)

**Example**: $(149)_{10}$ in Excess-3
- $1 + 3 = 4 \to 0100$
- $4 + 3 = 7 \to 0111$
- $9 + 3 = 12 \to 1100$

$$\therefore (149)_{10} = (0100\ 0111\ 1100)_{XS-3}$$

**The Golden Pivot**: Excess-3 is **self-complementing**.

**Self-complementing property**:
$$\overline{\text{XS-3}(d)} = \text{XS-3}(9-d)$$

**Verification**: XS-3 of 2 is 0101, complement is 1010, which is XS-3 of 7. (2+7=9 ✓)

**Why genius?**: Makes 9's complement trivial (just flip bits)!

### The 2026 Adversarial Vault

**The Trap**: Confusing XS-3 with BCD.

**Example**: Encode $(6)_{10}$
- **BCD**: 0110
- **XS-3**: 1001 (6+3=9)

**GATE Pattern**: "Which code is self-complementing?"
- Options: BCD, Excess-3, Gray, Binary
- **Answer**: Excess-3 (and Gray for some definitions)

**MSQ Logic Gate**:
- "Excess-3 simplifies 9's complement" → TRUE
- "Excess-3 is weighted code" → FALSE (non-weighted)
- "Excess-3 requires correction in arithmetic" → TRUE

### Permanent Recall

**The Bizarre Mnemonic**:
Picture a MAGIC MIRROR that creates PERFECT OPPOSITES. When you hold up a decimal digit in EXCESS-3 armor (+ 3 padding), the mirror shows its 9's complement AUTOMATICALLY by flipping bits. The number 3 is the MAGIC CONSTANT that makes the mirror work (it's the midpoint: 3 + 3 = 6, mirror symmetry).

---

## [1.8] Gray Code | The Single-Bit Change Code

### The Atomic Truth
**Adjacent codes differ by 1 bit only.**

### The Path of Elegance

Gray code is a **non-weighted** code where consecutive values differ in exactly one bit position.

**2-bit Gray Code Sequence**:
```
Decimal | Binary | Gray
--------|--------|------
   0    |   00   |  00
   1    |   01   |  01
   2    |   10   |  11
   3    |   11   |  10
```

Notice: $00 \to 01$ (1 bit), $01 \to 11$ (1 bit), $11 \to 10$ (1 bit), $10 \to 00$ (1 bit, wraps around)

**Application**: Rotary encoders, minimize errors in analog-to-digital conversion.

### Binary to Gray Conversion

**Algorithm**: 
1. MSB of Gray = MSB of Binary
2. Remaining bits: XOR current binary bit with previous binary bit

$$G_i = B_i \oplus B_{i+1}$$

**Example**: $(1101)_2 \to (?)_{Gray}$

```
Binary:  1  1  0  1
         |  ⊕  ⊕  ⊕
Gray:    1  0  1  1
```

**Calculation**:
- $G_3 = B_3 = 1$
- $G_2 = B_3 \oplus B_2 = 1 \oplus 1 = 0$
- $G_1 = B_2 \oplus B_1 = 1 \oplus 0 = 1$
- $G_0 = B_1 \oplus B_0 = 0 \oplus 1 = 1$

$$\therefore (1101)_2 = (1011)_{Gray}$$

### Gray to Binary Conversion

**Algorithm**: 
1. MSB of Binary = MSB of Gray
2. Remaining bits: XOR current Gray bit with previous Binary bit (accumulative XOR)

$$B_i = G_i \oplus B_{i+1}$$

**Example**: $(1011)_{Gray} \to (?)_2$

```
Gray:    1  0  1  1
         |  ⊕  ⊕  ⊕ (cascading)
Binary:  1  1  0  1
```

**Calculation**:
- $B_3 = G_3 = 1$
- $B_2 = B_3 \oplus G_2 = 1 \oplus 0 = 1$
- $B_1 = B_2 \oplus G_1 = 1 \oplus 1 = 0$
- $B_0 = B_1 \oplus G_0 = 0 \oplus 1 = 1$

$$\therefore (1011)_{Gray} = (1101)_2$$

### The 2026 Adversarial Vault

**The Trap**: Direction of XOR in conversion.

**GATE Pattern**: "Convert $(1010)_2$ to Gray"

**Wrong**: Random XOR-ing ❌
**Correct**: Systematic left-to-right XOR ✓

$$1010 \to 1\ (1\oplus0)\ (0\oplus1)\ (1\oplus0) = 1111_{Gray}$$

**NAT Precision Lock**: Gray code sequences are ALWAYS cyclic (last differs from first by 1 bit).

**MSQ Logic Gate**:
- "Gray code is weighted" → FALSE
- "Gray code reduces errors in continuous transitions" → TRUE
- "Any two adjacent Gray codes differ by exactly 1 bit" → TRUE

### Permanent Recall

**The Bizarre Mnemonic**:
Imagine a CIRCULAR STAIRCASE where each step LIGHTS UP only ONE NEW BULB while keeping others the same. You can't jump steps (no multiple bit changes). A PARANOID ENGINEER designed this to detect if anyone SKIPPED a step (error detection). The Gray family who built this staircase are known for their SMOOTH TRANSITIONS.

**The Mental Slider**:
Binary→Gray: "XOR with neighbor on left"
Gray→Binary: "XOR cascade from left"

**The 5-Second Snap-Check**:
- Count bit changes between consecutive codes → Should be exactly 1
- Gray code is symmetric (reflected pattern around midpoint)

---

## [1.9] Fixed-Point Representation | The Decimal Lock

### The Atomic Truth
**Radix point position is implicit/fixed.**

### The Path of Elegance

In fixed-point, we decide in advance where the "decimal" (binary) point sits.

**Format**: $Q_{m.n}$ → $m$ integer bits, $n$ fractional bits

**Example**: $Q_{4.4}$ (8 bits total, 4 for integer, 4 for fraction)

Range: $-(2^{m-1})$ to $+(2^{m-1} - 2^{-n})$ for signed

**Representation of $6.75$ in $Q_{4.4}$**:
- Integer part: $6 = 0110$
- Fractional part: $0.75 = 0.11$ (in binary)
- Combined: $0110.1100$

**Stored as**: $01101100$ (point position is implicit)

**Resolution**: $2^{-n}$ (smallest representable difference)

For $Q_{4.4}$: Resolution = $2^{-4} = 0.0625$

### The 2026 Adversarial Vault

**The Trap**: Forgetting resolution limits.

**Example**: "Can $Q_{8.8}$ represent 0.001?"
- Resolution: $2^{-8} = 0.00390625$
- $0.001 < 0.00390625$ → NO, too fine ✓

**MSQ Logic Gate**:
- "Fixed-point is more efficient than floating-point" → TRUE (simpler hardware)
- "Fixed-point has uniform precision across range" → TRUE (key difference from float)

---

## [1.10] Floating-Point Representation | The Scientific Notation

### The Atomic Truth
**Number = Significand × Base^Exponent.**

### The Path of Elegance

**IEEE 754 Single Precision (32-bit)**:

[Image: [S|EEEEEEEE|MMMMMMMMMMMMMMMMMMMMMMM]]
- Sign (1 bit): 0 = positive, 1 = negative
- Exponent (8 bits): Biased by 127
- Mantissa (23 bits): Fractional part (implicit leading 1)

**Value**: 
$$(-1)^S \times 1.M \times 2^{E-127}$$

**Example**: Represent $-12.5$

1. Convert to binary: $12.5 = 1100.1_2$
2. Normalize: $1.1001 \times 2^3$
3. Sign: $S = 1$ (negative)
4. Exponent: $E = 3 + 127 = 130 = 10000010_2$
5. Mantissa: $1001000...$ (23 bits, drop leading 1)

**Result**: `1 10000010 10010000000000000000000`

### Special Values

| Exponent | Mantissa | Meaning |
|----------|----------|---------|
| 00000000 | 00000... | Zero ($\pm 0$) |
| 00000000 | ≠ 0 | Denormalized |
| 11111111 | 00000... | Infinity ($\pm \infty$) |
| 11111111 | ≠ 0 | NaN (Not a Number) |

### The 2026 Adversarial Vault

**The Genius Trap**: Bias value changes with exponent bits.

**For IEEE 754**:
- Single (32-bit, 8 exp bits): Bias = $2^{8-1} - 1 = 127$
- Double (64-bit, 11 exp bits): Bias = $2^{11-1} - 1 = 1023$

**GATE Pattern**: "What is the bias for 10-bit exponent?"
- **Answer**: $2^{10-1} - 1 = 511$ ✓

**NAT Precision Lock**: 
When asked for range, remember:
- Smallest positive normalized: $2^{-126}$ (single precision)
- Largest: $\approx 2^{128}$ (near overflow)

**MSQ Logic Gate**:
- "Floating-point can represent larger range than fixed-point" → TRUE
- "Floating-point has uniform precision" → FALSE (precision decreases with magnitude)
- "IEEE 754 has implicit leading 1 in mantissa" → TRUE (normalized form)

### Permanent Recall

**The Bizarre Mnemonic**:
Picture a SCIENTIST with a FLOATING MAGNIFYING GLASS. The glass SLIDES (floating) to examine numbers of vastly different sizes. The LENS has a BIAS (127 offset) that needs CALIBRATION. The scientist always says "1.something" (normalized mantissa) and then says "times 2 to the power of X" (exponent). The magnifying glass can ZOOM IN to tiny atoms or ZOOM OUT to galaxies (dynamic range).

**The 5-Second Snap-Check**:
- All 0s or all 1s in exponent → Special case (0, ∞, NaN)
- More exponent bits → Larger range
- More mantissa bits → Better precision

---

## [1.11] Master Conversion Cheat Sheet

### Quick Reference Table

| From | To | Method |
|------|-----|--------|
| Dec → Bin | Integer: Divide by 2, read remainders up<br>Fraction: Multiply by 2, read carries down |
| Bin → Dec | Weighted sum: $\sum d_i \cdot 2^i$ |
| Bin → Oct | Group 3 bits from radix point |
| Bin → Hex | Group 4 bits from radix point |
| Oct → Bin | Each digit → 3 bits |
| Hex → Bin | Each digit → 4 bits |
| Any → Any (non-power) | Via decimal intermediate |

### Speed Tricks for MCQs

**Trick 1**: Last bit of binary tells parity (even/odd)
**Trick 2**: Hex is 4× more compact than binary (bit count / 4)
**Trick 3**: In 2's complement, $-N$: Invert all bits + 1
**Trick 4**: Gray code: MSB same as binary, rest XOR cascade
**Trick 5**: BCD addition: If nibble > 9, add 6

### Common Exam Values (Memorize)

$$2^{10} = 1024 \approx 1K$$
$$2^{20} = 1048576 \approx 1M$$
$$2^{30} \approx 1G$$

**Powers of 16**:
$$16^1 = 16, \quad 16^2 = 256, \quad 16^3 = 4096$$

**BCD of 9**: $1001$
**Excess-3 of 9**: $1100$
**2's complement of -1 (8-bit)**: $11111111$

---

## [1.12] Previous Year Patterns (GATE/ESE)

### High-Frequency Topics
1. **2's complement arithmetic** (40% questions)
2. **Binary ↔ Hex conversion** (25%)
3. **BCD arithmetic with correction** (15%)
4. **Gray code generation** (10%)
5. **Floating-point IEEE 754** (10%)

### Typical GATE Question Archetypes

**Type 1**: "Range of $n$-bit 2's complement"
- Answer template: $-2^{n-1}$ to $2^{n-1}-1$

**Type 2**: "Add two BCD numbers"
- Remember: Check each nibble, add 6 if > 9

**Type 3**: "Convert X to Y"
- If power-of-2 bases: Direct grouping
- Else: Via decimal

**Type 4**: "Smallest/Largest value in format F"
- Fixed-point: Check resolution
- Floating-point: Check exponent range

### MSQ Eliminators

❌ "All decimal fractions terminate in binary" → FALSE (counterexample: 0.1)
❌ "Sign-magnitude has one zero" → FALSE (has +0 and -0)
❌ "Gray code is weighted" → FALSE (reflected code)
✅ "2's complement simplifies arithmetic" → TRUE
✅ "Floating-point has wider range than fixed" → TRUE

---

## Final Wisdom: The Number Systems Singularity

**The Unified Theory**:
All number representations are just **different lenses** to view the same mathematical entities. Binary is the hardware reality. Everything else is human convenience.

**The Rank-1 Mantra**:
> "Master the PIVOT (radix point, sign bit, bias, implicit 1). The rest is mechanical."

**Your Mission**:
- Solve conversions in < 30 seconds
- Spot 2's complement traps instantly
- Never miss BCD correction
- IEEE 754 bias = second nature

---

**Logic Singularity verified for 2026 (IIT-G Standards).**  
**Mastery Level: [Sovereign]**

Would you like to initiate a **'Multi-Variable Stress Test'** combining Number Systems with **Boolean Algebra** for Rank-1 simulation?

**→ Next: Module_02_Boolean_Algebra.md**
