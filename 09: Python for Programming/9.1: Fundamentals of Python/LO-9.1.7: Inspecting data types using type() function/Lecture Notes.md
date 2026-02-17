# Lecture Notes: Inspecting Data Types Using type()

## Introduction

Python is **dynamically typed** - you don't declare types explicitly. The `type()` function lets you inspect what type a variable currently holds, which is essential for understanding and debugging code.

---

## Understanding type()

### Basic Usage

```python
age = 25
print(type(age))  # <class 'int'>

name = "Alice"
print(type(name))  # <class 'str'>

price = 19.99
print(type(price))  # <class 'float'>

is_active = True
print(type(is_active))  # <class 'bool'>
```

### What Does `<class 'int'>` Mean?

The output `<class 'int'>` tells us:
- This value belongs to the **class** (type) called `int`
- In Python, types are implemented as classes
- You'll learn more about classes later in OOP

For now, just recognize the type name: `int`, `str`, `float`, `bool`

---

## Why Type Inspection Matters

### Python's Dynamic Typing

Unlike languages like C or Java, Python doesn't require type declarations:

```python
# Python - types are inferred
x = 5        # Python knows it's an int
x = "hello"  # Now x is a string - type changed!

# Java - types must be declared
int x = 5;
x = "hello";  // ❌ Error! Can't assign string to int variable
```

**Advantage**: Faster to write, more flexible
**Challenge**: Sometimes you're not sure what type a variable is

The `type()` function solves this challenge.

### Real-World Analogy

Think of `type()` like a **label reader**:
- You find an unlabeled box in storage
- You use a label reader to scan it
- It tells you: "This is a box of tools" vs "This is a box of toys"

Similarly, `type()` tells you what kind of data a variable contains.

---

## Practical Examples

### Example 1: Debugging Type Errors

```python
age = "25"  # Accidentally a string!
bonus = age + 5  # ❌ TypeError

# Use type() to debug
print(type(age))    # <class 'str'> - Aha! Should be int
print(type(bonus))  # Won't run due to error

# Fix it
age = int(age)  # Convert to integer
print(type(age))  # <class 'int'> ✓
bonus = age + 5   # Now works!
```

### Example 2: Understanding Function Results

```python
result = 10 / 3
print(result)        # 3.3333...
print(type(result))  # <class 'float'> - division returns float

result = 10 // 3
print(result)        # 3
print(type(result))  # <class 'int'> - floor division returns int
```

### Example 3: Validating Input

```python
user_input = input("Enter your age: ")
print(type(user_input))  # <class 'str'> - input() always returns string!

# Must convert before arithmetic
age = int(user_input)
print(type(age))  # <class 'int'> - now it's a number
```

---

## Dynamic Typing: A Double-Edged Sword

### Flexibility

```python
x = 5          # x is an int
x = "hello"    # Now x is a string
x = [1, 2, 3]  # Now x is a list
# Python doesn't care - types can change
```

This flexibility is powerful but can lead to bugs:

```python
def calculate_total(price, quantity):
    return price * quantity

# Works as expected
total = calculate_total(10, 3)  # 30

# Unexpected behavior!
total = calculate_total(10, "3")  # "10101010101010" (repeats string 10 times!)
```

The `type()` function helps catch these issues.

---

## When to Use type()

| Scenario | Example |
|----------|---------|
| **Debugging errors** | Figure out why operations fail |
| **Learning code** | Understand what a function returns |
| **Validation** | Check if user input is the right type |
| **Testing** | Verify function output types |
| **Exploration** | Experiment with new Python features |

---

## Comparison with isinstance()

**Advanced note**: Python also has `isinstance()` for type checking:

```python
age = 25

# Using type()
print(type(age) == int)  # True

# Using isinstance() - preferred for checking
print(isinstance(age, int))  # True
```

`isinstance()` is generally better for type checking, but `type()` is great for inspection and learning.

---

## Key Takeaways

1. **type() reveals data types** - essential in dynamically typed Python
2. **Returns class object** - `<class 'int'>`, `<class 'str'>`, etc.
3. **Helps debug type errors** - find where types don't match expectations
4. **Types can change** - variables can be reassigned to different types
5. **Use for learning** - explore what functions return and how operations work

---

## Why Dynamic Typing Matters

**Python's philosophy**: "We're all consenting adults here"

Python trusts you to manage types correctly, rather than enforcing strict type declarations like C++ or Java. This makes Python:
- **Faster to write**: No boilerplate type declarations
- **More flexible**: Same function can work with multiple types
- **More forgiving**: Easier for beginners

But with great power comes great responsibility - use `type()` to verify your assumptions!
