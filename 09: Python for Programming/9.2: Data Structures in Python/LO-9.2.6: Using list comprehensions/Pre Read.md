## Pre-Read: Using List Comprehensions

## What Are List Comprehensions?

List comprehensions are Python's **one-liner magic** for creating lists - like using a formula instead of manual calculation!

### Simple Analogy

Think of list comprehensions like **a factory machine**:
- **Traditional loop**: Manually take each raw material, process it, put in output box (slow!)
- **Comprehension**: Feed raw materials into machine, get processed items out (fast!)
- **Same result**: Processed items, but comprehension is elegant and quick

Or like **Excel formulas**:
- **Manual**: Type value in each cell one by one (tedious!)
- **Formula**: Write once, applies to all cells (=A1*2, drag down)
- **Comprehension**: Same idea for Python lists!

### Why Comprehensions Rock

**Readability**: Clear intent - "create list of squares"
**Speed**: 2-3x faster than loops (optimized internally)
**Pythonic**: Professional Python code uses them everywhere

**Before comprehensions existed** (Python 1.x), programmers had to write verbose loops. **After** (Python 2.0+), one clean line does it all!

### What You'll Learn

List comprehensions are a concise way to create lists in Python - transforming loops into single, elegant lines.

### Why It Matters

Without comprehensions:
```python
squares = []
for x in range(5):
    squares.append(x ** 2)
# 4 lines, verbose
```

With comprehensions:
```python
squares = [x ** 2 for x in range(5)]
# 1 line, clear intent
```

### Basic Syntax

**Pattern:**
```python
[expression for item in iterable]
```

**Examples:**
```python
# Numbers 0-4
nums = [x for x in range(5)]
# [0, 1, 2, 3, 4]

# Squares
squares = [x ** 2 for x in range(5)]
# [0, 1, 4, 9, 16]

# Uppercase strings
words = ['hello', 'world']
upper = [w.upper() for w in words]
# ['HELLO', 'WORLD']
```

### Adding Filters

Add `if` at the end to filter:

```python
# Only even numbers
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Only long words
words = ['a', 'bat', 'elephant']
long = [w for w in words if len(w) > 3]
# ['elephant']
```

### if-else for Transformation

Use conditional expression to transform all elements:

```python
# Categorize as even/odd
types = ['even' if x % 2 == 0 else 'odd' for x in range(4)]
# ['even', 'odd', 'even', 'odd']

# Replace negatives with zero
nums = [5, -2, 8, -1]
positive = [x if x > 0 else 0 for x in nums]
# [5, 0, 8, 0]
```

### Key Differences

**Filter (omits items):**
```python
[x for x in list if condition]
# Some items removed
```

**Transform (keeps all):**
```python
[x if cond else y for x in list]
# All items kept, some changed
```

### Common Use Cases

**Extract data:**
```python
users = [{'name': 'Alice'}, {'name': 'Bob'}]
names = [u['name'] for u in users]
# ['Alice', 'Bob']
```

**Process strings:**
```python
data = "10,20,30"
numbers = [int(x) for x in data.split(',')]
# [10, 20, 30]
```

**Calculate:**
```python
prices = [10, 20, 30]
with_tax = [p * 1.08 for p in prices]
# [10.8, 21.6, 32.4]
```

### Benefits

1. **Concise** - One line vs multiple
2. **Faster** - Optimized internally
3. **Readable** - Clear intent
4. **Pythonic** - Preferred style

### Try to Predict

```python
result = [x * 3 for x in range(4) if x % 2 != 0]
```

What is `result`?

Answer: `[3, 9]`
- range(4) gives [0, 1, 2, 3]
- Filter odd: [1, 3]
- Multiply by 3: [3, 9]

List comprehensions = concise + powerful!
