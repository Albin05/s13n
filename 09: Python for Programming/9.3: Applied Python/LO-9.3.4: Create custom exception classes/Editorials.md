## Editorials: Create Custom Exception Classes

---

### Q1 Solution: Basic Custom Exception

```python
class InvalidAgeError(ValueError):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid age: {age}. Age must be 0-150")

def set_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError(age)
    return age

for a in [25, -5, 200]:
    try:
        print(f"set_age({a}): {set_age(a)}")
    except InvalidAgeError as e:
        print(f"set_age({a}): {type(e).__name__}: {e}")
```

---

### Q2 Solution: Exception Hierarchy

```python
class BankError(Exception): pass

class InsufficientFundsError(BankError):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Need ${amount} but only ${balance} available")

class AccountLockedError(BankError):
    def __init__(self, account_id):
        self.account_id = account_id
        super().__init__(f"Account {account_id} is locked")

class InvalidAmountError(BankError):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(f"Invalid amount: {amount}")

# Catching base class catches all
errors = [
    InsufficientFundsError(100, 500),
    AccountLockedError("ACC-001"),
    InvalidAmountError(-50)
]
for err in errors:
    try:
        raise err
    except BankError as e:
        print(f"Caught BankError: {type(e).__name__}: {e}")
```

---

### Q3 Solution: Validation Error Collection

```python
class ValidationError(Exception):
    def __init__(self, errors):
        self.errors = errors
        super().__init__(f"{len(errors)} validation error(s)")

def validate_user(data):
    errors = []
    if 'name' not in data or not data['name'].strip():
        errors.append("name: required non-empty string")
    if 'age' not in data:
        errors.append("age: required")
    elif not isinstance(data['age'], int) or not 0 <= data['age'] <= 150:
        errors.append(f"age: must be int 0-150, got {data.get('age')}")
    if 'email' not in data:
        errors.append("email: required")
    elif '@' not in data['email']:
        errors.append(f"email: must contain @, got '{data['email']}'")
    if errors:
        raise ValidationError(errors)
    return True

try:
    validate_user({'name': '', 'age': -5, 'email': 'bad'})
except ValidationError as e:
    for err in e.errors:
        print(f"  - {err}")
```

---

### Q4 Solution: HTTP-style Exceptions

```python
class HTTPError(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        super().__init__(f"{status_code}: {message}")

class NotFoundError(HTTPError):
    def __init__(self, resource):
        self.resource = resource
        super().__init__(404, f"Not Found: {resource}")

class ForbiddenError(HTTPError):
    def __init__(self, action):
        super().__init__(403, f"Forbidden: {action}")

class ServerError(HTTPError):
    def __init__(self, detail):
        super().__init__(500, f"Internal Server Error: {detail}")

for err in [NotFoundError("/api/users/99"), ForbiddenError("delete"), ServerError("DB down")]:
    try:
        raise err
    except HTTPError as e:
        print(f"[{e.status_code}] {e}")
```

---

### Q5 Solution: Retry with Custom Exception

```python
import random

class RetryableError(Exception):
    pass

def retry(max_attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except RetryableError as e:
                    print(f"  Attempt {attempt} failed: {e}")
                    if attempt == max_attempts:
                        raise
            return wrapper
        return wrapper
    return decorator

@retry(max_attempts=3)
def unstable_operation():
    if random.random() < 0.7:
        raise RetryableError("Service unavailable")
    return "Success!"

try:
    result = unstable_operation()
    print(f"Result: {result}")
except RetryableError:
    print("All attempts failed")
```
