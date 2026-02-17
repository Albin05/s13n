## Lecture Notes: Raise Exceptions to Signal Errors


---

## Introduction

The `raise` statement implements **explicit error signaling** - making errors loud and impossible to ignore! Before exceptions, functions returned error codes (NULL, -1, false) which callers often forgot to check, causing **silent failures** where bugs propagate far from their source. Raising exceptions enforces **fail-fast**: errors crash immediately at the source!

### Why Explicit Error Signaling is Essential

**Before raise** (error codes): Silent failures, bugs propagate:
```python
# BAD - error codes easy to ignore!
def divide(a, b):
    if b == 0:
        return None  # Silently fail
    return a / b

result = divide(10, 0)  # None
print(result + 5)  # TypeError LATER! Bug far from source!
```

**With raise** (explicit): Errors loud and immediate:
```python
# GOOD - errors impossible to ignore!
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("b cannot be zero")
    return a / b

result = divide(10, 0)  # CRASHES HERE!
# Bug detected at source, not downstream!
```

**This is "fail-fast"** - better to crash immediately than produce wrong results later!

### Historical Context

**Exception raising** from **PL/I** (IBM, 1964) which had SIGNAL/ON statements. Refined by **CLU** (Barbara Liskov, 1975) with `signal` keyword. Python's `raise` follows **Modula-3** (1980s) and **Java** (1995) syntax.

**Python 3 changed raise syntax**: Python 2 allowed `raise ValueError, "message"` (tuple-like). Python 3 requires `raise ValueError("message")` (function call syntax) - cleaner and more explicit!

**Design philosophy**: **Guido van Rossum** advocated "errors should never pass silently" - core Python principle! Raising exceptions embodies this philosophy.

### Real-World Analogies

**Raising exceptions like fire alarm**:
- **Detect smoke** (invalid input/state)
- **Pull alarm** (raise exception)
- **Loud siren** (cannot ignore)
- **Evacuation** (program stops)
**You don't whisper about fires - you SOUND THE ALARM!**

**Or like referee's whistle in sports**:
```python
def score_goal(player, ball_position):
    if ball_position == "offside":
        raise OffsideException("Goal invalid!")
    # Whistle blows - play stops immediately!
```

**Or like medical alert system**:
- **Monitor patient** (check function inputs)
- **Detect abnormality** (invalid state)
- **Trigger alarm** (raise exception)
- **Emergency response** (exception handler)
**Errors in medicine cannot be silent - same for code!**

### The Exception Taxonomy

**Python provides semantic exception types**:
```python
ValueError   # Right type, wrong value
TypeError    # Wrong type entirely
RuntimeError # Generic runtime problem
KeyError     # Missing dictionary key
IndexError   # List index out of bounds
# Each type signals SPECIFIC error category!
```

**Why specific types?** Allows catching errors at different granularity:
```python
try:
    operation()
except ValueError:
    # Handle value problems
except TypeError:
    # Handle type problems
except Exception:
    # Catch all others
```

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
