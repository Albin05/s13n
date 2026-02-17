### Defining Reusable Functions in Python


### CS Theory Bite

> **Origin**: Functions (called **subroutines** in the 1950s) were formalized to enable **code reuse**. The **DRY principle** (Don't Repeat Yourself) — Andy Hunt & Dave Thomas, 1999 — is built on functions.
>
> **Analogy**: A function is like a **recipe** — define it once, cook it anytime you want. Change the recipe, and every dish improves.
>
> **Why it matters**: Functions are the primary unit of code organization — every large program is built from small functions.


### Hook (3 minutes)

"Imagine you're making breakfast. Every morning, you follow the same routine to make coffee - you don't relearn the steps each time. Functions in Python work the same way: define once, use many times!"

Think about your calculator's 'add' button - programmers wrote ONE function and reused it thousands of times!

### Section 1: What is a Function? (4 minutes)

A function is a named block of reusable code that performs a specific task.

**Without functions - repetitive code:**
```python
# Print header - First time
print("=" * 40)
print("   Welcome to My Program")
print("=" * 40)

# Later, print header again (copy-paste!)
print("=" * 40)
print("   Welcome to My Program")
print("=" * 40)
```

This is repetitive! If we change the header, we update it everywhere. Functions solve this.

### Section 2: Function Syntax (5 minutes)

```python
def function_name():
    # Function body (indented)
    # Code to execute
    pass
```

**Components:**
- `def` - keyword to start function definition
- `function_name` - descriptive name (PEP 8 conventions)
- `()` - parentheses (for parameters later)
- `:` - colon to start the block
- Indented code - function body

**Example:**
```python
def greet():
    print("Hello, World!")
    print("Welcome to Python!")
```

Note: Defining doesn't run it! We must CALL it.

### Section 3: Calling Functions (4 minutes)

```python
# STEP 1: Define
def greet():
    print("Hello, World!")
    print("Welcome to Python!")

# STEP 2: Call
greet()  # Output: Hello, World!
         #         Welcome to Python!

# Call multiple times
greet()
greet()  # Each call executes the entire function!
```

**Practical example:**
```python
def print_header():
    print("=" * 40)
    print("   Welcome to My Program")
    print("=" * 40)

print_header()  # Use anywhere
print("Loading...")
print_header()  # Use again
```

### Section 4: Functions Can Contain Any Code (4 minutes)

**Conditionals:**
```python
def check_age():
    age = 20
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a minor")

check_age()
```

**Loops:**
```python
def print_countdown():
    for i in range(5, 0, -1):
        print(i)
    print("Blast off!")

print_countdown()
```

**Multiple operations:**
```python
def daily_report():
    print("Generating report...")
    total = 100 + 200 + 300
    print(f"Total: {total}")
```

### Section 5: Why Use Functions? (3 minutes)

**Benefits:**
1. Reusability - Write once, use many times
2. Organization - Break large programs into manageable pieces
3. Maintainability - Update code in one place
4. Readability - Descriptive names make code self-documenting

**Example:**
```python
def show_menu():
    print("=" * 30)
    print("1. New Game")
    print("2. Load Game")
    print("3. Exit")

show_menu()  # On startup
# ... code ...
show_menu()  # After game over
# To change menu, update function once!
```

### Section 6: Common Mistakes (3 minutes)

**Mistake 1: Forgetting to call**
```python
def greet():
    print("Hello!")
# Nothing happens - not called!
```

**Mistake 2: Indentation errors**
```python
def greet():
print("Hello!")  # IndentationError!
```

**Mistake 3: Calling before defining**
```python
greet()  # NameError!

def greet():
    print("Hello!")
```

### Section 7: Practice (2 minutes)

Write a function `print_stars` that prints 5 stars:
```python
def print_stars():
    print("*" * 5)

print_stars()  # *****
```

### Wrap-Up (2 minutes)

**Key points:**
- Functions are reusable blocks of code
- Define with `def` keyword
- Call using function name with parentheses
- Make code organized and maintainable

**Template:**
```python
def function_name():
    # Your code here
    pass

function_name()  # Call it
```
