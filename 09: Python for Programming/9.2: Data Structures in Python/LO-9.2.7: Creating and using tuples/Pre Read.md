## Pre-Read: Creating and Using Tuples

### What You'll Learn

Tuples are immutable sequences - like lists that can't be changed after creation.

### Why It Matters

Lists are great when data changes:
```python
cart = ['milk', 'bread']
cart.append('eggs')  # Can modify
```

But sometimes data shouldn't change:
```python
coordinates = (3, 4)  # Fixed point
# coordinates[0] = 5  # Error - can't change!
```

### Creating Tuples

**Basic syntax:**
```python
# With parentheses
point = (3, 4)
person = ('Alice', 25, 'Engineer')

# Without parentheses
coords = 3, 4  # Still creates tuple!

# Empty tuple
empty = ()
```

**Important - Single element:**
```python
# WRONG - not a tuple!
not_tuple = (5)  # This is just int 5

# RIGHT - need comma
single = (5,)  # This is a tuple
```

### Accessing Elements

Same as lists:
```python
fruits = ('apple', 'banana', 'orange')

# Indexing
fruits[0]    # 'apple'
fruits[-1]   # 'orange'

# Slicing
fruits[1:3]  # ('banana', 'orange')
fruits[:2]   # ('apple', 'banana')
```

### Immutability

Cannot modify after creation:
```python
colors = ('red', 'green', 'blue')

# This will ERROR
# colors[0] = 'yellow'  # TypeError!
# colors.append('purple')  # AttributeError!
```

But can create new tuples:
```python
# Concatenation
colors1 = ('red', 'green')
colors2 = ('blue', 'yellow')
all_colors = colors1 + colors2
# ('red', 'green', 'blue', 'yellow')
```

### Tuple Methods

Only 2 methods (vs 11 for lists):
```python
numbers = (1, 2, 3, 2, 4, 2)

# count() - how many times
numbers.count(2)  # 3

# index() - find position
numbers.index(3)  # 2
```

### Multiple Return Values

Functions often return tuples:
```python
def get_name_age():
    return 'Alice', 25  # Returns tuple

# Unpack the result
name, age = get_name_age()
print(f"{name} is {age}")  # Alice is 25
```

### When to Use Tuples

**Use Tuple:**
- Data shouldn't change
- Fixed coordinates (3, 4)
- RGB colors (255, 0, 0)
- Database records
- Dictionary keys

**Use List:**
- Data will change
- Adding/removing items
- Shopping cart
- To-do list

### Lists vs Tuples

| Aspect | Tuple | List |
|--------|-------|------|
| Change? | No | Yes |
| Speed | Faster | Slower |
| Memory | Less | More |
| Syntax | `(1,2,3)` | `[1,2,3]` |

### Try to Predict

```python
t = (10, 20, 30)
a, b, c = t

# What are a, b, c?
```

Answer:
- a = 10
- b = 20
- c = 30

This is called "unpacking"!

Tuples = immutable, safe, fast!
