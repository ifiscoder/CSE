# Chapter 11: Previous Year Questions (GATE/ESE)

## 🎯 Practice Makes Perfect

---

## Section A: Lexical Analysis Questions

### Q1. (GATE 2019)
**Consider the following statements:**
1. The set of all strings over {a, b} that start and end with 'a' is regular.
2. The set of all strings over {a, b} with equal number of a's and b's is regular.

Which of the above is/are TRUE?

**Solution:**
- Statement 1: TRUE. RE = `a(a|b)*a | a`
- Statement 2: FALSE. This requires counting (context-free, not regular)

**Answer: Only Statement 1**

---

### Q2. (GATE 2018)
**The minimum number of states in a DFA that accepts the language L = {w | w ∈ {0,1}* and w has an even number of 1s}**

**Solution:**
States track parity of 1s:
- q0: Even number of 1s (start and accept)
- q1: Odd number of 1s

```
Transitions:
q0 --0--> q0
q0 --1--> q1
q1 --0--> q1
q1 --1--> q0
```

**Answer: 2 states**

---

### Q3. (GATE 2016)
**Consider the regular expression (0+1)(0+1)....(0+1) with n (0+1)s. The minimum number of states in DFA that recognizes this language is:**

**Solution:**
Language = All binary strings of length exactly n
- Need to count positions: 0, 1, 2, ..., n characters seen
- Need n+2 states: q0, q1, ..., qn (accepting), and dead state

**Answer: n + 2 states**

---

## Section B: Parsing Questions

### Q4. (GATE 2020)
**For the grammar:**
```
S → aABe
A → Abc | b
B → d
```
**Compute FIRST and FOLLOW sets.**

**Solution:**

**FIRST Sets:**
- FIRST(S) = {a}
- FIRST(A) = {b} (A → Abc starts with A which → b)
- FIRST(B) = {d}

**FOLLOW Sets:**
- FOLLOW(S) = {$}
- FOLLOW(A) = {b, d} (from A → Abc: FIRST(bc) = {b}; from S → aABe: FIRST(B) = {d})
- FOLLOW(B) = {e} (from S → aABe)

---

### Q5. (GATE 2019)
**Consider the grammar:**
```
E → E + T | T
T → T * F | F  
F → id
```
**How many items are in the canonical collection of LR(0) items?**

**Solution:**
Augmented grammar: E' → E

Items:
```
E' → •E, E' → E•
E → •E+T, E → E•+T, E → E+•T, E → E+T•
E → •T, E → T•
T → •T*F, T → T•*F, T → T*•F, T → T*F•
T → •F, T → F•
F → •id, F → id•
```

Total: 2 + 4 + 2 + 4 + 2 + 2 = **16 items**

---

### Q6. (GATE 2017)
**Given grammar:**
```
S → AS | b
A → SA | a
```
**Is this grammar LL(1)?**

**Solution:**
Check for LL(1) conditions:

FIRST(AS) = FIRST(A) = {a} ∪ FIRST(S) = {a, b}
FIRST(b) = {b}

For S → AS | b:
- FIRST(AS) = {a, b}
- FIRST(b) = {b}
- FIRST(AS) ∩ FIRST(b) = {b} ≠ ∅

**Answer: NO, not LL(1)** (conflict on 'b')

---

### Q7. (GATE 2015)
**Consider the grammar:**
```
S → Aa | bAc | dc | bda
A → d
```
**This grammar is:**
(a) LL(1) (b) SLR(1) but not LL(1) (c) LALR(1) but not SLR(1) (d) Not LALR(1)

**Solution:**

For LL(1), check productions with same LHS:
- S → Aa | bAc | dc | bda

For S with input 'b': 
- FIRST(bAc) = {b}
- FIRST(bda) = {b}
- Conflict! Not LL(1)

For SLR(1), construct item sets...
[After analysis, this is SLR(1)]

**Answer: (b) SLR(1) but not LL(1)**

---

### Q8. (GATE 2014)
**For the grammar E → E + E | E * E | id, and string id + id * id, how many parse trees are possible?**

**Solution:**
This grammar is ambiguous. For id + id * id:

**Parse Tree 1:** (id + id) * id
```
        E
      / | \
     E  *  E
    /|\    |
   E + E  id
   |   |
  id  id
```

**Parse Tree 2:** id + (id * id)
```
        E
      / | \
     E  +  E
     |    /|\
    id   E * E
         |   |
        id  id
```

**Answer: 2 parse trees**

---

## Section C: SDT Questions

### Q9. (GATE 2018)
**Consider the SDT:**
```
S → aA    {A.i = 2}
A → b     {S.s = A.i + 1}
```
**What is the value of S.s for input "ab"?**

**Solution:**
- Parse "ab" using S → aA, A → b
- A.i = 2 (inherited, set by S)
- S.s = A.i + 1 = 2 + 1 = 3

**Answer: 3**

---

### Q10. (GATE 2016)
**Identify the type of attribute definition:**
```
E → E₁ + T    { E.val = E₁.val + T.val }
E → T         { E.val = T.val }
T → T₁ * F    { T.val = T₁.val * F.val }
T → F         { T.val = F.val }
F → num       { F.val = num.lexval }
```

**Solution:**
All attributes are computed from children's attributes (RHS to LHS).
These are all **synthesized attributes**.

**Answer: S-attributed definition**

---

## Section D: Intermediate Code Questions

### Q11. (GATE 2019)
**Generate TAC for: a = b * -c + b * -c**

**Solution:**
```
t1 = -c
t2 = b * t1
t3 = -c
t4 = b * t3
t5 = t2 + t4
a = t5
```

With CSE optimization:
```
t1 = -c
t2 = b * t1
t3 = t2 + t2
a = t3
```

**Number of temporaries (without optimization): 5**
**Number of temporaries (with CSE): 3**

---

### Q12. (GATE 2017)
**For the expression (a+b)*(c+d)+(a+b), how many nodes will the DAG have?**

**Solution:**
DAG shares common subexpression (a+b):

```
Nodes:
1. a (leaf)
2. b (leaf)
3. + (for a+b) - SHARED
4. c (leaf)
5. d (leaf)
6. + (for c+d)
7. * (for (a+b)*(c+d))
8. + (for result)
```

**Answer: 8 nodes** (not 10, because a+b is computed once)

---

### Q13. (GATE 2015)
**Represent x = y + z * w in quadruples and triples.**

**Quadruples:**
| # | op | arg1 | arg2 | result |
|---|----|------|------|--------|
| 0 | * | z | w | t1 |
| 1 | + | y | t1 | t2 |
| 2 | = | t2 | - | x |

**Triples:**
| # | op | arg1 | arg2 |
|---|----|------|------|
| 0 | * | z | w |
| 1 | + | y | (0) |
| 2 | = | x | (1) |

---

## Section E: Runtime Environment Questions

### Q14. (GATE 2018)
**Consider the following C code:**
```c
void foo(int *x, int y) {
    *x = y + 1;
    y = y + 1;
}
int main() {
    int a = 1, b = 2;
    foo(&a, b);
    printf("%d %d", a, b);
}
```
**What is printed?**

**Solution:**
- x is passed by reference (pointer), y by value
- *x = y + 1 → *x = 2 + 1 = 3 → a = 3
- y = y + 1 → local y becomes 3 (doesn't affect b)

**Answer: 3 2**

---

### Q15. (GATE 2016)
**What is the maximum stack depth for recursive factorial(n)?**

**Solution:**
```
factorial(n) calls factorial(n-1) ... factorial(1)
```
Call stack: n activation records (factorial(n), factorial(n-1), ..., factorial(1))

**Answer: n** (or n+1 if counting main)

---

### Q16. (GATE 2014)
**In a call by copy-restore, given:**
```
procedure P(x, y) {
    x = x + 1;
    y = y + 1;
}
a = 0;
P(a, a);
```
**What is the value of a after the call?**

**Solution:**
Call by copy-restore:
1. Copy a to x and y: x = 0, y = 0
2. Execute: x = 1, y = 1
3. Copy back: a = x = 1, then a = y = 1

Last copy wins: **a = 1**

---

## Section F: Optimization Questions

### Q17. (GATE 2019)
**Identify the basic blocks in:**
```
1. i = 1
2. j = 1
3. t1 = 10 * i
4. t2 = t1 + j
5. if t2 < 100 goto 3
6. i = i + 1
7. if i <= 10 goto 2
8. ...
```

**Solution:**
Leaders:
- 1 (first statement)
- 3 (target of goto 3)
- 6 (after conditional goto)
- 8 (after conditional goto)

Basic Blocks:
- B1: 1, 2
- B2: 3, 4, 5
- B3: 6, 7
- B4: 8, ...

**Answer: 4 basic blocks**

---

### Q18. (GATE 2017)
**Which optimization is applied?**
```
Before:              After:
t1 = a * b           t1 = a * b
t2 = a * b           t2 = t1
t3 = t1 + t2         t3 = t1 + t1
```

**Answer: Common Subexpression Elimination (CSE)**

---

### Q19. (GATE 2015)
**Which of the following cannot be done by a compiler?**
(a) Remove dead code
(b) Detect infinite loops
(c) Constant folding
(d) Loop invariant code motion

**Solution:**
(b) Detect infinite loops - This is the halting problem, undecidable!

**Answer: (b)**

---

## Section G: Code Generation Questions

### Q20. (GATE 2018)
**How many registers are needed to evaluate (a+b)*(c+d) without spilling?**

**Solution:**
Using Ershov numbers:
```
        *
       / \
      +   +
     /|   |\
    a b   c d
    
Labels:
    a=1, b=0 → + = max(1,0) = 1
    c=1, d=0 → + = max(1,0) = 1
    * = 1 + 1 = 2 (equal children)
```

**Answer: 2 registers**

---

### Q21. (GATE 2016)
**Generate target code for:**
```
t1 = a + b
t2 = t1 * c
```
**Using 2 registers R0, R1.**

**Solution:**
```
LD a, R0        ; R0 = a
LD b, R1        ; R1 = b
ADD R1, R0      ; R0 = a + b = t1
LD c, R1        ; R1 = c
MUL R1, R0      ; R0 = t1 * c = t2
ST R0, t2       ; Store result
```

---

## Section H: Error Handling Questions

### Q22. (GATE 2017)
**Match the error with the phase that detects it:**
1. Missing semicolon
2. Undeclared variable
3. Illegal character

**Solution:**
1. Missing semicolon → **Syntax Analysis**
2. Undeclared variable → **Semantic Analysis**
3. Illegal character → **Lexical Analysis**

---

## Section I: Mixed/Tricky Questions

### Q23. (GATE 2019)
**Which of the following is true?**
(a) Every LL(1) grammar is LALR(1)
(b) Every LALR(1) grammar is LL(1)
(c) Every SLR(1) grammar is LL(1)
(d) Every LL(1) grammar is SLR(1)

**Solution:**
Grammar power hierarchy: LL(1) ⊂ SLR(1) ⊂ LALR(1) ⊂ CLR(1)

**Answer: (a) Every LL(1) grammar is LALR(1)** ✓

---

### Q24. (GATE 2018)
**A language L is regular if and only if:**
(a) It can be recognized by a PDA
(b) It can be generated by a CFG
(c) It can be accepted by a DFA
(d) It can be generated by a Type-0 grammar

**Solution:**
(c) is the definition of regular language.

**Answer: (c)**

---

### Q25. (GATE 2016)
**For compiling n source languages to m target machines, how many compilers are needed with and without using IR?**

**Solution:**
- Without IR: n × m compilers
- With IR: n front-ends + m back-ends = n + m

**Answer: n×m without IR, n+m with IR**

---

## 🎯 Key Takeaways

### Most Frequent Topics
1. **FIRST/FOLLOW computation** - Every year
2. **LL(1) and SLR conflicts** - Every year
3. **Basic block identification** - Very common
4. **TAC generation** - Common
5. **Parameter passing** - Occasional
6. **Register counting** - Occasional

### Common Tricks
1. Read question carefully - many have subtle wording
2. Check for ε in FIRST before computing FOLLOW
3. Remember $ in FOLLOW(Start)
4. Verify ambiguity by finding 2 parse trees
5. For optimization questions, identify exact optimization type

---

*Logic Singularity verified for 2026 (IIT-G Standards). Problem Solving Complete.*
