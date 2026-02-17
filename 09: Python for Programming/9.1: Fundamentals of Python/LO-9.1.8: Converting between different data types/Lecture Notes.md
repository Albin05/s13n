# Lecture Notes: Convert Between Data Types

## Introduction

Type conversion, also called **type casting**, is the process of transforming data from one type to another. This is essential in Python because different types can't always interact directly.

### Why Type Conversion Matters

Consider this common scenario:
```python
age = input("Enter your age: ")  # Returns "25" (string)
next_age = age + 1  # ❌ TypeError: can only concatenate str to str
```

The user types numbers, but `input()` returns a **string**. We must convert it to a number before doing math.

### The Fundamental Problem

At the computer's memory level, different types are stored differently:
- **Integers**: Stored as binary numbers: `25` = `11001` in binary
- **Floats**: Stored using scientific notation (mantissa + exponent)
- **Strings**: Stored as sequences of character codes: `"25"` = `[50, 53]` (ASCII codes)

Because they're stored differently, computers need explicit instructions to convert between them. That's what type conversion functions do.

### Real-World Analogy

Think of type conversion like **language translation**:
- You have a message in Spanish (string "25")
- You need to understand it as a number (int 25)
- You use a translator (int() function)
- Now you can do math with it

Or think of it like **currency conversion**:
- $25 (dollars) vs €25 (euros)
- They represent similar values but are stored in different "formats"
- You need a conversion to make them compatible

### Static vs. Dynamic Typing

**Static languages** (C, Java): Types are declared and fixed
```java
int age = 25;
age = "hello";  // ❌ Compile error
```

**Dynamic languages** (Python): Types can change, but you must convert explicitly for operations
```python
age = 25
age = "hello"  # ✓ Allowed
result = 25 + "5"  # ❌ Error - must convert first
```

Python's approach: Flexible but requires awareness of types.

---

## Type Conversion Functions

### int() - Convert to Integer
```python
int("25")       # 25 (string to int)
int(25.9)       # 25 (float to int - truncates)
int(True)       # 1
int(False)      # 0
# int("25.5")   # Error - can't convert decimal string
```


### float() - Convert to Float
```python
float("3.14")   # 3.14
float(5)        # 5.0
float("5")      # 5.0
float(True)     # 1.0
```

### str() - Convert to String
```python
str(25)         # "25"
str(3.14)       # "3.14"
str(True)       # "True"
str(False)      # "False"
```

### bool() - Convert to Boolean
```python
bool(1)         # True (non-zero = True)
bool(0)         # False (zero = False)
bool("text")    # True (non-empty = True)
bool("")        # False (empty = False)
bool([1,2,3])   # True (non-empty = True)
```

## Common Use Cases

### User Input
```python
age_str = input("Enter age: ")  # Returns string
age = int(age_str)               # Convert to int
next_year = age + 1              # Now can do math
```

### String Concatenation
```python
score = 95
message = "Score: " + str(score)  # Convert int to str
print(message)  # "Score: 95"
```

### Calculation Display
```python
result = 10 / 3
print("Result: " + str(result))  # Convert float to str
```

## When Conversion Fails

Not all conversions are valid:
```python
int("hello")    # ❌ ValueError: invalid literal for int()
int("25.5")     # ❌ ValueError: invalid literal (use float() first)
float("abc")    # ❌ ValueError: could not convert string to float
```

**Best practice**: Use try-except blocks (you'll learn later) to handle conversion errors gracefully.

## Implicit vs. Explicit Conversion

### Implicit (Automatic)
Python does some conversions automatically:
```python
result = 5 + 2.5  # int + float → automatically converts to float
print(result)      # 13.5 (float)
```

### Explicit (Manual)
Most conversions require explicit function calls:
```python
age = int("25")        # Manual conversion needed
message = str(100)     # Manual conversion needed
```

**Design principle**: Python's motto is "Explicit is better than implicit". Automatic conversions can hide bugs, so Python makes you do most conversions explicitly.

---

## Key Takeaways
1. **Type conversion transforms data** from one type to another
2. **Use built-in functions**: `int()`, `float()`, `str()`, `bool()`
3. **User input always needs conversion** - input() returns strings
4. **Can't mix incompatible types** - must convert first
5. **Some conversions may fail** - not all strings can become numbers
6. **Explicit is better** - Python requires most conversions to be manual
7. **Know the rules** - int() truncates floats, bool() has specific falsy values
