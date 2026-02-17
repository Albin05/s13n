## Pre-Read: Write Data to Text Files


---

## Introduction

**File writing** saves data permanently to disk, enabling **data persistence** across program runs! This is how applications save user work, create logs, generate reports, and store configuration. Writing is the **output half** of file I/O!

### Why File Writing Matters

**Problem without persistence**: Data lost when program ends:
```python
# All work lost!
results = calculate_for_hours()
# Program ends → results disappear!
```

**Solution with file writing**: Save data permanently:
```python
# Work saved forever!
results = calculate_for_hours()
with open("results.txt", "w") as f:
    f.write(str(results))
# Data persists on disk!
```

**This is data permanence** - your work survives!

### Critical Warning: Write Mode Destroys Data!

**`"w"` mode ERASES existing files**:
```python
# DANGER - old content LOST!
with open("important.txt", "w") as f:
    f.write("New content")
# Previous content GONE forever!
```

**Use `"a"` (append) to preserve**:
```python
# SAFE - keeps old content
with open("log.txt", "a") as f:
    f.write("New entry\n")
# Old content preserved!
```

### Real-World Analogy

**Write modes like document editing**:
- **`"w"` mode**: "Save As" new file (overwrites)
- **`"a"` mode**: "Add to existing" (preserves)
- **`"x"` mode**: "Create only if new" (safety check)
**Choose the right mode to avoid data loss!**

---

### Writing to a File

```python
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
```

---

### Write Modes

- `"w"` — write (creates new or **overwrites** existing)
- `"a"` — append (adds to end of file)
- `"x"` — create only (fails if file exists)

---

### Key Point

`write()` only accepts strings. Convert numbers first:
```python
f.write(str(42) + "\n")
# Or use print:
print(42, file=f)
```

---

### Try This

```python
with open("test_output.txt", "w") as f:
    for i in range(5):
        f.write(f"Line {i+1}\n")
```
