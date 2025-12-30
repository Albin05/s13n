## Lecture Script: Iterating Through Lists Using Loops

**Duration:** 18 minutes

---

### Hook (2 minutes)

"You have a list of 100 student names and need to print each one with a greeting. Or maybe you have a list of prices and need to calculate which ones are above $50. Or perhaps you need to process temperature readings from the last 30 days. What do all these tasks have in common? Iteration - the ability to process each element in a list.

Iteration is how you bring lists to life. A list sitting there is just data. But when you loop through it, applying logic to each element, you turn static data into dynamic processing. You can filter, transform, analyze, or take action on every item.

Today, we'll master list iteration in Python. You'll learn multiple ways to loop through lists - from basic for loops to advanced techniques with enumerate() and zip(). By the end, you'll be processing lists efficiently and elegantly, whether you're handling 10 items or 10,000."

---

### Section 1: Basic For Loop Iteration (3 minutes)

**Iterating Directly Over Elements:**

```python
# Simple iteration
fruits = ['apple', 'banana', 'orange', 'mango']

for fruit in fruits:
    print(fruit)
# apple
# banana
# orange
# mango

# Processing each element
prices = [10.99, 25.50, 5.75, 100.00]

for price in prices:
    print(f"${price:.2f}")
# $10.99
# $25.50
# $5.75
# $100.00

# Conditional processing
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

**Accumulating Results:**

```python
# Sum all elements
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print(total)  # 150

# Build new list
numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
    squares.append(num ** 2)

print(squares)  # [1, 4, 9, 16, 25]

# Count matching elements
grades = [85, 92, 78, 90, 88, 76, 95, 82]
passing = 0

for grade in grades:
    if grade >= 80:
        passing += 1

print(f"Passing students: {passing}")  # 6
```

**Finding Elements:**

```python
# Find first match
numbers = [12, 45, 23, 78, 34, 89, 56]
target = 78
found = False

for num in numbers:
    if num == target:
        found = True
        break

print(f"Found: {found}")  # True

# Find maximum
numbers = [12, 45, 23, 78, 34, 89, 56]
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print(f"Maximum: {maximum}")  # 89
```

---

### Section 2: Using enumerate() (3 minutes)

**Getting Index and Value:**

```python
# Basic enumerate
fruits = ['apple', 'banana', 'orange']

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: orange

# Start counting from 1
fruits = ['apple', 'banana', 'orange']

for num, fruit in enumerate(fruits, start=1):
    print(f"{num}. {fruit}")
# 1. apple
# 2. banana
# 3. orange
```

**Practical Applications:**

```python
# Modify specific indices
grades = [78, 85, 92, 88, 76]

for i, grade in enumerate(grades):
    if grade < 80:
        grades[i] = 80  # Curve to minimum 80
        print(f"Curved grade at position {i}: {grade} → {grades[i]}")

print(grades)  # [80, 85, 92, 88, 80]

# Find positions of matching elements
items = ['apple', 'banana', 'apple', 'orange', 'apple']
apple_positions = []

for index, item in enumerate(items):
    if item == 'apple':
        apple_positions.append(index)

print(apple_positions)  # [0, 2, 4]

# Create index-value mapping
words = ['hello', 'world', 'python']
word_map = {}

for i, word in enumerate(words):
    word_map[i] = word

print(word_map)  # {0: 'hello', 1: 'world', 2: 'python'}
```

**Parallel Processing:**

```python
# Process with both index and value
students = ['Alice', 'Bob', 'Charlie', 'Diana']
scores = [85, 92, 78, 88]

for i, student in enumerate(students):
    print(f"{i+1}. {student}: {scores[i]}")
# 1. Alice: 85
# 2. Bob: 92
# 3. Charlie: 78
# 4. Diana: 88
```

---

### Section 3: While Loop Iteration (2 minutes)

**Index-Based Iteration:**

```python
# Basic while loop
fruits = ['apple', 'banana', 'orange', 'mango']
i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1
# apple
# banana
# orange
# mango

# Skip elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
i = 0

while i < len(numbers):
    print(numbers[i])
    i += 2  # Skip every other element
# 1
# 3
# 5
# 7
```

**Conditional Termination:**

```python
# Stop when condition met
numbers = [10, 20, 30, 40, 50, 60, 70]
i = 0

while i < len(numbers) and numbers[i] < 50:
    print(numbers[i])
    i += 1
# 10
# 20
# 30
# 40

# Search with early exit
items = ['apple', 'banana', 'orange', 'mango']
target = 'orange'
i = 0

while i < len(items):
    if items[i] == target:
        print(f"Found {target} at index {i}")
        break
    i += 1
# Found orange at index 2
```

---

### Section 4: Iterating with zip() (3 minutes)

**Parallel Iteration:**

```python
# Combine two lists
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 85
# Bob: 92
# Charlie: 78

# Three or more lists
first_names = ['Alice', 'Bob', 'Charlie']
last_names = ['Smith', 'Jones', 'Brown']
ages = [25, 30, 22]

for first, last, age in zip(first_names, last_names, ages):
    print(f"{first} {last}, age {age}")
# Alice Smith, age 25
# Bob Jones, age 30
# Charlie Brown, age 22
```

**Creating Pairs and Dictionaries:**

```python
# Create dictionary from two lists
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'NYC']

person = {}
for key, value in zip(keys, values):
    person[key] = value

print(person)  # {'name': 'Alice', 'age': 25, 'city': 'NYC'}

# Or use dict() constructor
person = dict(zip(keys, values))

# Create list of tuples
products = ['laptop', 'mouse', 'keyboard']
prices = [999, 29, 79]

cart = list(zip(products, prices))
print(cart)  # [('laptop', 999), ('mouse', 29), ('keyboard', 79)]
```

**Handling Different Lengths:**

```python
# zip stops at shortest list
names = ['Alice', 'Bob', 'Charlie', 'Diana']
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 85
# Bob: 92
# Charlie: 78
# Diana is skipped

# Use itertools.zip_longest for longest
from itertools import zip_longest

names = ['Alice', 'Bob', 'Charlie', 'Diana']
scores = [85, 92, 78]

for name, score in zip_longest(names, scores, fillvalue=0):
    print(f"{name}: {score}")
# Alice: 85
# Bob: 92
# Charlie: 78
# Diana: 0
```

---

### Section 5: Modifying Lists While Iterating (3 minutes)

**Safe Modification Patterns:**

```python
# WRONG - Don't modify while iterating
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # BAD - can skip elements
# Result may be unpredictable

# RIGHT - Iterate over copy
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:  # Create copy with [:]
    if num % 2 == 0:
        numbers.remove(num)

print(numbers)  # [1, 3, 5]

# RIGHT - Use list comprehension instead
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]
print(numbers)  # [1, 3, 5]
```

**Modifying Elements (Safe):**

```python
# Modify elements by index - SAFE
prices = [10.00, 20.00, 30.00, 40.00]

for i in range(len(prices)):
    prices[i] = prices[i] * 1.1  # 10% increase

print(prices)  # [11.0, 22.0, 33.0, 44.0]

# Using enumerate - SAFE
grades = [75, 82, 68, 91, 79]

for i, grade in enumerate(grades):
    if grade < 80:
        grades[i] = 80  # Curve to minimum

print(grades)  # [80, 82, 80, 91, 80]
```

**Building New Lists:**

```python
# Filter and transform - create new list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = []

for num in numbers:
    if num % 2 == 0:
        even_squares.append(num ** 2)

print(even_squares)  # [4, 16, 36, 64, 100]

# Or use list comprehension
even_squares = [num ** 2 for num in numbers if num % 2 == 0]
```

---

### Section 6: Nested Lists and 2D Iteration (2 minutes)

**Iterating Through 2D Lists:**

```python
# Matrix iteration
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Iterate rows
for row in matrix:
    print(row)
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

# Iterate all elements
for row in matrix:
    for element in matrix:
        print(element, end=' ')
    print()  # New line after each row
# 1 2 3
# 4 5 6
# 7 8 9

# With indices
for i, row in enumerate(matrix):
    for j, element in enumerate(row):
        print(f"matrix[{i}][{j}] = {element}")
# matrix[0][0] = 1
# matrix[0][1] = 2
# ...
```

**Practical 2D Examples:**

```python
# Student grades by subject
grades = [
    [85, 90, 78],  # Alice
    [92, 88, 95],  # Bob
    [78, 82, 80]   # Charlie
]

students = ['Alice', 'Bob', 'Charlie']

# Calculate averages
for i, student_grades in enumerate(grades):
    avg = sum(student_grades) / len(student_grades)
    print(f"{students[i]}: {avg:.1f}")
# Alice: 84.3
# Bob: 91.7
# Charlie: 80.0
```

---

### Section 7: Loop Control (1 minute)

**break and continue:**

```python
# break - exit loop early
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num > 5:
        break
    print(num)
# 1 2 3 4 5

# continue - skip to next iteration
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)
# 1 3 5 7 9

# else clause - executes if loop completes normally
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num > 10:
        print("Found large number")
        break
else:
    print("No large numbers found")
# No large numbers found
```

---

### Summary (1 minute)

Today we mastered list iteration in Python:

**Basic Iteration:**
- `for item in list:` - Direct iteration over elements
- `for i in range(len(list)):` - Index-based iteration
- `while i < len(list):` - While loop with index

**Advanced Techniques:**
- `enumerate(list)` - Get index and value together
- `enumerate(list, start=1)` - Custom starting index
- `zip(list1, list2)` - Iterate multiple lists in parallel

**Safe Modification:**
- Iterate over copy: `for item in list[:]:`
- Use indices: `for i in range(len(list)):`
- Build new list instead of modifying

**Control Flow:**
- `break` - Exit loop early
- `continue` - Skip to next iteration
- `for...else` - Execute if loop completes

**Remember:**
- Don't modify list while iterating directly over it
- Use enumerate() when you need indices
- Use zip() for parallel lists
- List comprehensions often cleaner than loops

Iteration is fundamental to working with lists. Master these patterns and you'll process data efficiently!
