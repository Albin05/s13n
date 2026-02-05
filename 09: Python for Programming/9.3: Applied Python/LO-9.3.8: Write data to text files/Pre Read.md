## Pre-Read: Write Data to Text Files

**Duration:** 5 minutes

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
