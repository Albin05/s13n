# Lecture Notes: Create Custom Exceptions

## Create Custom Exceptions

Defining your own exception classes


---

<div align="center">

![Error handling and debugging](https://images.unsplash.com/photo-1564760055775-d63b17a55c44?w=800&q=80)

*Exception handling prevents your program from crashing on errors*

</div>

---
### Key Concepts

**Core principle**: class CustomError(Exception): pass

### Syntax and Usage

```python
# Basic example will be shown in practical examples below
```

### Practical Examples

#### Example 1: Basic Custom Exception

```python
class ValidationError(Exception):
    pass

def validate_email(email):
    if '@' not in email:
        raise ValidationError(f"Invalid email: {email}")
    return email

try:
    validate_email("invalid_email")
except ValidationError as e:
    print(f"Error: {e}")
```

#### Example 2: Exception with Additional Info

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: ${balance} < ${amount}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(100, 150)
except InsufficientFundsError as e:
    print(f"Cannot withdraw ${e.amount}, only ${e.balance} available")
```

#### Example 3: Exception Hierarchy

```python
class DatabaseError(Exception):
    pass

class ConnectionError(DatabaseError):
    pass

class QueryError(DatabaseError):
    pass

try:
    raise QueryError("Invalid SQL query")
except DatabaseError as e:
    print(f"Database problem: {e}")
```

### Best Practices

1. Write clear, readable code
2. Handle errors appropriately
3. Follow Python conventions
4. Document your code
5. Test thoroughly

### Common Mistakes

1. Not handling edge cases
2. Overcomplicating simple tasks
3. Not following naming conventions

### Key Takeaways

1. Understanding the core concept is essential
2. Practice with real examples
3. Apply best practices
4. Avoid common pitfalls
5. Write clean, maintainable code
