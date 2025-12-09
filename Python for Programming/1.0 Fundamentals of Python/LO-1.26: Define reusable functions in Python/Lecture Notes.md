# Lecture Notes: Define Functions

## Functions

A function is a reusable block of code that performs a specific task.


---

<div align="center">

![Variables concept - labeled storage containers](https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800&q=80)

*Think of variables as labeled containers storing different types of data*

</div>

---
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
