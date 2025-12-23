# Lecture Notes: Implement Float Data Types

## Introduction
Floats represent numbers with decimal points, providing precision for measurements, calculations, and scientific data.

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
