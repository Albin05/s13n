## Lecture Notes: Read Text Files in Python

**Duration:** 12 minutes

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
