## Lecture Script: Read Text Files in Python

**Duration:** 12 minutes

---

### Hook (2 minutes)

Every application reads files — config files, log files, data files, user documents. Python makes it simple:

```python
with open("data.txt") as f:
    content = f.read()
```

Three lines to read any text file. Today we master every way to read files.

---

### Section 1: Opening Files (2 minutes)

```python
# Always use 'with' — auto-closes the file
with open("data.txt") as f:
    content = f.read()

# Without 'with' (don't do this)
f = open("data.txt")
content = f.read()
f.close()  # Easy to forget!
```

---

### Section 2: Three Reading Methods (3 minutes)

```python
# read() — entire file as string
with open("data.txt") as f:
    everything = f.read()

# readline() — one line at a time
with open("data.txt") as f:
    first = f.readline()
    second = f.readline()

# readlines() — all lines as a list
with open("data.txt") as f:
    all_lines = f.readlines()  # ['line1\n', 'line2\n']
```

---

### Section 3: Line-by-Line Iteration (3 minutes)

```python
# Best approach — memory efficient
with open("big_file.txt") as f:
    for line in f:
        print(line.strip())
```

Always use `.strip()` to remove the trailing newline.

With line numbers:
```python
with open("data.txt") as f:
    for i, line in enumerate(f, 1):
        print(f"{i}: {line.strip()}")
```

---

### Section 4: Error Handling (1 minute)

```python
try:
    with open("data.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
```

---

### Summary (1 minute)

1. Use `with open()` — always
2. `read()` for small files, iteration for large files
3. `.strip()` to clean newlines
4. Handle `FileNotFoundError`
