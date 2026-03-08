# Algebra of Aptitude | The Singularity

## Scope

This note is built for **GATE, ESE, PSU, and Bank aptitude algebra**. It is designed for the **aha moment** first, then speed, then accuracy. Every section answers:

- **what** the idea is,
- **why** the formula works,
- **how** to solve fast,
- **where** top students still lose marks.

## Complexity Assessment

- **Failure cluster:** high.
- **Why candidates fall:** not because algebra is long, but because they mishandle **sign**, **domain**, **hidden restrictions**, and **translation from words to equations**.
- **IIT-G style genius trap:** the paper rarely rewards brute force; it rewards noticing the **one controlling variable** before expanding anything.

## Zero-Error Commandments

1. Never divide by an expression unless you know it is non-zero.
2. Never square both sides without checking for **extraneous roots**.
3. For logs, ensure **base \(>0\), base \(\neq 1\), argument \(>0\)**.
4. When multiplying or dividing an inequality by a negative number, **reverse the sign**.
5. In aptitude algebra, the fastest solution is often **substitution, symmetry, or factorization**, not expansion.

---

## 1. Linear Expressions and Algebraic Identities | The Singularity

### The Atomic Truth

**Patterns beat expansion.**

**Mental image:** a balance beam with two interlocking squares.

### The Path of Elegance

Start from multiplication:

$$
(a+b)^2=(a+b)(a+b)=a^2+ab+ab+b^2=a^2+2ab+b^2
$$

$$
(a-b)^2=(a-b)(a-b)=a^2-2ab+b^2
$$

Subtract the two:

$$
(a+b)^2-(a-b)^2=4ab
$$

Multiply conjugates:

$$
(a+b)(a-b)=a^2-b^2
$$

Cube identity:

$$
a^3-b^3=(a-b)(a^2+ab+b^2)
$$

because

$$
(a-b)(a^2+ab+b^2)=a^3+a^2b+ab^2-a^2b-ab^2-b^3=a^3-b^3
$$

Similarly,

$$
a^3+b^3=(a+b)(a^2-ab+b^2)
$$

### The Golden Pivot

Look for the pair \(a+b\) and \(a-b\). They are the master switches for simplification.

### Fast Use Cases

1. If \(x+\frac{1}{x}=5\), find \(x^2+\frac{1}{x^2}\).

   $$
   \left(x+\frac{1}{x}\right)^2=x^2+2+\frac{1}{x^2}
   $$

   $$
   25=x^2+\frac{1}{x^2}+2
   \Rightarrow x^2+\frac{1}{x^2}=23
   $$

2. If \(a-b=3\) and \(ab=10\), find \(a^2+b^2\).

   $$
   (a-b)^2=a^2+b^2-2ab
   $$

   $$
   9=a^2+b^2-20 \Rightarrow a^2+b^2=29
   $$

### The 2026 Adversarial Vault

- **The Inversion:** expanding everything when a square or conjugate is visible.
- **Trap:** from \(x+\frac{1}{x}=n\), students forget the \(+2\) term after squaring.
- **MSQ Logic Gate:** identities with even powers often create multiple valid values; check all signs.
- **NAT Precision Lock:** if values are close, carry exact fractions as long as possible; round only at the last line.

### Permanent Recall

- **Bizarre Mnemonic:** imagine two metal doors marked \(a+b\) and \(a-b\). When they slam together, the middle terms self-destruct, leaving \(a^2-b^2\).
- **Mental Slider:** slide \(b\) from positive to negative; watch \((a+b)^2\) morph into \((a-b)^2\), and the cross-term flips sign.
- **5-Second Snap-Check:** if your expanded square does not contain \(2ab\) or \(-2ab\), it is wrong.

---

## 2. Linear Equations and Word Translation | The Singularity

### The Atomic Truth

**Unknowns are balances.**

**Mental image:** a weighing machine with variables acting as weights.

### The Path of Elegance

A linear equation in one variable has the form

$$
ax+b=0,\quad a\neq 0
$$

Move constants, isolate the variable:

$$
ax=-b \Rightarrow x=-\frac{b}{a}
$$

For two variables,

$$
a_1x+b_1y=c_1,\qquad a_2x+b_2y=c_2
$$

Use elimination or substitution.

If the ratios satisfy

$$
\frac{a_1}{a_2}\neq \frac{b_1}{b_2}
$$

there is a unique solution.

If

$$
\frac{a_1}{a_2}= \frac{b_1}{b_2}= \frac{c_1}{c_2}
$$

there are infinitely many solutions.

If

$$
\frac{a_1}{a_2}= \frac{b_1}{b_2}\neq \frac{c_1}{c_2}
$$

there is no solution.

### The Golden Pivot

Translate the sentence into **one clean equation** before solving.

### Example

The sum of a number and its one-third is \(28\).

Let the number be \(x\).

$$
x+\frac{x}{3}=28
$$

$$
\frac{4x}{3}=28 \Rightarrow x=21
$$

### Aptitude Translation Table

- “is” \(\to =\)
- “more than” \(\to +\)
- “less than” \(\to -\)
- “of” \(\to \times\)
- “per” \(\to \div\)
- “consecutive integers” \(\to x, x+1, x+2\)

### The 2026 Adversarial Vault

- **The Inversion:** solving first, translating later.
- **Trap:** “\(5\) less than \(x\)” is \(x-5\), but “less than \(5x\)” reverses order.
- **MSQ Logic Gate:** when the system is dependent, many ordered pairs may satisfy it.
- **NAT Precision Lock:** if the variable models people, time slots, or objects, reject impossible negative answers unless the question explicitly allows them.

### Permanent Recall

- **Bizarre Mnemonic:** put every word-problem sentence on a weighing scale; if both sides do not represent the same quantity, your equation is fake.
- **Mental Slider:** move one term across the equal sign and watch its sign flip.
- **5-Second Snap-Check:** substitute the answer back into the original sentence, not only the final equation.

---

## 3. Factorization | The Singularity

### The Atomic Truth

**Break form before computation.**

**Mental image:** a lock opening into smaller gears.

### The Path of Elegance

Common factor:

$$
ax+ay=a(x+y)
$$

Quadratic form:

$$
x^2-(p+q)x+pq=(x-p)(x-q)
$$

because

$$
(x-p)(x-q)=x^2-(p+q)x+pq
$$

Grouping:

$$
ax+ay+bx+by=a(x+y)+b(x+y)=(a+b)(x+y)
$$

### The Golden Pivot

Identify the structure: common factor, identity, or grouping.

### Example

Factorize:

$$
x^2-11x+28
$$

Find two numbers whose sum is \(11\) and product is \(28\): \(7\) and \(4\).

$$
x^2-11x+28=(x-7)(x-4)
$$

### The 2026 Adversarial Vault

- **The Inversion:** hunting roots by trial while missing a common factor.
- **Trap:** \(x^2+5x+6=(x+2)(x+3)\), not \((x-2)(x-3)\).
- **MSQ Logic Gate:** after factorization, each factor can create a branch; do not lose any branch.
- **NAT Precision Lock:** in equation-solving, never cancel a factor before recording the possibility that the factor is zero.

### Permanent Recall

- **Bizarre Mnemonic:** a large machine disassembles into exact smaller gears; factorization is reverse engineering.
- **Mental Slider:** tune the middle coefficient until the product of the split terms matches the constant.
- **5-Second Snap-Check:** multiply the factors back mentally; if the middle term mismatches, rebuild.

---

## 4. Quadratic Equations | The Singularity

### The Atomic Truth

**Roots are controlled by the discriminant.**

**Mental image:** a parabola with a glowing vertex.

### The Path of Elegance

Start from

$$
ax^2+bx+c=0,\qquad a\neq 0
$$

Divide by \(a\):

$$
x^2+\frac{b}{a}x+\frac{c}{a}=0
$$

Move the constant:

$$
x^2+\frac{b}{a}x=-\frac{c}{a}
$$

Complete the square:

$$
x^2+\frac{b}{a}x+\frac{b^2}{4a^2}=\frac{b^2-4ac}{4a^2}
$$

Thus,

$$
\left(x+\frac{b}{2a}\right)^2=\frac{b^2-4ac}{4a^2}
$$

So,

$$
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
$$

Let

$$
D=b^2-4ac
$$

Then:

- \(D>0\): two distinct real roots
- \(D=0\): equal real roots
- \(D<0\): no real roots

Also, if roots are \(\alpha,\beta\), then

$$
\alpha+\beta=-\frac{b}{a}, \qquad \alpha\beta=\frac{c}{a}
$$

### The Golden Pivot

The master switch is the **discriminant** \(D\).

### Example

Solve:

$$
x^2-5x+6=0
$$

$$
(x-2)(x-3)=0
$$

So,

$$
x=2,\ 3
$$

### Shortcut Pattern

If

$$
x+\frac{1}{x}=k
$$

then

$$
x^2-kx+1=0
$$

because multiplying by \(x\) gives

$$
x^2+1=kx
$$

### The 2026 Adversarial Vault

- **The Inversion:** using the formula for every quadratic, even when factorization is immediate.
- **Trap:** forgetting that \(\sqrt{D}\) only makes real sense when \(D\ge 0\).
- **Trap:** in word problems, one root may be algebraically valid but contextually impossible.
- **MSQ Logic Gate:** when parameter-based quadratics are asked, first classify by \(D\), then apply domain restrictions.
- **NAT Precision Lock:** if \(D\) is not a perfect square, retain the radical form until the final decimal.

### Permanent Recall

- **Bizarre Mnemonic:** the discriminant is a scanner over the parabola; green means two crossings, yellow means one touch, red means no real crossing.
- **Mental Slider:** drag \(c\) up and down; the parabola shifts, and \(D\) changes the number of x-axis intersections.
- **5-Second Snap-Check:** sum of roots and product of roots must match \(-\frac{b}{a}\) and \(\frac{c}{a}\).

---

## 5. Inequalities and Modulus | The Singularity

### The Atomic Truth

**Order changes under negative scaling.**

**Mental image:** a number line with a mirror at zero.

### The Path of Elegance

Basic rule:

If \(a>b\), then

$$
a+c>b+c
$$

and for \(k>0\),

$$
ka>kb
$$

but for \(k<0\),

$$
ka<kb
$$

This sign reversal is the entire game.

Modulus definition:

$$
|x|=
\begin{cases}
x, & x\ge 0 \\
-x, & x<0
\end{cases}
$$

Therefore,

$$
|x-a|=d
$$

means the distance between \(x\) and \(a\) is \(d\), so

$$
x=a\pm d
$$

And

$$
|x-a|<d \Rightarrow a-d<x<a+d
$$

$$
|x-a|>d \Rightarrow x<a-d \text{ or } x>a+d
$$

### The Golden Pivot

The master switch is the **sign of the multiplying quantity**.

### Example

Solve:

$$
|2x-3|<5
$$

$$
-5<2x-3<5
$$

$$
-2<2x<8
$$

$$
-1<x<4
$$

### The 2026 Adversarial Vault

- **The Inversion:** squaring an inequality too early.
- **Trap:** \(|x|<a\) has solutions only when \(a>0\); if \(a\le 0\), handle separately.
- **Trap:** \(|x|=a\) has no real solution for \(a<0\).
- **MSQ Logic Gate:** boundary inclusion matters; \(<\) and \(\le\) are different universes.
- **NAT Precision Lock:** interval endpoints are often the only place marks are lost. Write them explicitly.

### Permanent Recall

- **Bizarre Mnemonic:** every negative multiplier is a trapdoor that flips the inequality arrow.
- **Mental Slider:** move \(d\) outward from the center \(a\); the allowed interval expands symmetrically.
- **5-Second Snap-Check:** test one point from each interval region before finalizing.

---

## 6. Indices, Surds, and Logarithms | The Singularity

### The Atomic Truth

**Exponents create logs; logs undo exponents.**

**Mental image:** a staircase going up as powers and down as logs.

### The Path of Elegance

For exponents:

$$
a^m\cdot a^n=a^{m+n}
$$

because repeated multiplication adds counts of factors.

$$
\frac{a^m}{a^n}=a^{m-n}, \qquad a\neq 0
$$

$$
(a^m)^n=a^{mn}
$$

Fractional powers:

$$
a^{1/n}=\sqrt[n]{a}
$$

since if \(x=a^{1/n}\), then \(x^n=a\).

For logarithms, define

$$
\log_a b = x \iff a^x=b
$$

Therefore:

$$
\log_a (mn)=\log_a m+\log_a n
$$

because if \(m=a^p\) and \(n=a^q\), then \(mn=a^{p+q}\).

Also,

$$
\log_a \left(\frac{m}{n}\right)=\log_a m-\log_a n
$$

$$
\log_a (m^r)=r\log_a m
$$

Change of base:

$$
\log_a b=\frac{\log_c b}{\log_c a}
$$

### Domain Wall

- \(a>0\)
- \(a\neq 1\)
- \(b>0\)

### The Golden Pivot

Convert between **exponential form** and **log form** without panic.

### Examples

1. Simplify:

   $$
   2^3\cdot 2^{-5}=2^{-2}=\frac{1}{4}
   $$

2. Solve:

   $$
   \log_2 (x-1)=3
   $$

   $$
   x-1=2^3=8 \Rightarrow x=9
   $$

   Domain check: \(x-1>0\Rightarrow x>1\). Valid.

3. Rationalize:

   $$
   \frac{1}{\sqrt{5}-\sqrt{2}}=\frac{\sqrt{5}+\sqrt{2}}{5-2}=\frac{\sqrt{5}+\sqrt{2}}{3}
   $$

### The 2026 Adversarial Vault

- **The Inversion:** using log rules on sums: \(\log(a+b)\neq \log a+\log b\).
- **Trap:** \(a^0=1\) only for \(a\neq 0\); \(0^0\) is undefined in elementary exam math.
- **Trap:** even roots of negative numbers are not real.
- **MSQ Logic Gate:** multiple algebraic answers can appear before domain screening; only positive arguments survive log equations.
- **NAT Precision Lock:** use natural logs or common logs consistently; switching mid-solution causes rounding drift.

### Permanent Recall

- **Bizarre Mnemonic:** exponents are elevators going up floors; logs are the security system asking, “Which floor did you come from?”
- **Mental Slider:** rotate the expression between \(a^x=b\) and \(\log_a b=x\).
- **5-Second Snap-Check:** before any log step, ask: “Is every argument positive?”

---

## 7. Ratio, Proportion, and Variation Through Algebra | The Singularity

### The Atomic Truth

**Ratios become equations when scaled.**

**Mental image:** gears linked by a single scaling rod.

### The Path of Elegance

If

$$
\frac{a}{b}=\frac{m}{n}
$$

then

$$
an=bm
$$

This is cross-multiplication, but the deeper meaning is equality of two fractions.

Direct variation:

$$
y\propto x \Rightarrow y=kx
$$

Inverse variation:

$$
y\propto \frac{1}{x} \Rightarrow y=\frac{k}{x}
$$

Joint variation:

$$
y\propto xz \Rightarrow y=kxz
$$

### The Golden Pivot

Find the constant of proportionality \(k\).

### Example

If \(y\) varies directly as \(x\), and \(y=15\) when \(x=3\), find \(y\) when \(x=8\).

$$
y=kx
$$

$$
15=3k \Rightarrow k=5
$$

$$
y=5\cdot 8=40
$$

### The 2026 Adversarial Vault

- **The Inversion:** applying direct variation where inverse variation is hidden in words like “fixed work”, “same journey”, or “constant product”.
- **Trap:** ratios compare same units; if units differ, normalize first.
- **MSQ Logic Gate:** if data are scaled by a common factor, the ratio may remain unchanged though raw values differ.
- **NAT Precision Lock:** in compound ratios, simplify before multiplying large numbers to avoid arithmetic errors.

### Permanent Recall

- **Bizarre Mnemonic:** a glowing constant \(k\) sits behind every proportional relation like an invisible controller.
- **Mental Slider:** turn \(x\) upward; in direct variation \(y\) rises with it, in inverse variation it drops.
- **5-Second Snap-Check:** ask whether the product or quotient should stay constant.

---

## 8. Progressions | The Singularity

### The Atomic Truth

**Sequences are patterns with memory.**

**Mental image:** equally spaced steps beside a multiplying spiral.

### The Path of Elegance

For an arithmetic progression:

$$
a,\ a+d,\ a+2d,\dots
$$

the \(n\)-th term is

$$
a_n=a+(n-1)d
$$

Sum of first \(n\) terms:

Write the sum forward and backward:

$$
S_n=a+(a+d)+\dots+[a+(n-1)d]
$$

$$
S_n=[a+(n-1)d]+[a+(n-2)d]+\dots+a
$$

Adding,

$$
2S_n=n[2a+(n-1)d]
$$

So,

$$
S_n=\frac{n}{2}[2a+(n-1)d]
$$

For a geometric progression:

$$
a,\ ar,\ ar^2,\dots
$$

the \(n\)-th term is

$$
a_n=ar^{n-1}
$$

Sum:

$$
S_n=a+ar+ar^2+\dots+ar^{n-1}
$$

Multiply by \(r\):

$$
rS_n=ar+ar^2+\dots+ar^n
$$

Subtract:

$$
S_n-rS_n=a-ar^n
$$

Hence for \(r\neq 1\),

$$
S_n=\frac{a(1-r^n)}{1-r}
$$

### The Golden Pivot

In AP, the master switch is \(d\). In GP, it is \(r\).

### Example

In an AP, \(a=4\), \(d=3\). Find the \(10\)-th term.

$$
a_{10}=4+9\cdot 3=31
$$

### The 2026 Adversarial Vault

- **The Inversion:** confusing term formula with sum formula.
- **Trap:** GP sum formula fails at \(r=1\); then \(S_n=na\).
- **Trap:** in AP, “difference” can be negative.
- **MSQ Logic Gate:** a decreasing AP is still an AP; a GP with \(0<r<1\) is still a GP.
- **NAT Precision Lock:** for GP decimals, keep powers exact as fractions when possible.

### Permanent Recall

- **Bizarre Mnemonic:** AP is a staircase with equal steps; GP is a spiral where each jump is scaled.
- **Mental Slider:** move \(d\) or \(r\) and watch the whole sequence reshape.
- **5-Second Snap-Check:** plug \(n=1\); the formula must return the first term \(a\).

---

## 9. Functions and Graph Sense | The Singularity

### The Atomic Truth

**Input goes in; one output comes out.**

**Mental image:** a machine taking \(x\) as input and emitting \(f(x)\).

### The Path of Elegance

A function maps each input in its domain to exactly one output.

Examples:

$$
f(x)=2x+1,\qquad f(3)=7
$$

$$
g(x)=x^2
$$

Domain restrictions matter:

- For \(\frac{1}{x}\), \(x\neq 0\)
- For \(\sqrt{x}\) over reals, \(x\ge 0\)
- For \(\log x\), \(x>0\)

### The Golden Pivot

The master switch is the **domain**.

### Example

If

$$
f(x)=x^2-3x+2
$$

then

$$
f(4)=16-12+2=6
$$

### The 2026 Adversarial Vault

- **The Inversion:** computing values without checking domain.
- **Trap:** a relation can produce valid numbers and still not be a function if one input gives two outputs.
- **MSQ Logic Gate:** domain and range statements are frequent distractors; test extreme or forbidden values.
- **NAT Precision Lock:** graph-based answers often depend on whether endpoints are included.

### Permanent Recall

- **Bizarre Mnemonic:** a strict machine rejects illegal inputs at the gate.
- **Mental Slider:** move \(x\) along the axis and watch the output track the graph.
- **5-Second Snap-Check:** before substitution, ask: “Is this input allowed?”

---

## 10. Algebraic Word-Problem Engine

### The Atomic Truth

**Model first. Solve second.**

### Universal Procedure

1. Define the unknown cleanly.
2. Translate every sentence into an equation.
3. Solve algebraically.
4. Check units, sign, and context.

### Classic Templates

#### Age Problems

Present age \(=x\).  
After \(n\) years \(=x+n\).  
\(n\) years ago \(=x-n\).

#### Work Problems

If A finishes in \(a\) days, A’s one-day work is

$$
\frac{1}{a}
$$

Together:

$$
\frac{1}{a}+\frac{1}{b}
$$

#### Speed-Distance-Time

$$
\text{Distance}=\text{Speed}\times \text{Time}
$$

Average speed is

$$
\frac{\text{Total distance}}{\text{Total time}}
$$

not the simple mean unless distances are equal.

### The 2026 Adversarial Vault

- **The Inversion:** solving with intuition before defining variables.
- **Trap:** average speed and average of speeds are not the same.
- **Trap:** work rates add, times do not.
- **Trap:** ages can be negative algebraically but impossible physically.

---

## Formula Forge: How the Key Results Are Born

### 1. Difference of Squares

$$
(a+b)(a-b)=a^2-b^2
$$

This exists because the cross terms cancel.

### 2. Quadratic Formula

Born from completing the square:

$$
ax^2+bx+c=0
\Rightarrow
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
$$

### 3. AP Sum

Born by pairing the first and last terms:

$$
S_n=\frac{n}{2}[2a+(n-1)d]
$$

### 4. GP Sum

Born by subtracting \(rS_n\) from \(S_n\):

$$
S_n=\frac{a(1-r^n)}{1-r},\quad r\neq 1
$$

### 5. Log Rules

Born directly from exponent laws:

$$
\log_a (mn)=\log_a m+\log_a n
$$

because powers multiply by adding exponents.

---

## Edge Cases That Destroy Marks

- \(0\) in denominator: undefined.
- \(0^0\): undefined for aptitude exam purposes.
- Negative inside an even root: not real.
- Negative or zero log argument: invalid.
- Squaring both sides: may introduce fake roots.
- Cancelling \((x-a)\): only legal if \(x\neq a\).
- Using \(\sqrt{x^2}=x\): wrong in general; correct form is

  $$
  \sqrt{x^2}=|x|
  $$

---

## High-Speed Solving Techniques

1. **Substitute symmetry first**

   If the expression contains \(x+\frac{1}{x}\), square once and reuse.

2. **Use Vieta before solving**

   For questions on sum/product of roots, do not compute the roots.

3. **Factor before formula**

   If coefficients are small, trial factorization is faster than the quadratic formula.

4. **Convert words into a table**

   For ages, work, mixtures, and ratio problems, structured variables cut mistakes.

5. **Check dimension and sign**

   If an answer for speed, age, or count is negative, recheck context.

---

## A-Z Revision Grid

- **A**: Algebraic identities
- **B**: Brackets and expansion
- **C**: Common factor and cancellation restrictions
- **D**: Discriminant
- **E**: Exponents
- **F**: Factorization
- **G**: GP and growth-decay pattern
- **H**: Hidden domain restrictions
- **I**: Inequalities
- **J**: Joint variation
- **K**: Constant of proportionality \(k\)
- **L**: Linear equations
- **M**: Modulus
- **N**: NAT rounding discipline
- **O**: Order of operations
- **P**: Proportion
- **Q**: Quadratic equations
- **R**: Ratio and roots
- **S**: Surds and sequences
- **T**: Translation of word problems
- **U**: Units and feasibility
- **V**: Vieta relations
- **W**: Work-rate algebra
- **X**: Unknown variable discipline
- **Y**: “Y varies as \(x\)” models
- **Z**: Zero traps

---

## Final 5-Second Snap-Check

Before locking an answer, ask:

1. Did I violate any domain rule?
2. Did I flip the inequality sign when required?
3. Did I lose or create a root during cancellation or squaring?
4. Can I verify the answer by substitution in one line?
5. Did I choose the fastest structure: factorize, substitute, or use roots directly?

---

## Pythonic Validation Notes

Every shortcut above survives edge-case scrutiny only with its conditions:

- \(a^m/a^n=a^{m-n}\) requires \(a\neq 0\).
- GP sum formula requires \(r\neq 1\).
- \(\log_a b\) requires \(a>0\), \(a\neq 1\), \(b>0\).
- \(\sqrt{x^2}=|x|\), not \(x\).
- Cross-multiplication is safe only when the denominators are defined.

If any shortcut ignores these conditions, discard it.

---

## Repository References

The following companion PDFs are already present in the same `GateOverflow` folder of this repository:

- [volume1.pdf](./volume1.pdf)
- [volume2.pdf](./volume2.pdf)

Use this note as the fast-revision, high-clarity layer. Use the PDFs as the broader practice and reference layer.

---

Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: **Sovereign**. Would you like to initiate a **Multi-Variable Stress Test** combining this with **Arithmetic and Word Problems** for a Rank-1 simulation?
