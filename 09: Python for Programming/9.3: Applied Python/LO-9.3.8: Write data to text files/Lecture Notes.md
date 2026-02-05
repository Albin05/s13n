## Lecture Notes: Write Data to Text Files

**Duration:** 10 minutes

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
