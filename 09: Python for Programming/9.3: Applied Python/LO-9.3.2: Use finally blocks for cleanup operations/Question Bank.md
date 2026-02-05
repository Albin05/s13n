## Question Bank: Use finally Blocks for Cleanup Operations

---

### Q1: Basic Finally Behavior (3 minutes, Low Difficulty)

What is the output of each block? Predict, then verify:

```python
# Block A
try:
    print("A1")
    x = 10 / 2
except ZeroDivisionError:
    print("A2")
finally:
    print("A3")

# Block B
try:
    print("B1")
    x = 10 / 0
except ZeroDivisionError:
    print("B2")
finally:
    print("B3")

# Block C
try:
    print("C1")
    x = int("abc")
except ZeroDivisionError:
    print("C2")
finally:
    print("C3")
```

**Expected Output:**
```
A1, A3 (no error)
B1, B2, B3 (error caught)
C1, C3 then ValueError crashes (error NOT caught, but finally still runs)
```

**Key Concepts:** finally always runs

---

### Q2: File Cleanup (3 minutes, Low Difficulty)

Write a function `read_first_line(filename)` that:
- Opens a file, reads the first line
- Uses `finally` to ensure the file is always closed
- Handles `FileNotFoundError`
- Returns the first line or `None`

**Key Concepts:** finally for resource cleanup

---

### Q3: Database Simulation (5 minutes, Medium Difficulty)

Simulate a database connection with cleanup:

```python
class FakeDB:
    def connect(self): print("Connected")
    def query(self, sql):
        if "DROP" in sql: raise PermissionError("Not allowed")
        return f"Results for: {sql}"
    def close(self): print("Connection closed")
```

Write a function `run_query(db, sql)` that:
- Connects to the database
- Runs the query
- Always closes the connection (even on error)
- Returns the result or an error message

Test with `"SELECT * FROM users"` and `"DROP TABLE users"`.

**Key Concepts:** finally for connection cleanup

---

### Q4: Transaction Handler (5 minutes, Medium Difficulty)

Write a function `transfer_money(accounts, from_acc, to_acc, amount)` that:
- Logs "Transaction started"
- Deducts from source, adds to destination
- Raises `ValueError` if insufficient funds
- Uses finally to always log "Transaction ended"
- On error, rolls back the deduction

```python
accounts = {'Alice': 1000, 'Bob': 500}
```

Test with valid transfer (Alice→Bob $200) and invalid (Bob→Alice $1000).

**Key Concepts:** finally for transaction logging, rollback pattern

---

### Q5: Resource Manager (5 minutes, Medium Difficulty)

Write a class `Timer` that tracks execution time:

```python
import time

class Timer:
    def start(self): ...
    def stop(self): ...
    def elapsed(self): ...
```

Use it with try-finally to ensure `stop()` is always called:

```python
timer = Timer()
try:
    timer.start()
    # some operation
    result = sum(range(1000000))
finally:
    timer.stop()
    print(f"Elapsed: {timer.elapsed():.4f}s")
```

**Key Concepts:** finally for timing/cleanup, class usage
