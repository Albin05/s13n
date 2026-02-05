## Lecture Script: Handle Multiple Exception Types

**Duration:** 12 minutes

---

### Hook (2 minutes)

Real code fails in many ways. A single function might face:

```python
def get_user_score(data, user_id):
    user = data[user_id]          # KeyError if user missing
    score = float(user['score'])  # ValueError if not a number
    return 100 / score            # ZeroDivisionError if score is 0
```

Three different exceptions, three different fixes. You need to handle each appropriately.

---

### Section 1: Multiple except Blocks (3 minutes)

```python
try:
    user = data[user_id]
    score = float(user['score'])
    result = 100 / score
except KeyError:
    print(f"User {user_id} not found")
except ValueError:
    print("Score is not a number")
except ZeroDivisionError:
    print("Score is zero")
```

**Order matters:** specific first, general last.

---

### Section 2: Grouping Exceptions (2 minutes)

```python
# Same handler for related errors
try:
    process(data)
except (ValueError, TypeError):
    print("Bad input data")
except (FileNotFoundError, PermissionError):
    print("File access problem")
```

---

### Section 3: The Complete Structure (3 minutes)

```python
try:
    result = compute(x, y)
except ValueError:
    result = default_value
except ZeroDivisionError:
    result = float('inf')
else:
    print(f"Success: {result}")
finally:
    log("computation attempted")
```

- `try` — risky code
- `except` — error handlers (checked in order)
- `else` — success path (no error)
- `finally` — always runs (cleanup)

---

### Section 4: Catching the Base Class (1 minute)

```python
try:
    operation()
except ValueError:
    handle_specific()
except Exception as e:
    print(f"Unexpected: {type(e).__name__}: {e}")
```

`Exception` is the catch-all — use it last, as a safety net.

---

### Summary (1 minute)

1. Multiple `except` blocks for different error types
2. Group with `(ExcA, ExcB)` for shared handlers
3. Order: specific → general
4. `else` for success, `finally` for cleanup
5. `Exception` as last resort catch-all
