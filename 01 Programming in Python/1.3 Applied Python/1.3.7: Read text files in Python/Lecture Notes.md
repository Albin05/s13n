# Lecture Notes: Read Text Files

## Reading Files

Access and process data from text files.


---

<div align="center">

![File folders and documents](https://images.unsplash.com/photo-1544396821-4dd40b938ad3?w=800&q=80)

*Python can read from and write to files on your system*

</div>

---
### Basic Syntax

```python
with open("filename.txt", "r") as file:
    content = file.read()
```

## Reading Methods

### read() - Entire File

```python
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
```

### readline() - One Line

```python
with open("data.txt", "r") as f:
    line = f.readline()
    print(line)
```

### readlines() - List of Lines

```python
with open("data.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
```

### Iterate Lines

```python
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())
```

## Why Use `with`?

```python
# Without with (manual close)
f = open("data.txt", "r")
content = f.read()
f.close()  # Must remember!

# With with (auto close)
with open("data.txt", "r") as f:
    content = f.read()
# Closes automatically!
```

## Real-World Examples

### Read Configuration

```python
with open("config.txt", "r") as f:
    for line in f:
        key, value = line.strip().split("=")
        print(f"{key}: {value}")
```

### Process CSV Data

```python
with open("scores.txt", "r") as f:
    for line in f:
        name, score = line.strip().split(",")
        print(f"{name}: {score}")
```

## Key Takeaways

1. **open()**: Opens file
2. **"r" mode**: Read mode
3. **with statement**: Auto closes file
4. **read()**: Entire content
5. **Iterate**: Process line by line
