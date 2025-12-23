# Pre-Read: Apply Decorators

## Decorators

Decorators are functions that modify the behavior of other functions:

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call
```

## The @ Syntax

```python
# These two are equivalent:

# Using @ syntax
@my_decorator
def greet():
    print("Hi!")

# Without @ syntax (manual decoration)
def greet():
    print("Hi!")
greet = my_decorator(greet)
```

## Decorators with Arguments

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello {name}!")

say_hello("Alice")
# Output:
# Hello Alice!
# Hello Alice!
# Hello Alice!
```
