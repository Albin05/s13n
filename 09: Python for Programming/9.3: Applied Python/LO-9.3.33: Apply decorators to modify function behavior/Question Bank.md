# Question Bank: Apply Decorators

## Problem 1 (Easy)

**Title:** Simple Logging Decorator

**Problem Statement:**
Create a decorator called `log_function` that prints "Calling [function_name]" before executing the function and "Finished [function_name]" after execution.

**Input Format:**
Apply the decorator to any function.

**Output Format:**
Print log messages before and after function execution.

**Sample Usage:**
```python
@log_function
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

**Sample Output:**
```
Calling greet
Hello, Alice!
Finished greet
```

**Constraints:**
- Decorator must work with functions that have any number of arguments
- Use *args and **kwargs

---

## Problem 2 (Easy)

**Title:** Uppercase Decorator

**Problem Statement:**
Create a decorator called `uppercase` that converts the return value of a function to uppercase.

**Input Format:**
Apply decorator to functions that return strings.

**Output Format:**
Return the uppercase version of the function's return value.

**Sample Usage:**
```python
@uppercase
def get_name():
    return "alice"

print(get_name())
```

**Sample Output:**
```
ALICE
```

**Constraints:**
- Function will always return a string
- Preserve original function behavior

---

## Problem 3 (Medium)

**Title:** Execution Time Decorator

**Problem Statement:**
Create a decorator called `time_it` that measures and prints how long a function takes to execute in seconds.

**Input Format:**
Apply decorator to any function.

**Output Format:**
Print execution time in seconds with 4 decimal places.

**Sample Usage:**
```python
import time

@time_it
def slow_function():
    time.sleep(1)
    return "Done"

result = slow_function()
```

**Sample Output:**
```
slow_function executed in 1.0001 seconds
```

**Constraints:**
- Use the time module
- Print time with 4 decimal places
- Return the original function result

**Hint:**
Use `time.time()` before and after function execution, then calculate the difference.

---

## Problem 4 (Medium)

**Title:** Repeat Decorator

**Problem Statement:**
Create a decorator factory called `repeat` that takes a parameter `times` and creates a decorator that executes the function that many times.

**Input Format:**
A decorator that accepts a `times` parameter.

**Output Format:**
Execute the function the specified number of times.

**Sample Usage:**
```python
@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
```

**Sample Output:**
```
Hello!
Hello!
Hello!
```

**Constraints:**
- Must be a decorator factory (takes parameter)
- times >= 1
- Function should execute exactly `times` times

---

## Problem 5 (Hard)

**Title:** Cache Decorator with Expiry

**Problem Statement:**
Create a decorator called `cache_with_expiry` that caches function results for a specified number of seconds. After the expiry time, recalculate the result.

**Input Format:**
A decorator that takes `expiry_seconds` parameter.

**Output Format:**
Return cached result if not expired, otherwise recalculate.

**Sample Usage:**
```python
import time

@cache_with_expiry(expiry_seconds=2)
def expensive_calculation(n):
    print(f"Calculating for {n}...")
    time.sleep(1)  # Simulate expensive operation
    return n * n

print(expensive_calculation(5))  # Calculates
print(expensive_calculation(5))  # Uses cache
time.sleep(3)
print(expensive_calculation(5))  # Cache expired, recalculates
```

**Sample Output:**
```
Calculating for 5...
25
25
Calculating for 5...
25
```

**Constraints:**
- Use time module to track expiry
- Store cache with timestamp
- Support multiple different arguments
- Clear expired entries

**Hint:**
Store cache as a dictionary with keys being function arguments and values being (result, timestamp) tuples.
