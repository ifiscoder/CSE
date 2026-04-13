# Chapter 2: Combinational Circuits and Minimization

## 2.1 Logic Minimization

### Algebraic simplification
- Direct theorem-based reduction:
  - Use Boolean identities directly (\(A + AB = A\), \(A(A + B) = A\), \(A + A'B = A + B\), etc.).
  - Remove redundant literals/terms without changing the truth table.

### Karnaugh map (K-map)
- Grouping rules:
  - Make groups only in powers of two: \(1, 2, 4, 8, \dots\)
  - Prefer largest valid groups to reduce literals.
  - Edge wrapping is valid (top-bottom, left-right).
- Prime implicants and essential prime implicants:
  - Prime implicant: largest possible group not fully contained in another group.
  - Essential prime implicant: covers at least one minterm not covered by any other prime implicant.
  - Select a minimal cover that includes all required minterms.
- Don’t-care handling:
  - Use \(X\) entries only when they improve reduction.
  - Ignore \(X\) when they do not reduce expression complexity.

## 2.2 Standard Combinational Building Blocks

### Arithmetic circuits
- Half adder:
  - Sum: \(S = A \oplus B\)
  - Carry: \(C = AB\)
- Full adder:
  - Sum: \(S = A \oplus B \oplus C_{in}\)
  - Carry: \(C_{out} = AB + BC_{in} + AC_{in}\)
- Half subtractor:
  - Difference: \(D = A \oplus B\)
  - Borrow: \(Borrow = A'B\)
- Full subtractor:
  - Difference: \(D = A \oplus B \oplus B_{in}\)
  - Borrow: \(Borrow_{out} = A'B + A'B_{in} + BB_{in}\)

### Data routing/selection circuits
- Multiplexer (MUX):
  - Selects one of many inputs to one output using select lines.
  - Realize Boolean functions by connecting data inputs to \(0, 1,\) variables, or complements.
- Demultiplexer (DEMUX):
  - Routes one input to one of many outputs based on select lines.
  - One-to-many controlled routing.

### Coding circuits
- Encoder / Priority encoder:
  - Encoder maps active input line to binary code.
  - Priority encoder resolves multiple active inputs using a fixed priority rule.
- Decoder:
  - \(n\)-to-\(2^n\) mapping with one active output per input code.

### Comparison and parity circuits
- Magnitude comparator:
  - Outputs \(A > B\), \(A = B\), \(A < B\) for two binary numbers.
- Parity generator/checker:
  - Uses XOR/XNOR logic for single-bit error detection.
  - Even parity bit makes total number of 1s even; odd parity makes it odd.
