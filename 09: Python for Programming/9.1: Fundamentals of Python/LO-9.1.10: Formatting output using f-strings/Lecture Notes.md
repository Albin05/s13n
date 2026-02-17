# Lecture Notes: Format Output with F-strings

## Introduction
F-strings (formatted string literals) provide a clean, readable way to embed expressions in strings.

### The Evolution of String Formatting

Python has had multiple ways to format strings over its history:

**1991 - Python 1.x**: String concatenation
```python
"Hello " + name + ", you are " + str(age)
```
- Simple but clunky
- Must convert types manually
- Hard to read with many variables

**1997 - Python 1.5**: % formatting (borrowed from C)
```python
"Hello %s, you are %d" % (name, age)
```
- More powerful but cryptic
- Hard to remember format codes (%s, %d, %f)

**2006 - Python 2.6/3.0**: .format() method
```python
"Hello {}, you are {}".format(name, age)
```
- More flexible and readable
- But still verbose

**2015 - Python 3.6**: F-strings (PEP 498)
```python
f"Hello {name}, you are {age}"
```
- Concise, readable, and fast
- Expressions evaluated at runtime
- Now the standard way

### Why F-strings Matter

**The problem**: Building strings with variables was always awkward in Python. Consider:
```python
name = "Alice"
score = 95
level = 10
message = "Player " + name + " scored " + str(score) + " points at level " + str(level) + "!"
# Hard to read, easy to make mistakes!
```

**The solution**: F-strings use **template syntax** - placeholders that get filled in:
```python
message = f"Player {name} scored {score} points at level {level}!"
# Clean, readable, obvious!
```

This is called **string interpolation** - inserting variable values into a string template.

### Real-World Analogy

Think of f-strings like **mail merge** in word processing:
- You write a letter template: "Dear {name}, you won {prize}!"
- The program fills in the blanks for each person
- Same template, different data

Or think of them like **Mad Libs**:
- Template: "The {adjective} {noun} {verb} the {noun}!"
- Fill in: "The big dog ate the sandwich!"

F-strings are Mad Libs for programmers - templates with blanks to fill.

### Why Called "F-strings"?

The `f` stands for **"formatted string"**. The `f` prefix tells Python:
- This string has placeholders: `{}`
- Evaluate the expressions inside: `{x + 1}`
- Format them into the final string

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

## The Philosophy Behind F-strings

**Python's Zen**: "Readability counts"

Compare these approaches:
```python
# Concatenation - error-prone
msg = "Total: $" + str(price * qty) + " for " + str(qty) + " items"

# F-string - clear intent
msg = f"Total: ${price * qty} for {qty} items"
```

F-strings embody Python's philosophy:
- **Readable**: Looks like what it does
- **Concise**: No boilerplate
- **Powerful**: Can embed any expression
- **Fast**: Evaluated at compile-time (faster than .format())

### Why This Matters for You

As a programmer, you'll spend more time reading code than writing it. F-strings make your intent obvious:
- What's the template?
- Where do values get inserted?
- What calculations happen?

All visible at a glance.

**Best practice**: Use f-strings as your default string formatting method in Python 3.6+. Only use older methods when working with legacy code.

---

## Key Takeaways
1. **F-strings are Python 3.6+'s modern solution** to string formatting
2. **Start with `f`** before quotes: `f"..."`
3. **Use `{}` for interpolation** - embed variables and expressions
4. **Can evaluate expressions**: `{price * quantity}`, `{name.upper()}`
5. **Format specifiers**: `:.2f` (decimals), `:,` (thousands), `:^5` (alignment)
6. **More readable than alternatives** - concatenation, %, .format()
7. **String interpolation** - fill template placeholders with values
8. **Python philosophy**: Readability counts, explicit is better than implicit
