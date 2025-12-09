# Editorials: Use Context Managers

## Problem 1: Basic File Context Manager

```python
def read_file_safe(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"

# Test
content = read_file_safe("example.txt")
print(content)
```

### Explanation
Uses with statement to ensure file is closed. Try-except handles missing files gracefully.

---

## Problem 2: Write List to File

```python
def write_list_to_file(filename, data_list):
    with open(filename, "w") as file:
        for item in data_list:
            file.write(f"{item}\n")

# Test
items = ["apple", "banana", "cherry"]
write_list_to_file("fruits.txt", items)
```

### Explanation
Opens file in write mode with context manager. Writes each item followed by newline.

---

## Problem 3: Timer Context Manager

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()
        elapsed = self.end - self.start
        print(f"Elapsed time: {elapsed:.4f} seconds")
        return False

# Test
with Timer():
    time.sleep(1)
```

### Explanation
`__enter__` records start time. `__exit__` calculates and prints elapsed time.

---

## Problem 4: List State Manager

```python
class ListStateManager:
    def __init__(self, managed_list):
        self.managed_list = managed_list
        self.original_state = None

    def __enter__(self):
        # Save current state
        self.original_state = self.managed_list.copy()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Restore original state
        self.managed_list.clear()
        self.managed_list.extend(self.original_state)
        return False

# Test
my_list = [1, 2, 3]
print(f"Before: {my_list}")

with ListStateManager(my_list):
    my_list.append(4)
    my_list.append(5)
    print(f"Inside: {my_list}")

print(f"After: {my_list}")
```

### Explanation
Saves list copy on enter. Restores by clearing and extending on exit.

---

## Problem 5: Transaction Context Manager

```python
from contextlib import contextmanager

@contextmanager
def Transaction():
    class TransactionObject:
        def __init__(self):
            self.operations = []

        def add_operation(self, operation):
            print(f"Operation: {operation}")
            self.operations.append(operation)

    trans = TransactionObject()
    print("Transaction started")

    try:
        yield trans
        print("Transaction committed")
    except Exception as e:
        print(f"Transaction rolled back due to: {e}")
        raise

# Test successful
with Transaction() as trans:
    trans.add_operation("INSERT user1")
    trans.add_operation("UPDATE balance")

# Test failed
try:
    with Transaction() as trans:
        trans.add_operation("INSERT user2")
        raise ValueError("Error occurred")
except ValueError:
    pass
```

### Explanation
Uses @contextmanager decorator. Yields transaction object. Commits on success, rolls back on exception.
