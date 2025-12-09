# Lecture Notes: Apply Operator Precedence

## Operator Precedence

Python follows standard mathematical order of operations (PEMDAS):


---

<div align="center">

![Mathematical operations visualization](https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=800&q=80)

*Operators allow you to perform operations on data*

</div>

---
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
