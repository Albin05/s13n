## Post-class Quiz: Handle File Paths Across Platforms

---

### Question 1
What module provides cross-platform path handling?

A) `os.system`
B) `pathlib`
C) `sys.path`
D) `filepath`

**Correct Answer: B**

*Explanation: `pathlib` (specifically `pathlib.Path`) provides an object-oriented way to handle file paths that works across Windows, macOS, and Linux.*

---

### Question 2
What does `Path("a") / "b" / "c.txt"` produce?

A) `"a/b/c.txt"` or `"a\b\c.txt"` depending on OS
B) `"a//b//c.txt"`
C) Error
D) `"abc.txt"`

**Correct Answer: A**

*Explanation: The `/` operator joins path components using the correct separator for the current OS. On Unix it uses `/`, on Windows it uses `\`.*

---

### Question 3
What does `Path("file.tar.gz").suffix` return?

A) `".tar.gz"`
B) `".gz"`
C) `".tar"`
D) `"tar.gz"`

**Correct Answer: B**

*Explanation: `.suffix` returns only the last extension. For `file.tar.gz`, that's `.gz`. Use `.suffixes` to get all: `['.tar', '.gz']`.*

---

### Question 4
How do you find all `.py` files recursively in a directory?

A) `Path("dir").glob("*.py")`
B) `Path("dir").rglob("*.py")`
C) `Path("dir").find("*.py")`
D) `Path("dir").search("*.py")`

**Correct Answer: B**

*Explanation: `rglob()` searches recursively through all subdirectories. `glob()` only searches the immediate directory.*

---

### Question 5
What does `Path("data.txt").resolve()` do?

A) Deletes the file
B) Converts to an absolute path
C) Checks if the path is valid
D) Creates the file

**Correct Answer: B**

*Explanation: `resolve()` converts a relative path to an absolute path by prepending the current working directory and resolving any `..` or symlinks.*

---
