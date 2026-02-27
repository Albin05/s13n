# Lecture Notes: Apply Operator Precedence

## Introduction

Operator precedence determines **which operations happen first** in complex expressions. Without these rules, `2 + 3 * 4` could mean either 20 or 14 - ambiguous and chaos!

---

<div align="center">

![Python Operator Precedence Table](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.12.jpg)

*Python follows PEMDAS/BODMAS rules: Parentheses → Exponents → Multiplication/Division → Addition/Subtraction*

</div>

---

### Why Precedence Rules Exist

**The problem**: Expressions can be read multiple ways
- `2 + 3 * 4` could be `(2 + 3) * 4 = 20` or `2 + (3 * 4) = 14`

**The solution**: Universal rules everyone follows

**Historical note**: These rules come from mathematics, standardized over centuries. When programming languages were invented in the 1950s, they adopted mathematical conventions so formulas would work the same way in code as on paper.

### Real-World Analogy

Think of precedence like **grammar rules** in language:
- "I saw a man with a telescope" - Who has the telescope? Grammar rules help clarify.
- Similarly, operator precedence clarifies: "2 + 3 × 4" - Math rules say multiply first

Or think of it like **traffic rules**:
- At an intersection, who goes first? Traffic rules provide the answer (stop signs, right-of-way)
- In expressions, what happens first? Precedence rules provide the answer

### The Origin of PEMDAS

**PEMDAS** is a mnemonic (memory aid) taught in schools:
- **P**arentheses
- **E**xponents
- **M**ultiplication/**D**ivision
- **A**ddition/**S**ubtraction

This order reflects mathematical convention developed over 400+ years to avoid ambiguity.

## Operator Precedence

Python follows standard mathematical order of operations (PEMDAS):


1. **Parentheses** `()`
2. **Exponentiation** `**`
3. **Multiplication, Division** `*`, `/`, `//`, `%` (left to right)
4. **Addition, Subtraction** `+`, `-` (left to right)

## Examples

```python
# Multiplication before addition
result = 2 + 3 * 4
# Evaluates as: 2 + (3 * 4) = 2 + 12 = 14

# Force different order with parentheses
result = (2 + 3) * 4
# Evaluates as: 5 * 4 = 20

# Complex expression
result = 10 + 5 * 2 - 3
# Step 1: 5 * 2 = 10
# Step 2: 10 + 10 = 20
# Step 3: 20 - 3 = 17

# With exponentiation
result = 2 + 3 ** 2 * 4
# Step 1: 3 ** 2 = 9
# Step 2: 9 * 4 = 36
# Step 3: 2 + 36 = 38
```

## Best Practice

**Use parentheses for clarity**, even when not required:

```python
# Harder to read
total = price * quantity + tax

# Clearer intent
total = (price * quantity) + tax
```

## Key Takeaways
1. Follow PEMDAS
2. Use parentheses to override
3. When unsure, add parentheses
4. Left-to-right for same precedence
