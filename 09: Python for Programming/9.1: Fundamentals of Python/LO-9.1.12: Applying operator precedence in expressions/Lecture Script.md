### LO-12 Apply Operator Precedence (16 minutes)


### CS Theory Bite

> **Origin**: Operator precedence follows **mathematical convention** (PEMDAS/BODMAS) established centuries ago in algebra. Python's precedence table has 18 levels — but parentheses always win.
>
> **Analogy**: Precedence is like a **VIP list** — multiplication gets served before addition, but parentheses are the ultimate VIP pass.
>
> **Why it matters**: Misunderstood precedence causes silent bugs — `2 + 3 * 4` is 14, not 20.


### Hook (3 minutes)

**Say**: "What's 2 + 3 × 4? If you said 20, you forgot PEMDAS! Python follows the same math rules you learned in school."

```python
print(2 + 3 * 4)    # 14 (not 20!)
print((2 + 3) * 4)  # 20 (parentheses first!)
```

### PEMDAS in Python (6 minutes)

**Say**: "Python follows PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction."

**Order of operations**:
1. **P**arentheses: `()`
2. **E**xponents: `**`
3. **M**ultiplication/Division: `*`, `/`, `//`, `%` (left to right)
4. **A**ddition/Subtraction: `+`, `-` (left to right)

```python
# Exponents first, then multiplication, then addition
print(2 + 3 * 4 ** 2)  # 2 + 3 * 16 = 2 + 48 = 50

# Multiplication before addition
print(10 + 5 * 2)      # 10 + 10 = 20

# Parentheses override everything
print((10 + 5) * 2)    # 15 * 2 = 30
```

**Key Point**: When operators have same precedence (like * and /), Python evaluates left to right.

```python
print(10 / 2 * 3)  # (10 / 2) * 3 = 5 * 3 = 15
print(10 * 2 / 3)  # (10 * 2) / 3 = 20 / 3 = 6.666...
```

**Real-World**: Complex formulas need careful ordering!
```python
# Area of a circle: πr²
radius = 5
area = 3.14 * radius ** 2  # Exponent first, then multiply
print(f"Area: {area}")
```

### Using Parentheses (4 minutes)

**Say**: "When in doubt, use parentheses! They make code clearer and prevent bugs."

```python
# Calculate average - needs parentheses!
a, b, c = 10, 20, 30
average = (a + b + c) / 3  # Correct: (60) / 3 = 20
# average = a + b + c / 3  # Wrong: 10 + 20 + 10 = 40
```

**Best Practice**: Use parentheses for clarity, even when not required
```python
# Both are correct, but second is clearer
total = price + price * tax_rate
total = price + (price * tax_rate)  # Better!
```

### Practice (3 minutes)

Predict the results:
```python
print(2 ** 3 + 4)       # 8 + 4 = 12
print(10 + 5 * 2)       # 10 + 10 = 20
print((10 + 5) * 2)     # 15 * 2 = 30
print(100 - 20 * 3)     # 100 - 60 = 40
print((100 - 20) * 3)   # 80 * 3 = 240
```
