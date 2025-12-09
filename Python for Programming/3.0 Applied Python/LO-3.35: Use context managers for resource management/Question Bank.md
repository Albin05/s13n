# Question Bank: Use Context Managers

## Problem 1 (Easy)

**Title:** Basic File Context Manager

**Problem Statement:**
Write a function `read_file_safe(filename)` that uses a context manager to read a file and return its contents. The function should handle the file not existing gracefully.

**Input Format:**
A filename string.

**Output Format:**
File contents as a string, or an error message if file doesn't exist.

**Sample Usage:**
```python
content = read_file_safe("example.txt")
print(content)
```

**Constraints:**
- Use with statement
- Handle FileNotFoundError
- Return error message if file not found

---

## Problem 2 (Easy)

**Title:** Write List to File

**Problem Statement:**
Write a function `write_list_to_file(filename, data_list)` that writes each item in a list to a new line in a file using a context manager.

**Input Format:**
Filename and a list of strings.

**Output Format:**
Write to file, no return value.

**Sample Usage:**
```python
items = ["apple", "banana", "cherry"]
write_list_to_file("fruits.txt", items)
```

**Sample Output in File:**
```
apple
banana
cherry
```

**Constraints:**
- Use with statement
- Write each item on new line

---

## Problem 3 (Medium)

**Title:** Timer Context Manager

**Problem Statement:**
Create a context manager class called `Timer` that measures and prints how long code takes to execute. It should print the elapsed time when exiting the with block.

**Input Format:**
None (used as context manager).

**Output Format:**
Print elapsed time in seconds when exiting.

**Sample Usage:**
```python
import time

with Timer():
    time.sleep(1)
    # Do some work
```

**Sample Output:**
```
Elapsed time: 1.0023 seconds
```

**Constraints:**
- Implement `__enter__()` and `__exit__()`
- Use time.time()
- Print time with 4 decimal places

---

## Problem 4 (Medium)

**Title:** List State Manager

**Problem Statement:**
Create a context manager class called `ListStateManager` that takes a list and saves its state. When entering, it stores the current state. When exiting, it restores the list to that state, effectively undoing any changes made within the with block.

**Input Format:**
A list to manage.

**Output Format:**
List restored to original state on exit.

**Sample Usage:**
```python
my_list = [1, 2, 3]
print(f"Before: {my_list}")

with ListStateManager(my_list):
    my_list.append(4)
    my_list.append(5)
    print(f"Inside: {my_list}")

print(f"After: {my_list}")
```

**Sample Output:**
```
Before: [1, 2, 3]
Inside: [1, 2, 3, 4, 5]
After: [1, 2, 3]
```

**Constraints:**
- Implement `__enter__()` and `__exit__()`
- Save and restore list state
- Changes made inside with block are undone

---

## Problem 5 (Hard)

**Title:** Transaction Context Manager

**Problem Statement:**
Create a context manager called `Transaction` that simulates a database transaction. It should:
- Start a transaction on enter
- If no errors occur, commit the transaction on exit
- If an error occurs, rollback the transaction
- Track all operations performed

Implement using the contextmanager decorator from contextlib.

**Input Format:**
None (context manager).

**Output Format:**
Print transaction status and operations.

**Sample Usage:**
```python
from contextlib import contextmanager

# Successful transaction
with Transaction() as trans:
    trans.add_operation("INSERT user1")
    trans.add_operation("UPDATE balance")
```

**Sample Output:**
```
Transaction started
Operation: INSERT user1
Operation: UPDATE balance
Transaction committed
```

**Failed Transaction:**
```python
try:
    with Transaction() as trans:
        trans.add_operation("INSERT user2")
        raise ValueError("Error occurred")
        trans.add_operation("This won't execute")
except ValueError:
    pass
```

**Output:**
```
Transaction started
Operation: INSERT user2
Transaction rolled back due to: Error occurred
```

**Constraints:**
- Use @contextmanager decorator
- Track operations in a list
- Print appropriate messages
- Handle exceptions and rollback
