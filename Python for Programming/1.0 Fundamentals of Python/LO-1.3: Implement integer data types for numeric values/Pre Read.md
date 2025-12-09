# Pre-Read: Implement Integer Data Types

## What are Integers?

**Integers** are whole numbers - no decimal points!

Examples: `5`, `-3`, `0`, `1000`, `-999`

Not integers: `5.5`, `3.14`, `0.1` (these are floats)

## Creating Integer Variables

```python
age = 25
year = 2024
count = 0
temperature = -5
```

## Integer Operations

### Basic Arithmetic
```python
a = 10
b = 3

print(a + b)   # 13 (addition)
print(a - b)   # 7 (subtraction)
print(a * b)   # 30 (multiplication)
```

### Division: Two Types!

**Regular division** (`/`) - returns float:
```python
print(10 / 3)   # 3.3333...
print(10 / 2)   # 5.0 (still a float!)
```

**Integer division** (`//`) - returns integer:
```python
print(10 // 3)  # 3 (drops decimal)
print(10 // 2)  # 5 (integer)
```

### Modulo (Remainder)
```python
print(10 % 3)   # 1 (remainder of 10 ÷ 3)
print(10 % 2)   # 0 (10 is even, no remainder)
```

## When to Use Integers

✅ **Use integers for:**
- Counting things (10 students)
- Ages (25 years old)
- Years (2024)
- Quantities that don't need decimals

❌ **Don't use integers for:**
- Prices ($19.99)
- Measurements (5.5 feet)
- Percentages (87.5%)

## Try Before Class

```python
students = 30
teachers = 5

total_people = students + teachers
print(total_people)  # What will this print?

ratio = students // teachers
print(ratio)  # What about this?
```

## Key Points
- Integers = whole numbers
- Use `/` for decimal division, `//` for integer division
- Python integers have no size limit!
- Choose int when you don't need decimals
