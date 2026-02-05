## Post-class Quiz: Write Data to Text Files

---

### Question 1
What does mode `"w"` do if the file already exists?

A) Appends to it
B) Raises an error
C) Overwrites it completely
D) Does nothing

**Correct Answer: C**

*Explanation: Write mode `"w"` erases the existing file content and starts fresh. If you want to keep existing content, use `"a"` (append) instead.*

---

### Question 2
What is the difference between `write()` and `print(file=f)`?

A) No difference
B) `write()` doesn't add a newline; `print()` does
C) `print()` is faster
D) `write()` can handle any type; `print()` only strings

**Correct Answer: B**

*Explanation: `write()` writes exactly what you give it — no newline added. `print()` adds a newline by default. Also, `print()` converts non-strings automatically, while `write()` requires strings.*

---

### Question 3
What does `writelines()` do?

A) Writes each string on a new line
B) Writes a list of strings as-is (no newlines added)
C) Writes line numbers
D) Reads lines from one file and writes to another

**Correct Answer: B**

*Explanation: `writelines()` writes each string in the list exactly as-is. It does NOT add newline characters between items. You must include `\n` in your strings.*

---

### Question 4
What mode prevents accidentally overwriting an existing file?

A) `"w"`
B) `"a"`
C) `"x"`
D) `"r+"`

**Correct Answer: C**

*Explanation: `"x"` (exclusive creation) raises `FileExistsError` if the file already exists. This prevents accidental data loss from overwriting.*

---

### Question 5
What is the output file content after this code?

```python
with open("test.txt", "w") as f:
    f.write("A")
    f.write("B")
    f.write("C")
```

A) `A\nB\nC`
B) `ABC`
C) `A B C`
D) Error

**Correct Answer: B**

*Explanation: `write()` doesn't add newlines or spaces. It writes exactly what you give it. The three `write()` calls produce `ABC` with no separation.*

---
