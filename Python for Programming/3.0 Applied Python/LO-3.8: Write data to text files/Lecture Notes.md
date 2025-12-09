# Lecture Notes: Write Text Files

## Writing Files

Save data to text files.


---

<div align="center">

![File folders and documents](https://images.unsplash.com/photo-1544396821-4dd40b938ad3?w=800&q=80)

*Python can read from and write to files on your system*

</div>

---
### Basic Syntax

```python
with open("filename.txt", "w") as file:
    file.write("content")
```

## Writing Modes

- **"w"**: Write (overwrites existing)
- **"a"**: Append (adds to end)
- **"x"**: Exclusive create (fails if exists)

## Examples

### Example 1: Write Text

```python
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is line 2\n")
```

### Example 2: Append Text

```python
with open("log.txt", "a") as f:
    f.write("New log entry\n")
```

### Example 3: Write List

```python
fruits = ["apple", "banana", "cherry"]

with open("fruits.txt", "w") as f:
    for fruit in fruits:
        f.write(fruit + "\n")
```

### Example 4: Save User Data

```python
name = input("Name: ")
age = input("Age: ")

with open("user.txt", "w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Age: {age}\n")
```

## Read and Write

```python
# Read existing
with open("data.txt", "r") as f:
    data = f.read()

# Process
data = data.upper()

# Write back
with open("data.txt", "w") as f:
    f.write(data)
```

## Key Takeaways

1. **"w" mode**: Write (overwrites)
2. **"a" mode**: Append (adds to end)
3. **write()**: Writes string
4. **with statement**: Auto closes
5. **\n**: Add newlines manually
