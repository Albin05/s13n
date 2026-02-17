## Lecture Script: Write Data to Text Files


---

### CS Theory Bite

> **Origin**: File writing uses **buffered I/O** — data accumulates in memory before flushing to disk in bulk. This **batching** makes writes up to 100x faster than writing byte-by-byte.
>
> **Analogy**: Buffered writing is like **filling a truck before delivering** — more efficient than sending one package at a time.
>
> **Why it matters**: Understanding write modes (`w` overwrites, `a` appends, `x` creates) prevents accidental data loss.



### Hook (2 minutes)

You've analyzed data, built reports, crunched numbers. Now you need to save the results. Without file writing, all your work vanishes when the program ends.

```python
with open("results.txt", "w") as f:
    f.write("Analysis complete!\n")
    f.write(f"Total: {total}\n")
```

---

### Section 1: Write Mode (3 minutes)

```python
# "w" — write (creates or overwrites!)
with open("output.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")

# "a" — append (adds to end)
with open("output.txt", "a") as f:
    f.write("Appended line\n")

# "x" — exclusive (fails if exists)
with open("new_file.txt", "x") as f:
    f.write("Brand new!\n")
```

---

### Section 2: Writing Methods (3 minutes)

```python
# write() — one string at a time
f.write("text\n")  # Must add \n yourself

# writelines() — list of strings
f.writelines(["line1\n", "line2\n"])

# print() — adds newline automatically
print("text", file=f)
print(42, file=f)  # Handles type conversion
```

---

### Section 3: Common Patterns (3 minutes)

**Write a list of numbers:**
```python
with open("nums.txt", "w") as f:
    for n in range(1, 11):
        print(n, file=f)
```

**Write formatted data:**
```python
with open("report.txt", "w") as f:
    for name, score in results:
        f.write(f"{name:20s} {score:5.1f}\n")
```

**Copy and transform:**
```python
with open("in.txt") as fin, open("out.txt", "w") as fout:
    for line in fin:
        fout.write(line.upper())
```

---

### Summary (1 minute)

1. `"w"` creates/overwrites, `"a"` appends, `"x"` creates only
2. `write()` for strings, `print(file=f)` for convenience
3. Always add `\n` with `write()` — `print()` does it automatically
4. Use `with` to ensure files are properly closed
