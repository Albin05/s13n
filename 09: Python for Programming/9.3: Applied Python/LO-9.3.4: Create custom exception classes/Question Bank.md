## Question Bank: Create Custom Exception Classes

---

### Q1: Basic Custom Exception (3 minutes, Low Difficulty)

Create a custom exception `InvalidAgeError` that inherits from `ValueError`. It should accept age and message. Write a function `set_age(age)` that raises it for invalid ages (< 0 or > 150).

**Expected Output:**
```
set_age(25): 25
set_age(-5): InvalidAgeError: Invalid age: -5. Age must be 0-150
set_age(200): InvalidAgeError: Invalid age: 200. Age must be 0-150
```

**Key Concepts:** Custom exception class, inheritance from ValueError

---

### Q2: Exception Hierarchy (3 minutes, Low Difficulty)

Create an exception hierarchy for a banking app:
- `BankError` (base, inherits Exception)
  - `InsufficientFundsError` (includes balance and amount)
  - `AccountLockedError` (includes account_id)
  - `InvalidAmountError` (includes amount)

Demonstrate catching `BankError` catches all three subtypes.

**Key Concepts:** Exception hierarchies, polymorphic catching

---

### Q3: Validation Error Collection (5 minutes, Medium Difficulty)

Create a `ValidationError` that can hold multiple errors:

```python
class ValidationError(Exception):
    def __init__(self, errors):
        self.errors = errors
        super().__init__(f"{len(errors)} validation error(s)")
```

Write `validate_user(data)` that collects ALL errors before raising:
- name: required, non-empty string
- age: required, int, 0-150
- email: required, must contain '@'

Instead of stopping at first error, collect all and raise once.

**Key Concepts:** Custom exception with data, collecting errors

---

### Q4: HTTP-style Exceptions (5 minutes, Medium Difficulty)

Create exceptions modeling HTTP errors:
- `HTTPError(status_code, message)`
- `NotFoundError(resource)` — 404
- `ForbiddenError(action)` — 403
- `ServerError(detail)` — 500

Each should have `status_code` and human-readable `__str__`. Use them in a simulated API.

**Key Concepts:** Custom attributes, __str__ override

---

### Q5: Retry with Custom Exception (5 minutes, Medium Difficulty)

Create `RetryableError` with a `max_retries` attribute. Write a decorator `retry(max_attempts)` that catches `RetryableError` and retries the function.

```python
@retry(max_attempts=3)
def unstable_operation():
    import random
    if random.random() < 0.7:
        raise RetryableError("Service unavailable")
    return "Success!"
```

**Key Concepts:** Custom exceptions with metadata, retry pattern
