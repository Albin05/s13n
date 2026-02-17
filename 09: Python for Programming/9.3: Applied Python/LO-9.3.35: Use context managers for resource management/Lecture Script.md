# Lecture Script: LO-9.3.35 Use Context Managers for Resource Management


### CS Theory Bite

> **Origin**: Context managers (Python 2.5, PEP 343) implement **RAII** — automatic resource cleanup. The `with` statement guarantees `__exit__()` runs even if exceptions occur — Java copied this as try-with-resources (2011).
>
> **Analogy**: A context manager is like a **hotel checkout** — check in (`__enter__`), use the room, check out (`__exit__`) is guaranteed even if you leave early.
>
> **Why it matters**: `with open() as f:` prevents file leaks — the #1 resource management pattern in Python.


## [0:00-0:02] Hook (2 min)
**Say**: "File not closed, database connection leaked, lock never released — these bugs are SILENT KILLERS. Context managers solve this with one word: 'with'. Automatic cleanup, guaranteed. No leaks, no crashes, no stress!"

**Demo**:
```python
# The problem - file never closed if error occurs
file = open("data.txt", "w")
file.write("Some data")
# If error here, file.close() never runs!
file.close()

# The solution - context manager
with open("data.txt", "w") as file:
    file.write("Some data")
# File automatically closed, even if error occurs!

print("File handle cleaned up automatically!")
```

**Say**: "That's the with statement! Let's master context managers."

## [0:02-0:06] The Problem: Resource Leaks (4 min)

**Say**: "Without context managers, you need try-finally blocks everywhere. Ugly and error-prone!"

**Live Code**:
```python
# Manual cleanup - verbose and easy to forget
file = None
try:
    file = open("example.txt", "w")
    file.write("Hello, World!")
    # If exception here, file still needs closing
    raise ValueError("Oops!")
finally:
    if file:
        file.close()
        print("File closed in finally block")

# With context manager - clean and automatic
try:
    with open("example.txt", "w") as file:
        file.write("Hello, World!")
        # If exception here, file STILL closed automatically
        raise ValueError("Oops!")
except ValueError:
    print("Error handled, but file was still closed!")
```

**Point out**: "The with statement GUARANTEES cleanup happens, even if exceptions occur!"

**Emphasize**: "This isn't just for files — any resource that needs cleanup benefits from context managers!"

## [0:06-0:10] Basic Context Manager Usage (4 min)

**Say**: "The with statement works with any object that implements the context manager protocol."

**Live Code**:
```python
# File operations - most common use case
with open("data.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")
# File automatically closed here

# Verify file is closed
print(f"File closed: {file.closed}")  # True

# Multiple files at once
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line.upper())
# Both files automatically closed

# Nested with statements (older style)
with open("input.txt", "r") as infile:
    with open("output.txt", "w") as outfile:
        for line in infile:
            outfile.write(line.upper())
```

**Say**: "Use comma-separated syntax for multiple context managers on one line. Cleaner!"

## [0:10-0:13] Creating Custom Context Managers (3 min)

**Say**: "Build your own with two magic methods: __enter__ and __exit__."

**Live Code**:
```python
class DatabaseConnection:
    """Context manager for database connections"""

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        """Called when entering 'with' block"""
        print(f"Connecting to {self.db_name}...")
        self.connection = f"Connection to {self.db_name}"
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        """Called when exiting 'with' block"""
        print(f"Closing connection to {self.db_name}...")
        self.connection = None
        if exc_type:
            print(f"An error occurred: {exc_value}")
        return False  # Don't suppress exceptions

# Using the context manager
with DatabaseConnection("mydb") as conn:
    print(f"Using {conn}")
    print("Performing database operations...")
# Output:
# Connecting to mydb...
# Using Connection to mydb
# Performing database operations...
# Closing connection to mydb...

# Even with errors, cleanup happens!
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

**Point out**: "__exit__ receives exception info. Return True to suppress the exception, False to propagate it."

## [0:13-0:16] Real-World Example: Timer Context Manager (3 min)

**Say**: "Perfect for measuring code execution time."

**Live Code**:
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
print("Timing a slow operation:")
with Timer():
    total = sum(range(1000000))
    time.sleep(0.5)
# Output: Elapsed time: 0.5234 seconds

# Access elapsed time
with Timer() as timer:
    time.sleep(1)
    result = "Done"

print(f"Operation took {timer.elapsed:.2f} seconds")
print(f"Result: {result}")
```

**Say**: "The context manager object is returned by __enter__, accessible via 'as' variable!"

## [0:16-0:19] Real-World Example: Directory Changer (3 min)

**Say**: "Temporarily change directories, then automatically return."

**Live Code**:
```python
import os

class ChangeDirectory:
    """Context manager to temporarily change directory"""

    def __init__(self, new_path):
        self.new_path = new_path
        self.original_path = None

    def __enter__(self):
        self.original_path = os.getcwd()
        print(f"Changing from {self.original_path}")
        print(f"         to {self.new_path}")
        os.chdir(self.new_path)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Returning to {self.original_path}")
        os.chdir(self.original_path)
        return False

# Demonstrate
current = os.getcwd()
print(f"Current directory: {current}")

with ChangeDirectory("/tmp"):
    print(f"Inside with block: {os.getcwd()}")
    # Do work in /tmp

print(f"After with block: {os.getcwd()}")
```

**Point out**: "Perfect for operations that need a specific working directory but shouldn't affect the rest of the program!"

## [0:19-0:21] Using contextlib for Simple Context Managers (2 min)

**Say**: "The contextlib module makes creating context managers even easier with decorators!"

**Live Code**:
```python
from contextlib import contextmanager
import time

@contextmanager
def timer_context():
    """Timer using contextmanager decorator"""
    start = time.time()
    yield  # Code here runs in the with block
    end = time.time()
    print(f"Time elapsed: {end - start:.4f} seconds")

with timer_context():
    time.sleep(0.5)
    print("Doing work...")
# Output:
# Doing work...
# Time elapsed: 0.5001 seconds

@contextmanager
def file_manager(filename, mode):
    """Simple file manager"""
    file = open(filename, mode)
    try:
        yield file  # Provide file to with block
    finally:
        file.close()  # Cleanup always runs

with file_manager("test.txt", "w") as f:
    f.write("Hello from contextmanager!")

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

**Emphasize**: "The @contextmanager decorator turns a generator into a context manager. Code before yield is __enter__, after yield is __exit__!"

## [0:21-0:23] Real-World Example: Resource Lock (2 min)

**Say**: "Context managers ensure locks are always released, preventing deadlocks."

**Live Code**:
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
    print("Operation complete")
# Lock automatically released

# Multiple locks
with ResourceLock("file1"), ResourceLock("file2"):
    print("Working with multiple resources")
# Both locks released automatically
```

**Say**: "Critical in multi-threaded applications where forgetting to release a lock causes deadlock!"

## [0:23-0:24] Practice Challenge (1 min)

**Challenge**: "Create a context manager that suppresses print statements inside its block."

**Skeleton**:
```python
import sys
from io import StringIO

class SuppressOutput:
    def __enter__(self):
        # TODO: Redirect stdout to a string buffer
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        # TODO: Restore original stdout
        pass

# Test
print("This will be printed")
with SuppressOutput():
    print("This will NOT be printed")
print("This will be printed again")
```

**Solution** (show after 1 minute):
```python
class SuppressOutput:
    def __enter__(self):
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()  # Redirect to string buffer
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.original_stdout  # Restore
        return False
```

## [0:24-0:25] Wrap-up (1 min)

**Key Points**:
1. **with statement**: Ensures automatic resource cleanup
2. **__enter__()**: Setup, returns resource object
3. **__exit__()**: Cleanup, receives exception info
4. **@contextmanager**: Decorator for simpler context managers
5. **Guaranteed cleanup**: Even if exceptions occur

**Common Mistakes**:
- Forgetting to return self from __enter__
- Not handling exceptions properly in __exit__
- Not using with for file operations (ALWAYS use it!)
- Returning True from __exit__ accidentally (suppresses all errors)

**Real-World Use Cases**:
- File operations (always!)
- Database connections
- Network sockets
- Locks and semaphores
- Temporary state changes (directory, environment variables)
- Timing and profiling
- Transaction management

**Built-in Context Managers**:
- open(): File operations
- threading.Lock(): Thread synchronization
- sqlite3.connect(): Database connections
- decimal.localcontext(): Decimal precision

**Closing**: "Context managers are Python's way of saying 'clean up after yourself'. Use them for ANY resource that needs cleanup. Your code will be more reliable, cleaner, and bug-free!"
