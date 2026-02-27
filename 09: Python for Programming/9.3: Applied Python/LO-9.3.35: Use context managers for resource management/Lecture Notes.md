# Lecture Notes: Use Context Managers

## Context Managers

Context managers provide a way to allocate and release resources precisely when needed. They use the `with` statement to ensure cleanup code is always executed.


---

<div align="center">

![Python Context Manager with Statement](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/LO-9.3.35.png)

*Context managers follow an enter-then-exit pattern, ensuring resources are properly acquired and released*

</div>

---

## Introduction

Context managers implement **RAII** (Resource Acquisition Is Initialization) - automatic resource lifecycle management! This is **deterministic cleanup** - guaranteed resource release regardless of exceptions. Context managers are **safety nets** for system resources!

### Why Context Managers are Critical

**Problem without context managers**: Resource leaks:
```python
# DANGEROUS - resource leak if exception!
f = open("data.txt")
data = f.read()
process(data)  # If this crashes...
f.close()      # ...close() never runs! File leaked!
```

**Solution with context managers**: Guaranteed cleanup:
```python
# SAFE - cleanup guaranteed!
with open("data.txt") as f:
    data = f.read()
    process(data)  # Even if this crashes...
# f.close() runs automatically! Always!
```

**This is resource safety** - no leaks, no orphaned connections!

### Historical Context

**Context managers** added **Python 2.5** (2006) with **PEP 343**. Inspired by **C++ RAII** (Bjarne Stroustrup, 1984) - resource lifetime tied to object scope. **Java's try-with-resources** (2011) copied Python's approach!

**`__enter__` and `__exit__`** protocol - Python's context management protocol. **`__exit__`** receives exception info - can suppress or propagate exceptions! This **exception-aware cleanup** more powerful than simple `finally`!

**contextlib module** (Python 2.6) added `@contextmanager` decorator - write context managers as generators instead of classes. **Simplified syntax** made custom context managers accessible to all Python programmers!

### Real-World Analogies

**Context managers like hotel checkout**:
- **`__enter__`**: Check in (acquire room key, access resources)
- **`with` block**: Stay at hotel (use resources)
- **`__exit__`**: Check out (return key, clean room) - **always happens!**
**Hotel guarantees room gets cleaned, even if you leave early!**

**Or like borrowing library books**:
```python
with library.borrow("Python Book") as book:
    book.read()    # Use the resource
    book.study()   # Take your time
# Book automatically returned! No overdue fines!
```

**Or like lab safety protocol**:
- **Enter lab**: Put on safety equipment (`__enter__`)
- **Do experiment**: Work with materials (`with` block)
- **Exit lab**: Remove equipment, clean up (`__exit__`)
**Safety protocol runs even if experiment fails!**

### Context Manager Protocol

**Two magic methods control the lifecycle**:
```python
class ManagedResource:
    def __enter__(self):
        # Acquire resource
        return self  # Value for 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Release resource (ALWAYS runs!)
        # Return True to suppress exception
        # Return False to propagate exception
        pass
```

**This is the contract** - enter acquires, exit releases, always!

---
### Basic Syntax

```python
with expression as variable:
    # Use the resource
    pass
# Resource automatically cleaned up here
```

## File Handling with Context Managers

```python
# Traditional approach (manual cleanup)
file = open("example.txt", "w")
try:
    file.write("Hello, World!")
finally:
    file.close()

# With context manager (automatic cleanup)
with open("example.txt", "w") as file:
    file.write("Hello, World!")
# File automatically closed here

# Reading files
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# File automatically closed

# Multiple files
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line.upper())
# Both files automatically closed
```

## Why Context Managers?

```python
# Problem: File handle leak if error occurs
def process_file_unsafe():
    file = open("data.txt", "r")
    data = file.read()
    result = risky_operation(data)  # If this fails, file not closed
    file.close()  # This line never reached if error above
    return result

# Solution: with statement ensures cleanup
def process_file_safe():
    with open("data.txt", "r") as file:
        data = file.read()
        result = risky_operation(data)  # File closed even if this fails
    return result
```

## The Context Manager Protocol

```python
class MyContextManager:
    def __enter__(self):
        """Called when entering the with block"""
        print("Entering context")
        return self  # Returns value assigned to 'as' variable

    def __exit__(self, exc_type, exc_value, traceback):
        """Called when exiting the with block"""
        print("Exiting context")
        # exc_type, exc_value, traceback contain exception info if error occurred
        # Return True to suppress exception, False to propagate it
        return False

# Using the context manager
with MyContextManager() as cm:
    print("Inside with block")
# Output:
# Entering context
# Inside with block
# Exiting context
```

## Real-World Examples

### Example 1: Database Connection Manager

```python
class DatabaseConnection:
    """Context manager for database connections"""

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        print(f"Connecting to {self.db_name}...")
        # Simulate connection
        self.connection = f"Connection to {self.db_name}"
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing connection to {self.db_name}...")
        self.connection = None
        if exc_type:
            print(f"An error occurred: {exc_value}")
        return False  # Don't suppress exceptions

# Using the database connection
with DatabaseConnection("mydb") as conn:
    print(f"Using {conn}")
    print("Performing database operations...")
# Output:
# Connecting to mydb...
# Using Connection to mydb
# Performing database operations...
# Closing connection to mydb...

# Even with errors, connection closes
try:
    with DatabaseConnection("errordb") as conn:
        print("Working...")
        raise ValueError("Something went wrong!")
except ValueError:
    print("Error handled")
# Output:
# Connecting to errordb...
# Working...
# Closing connection to errordb...
# An error occurred: Something went wrong!
# Error handled
```

### Example 2: Timer Context Manager

```python
import time

class Timer:
    """Context manager to measure execution time"""

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()
        self.elapsed = self.end - self.start
        print(f"Elapsed time: {self.elapsed:.4f} seconds")
        return False

# Using the timer
with Timer():
    # Some time-consuming operation
    total = sum(range(1000000))
    time.sleep(0.5)
# Output: Elapsed time: 0.5234 seconds

# Accessing elapsed time
with Timer() as timer:
    time.sleep(1)
print(f"Operation took {timer.elapsed:.2f} seconds")
```

### Example 3: Directory Changer

```python
import os

class ChangeDirectory:
    """Context manager to temporarily change directory"""

    def __init__(self, new_path):
        self.new_path = new_path
        self.original_path = None

    def __enter__(self):
        self.original_path = os.getcwd()
        print(f"Changing from {self.original_path} to {self.new_path}")
        # In real code: os.chdir(self.new_path)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Returning to {self.original_path}")
        # In real code: os.chdir(self.original_path)
        return False

# Using the directory changer
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

with ChangeDirectory("/tmp"):
    print("Working in temporary directory")
    # Do work in /tmp

print("Back in original directory")
```

### Example 4: Resource Lock Manager

```python
import time

class ResourceLock:
    """Context manager for acquiring and releasing a lock"""

    def __init__(self, resource_name):
        self.resource_name = resource_name
        self.locked = False

    def __enter__(self):
        print(f"Acquiring lock on {self.resource_name}...")
        time.sleep(0.1)  # Simulate lock acquisition
        self.locked = True
        print(f"Lock acquired on {self.resource_name}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Releasing lock on {self.resource_name}...")
        self.locked = False
        print(f"Lock released on {self.resource_name}")
        return False

# Using the resource lock
with ResourceLock("database"):
    print("Performing critical operation")
    time.sleep(0.5)
# Lock automatically released

# Multiple locks
with ResourceLock("file1"), ResourceLock("file2"):
    print("Working with multiple resources")
# Both locks released
```

### Example 5: Temporary File Suppressor

```python
import sys
from io import StringIO

class SuppressOutput:
    """Context manager to suppress stdout"""

    def __enter__(self):
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()  # Redirect to string buffer
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.original_stdout  # Restore original stdout
        return False

# Using output suppression
print("This will be printed")

with SuppressOutput():
    print("This will NOT be printed")
    print("Neither will this")

print("This will be printed again")
# Output:
# This will be printed
# This will be printed again
```

## Using contextlib Module

```python
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    """Simple file manager using contextmanager decorator"""
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

# Using the decorator-based context manager
with file_manager("test.txt", "w") as f:
    f.write("Hello from contextmanager!")

@contextmanager
def timer_context():
    """Timer using contextmanager decorator"""
    start = time.time()
    yield
    end = time.time()
    print(f"Time elapsed: {end - start:.4f} seconds")

with timer_context():
    time.sleep(0.5)
# Output: Time elapsed: 0.5001 seconds

@contextmanager
def tag(name):
    """HTML tag context manager"""
    print(f"<{name}>")
    yield
    print(f"</{name}>")

with tag("div"):
    with tag("p"):
        print("Hello, World!")
# Output:
# <div>
# <p>
# Hello, World!
# </p>
# </div>
```

## Exception Handling in Context Managers

```python
class ErrorHandler:
    """Context manager that handles specific errors"""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is ValueError:
            print(f"ValueError handled: {exc_value}")
            return True  # Suppress the exception
        return False  # Propagate other exceptions

# ValueError is suppressed
with ErrorHandler():
    raise ValueError("This error will be handled")
print("Execution continues")

# Other errors propagate
try:
    with ErrorHandler():
        raise TypeError("This error will NOT be handled")
except TypeError as e:
    print(f"TypeError caught: {e}")
```

## Nested Context Managers

```python
# Multiple context managers
with open("file1.txt", "r") as f1, open("file2.txt", "w") as f2:
    content = f1.read()
    f2.write(content.upper())

# Nested with statements
with open("input.txt", "r") as infile:
    with open("output.txt", "w") as outfile:
        for line in infile:
            outfile.write(line.upper())
```

## Common Built-in Context Managers

```python
import threading
import sqlite3

# Thread locks
lock = threading.Lock()
with lock:
    # Critical section
    print("Thread-safe operation")

# Database connections
# with sqlite3.connect("database.db") as conn:
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users")
#     results = cursor.fetchall()

# Decimal context
from decimal import Decimal, localcontext

with localcontext() as ctx:
    ctx.prec = 2  # Set precision to 2 decimal places
    result = Decimal("1.234") + Decimal("2.345")
    print(result)  # 3.6
```

## Key Takeaways

1. **Context managers**: Ensure proper resource cleanup
2. **with statement**: Simplifies resource management
3. **Protocol**: Implement `__enter__()` and `__exit__()`
4. **Automatic cleanup**: Resources released even if errors occur
5. **contextlib.contextmanager**: Decorator for simpler context managers
6. **Common use cases**: Files, locks, connections, timers
7. **Exception handling**: `__exit__()` can suppress or propagate exceptions
8. **Best practice**: Always use with statement for file operations
