# Editorials: Apply Decorators

## Problem 1: Simple Logging Decorator

```python
def log_function(func):
    """Decorator that logs function calls"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

# Test
@log_function
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

### Explanation
The decorator wraps the original function, printing log messages before and after execution. The `*args` and `**kwargs` allow it to work with any function signature.

---

## Problem 2: Uppercase Decorator

```python
def uppercase(func):
    """Decorator that converts return value to uppercase"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

# Test
@uppercase
def get_name():
    return "alice"

print(get_name())  # ALICE
```

### Explanation
The decorator calls the original function, captures its return value, and converts it to uppercase before returning it.

---

## Problem 3: Execution Time Decorator

```python
import time

def time_it(func):
    """Decorator that measures execution time"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.4f} seconds")
        return result
    return wrapper

# Test
@time_it
def slow_function():
    time.sleep(1)
    return "Done"

result = slow_function()
```

### Explanation
Records start time before execution, end time after, calculates difference, and prints formatted time.

---

## Problem 4: Repeat Decorator

```python
def repeat(times):
    """Decorator factory that repeats function execution"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

# Test
@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
```

### Explanation
This is a decorator factory (decorator with parameters). The outer function takes the parameter, the middle function is the actual decorator, and the innermost function is the wrapper.

---

## Problem 5: Cache Decorator with Expiry

```python
import time

def cache_with_expiry(expiry_seconds):
    """Decorator factory that caches results with expiry"""
    def decorator(func):
        cache = {}

        def wrapper(*args):
            current_time = time.time()

            # Check if result is in cache and not expired
            if args in cache:
                result, timestamp = cache[args]
                if current_time - timestamp < expiry_seconds:
                    return result

            # Calculate new result
            result = func(*args)
            cache[args] = (result, current_time)
            return result

        return wrapper
    return decorator

# Test
@cache_with_expiry(expiry_seconds=2)
def expensive_calculation(n):
    print(f"Calculating for {n}...")
    time.sleep(1)
    return n * n

print(expensive_calculation(5))
print(expensive_calculation(5))
time.sleep(3)
print(expensive_calculation(5))
```

### Explanation
Stores results with timestamps. Checks if cached result exists and hasn't expired before using it. If expired or not cached, recalculates and updates cache.
