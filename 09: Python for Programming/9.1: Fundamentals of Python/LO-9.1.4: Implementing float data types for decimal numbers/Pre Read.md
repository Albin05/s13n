# Pre-Read: Implement Float Data Types

## What are Floats?

**Floats** are numbers with decimal points.

Examples: `3.14`, `0.5`, `-2.75`, `100.0`

## Creating Floats
```python
price = 19.99
height = 5.8
temperature = 98.6
pi = 3.14159
```

Even `5.0` is a float (has decimal point)!

## Float Arithmetic
```python
a = 10.5
b = 2.5

print(a + b)  # 13.0
print(a - b)  # 8.0
print(a * b)  # 26.25
print(a / b)  # 4.2
```

## Precision Surprise
```python
result = 0.1 + 0.2
print(result)  # 0.30000000000000004 (not exactly 0.3!)
```

Why? Computers store decimals in binary - some can't be represented exactly.

## When to Use Floats
✅ Prices, measurements, percentages, scientific calculations
❌ Counting, ages, years (use int)

## Try It
```python
price = 19.99
quantity = 3
total = price * quantity
print(total)  # What will this be?
```
