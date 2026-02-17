## Lecture Script: Handle File Paths Across Platforms


---

### CS Theory Bite

> **Origin**: Path separators differ because **DOS** (1981) chose backslash `\` while **Unix** (1971) used forward slash `/`. Python's `pathlib` (Python 3.4) provides platform-independent path handling.
>
> **Analogy**: Cross-platform paths are like **universal power adapters** — one interface works regardless of which country (OS) you're in.
>
> **Why it matters**: Hardcoding `/` or `\` breaks your code on other platforms — use `pathlib.Path` or `os.path.join()`.



### Hook (2 minutes)

Windows paths use backslashes: `C:\\Users\\alice\\data.txt`
Mac/Linux use forward slashes: `/home/alice/data.txt`

Hardcoding either breaks on the other OS. Solution: `pathlib`.

```python
from pathlib import Path
data_file = Path("home") / "alice" / "data.txt"
# Works on ALL platforms!
```

---

### Section 1: Creating Paths (3 minutes)

```python
from pathlib import Path

p = Path("documents/reports/annual.txt")
print(p.name)    # annual.txt
print(p.stem)    # annual
print(p.suffix)  # .txt
print(p.parent)  # documents/reports
```

Join paths with `/`:
```python
base = Path("/home/user")
full = base / "projects" / "app" / "main.py"
```

---

### Section 2: Checking Paths (3 minutes)

```python
p = Path("data.txt")
p.exists()      # Does it exist?
p.is_file()     # Is it a file?
p.is_dir()      # Is it a directory?
p.is_absolute() # Absolute path?
p.resolve()     # Convert to absolute
```

---

### Section 3: Working with Directories (3 minutes)

```python
d = Path("my_project")
d.mkdir(exist_ok=True)           # Create directory
d.mkdir(parents=True, exist_ok=True)  # Create nested

# List files
for f in d.iterdir():
    print(f.name)

# Find by pattern
for f in d.glob("*.py"):
    print(f)

# Recursive search
for f in d.rglob("*.txt"):
    print(f)
```

---

### Summary (1 minute)

1. Use `pathlib.Path` — not string concatenation
2. `/` operator joins paths safely
3. `.name`, `.stem`, `.suffix`, `.parent` for components
4. `.exists()`, `.is_file()`, `.is_dir()` for checks
5. `.glob()` and `.rglob()` for searching
