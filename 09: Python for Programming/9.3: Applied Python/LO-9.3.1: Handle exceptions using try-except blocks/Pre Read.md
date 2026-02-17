## Pre-Read: Handle Exceptions Using try-except Blocks


---

## Introduction

**Exception handling** is how programs recover from errors gracefully instead of crashing. Before exceptions, programmers used **error codes** (return values like -1, NULL, false) which were easy to ignore. Exceptions are **impossible to ignore** - they force you to handle errors explicitly!

### Why Exceptions Matter

**Problem with error codes**: Easy to forget checking:
```python
# Old way (error codes) - dangerous!
result = divide(10, 0)  # Returns None on error
print(result + 5)  # TypeError far from source!
```

**Solution with exceptions**: Errors crash immediately:
```python
# Modern way (exceptions) - safe!
result = 10 / 0  # ZeroDivisionError RIGHT HERE
# Cannot proceed with bad data!
```

**This is "fail-fast"** - catch errors at the source, not downstream!

### Python's EAFP Philosophy

**EAFP**: "Easier to Ask Forgiveness than Permission"
```python
try:
    value = dict[key]  # Just try it!
except KeyError:
    value = default  # Handle failure
```

**LBYL**: "Look Before You Leap" (other languages)
```python
if key in dict:  # Check first
    value = dict[key]  # Then act
else:
    value = default
```

**Python prefers EAFP** - try first, handle errors later. More concise and often faster!

### Real-World Analogy

**Exception handling like safety net**:
- **Try**: Walk tightrope (risky code)
- **Except**: Safety net catches you (error handler)
- **No net**: Fall to ground (program crash)
**Exceptions are your safety net!**

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
