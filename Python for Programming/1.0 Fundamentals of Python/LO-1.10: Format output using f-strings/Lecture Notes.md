# Lecture Notes: Format Output with F-strings

## Introduction
F-strings (formatted string literals) provide a clean, readable way to embed expressions in strings.

---


---

<div align="center">

![Different data types representation](https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80)

*Python supports multiple data types: integers, floats, strings, and booleans*

</div>

---
## Basic F-string Syntax

### Simple Variable Embedding
```python
name = "Alice"
age = 25
message = f"Hello, {name}! You are {age} years old."
print(message)
# Output: Hello, Alice! You are {25 years old.
```

### Multiple Variables
```python
first = "John"
last = "Doe"
age = 30
print(f"{first} {last} is {age}")
# Output: John Doe is 30
```

---

## Expressions in F-strings

### Arithmetic
```python
price = 10
quantity = 3
print(f"Total: ${price * quantity}")
# Output: Total: $30
```

### Method Calls
```python
name = "alice"
print(f"Welcome, {name.upper()}!")
# Output: Welcome, ALICE!
```

### Comparisons
```python
age = 20
print(f"Adult: {age >= 18}")
# Output: Adult: True
```

---

## Number Formatting

### Decimal Places
```python
pi = 3.14159265
print(f"Pi: {pi:.2f}")   # Pi: 3.14
print(f"Pi: {pi:.4f}")   # Pi: 3.1416
```

### Width and Alignment
```python
num = 42
print(f"{num:5}")    # "   42" (width 5, right-aligned)
print(f"{num:<5}")   # "42   " (left-aligned)
print(f"{num:^5}")   # " 42  " (centered)
```

### Thousands Separator
```python
big_num = 1000000
print(f"{big_num:,}")  # 1,000,000
```

---

## Practical Examples

### Example 1: Receipt
```python
item = "Coffee"
price = 4.50
quantity = 2
total = price * quantity

print(f"Item: {item}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: ${total:.2f}")
```

Output:
```
Item: Coffee
Price: $4.50
Quantity: 2
Total: $9.00
```

### Example 2: Student Report
```python
name = "Alice Johnson"
math_score = 95
english_score = 87
average = (math_score + english_score) / 2

print(f"Student: {name}")
print(f"Math: {math_score}")
print(f"English: {english_score}")
print(f"Average: {average:.1f}")
```

### Example 3: Temperature Conversion
```python
celsius = 25
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C = {fahrenheit:.1f}°F")
# Output: 25°C = 77.0°F
```

---

## Comparing Formatting Methods

### Concatenation (Old)
```python
name = "Bob"
age = 30
# Hard to read, error-prone
msg = "Hi " + name + ", you are " + str(age)
```

### .format() (Older)
```python
msg = "Hi {}, you are {}".format(name, age)
# Better, but verbose
```

### F-strings (Modern) ✅
```python
msg = f"Hi {name}, you are {age}"
# Clean and readable!
```

---

## Key Takeaways
1. F-strings start with `f` before quotes
2. Use `{}` to embed variables and expressions
3. Can do calculations inside `{}`
4. Format numbers with `:.2f` (2 decimal places)
5. Much cleaner than concatenation
6. Modern Python standard (Python 3.6+)
