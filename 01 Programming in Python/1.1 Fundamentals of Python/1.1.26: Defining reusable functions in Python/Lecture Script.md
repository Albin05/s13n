# Lecture Script: Defining Reusable Functions in Python

**Duration:** 20-25 minutes
**Learning Objective:** Students will be able to define reusable functions using the `def` keyword and understand the benefits of function-based programming.

---

## Hook (2 minutes)

"Imagine you're making breakfast. Every morning, you follow the same steps to make coffee: boil water, add coffee grounds, pour water, wait, and serve. You don't need to relearn these steps each time - it's a routine you've defined once and repeat daily.

Functions in programming work exactly the same way! Instead of writing the same code over and over, you define it ONCE as a function and then 'call' it whenever you need it.

Today, you're going to learn one of the most powerful concepts in programming: defining reusable functions. This will transform how you write code - making it cleaner, shorter, and way more professional. By the end of this lesson, you'll wonder how you ever coded without functions!"

---

## Section 1: What is a Function? (3 minutes)

### Definition

"A function is a named block of reusable code that performs a specific task. Think of it as a mini-program within your program!"

### Why Do We Need Functions?

**Problem Without Functions:**

```python
# Printing a header - First time
print("=" * 40)
print("   Welcome to My Program")
print("=" * 40)

# Some code here...

# Printing a header - Second time (copy-paste!)
print("=" * 40)
print("   Another Section")
print("=" * 40)

# More code...

# Printing a header - Third time (copy-paste again!)
print("=" * 40)
print("   Final Section")
print("=" * 40)
```

**Issue:** Repetitive code! What if you want to change the design? You'd need to update it in THREE places!

**Solution With Functions:**

```python
def print_header():
    print("=" * 40)
    print("   Welcome to My Program")
    print("=" * 40)

print_header()  # First use
# Some code...
print_header()  # Second use
# More code...
print_header()  # Third use
```

**Benefits:**
- Write once, use many times
- Change once, affects all uses
- Code is cleaner and more organized

---

## Section 2: Function Syntax - The Anatomy (4 minutes)

### Basic Structure

```python
def function_name():
    # Function body (indented)
    # Code to execute
    pass
```

**Let's break this down piece by piece:**

### 1. The `def` Keyword

"'def' stands for 'define'. It tells Python: 'Hey, I'm about to define a function!'"

```python
def  # This keyword starts every function definition
```

### 2. Function Name

"Choose a descriptive name using snake_case (lowercase with underscores)."

```python
def greet():  # Good: clear, descriptive
def g():      # Bad: too short, unclear
def PrintMessage():  # Bad: should be lowercase
```

**Rules for function names:**
- Start with letter or underscore
- Can contain letters, numbers, underscores
- Cannot start with a number
- Cannot be a Python keyword (like `def`, `if`, `class`)

### 3. Parentheses `()`

"Always required, even when there are no parameters (we'll learn about parameters in the next lesson)."

```python
def greet():  # Parentheses are REQUIRED
    print("Hello!")
```

### 4. Colon `:`

"The colon signals the start of the function body. Don't forget it!"

```python
def greet():  # Colon is MANDATORY
    print("Hello!")
```

### 5. Function Body (Indented Code)

"Everything indented after the colon is part of the function. Python uses indentation to know what belongs to the function."

```python
def greet():
    print("Hello!")      # Part of function (indented)
    print("Welcome!")    # Part of function (indented)

print("Outside")  # NOT part of function (not indented)
```

**Key Point:** Indentation is not optional in Python - it's how Python knows what code belongs to the function!

---

## Section 3: Defining and Calling Functions (5 minutes)

### Example 1: Simple Greeting

```python
# STEP 1: Define the function
def greet():
    print("Hello, World!")
    print("Welcome to Python!")

# STEP 2: Call the function
greet()
```

**Output:**
```
Hello, World!
Welcome to Python!
```

**Important:** Defining a function doesn't execute it! You must CALL it.

### Example 2: Function with Calculations

```python
def calculate_area():
    radius = 5
    pi = 3.14159
    area = pi * radius * radius
    print(f"Area of circle: {area}")

calculate_area()
```

**Output:**
```
Area of circle: 78.53975
```

### Example 3: Function with a Loop

```python
def count_to_five():
    for i in range(1, 6):
        print(i, end=" ")
    print()  # New line

count_to_five()
```

**Output:**
```
1 2 3 4 5
```

### Example 4: Reusing Functions

```python
def print_separator():
    print("-" * 30)

print("Section 1")
print_separator()  # First use

print("Section 2")
print_separator()  # Second use - same function!

print("Section 3")
print_separator()  # Third use
```

**Output:**
```
Section 1
------------------------------
Section 2
------------------------------
Section 3
------------------------------
```

**Teaching Point:** "See how we defined `print_separator()` ONCE but used it THREE times? That's the power of reusability!"

---

## Section 4: Functions Can Contain ANY Code (3 minutes)

### Conditionals in Functions

```python
def check_age():
    age = 20
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a minor")

check_age()
```

**Output:**
```
You are an adult
```

### Nested Loops in Functions

```python
def print_pattern():
    for i in range(1, 4):
        for j in range(i):
            print("*", end=" ")
        print()

print_pattern()
```

**Output:**
```
*
* *
* * *
```

### Multiple Operations

```python
def analyze_number():
    num = 17
    print(f"Number: {num}")

    # Check if even or odd
    if num % 2 == 0:
        print("Type: Even")
    else:
        print("Type: Odd")

    # Check if prime
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime: Yes")
    else:
        print("Prime: No")

analyze_number()
```

**Output:**
```
Number: 17
Type: Odd
Prime: Yes
```

---

## Section 5: Common Mistakes (3 minutes)

### Mistake 1: Forgetting to Call the Function

```python
# WRONG - Function defined but never called
def greet():
    print("Hello!")

# Nothing happens! The function is defined but not executed.
```

```python
# RIGHT - Function defined AND called
def greet():
    print("Hello!")

greet()  # Now it executes!
```

### Mistake 2: Calling Before Defining

```python
# WRONG - Calling before defining
greet()  # NameError!

def greet():
    print("Hello!")
```

```python
# RIGHT - Define first, then call
def greet():
    print("Hello!")

greet()  # Works!
```

### Mistake 3: Missing Colon

```python
# WRONG - Missing colon
def greet()  # SyntaxError!
    print("Hello!")
```

```python
# RIGHT - Has colon
def greet():
    print("Hello!")
```

### Mistake 4: Incorrect Indentation

```python
# WRONG - Not indented
def greet():
print("Hello!")  # IndentationError!
```

```python
# RIGHT - Properly indented
def greet():
    print("Hello!")
```

### Mistake 5: Forgetting Parentheses When Calling

```python
def greet():
    print("Hello!")

greet  # Just references the function, doesn't call it
greet()  # Actually calls the function
```

---

## Section 6: Real-World Applications (3 minutes)

### Use Case 1: Menu System

```python
def show_menu():
    print("=" * 30)
    print("      MAIN MENU")
    print("=" * 30)
    print("1. New Game")
    print("2. Load Game")
    print("3. Settings")
    print("4. Exit")
    print("=" * 30)

# Use it whenever you need to show the menu
show_menu()
```

### Use Case 2: Data Validation

```python
def validate_password():
    password = "Secure123"

    # Check length
    if len(password) < 8:
        print("Password too short!")
        return

    # Check for numbers
    has_number = any(char.isdigit() for char in password)

    # Check for letters
    has_letter = any(char.isalpha() for char in password)

    if has_number and has_letter:
        print("Password is valid!")
    else:
        print("Password must contain letters and numbers!")

validate_password()
```

### Use Case 3: Report Generation

```python
def generate_report():
    print("=" * 50)
    print("           SALES REPORT")
    print("=" * 50)
    print(f"Total Sales: $45,230")
    print(f"Total Customers: 156")
    print(f"Average Sale: ${45230/156:.2f}")
    print("=" * 50)

generate_report()
```

### Use Case 4: Game Functions

```python
def display_health():
    health = 75
    max_health = 100

    # Create health bar
    bars = int((health / max_health) * 20)
    print(f"Health: [{'█' * bars}{' ' * (20-bars)}] {health}/{max_health}")

display_health()
```

**Output:**
```
Health: [███████████████     ] 75/100
```

---

## Section 7: Best Practices (2 minutes)

### 1. Use Descriptive Names

```python
# BAD
def f():
    print("Hello")

def x():
    print("Calculating...")

# GOOD
def greet_user():
    print("Hello")

def calculate_total():
    print("Calculating...")
```

### 2. One Function, One Task

```python
# BAD - Function does too many things
def do_everything():
    print("Hello")
    calculate_area()
    validate_password()
    print("Goodbye")

# GOOD - Each function has one clear purpose
def greet():
    print("Hello")

def farewell():
    print("Goodbye")
```

### 3. Add Docstrings

```python
def calculate_circle_area():
    """
    Calculate and print the area of a circle with radius 5.
    Formula: area = π × r²
    """
    radius = 5
    pi = 3.14159
    area = pi * radius * radius
    print(f"Area: {area}")
```

### 4. Keep It Short

"If a function is getting too long (more than 20-30 lines), consider breaking it into smaller functions."

### 5. Use Consistent Naming

"Stick to snake_case for all function names. Be consistent across your entire program."

---

## Practice Problems (2 minutes)

### Quick Exercise 1

"Write a function called `print_stars` that prints 5 stars in a row."

**Solution:**
```python
def print_stars():
    print("*" * 5)

print_stars()
```

### Quick Exercise 2

"Write a function called `countdown` that prints numbers from 10 to 1."

**Solution:**
```python
def countdown():
    for i in range(10, 0, -1):
        print(i, end=" ")
    print()

countdown()
```

### Quick Exercise 3

"Write a function called `check_even` that checks if 42 is even."

**Solution:**
```python
def check_even():
    number = 42
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

check_even()
```

---

## Wrap-Up (1 minute)

### Key Takeaways

**Definition:**
- Functions are reusable blocks of code
- Defined with `def` keyword
- Called by using function name with parentheses

**Syntax:**
```python
def function_name():
    # Indented code
    # Function body
    pass
```

**Remember:**
1. **DEF**ine the function first
2. **Call** it with parentheses `()`
3. **Indent** the function body
4. **Colon** after the function name
5. **Use** descriptive names

**Benefits:**
- ✓ Code reusability
- ✓ Better organization
- ✓ Easier maintenance
- ✓ Improved readability
- ✓ Easier testing

**Common Mistakes to Avoid:**
- ✗ Forgetting the colon
- ✗ Wrong indentation
- ✗ Calling before defining
- ✗ Forgetting parentheses when calling
- ✗ Using invalid function names

**Next Lesson Preview:**

"In our next lesson, we'll learn about function PARAMETERS - how to pass information INTO functions to make them even more flexible and powerful! Today we learned to make coffee the same way every time. Next, we'll learn how to customize it - regular, decaf, with milk, etc.!"

---

## Quick Reference Card

```python
# Template
def function_name():
    """Optional description of what the function does."""
    # Your code here
    pass

# Example
def greet():
    """Print a friendly greeting."""
    print("Hello, World!")

# Calling
greet()
```

**Function Checklist:**
- [ ] Starts with `def`
- [ ] Has descriptive name (snake_case)
- [ ] Has parentheses `()`
- [ ] Ends with colon `:`
- [ ] Body is indented
- [ ] Called with `function_name()`

---

## Engagement Questions

**Q: Why use functions instead of just writing code normally?**
A: Reusability! Write once, use many times. Plus easier to maintain and test.

**Q: Can I have multiple functions in one program?**
A: Absolutely! Professional programs have dozens or hundreds of functions.

**Q: Can a function call another function?**
A: Yes! Functions can call other functions. We'll explore this more in future lessons.

**Q: What happens if I define a function but never call it?**
A: The function exists in memory but never executes. It's like having a recipe but never cooking it.

**Q: Can functions have the same name as variables?**
A: Technically yes, but DON'T! It causes confusion. Use unique, descriptive names.

---

## Homework Preview

"For homework, you'll practice:
1. Writing functions for common tasks (greetings, calculations, patterns)
2. Converting repetitive code into reusable functions
3. Building a menu system using functions
4. Creating functions for data validation

Remember: The best way to learn functions is to WRITE them. Start small, then gradually build more complex ones. See you next class!"

---

**End of Lecture**

"Great work today! You've just learned one of the foundational concepts of programming. Functions will be in almost EVERY program you write from now on. Practice defining and calling functions until it becomes second nature. Happy coding!"
