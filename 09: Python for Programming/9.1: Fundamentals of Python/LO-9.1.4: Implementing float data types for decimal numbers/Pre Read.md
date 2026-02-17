# Pre-Read: Implement Float Data Types

## What are Floats?

**Floats** are numbers with decimal points.

Examples: `3.14`, `0.5`, `-2.75`, `100.0`

### Why Floats Matter

Imagine building a calculator that can only handle whole numbers. You couldn't:
- Calculate prices: $19.99
- Measure distances: 3.7 miles
- Find averages: 87.5%
- Do scientific work: π = 3.14159...

Floats give us the ability to work with **continuous quantities** - things that can be divided infinitely small, like length, weight, time, and money.

### Simple Analogy

**Integers** are like **stairs**: You're on step 1, step 2, step 3. No in-between.

**Floats** are like a **ramp**: You can be at position 1.5, 2.3, 2.75 - anywhere along the slope.

Both get you up a level, but floats give you more precise positions.

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

**Think of it like measuring with a ruler**:
- You want to measure exactly 0.1 inches
- But your ruler only has marks at 0.09 and 0.11
- You have to pick the closest mark
- That tiny error adds up when you combine measurements

This is rare in practice, but important to know. For everyday calculations (prices, percentages), Python's floats work great!

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
