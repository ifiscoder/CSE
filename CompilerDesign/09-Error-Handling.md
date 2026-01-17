# Chapter 9: Error Handling

## 🎯 The Atomic Truth
> **"Error Handling = Detect, Report, Recover, Continue"**

---

## 9.1 What is Error Handling?

### Definition
**Error Handling** encompasses the detection, reporting, and recovery from errors that occur during compilation, allowing the compiler to continue processing and find more errors.

```
┌────────────────────────────────────────────────────────────────────────┐
│                         ERROR HANDLING                                 │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   ┌─────────────┐      ┌─────────────────┐      ┌─────────────────┐   │
│   │   Source    │      │    COMPILER     │      │     Error       │   │
│   │   Code      │ ──►  │    + ERROR      │ ──►  │    Reports      │   │
│   │ (with bugs) │      │    HANDLER      │      │   (helpful!)    │   │
│   └─────────────┘      └─────────────────┘      └─────────────────┘   │
│                                                                        │
│   Goals:                                                               │
│   • Detect errors accurately                                          │
│   • Report errors clearly                                             │
│   • Recover quickly                                                   │
│   • Don't get confused by cascading errors                           │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### 🧠 Analogy: The Proofreader
An error handler is like a proofreader who:
- Spots mistakes (detection)
- Marks them with explanations (reporting)
- Keeps reading despite errors (recovery)
- Doesn't flag the same issue repeatedly (avoiding cascades)

---

## 9.2 Types of Errors

### Classification by Phase

| Phase | Error Type | Examples |
|-------|------------|----------|
| **Lexical** | Token errors | Illegal character, malformed number |
| **Syntax** | Grammar errors | Missing semicolon, unbalanced parens |
| **Semantic** | Meaning errors | Type mismatch, undeclared variable |
| **Logical** | Program logic | Infinite loops, wrong algorithm |

### Classification by Severity

| Severity | Description | Action |
|----------|-------------|--------|
| **Warning** | Suspicious but valid | Continue compilation |
| **Error** | Invalid, cannot generate code | Report, try to recover |
| **Fatal** | Cannot continue | Abort compilation |

### Examples by Type

#### Lexical Errors
```c
int x = 0x3G;      // Invalid hex digit
char c = 'ab';     // Malformed character literal
string s = "hello  // Unterminated string
```

#### Syntax Errors
```c
if x > 0           // Missing parentheses: if (x > 0)
int 123abc;        // Identifier cannot start with digit
while (x < y       // Missing closing parenthesis
```

#### Semantic Errors
```c
int x = "hello";   // Type mismatch
printf("%d", y);   // y not declared
int arr[10];
arr[10] = 5;       // Array index out of bounds (if detectable)
```

---

## 9.3 Error Detection by Phase

### 9.3.1 Lexical Error Detection
**What's caught:**
- Unrecognized characters
- Malformed tokens (numbers, strings)
- Unterminated strings/comments

**What's NOT caught:**
- Using wrong keyword (`fro` instead of `for`)
- Misspelled identifiers

```
Scanner State Machine:
    If no transition for input character → ERROR
    If end of input in middle of token → ERROR
```

### 9.3.2 Syntax Error Detection
**What's caught:**
- Missing tokens (semicolons, brackets)
- Extra tokens
- Wrong token order
- Unbalanced constructs

**Detection in Parsing:**
```
LL(1): Parsing table entry is empty
LR: No valid action in parsing table
Recursive Descent: Unexpected token encountered
```

### 9.3.3 Semantic Error Detection
**What's caught:**
- Type mismatches
- Undeclared identifiers
- Duplicate declarations
- Scope violations
- Argument count mismatch

**Detection Method:**
- Symbol table lookups
- Type checking rules
- Scope management

---

## 9.4 Error Recovery Strategies

### 9.4.1 Panic Mode Recovery

**Concept:** Skip input until a "synchronizing token" is found.

**Synchronizing Tokens:** Statement delimiters like `;`, `}`, keywords like `end`, `while`

```
When error detected:
    1. Report error
    2. Discard tokens until sync token found
    3. Resume normal parsing
```

**Advantages:**
- Simple to implement
- Never loops infinitely

**Disadvantages:**
- May skip valid code
- May miss errors in skipped region

### Example
```c
int x = 10 20;      // Error: missing operator
int y = 30;         // Resume here (after ;)
```

### 9.4.2 Phrase-Level Recovery

**Concept:** Make local corrections to continue parsing.

**Actions:**
- Insert missing token
- Delete extra token
- Replace one token with another

```
if (x < y
    z = 1;

Recovery: Insert missing )
    if (x < y)
```

**Advantages:**
- More graceful than panic mode
- Fewer false errors

**Disadvantages:**
- May introduce additional errors
- Complex to implement well

### 9.4.3 Error Productions

**Concept:** Add grammar productions that match common errors.

```
Original Grammar:
    stmt → if ( expr ) stmt

With Error Production:
    stmt → if ( expr ) stmt
         | if expr stmt { error("Missing parentheses") }
```

**Advantages:**
- Catches specific common errors
- Can give precise error messages

**Disadvantages:**
- Increases grammar size
- Cannot anticipate all errors

### 9.4.4 Global Correction

**Concept:** Find minimum changes to make program valid.

**Approach:** Compute minimum edit distance to valid program.

**Advantages:**
- Theoretically optimal

**Disadvantages:**
- Very expensive (impractical for large programs)
- Only used in theoretical discussions

---

## 9.5 Error Recovery in Parsers

### 9.5.1 LL(1) Parser Error Recovery

**When Error Detected:** `M[A, a] = empty`

**Recovery Options:**
1. **Panic mode:** Pop until synchronizing symbol
2. **Insert:** If `a ∈ FOLLOW(A)`, pop A (pretend it derived ε)
3. **Delete:** Skip input token a

### 9.5.2 LR Parser Error Recovery

**When Error Detected:** `ACTION[s, a] = empty`

**Recovery:**
1. Pop states until one with goto on error symbol
2. Shift error symbol
3. Discard input until something acceptable
4. Resume parsing

### Shift-Reduce Error Recovery
```
Stack: ... E + (     State: s5
Input: ) ...         (mismatched parenthesis)

Recovery:
    1. Report "unbalanced parenthesis"
    2. Pop states for incomplete expression
    3. Skip to ; or other sync token
    4. Continue parsing
```

---

## 9.6 Error Reporting

### Good Error Messages Have:

1. **Location:** Line number, column, file name
2. **Description:** What's wrong
3. **Context:** Show the offending code
4. **Suggestion:** How to fix (if possible)

### Example: Good vs Bad Error Messages

**Bad:**
```
Error at line 10
```

**Good:**
```
error: line 10, column 15: expected ';' before 'int'
    10 |     x = 5 int y = 10;
       |           ^^^
       | Did you forget a semicolon after 'x = 5'?
```

### Error Message Guidelines
- Be specific, not generic
- Point to exact location
- Suggest corrections when obvious
- Don't blame the user
- Group related errors

---

## 9.7 Avoiding Cascading Errors

### Problem
One error can cause many false error reports.

```c
int x = ;           // Primary error
y = x + 1;          // Secondary: "x is undefined" (false)
z = y * 2;          // Secondary: "y is undefined" (false)
```

### Solutions

1. **Error Recovery:** Fix first error, continue
2. **Error Limit:** Stop after n errors
3. **Error Suppression:** Don't report errors near previous ones
4. **Synchronization:** Skip to clear state before continuing

---

## 9.8 Semantic Error Handling

### Type Error Handling
```c
int x = "hello";    // Error: cannot assign string to int

Recovery:
    - Report error
    - Treat x as having declared type (int)
    - Continue checking other statements
```

### Undeclared Variable Handling
```c
y = x + 1;          // x not declared

Recovery:
    - Report "x undeclared"
    - Add x to symbol table with "unknown" type
    - Don't report x as undeclared again
```

### Scope Error Handling
```c
{
    int x = 1;
}
x = 2;              // Error: x not in scope

Recovery:
    - Report "x not declared in this scope"
    - Perhaps suggest the inner x
```

---

## 9.9 Error Handler Design

### Components

```
┌─────────────────────────────────────────────────────────────────┐
│                     ERROR HANDLER                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌──────────────────────────────────────────────────────┐     │
│   │              Error Reporter                           │     │
│   │  • Format error messages                              │     │
│   │  • Track locations                                    │     │
│   │  • Manage error count                                 │     │
│   └──────────────────────────────────────────────────────┘     │
│                           │                                     │
│   ┌──────────────────────────────────────────────────────┐     │
│   │              Error Recoverer                          │     │
│   │  • Panic mode logic                                   │     │
│   │  • Phrase-level corrections                           │     │
│   │  • Sync token handling                                │     │
│   └──────────────────────────────────────────────────────┘     │
│                           │                                     │
│   ┌──────────────────────────────────────────────────────┐     │
│   │              Error State Manager                      │     │
│   │  • Track error mode (in recovery or not)              │     │
│   │  • Cascade prevention                                 │     │
│   │  • Error counting                                     │     │
│   └──────────────────────────────────────────────────────┘     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Implementation Sketch
```c
void reportError(int line, int col, char* msg) {
    errorCount++;
    printf("Error [%d:%d]: %s\n", line, col, msg);
    showSourceContext(line, col);
    
    if (errorCount > MAX_ERRORS) {
        printf("Too many errors. Stopping.\n");
        exit(1);
    }
}

void panicModeRecovery(TokenSet syncTokens) {
    while (!isIn(currentToken, syncTokens) && currentToken != EOF) {
        advance();
    }
    // Now at sync point, resume parsing
}
```

---

## 9.10 Error Handling in Different Compilers

### GCC Error Handling
- Very detailed messages
- Points to exact location with caret (^)
- Often suggests fixes
- Color-coded output

### Clang Error Handling
- Known for excellent error messages
- Shows "fix-it" hints
- Explains what went wrong and why

### Example (Clang-style)
```
test.c:5:10: error: use of undeclared identifier 'foo'
    int x = foo + 1;
            ^~~
test.c:5:10: note: did you mean 'fo' (declared at line 3)?
    int fo = 5;
        ^~
```

---

## 9.11 GATE Previous Year Patterns

### Pattern 1: Error Type Identification
**Q:** Which phase detects "undeclared variable"?
**A:** Semantic analysis

### Pattern 2: Recovery Strategy
**Q:** What is panic mode recovery?
**A:** Skip input until synchronizing token found.

### Pattern 3: Error Classification
**Q:** Classify given error (lexical/syntax/semantic).
**Approach:** Based on what rule is violated.

---

## 📝 Quick Revision Points

1. **Lexical Errors:** Bad tokens, illegal characters
2. **Syntax Errors:** Grammar violations
3. **Semantic Errors:** Type/scope/declaration issues
4. **Panic Mode:** Skip to sync token
5. **Phrase-Level:** Local corrections
6. **Error Productions:** Grammar rules for errors
7. **Cascading:** One error causes many false errors
8. **Good Messages:** Location + description + context + fix
9. **Recovery Goal:** Continue to find more errors
10. **Sync Tokens:** `;`, `}`, keywords

---

## 🧠 Mnemonic Summary

### Error Types by Phase
> **"Lex sees letters, Syn sees structure, Sem sees sense"**

### Recovery Strategies
> **"Panic Skips, Phrase Fixes, Productions Match"**

### Good Error Messages
> **"LCDS: Location, Context, Description, Suggestion"**

---

## 🔥 The Adversarial Vault

### Trap 1: Logical Errors
**Q:** Does compiler detect infinite loops?
**A:** NO! Logical errors cannot be detected by compilers (halting problem).

### Trap 2: Error Phase
**Q:** "Missing semicolon" - lexical or syntax?
**A:** SYNTAX! Semicolon is a valid token; the error is in how tokens are combined.

### Trap 3: Recovery Completeness
**Q:** Can error recovery always find all errors?
**A:** NO! Recovery may skip code containing errors.

---

## ✅ Self-Assessment Questions

1. Classify these errors: `int 5x`, `if x>y`, `int x = "hi"`
2. Describe panic mode recovery with example.
3. Why do cascading errors occur? How to prevent?
4. Write a good error message for missing `}`.
5. When is phrase-level recovery preferred over panic mode?

---

**Next Chapter:** [Quick Revision →](10-Quick-Revision.md)

---

*Logic Singularity verified for 2026 (IIT-G Standards). Mastery Level: Sovereign.*
