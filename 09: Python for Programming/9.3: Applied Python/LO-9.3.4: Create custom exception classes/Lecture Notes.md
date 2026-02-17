# Lecture Notes: Create Custom Exceptions

## Create Custom Exceptions

Defining your own exception classes


---

<div align="center">

![Error handling and debugging](https://images.unsplash.com/photo-1564760055775-d63b17a55c44?w=800&q=80)

*Exception handling prevents your program from crashing on errors*

</div>

---

## Introduction

Custom exceptions implement **semantic error types** - exceptions that carry domain-specific meaning instead of generic "ValueError" or "RuntimeError". This enables **self-documenting error handling** where exception names explain what went wrong. Custom exceptions are the **type system for errors**!

### Why Custom Exceptions are Powerful

**Before custom exceptions** (generic): Errors lack context:
```python
# Generic - what went wrong?
if balance < amount:
    raise ValueError("insufficient funds")
# Catch: except ValueError - too broad!
```

**With custom exceptions** (semantic): Errors carry meaning:
```python
# Semantic - error TYPE tells the story!
if balance < amount:
    raise InsufficientFundsError(balance, amount)
# Catch: except InsufficientFundsError - specific!
```

**This is "type-safe error handling"** - different errors → different types → different handlers!

### Historical Context

**Custom exceptions** from **Modula-3** (1980s) which allowed user-defined exception types. Popularized by **Java** (1995) with checked exceptions forcing explicit handling. Python adopted unchecked exceptions (more flexible) but kept custom exception capability.

**Python's exception hierarchy**: All exceptions inherit from `BaseException`. User exceptions should inherit from `Exception` (not `BaseException` which includes system exits).

**Design pattern**: **Exception hierarchies** enable catching at different granularities - catch `DatabaseError` to handle all DB errors, or catch `ConnectionError` for just connection issues!

### Real-World Analogies

**Custom exceptions like medical diagnoses**:
- **Generic**: "Patient sick" (like ValueError)
- **Specific**: "Patient has influenza" (like InfluenzaException)
- **Treatment**: Specific diagnosis → specific treatment
- **Exception handling**: Specific exception → specific handler
**Doctors don't treat "sick" - they treat specific conditions!**

**Or like car dashboard warnings**:
```python
# Generic warning light - confusing!
raise WarningLight("Something wrong!")

# Specific warning - actionable!
raise LowOilPressureWarning(current_psi=15, min_psi=20)
# You know EXACTLY what's wrong!
```

**Or like building safety alarms**:
- **Fire alarm**: Evacuate (FireAlarmException)
- **Carbon monoxide**: Ventilate (COAlarmException)
- **Burglar alarm**: Call police (IntruderException)
**Different alarms → different responses!**

### Exception Hierarchies

**Build exception taxonomies** for flexible handling:
```python
class AppError(Exception):
    """Base for all app exceptions"""
    pass

class DatabaseError(AppError):
    """Base for DB exceptions"""
    pass

class ConnectionError(DatabaseError):
    """DB connection failed"""
    pass

class QueryError(DatabaseError):
    """SQL query failed"""
    pass

# Catch specific or broad:
try:
    db_operation()
except ConnectionError:
    reconnect()  # Specific handler
except DatabaseError:
    log_db_error()  # Catches ALL DB errors
except AppError:
    log_app_error()  # Catches ALL app errors
```

**This is inheritance for error types** - organize errors hierarchically!

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
