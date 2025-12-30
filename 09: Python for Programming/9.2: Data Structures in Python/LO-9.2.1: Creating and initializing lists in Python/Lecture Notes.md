## Creating and Initializing Lists in Python

### Creating Empty Lists

```python
# Method 1: Square brackets (preferred)
empty = []

# Method 2: list() constructor
empty = list()

# Check if empty
if not empty:
    print("List is empty")
```

---

### Lists with Initial Values

```python
# Integers
numbers = [1, 2, 3, 4, 5]

# Strings
fruits = ['apple', 'banana', 'orange']

# Floats
prices = [19.99, 29.99, 9.99]

# Mixed types
student = ['Alice', 21, 3.8, True]

# Duplicates allowed
numbers = [1, 2, 2, 3, 3, 3]
```

---

### From Other Types

**From range:**
```python
nums = list(range(10))  # [0, 1, 2, ..., 9]
evens = list(range(2, 11, 2))  # [2, 4, 6, 8, 10]
```

**From strings:**
```python
# Characters
chars = list("hello")  # ['h', 'e', 'l', 'l', 'o']

# Words
words = "a b c".split()  # ['a', 'b', 'c']

# Custom delimiter
items = "x,y,z".split(',')  # ['x', 'y', 'z']
```

---

### Nested Lists

```python
# 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access
row = matrix[0]  # [1, 2, 3]
element = matrix[0][1]  # 2

# Student data
students = [
    ['Alice', 85, 90],
    ['Bob', 78, 82]
]
```

---

### Special Patterns

**Repeated elements:**
```python
zeros = [0] * 5  # [0, 0, 0, 0, 0]
```

**Concatenation:**
```python
list1 = [1, 2]
list2 = [3, 4]
combined = list1 + list2  # [1, 2, 3, 4]
```

---

### Quick Reference

```python
# Empty
empty = []

# With values
nums = [1, 2, 3]

# From range
nums = list(range(5))  # [0, 1, 2, 3, 4]

# From string
chars = list("abc")  # ['a', 'b', 'c']
words = "a b".split()  # ['a', 'b']

# Nested
matrix = [[1, 2], [3, 4]]

# Repeated
zeros = [0] * 10

# Combined
result = [1] + [2, 3]  # [1, 2, 3]
```

---

### Key Points

- Use `[]` for empty lists
- Lists are mutable and ordered
- Allow duplicates and mixed types
- `list(range(n))` for sequences
- `string.split()` for words
- Nested lists for tables/matrices
- `+` concatenates lists
- `*` repeats elements
