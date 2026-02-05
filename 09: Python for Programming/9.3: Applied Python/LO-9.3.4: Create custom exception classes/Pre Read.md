## Pre-Read: Create Custom Exception Classes

**Duration:** 5 minutes

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
