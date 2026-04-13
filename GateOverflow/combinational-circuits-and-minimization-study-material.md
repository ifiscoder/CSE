# Chapter 2: Combinational Circuits and Minimization

## 2.1 Logic Minimization

### Topic: Algebraic simplification
- Point: Direct theorem-based reduction
  - Subpoint: Remove redundant literals/terms

### Topic: Karnaugh map (K-map)
- Point: Grouping rules
  - Subpoint: Groups in powers of two (1, 2, 4, 8, ...)
- Point: Prime implicants and essential prime implicants
  - Subpoint: Select minimal cover with all required minterms
- Point: Don’t-care handling
  - Subpoint: Use `X` entries only when reduction improves

## 2.2 Standard Combinational Building Blocks

### Topic: Arithmetic circuits
- Point: Half adder / Full adder
  - Subpoint: Sum and carry equations
- Point: Half subtractor / Full subtractor
  - Subpoint: Difference and borrow equations

### Topic: Data routing/selection circuits
- Point: Multiplexer (MUX)
  - Subpoint: Realization of Boolean functions using MUX
- Point: Demultiplexer (DEMUX)
  - Subpoint: One-to-many controlled routing

### Topic: Coding circuits
- Point: Encoder / Priority encoder
  - Subpoint: Resolve multiple active inputs (priority rule)
- Point: Decoder
  - Subpoint: n-to-`2^n` line activation

### Topic: Comparison and parity circuits
- Point: Magnitude comparator
  - Subpoint: `A>B`, `A=B`, `A<B` outputs
- Point: Parity generator/checker
  - Subpoint: Error-detection via XOR logic
