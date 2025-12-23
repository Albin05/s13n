# Lecture Notes: Raise Exceptions

## Raise Exceptions

Manually triggering exceptions in your code


---

<div align="center">

![Error handling and debugging](https://images.unsplash.com/photo-1564760055775-d63b17a55c44?w=800&q=80)

*Exception handling prevents your program from crashing on errors*

</div>

---
### Key Concepts

**Core principle**: raise ExceptionType('message')

### Syntax and Usage

```python
# Basic example will be shown in practical examples below
```

### Practical Examples

#### Example 1: Basic Exception Raising

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")
# Output: Error: Cannot divide by zero
```

#### Example 2: Input Validation

```python
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age

try:
    age = set_age(-5)
except ValueError as e:
    print(f"Invalid age: {e}")
```

#### Example 3: Re-raising Exceptions

```python
def process_data(data):
    try:
        result = int(data)
        return result
    except ValueError:
        print("Logging error...")
        raise  # Re-raise the same exception
```

### Best Practices

1. Write clear, readable code
2. Handle errors appropriately
3. Follow Python conventions
4. Document your code
5. Test thoroughly

### Common Mistakes

1. Not handling edge cases
2. Overcomplicating simple tasks
3. Not following naming conventions

### Key Takeaways

1. Understanding the core concept is essential
2. Practice with real examples
3. Apply best practices
4. Avoid common pitfalls
5. Write clean, maintainable code
