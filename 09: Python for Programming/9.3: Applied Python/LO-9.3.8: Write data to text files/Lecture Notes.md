## Lecture Notes: Write Data to Text Files


---

<div align="center">

![Python Write Text File open() write mode](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/LO-9.3.8.png)

*Writing files follows the Input-Process-Output pattern: prepare data, then write it to a file*

</div>

---

## Introduction

File writing implements **persistent data storage** - saving data that survives program execution! This enables **data permanence** across sessions, the foundation of databases, logs, configuration files, and all modern applications. Writing is the complement to reading - together they form the **I/O contract**!

### Why File Writing is Essential

**Before file writing** (volatile memory only): All data lost on exit:
```python
# Data only in RAM - ephemeral!
results = calculate_important_data()
# Program ends → results GONE FOREVER!
```

**With file writing** (persistent storage): Data saved for later:
```python
# Data persists on disk!
results = calculate_important_data()
with open("results.txt", "w") as f:
    f.write(str(results))
# Data survives program restarts!
```

**This is data permanence** - computational results preserved indefinitely!

### Historical Context

**File writing** emerged with **early file systems**: **Multics** (1964) and **Unix** (1971). Before this, data stored on **punch cards** (physical) or **magnetic tape** (sequential only).

**Write modes** (`w`, `a`, `x`): Inherited from **C stdio** (1970s) which defined `fopen()` modes. Python adopted this convention for familiarity. `x` mode (exclusive create) added in **Python 3.3** to prevent accidental overwrites!

**Buffered writing**: Python doesn't write immediately - uses **buffer** (default 8KB). Flush on close, or manually with `flush()`. Invented by **Unix** for performance - reduces disk I/O syscalls!

### Real-World Analogies

**File writing like taking notes in class**:
- **Write mode**: New notebook (overwrites old notes)
- **Append mode**: Add to existing notebook (keeps old notes)
- **Exclusive mode**: Won't write if notebook exists (safety)
**Files are your program's permanent notebook!**

**Or like saving a document**:
```python
# Write mode - "Save As" (creates new)
with open("essay.txt", "w") as f:
    f.write("My essay content...")

# Append mode - "Add to existing"
with open("diary.txt", "a") as f:
    f.write("Today's entry...")
```

**Or like bank transactions**:
- **Write**: Replace entire account balance (dangerous!)
- **Append**: Add transaction to ledger (safe!)
- **Exclusive**: Create new account only if doesn't exist
**Append mode is like transaction log - preserves history!**

### The Dangerous Write Mode

**Critical warning**: `"w"` mode **DESTROYS** existing files!
```python
# DANGEROUS - file.txt content LOST!
with open("file.txt", "w") as f:
    f.write("New content")
# All previous data GONE - irreversible!
```

**Safer alternative**: Use `"x"` (exclusive) or `"a"` (append):
```python
# SAFE - fails if exists
with open("file.txt", "x") as f:
    f.write("New content")
# Or append - preserves existing
with open("file.txt", "a") as f:
    f.write("Additional content")
```

---

### Writing to Files

Use `open()` with mode `"w"` (write) or `"a"` (append):

```python
# Write mode — creates new or OVERWRITES existing
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("Second line\n")
```

**Warning:** `"w"` mode erases the file if it exists!

---

### Write Modes

| Mode | Description |
|------|-------------|
| `"w"` | Write — creates new or overwrites |
| `"a"` | Append — adds to end of existing file |
| `"x"` | Exclusive create — fails if file exists |

---

### Writing Methods

**`write()` — write a string:**
```python
with open("output.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
```

**`writelines()` — write a list of strings:**
```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)
```

Note: `writelines()` does NOT add newlines — include `\n` in your strings.

---

### Using print() to Write

```python
with open("output.txt", "w") as f:
    print("Hello, World!", file=f)
    print("Line 2", file=f)
    print(f"Result: {42}", file=f)
```

`print()` automatically adds newlines.

---

### Writing Numbers and Other Types

`write()` only accepts strings — convert first:

```python
with open("numbers.txt", "w") as f:
    numbers = [10, 20, 30, 40, 50]
    for num in numbers:
        f.write(f"{num}\n")
```

Or use `print()`:
```python
with open("numbers.txt", "w") as f:
    for num in [10, 20, 30]:
        print(num, file=f)
```

---

### Exclusive Create Mode (`"x"`)

Fails if file already exists (prevents accidental overwrite):

```python
try:
    with open("output.txt", "x") as f:
        f.write("New file content")
except FileExistsError:
    print("File already exists!")
```

---

### Practical Examples

**1. Save a Report:**
```python
def save_report(filename, title, data):
    with open(filename, "w") as f:
        f.write(f"{'='*40}\n")
        f.write(f"{title}\n")
        f.write(f"{'='*40}\n\n")
        for key, value in data.items():
            f.write(f"{key}: {value}\n")

save_report("report.txt", "Sales Report", {"Q1": 1000, "Q2": 1500, "Q3": 1200})
```

**2. Write CSV-style Data:**
```python
students = [("Alice", 22, "A"), ("Bob", 24, "B"), ("Charlie", 21, "A")]

with open("students.txt", "w") as f:
    f.write("Name,Age,Grade\n")
    for name, age, grade in students:
        f.write(f"{name},{age},{grade}\n")
```

**3. Copy and Transform:**
```python
with open("input.txt") as fin, open("output.txt", "w") as fout:
    for line in fin:
        fout.write(line.upper())
```

---

### Key Takeaways

1. `"w"` mode creates or **overwrites** — be careful!
2. `"a"` mode appends to existing content
3. `"x"` mode prevents accidental overwrites
4. `write()` needs strings — convert numbers first
5. `print(data, file=f)` is convenient and adds newlines
6. Always use `with` for automatic file closing
