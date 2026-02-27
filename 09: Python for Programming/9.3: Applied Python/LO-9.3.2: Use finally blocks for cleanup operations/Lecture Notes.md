# Lecture Notes: Use Finally Blocks

## Use Finally Blocks

Executing cleanup code regardless of exceptions


---

<div align="center">

![Python try-finally Cleanup Block](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/LO-9.3.2.png)

*The finally block guarantees cleanup runs regardless of which branch executes, like a guaranteed exit path in a flowchart*

</div>

---

## Introduction

The `finally` block implements **guaranteed cleanup** - code that MUST execute regardless of success, failure, or early returns. This solves the **resource leak problem**: files left open, connections not closed, locks not released. `finally` ensures cleanup happens **no matter what**!

### Why Guaranteed Cleanup is Critical

**Before finally** (manual cleanup): Easy to miss cleanup paths:
```python
# Fragile - many ways to skip cleanup!
file = open("data.txt")
result = process(file.read())  # Exception here?
return result  # Early return?
file.close()  # MIGHT NOT RUN!
```

**With finally** (guaranteed): Cleanup always happens:
```python
# Robust - cleanup ALWAYS executes!
file = open("data.txt")
try:
    result = process(file.read())
    return result  # Even if we return...
finally:
    file.close()  # ...this STILL runs!
```

**This is "deterministic cleanup"** - you know EXACTLY when resources are released!

### Historical Context

**Finally block** introduced in **CLU** (Barbara Liskov, MIT, 1975) as part of exception handling mechanism. Adopted by **C++** (destructors, 1985), **Java** (finally, 1995), and **Python** (1991).

**C++ used RAII** (Resource Acquisition Is Initialization) - cleanup in destructors. **Java/Python use finally** - explicit cleanup blocks. Different approaches, same goal: **prevent resource leaks**!

**Python 2.5 (2006)** introduced `with` statement (context managers) as cleaner alternative to try-finally for common cases. But `finally` still essential for complex cleanup logic!

### Real-World Analogies

**Finally block like closing a gate**:
- **Try**: Open gate, enter building (acquire resource)
- **Success**: Complete your task inside
- **Exception**: Emergency evacuation
- **Finally**: Close gate on your way out (ALWAYS)
**Gate must be closed whether you finished work or evacuated!**

**Or like washing hands after cooking**:
```python
try:
    prepare_ingredients()
    cook_meal()  # Might burn yourself!
except BurnException:
    apply_first_aid()
finally:
    wash_hands()  # ALWAYS wash, even if burned!
```

**Or like airplane landing**:
- **Try**: Fly the route
- **Exception**: Bad weather forces diversion
- **Finally**: Landing (one way or another)
**Plane MUST land - either at destination or alternate airport!**

### The Context Manager Alternative

**Modern Python prefers `with` statement** for common patterns:
```python
# Old way - explicit finally
file = open("data.txt")
try:
    data = file.read()
finally:
    file.close()

# New way - context manager
with open("data.txt") as file:
    data = file.read()  # Automatically closed!
```

**`with` statement uses `__enter__` and `__exit__` magic methods** - essentially automatic try-finally! But `finally` still needed for custom cleanup logic.

---
### Key Concepts

The `finally` block:
- Executes code regardless of whether an exception occurred
- Used for cleanup operations (closing files, releasing resources)
- Runs even if `try` block has `return` statement
- Ensures resources are properly released

### Core Principles

**Structure**: `try` → `except` → `else` → `finally` (all optional except `try`)

### Syntax and Usage

```python
try:
    # Code that might raise an exception
    file = open('data.txt', 'r')
    data = file.read()
except FileNotFoundError:
    # Handle specific exception
    print("File not found")
finally:
    # Always executes - cleanup code
    if 'file' in locals():
        file.close()
    print("Cleanup complete")
```

### Practical Examples

#### Example 1: File Handling with Finally

```python
def read_file(filename):
    """Read file with proper cleanup"""
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        print(f"Read {len(content)} characters")
        return content

    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None

    except PermissionError:
        print(f"Error: No permission to read {filename}")
        return None

    finally:
        if file:
            file.close()
            print(f"File {filename} closed")

# Usage
content = read_file('data.txt')
# Output (if file exists):
# Read 1234 characters
# File data.txt closed

# Output (if file doesn't exist):
# Error: data.txt not found
# File data.txt closed
```

#### Example 2: Database Connection

```python
class DatabaseConnection:
    """Simulated database connection"""

    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def connect(self):
        print(f"Connecting to {self.db_name}...")
        self.connected = True

    def execute(self, query):
        if not self.connected:
            raise Exception("Not connected to database")
        print(f"Executing: {query}")
        return f"Result for {query}"

    def close(self):
        if self.connected:
            print(f"Closing connection to {self.db_name}")
            self.connected = False

def query_database(db_name, query):
    """Execute database query with proper cleanup"""
    db = DatabaseConnection(db_name)

    try:
        db.connect()
        result = db.execute(query)
        return result

    except Exception as e:
        print(f"Database error: {e}")
        return None

    finally:
        db.close()
        print("Database cleanup complete")

# Usage
result = query_database("users_db", "SELECT * FROM users")
print(f"Result: {result}")

# Output:
# Connecting to users_db...
# Executing: SELECT * FROM users
# Closing connection to users_db
# Database cleanup complete
# Result: Result for SELECT * FROM users
```

#### Example 3: Try-Except-Else-Finally

```python
def divide_numbers(a, b):
    """Demonstrate all exception handling blocks"""
    print(f"Attempting to divide {a} by {b}")

    try:
        result = a / b
        print("Division successful")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None

    except TypeError:
        print("Error: Invalid types for division")
        return None

    else:
        # Runs only if no exception occurred
        print(f"Result calculated: {result}")
        return result

    finally:
        # Always runs
        print("Division operation complete\n")

# Test cases
divide_numbers(10, 2)
# Attempting to divide 10 by 2
# Division successful
# Result calculated: 5.0
# Division operation complete

divide_numbers(10, 0)
# Attempting to divide 10 by 0
# Error: Cannot divide by zero
# Division operation complete

divide_numbers("10", 2)
# Attempting to divide 10 by 2
# Error: Invalid types for division
# Division operation complete
```

#### Example 4: Resource Manager

```python
class ResourceManager:
    """Manage resources with proper cleanup"""

    def __init__(self, resource_name):
        self.resource_name = resource_name
        self.allocated = False

    def allocate(self):
        """Allocate resource"""
        print(f"Allocating {self.resource_name}")
        self.allocated = True

    def use(self):
        """Use the resource"""
        if not self.allocated:
            raise Exception("Resource not allocated")
        print(f"Using {self.resource_name}")

    def release(self):
        """Release resource"""
        if self.allocated:
            print(f"Releasing {self.resource_name}")
            self.allocated = False

def perform_task(task_name, should_fail=False):
    """Perform task with resource management"""
    resource = ResourceManager(f"Resource-{task_name}")

    try:
        resource.allocate()
        resource.use()

        if should_fail:
            raise ValueError("Task failed!")

        print(f"Task {task_name} completed successfully")
        return True

    except ValueError as e:
        print(f"Task {task_name} error: {e}")
        return False

    finally:
        resource.release()
        print(f"Task {task_name} cleanup done\n")

# Usage
perform_task("A", should_fail=False)
# Allocating Resource-A
# Using Resource-A
# Task A completed successfully
# Releasing Resource-A
# Task A cleanup done

perform_task("B", should_fail=True)
# Allocating Resource-B
# Using Resource-B
# Task B error: Task failed!
# Releasing Resource-B
# Task B cleanup done
```

#### Example 5: Transaction Management

```python
class Transaction:
    """Simulated transaction with rollback"""

    def __init__(self, transaction_id):
        self.transaction_id = transaction_id
        self.started = False
        self.committed = False

    def begin(self):
        print(f"Transaction {self.transaction_id}: BEGIN")
        self.started = True

    def commit(self):
        if self.started and not self.committed:
            print(f"Transaction {self.transaction_id}: COMMIT")
            self.committed = True

    def rollback(self):
        if self.started and not self.committed:
            print(f"Transaction {self.transaction_id}: ROLLBACK")

def process_payment(amount, should_fail=False):
    """Process payment with transaction management"""
    transaction = Transaction(f"PAY-{amount}")

    try:
        transaction.begin()

        # Validation
        if amount <= 0:
            raise ValueError("Amount must be positive")

        # Processing
        print(f"Processing payment: ${amount}")

        if should_fail:
            raise Exception("Payment gateway error")

        print(f"Payment ${amount} successful")
        transaction.commit()
        return True

    except ValueError as e:
        print(f"Validation error: {e}")
        return False

    except Exception as e:
        print(f"Payment error: {e}")
        return False

    finally:
        # Rollback if not committed
        if transaction.started and not transaction.committed:
            transaction.rollback()
        print(f"Transaction cleanup complete\n")

# Usage
process_payment(100, should_fail=False)
# Transaction PAY-100: BEGIN
# Processing payment: $100
# Payment $100 successful
# Transaction PAY-100: COMMIT
# Transaction cleanup complete

process_payment(200, should_fail=True)
# Transaction PAY-200: BEGIN
# Processing payment: $200
# Payment error: Payment gateway error
# Transaction PAY-200: ROLLBACK
# Transaction cleanup complete

process_payment(-50, should_fail=False)
# Transaction PAY--50: BEGIN
# Validation error: Amount must be positive
# Transaction PAY--50: ROLLBACK
# Transaction cleanup complete
```

### Finally vs Context Managers

```python
# Using finally
file = None
try:
    file = open('data.txt', 'r')
    content = file.read()
finally:
    if file:
        file.close()

# Better: Using context manager (with statement)
with open('data.txt', 'r') as file:
    content = file.read()
# File automatically closed
```

### Best Practices

1. **Use for cleanup**: Finally is for releasing resources
2. **Keep it simple**: Don't put complex logic in finally
3. **Prefer context managers**: Use `with` when available
4. **Don't catch in finally**: Finally is not for exception handling
5. **Always release resources**: Even if exception occurs

### Common Mistakes

1. **Returning in finally**: Overwrites return from try/except
   ```python
   # Bad - finally return overwrites try return
   def bad_example():
       try:
           return "try"
       finally:
           return "finally"  # This is what gets returned!
   ```

2. **Raising new exceptions**: Can hide original exception
3. **Complex logic**: Keep finally block simple and focused
4. **Not checking if resource exists**: Check before cleanup

### When to Use

Use `finally` when:
- You need to release resources (files, connections, locks)
- Cleanup must happen regardless of success/failure
- You can't use context managers
- You need to log completion status
- Rolling back transactions

### Key Takeaways

1. `finally` block always executes
2. Runs even if exception occurs or return is called
3. Used for cleanup operations
4. Can't prevent exception propagation
5. Prefer `with` statement when possible
6. Keep finally blocks simple and focused on cleanup
7. Essential for proper resource management
