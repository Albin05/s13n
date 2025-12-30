## Pre-Read: Iterating Through Lists Using Loops

### What You'll Learn

Iteration means processing each element in a list one by one. Essential for working with list data.

### Why It Matters

Without iteration:
- Can't process multiple elements
- Can't apply logic to each item
- Limited to manual access

With iteration:
- Process all elements automatically
- Apply transformations
- Calculate aggregates

### Basic For Loop

**Most Common Pattern:**
```python
fruits = ['apple', 'banana', 'orange']

for fruit in fruits:
    print(fruit)
# apple
# banana
# orange
```

**With Conditions:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
# 2 is even
# 4 is even
# 6 is even
# 8 is even
# 10 is even
```

### Getting Index with enumerate()

Sometimes you need both the position and the value:

```python
fruits = ['apple', 'banana', 'orange']

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: orange

# Start counting from 1
for position, fruit in enumerate(fruits, start=1):
    print(f"{position}. {fruit}")
# 1. apple
# 2. banana
# 3. orange
```

### Parallel Lists with zip()

Process multiple related lists together:

```python
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 85
# Bob: 92
# Charlie: 78
```

### Common Patterns

**Calculate Sum:**
```python
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print(total)  # 150
```

**Build New List:**
```python
numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
    squares.append(num ** 2)

print(squares)  # [1, 4, 9, 16, 25]
```

**Count Matches:**
```python
grades = [85, 92, 78, 90, 88]
passing = 0

for grade in grades:
    if grade >= 80:
        passing += 1

print(f"Passing: {passing}")  # 4
```

### Important: Don't Modify While Iterating

```python
# WRONG - unpredictable behavior
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # BAD!

# RIGHT - iterate over copy
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:
    if num % 2 == 0:
        numbers.remove(num)
```

### Try to Predict

```python
scores = [70, 85, 90, 75]
total = 0

for score in scores:
    total += score

average = total / len(scores)

# What is total?
# What is average?
```

Answers:
- total: `320`
- average: `80.0`

Iteration unlocks the power of lists!
