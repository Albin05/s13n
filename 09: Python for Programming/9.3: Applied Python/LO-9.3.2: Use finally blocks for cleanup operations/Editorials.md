## Editorials: Use finally Blocks for Cleanup

---

### Q1 Solution: Basic Finally Behavior

```python
# Block A — no error
try:
    print("A1")
    x = 10 / 2
except ZeroDivisionError:
    print("A2")
finally:
    print("A3")
# Output: A1, A3

# Block B — error caught
try:
    print("B1")
    x = 10 / 0
except ZeroDivisionError:
    print("B2")
finally:
    print("B3")
# Output: B1, B2, B3

# Block C — error NOT caught
try:
    try:
        print("C1")
        x = int("abc")
    except ZeroDivisionError:
        print("C2")
    finally:
        print("C3")
except ValueError:
    print("ValueError propagated")
# Output: C1, C3, ValueError propagated
```

**Explanation:** Block A: no error, so except is skipped but finally runs. Block B: error is caught AND finally runs. Block C: ValueError is not caught by ZeroDivisionError handler, but finally STILL runs before the error propagates.

---

### Q2 Solution: File Cleanup

```python
def read_first_line(filename):
    f = None
    try:
        f = open(filename)
        return f.readline().strip()
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None
    finally:
        if f is not None:
            f.close()
            print(f"File closed")

result = read_first_line("data.txt")
```

**Explanation:** We initialize `f = None` before try so finally can check if the file was opened. If `open()` fails with FileNotFoundError, `f` stays None and we skip `f.close()`.

---

### Q3 Solution: Database Simulation

```python
class FakeDB:
    def connect(self): print("Connected")
    def query(self, sql):
        if "DROP" in sql: raise PermissionError("Not allowed")
        return f"Results for: {sql}"
    def close(self): print("Connection closed")

def run_query(db, sql):
    db.connect()
    try:
        result = db.query(sql)
        return result
    except PermissionError as e:
        return f"Error: {e}"
    finally:
        db.close()

db = FakeDB()
print(run_query(db, "SELECT * FROM users"))
print()
print(run_query(db, "DROP TABLE users"))
```

---

### Q4 Solution: Transaction Handler

```python
def transfer_money(accounts, from_acc, to_acc, amount):
    print("Transaction started")
    try:
        if accounts[from_acc] < amount:
            raise ValueError(f"Insufficient funds in {from_acc}")
        accounts[from_acc] -= amount
        accounts[to_acc] += amount
        print(f"Transferred ${amount} from {from_acc} to {to_acc}")
    except ValueError as e:
        print(f"Failed: {e}")
    finally:
        print("Transaction ended")
        print(f"Balances: {accounts}")

accounts = {'Alice': 1000, 'Bob': 500}
transfer_money(accounts, 'Alice', 'Bob', 200)
print()
transfer_money(accounts, 'Bob', 'Alice', 2000)
```

---

### Q5 Solution: Resource Manager

```python
import time

class Timer:
    def __init__(self):
        self._start = None
        self._end = None
    def start(self):
        self._start = time.time()
    def stop(self):
        self._end = time.time()
    def elapsed(self):
        return self._end - self._start

timer = Timer()
try:
    timer.start()
    result = sum(range(1_000_000))
    print(f"Result: {result}")
finally:
    timer.stop()
    print(f"Elapsed: {timer.elapsed():.4f}s")
```

**Explanation:** `finally` ensures `timer.stop()` is called even if the computation raises an error. The Timer class stores start/end times and calculates the difference.
