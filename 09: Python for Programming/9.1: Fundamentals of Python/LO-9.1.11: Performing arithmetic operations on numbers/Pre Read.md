# Pre-Read: Perform Arithmetic Operations

## Arithmetic Operators in Python

Python supports all standard math operations plus more!

### Why Programming Needs Arithmetic

Every program you've ever used does math behind the scenes:
- **Social media**: Counting likes, calculating timestamps, sorting posts
- **Games**: Health points, damage calculations, scoreboards
- **Shopping apps**: Prices, discounts, totals, tax
- **Music players**: Track duration, progress bar position
- **Maps**: Distance calculations, estimated arrival time

Without arithmetic operators, programs would be useless - they couldn't count, calculate, or keep score!

### Simple Analogy

Think of arithmetic operators as **buttons on a calculator**:
- **+** button for addition
- **−** button for subtraction
- **×** button for multiplication
- **÷** button for division

Python gives you these same "buttons" (operators) to perform calculations in code.

The difference? A calculator handles one operation at a time. Python can perform millions of calculations per second, automatically, following your instructions!

### Basic Operations

```python
a = 10
b = 3

print(a + b)   # 13 (addition)
print(a - b)   # 7 (subtraction)
print(a * b)   # 30 (multiplication)
print(a / b)   # 3.333... (division - always float)
```

### Special Operators

**Integer Division** (`//`):
```python
print(10 // 3)  # 3 (drops decimal)
```

**Modulo/Remainder** (`%`):
```python
print(10 % 3)   # 1 (remainder)
```

**Exponentiation** (`**`):
```python
print(2 ** 3)   # 8 (2³ = 2 × 2 × 2)
```

### Augmented Assignment

Shortcuts for updating variables:

```python
score = 100
score = score + 50  # Long way
score += 50         # Short way (same thing!)
```

All operators have shortcuts:
```python
x += 5   # x = x + 5
x -= 3   # x = x - 3
x *= 2   # x = x * 2
x /= 4   # x = x / 4
```

## Try Before Class

```python
# Calculate area of rectangle
length = 10
width = 5
area = length * width
print(area)  # What will this be?

# Update score
score = 100
score += 50  # Add 50 points
score -= 25  # Lose 25 points
print(score)  # What's the final score?
```

## Key Points
- `/` always returns float, even for whole numbers
- `//` returns integer (floor division)
- `%` gives remainder (useful for even/odd checks)
- `**` is power/exponentiation
- Augmented assignment makes code cleaner
