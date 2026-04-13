# Chapter 1: Boolean Algebra and Logic Fundamentals

## 1.1 Boolean Algebra Basics

### Topic: Boolean variables and constants
- **Binary domain**
  - Values are only `0` and `1`.
- **Logical interpretation**
  - `0 = False`, `1 = True`.

### Topic: Fundamental operators
- **`AND`, `OR`, `NOT`**
  - Symbolic forms: `·`, `+`, complement (`'`).
- **Universal gates**
  - `NAND` and `NOR` are functionally complete sets.

## 1.2 Laws and Theorems

### Topic: Core algebraic laws
- **Commutative law**
  - Order of operands does not change the result.
- **Associative law**
  - Grouping of operands does not change the result.
- **Distributive law**
  - Supports expansion and factorization forms.

### Topic: Reduction laws
- **Identity and null laws**
  - `A + 0 = A`
  - `A · 1 = A`
  - `A + 1 = 1`
  - `A · 0 = 0`
- **Idempotent and complement laws**
  - `A + A = A`
  - `A · A = A`
  - `A + A' = 1`
  - `A · A' = 0`
- **Involution and absorption**
  - `(A')' = A`
  - `A + A · B = A`
  - `A · (A + B) = A`

### Topic: De Morgan’s theorems
- **Sum-to-product dual**
  - `(A + B)' = A' · B'`
- **Product-to-sum dual**
  - `(A · B)' = A' + B'`

## 1.3 Canonical Forms and Functional Representation

### Topic: Standard forms
- **SOP (Sum of Products)**
  - Minterm-based representation.
- **POS (Product of Sums)**
  - Maxterm-based representation.

### Topic: Truth table ↔ expression mapping
- **Minterm indexing**
  - Select rows with output `1`.
- **Maxterm indexing**
  - Select rows with output `0`.
