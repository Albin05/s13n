# Pre-Read: Define Functions

## What are Functions?

Functions are **reusable blocks of code** that perform a specific task. They're like creating your own custom commands!

### Simple Analogy

Think of functions like **remote control buttons**:
- **Power button**: One press does a complex series of actions (turn on screen, load settings, connect to input, etc.)
- **You**: Just press button (call function)
- **Inside**: Complex code runs automatically
- **Result**: You work at a higher level - thinking in terms of actions, not implementation

Or like **a vending machine**:
- **Button**: You press "A3"
- **Hidden process**: Machine finds item, charges card, dispenses snack
- **You see**: Simple interface, complex internals

Functions let you create **custom actions** for your program!

### Why Functions Matter

Before functions, programmers copied the same code everywhere:
```python
# Without functions - repetitive nightmare!
print("-" * 40)
print("Welcome!")
print("-" * 40)

# ...100 lines later...
print("-" * 40)  # Same code again!
print("Welcome!")
print("-" * 40)
```

With functions - write once, use anywhere:
```python
def show_welcome():
    print("-" * 40)
    print("Welcome!")
    print("-" * 40)

show_welcome()  # Use anywhere, anytime!
```

## What are Functions?

Functions are reusable blocks of code that perform a specific task.

```python
def greet():
    print("Hello!")

greet()  # Calls the function
# Output: Hello!
```

## Why Use Functions?

1. **Reusability**: Write once, use many times
2. **Organization**: Break code into logical pieces
3. **Maintainability**: Easier to update and debug

## Basic Syntax

```python
def function_name():
    # Code here
    pass
```

## Example

```python
def say_hello():
    print("Hello, World!")

# Call the function
say_hello()
say_hello()
say_hello()

# Output: Hello, World! (3 times)
```
