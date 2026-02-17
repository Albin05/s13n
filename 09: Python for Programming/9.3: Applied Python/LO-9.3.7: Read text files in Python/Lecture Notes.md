## Lecture Notes: Read Text Files in Python


---

## Introduction

File reading implements **persistent storage access** - retrieving data that outlives program execution! Before file systems, data existed only in RAM (volatile) and disappeared when programs ended. File I/O enables **data persistence** - the foundation of all modern applications, databases, and operating systems!

### Why File I/O is Fundamental

**Before file systems** (punch cards, 1950s): Data manually re-entered each run:
```
// No persistence - enter data every time!
ENTER 10 NUMBERS: 1, 2, 3...
PROGRAM ENDS → DATA LOST!
```

**With file systems** (1960s onwards): Data saved and reloaded:
```python
# Write once, read forever!
with open("data.txt") as f:
    data = f.read()  # Data survives program restarts!
```

**This is persistent storage** - data outlives the program that created it!

### Historical Context

**File systems invented**: **Multics** (1964, MIT) pioneered hierarchical file systems. **Unix** (1971, Bell Labs) introduced "everything is a file" philosophy - devices, sockets, pipes all accessed like files!

**Context managers** (`with` statement): Introduced in **Python 2.5 (2006)** via **PEP 343**. Based on **RAII** (Resource Acquisition Is Initialization) from **C++** (1985). Solves **resource leak problem** - files left open consuming file descriptors!

**Buffered I/O**: Python's file objects use **buffering** - read/write in chunks (8KB default) rather than byte-by-byte. Invented by **Unix** (1970s) for performance. Reduces syscalls by 1000x+!

### Real-World Analogies

**Reading files like checking out library books**:
- **Open file**: Request book from library (`open()`)
- **Read content**: Read the book (`read()`)
- **Close file**: Return book to library (`close()`)
- **With statement**: Auto-return when done (context manager)
**You don't forget to return books - don't forget to close files!**

**Or like reading a recipe**:
```python
with open("recipe.txt") as f:
    for step in f:  # Read step-by-step
        follow_instruction(step.strip())
# Recipe book auto-closes when done!
```

**Or like streaming video**:
- **Read entire file**: Download entire video first (`read()`)
- **Line-by-line**: Stream video chunk-by-chunk (`for line in f`)
- **Memory efficient**: Don't load 2-hour video into RAM at once!
**Streaming prevents memory overflow - same for large files!**

### The Context Manager Pattern

**Problem with manual close**: Easy to forget, especially with errors:
```python
# DANGEROUS - might not close!
file = open("data.txt")
data = file.read()
process(data)  # Exception here?
file.close()  # Might not execute!
```

**Solution with context manager**: Guaranteed cleanup:
```python
# SAFE - always closes!
with open("data.txt") as file:
    data = file.read()
    process(data)  # Exception OK!
# File auto-closed here, always!
```

**This implements RAII** - Resource Acquisition Is Initialization. `__enter__` and `__exit__` magic methods ensure cleanup!

---

### Opening and Reading Files

The `open()` function opens a file. Always close it when done.

```python
# Basic pattern
file = open("data.txt", "r")  # "r" = read mode (default)
content = file.read()
print(content)
file.close()
```

---

### The `with` Statement (Recommended)

Automatically closes the file when done:

```python
with open("data.txt") as file:
    content = file.read()
    print(content)
# File is automatically closed here
```

Always prefer `with` — it handles cleanup even if an error occurs.

---

### Three Ways to Read

**1. `read()` — entire file as one string:**
```python
with open("data.txt") as f:
    content = f.read()
    print(content)  # Entire file content
```

**2. `readline()` — one line at a time:**
```python
with open("data.txt") as f:
    line1 = f.readline()  # First line
    line2 = f.readline()  # Second line
    print(line1.strip())
    print(line2.strip())
```

**3. `readlines()` — all lines as a list:**
```python
with open("data.txt") as f:
    lines = f.readlines()
    print(lines)  # ['line1\n', 'line2\n', 'line3\n']
```

---

### Iterating Line by Line (Most Common)

```python
with open("data.txt") as f:
    for line in f:
        print(line.strip())  # .strip() removes \n
```

This is memory-efficient — reads one line at a time instead of loading everything.

---

### Handling Newlines

Each line from a file includes `\n` at the end:

```python
with open("data.txt") as f:
    lines = f.readlines()
    print(lines)  # ['Hello\n', 'World\n']

# Clean them up:
clean_lines = [line.strip() for line in lines]
print(clean_lines)  # ['Hello', 'World']
```

---

### Reading with Encoding

```python
# UTF-8 (handles special characters)
with open("data.txt", encoding="utf-8") as f:
    content = f.read()

# For other encodings:
with open("legacy.txt", encoding="latin-1") as f:
    content = f.read()
```

---

### File Not Found Handling

```python
try:
    with open("missing.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("File does not exist!")
```

---

### Practical Examples

**1. Count Lines and Words:**
```python
with open("document.txt") as f:
    lines = f.readlines()

line_count = len(lines)
word_count = sum(len(line.split()) for line in lines)
char_count = sum(len(line) for line in lines)

print(f"Lines: {line_count}")
print(f"Words: {word_count}")
print(f"Characters: {char_count}")
```

**2. Search for a Pattern:**
```python
with open("log.txt") as f:
    for i, line in enumerate(f, 1):
        if "ERROR" in line:
            print(f"Line {i}: {line.strip()}")
```

**3. Read Numbers from File:**
```python
with open("numbers.txt") as f:
    numbers = [float(line.strip()) for line in f if line.strip()]

print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers)/len(numbers):.2f}")
```

**4. Read CSV-like Data:**
```python
with open("students.txt") as f:
    for line in f:
        parts = line.strip().split(",")
        name, age, grade = parts[0], int(parts[1]), parts[2]
        print(f"{name} (age {age}): {grade}")
```

---

### Key Takeaways

1. Always use `with open()` — auto-closes the file
2. `read()` gets everything, `readline()` one line, `readlines()` all as list
3. Iterate with `for line in file` for memory efficiency
4. Use `.strip()` to remove newline characters
5. Handle `FileNotFoundError` for missing files
6. Specify `encoding="utf-8"` for special characters
