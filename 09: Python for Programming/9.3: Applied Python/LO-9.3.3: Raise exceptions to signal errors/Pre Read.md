## Pre-Read: Raise Exceptions to Signal Errors


---

## Introduction

The `raise` statement makes errors **loud and explicit** instead of silent and hidden! Before exceptions, functions returned error codes (None, -1, false) which callers often forgot to check. `raise` forces error handling - bugs crash immediately at their source instead of propagating downstream!

### Why Explicit Errors Matter

**Problem with error codes**: Easy to ignore, bugs propagate:
```python
# Returning None - silent failure!
def divide(a, b):
    if b == 0: return None
result = divide(10, 0)  # None
print(result + 5)  # Bug shows up HERE, not at source!
```

**Solution with raise**: Impossible to ignore:
```python
# Raising exception - loud failure!
def divide(a, b):
    if b == 0: raise ZeroDivisionError("b cannot be zero")
    return a / b
divide(10, 0)  # Crashes IMMEDIATELY!
```

**This is "fail-fast"** - detect errors at the source, don't let them spread!

### Real-World Analogy

**Raising exceptions like smoke alarm**:
- **Detect problem** (invalid input)
- **Sound alarm** (raise exception)
- **Cannot ignore** (program stops)
- **Handle emergency** (exception handler)
**You don't silently note smoke - you SOUND THE ALARM!**

---

### What Is raise?

`raise` lets you intentionally trigger an exception:

```python
if age < 0:
    raise ValueError("Age cannot be negative")
```

---

### Why Not Just Return None?

```python
# Problem: caller forgets to check
def divide(a, b):
    if b == 0: return None
result = divide(10, 0)
print(result + 1)  # TypeError: None + 1 — bug far from cause

# Better: exception at the source
def divide(a, b):
    if b == 0: raise ZeroDivisionError("b cannot be zero")
    return a / b
```

---

### Common Exception Types

| Exception | When to Use |
|-----------|-------------|
| `ValueError` | Right type, wrong value |
| `TypeError` | Wrong type |
| `RuntimeError` | Logic or state error |

---

### Try This

```python
def positive_only(n):
    if n <= 0:
        raise ValueError(f"Must be positive, got {n}")
    return n

positive_only(5)   # Works
positive_only(-3)  # What happens?
```
