# Pre-Read: Handle File Paths

## Working with File Paths

Different operating systems use different path separators:
- Windows: `C:\\Users\\name\\file.txt`
- Mac/Linux: `/Users/name/file.txt`

## The os.path Module

Python's `os.path` handles paths correctly across platforms:

```python
import os

# Join paths (works on any OS)
path = os.path.join("folder", "subfolder", "file.txt")
print(path)
# Windows: folder\subfolder\file.txt
# Mac/Linux: folder/subfolder/file.txt
```

## Common Operations

```python
import os

# Check if file exists
if os.path.exists("data.txt"):
    print("File found!")

# Get absolute path
abs_path = os.path.abspath("file.txt")

# Get file name from path
filename = os.path.basename("/path/to/file.txt")  # "file.txt"
```

## Why Use os.path?

1. **Cross-platform**: Works on Windows, Mac, Linux
2. **Safer**: Handles special characters
3. **Convenient**: Many helpful functions
