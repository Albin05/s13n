# Post-class Quiz: Returning Values from Functions Using Return

## Question 1

What is the primary purpose of the `return` statement in a function?

A) To print output to the console
B) To send a value back to the caller
C) To end the program
D) To create a new variable

**Answer: B) To send a value back to the caller**

**Explanation:** The `return` statement sends a value back to the code that called the function, allowing that value to be stored, used in calculations, or passed to other functions. This is different from `print()`, which only displays output to the console. Example:
```python
def add(a, b):
    return a + b  # Sends value back

result = add(5, 3)  # result gets 8
print(result)  # Now we can use the returned value
```
Without `return`, the function would execute but wouldn't provide a value back to the caller.

---

## Question 2

What will this code output?

```python
def calculate():
    return 10 + 5
    print("Done")

result = calculate()
print(result)
```

A) `Done` then `15`
B) `15` then `Done`
C) `15` only
D) `Done` only

**Answer: C) `15` only**

**Explanation:** When a `return` statement is executed, the function exits immediately. Any code after the `return` statement is unreachable and will never execute. In this case:
1. Function is called
2. `return 10 + 5` executes, sending back 15
3. Function exits immediately
4. `print("Done")` is never reached (unreachable code)
5. `result` receives 15
6. `print(result)` displays 15

This is a common mistake - always place `return` as the last statement in your function logic.

---

## Question 3

What is the difference between these two functions?

```python
# Function A
def add_print(a, b):
    print(a + b)

# Function B
def add_return(a, b):
    return a + b
```

A) They do exactly the same thing
B) Function A can be used in calculations, Function B cannot
C) Function B can be used in calculations, Function A cannot
D) Function A is faster than Function B

**Answer: C) Function B can be used in calculations, Function A cannot**

**Explanation:** This demonstrates the critical difference between `print()` and `return`:

**Function A (print):**
```python
x = add_print(5, 3)  # Displays: 8
print(x)  # Output: None (function returned nothing)
y = x + 10  # Error! Can't add None + 10
```

**Function B (return):**
```python
x = add_return(5, 3)  # Returns 8 (no display)
print(x)  # Output: 8
y = x + 10  # Works! y = 18
```

`print()` displays output but doesn't provide a value for reuse. `return` sends the value back for further use in your code.

---

## Question 4

What does a function return if no `return` statement is specified?

A) 0
B) Empty string ""
C) None
D) Error is raised

**Answer: C) None**

**Explanation:** In Python, if a function doesn't have a `return` statement, it automatically returns `None`. Example:
```python
def greet(name):
    print(f"Hello, {name}")
    # No return statement

result = greet("Alice")
print(result)  # Output: None
```

This is called an "implicit return None". You can also explicitly return None:
```python
def do_something():
    print("Working...")
    return None  # Explicit

# Both functions behave the same way
```

---

## Question 5

What will this code print?

```python
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

result = check_number(-5)
print(result)
```

A) `Positive`
B) `Negative`
C) `Zero`
D) All three strings

**Answer: B) `Negative`**

**Explanation:** A function can have multiple `return` statements, but only ONE will execute - the first one that's reached. Here's the flow:
1. `check_number(-5)` is called
2. Check `if num > 0`: -5 > 0 is False, skip
3. Check `elif num < 0`: -5 < 0 is True, enter this block
4. Execute `return "Negative"` - function exits immediately
5. The `else` block never runs
6. `result` receives "Negative"

Only the first matching condition's return executes. This pattern of multiple returns is useful for different cases.

---

## Question 6

What is returned by this function?

```python
def get_info():
    name = "Alice"
    age = 25
    return name, age

result = get_info()
print(type(result))
```

A) `<class 'list'>`
B) `<class 'dict'>`
C) `<class 'tuple'>`
D) `<class 'str'>`

**Answer: C) `<class 'tuple'>`**

**Explanation:** When you return multiple values separated by commas, Python automatically packs them into a tuple:
```python
def get_info():
    return "Alice", 25  # Returns tuple: ("Alice", 25)

# Can unpack the tuple
name, age = get_info()
print(name)  # Alice
print(age)   # 25

# Or keep as tuple
result = get_info()
print(result)  # ('Alice', 25)
print(type(result))  # <class 'tuple'>
```

This is a powerful feature for returning multiple related values from a single function.

---

## Question 7

What will this function return?

```python
def find_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num

result = find_even([1, 3, 5, 8, 9, 10])
print(result)
```

A) `[8, 10]` (all even numbers)
B) `8` (first even number)
C) `10` (last even number)
D) `None`

**Answer: B) `8` (first even number)**

**Explanation:** When `return` is executed inside a loop, the function exits immediately, returning that value and stopping the loop:
```python
# Flow of execution:
[1, 3, 5, 8, 9, 10]
 ↓
Check 1: odd, continue
Check 3: odd, continue
Check 5: odd, continue
Check 8: even! → return 8 → EXIT FUNCTION
# 9 and 10 are never checked
```

This is a common pattern for "find first" operations. If you wanted all even numbers, you'd build a list and return it after the loop:
```python
def find_all_evens(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens  # Return after loop completes
```

---

## Question 8

Which function follows the early return pattern correctly?

A)
```python
def validate(age):
    if age >= 18:
        return "Valid"
    else:
        if age < 0:
            return "Invalid"
        else:
            return "Too young"
```

B)
```python
def validate(age):
    if age < 0:
        return "Invalid"
    if age < 18:
        return "Too young"
    return "Valid"
```

C)
```python
def validate(age):
    result = ""
    if age < 0:
        result = "Invalid"
    elif age < 18:
        result = "Too young"
    else:
        result = "Valid"
    return result
```

D) All are equally good

**Answer: B) - Early return pattern**

**Explanation:** The early return pattern handles error/edge cases first, then handles the normal case:

**Option B (Best - Early Return Pattern):**
```python
def validate(age):
    # Check errors first, exit early
    if age < 0:
        return "Invalid"  # Exit immediately
    if age < 18:
        return "Too young"  # Exit immediately
    # If we reach here, age is valid
    return "Valid"
```

**Benefits:**
- Clearer logic flow
- Less nesting
- Error cases are obvious and handled first
- Main logic isn't buried in nested conditions

**Option A** has unnecessary nesting. **Option C** works but requires tracking state in a variable. Option B is cleaner and more Pythonic.

---

## Question 9

What can you do with a returned value?

A) Store it in a variable
B) Use it in calculations
C) Pass it to another function
D) All of the above

**Answer: D) All of the above**

**Explanation:** Returned values are extremely versatile:

**1. Store in a variable:**
```python
result = add(5, 3)  # result = 8
```

**2. Use in calculations:**
```python
total = add(5, 3) + add(10, 2)  # 8 + 12 = 20
```

**3. Pass to another function:**
```python
print(add(5, 3))  # Pass 8 to print()
squared = square(add(2, 3))  # Pass 5 to square()
```

**4. Use in conditionals:**
```python
if is_valid(data):
    process(data)
```

**5. Return from another function:**
```python
def calculate():
    return add(5, 3)  # Return the result of add()
```

This flexibility makes functions with return statements reusable building blocks for complex programs.

---

## Question 10

What will this code output?

```python
def process(x):
    if x < 0:
        return
    return x * 2

print(process(-5))
print(process(5))
```

A) `None` and `10`
B) `0` and `10`
C) `-10` and `10`
D) Error

**Answer: A) `None` and `10`**

**Explanation:** `return` without a value returns `None`:

**First call: `process(-5)`**
```python
x = -5
if x < 0:  # True
    return  # Returns None, exits function
# x * 2 never executes
```
Output: `None`

**Second call: `process(5)`**
```python
x = 5
if x < 0:  # False, skip
return x * 2  # Returns 10
```
Output: `10`

**Common use case:** Using bare `return` to exit early when there's nothing meaningful to return:
```python
def log_message(msg, level):
    if level < 1:  # Invalid level
        return  # Exit early, return None
    print(f"[Level {level}] {msg}")
```

---

## Question 11

Which statement about return values is FALSE?

A) A function can return different data types depending on conditions
B) You can only return one value at a time
C) Return statements execute immediately and exit the function
D) Returned values can be ignored when calling a function

**Answer: B) You can only return one value at a time**

**Explanation:** This statement is FALSE because Python can return multiple values as a tuple:

```python
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

minimum, maximum, total = get_stats([1, 2, 3, 4, 5])
# Returns: (1, 5, 15)
```

**Why other options are TRUE:**

**A) Different data types:**
```python
def process(x):
    if x < 0:
        return "Negative"  # Returns string
    return x * 2  # Returns number
```

**C) Immediate execution and exit:**
```python
def example():
    return 5
    print("Never runs")  # Unreachable
```

**D) Returned values can be ignored:**
```python
calculate_total(10, 20)  # Call but don't store result
# Result is calculated but not used
```

---

## Question 12

What will be the value of `result`?

```python
def multiply(a, b):
    answer = a * b
    print(f"The product is {answer}")

result = multiply(4, 5)
print(f"Result: {result}")
```

A) `Result: 20`
B) `Result: The product is 20`
C) `Result: None`
D) Error

**Answer: C) `Result: None`**

**Explanation:** The function prints but doesn't return anything, so it implicitly returns `None`:

**Output:**
```
The product is 20  ← From print() inside function
Result: None  ← result is None
```

**To fix this, add a return statement:**
```python
def multiply(a, b):
    answer = a * b
    print(f"The product is {answer}")
    return answer  # Now returns the value

result = multiply(4, 5)
print(f"Result: {result}")
```

**Output:**
```
The product is 20
Result: 20
```

Many beginners confuse printing with returning - they're different operations with different purposes.

---

## Question 13

What is the output of this code?

```python
def outer():
    def inner():
        return 10
    inner()
    return 5

result = outer()
print(result)
```

A) `10`
B) `5`
C) `15`
D) `None`

**Answer: B) `5`**

**Explanation:** The inner function returns 10, but that return value is not used or returned by the outer function:

**Step-by-step:**
1. `outer()` is called
2. `inner()` is called inside `outer()`
3. `inner()` returns 10, but this value is not stored or used
4. `outer()` continues to the next line
5. `outer()` returns 5
6. `result` gets 5

**To use inner's return value:**
```python
def outer():
    def inner():
        return 10
    inner_result = inner()  # Store the returned value
    return inner_result + 5  # Use it

result = outer()
print(result)  # 15
```

Just calling a function doesn't do anything with its return value unless you capture it.

---

## Question 14

Which function correctly returns a boolean value?

A)
```python
def is_adult(age):
    if age >= 18:
        print(True)
    else:
        print(False)
```

B)
```python
def is_adult(age):
    if age >= 18:
        return "True"
    else:
        return "False"
```

C)
```python
def is_adult(age):
    return age >= 18
```

D)
```python
def is_adult(age):
    age >= 18
```

**Answer: C)**

**Explanation:** Let's analyze each option:

**Option A (Wrong - Prints instead of returns):**
```python
result = is_adult(20)
print(result)  # None (function doesn't return anything)
```

**Option B (Wrong - Returns strings, not booleans):**
```python
result = is_adult(20)
print(type(result))  # <class 'str'> not <class 'bool'>
if result:  # "True" string is truthy, but not a real boolean
    print("Adult")
```

**Option C (Correct - Returns actual boolean):**
```python
result = is_adult(20)
print(result)  # True (actual boolean)
print(type(result))  # <class 'bool'>
```
The comparison `age >= 18` evaluates to `True` or `False`, which is directly returned.

**Option D (Wrong - No return statement):**
```python
result = is_adult(20)
print(result)  # None (expression calculated but not returned)
```

**Best practice for boolean functions:** Return the comparison directly rather than using if-else.

---

## Question 15

What is a key benefit of using return statements?

A) They make code run faster
B) They allow function results to be reused and composed
C) They reduce memory usage
D) They make code longer and more detailed

**Answer: B) They allow function results to be reused and composed**

**Explanation:** The primary benefit of `return` is enabling function composition and reusability:

**Without return (Limited reuse):**
```python
def add(a, b):
    print(a + b)

def multiply(a, b):
    print(a * b)

# Can't combine these!
# Want to do: (5 + 3) * 2
add(5, 3)  # Prints 8, but can't use it
multiply(???, 2)  # Can't pass the result of add()
```

**With return (Composable):**
```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Functions can be combined!
result = multiply(add(5, 3), 2)  # (5 + 3) * 2 = 16

# Build complex operations from simple functions
total = add(multiply(2, 3), multiply(4, 5))  # 6 + 20 = 26
```

**Real-world example:**
```python
def calculate_tax(income):
    return income * 0.15

def calculate_net(income):
    tax = calculate_tax(income)  # Use returned value
    return income - tax

net_income = calculate_net(50000)  # $42,500
```

Return statements transform functions into reusable building blocks that can work together to solve complex problems.

---

## Summary

### Key Concepts Tested:

1. **Purpose of Return**: Sends values back to caller, different from print
2. **Unreachable Code**: Code after return never executes
3. **Return vs Print**: Return for data reuse, print for display
4. **Implicit None**: Functions without return automatically return None
5. **Multiple Returns**: Different return statements for different conditions
6. **Returning Multiple Values**: Comma-separated values return as tuple
7. **Return in Loops**: Exits function immediately, useful for "find first"
8. **Early Return Pattern**: Handle errors first, main logic last
9. **Using Returned Values**: Store, calculate, pass to functions, use in conditions
10. **Return Without Value**: Plain `return` exits and returns None
11. **Multiple Values**: Can return more than one value as tuple
12. **No Return Statement**: Implicitly returns None
13. **Nested Functions**: Inner function returns don't affect outer unless captured
14. **Boolean Returns**: Return comparison results directly
15. **Function Composition**: Return enables building complex operations from simple functions

### Common Patterns:

**Pattern 1: Simple Return**
```python
def calculate(x):
    result = x * 2
    return result
```

**Pattern 2: Early Return (Error Handling)**
```python
def process(data):
    if not data:
        return None  # Exit early on error
    # Main logic here
    return processed_data
```

**Pattern 3: Multiple Returns (Conditional)**
```python
def classify(x):
    if x > 0:
        return "Positive"
    elif x < 0:
        return "Negative"
    return "Zero"
```

**Pattern 4: Return Multiple Values**
```python
def get_stats(numbers):
    return min(numbers), max(numbers), len(numbers)

minimum, maximum, count = get_stats([1, 2, 3, 4, 5])
```

**Pattern 5: Boolean Return**
```python
def is_valid(x):
    return x >= 0 and x <= 100
```

**Pattern 6: Return from Loop**
```python
def find_first(items, target):
    for item in items:
        if item == target:
            return item
    return None  # Not found
```

**Pattern 7: Function Composition**
```python
def calculate_total(price, tax_rate):
    tax = calculate_tax(price, tax_rate)
    return price + tax
```

### Return vs Print Comparison:

| Aspect | return | print() |
|--------|--------|---------|
| **Purpose** | Send data back | Display to screen |
| **Reusability** | Value can be reused | Value is lost |
| **Storage** | Can store in variable | Cannot store output |
| **Calculations** | Can use in math | Cannot use in math |
| **Function chains** | Can compose functions | Cannot chain |
| **Best for** | Data processing | User output/debugging |

### Common Mistakes:

**Mistake 1: Forgetting to return**
```python
# WRONG
def add(a, b):
    a + b  # Calculated but not returned

# RIGHT
def add(a, b):
    return a + b
```

**Mistake 2: Code after return**
```python
# WRONG
def calculate():
    return 10
    print("Done")  # Never runs

# RIGHT
def calculate():
    print("Done")
    return 10
```

**Mistake 3: Confusing print with return**
```python
# WRONG - Can't use in calculations
def add(a, b):
    print(a + b)

# RIGHT - Can use result
def add(a, b):
    return a + b
```

**Mistake 4: Not capturing return value**
```python
# WRONG - Value is lost
calculate_total(100, 10)

# RIGHT - Store and use
total = calculate_total(100, 10)
print(total)
```

### Best Practices:

1. **Always return a value** if the function computes something
2. **Return early** for error cases to reduce nesting
3. **Return consistent types** - don't return string sometimes, number other times
4. **Use descriptive function names** that hint at what's returned
5. **Document return values** in comments/docstrings
6. **Return None explicitly** when there's no meaningful value
7. **Avoid side effects** - pure functions that just calculate and return are easier to test
8. **Return comparison results directly** instead of if-else for booleans

### Quick Reference:

```python
# Basic return
def function_name(parameters):
    result = calculate_something(parameters)
    return result

# Multiple returns
def check(x):
    if condition:
        return value1
    return value2

# Return multiple values
def get_data():
    return value1, value2, value3

# Return None
def process():
    if error:
        return None
    return result

# Boolean return
def is_valid(x):
    return x > 0 and x < 100

# Early return
def validate(x):
    if x < 0:
        return "Error"
    if x > 100:
        return "Too large"
    return "Valid"
```

### Memory Aid:

**Print** → For **P**resenting (displaying to users)
**Return** → For **R**eusing (using in code)

Think: "Print shows, Return gives"

---

### Real-World Analogy:

Think of a function like a **vending machine**:
- **Parameters** are like the money you insert (input)
- **Function body** is the internal mechanism
- **Return** is the product that comes out (output you can use)
- **Print** is like a receipt display (shows info but you can't "use" the display)

You can take the returned product (candy bar) and use it (eat it, trade it, save it).
You can't do anything with the display text - it's just information.

---

**Congratulations!** You've completed the quiz on returning values from functions. Understanding `return` is crucial for writing reusable, composable functions that form the building blocks of larger programs. Remember: return is for data you want to reuse, print is for data you want to display!
