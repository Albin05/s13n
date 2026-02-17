## Pre-Read: Create Custom Exception Classes


---

## Introduction

**Custom exceptions** give errors specific, meaningful names instead of generic "ValueError" or "RuntimeError". This makes error handling **self-documenting** - the exception name explains what went wrong! Custom exceptions are the **type system for errors**.

### Why Custom Exceptions Matter

**Problem with generic exceptions**: Lack context and specificity:
```python
# Generic - hard to understand!
if balance < amount:
    raise ValueError("bad transaction")
# What kind of bad? How to handle?
```

**Solution with custom exceptions**: Error type tells the story:
```python
# Specific - crystal clear!
if balance < amount:
    raise InsufficientFundsError(balance, amount)
# Immediately know what's wrong and how to fix!
```

**This is semantic error handling** - error types carry meaning!

### Real-World Analogy

**Custom exceptions like car dashboard lights**:
- **Generic**: "Check engine" (like ValueError - vague!)
- **Specific**: "Low oil pressure" (like LowOilException - clear!)
- **Action**: Specific light → specific action
**Specific error types enable specific responses!**

---

### Why Custom Exceptions?

Built-in exceptions like `ValueError` are generic. Custom exceptions describe your specific errors:

```python
# Generic — what went wrong?
raise ValueError("bad value")

# Specific — clear!
raise InsufficientFundsError(balance=100, amount=500)
```

---

### How to Create One

```python
class NegativeAgeError(ValueError):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Age cannot be negative: {age}")
```

1. Create a class inheriting from `Exception` (or a built-in exception)
2. Add custom attributes
3. Call `super().__init__()` with a message

---

### Using It

```python
def set_age(age):
    if age < 0:
        raise NegativeAgeError(age)

try:
    set_age(-5)
except NegativeAgeError as e:
    print(f"Bad age: {e.age}")
```
