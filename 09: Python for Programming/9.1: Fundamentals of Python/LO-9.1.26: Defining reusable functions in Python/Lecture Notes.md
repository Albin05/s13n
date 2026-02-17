# Lecture Notes: Define Functions

## Introduction

Functions introduce **code reusability** and **abstraction** - two of the most fundamental concepts in programming. They represent the shift from **linear, repetitive code** to **modular, maintainable software**.

### Why Functions Are Revolutionary

**The repetition problem**: Early programs repeated the same code blocks hundreds of times. A bug meant fixing it everywhere. A change meant updating hundreds of locations.
**Functions solution**: Write code once, call it anywhere. Fix bugs in one place. Update features once.

**Historical note**: Subroutines (early functions) appeared in FORTRAN (1954) and revolutionized programming. Before this, code was a tangled mess. After, programs became organized, maintainable systems.

### Real-World Analogy

Functions are like **recipes in a cookbook**:
- **Define once**: Write the recipe for "make pasta" once
- **Use many times**: Cook pasta Monday, Wednesday, Friday without rewriting steps
- **Share**: Others can use your recipe (code reuse!)
- **Modify**: Update recipe in one place, everyone gets the improvement

Or like **keyboard shortcuts**:
- **Ctrl+C (copy)**: A complex series of operations wrapped into one simple action
- **Function**: Complex code wrapped into one simple name
- **Result**: Simpler, more readable programs

### The Power of Abstraction

Functions hide **implementation details** behind a simple name:
```python
calculate_tax(income)  # Don't need to know HOW tax is calculated!
send_email(to, subject, body)  # Don't need to know HOW email works!
```

This **abstraction** lets you work at a higher level - thinking in terms of "what" not "how".

### DRY Principle

Functions embody **DRY: Don't Repeat Yourself**:
- **Without functions**: Same code copied 50 times (nightmare to maintain!)
- **With functions**: One function called 50 times (update once, fixed everywhere!)

This is the foundation of professional software engineering.

## Functions

A function is a reusable block of code that performs a specific task.


### Basic Syntax

```python
def function_name():
    # Function body
    # Code to execute
```

## Simple Examples

### Example 1: Hello Function

```python
def say_hello():
    print("Hello, World!")

# Call the function
say_hello()
# Output: Hello, World!
```

### Example 2: Multiple Statements

```python
def greet_user():
    print("Welcome!")
    print("Thanks for using our program")
    print("Have a great day!")

greet_user()
```

### Example 3: Reusability

```python
def print_line():
    print("-" * 40)

print_line()
print("Header")
print_line()
# Output:
# ----------------------------------------
# Header
# ----------------------------------------
```

## Why Use Functions?

1. **Reusability**: Write once, use many times
2. **Organization**: Break complex code into manageable pieces
3. **Maintainability**: Easier to debug and update
4. **Readability**: Makes code self-documenting

## Function Naming

```python
# Good names (verb-based, descriptive)
def calculate_total():
    pass

def send_email():
    pass

def validate_input():
    pass

# Avoid (not descriptive)
def func1():
    pass

def do_stuff():
    pass
```

## Calling Functions

```python
def display_menu():
    print("1. New Game")
    print("2. Load Game")
    print("3. Quit")

# Call it multiple times
display_menu()
display_menu()
```

## Functions Calling Functions

```python
def print_header():
    print("=" * 40)
    print("Welcome to My Program")
    print("=" * 40)

def print_footer():
    print("=" * 40)
    print("Thank you!")
    print("=" * 40)

def show_welcome():
    print_header()
    print("\nPlease choose an option:")
    print_footer()

show_welcome()
```

## Key Takeaways

1. **def keyword**: Defines a function
2. **Colon and indent**: Required syntax
3. **Call with ()**: parentheses needed to execute
4. **Reusable**: Can call multiple times
5. **Organization**: Breaks code into logical units
