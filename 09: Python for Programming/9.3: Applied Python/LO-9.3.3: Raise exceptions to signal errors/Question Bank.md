## Question Bank: Raise Exceptions to Signal Errors

---

### Q1: Input Validator (3 minutes, Low Difficulty)

Write a function `validate_password(password)` that raises exceptions:
- `TypeError` if password is not a string
- `ValueError("Password too short")` if less than 8 characters
- `ValueError("Password must contain a digit")` if no digit
- Returns `True` if valid

Test with: `"abc"`, `123`, `"hello123"`, `"ab1"`

**Key Concepts:** raise with specific messages

---

### Q2: Age Range Checker (3 minutes, Low Difficulty)

Write a function `categorize_age(age)` that:
- Raises `TypeError` if age is not int/float
- Raises `ValueError` if age < 0 or age > 150
- Returns category: "child" (0-12), "teen" (13-17), "adult" (18-64), "senior" (65+)

**Key Concepts:** Multiple validation checks with raise

---

### Q3: Bank Account (5 minutes, Medium Difficulty)

Write a `BankAccount` class with:
- `deposit(amount)` — raises `ValueError` if amount <= 0
- `withdraw(amount)` — raises `ValueError` if amount <= 0, raises `ValueError("Insufficient funds")` if amount > balance
- `transfer(other_account, amount)` — raises `TypeError` if other isn't BankAccount

**Key Concepts:** raise in methods, type checking

---

### Q4: Data Parser (5 minutes, Medium Difficulty)

Write `parse_record(record_string)` that parses `"name,age,score"` format:
- Raises `ValueError("Empty record")` for empty strings
- Raises `ValueError("Expected 3 fields")` if not exactly 3 fields
- Raises `ValueError("Age must be integer")` if age can't convert
- Raises `ValueError("Score must be 0-100")` if score out of range
- Returns `{'name': str, 'age': int, 'score': float}`

Test with various valid and invalid inputs.

**Key Concepts:** Sequential validation with specific errors

---

### Q5: Configuration Validator (5 minutes, Medium Difficulty)

Write `validate_config(config)` that checks a dict:
- Required keys: `'host'`, `'port'`, `'database'`
- Port must be int between 1-65535
- Host must be non-empty string
- Raises `KeyError` for missing keys
- Raises `ValueError` for invalid values

```python
config1 = {'host': 'localhost', 'port': 5432, 'database': 'mydb'}  # Valid
config2 = {'host': '', 'port': 5432, 'database': 'mydb'}  # Invalid host
config3 = {'port': 5432}  # Missing keys
```

**Key Concepts:** Dictionary validation, multiple error types
