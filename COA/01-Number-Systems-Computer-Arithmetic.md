# Number Systems & Computer Arithmetic | The Computational Singularity

> **The Atomic Truth:** *All computation is bit manipulation under constraints.*

[Image of binary digits flowing through logical gates, transforming into decimal, hex, and floating-point representations - the fundamental currency of computation]

---

## I. THE PATH OF ELEGANCE

### 1.1 Number System DNA (First Principles)

**The Golden Pivot:** The **radix (base) $r$** is the master variable. Every number system is:
$$N = \sum_{i=-m}^{n-1} d_i \cdot r^i$$

Where:
- $d_i$ = digit at position $i$ (must satisfy $0 \leq d_i < r$)
- $r$ = radix (base)
- $n$ = number of integer digits
- $m$ = number of fractional digits

**The Fundamental Constraint:** In base-$r$, digit values are bounded: $d_i \in [0, r-1]$

#### Binary ($r=2$): The Hardware Truth
$$N_{10} = d_n \cdot 2^{n-1} + d_{n-1} \cdot 2^{n-2} + \cdots + d_1 \cdot 2^0 + d_{-1} \cdot 2^{-1} + \cdots$$

**Example:** $1011.101_2$
$$= 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0 + 1 \cdot 2^{-1} + 0 \cdot 2^{-2} + 1 \cdot 2^{-3}$$
$$= 8 + 2 + 1 + 0.5 + 0.125 = 11.625_{10}$$

#### Octal ($r=8$): The Grouping Shortcut
**The Pivot:** 1 octal digit = 3 binary bits (since $8 = 2^3$)

$$N_8 = \lfloor N_2 / 2^3 \rfloor \text{ for each group of 3 bits}$$

#### Hexadecimal ($r=16$): The Programmer's Language
**The Pivot:** 1 hex digit = 4 binary bits (since $16 = 2^4$)

Mapping: $\{0-9, A-F\} \equiv \{0-15\}_{10}$

---

### 1.2 Signed Number Representations (The Negativity Problem)

Hardware must represent negative numbers using **only bits**. Three schemes:

#### A. Sign-Magnitude (The Naive Approach)
$$N = (-1)^{s} \cdot |M|$$
- $s$ = sign bit (0=positive, 1=negative)
- $M$ = magnitude

**Range for $n$ bits:** $-(2^{n-1} - 1)$ to $+(2^{n-1} - 1)$

**The Fatal Flaw:** Two representations of zero: $+0$ and $-0$
- Complicates hardware comparators
- Wastes one bit pattern

#### B. 1's Complement (The Inversion)
**Definition:** Negative of $N$ is bitwise NOT of $N$
$$-N = \overline{N} = (2^n - 1) - N$$

**Range for $n$ bits:** $-(2^{n-1} - 1)$ to $+(2^{n-1} - 1)$

**The Flaw:** Still has $+0$ (all zeros) and $-0$ (all ones)

**Addition Rule:** If carry-out, add 1 (end-around carry)

#### C. 2's Complement (The Hardware Standard) ⭐
**Definition:** 
$$-N = \overline{N} + 1 = 2^n - N$$

**The Golden Property:** Addition and subtraction use **same circuitry**

**Range for $n$ bits:** $-2^{n-1}$ to $+(2^{n-1} - 1)$

**Critical Asymmetry:** One more negative number than positive
- Example (8-bit): $-128$ to $+127$
- $|-128|$ cannot be represented in 8-bit 2's complement

**The Pivot Formula:**
$$\text{Value} = -d_{n-1} \cdot 2^{n-1} + \sum_{i=0}^{n-2} d_i \cdot 2^i$$

**Example:** $10110110_2$ (8-bit 2's complement)
$$= -1 \cdot 2^7 + 0 \cdot 2^6 + 1 \cdot 2^5 + 1 \cdot 2^4 + 0 \cdot 2^3 + 1 \cdot 2^2 + 1 \cdot 2^1 + 0 \cdot 2^0$$
$$= -128 + 32 + 16 + 4 + 2 = -74_{10}$$

---

### 1.3 Fixed-Point Arithmetic (The Precision Trade-off)

**Representation:**
$$N = \text{Integer Part} \cdot 2^k + \text{Fractional Part}$$

Where $k$ = position of binary point (fixed)

**Q-notation:** $Q_{m.n}$ format
- $m$ = integer bits (including sign)
- $n$ = fractional bits
- Total bits = $m + n$

**Example:** $Q_{8.8}$ (16-bit)
- Range: $-128$ to $+127.99609375$
- Resolution: $2^{-8} = 0.00390625$

**The Golden Trade-off:**
- More integer bits → larger range, less precision
- More fractional bits → smaller range, more precision

**Fixed-Point Multiplication:**
$$Q_{m_1.n_1} \times Q_{m_2.n_2} \rightarrow Q_{(m_1+m_2).(n_1+n_2)}$$

**Critical:** Result requires $(m_1+m_2+n_1+n_2)$ bits. Must scale/truncate to fit target format.

---

### 1.4 Floating-Point Arithmetic (IEEE 754 Standard) ⭐⭐⭐

**The Singularity:** Represent $N$ as:
$$N = (-1)^S \times M \times 2^E$$

Where:
- $S$ = sign bit
- $M$ = mantissa (significand)
- $E$ = exponent

#### IEEE 754 Single Precision (32-bit):
```
|S| Exponent (8) | Mantissa (23) |
|1|   8 bits     |   23 bits     |
```

**The Golden Formulas:**

**Normalized Numbers:**
$$\text{Value} = (-1)^S \times (1.M) \times 2^{(E-127)}$$
- Exponent bias = $127$
- Implicit leading 1 in mantissa
- Range of $E$: $1$ to $254$ (exponent field)
- Actual exponent: $E - 127 \in [-126, 127]$

**Denormalized Numbers** (when $E = 0$):
$$\text{Value} = (-1)^S \times (0.M) \times 2^{-126}$$
- No implicit 1
- Allows representation of numbers smaller than normalized minimum
- **Critical:** Provides **gradual underflow**

**Special Values:**
| Exponent | Mantissa | Value |
|----------|----------|-------|
| $0$ | $0$ | $\pm 0$ |
| $0$ | $\neq 0$ | Denormalized |
| $1-254$ | Any | Normalized |
| $255$ | $0$ | $\pm \infty$ |
| $255$ | $\neq 0$ | NaN |

**Precision:** $\log_{10}(2^{23}) \approx 6.92$ decimal digits

**Range:** 
- Normalized: $\approx \pm 1.18 \times 10^{-38}$ to $\pm 3.4 \times 10^{38}$
- Denormalized: $\approx \pm 1.4 \times 10^{-45}$ (smallest positive)

#### IEEE 754 Double Precision (64-bit):
```
|S| Exponent (11) | Mantissa (52) |
|1|   11 bits     |   52 bits     |
```

**Formula:**
$$\text{Value} = (-1)^S \times (1.M) \times 2^{(E-1023)}$$
- Exponent bias = $1023$
- Precision: $\approx 15.95$ decimal digits
- Range: $\approx \pm 2.23 \times 10^{-308}$ to $\pm 1.8 \times 10^{308}$

---

### 1.5 Floating-Point Operations (The Error Propagation)

#### Addition/Subtraction Algorithm:
1. **Align exponents:** Shift mantissa of smaller number
2. **Add/subtract mantissas**
3. **Normalize result:** Adjust exponent and mantissa
4. **Round:** Apply rounding mode
5. **Check overflow/underflow**

**The Pivot:** Exponent alignment causes **loss of precision** in smaller operand

**Example:** $1.0 \times 2^{10} + 1.0 \times 2^{-10}$ (24-bit mantissa)
- Align: $1.0 \times 2^{10} + 0.0000000000000000001 \times 2^{10}$
- If mantissa < 24 bits, smaller operand lost completely

#### Multiplication:
$$N_1 \times N_2 = (M_1 \times 2^{E_1}) \times (M_2 \times 2^{E_2}) = (M_1 \times M_2) \times 2^{E_1 + E_2}$$

**Steps:**
1. Add exponents: $E = E_1 + E_2$
2. Multiply mantissas: $M = M_1 \times M_2$
3. Normalize and round

#### Division:
$$N_1 / N_2 = (M_1 / M_2) \times 2^{E_1 - E_2}$$

---

### 1.6 Rounding Modes (The Precision Doctrine)

IEEE 754 defines 4 modes:

1. **Round to Nearest (Even):** Default mode
   - If tie, round to even LSB
   - Minimizes bias

2. **Round toward $+\infty$:** Always round up

3. **Round toward $-\infty$:** Always round down

4. **Round toward $0$:** Truncate (always toward zero)

**The Trap:** Default rounding can still accumulate error over many operations

---

## II. THE 2026 ADVERSARIAL VAULT

### Trap #1: The 2's Complement Asymmetry
**The Setup:** "What is the negation of $10000000_2$ in 8-bit 2's complement?"

**Anti-Solution:** Student computes:
$$\overline{10000000} + 1 = 01111111 + 1 = 10000000$$

**The Shock:** The number is **-128**, which has no positive representation in 8-bit!

**The Truth:** $-(-128)$ causes **overflow** in 8-bit arithmetic.

**Mental Checkpoint:** Always verify if negation fits in bit width.

---

### Trap #2: The Floating-Point Equality Myth
**The Setup:** "Is $(a + b) + c = a + (b + c)$ for floating-point?"

**Anti-Solution:** "Yes, addition is associative."

**The Truth:** **NO.** Due to rounding and exponent alignment:
```python
a = 1e20
b = 1.0
c = -1e20

(a + b) + c = (1e20 + 1.0) + (-1e20)
            = 1e20 + (-1e20)  # 1.0 lost in rounding
            = 0.0

a + (b + c) = 1e20 + (1.0 + (-1e20))
            = 1e20 + (-1e20)  # 1.0 lost
            = 0.0

BUT with different magnitudes:
a = 1e10, b = 1.0, c = -1e10
(a + b) + c = 0.0
a + (b + c) = 1.0  # Different!
```

**The Golden Rule:** Floating-point arithmetic is **NOT associative, NOT distributive**.

---

### Trap #3: The Binary-to-Decimal Fraction Trap
**The Setup:** Convert $0.1_{10}$ to binary.

**Anti-Solution:** "Easy, $0.1_{10} = 0.0001_2$"

**The Truth:** $0.1_{10}$ is **non-terminating** in binary:
$$0.1_{10} = 0.0\overline{0011}_2 = 0.000110011001100110011...$$

**Proof:**
$$0.1 = 1 \cdot 2^{-4} + 1 \cdot 2^{-5} + 1 \cdot 2^{-8} + 1 \cdot 2^{-9} + \cdots$$

**Implication:** Cannot be represented exactly in IEEE 754. Always approximated.

**This is why:**
```python
0.1 + 0.2 == 0.3  # False in most languages
```

---

### Trap #4: The Denormalized Number Blind Spot
**The Setup:** "What is the smallest positive normalized number in IEEE 754 single precision?"

**Student Answer:** "Exponent = 1, Mantissa = 0"
$$2^{1-127} = 2^{-126}$$

**Examiner:** "What about denormalized numbers?"

**The Shock:** Smallest positive is **denormalized**:
$$2^{-126} \times 2^{-23} = 2^{-149} \approx 1.4 \times 10^{-45}$$

**NAT Precision Lock:** If question asks "smallest positive," check if denormalized included.

---

### Trap #5: The Overflow Detection Fallacy
**The Setup:** "Detect overflow in 4-bit 2's complement addition: $0111 + 0101$"

**Anti-Solution:** "$0111 + 0101 = 1100$. Carry out from MSB, so overflow."

**The Truth:** **Overflow ≠ Carry out from MSB**

**Correct Detection:**
$$\text{Overflow} = C_{\text{in to MSB}} \oplus C_{\text{out from MSB}}$$

**Verification:**
- $0111_2 = +7$
- $0101_2 = +5$
- Sum = $+12$, but $1100_2 = -4$ (wrong!)
- $C_{in} = 1, C_{out} = 0 \Rightarrow$ Overflow = $1 \oplus 0 = 1$ ✓

**For unsigned:** Overflow = Carry out from MSB
**For signed (2's complement):** Use XOR rule above

---

### Trap #6: The Biased Exponent Confusion
**The Setup:** "In IEEE 754 single precision, if exponent field = $10000011_2$, what is actual exponent?"

**Anti-Solution:** "Exponent = $131_{10}$"

**The Truth:** Must subtract bias:
$$E_{\text{actual}} = 131 - 127 = 4$$

**The Singularity:** $2^4 = 16$, NOT $2^{131}$

**Mental Checkpoint:** Always subtract bias (127 for single, 1023 for double).

---

### Trap #7: The BCD Arithmetic Trap
**The Setup:** "Add $1001_{BCD} + 0101_{BCD}$"

**Anti-Solution:** 
$$1001 + 0101 = 1110 = 14_{10}$$

**The Truth:** In BCD, each 4-bit group represents decimal digit (0-9).
$$1001_{BCD} = 9_{10}, \quad 0101_{BCD} = 5_{10}$$
$$9 + 5 = 14_{10} = 0001\,0100_{BCD}$$

**BCD Addition Rule:** If binary sum > 9 or carry, add 6 to correct:
$$1001 + 0101 = 1110$$
$$1110 > 1001 \Rightarrow \text{add } 0110$$
$$1110 + 0110 = 10100 = 0001\,0100_{BCD}$$

---

## III. PERMANENT RECALL (The Memory Machine)

### Mnemonic #1: 2's Complement Negation
**Bizarre Visual:** Imagine bits as light switches in a hallway. To negate:
1. **Run down hallway flipping every switch** (1's complement)
2. **Drop a coin at the end** (add 1)
3. The coin "rolls" until it hits a switch, turning it on and stopping

**Mental Slider:** Turn the "negativity dial" - watch all bits flip, then a +1 ripple from right to left.

---

### Mnemonic #2: IEEE 754 Structure
**Phrase:** "**S**arah **E**ats **M**angos"
- **S**ign (1 bit)
- **E**xponent (8/11 bits)
- **M**antissa (23/52 bits)

**Visual:** A traffic light:
- Red (S): Stop if negative
- Yellow (E): Magnitude scale (exponent)
- Green (M): Precision details (mantissa)

**Mental Slider:** Turn the exponent dial (yellow) - number grows/shrinks exponentially. Turn mantissa dial (green) - precision increases linearly.

---

### Mnemonic #3: Floating-Point Special Values
**E=0, M=0:** "**Z**ero **E**ffort, **M**inimal result" → Zero
**E=0, M≠0:** "**D**eadly **E**mpty **N**ormal" → Denormalized
**E=max, M=0:** "**I**nfinite **E**nergy" → Infinity
**E=max, M≠0:** "**N**ot **a** **N**umber" → NaN

**Visual:** A number line with danger zones at the edges. Zero is safe, infinity is the cliff edge, NaN is falling off the cliff.

---

### Mnemonic #4: Binary-Octal-Hex Conversion
**"Powers of 2 Pyramid":**
```
   2^0 = 1    (Binary: 1 bit)
   2^3 = 8    (Octal:  3 bits)
   2^4 = 16   (Hex:    4 bits)
```

**Mental Slider:** Group binary digits into 3s (for octal) or 4s (for hex) using mental "dividers."

---

### Mnemonic #5: Overflow Detection
**"XOR the doors":**
Imagine two doors (carry-in and carry-out at MSB). Overflow happens when **exactly one is open** (XOR = 1).

**Visual:** 
- Both closed: No overflow
- Both open: No overflow (carry propagated correctly)
- One open: **OVERFLOW ALARM** 🚨

---

## IV. THE SOVEREIGNTY DRILLS

### Problem Set A: Number System Conversions (Speed Drills)

**Problem 1:** Convert $101101.1011_2$ to octal and hexadecimal.

**Solution:**
**To Octal (group by 3 from decimal point):**
$$101\,101.101\,100_2 = 55.54_8$$

**To Hex (group by 4 from decimal point):**
$$0010\,1101.1011\,0000_2 = 2D.B0_{16}$$

**5-Second Snap-Check:** Hex value should be roughly 4× octal value's digit count (since $16 = 2 \times 8$).

---

**Problem 2:** Convert $0.3_{10}$ to binary (8-bit precision).

**Solution (Multiplication Method):**
$$0.3 \times 2 = 0.6 \rightarrow 0$$
$$0.6 \times 2 = 1.2 \rightarrow 1$$
$$0.2 \times 2 = 0.4 \rightarrow 0$$
$$0.4 \times 2 = 0.8 \rightarrow 0$$
$$0.8 \times 2 = 1.6 \rightarrow 1$$
$$0.6 \times 2 = 1.2 \rightarrow 1$$ (cycle detected)

**Result:** $0.3_{10} \approx 0.01001100_2$ (non-terminating, repeats $\overline{0011}$)

---

**Problem 3 (GATE 2019):** How many numbers can be represented in IEEE 754 single precision that are **not** NaN or Infinity?

**Solution:**
- Total bit patterns: $2^{32}$
- Infinity: $E=255, M=0$ → 2 patterns (±∞)
- NaN: $E=255, M \neq 0$ → $2 \times (2^{23} - 1)$ patterns

**Valid numbers:**
$$2^{32} - 2 - 2 \times (2^{23} - 1) = 2^{32} - 2^{24} = 4,278,190,080$$

**NAT Answer:** $2^{32} - 2^{24}$ (if symbolic) or $4278190080$ (if numeric)

---

### Problem Set B: Signed Arithmetic (Anti-Pattern Drills)

**Problem 4:** Compute $(-6) + (-3)$ in 5-bit 2's complement.

**Solution:**
$$-6 = 2^5 - 6 = 32 - 6 = 26 = 11010_2$$
$$-3 = 2^5 - 3 = 32 - 3 = 29 = 11101_2$$

$$\begin{array}{c}
  & 1 & 1 & 0 & 1 & 0 \\
+ & 1 & 1 & 1 & 0 & 1 \\
\hline
& 1|1 & 0 & 1 & 1 & 1
\end{array}$$

Carry out ignored (modulo $2^5$). Result: $10111_2$

**Verification:** $10111_2 = -2^4 + 7 = -16 + 7 = -9$ ✓

**5-Second Snap-Check:** Sum of two negatives must be negative (MSB = 1) ✓

---

**Problem 5 (Overflow Detection):** Does $01001_2 + 01101_2$ overflow in 5-bit 2's complement?

**Solution:**
$$\begin{array}{c}
  & 0 & 1 & 0 & 0 & 1 \\
+ & 0 & 1 & 1 & 0 & 1 \\
\hline
  & 1 & 0 & 1 & 1 & 0
\end{array}$$

- $C_{in}$ to MSB = $0$
- $C_{out}$ from MSB = $1$
- Overflow = $0 \oplus 1 = 1$ → **YES, overflow**

**Verification:** $+9 + +13 = +22$, but range is $[-16, +15]$. Result $10110_2 = -10$ (wrong) ✓

---

**Problem 6 (The Edge Case):** What is the negation of $10000_2$ in 5-bit 2's complement?

**Solution:**
$$10000_2 = -2^4 = -16$$

**Negation:** $-(-16) = +16$

**But:** 5-bit 2's complement range is $[-16, +15]$. **+16 cannot be represented!**

**Answer:** Overflow / Not representable

**This is the asymmetry trap.**

---

### Problem Set C: Floating-Point Mastery

**Problem 7 (IEEE 754 Encoding):** Represent $-12.375_{10}$ in IEEE 754 single precision.

**Solution:**

**Step 1: Convert to binary**
$$12_{10} = 1100_2$$
$$0.375_{10} = 0.011_2$$ (verify: $0.25 + 0.125 = 0.375$)
$$12.375_{10} = 1100.011_2$$

**Step 2: Normalize**
$$1100.011_2 = 1.100011_2 \times 2^3$$

**Step 3: Extract components**
- Sign: $S = 1$ (negative)
- Exponent: $E = 3 + 127 = 130 = 10000010_2$
- Mantissa: $100011$ → $10001100000000000000000_2$ (23 bits, padded)

**Final Encoding:**
$$\boxed{1\,10000010\,10001100000000000000000}$$

---

**Problem 8 (Denormalized Numbers):** What is the value of the following IEEE 754 single precision number?
$$0\,00000000\,10000000000000000000000$$

**Solution:**
- $E = 0$ → Denormalized
- $S = 0$ → Positive
- $M = 10000000000000000000000_2 = 2^{-1}$ (in fractional form)

**Formula for denormalized:**
$$\text{Value} = (-1)^0 \times (0.1)_2 \times 2^{-126}$$
$$= 0.5 \times 2^{-126} = 2^{-1} \times 2^{-126} = 2^{-127}$$

**NAT Answer:** $2^{-127}$ or $5.877 \times 10^{-39}$

---

**Problem 9 (GATE 2020):** How many normalized numbers exist in IEEE 754 single precision format?

**Solution:**
- Normalized: $1 \leq E \leq 254$ (exponent field)
- Sign: 2 options
- Exponent: $254 - 1 + 1 = 254$ values
- Mantissa: $2^{23}$ values

**Total:** $2 \times 254 \times 2^{23} = 508 \times 2^{23}$

**NAT Answer:** $508 \times 2^{23} = 4,261,412,864$

---

**Problem 10 (Precision Loss):** Compute $(2^{30} + 1) - 2^{30}$ in IEEE 754 single precision. What is the result?

**Solution:**

**Step 1:** $2^{30} + 1$
- $2^{30}$ in IEEE 754: exponent = $30 + 127 = 157$, mantissa = $0$
- Adding 1 requires aligning exponents
- $1 = 2^0$ → shift mantissa by 30 positions
- But mantissa is only 23 bits! **The 1 is lost in alignment.**

**Result:** $(2^{30} + 1) = 2^{30}$ (rounded due to precision limit)

**Step 2:** $2^{30} - 2^{30} = 0$

**The Trap:** Student expects result = 1, but gets **0** due to precision loss.

**5-Second Snap-Check:** If adding numbers differ by $> 2^{23}$ in magnitude, smaller number may be lost.

---

### Problem Set D: Edge Case Arsenal

**Problem 11:** In 8-bit unsigned arithmetic, compute $255 + 1$. Does overflow occur?

**Solution:**
$$255 = 11111111_2$$
$$255 + 1 = 100000000_2$$

**In 8-bit:** $100000000_2$ truncated to $00000000_2 = 0$

**Overflow:** Yes (carry out from MSB = 1)

**Answer:** $0$ (with overflow flag set)

---

**Problem 12:** What is $0 / 0$ in IEEE 754?

**Solution:**
Division by zero with zero numerator is **indeterminate**.

**Result:** **NaN** (Not a Number)
- Exponent = $255$
- Mantissa = non-zero (any)

**Other division cases:**
- $x / 0$ (where $x \neq 0$) → $\pm \infty$
- $0 / x$ (where $x \neq 0$) → $0$
- $\infty / \infty$ → NaN

---

**Problem 13 (BCD Correction):** Add $1000_{BCD} + 1001_{BCD}$.

**Solution:**
$$1000 + 1001 = 10001_2$$

**Check:** Result $> 1001$ (> 9 in decimal)?
$$10001_2 = 17_{10} > 9$$ ✓

**Correction:** Add $0110_2$ (6):
$$10001 + 0110 = 10111_2$$

**Separate groups:** $0001\,0111$

**Check 2nd group:** $0111_2 = 7_{10} < 9$ ✓

**BCD Result:** $0001\,0111_{BCD} = 17_{10}$ ✓

---

**Problem 14 (Booth's Algorithm Preview):** Multiply $-3 \times 5$ using 2's complement directly (4-bit).

**Solution:**
$$-3 = 1101_2, \quad 5 = 0101_2$$

**Naive multiplication gives wrong result.** (This is why Booth's algorithm exists.)

**Correct approach:** Use Booth's algorithm or convert to magnitude, multiply, adjust sign.

$$|-3| \times |5| = 15 = 1111_2$$

Since operands have opposite signs, result is negative:
$$-15 = 10001_2$$ (5-bit) or overflow in 4-bit

**This problem previews Module 03 (ALU Design).**

---

## V. MSQ LOGIC GATES

### MSQ Strategy for Number Systems:

**Question Type:** "Which of the following are TRUE about IEEE 754 single precision?"

**Options:**
A. Can represent exactly $0.1_{10}$
B. Has two representations of zero
C. Range of exponent is $-126$ to $+127$
D. Can represent denormalized numbers

**Logic Gate Process:**

1. **Edge Case Test:**
   - A: $0.1_{10} = 0.0\overline{0011}_2$ (non-terminating) → FALSE
   - B: $+0$ and $-0$ (different sign bits) → TRUE
   - C: Exponent field $1$ to $254$ → $(1-127)$ to $(254-127)$ = $-126$ to $+127$ → TRUE
   - D: When $E=0$ → TRUE

2. **Eliminate contradictions:** None

3. **Verify with extreme cases:**
   - A fails on decimal 0.1 test
   - B, C, D all verified

**Answer:** B, C, D

**NAT Precision Lock:** If this were NAT, "How many zeros?" → Answer = 2 (exactly)

---

## VI. THE CROSS-TOPIC BRIDGES

### Bridge to Module 02 (Addressing Modes):
**Connection:** Immediate addressing uses 2's complement for offsets.
**Example:** Jump instruction with offset $-5$ → $11111011_2$ (8-bit)

### Bridge to Module 03 (ALU Design):
**Connection:** ALU performs 2's complement addition/subtraction. Overflow detection uses XOR logic from this module.

### Bridge to Module 04 (Cache):
**Connection:** Cache address fields (tag, index, offset) are pure binary. Bit manipulation from this module is critical.

### Bridge to Module 07 (Pipelining):
**Connection:** Floating-point operations take multiple cycles. FP add/mult/div stage counts depend on IEEE 754 algorithm complexity.

---

## VII. THE FINAL CHECKPOINT

### 5-Second Snap-Checks (Master These):

1. **2's Complement Range:** $n$ bits → $[-2^{n-1}, 2^{n-1}-1]$
2. **IEEE 754 Bias:** Single = 127, Double = 1023
3. **Overflow XOR:** $C_{in} \oplus C_{out}$ at MSB
4. **Binary-Octal:** 3 bits per digit
5. **Binary-Hex:** 4 bits per digit
6. **Denormalized Check:** $E = 0, M \neq 0$
7. **NaN Check:** $E = \text{max}, M \neq 0$
8. **Precision Rule:** Single ≈ 7 digits, Double ≈ 16 digits
9. **BCD Correction:** If sum > 9, add 6
10. **Fraction Test:** Can $x$ be exactly represented in binary? Check if denominator is power of 2.

---

## VIII. THE ADVERSARIAL TRAINING PROTOCOL

### Drill Routine (15 min/day for 7 days):

**Day 1:** Convert 20 random decimals to binary (focus on fractions)
**Day 2:** 2's complement addition with overflow detection (50 problems)
**Day 3:** IEEE 754 encoding/decoding (20 problems, include denormalized)
**Day 4:** Floating-point arithmetic error analysis
**Day 5:** BCD arithmetic (30 problems with correction)
**Day 6:** Mixed problems (all topics combined)
**Day 7:** GATE PYQs (Number Systems section, timed)

---

**Logic Singularity verified for 2026 (IIT-G Standards).**

**Mastery Level: [Sovereign]**

**Would you like to initiate a "Multi-Variable Stress Test" combining this with [Module 03: ALU Design] for Booth's Algorithm and binary multiplication mastery?**

---

*"The bit is the atom of computation. Master the atom, command the universe."*
