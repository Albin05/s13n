# Lecture Notes: Implement Float Data Types

## Introduction
Floats represent numbers with decimal points, providing precision for measurements, calculations, and scientific data.

---

<div align="center">

![Python Float Object Diagram](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.4.png)

*Floats represent decimal numbers using IEEE 754 standard — essential for scientific calculations and measurements*

</div>

---


## What are Floats?

### Definition
**Float**: Number with decimal point (floating-point number)

```python
price = 19.99
height = 5.8
percentage = 87.5
pi = 3.14159
```

### Why "Floating-Point"?

The name comes from how computers store these numbers. Unlike fixed-point notation, the decimal point can "float" to different positions:

- `1.23` (decimal point after first digit)
- `123.0` (decimal point after third digit)
- `0.0123` (decimal point before digits)

Computers use **scientific notation** internally:
- `1.23 × 10²` represents 123.0
- `1.23 × 10⁻²` represents 0.0123

This allows floats to represent both very large (3.4 × 10³⁸) and very small (1.0 × 10⁻³⁸) numbers in limited memory.

### Real-World Analogy

Think of floats like a **measuring tape**:
- You can measure 5 feet, 5.5 feet, 5.75 feet
- You can be precise, but not infinitely precise
- There's always a smallest unit you can measure

Integers are like **counting marbles**:
- You can only count whole marbles: 1, 2, 3...
- No "half a marble"

### Always Has Decimal Point
```python
x = 5.0   # Float (has decimal)
y = 5     # Integer (no decimal)

print(type(x))  # <class 'float'>
print(type(y))  # <class 'int'>
```

---

## Float Arithmetic

### Basic Operations
```python
a = 10.5
b = 2.5

print(a + b)  # 13.0
print(a - b)  # 8.0
print(a * b)  # 26.25
print(a / b)  # 4.2
```

### Division Always Returns Float
```python
result = 10 / 2
print(result)        # 5.0
print(type(result))  # <class 'float'>
```

---

## Precision Limitations

### The 0.1 + 0.2 Problem
```python
result = 0.1 + 0.2
print(result)  # 0.30000000000000004 (not exactly 0.3!)
```

**Why?** Computers store numbers in binary. Some decimals can't be represented exactly.

### Understanding the Problem

Think about representing 1/3 in decimal:
- 1/3 = 0.3333333... (infinite)
- We must round: 0.33 or 0.333 or 0.3333

The same happens in binary! In base-10, we can exactly represent 0.1, but in base-2 (binary):
- 0.1 (decimal) = 0.0001100110011001... (binary, repeating forever)

Computers have finite memory, so they must round. This tiny rounding error propagates through calculations.

**Historical Impact**: Float precision errors have caused:
- The Patriot missile failure (1991) - clock drift killed 28 people
- Ariane 5 rocket explosion (1996) - $370 million lost
- Vancouver Stock Exchange index error (1982) - accumulated rounding errors

For financial calculations, use Python's `decimal` module for exact decimal arithmetic.

### Practical Impact
```python
# Be careful with equality checks
if 0.1 + 0.2 == 0.3:
    print("Equal")
else:
    print("Not equal")  # This prints!
```

### Solution: Round for Display
```python
result = 0.1 + 0.2
print(round(result, 2))  # 0.3
```

---

## Mixed Type Arithmetic

### Int + Float = Float
```python
int_num = 10
float_num = 3.5

result = int_num + float_num
print(result)        # 13.5
print(type(result))  # <class 'float'>
```

---

## Common Use Cases
- Prices: `$19.99`
- Measurements: `5.8 feet`
- Percentages: `87.5%`
- Scientific: `3.14159`
- Temperatures: `98.6°F`

## Key Takeaways
1. Floats have decimal points
2. All division returns floats
3. Precision isn't perfect (binary representation)
4. Use for measurements, prices, percentages
5. Int + float = float
