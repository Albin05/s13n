## Iterating Through Lists Using Loops

## Introduction

List iteration represents the marriage of **data structures and control flow** - using loops to systematically process collections. This is where lists truly become powerful, enabling **batch processing** of data.

### Why Iteration Matters

**Single-item processing** (limited): Can only handle one piece of data at a time manually.
**Iteration** (powerful): Process thousands, millions, billions of items with the same code.

**Real-world impact**: Netflix processes millions of viewing records using iteration. Google searches billions of web pages. Your programs can work at scale using the same concept!

### Real-World Analogy

List iteration is like **an assembly line worker**:
- **Conveyor belt**: The list (items moving by)
- **Worker**: The loop (processes each item)
- **Same action**: Apply same operation to every item
- **Automatic**: Next item comes automatically

Or like **scanning groceries at checkout**:
- **Cart**: Your list
- **Scanner**: The loop
- **Each item**: Gets scanned (processed) one by one
- **Total**: Accumulated result (like sum/count)

### Python's Elegant Iteration

**C/Java way** (verbose):
```c
for (int i = 0; i < length; i++) {
    process(array[i]);  // Manual indexing
}
```

**Python way** (elegant):
```python
for item in list:
    process(item)  # Direct access!
```

This **direct iteration** makes Python code readable and less error-prone - no index mistakes!

### Basic For Loop

```python
# Iterate over elements
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)
# apple
# banana
# orange

# With conditional
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")

# Accumulate result
total = 0
for num in numbers:
    total += num
print(total)  # 15
```

**Pattern:**
- `for item in list:` - most common
- Direct access to element values
- Clean and readable

---

### Using enumerate()

```python
# Get index and value
fruits = ['apple', 'banana', 'orange']

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: orange

# Start from 1
for num, fruit in enumerate(fruits, start=1):
    print(f"{num}. {fruit}")
# 1. apple
# 2. banana
# 3. orange
```

**When to Use:**
- Need both index and value
- Modifying elements by index
- Finding positions of matches

**Modify by Index:**
```python
grades = [75, 82, 68]
for i, grade in enumerate(grades):
    if grade < 80:
        grades[i] = 80
# grades: [80, 82, 80]
```

---

### While Loop

```python
# Index-based iteration
fruits = ['apple', 'banana', 'orange']
i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1

# Conditional termination
numbers = [10, 20, 30, 40, 50]
i = 0

while i < len(numbers) and numbers[i] < 40:
    print(numbers[i])
    i += 1
# 10, 20, 30
```

**When to Use:**
- Need manual index control
- Conditional loop termination
- Variable step sizes

---

### Using zip()

```python
# Parallel iteration
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 85
# Bob: 92
# Charlie: 78

# Three or more lists
first = ['Alice', 'Bob']
last = ['Smith', 'Jones']
ages = [25, 30]

for f, l, a in zip(first, last, ages):
    print(f"{f} {l}, {a}")
# Alice Smith, 25
# Bob Jones, 30
```

**Key Points:**
- Stops at shortest list
- Perfect for related data
- Can zip 2+ lists

**Create Dictionary:**
```python
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'NYC']

person = dict(zip(keys, values))
# {'name': 'Alice', 'age': 25, 'city': 'NYC'}
```

---

### Safe Modification

**DON'T - Modify While Iterating:**
```python
# BAD - can skip elements
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # WRONG
```

**DO - Iterate Over Copy:**
```python
# GOOD - iterate over copy
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:
    if num % 2 == 0:
        numbers.remove(num)
# numbers: [1, 3, 5]
```

**DO - Use List Comprehension:**
```python
# BEST - create new list
numbers = [1, 2, 3, 4, 5]
numbers = [n for n in numbers if n % 2 != 0]
# numbers: [1, 3, 5]
```

**SAFE - Modify by Index:**
```python
# Safe to modify by index
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    numbers[i] *= 2
# numbers: [2, 4, 6, 8, 10]
```

---

### Nested Lists

```python
# 2D iteration
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Iterate rows
for row in matrix:
    print(row)
# [1, 2, 3]
# [4, 5, 6]

# Iterate all elements
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
# 1 2 3
# 4 5 6

# With indices
for i, row in enumerate(matrix):
    for j, element in enumerate(row):
        print(f"[{i}][{j}] = {element}")
```

---

### Loop Control

```python
# break - exit early
for num in [1, 2, 3, 4, 5]:
    if num > 3:
        break
    print(num)
# 1 2 3

# continue - skip iteration
for num in [1, 2, 3, 4, 5]:
    if num % 2 == 0:
        continue
    print(num)
# 1 3 5

# else clause
for num in [1, 2, 3]:
    if num > 10:
        break
else:
    print("No large numbers")
# No large numbers
```

---

### Quick Reference

```python
lst = ['a', 'b', 'c']

# Basic iteration
for item in lst:
    print(item)

# With index
for i, item in enumerate(lst):
    print(i, item)

# Start from 1
for i, item in enumerate(lst, start=1):
    print(i, item)

# Parallel lists
lst2 = [1, 2, 3]
for item1, item2 in zip(lst, lst2):
    print(item1, item2)

# By index
for i in range(len(lst)):
    print(lst[i])

# While loop
i = 0
while i < len(lst):
    print(lst[i])
    i += 1
```

**Remember:**
- Use `for item in list:` for simple iteration
- Use `enumerate()` when you need indices
- Use `zip()` for parallel lists
- Don't modify list while iterating over it
- Modify by index is safe
