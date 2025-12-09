# Pre-Read: Use Context Managers

## Context Managers

Context managers ensure proper resource cleanup using the `with` statement:

```python
# Without context manager (manual cleanup)
file = open("data.txt", "r")
content = file.read()
file.close()  # Must remember to close

# With context manager (automatic cleanup)
with open("data.txt", "r") as file:
    content = file.read()
# File automatically closed after the block
```

## Why Use Context Managers

```python
# Problem: File not closed if error occurs
try:
    file = open("data.txt", "r")
    content = file.read()
    # If error happens here, file stays open
    process(content)
finally:
    file.close()

# Solution: with statement handles cleanup automatically
with open("data.txt", "r") as file:
    content = file.read()
    process(content)
# File always closed, even if error occurs
```

## Common Context Managers

```python
# File handling
with open("file.txt", "w") as f:
    f.write("Hello, World!")

# Multiple files
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    content = infile.read()
    outfile.write(content.upper())
```
