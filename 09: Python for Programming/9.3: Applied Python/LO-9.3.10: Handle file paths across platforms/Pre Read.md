## Pre-Read: Handle File Paths Across Platforms


---

### The Problem

```python
# This breaks on Windows:
path = "/home/user/data.txt"

# This breaks on Mac/Linux:
path = "C:\\Users\\user\\data.txt"
```

---

### The Solution: pathlib

```python
from pathlib import Path

# Works on ALL platforms
data = Path("documents") / "data.txt"
print(data)  # documents/data.txt (or documents\data.txt on Windows)
```

---

### Key Operations

```python
p = Path("folder/file.txt")
p.name      # "file.txt"
p.stem      # "file"
p.suffix    # ".txt"
p.parent    # Path("folder")
p.exists()  # True/False
```

---

### Try This

```python
from pathlib import Path
home = Path.home()
print(f"Home: {home}")
print(f"CWD: {Path.cwd()}")
```
