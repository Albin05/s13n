## Lecture Notes: Raise Exceptions to Signal Errors

**Duration:** 10 minutes

---

### The `raise` Statement

Use `raise` to intentionally trigger an exception:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age

set_age(-5)  # ValueError: Age cannot be negative
```

---

### Why Raise Exceptions?

Raising exceptions lets you **signal errors early** instead of letting bad data propagate:

```python
# BAD: silent failure
def divide(a, b):
    if b == 0:
        return None  # Caller might forget to check!

# GOOD: loud failure
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
```

---

### Raising Different Exception Types

```python
# ValueError — bad value
def set_score(score):
    if not 0 <= score <= 100:
        raise ValueError(f"Score must be 0-100, got {score}")

# TypeError — wrong type
def greet(name):
    if not isinstance(name, str):
        raise TypeError(f"Expected string, got {type(name).__name__}")
    return f"Hello, {name}!"

# RuntimeError — general runtime issue
def connect():
    if not network_available:
        raise RuntimeError("No network connection")
```

---

### Re-raising Exceptions

Catch an exception, do something, then re-raise it:

```python
def process_data(data):
    try:
        result = transform(data)
    except ValueError as e:
        print(f"Logging error: {e}")
        raise  # Re-raises the same exception
```

`raise` without arguments re-raises the current exception.

---

### Raising with Custom Messages

```python
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError(f"Amount must be positive, got {amount}")
    if amount > balance:
        raise ValueError(f"Insufficient funds: balance={balance}, requested={amount}")
    return balance - amount
```

Good error messages include:
- What went wrong
- What was expected
- What was received

---

### Practical Examples

**1. Input Validation:**
```python
def create_user(name, email):
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")
    if '@' not in email:
        raise ValueError(f"Invalid email: {email}")
    return {'name': name.strip(), 'email': email.lower()}
```

**2. Precondition Checking:**
```python
def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot average empty list")
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError("All elements must be numbers")
    return sum(numbers) / len(numbers)
```

**3. State Validation:**
```python
class Oven:
    def __init__(self):
        self.temperature = 0
        self.is_on = False
    
    def bake(self, item):
        if not self.is_on:
            raise RuntimeError("Oven is not turned on")
        if self.temperature < 100:
            raise RuntimeError(f"Temperature too low: {self.temperature}°C")
        return f"Baking {item} at {self.temperature}°C"
```

---

### Key Takeaways

1. `raise ExceptionType("message")` triggers an exception
2. Use specific exception types (`ValueError`, `TypeError`, etc.)
3. Include helpful error messages with context
4. `raise` alone re-raises the current exception
5. Raise exceptions early to catch bugs before they propagate
6. Prefer raising exceptions over returning error codes or None
