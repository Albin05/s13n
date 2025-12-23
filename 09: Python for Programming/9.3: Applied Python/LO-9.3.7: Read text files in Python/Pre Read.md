# Pre-Read: Read Text Files

## Reading Files

Access data stored in text files.

```python
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
```

## Better Way: Using `with`

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# File closes automatically!
```

## Why Read Files?

1. **Persistent data**: Data survives program restart
2. **Large datasets**: Process data from files
3. **Configuration**: Read settings from files

## Basic Example

```python
with open("names.txt", "r") as f:
    for line in f:
        print(line.strip())
```
