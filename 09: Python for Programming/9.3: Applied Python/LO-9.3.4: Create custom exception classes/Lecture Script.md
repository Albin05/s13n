## Lecture Script: Create Custom Exception Classes

**Duration:** 12 minutes

---

### Hook (2 minutes)

You're building a banking app. This happens:

```python
except ValueError as e:
    # Is this a bad amount? Wrong account? Invalid currency?
    print(e)  # "invalid value" — not helpful!
```

With custom exceptions:

```python
except InsufficientFundsError as e:
    print(f"Need ${e.required - e.balance} more")
except AccountLockedError as e:
    print(f"Account {e.account_id} is locked, contact support")
```

Custom exceptions carry **meaningful data** and enable **precise error handling**.

---

### Section 1: Creating Custom Exceptions (3 minutes)

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw ${amount}: only ${balance} available")

# Usage
raise InsufficientFundsError(100, 250)
# InsufficientFundsError: Cannot withdraw $250: only $100 available
```

Key: inherit from `Exception` (or a more specific built-in), call `super().__init__()`.

---

### Section 2: Exception Hierarchies (3 minutes)

```python
class AppError(Exception): pass
class DatabaseError(AppError): pass
class NetworkError(AppError): pass
class AuthError(AppError): pass

# Catch all app errors
try:
    operation()
except AppError as e:
    log(e)

# Or catch specific ones
try:
    query()
except DatabaseError:
    reconnect()
except NetworkError:
    retry()
```

---

### Section 3: Adding Data to Exceptions (2 minutes)

```python
class ValidationError(Exception):
    def __init__(self, field, value, message):
        self.field = field
        self.value = value
        super().__init__(f"{field}: {message} (got {value!r})")

raise ValidationError("age", -5, "must be positive")
# ValidationError: age: must be positive (got -5)
```

---

### Summary (1 minute)

1. Inherit from `Exception` or a specific built-in
2. Add attributes for context (`balance`, `field`, `status_code`)
3. Call `super().__init__()` with a readable message
4. Build hierarchies for related errors
5. Custom exceptions = better debugging + precise handling
