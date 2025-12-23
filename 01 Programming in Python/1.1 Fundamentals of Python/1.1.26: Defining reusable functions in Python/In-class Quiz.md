# Post-class Quiz: Defining Reusable Functions in Python

## Question 1

What is the correct syntax to define a function named `greet` in Python?

A) `function greet():`
B) `def greet():`
C) `define greet():`
D) `func greet():`

**Answer: B) `def greet():`**

**Explanation:** In Python, the `def` keyword is used to define a function. The syntax is `def function_name():` followed by the function body, which must be indented. Other languages use different keywords (like `function` in JavaScript), but Python specifically uses `def`.

---

## Question 2

What happens when you define a function but never call it?

A) The function executes automatically
B) Python throws an error
C) The function is stored but never executes
D) The function is deleted

**Answer: C) The function is stored but never executes**

**Explanation:** Defining a function with `def` only creates the function in memory. The code inside the function doesn't execute until you explicitly call the function by using its name followed by parentheses. This is a key distinction: definition vs. execution.

---

## Question 3

What will this code output?

```python
def message():
    print("Hello")
    print("World")

message()
```

A) `Hello`
B) `Hello World`
C) `Hello` on one line, `World` on the next
D) Error

**Answer: C) `Hello` on one line, `World` on the next**

**Explanation:** The function contains two separate `print()` statements. Each `print()` outputs its content on a new line by default. When `message()` is called, both print statements execute, producing two lines of output.

---

## Question 4

Which of these is a valid function name in Python?

A) `calculate_sum`
B) `2nd_function`
C) `my-function`
D) `def`

**Answer: A) `calculate_sum`**

**Explanation:** Python function names must:
- Start with a letter or underscore (not a number)
- Contain only letters, numbers, and underscores (no hyphens)
- Not be a reserved keyword (like `def`, `if`, `class`)

`calculate_sum` follows all these rules. Option B starts with a number, C contains a hyphen, and D is a reserved keyword.

---

## Question 5

What is required after the function definition line?

A) Semicolon
B) Colon
C) Comma
D) Nothing

**Answer: B) Colon**

**Explanation:** The colon (`:`) is required at the end of the function definition line. It signals to Python that the function body follows. The syntax is `def function_name():` - the colon is mandatory.

---

## Question 6

How do you call a function named `display_menu`?

A) `call display_menu`
B) `display_menu()`
C) `display_menu[]`
D) `run display_menu`

**Answer: B) `display_menu()`**

**Explanation:** To call (execute) a function, use its name followed by parentheses. Even if the function takes no parameters, the parentheses are required. Without parentheses, you're just referencing the function object, not calling it.

---

## Question 7

What will happen with this code?

```python
greet()

def greet():
    print("Hello")
```

A) Prints "Hello"
B) NameError: name 'greet' is not defined
C) Prints nothing
D) SyntaxError

**Answer: B) NameError: name 'greet' is not defined**

**Explanation:** In Python, you must define a function before calling it. Python reads code from top to bottom, so when it encounters `greet()` on line 1, the function hasn't been defined yet. Always define functions before calling them, or call them from within another function that's called after the definition.

---

## Question 8

What is the purpose of indentation in function definitions?

A) For readability only
B) To define the function body
C) Optional style choice
D) To separate functions

**Answer: B) To define the function body**

**Explanation:** Indentation in Python is not optional or just for style - it's syntactically significant. The indented lines after `def function_name():` form the function body. Python uses indentation to determine which code belongs to the function. Inconsistent or missing indentation will cause errors.

---

## Question 9

Which naming convention is preferred for Python functions?

A) `camelCase` (e.g., `calculateSum`)
B) `PascalCase` (e.g., `CalculateSum`)
C) `snake_case` (e.g., `calculate_sum`)
D) `kebab-case` (e.g., `calculate-sum`)

**Answer: C) `snake_case` (e.g., `calculate_sum`)**

**Explanation:** According to PEP 8 (Python's style guide), function names should use snake_case: lowercase letters with underscores separating words. This is the standard Python convention. PascalCase is used for class names, and kebab-case is invalid in Python (hyphens aren't allowed in identifiers).

---

## Question 10

What will this code print?

```python
def count():
    for i in range(3):
        print(i)

count()
count()
```

A) `0 1 2`
B) `0 1 2 0 1 2`
C) `0 1 2` on one line, `0 1 2` on the next
D) Error

**Answer: B) `0 1 2 0 1 2`**

**Explanation:** Each time `count()` is called, the function executes completely. The first call prints `0 1 2` (each on a new line), and the second call also prints `0 1 2` (each on a new line). The function is reusable - you can call it as many times as needed, and it executes the same code each time.

---

## Question 11

What is one main benefit of using functions?

A) Makes code longer
B) Code reusability
C) Increases execution time
D) Uses more memory

**Answer: B) Code reusability**

**Explanation:** Functions allow you to write code once and reuse it multiple times by calling the function. This reduces code duplication, makes maintenance easier, and improves organization. Instead of copying the same code in multiple places, you define it once as a function and call it wherever needed.

---

## Question 12

What will this code output?

```python
def show_stars():
    print("***")

print("Start")
show_stars()
print("End")
```

A) `Start *** End`
B) `Start` then `***` then `End` (on separate lines)
C) `***`
D) Error

**Answer: B) `Start` then `***` then `End` (on separate lines)**

**Explanation:** The code executes sequentially:
1. `print("Start")` outputs "Start"
2. `show_stars()` is called, which prints "***"
3. `print("End")` outputs "End"

Each print statement outputs on a new line, so the result is three lines of output.

---

## Question 13

Can a function contain conditional statements (if/else)?

A) No, only print statements
B) No, only loops
C) Yes, functions can contain any valid Python code
D) Only simple functions can

**Answer: C) Yes, functions can contain any valid Python code**

**Explanation:** Functions can contain any valid Python code including: conditionals (if/else), loops (for/while), calculations, variable assignments, other function calls, and more. Functions are containers for organized, reusable code blocks of any complexity.

---

## Question 14

What happens if you have a syntax error inside a function definition?

A) Only the function fails when called
B) Python reports the error immediately when defining
C) The error is ignored
D) Python auto-corrects it

**Answer: B) Python reports the error immediately when defining**

**Explanation:** Python checks syntax when it parses the function definition. If there's a syntax error (like missing colon, incorrect indentation, invalid syntax), Python will raise a SyntaxError immediately when it tries to define the function, before the function is ever called.

---

## Question 15

Which is true about the `pass` statement in functions?

A) It terminates the function
B) It's a placeholder that does nothing
C) It returns a value
D) It's required in all functions

**Answer: B) It's a placeholder that does nothing**

**Explanation:** The `pass` statement is a null operation - when executed, nothing happens. It's useful as a placeholder when defining a function structure but not implementing it yet. For example:
```python
def future_function():
    pass  # Will implement later
```
Without `pass`, an empty function body would cause a syntax error.

---

## Summary

### Key Concepts Tested:

1. **Function Syntax**: `def` keyword, colon, indentation
2. **Function Calling**: Using function_name() with parentheses
3. **Execution Order**: Define before call
4. **Naming Conventions**: snake_case for functions
5. **Code Reusability**: Call functions multiple times
6. **Function Body**: Can contain any valid Python code
7. **Benefits**: Organization, reusability, maintainability
8. **Indentation**: Syntactically significant, defines function body
9. **Pass Statement**: Placeholder for empty functions
10. **Error Handling**: Syntax errors caught at definition time

### Function Definition Template:

```python
def function_name():
    """Optional docstring describing the function."""
    # Function body - indented code
    # Can include any valid Python code
    print("Example output")

# Call the function
function_name()
```

### Common Mistakes to Avoid:

1. **Forgetting Parentheses**: `function_name` vs `function_name()`
   - Without parentheses, you reference the function object
   - With parentheses, you call/execute the function

2. **Calling Before Defining**:
   ```python
   # WRONG
   greet()  # Error!
   def greet():
       print("Hi")

   # RIGHT
   def greet():
       print("Hi")
   greet()  # Works!
   ```

3. **Missing Colon**:
   ```python
   # WRONG
   def greet()  # Missing colon
       print("Hi")

   # RIGHT
   def greet():  # Has colon
       print("Hi")
   ```

4. **Incorrect Indentation**:
   ```python
   # WRONG
   def greet():
   print("Hi")  # Not indented

   # RIGHT
   def greet():
       print("Hi")  # Properly indented
   ```

5. **Invalid Function Names**:
   ```python
   # WRONG
   def 2greet():      # Starts with number
   def my-function(): # Contains hyphen
   def def():         # Reserved keyword

   # RIGHT
   def greet2():      # Number at end is OK
   def my_function(): # Underscore is OK
   def my_def():      # 'def' as part of name is OK
   ```

### Best Practices:

1. **Use Descriptive Names**: `calculate_total()` is better than `calc()` or `c()`

2. **One Task Per Function**: Each function should do one thing well

3. **Consistent Naming**: Always use snake_case for function names

4. **Add Docstrings**: Document what the function does
   ```python
   def greet():
       """Print a greeting message to the user."""
       print("Hello!")
   ```

5. **Keep Functions Short**: Aim for functions that fit on one screen

6. **Test Functions**: Make sure each function works before using it

7. **Group Related Functions**: Organize functions logically in your code

### Why Use Functions?

1. **Reusability**: Write once, use many times
   ```python
   def print_header():
       print("=" * 40)

   print_header()  # Use it
   # ... other code ...
   print_header()  # Reuse it
   ```

2. **Organization**: Break complex programs into manageable pieces

3. **Readability**: Named functions make code self-documenting
   ```python
   # Instead of:
   for i in range(1, 11):
       print(i * i)

   # Use:
   def print_squares():
       for i in range(1, 11):
           print(i * i)

   print_squares()  # Clear what this does
   ```

4. **Maintainability**: Update in one place, changes apply everywhere

5. **Testing**: Test individual functions independently

6. **Abstraction**: Hide complex details behind simple function calls

### Quick Reference:

```python
# Basic function
def greet():
    print("Hello, World!")

# Function with multiple statements
def show_menu():
    print("1. Start")
    print("2. Exit")

# Function with loop
def count_to_five():
    for i in range(1, 6):
        print(i)

# Function with conditional
def check_age():
    age = 20
    if age >= 18:
        print("Adult")
    else:
        print("Minor")

# Calling functions
greet()
show_menu()
count_to_five()
check_age()
```

### Real-World Analogy:

Think of functions like recipes:
- **Recipe Name** = Function name
- **Ingredients List** = Parameters (covered in next LO)
- **Instructions** = Function body
- **Following the Recipe** = Calling the function
- **Finished Dish** = Return value (covered in future LO)

Just like you can use the same recipe multiple times to make the same dish, you can call the same function multiple times to perform the same operation.

### Memory Aid:

**D.E.F. - Define, Execute, Function**
- **Define** the function with `def`
- **Execute** the function body when called
- **Function** name followed by `()` to call

Remember: "Define before you dine" - define functions before calling them!
