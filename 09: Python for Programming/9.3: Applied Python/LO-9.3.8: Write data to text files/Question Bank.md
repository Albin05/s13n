## Question Bank: Write Data to Text Files

---

### Q1: Basic File Writing (3 minutes, Low Difficulty)

Write a program that:
1. Creates "greeting.txt" with 3 lines of text using `write()`
2. Creates "numbers.txt" with numbers 1-10 using `print(file=f)`
3. Creates "list.txt" from a list using `writelines()`

Read each file back and verify the contents.

**Key Concepts:** write(), print(file=), writelines()

---

### Q2: Student Record Writer (3 minutes, Low Difficulty)

Given a list of students:
```python
students = [
    {"name": "Alice", "age": 22, "grade": "A"},
    {"name": "Bob", "age": 24, "grade": "B"},
    {"name": "Charlie", "age": 21, "grade": "A+"}
]
```

Write them to "students.txt" in a formatted table:
```
Name       Age  Grade
---------- ---- -----
Alice      22   A
Bob        24   B
Charlie    21   A+
```

**Key Concepts:** Formatted string writing

---

### Q3: Log Writer (5 minutes, Medium Difficulty)

Write a `Logger` class that:
- Opens a log file on creation
- Has `log(level, message)` method that writes timestamped entries
- Has `close()` method
- Uses context manager protocol (`__enter__`/`__exit__`)

Usage:
```python
with Logger("app.log") as log:
    log.log("INFO", "Application started")
    log.log("ERROR", "Connection failed")
```

**Key Concepts:** Class-based file writing, context manager

---

### Q4: Data Exporter (5 minutes, Medium Difficulty)

Write `export_data(data, filename, format)` that exports a list of dicts:
- format="csv": comma-separated with header row
- format="txt": human-readable aligned columns
- format="md": markdown table format

```python
data = [{"name": "Alice", "score": 92}, {"name": "Bob", "score": 85}]
```

**Key Concepts:** Multiple output formats, string formatting

---

### Q5: Safe File Writer (5 minutes, Medium Difficulty)

Write `safe_write(filename, content)` that:
- If file doesn't exist: creates it
- If file exists: asks before overwriting (use "x" mode + fallback)
- Creates a backup of existing file before overwriting
- Returns True if written, False if skipped

**Key Concepts:** "x" mode, FileExistsError, backup pattern
