## Pre-Read: Read Text Files in Python


---

## Introduction

**File reading** accesses persistent storage - data that survives program restarts! Before file systems (1960s), data lived only in RAM and disappeared when programs ended. File I/O enables **data persistence** - the foundation of all modern computing!

### Why File Reading Matters

**Problem without persistence**: Data lost after every run:
```
// Punch card era - re-enter data each time!
INPUT: 1, 2, 3, 4, 5
PROGRAM ENDS → ALL DATA LOST!
```

**Solution with files**: Data saved and reloaded:
```python
# Write once, read forever!
with open("data.txt") as f:
    data = f.read()  # Data persists!
```

**This is persistent storage** - data outlives the program!

### The Context Manager (`with`)

**Always use `with`** - auto-closes files even if errors occur:
```python
with open("data.txt") as f:
    content = f.read()
# File auto-closed here - guaranteed!
```

**Without `with`** - easy to forget closing:
```python
f = open("data.txt")
content = f.read()  # Exception here?
f.close()  # Might not run!
```

**Context managers** (Python 2.5+) implement RAII - Resource Acquisition Is Initialization!

---

### Reading a File

```python
with open("data.txt") as f:
    content = f.read()
    print(content)
```

`with` ensures the file is closed automatically.

---

### Three Ways to Read

```python
f.read()       # Entire file as one string
f.readline()   # One line at a time
f.readlines()  # All lines as a list
```

---

### Line by Line (Best for Large Files)

```python
with open("data.txt") as f:
    for line in f:
        print(line.strip())  # strip() removes newline
```

---

### Try This

Create a file called `test.txt` with a few lines of text. Then:
```python
with open("test.txt") as f:
    for i, line in enumerate(f, 1):
        print(f"Line {i}: {line.strip()}")
```
