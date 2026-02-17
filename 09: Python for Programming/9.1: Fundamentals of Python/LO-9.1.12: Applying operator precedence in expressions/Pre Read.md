# Pre-Read: Apply Operator Precedence

## Order of Operations (PEMDAS)

Just like in math, Python follows an order:

### Why This Matters

Without order rules, expressions would be ambiguous:
```python
result = 2 + 3 * 4
```

Should this be:
- `(2 + 3) * 4 = 20`? OR
- `2 + (3 * 4) = 14`?

**The answer**: Math rules say multiply first → `14`

### Simple Analogy

Think of operator precedence like a **cafeteria line**:
- VIP customers (parentheses) go first
- Regular customers follow in order (exponents, then ×/÷, then +/−)
- Everyone waits their turn!

Or like **assembly line priority**:
- Some tasks MUST happen before others
- Multiply before you add (just like you must bake before you frost a cake)

**P**arentheses
**E**xponents
**M**ultiplication/**D**ivision (left to right)
**A**ddition/**S**ubtraction (left to right)

```python
result = 2 + 3 * 4
print(result)  # 14, not 20!
# Because: 3 * 4 happens first (12), then + 2
```

## Use Parentheses

```python
result = (2 + 3) * 4
print(result)  # 20
# Parentheses force addition first
```

## Examples

```python
# Without parentheses
print(10 + 5 * 2)    # 20 (5*2=10, then +10)

# With parentheses  
print((10 + 5) * 2)  # 30 (10+5=15, then *2)
```

## Key Point
When in doubt, use parentheses!
