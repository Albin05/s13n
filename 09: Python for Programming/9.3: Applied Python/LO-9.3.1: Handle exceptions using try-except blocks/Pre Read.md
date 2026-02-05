## Pre-Read: Handle Exceptions Using try-except Blocks

**Duration:** 5 minutes

---

### The Problem

Programs crash when something unexpected happens:

```python
number = int("hello")  # CRASH! ValueError
result = 10 / 0        # CRASH! ZeroDivisionError
```

---

### The Solution: try-except

```python
try:
    number = int("hello")
except ValueError:
    print("That's not a number!")
# Program continues normally
```

**How it works:**
1. Python tries the code in `try`
2. If an error occurs, it jumps to `except`
3. If no error, `except` is skipped
4. Either way, the program continues after

---

### Common Errors You'll Handle

| Error | Cause |
|-------|-------|
| `ValueError` | Wrong value (e.g., `int("abc")`) |
| `ZeroDivisionError` | Dividing by zero |
| `IndexError` | List index out of range |
| `KeyError` | Dict key not found |
| `FileNotFoundError` | File doesn't exist |
| `TypeError` | Wrong type for operation |

---

### Try This

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Program still running!")
```

What prints? Both lines — the error is caught, and execution continues.
