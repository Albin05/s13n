# Lecture Notes: Apply Decorators

## Decorators

Decorators are a powerful feature in Python that allow you to modify or enhance functions without changing their source code. They use the `@decorator_name` syntax.


---

<div align="center">

![Variables concept - labeled storage containers](https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800&q=80)

*Think of variables as labeled containers storing different types of data*

</div>

---

## Introduction

Decorators implement **aspect-oriented programming** - adding cross-cutting concerns without modifying functions! This is **metaprogramming** - code that modifies code at definition time. Decorators are **higher-order functions** - functions that take functions and return enhanced functions!

### Why Decorators are Powerful

**Problem without decorators**: Cross-cutting concerns pollute code:
```python
# MESSY - logging mixed with business logic!
def calculate_tax(income):
    print("Starting calculate_tax")  # Logging
    start = time.time()              # Timing
    result = income * 0.3            # Actual logic
    print(f"Took {time.time()-start}s")  # Timing
    print("Finished calculate_tax")   # Logging
    return result
# Business logic buried in infrastructure!
```

**Solution with decorators**: Separate concerns cleanly:
```python
# CLEAN - concerns separated!
@log_calls
@timer
def calculate_tax(income):
    return income * 0.3  # Pure business logic!
# Logging and timing added without touching function!
```

**This is separation of concerns** - each decorator handles one aspect!

### Historical Context

**Decorators** added **Python 2.4** (2004) with **PEP 318**. Before: `func = decorator(func)` syntax - verbose! **@syntax** inspired by **Java annotations** (2004) but more powerful - Python decorators execute code!

**Higher-order functions** from **lambda calculus** (Alonzo Church, 1930s) - functions as first-class values! **LISP** (1958) pioneered functions-as-arguments. Python decorators are **closures** - inner functions remembering outer scope!

**Aspect-Oriented Programming (AOP)** formalized by **Gregor Kiczales** (1997) - cross-cutting concerns (logging, security, caching) separated from business logic. Decorators bring AOP to Python elegantly!

### Real-World Analogies

**Decorators like gift wrapping**:
- **Function**: The gift (core functionality)
- **Decorator**: Wrapping paper, ribbon, tag (added behavior)
- **Result**: Enhanced presentation without changing gift!
**Wrap functions with extra features!**

**Or like building security layers**:
```python
@require_admin        # Check admin status
@require_login        # Check authentication
@rate_limit(100)      # Limit requests
def delete_database():
    pass  # Dangerous operation!
# Three security layers, function untouched!
```

**Or like restaurant food preparation**:
- **Function**: Raw ingredients → cooked dish
- **@plate_decorator**: Add plating, garnish
- **@quality_check**: Verify taste, temperature
- **@serve_decorator**: Add service presentation
**Each step enhances without changing the core dish!**

### Decorator = Higher-Order Function

**What `@decorator` actually does**:
```python
@my_decorator
def say_hello():
    print("Hello!")

# Equivalent to:
def say_hello():
    print("Hello!")
say_hello = my_decorator(say_hello)  # Replace!
# say_hello now points to wrapper function!
```

**This is function replacement** - old function wrapped in new behavior!

---
### Basic Decorator Syntax

```python
def decorator_name(func):
    def wrapper(*args, **kwargs):
        # Code before function
        result = func(*args, **kwargs)
        # Code after function
        return result
    return wrapper

@decorator_name
def my_function():
    pass
```

## Simple Decorator Example

```python
def simple_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello, World!")

say_hello()
# Output:
# Before function execution
# Hello, World!
# After function execution
```

## How Decorators Work

```python
# These are equivalent:

# With @ syntax
@simple_decorator
def greet():
    print("Hi!")

# Without @ syntax (what Python actually does)
def greet():
    print("Hi!")
greet = simple_decorator(greet)
```

## Decorator with Arguments

```python
def log_decorator(func):
    """Decorator that logs function calls"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}()")
        result = func(*args, **kwargs)
        print(f"{func.__name__}() finished")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

@log_decorator
def greet(name):
    return f"Hello, {name}!"

result = add(5, 3)
print(f"Result: {result}")
# Output:
# Calling add()
# add() finished
# Result: 8

message = greet("Alice")
print(message)
# Output:
# Calling greet()
# greet() finished
# Hello, Alice!
```

## Real-World Examples

### Example 1: Timing Decorator

```python
import time

def timer_decorator(func):
    """Measure execution time of a function"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.4f} seconds to execute")
        return result
    return wrapper

@timer_decorator
def slow_function():
    """Simulate a slow operation"""
    time.sleep(1)
    return "Done!"

@timer_decorator
def calculate_sum(n):
    """Calculate sum of numbers from 1 to n"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

result = slow_function()
print(result)
# Output:
# slow_function took 1.0001 seconds to execute
# Done!

sum_result = calculate_sum(1000000)
print(f"Sum: {sum_result}")
# Output:
# calculate_sum took 0.0523 seconds to execute
# Sum: 500000500000
```

### Example 2: Authentication Decorator

```python
# Simulate a logged-in user
current_user = {"username": "alice", "logged_in": True}

def require_login(func):
    """Decorator to check if user is logged in"""
    def wrapper(*args, **kwargs):
        if current_user.get("logged_in"):
            return func(*args, **kwargs)
        else:
            return "Error: You must be logged in to access this function"
    return wrapper

@require_login
def view_profile():
    return f"Profile of {current_user['username']}"

@require_login
def edit_settings():
    return "Settings updated successfully"

def view_public_page():
    return "Welcome to our public page"

# User is logged in
print(view_profile())  # Profile of alice
print(edit_settings())  # Settings updated successfully

# User logs out
current_user["logged_in"] = False
print(view_profile())  # Error: You must be logged in to access this function

# Public page works without login
print(view_public_page())  # Welcome to our public page
```

### Example 3: Retry Decorator

```python
import random

def retry(max_attempts=3):
    """Decorator that retries a function if it fails"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    if attempts >= max_attempts:
                        print(f"Failed after {max_attempts} attempts")
                        raise
        return wrapper
    return decorator

@retry(max_attempts=3)
def unstable_operation():
    """Simulates an operation that might fail"""
    if random.random() < 0.7:  # 70% chance of failure
        raise Exception("Random failure occurred")
    return "Success!"

# Try the unstable operation
try:
    result = unstable_operation()
    print(result)
except Exception as e:
    print(f"Final error: {e}")

# Output (varies due to randomness):
# Attempt 1 failed: Random failure occurred
# Attempt 2 failed: Random failure occurred
# Success!
```

### Example 4: Validation Decorator

```python
def validate_positive(func):
    """Decorator to ensure all numeric arguments are positive"""
    def wrapper(*args, **kwargs):
        # Check positional arguments
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Argument must be positive, got {arg}")

        # Check keyword arguments
        for key, value in kwargs.items():
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError(f"Argument '{key}' must be positive, got {value}")

        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_area(length, width):
    """Calculate rectangle area"""
    return length * width

@validate_positive
def calculate_discount(price, discount_percent):
    """Calculate discounted price"""
    discount = price * (discount_percent / 100)
    return price - discount

# Valid calls
print(f"Area: {calculate_area(5, 10)}")  # Area: 50
print(f"Discounted price: {calculate_discount(100, 20)}")  # Discounted price: 80.0

# Invalid calls
try:
    calculate_area(-5, 10)
except ValueError as e:
    print(f"Error: {e}")  # Error: Argument must be positive, got -5

try:
    calculate_discount(100, -10)
except ValueError as e:
    print(f"Error: {e}")  # Error: Argument must be positive, got -10
```

### Example 5: Caching Decorator (Memoization)

```python
def memoize(func):
    """Decorator to cache function results"""
    cache = {}

    def wrapper(*args):
        if args in cache:
            print(f"Returning cached result for {args}")
            return cache[args]
        else:
            print(f"Calculating result for {args}")
            result = func(*args)
            cache[args] = result
            return result

    return wrapper

@memoize
def fibonacci(n):
    """Calculate nth Fibonacci number"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@memoize
def factorial(n):
    """Calculate factorial"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("Calculating fibonacci(5):")
print(fibonacci(5))
# Output:
# Calculating result for (5,)
# Calculating result for (4,)
# Calculating result for (3,)
# Calculating result for (2,)
# Calculating result for (1,)
# Returning cached result for (1,)
# Calculating result for (0,)
# Returning cached result for (2,)
# Returning cached result for (3,)
# 5

print("\nCalculating factorial(5):")
print(factorial(5))
# Output:
# Calculating result for (5,)
# Calculating result for (4,)
# Calculating result for (3,)
# Calculating result for (2,)
# Calculating result for (1,)
# 120
```

## Multiple Decorators

```python
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!!!"
    return wrapper

@exclamation_decorator
@uppercase_decorator
def greet(name):
    return f"hello {name}"

print(greet("alice"))
# Output: HELLO ALICE!!!

# Decorators are applied bottom-up:
# 1. uppercase_decorator is applied first
# 2. exclamation_decorator is applied second
```

## Decorators with Parameters

```python
def repeat(times):
    """Decorator factory that creates a decorator"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    return f"Hello, {name}!"

messages = greet("Alice")
for msg in messages:
    print(msg)
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!

@repeat(times=5)
def roll_dice():
    import random
    return random.randint(1, 6)

rolls = roll_dice()
print(f"Dice rolls: {rolls}")
# Output: Dice rolls: [3, 1, 6, 2, 4] (random)
```

## Preserving Function Metadata

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves original function's metadata
    def wrapper(*args, **kwargs):
        """Wrapper documentation"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def important_function():
    """This function does important things"""
    pass

print(important_function.__name__)  # important_function (not wrapper)
print(important_function.__doc__)   # This function does important things
```

## Class-Based Decorators

```python
class CountCalls:
    """Decorator that counts function calls"""

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")  # Call 1 to say_hello
say_hello("Bob")    # Call 2 to say_hello
say_hello("Charlie")  # Call 3 to say_hello
```

## Built-in Decorators

```python
class MyClass:
    """Demonstrate built-in decorators"""

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        """Getter - access like an attribute"""
        return self._value

    @value.setter
    def value(self, new_value):
        """Setter - set like an attribute"""
        if new_value < 0:
            raise ValueError("Value must be non-negative")
        self._value = new_value

    @staticmethod
    def static_method():
        """Static method - doesn't need self or cls"""
        return "I'm a static method"

    @classmethod
    def class_method(cls):
        """Class method - receives the class as first argument"""
        return f"I'm a class method of {cls.__name__}"

# Using the decorators
obj = MyClass(10)
print(obj.value)  # 10 (using @property getter)
obj.value = 20    # Using @property setter
print(obj.value)  # 20

print(MyClass.static_method())  # I'm a static method
print(MyClass.class_method())   # I'm a class method of MyClass
```

## Key Takeaways

1. **Decorators**: Functions that modify other functions
2. **@ syntax**: Syntactic sugar for applying decorators
3. **Wrapper function**: Inner function that wraps the original
4. **Preserving metadata**: Use `@wraps` from functools
5. **Multiple decorators**: Applied bottom-up
6. **Decorator factories**: Functions that return decorators
7. **Built-in decorators**: @property, @staticmethod, @classmethod
8. **Use cases**: Logging, timing, authentication, caching, validation
