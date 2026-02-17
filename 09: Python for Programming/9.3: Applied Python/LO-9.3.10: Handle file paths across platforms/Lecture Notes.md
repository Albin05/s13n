# Lecture Notes: Handle File Paths

## File Paths

A file path specifies the location of a file in the filesystem.


---

<div align="center">

![File folders and documents](https://images.unsplash.com/photo-1544396821-4dd40b938ad3?w=800&q=80)

*Python can read from and write to files on your system*

</div>

---

## Introduction

File paths implement **filesystem navigation** - locating files in hierarchical directory structures! The challenge: **platform differences** - Windows uses `\`, Unix/Mac use `/`. Cross-platform path handling solves the **portability problem** - code that works everywhere!

### Why Cross-Platform Paths Matter

**Problem**: Hardcoded paths break on different OSes:
```python
# BREAKS on Mac/Linux!
path = "C:\\Users\\Alice\\data.txt"  # Windows-only!

# BREAKS on Windows!
path = "/Users/Alice/data.txt"  # Unix-only!
```

**Solution**: Use `os.path.join()` for portability:
```python
# WORKS everywhere!
import os
path = os.path.join("Users", "Alice", "data.txt")
# Windows: Users\Alice\data.txt
# Unix: Users/Alice/data.txt
```

**This is platform abstraction** - same code, different platforms!

### Historical Context

**File paths from Unix** (1971): Hierarchical file systems with `/` as separator. **DOS** (1981) chose `\` to avoid conflict with command-line switches (`/help`). **Mistake**: Created decades of compatibility problems!

**`os.path` module** (Python 1.x, 1991): Abstracts platform differences. **`pathlib`** (Python 3.4, 2014): Modern object-oriented path handling - cleaner API than `os.path`!

**Why backslash?** DOS designer Tim Paterson chose `\` because `/` already used for switches. **Windows still pays** for this 1981 decision - most programming languages expect `/`!

### Real-World Analogies

**File paths like postal addresses**:
- **Absolute path**: Full address from country down to house
- **Relative path**: Directions from current location
- **Platform separator**: Different countries, different formats
**Your code should work in any "country"!**

**Or like GPS navigation**:
```python
# Absolute: Full coordinates
"/Users/Alice/Documents/file.txt"

# Relative: From current position
"../Documents/file.txt"
```

**Or like building directories**:
- **Windows**: Building\Floor\Room (backslash)
- **Unix**: Building/Floor/Room (forward slash)
**Same structure, different notation!**

---
### Types of Paths

**Absolute Path**: Full path from root
```python
# Windows
"C:\\Users\\Alice\\Documents\\file.txt"

# Mac/Linux
"/Users/Alice/Documents/file.txt"
```

**Relative Path**: Path from current directory
```python
"file.txt"  # Current directory
"data/file.txt"  # Subdirectory
"../file.txt"  # Parent directory
```

## The os.path Module

```python
import os

# Join paths (cross-platform)
path = os.path.join("folder", "file.txt")
# Windows: folder\file.txt
# Mac/Linux: folder/file.txt

# Get absolute path
abs_path = os.path.abspath("file.txt")
# /Users/Alice/project/file.txt

# Check if exists
exists = os.path.exists("file.txt")  # True/False

# Check if it's a file
is_file = os.path.isfile("file.txt")  # True/False

# Check if it's a directory
is_dir = os.path.isdir("folder")  # True/False

# Get filename from path
filename = os.path.basename("/path/to/file.txt")  # "file.txt"

# Get directory from path
dirname = os.path.dirname("/path/to/file.txt")  # "/path/to"

# Split path into parts
dir, file = os.path.split("/path/to/file.txt")
# dir: "/path/to", file: "file.txt"
```

## Examples

### Example 1: Build Path Safely

```python
import os

# Works on any OS
data_dir = "data"
filename = "users.txt"
filepath = os.path.join(data_dir, filename)

print(filepath)
# Windows: data\users.txt
# Mac/Linux: data/users.txt
```

### Example 2: Check Before Reading

```python
import os

filename = "config.txt"

if os.path.exists(filename):
    with open(filename, "r") as f:
        print(f.read())
else:
    print(f"{filename} not found!")
```

### Example 3: Find All .txt Files

```python
import os

for file in os.listdir("."):
    if os.path.isfile(file) and file.endswith(".txt"):
        print(f"Found text file: {file}")
```

## Key Takeaways

1. **os.path.join()**: Build paths safely
2. **os.path.exists()**: Check if path exists
3. **os.path.abspath()**: Get absolute path
4. **Cross-platform**: Works on any OS
5. **Always check**: Verify files exist before reading
