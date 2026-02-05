## Pre-Read: Raise Exceptions to Signal Errors

**Duration:** 5 minutes

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
