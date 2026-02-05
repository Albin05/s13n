## Pre-Read: Read Text Files in Python

**Duration:** 5 minutes

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
