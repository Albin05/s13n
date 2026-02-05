# Lecture Script: LO-9.3.33 Apply Decorators to Modify Function Behavior

## [0:00-0:02] Hook (2 min)
**Say**: "Imagine you need to time every function in your application. Copy-paste timing code 50 times? NO! Write it once, slap @timer on each function. That's decorators — code that wraps other code, adding behavior without changing the original function. Magic!"

**Demo**:
```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.5)
    return "Done!"

result = slow_function()
# slow_function took 0.5001 seconds
print(result)  # Done!
```

**Say**: "That @ syntax is a decorator! Let's master them."

## [0:02-0:06] Understanding Decorator Syntax (4 min)

**Say**: "A decorator is a function that takes a function and returns a modified version. The @ symbol is just syntactic sugar."

**Live Code**:
```python
def simple_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

# These two are equivalent:

# With @ syntax (preferred)
@simple_decorator
def say_hello():
    print("Hello, World!")

# Without @ syntax (what Python actually does)
def say_goodbye():
    print("Goodbye, World!")
say_goodbye = simple_decorator(say_goodbye)

# Both work the same way
say_hello()
# Before function execution
# Hello, World!
# After function execution

say_goodbye()
# Before function execution
# Goodbye, World!
# After function execution
```

**Point out**: "The @ syntax applies the decorator at function definition time. Clean and readable!"

**Emphasize**: "Decorators wrap functions — they don't modify the original code, they wrap it with new behavior!"

## [0:06-0:10] Decorators with Arguments (4 min)

**Say**: "Real functions take arguments. Our decorator wrapper must accept any arguments and pass them through."

**Live Code**:
```python
def log_decorator(func):
    """Decorator that logs function calls"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}()")
        print(f"  Args: {args}")
        print(f"  Kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__}() returned: {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

@log_decorator
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Test with positional arguments
print(add(5, 3))
# Calling add()
#   Args: (5, 3)
#   Kwargs: {}
# add() returned: 8
# 8

# Test with keyword arguments
print(greet("Alice", greeting="Hi"))
# Calling greet()
#   Args: ('Alice',)
#   Kwargs: {'greeting': 'Hi'}
# greet() returned: Hi, Alice!
# Hi, Alice!
```

**Point out**: "*args captures positional arguments, **kwargs captures keyword arguments. Pass them through to the original function!"

## [0:10-0:13] Real-World Example: Authentication Decorator (3 min)

**Say**: "Decorators are perfect for cross-cutting concerns like authentication, caching, and validation."

**Live Code**:
```python
# Simulate logged-in user
current_user = {"username": "alice", "logged_in": True}

def require_login(func):
    """Decorator to check if user is logged in"""
    def wrapper(*args, **kwargs):
        if current_user.get("logged_in"):
            return func(*args, **kwargs)
        else:
            return "Error: You must be logged in!"
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
print(view_profile())  # Error: You must be logged in!

# Public page still works
print(view_public_page())  # Welcome to our public page
```

**Say**: "Authentication logic in ONE place, applied to many functions. DRY principle in action!"

## [0:13-0:16] Real-World Example: Retry Decorator (3 min)

**Say**: "Decorators can add retry logic for unreliable operations like network calls."

**Live Code**:
```python
import random

def retry(max_attempts=3):
    """Decorator that retries a function if it fails"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    if attempts >= max_attempts:
                        print(f"Failed after {max_attempts} attempts")
                        raise
        return wrapper
    return decorator

@retry(max_attempts=3)
def unstable_network_call():
    """Simulates an unreliable operation"""
    if random.random() < 0.7:  # 70% failure rate
        raise ConnectionError("Network error")
    return "Success!"

# Try the operation
try:
    result = unstable_network_call()
    print(result)
except ConnectionError:
    print("Final failure")

# Output (varies):
# Attempt 1 failed: Network error
# Attempt 2 failed: Network error
# Success!
```

**Point out**: "This is a decorator factory — retry() returns a decorator. That's why we call it with () even with no arguments!"

## [0:16-0:19] Real-World Example: Caching Decorator (3 min)

**Say**: "Memoization — cache expensive function results to avoid recalculation."

**Live Code**:
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

print("Calculating fibonacci(5):")
print(fibonacci(5))
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

print("\nCalculating fibonacci(6):")
print(fibonacci(6))
# Calculating result for (6,)
# Returning cached result for (5,)
# Returning cached result for (4,)
# 8
```

**Say**: "Fibonacci without memoization is exponentially slow. With memoization, it's lightning fast!"

## [0:19-0:21] Stacking Multiple Decorators (2 min)

**Say**: "You can apply multiple decorators to a single function. They're applied bottom-up."

**Live Code**:
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

@exclamation_decorator  # Applied second
@uppercase_decorator    # Applied first
def greet(name):
    return f"hello {name}"

print(greet("alice"))
# HELLO ALICE!!!

# Order matters!
@uppercase_decorator    # Applied second
@exclamation_decorator  # Applied first
def greet2(name):
    return f"hello {name}"

print(greet2("bob"))
# HELLO BOB!!!
```

**Point out**: "Decorators are applied bottom-up: the one closest to the function is applied first!"

## [0:21-0:23] Preserving Function Metadata (2 min)

**Say**: "Decorators replace the function object. Use @wraps to preserve the original function's name and docstring."

**Live Code**:
```python
from functools import wraps

# Without @wraps - bad!
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        """Wrapper documentation"""
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def important_function():
    """This function does important things"""
    pass

print(important_function.__name__)  # wrapper
print(important_function.__doc__)   # Wrapper documentation

# With @wraps - good!
def good_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper documentation"""
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def another_function():
    """This function does important things"""
    pass

print(another_function.__name__)  # another_function
print(another_function.__doc__)   # This function does important things
```

**Emphasize**: "Always use @wraps! It keeps introspection working correctly!"

## [0:23-0:24] Practice Challenge (1 min)

**Challenge**: "Create a @validate_positive decorator that ensures all numeric arguments are positive."

**Skeleton**:
```python
def validate_positive(func):
    def wrapper(*args, **kwargs):
        # TODO: Check if all numeric args are positive
        # If not, raise ValueError
        # Otherwise, call and return func(*args, **kwargs)
        pass
    return wrapper

@validate_positive
def divide(a, b):
    return a / b

# Should work
print(divide(10, 2))

# Should raise ValueError
print(divide(-10, 2))
```

**Solution** (show after 1 minute):
```python
def validate_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Argument must be positive, got {arg}")
        for key, value in kwargs.items():
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError(f"{key} must be positive, got {value}")
        return func(*args, **kwargs)
    return wrapper
```

## [0:24-0:25] Wrap-up (1 min)

**Key Points**:
1. **Decorators**: Functions that wrap other functions
2. **@ syntax**: Applies decorator at function definition
3. **wrapper(*args, **kwargs)**: Accept and pass through any arguments
4. **Decorator factories**: Functions that return decorators (for parameterized decorators)
5. **@wraps**: Preserve original function metadata

**Common Mistakes**:
- Forgetting to return wrapper function from decorator
- Not using *args, **kwargs to handle all argument types
- Forgetting to return the result of func()
- Not using @wraps from functools

**Real-World Use Cases**:
- Logging and debugging
- Authentication and authorization
- Caching and memoization
- Timing and performance monitoring
- Input validation
- Error handling and retries

**Built-in Decorators to Know**:
- @property: Make methods look like attributes
- @staticmethod: Methods that don't need self
- @classmethod: Methods that receive the class

**Closing**: "Decorators are one of Python's most elegant features! They keep code DRY, separate concerns, and make functions more powerful without cluttering the original logic. Use them wisely!"
