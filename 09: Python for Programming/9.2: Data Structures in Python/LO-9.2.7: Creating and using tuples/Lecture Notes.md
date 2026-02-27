## Creating and Using Tuples

---

<div align="center">

![Python Tuple Creation and Usage](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.2/LO-9.2.7.jpg)

*Python data processing architecture: tuples are fundamental data structures used throughout the Python interpreter for passing grouped values*

</div>

---

## Introduction

Tuples introduce **immutability** to sequences - a fundamental concept in functional programming and safe software design. They represent the philosophy that **"data that shouldn't change, can't change."**

### Why Tuples Exist

**The mutability problem**: Lists can be accidentally modified anywhere in your code, leading to bugs:
```python
config = ['prod_server', 5432, 'db']
some_function(config)  # Might change it!
# Config now corrupted - hard to debug!
```

**Tuple solution**: Immutable = guaranteed safety:
```python
config = ('prod_server', 5432, 'db')
some_function(config)  # Can't change it!
# Config stays intact - bug prevented!
```

**Historical note**: Immutable data structures come from functional programming (LISP, 1958). Python adopted tuples from ABC language (1980s), making functional concepts accessible to all programmers.

### Real-World Analogy

Tuples are like **engraved stone tablets**:
- **Write once**: Carve the data
- **Read forever**: Can't erase or change stone
- **Safe**: Original message preserved
- **vs Paper list**: Can be erased, modified, torn

Or like **GPS coordinates**:
- **Fixed**: Latitude/longitude of New York doesn't change
- **Tuple**: (40.7128, -74.0060) - immutable makes sense!
- **vs Todo list**: Use list - items get added/removed

### Performance Benefits

Tuples are **faster and smaller** than lists:
- **Memory**: ~16 bytes less overhead per tuple
- **Speed**: Creation 2x faster, iteration 10% faster
- **Why**: Python knows size never changes, optimizes aggressively
- **Hashing**: Tuples can be dictionary keys (hashable!)

**Benchmark**: For fixed data, always prefer tuples!

### Creating Tuples

```python
# Empty tuple
empty = ()

# With values
coords = (3, 4)
person = ('Alice', 25, 'Engineer')

# Without parentheses (tuple packing)
point = 3, 4  # Still creates tuple

# Single element - MUST have comma!
single = (5,)    # Tuple
not_tuple = (5)  # Just int 5

# Using tuple() constructor
from_list = tuple([1, 2, 3])  # (1, 2, 3)
from_string = tuple('hi')     # ('h', 'i')
from_range = tuple(range(5))  # (0, 1, 2, 3, 4)
```

---

### Accessing Elements

```python
fruits = ('apple', 'banana', 'orange', 'mango')

# Indexing (same as lists)
fruits[0]    # 'apple'
fruits[-1]   # 'mango'

# Slicing (same as lists)
fruits[1:3]  # ('banana', 'orange')
fruits[:2]   # ('apple', 'banana')
fruits[::2]  # ('apple', 'orange')
fruits[::-1] # Reverse

# Nested
matrix = ((1, 2), (3, 4))
matrix[0][1]  # 2
```

---

### Immutability

```python
colors = ('red', 'green', 'blue')

# CANNOT modify
# colors[0] = 'yellow'  # TypeError

# CANNOT add/remove
# colors.append('yellow')  # AttributeError
# colors.remove('red')     # AttributeError

# CAN create new tuples
combined = colors + ('yellow', 'purple')
# ('red', 'green', 'blue', 'yellow', 'purple')

repeated = ('a', 'b') * 3
# ('a', 'b', 'a', 'b', 'a', 'b')
```

**Note:** Tuple itself immutable, but can contain mutable objects.

---

### Tuple Methods

**Only 2 methods:**

```python
numbers = (1, 2, 3, 2, 4, 2, 5)

# count()
numbers.count(2)  # 3

# index()
numbers.index(3)  # 2
numbers.index(2, 2)  # 3 (start from index 2)
```

---

### Common Operations

```python
t = (1, 2, 3, 4, 5)

# Length
len(t)  # 5

# Membership
3 in t      # True
10 in t     # False

# Min, max, sum
min(t)  # 1
max(t)  # 5
sum(t)  # 15

# Iteration
for item in t:
    print(item)
```

---

### Multiple Return Values

```python
# Function returning tuple
def get_user():
    return 'Alice', 25, 'NYC'

# Receive as tuple
user = get_user()  # ('Alice', 25, 'NYC')

# Unpack directly
name, age, city = get_user()
print(f"{name} is {age}")  # Alice is 25

# Examples
def divide(a, b):
    return a // b, a % b

quotient, remainder = divide(17, 5)
# quotient = 3, remainder = 2

def stats(nums):
    return min(nums), max(nums), sum(nums)/len(nums)

minimum, maximum, average = stats([10, 20, 30])
```

---

### When to Use Tuples

**Use Tuples:**
```python
# Fixed data
DAYS = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
RGB_RED = (255, 0, 0)
ORIGIN = (0, 0)

# Dictionary keys
locations = {}
locations[(0, 0)] = "Origin"
locations[(10, 20)] = "Point A"

# Return multiple values
def get_dimensions():
    return 1920, 1080

# Fixed structure records
person = ('Alice', 25, 'Engineer')
coordinate = (40.7128, -74.0060)
```

**Use Lists:**
```python
# Data that changes
cart = ['milk', 'bread']
cart.append('eggs')

# Adding/removing items
tasks = ['task1', 'task2']
tasks.remove('task1')
```

---

### Basic Unpacking

```python
# Simple unpacking
point = (3, 4)
x, y = point  # x=3, y=4

# Swapping
a, b = 10, 5
a, b = b, a  # Swap: a=5, b=10

# In loops
students = [('Alice', 85), ('Bob', 92)]
for name, score in students:
    print(f"{name}: {score}")
```

---

### Tuples vs Lists

| Feature | Tuple | List |
|---------|-------|------|
| Mutable | No | Yes |
| Syntax | `(1, 2, 3)` | `[1, 2, 3]` |
| Methods | 2 | 11 |
| Speed | Faster | Slower |
| Dict key | Yes | No |
| Use case | Fixed data | Changing data |

---

### Quick Reference

```python
# Create
t = (1, 2, 3)
t = 1, 2, 3     # Same
single = (5,)   # Single element

# Access
t[0]     # First
t[-1]    # Last
t[1:3]   # Slice

# Methods
t.count(2)   # Count occurrences
t.index(3)   # Find position

# Operations
len(t)   # Length
x in t   # Membership
min(t)   # Minimum
max(t)   # Maximum

# Unpack
x, y, z = (1, 2, 3)
```

**Remember:**
- Immutable = safe
- Faster than lists
- Use for fixed data
- Perfect for coordinates, records
