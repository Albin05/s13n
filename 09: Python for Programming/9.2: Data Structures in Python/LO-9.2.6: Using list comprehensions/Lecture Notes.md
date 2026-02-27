## Using List Comprehensions

---

<div align="center">

![Python List Comprehension Syntax Diagram](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.2/LO-9.2.6.png)

*Overview of data structure types including sequences and collections, showing how list comprehensions transform one collection into another*

</div>

---

## Introduction

List comprehensions introduce **declarative programming** to Python - expressing **what** you want rather than **how** to get it. This represents a paradigm shift from imperative (step-by-step instructions) to declarative (describe the goal) programming.

### Why Comprehensions Are Revolutionary

**Imperative approach** (traditional):
```python
result = []
for x in range(10):
    if x % 2 == 0:
        result.append(x ** 2)
# 4 lines, focuses on HOW
```

**Declarative approach** (comprehension):
```python
result = [x**2 for x in range(10) if x%2==0]
# 1 line, focuses on WHAT
```

**Historical note**: List comprehensions came from functional programming languages (Haskell's list comprehensions, 1990). Python added them in version 2.0 (2000), making functional programming accessible to mainstream developers.

### Real-World Analogy

List comprehensions are like **a coffee order**:
- **Traditional loop**: "Go to machine, get cup, add coffee, add milk, add sugar, stir, hand to me"
- **Comprehension**: "Grande latte with 2 sugars" (describe what you want!)
- **Result**: Same coffee, cleaner communication

Or like **SQL queries**:
- **Loop**: Manually check each database row, collect matches
- **SQL**: "SELECT * FROM users WHERE age > 18" (what, not how!)
- **Comprehension**: Same idea for lists!

### The Mathematical Notation

List comprehensions mirror **set-builder notation** from mathematics:
- **Math**: {x² | x ∈ ℕ, x < 10}
- **Python**: [x**2 for x in range(10)]
- **Read both as**: "x-squared for each x in the set"

This makes Python feel natural for mathematical/scientific computing!

### Performance Benefits

Comprehensions are **faster** than equivalent loops:
- **Optimized**: Python knows the pattern, can optimize execution
- **C-speed**: Internal implementation in C (faster than Python bytecode loops)
- **Memory**: Efficient allocation (knows size upfront when possible)

**Benchmark**: Comprehensions typically 2-3x faster than append loops!

### Basic Syntax

```python
# Pattern: [expression for item in iterable]

# Create list
numbers = [x for x in range(5)]
# [0, 1, 2, 3, 4]

# Transform elements
squares = [x ** 2 for x in range(5)]
# [0, 1, 4, 9, 16]

# From existing list
words = ['hello', 'world']
upper = [w.upper() for w in words]
# ['HELLO', 'WORLD']
```

---

### Filtering with if

```python
# Pattern: [expression for item in iterable if condition]

# Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Filter and transform
numbers = [1, 2, 3, 4, 5]
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
# [4, 16]

# String filtering
words = ['a', 'bat', 'cat', 'elephant']
long_words = [w for w in words if len(w) > 3]
# ['elephant']
```

---

### Conditional Expression (if-else)

```python
# Pattern: [true_expr if condition else false_expr for item in iterable]

# Categorize
types = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
# ['even', 'odd', 'even', 'odd', 'even']

# Replace negatives
values = [5, -2, 8, -7]
positive = [x if x > 0 else 0 for x in values]
# [5, 0, 8, 0]

# Cap maximum
scores = [85, 105, 92]
capped = [s if s <= 100 else 100 for s in scores]
# [85, 100, 92]
```

**Key Difference:**
- Filtering: `[x for x in list if condition]` - omits elements
- Conditional: `[x if cond else y for x in list]` - keeps all, transforms

---

### Nested Comprehensions

```python
# 2D list creation
matrix = [[i*3 + j for j in range(3)] for i in range(3)]
# [[0, 1, 2],
#  [3, 4, 5],
#  [6, 7, 8]]

# Flattening
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6]

# Cartesian product
colors = ['red', 'blue']
sizes = ['S', 'M']
products = [(c, s) for c in colors for s in sizes]
# [('red', 'S'), ('red', 'M'), ('blue', 'S'), ('blue', 'M')]
```

---

### With zip() and enumerate()

```python
# Parallel lists with zip()
names = ['Alice', 'Bob']
scores = [85, 92]

pairs = [(n, s) for n, s in zip(names, scores)]
# [('Alice', 85), ('Bob', 92)]

# With calculation
totals = [p * q for p, q in zip([10, 20], [2, 3])]
# [20, 60]

# With enumerate()
items = ['a', 'b', 'c']
indexed = [(i, item) for i, item in enumerate(items)]
# [(0, 'a'), (1, 'b'), (2, 'c')]

numbered = [f"{i+1}. {item}" for i, item in enumerate(items)]
# ['1. a', '2. b', '3. c']
```

---

### Common Patterns

**Extract from Dictionaries:**
```python
users = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30}
]

names = [u['name'] for u in users]
# ['Alice', 'Bob']

adults = [u for u in users if u['age'] >= 25]
# [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
```

**String Operations:**
```python
# Split and process
data = "10,20,30"
numbers = [int(x) for x in data.split(',')]
# [10, 20, 30]

# First letters
words = ['apple', 'banana', 'cherry']
initials = [w[0].upper() for w in words]
# ['A', 'B', 'C']
```

**Mathematical:**
```python
# Temperature conversion
celsius = [0, 10, 20, 30]
fahrenheit = [c * 9/5 + 32 for c in celsius]
# [32.0, 50.0, 68.0, 86.0]

# Fibonacci extension
fibs = [0, 1]
fibs.extend([fibs[i-1] + fibs[i-2] for i in range(2, 10)])
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

### Comparison: Loop vs Comprehension

```python
# Traditional loop
squares = []
for x in range(5):
    if x % 2 == 0:
        squares.append(x ** 2)

# Comprehension - one line
squares = [x ** 2 for x in range(5) if x % 2 == 0]

# Both give: [0, 4, 16]
```

---

### Best Practices

**Good - Simple and Clear:**
```python
squares = [x ** 2 for x in range(10)]
evens = [x for x in numbers if x % 2 == 0]
upper = [s.upper() for s in strings]
```

**Avoid - Too Complex:**
```python
# Hard to read
result = [
    x * y + z if x > y else y * z 
    for x in range(10) 
    for y in range(10) 
    for z in range(10) 
    if x + y > 5
]

# Better - use regular loop for complex logic
```

---

### Quick Reference

```python
# Basic
[x for x in range(5)]                    # [0, 1, 2, 3, 4]
[x * 2 for x in range(5)]                # [0, 2, 4, 6, 8]

# Filter
[x for x in range(10) if x % 2 == 0]    # [0, 2, 4, 6, 8]

# Transform + Filter
[x ** 2 for x in range(10) if x % 2]    # [1, 9, 25, 49, 81]

# Conditional
[x if x > 0 else 0 for x in [-1, 2]]    # [0, 2]

# Nested
[x for row in matrix for x in row]       # Flatten

# With zip
[(a, b) for a, b in zip(l1, l2)]        # Pairs
```

**Remember:**
- Comprehensions create new lists
- Faster than traditional loops
- Keep them simple and readable
- Use regular loops for complex logic
