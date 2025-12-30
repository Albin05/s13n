## Accessing List Elements Using Indexing

### Positive Indexing

```python
fruits = ['apple', 'banana', 'orange']
#          0        1         2

first = fruits[0]   # 'apple'
second = fruits[1]  # 'banana'
last = fruits[2]    # 'orange'

# Or using length
last = fruits[len(fruits) - 1]
```

**Key Points:**
- Indices start at 0
- First: index 0
- Last: index length-1
- Out of bounds raises IndexError

---

### Negative Indexing

```python
items = [10, 20, 30, 40, 50]
#        -5  -4  -3  -2  -1

last = items[-1]         # 50
second_last = items[-2]  # 40
first = items[-5]        # 10
```

**Benefits:**
- Access from end without knowing length
- `-1` always gets last element
- Clean and readable

---

### Nested Lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

row = matrix[0]      # [1, 2, 3]
element = matrix[0][1]  # 2
last = matrix[-1][-1]   # 6
```

**Pattern:**
- `matrix[row][col]`
- First index: row
- Second index: column

---

### Error Handling

```python
numbers = [1, 2, 3]

# Safe access
try:
    value = numbers[10]
except IndexError:
    value = None

# Check bounds
if 0 <= index < len(numbers):
    value = numbers[index]
```

---

### Finding Elements

```python
items = ['a', 'b', 'c']

# Check existence
if 'b' in items:
    print("Found")

# Get index
index = items.index('b')  # 1

# Safe find
try:
    idx = items.index('d')
except ValueError:
    idx = -1
```

---

### Quick Reference

```python
lst = ['a', 'b', 'c', 'd', 'e']

# Positive
lst[0]    # First
lst[2]    # Third
lst[4]    # Last

# Negative
lst[-1]   # Last
lst[-2]   # Second to last

# Nested
m = [[1,2], [3,4]]
m[0][1]   # 2

# Find
'b' in lst          # True
lst.index('c')      # 2
len(lst)            # 5
```

**Remember:**
- 0-based indexing
- Negative from end
- Bounds checking important
- Nested: multiple brackets
