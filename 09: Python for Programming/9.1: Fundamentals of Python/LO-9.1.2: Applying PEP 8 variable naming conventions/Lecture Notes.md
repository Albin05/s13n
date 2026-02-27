# Lecture Notes: Apply Variable Naming Conventions

## Introduction

Variable naming is more than just following syntax rules - it's about **communication**. Code is read far more often than it's written, and good naming makes your code self-documenting.

### Why Naming Conventions Exist

In the early days of programming, developers worked alone. But modern software is built by teams, often across countries and time zones. Without naming conventions:
- Reading someone else's code becomes a puzzle
- Different styles make codebases look inconsistent
- Onboarding new developers takes longer
- Bugs hide in unclear variable names

Think of naming conventions like **traffic rules** - they're not about restricting you, they're about making sure everyone can work together smoothly.

### PEP 8: Python's Style Guide

**PEP** stands for "Python Enhancement Proposal". PEP 8 is Python's official style guide, created in 2001.

It standardizes:
- How to name variables, functions, and classes
- How to format code (spacing, indentation)
- Best practices for writing readable Python

Following PEP 8 means your code looks "Pythonic" - like it belongs in the Python ecosystem.

**The Zen of Python** (type `import this` in Python) says:
> "Readability counts"
> "There should be one-- and preferably only one --obvious way to do it"

PEP 8 embodies these principles.

---

<div align="center">

![Python PEP 8 Naming Convention snake_case camelCase](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.2.png)

*PEP 8 naming conventions (snake_case for variables, UPPER_CASE for constants) keep Python code consistent and readable*

</div>

---

## Naming Rules (Must Follow)

### 1. Start with letter or underscore
✅ `name`, `_value`
❌ `1name`, `@user`


### 2. Only letters, numbers, underscores
✅ `student_name`, `score_2024`
❌ `student-name`, `total$`

### 3. Case sensitive
`age` ≠ `Age` ≠ `AGE`

### 4. No reserved keywords
❌ `for`, `if`, `while`, `class`

## Naming Conventions (Best Practice)

### snake_case: Python's Signature Style

Python uses **snake_case** (words separated by underscores) for variables and functions.

```python
student_name = "Alice"  # Pythonic ✅
studentName = "Alice"   # Not Pythonic (camelCase) ❌
StudentName = "Alice"   # Not Pythonic (PascalCase) ❌
```

**Why snake_case?**
- More readable than camelCase: `calculate_total_price` vs `calculateTotalPrice`
- Matches Python's standard library: `str.upper()`, `os.path`, `datetime.now()`
- Research shows snake_case is easier to read for most people

**Note**: Other languages use different conventions:
- JavaScript: `camelCase` (`studentName`)
- C#/Java: `PascalCase` for classes (`StudentName`)
- Python reserves `PascalCase` for class names only

### Be Descriptive: Names as Documentation

Your variable name should answer: "What does this store?"

```python
# Good - self-explanatory
student_count = 30
total_price = 199.99
is_logged_in = True

# Bad - requires comments or context
sc = 30       # What's sc? Student count? Score? Screen?
t = 199.99    # Total? Temperature? Time?
flag = True   # Flag for what?
```

**Exception**: Short names are fine for:
- Loop counters: `for i in range(10)`
- Mathematical formulas: `area = pi * r * r`
- Very local scope (< 5 lines)

### Constants in UPPER_CASE

Values that never change should use ALL_CAPS:

```python
MAX_SIZE = 100
PI = 3.14159
API_KEY = "abc123"
DEFAULT_TIMEOUT = 30
```

This signals to other developers: "Don't modify this value"

**Real-world impact**: In a team project, if you see `MAX_CONNECTIONS = 100`, you know it's a configuration constant. If you see `max_connections = 100`, it might be a variable that changes.

## Key Takeaways
1. Follow rules to avoid errors
2. Use snake_case for variables
3. Be descriptive and clear
4. Avoid reserved keywords
