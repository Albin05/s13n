## Editorials: Raise Exceptions to Signal Errors

---

### Q1 Solution: Input Validator

```python
def validate_password(password):
    if not isinstance(password, str):
        raise TypeError(f"Expected string, got {type(password).__name__}")
    if len(password) < 8:
        raise ValueError("Password too short")
    if not any(c.isdigit() for c in password):
        raise ValueError("Password must contain a digit")
    return True

tests = ["abc", 123, "hello123", "ab1"]
for t in tests:
    try:
        result = validate_password(t)
        print(f"  {t!r}: Valid")
    except (TypeError, ValueError) as e:
        print(f"  {t!r}: {e}")
```

---

### Q2 Solution: Age Range Checker

```python
def categorize_age(age):
    if not isinstance(age, (int, float)):
        raise TypeError(f"Age must be number, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"Age must be 0-150, got {age}")
    age = int(age)
    if age <= 12: return "child"
    if age <= 17: return "teen"
    if age <= 64: return "adult"
    return "senior"

for a in [5, 15, 30, 70, -1, 200, "old"]:
    try:
        print(f"  {a}: {categorize_age(a)}")
    except (TypeError, ValueError) as e:
        print(f"  {a}: Error — {e}")
```

---

### Q3 Solution: Bank Account

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError(f"Deposit must be positive, got {amount}")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError(f"Withdrawal must be positive, got {amount}")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds: balance={self.balance}, requested={amount}")
        self.balance -= amount

    def transfer(self, other, amount):
        if not isinstance(other, BankAccount):
            raise TypeError("Can only transfer to BankAccount")
        self.withdraw(amount)
        other.deposit(amount)

a = BankAccount("Alice", 1000)
b = BankAccount("Bob", 500)
a.transfer(b, 200)
print(f"Alice: {a.balance}, Bob: {b.balance}")  # 800, 700
```

---

### Q4 Solution: Data Parser

```python
def parse_record(record_string):
    if not record_string or not record_string.strip():
        raise ValueError("Empty record")
    parts = record_string.strip().split(',')
    if len(parts) != 3:
        raise ValueError(f"Expected 3 fields, got {len(parts)}")
    name = parts[0].strip()
    try:
        age = int(parts[1].strip())
    except ValueError:
        raise ValueError(f"Age must be integer, got '{parts[1].strip()}'")
    try:
        score = float(parts[2].strip())
    except ValueError:
        raise ValueError(f"Score must be number, got '{parts[2].strip()}'")
    if not 0 <= score <= 100:
        raise ValueError(f"Score must be 0-100, got {score}")
    return {'name': name, 'age': age, 'score': score}

tests = ["Alice,25,88.5", "", "Bob,abc,90", "Charlie,30,150", "Dan,20"]
for t in tests:
    try:
        print(f"  '{t}': {parse_record(t)}")
    except ValueError as e:
        print(f"  '{t}': Error — {e}")
```

---

### Q5 Solution: Configuration Validator

```python
def validate_config(config):
    required = ['host', 'port', 'database']
    for key in required:
        if key not in config:
            raise KeyError(f"Missing required key: '{key}'")
    if not isinstance(config['host'], str) or not config['host'].strip():
        raise ValueError("Host must be a non-empty string")
    if not isinstance(config['port'], int) or not 1 <= config['port'] <= 65535:
        raise ValueError(f"Port must be 1-65535, got {config['port']}")
    return True

configs = [
    {'host': 'localhost', 'port': 5432, 'database': 'mydb'},
    {'host': '', 'port': 5432, 'database': 'mydb'},
    {'port': 5432},
]
for c in configs:
    try:
        validate_config(c)
        print(f"  {c}: Valid")
    except (KeyError, ValueError) as e:
        print(f"  Error: {e}")
```
