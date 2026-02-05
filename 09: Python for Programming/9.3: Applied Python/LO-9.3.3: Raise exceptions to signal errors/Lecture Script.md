## Lecture Script: Raise Exceptions to Signal Errors

**Duration:** 12 minutes

---

### Hook (2 minutes)

A function receives a negative age and silently returns None:

```python
def set_age(age):
    if age < 0:
        return None  # Silent failure

user_age = set_age(-5)
print(f"Next year: {user_age + 1}")  # TypeError: None + 1!
```

The bug appears far from its cause. Instead:

```python
def set_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
```

Now the error appears exactly where the bad data enters. Debugging becomes easy.

---

### Section 1: Basic raise (2 minutes)

```python
raise ValueError("Something went wrong")
raise TypeError("Expected string, got int")
raise RuntimeError("Connection failed")
```

Choose the right exception type:
- `ValueError` — right type, wrong value
- `TypeError` — wrong type entirely
- `RuntimeError` — logic/state error

---

### Section 2: Validation Pattern (3 minutes)

```python
def create_user(name, age, email):
    if not isinstance(name, str):
        raise TypeError(f"Name must be string, got {type(name).__name__}")
    if not name.strip():
        raise ValueError("Name cannot be empty")
    if not isinstance(age, int) or age < 0:
        raise ValueError(f"Invalid age: {age}")
    if '@' not in email:
        raise ValueError(f"Invalid email: {email}")
    
    return {'name': name, 'age': age, 'email': email}
```

Validate early, fail fast, give clear messages.

---

### Section 3: Re-raising (2 minutes)

```python
def load_data(filename):
    try:
        with open(filename) as f:
            return parse(f.read())
    except FileNotFoundError:
        print(f"Warning: {filename} not found")
        raise  # Let caller handle it too
```

---

### Section 4: Good Error Messages (2 minutes)

```python
# BAD
raise ValueError("Invalid")

# GOOD
raise ValueError(f"Score must be 0-100, got {score}")

# GOOD
raise ValueError(
    f"Insufficient funds: balance=${balance:.2f}, "
    f"requested=${amount:.2f}"
)
```

Include: what went wrong, what was expected, what was received.

---

### Summary (1 minute)

1. `raise` signals errors explicitly and immediately
2. Use specific exception types
3. Include context in error messages
4. `raise` alone re-raises the current exception
5. Fail fast — raise as soon as bad data is detected
