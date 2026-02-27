# Lecture Notes: Use List Comprehensions

## List Comprehensions

List comprehensions provide a concise, readable way to create lists based on existing sequences.


---

<div align="center">

![Python List Comprehension Syntax Diagram](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/LO-9.3.29.png)

*List comprehensions condense a for-loop pattern into a single expression for concise list creation*

</div>

---

## Introduction

List comprehensions implement **syntactic sugar** - elegant syntax for common list operations! This is **declarative programming** - describe **what** you want, not **how** to build it. Comprehensions are **functional programming** in Python - transform data streams concisely!

### Why List Comprehensions are Revolutionary

**Problem with traditional loops**: Verbose, imperative style:
```python
# VERBOSE - 4 lines for simple task!
squares = []
for i in range(10):
    squares.append(i ** 2)
# Boilerplate obscures intent!
```

**Solution with comprehensions**: Concise, declarative style:
```python
# ELEGANT - one line expresses intent!
squares = [i ** 2 for i in range(10)]
# "Map square function over range" - clear!
```

**This is expressive syntax** - code reads like English!

### Historical Context

**List comprehensions** inspired by **Haskell** (1990) and **mathematical set notation**! Mathematics writes: `{x² | x ∈ ℕ, x < 10}` (set of x² where x in naturals less than 10). **Python translates**: `[x**2 for x in range(10)]` - almost identical syntax!

**Added in Python 2.0** (2000) with **PEP 202**. **Guido van Rossum**: "List comprehensions are more concise than map/filter lambdas" - influenced by **functional programming** but with Python's readability!

**Performance advantage**: List comprehensions run in **C code** (CPython), faster than explicit Python loops! **Optimization** - Python pre-allocates list size when possible, avoiding repeated resizing.

### Real-World Analogies

**Comprehensions like assembly line**:
- **Traditional loop**: Process items one-by-one manually (slow)
- **Comprehension**: Set up automatic transformation pipeline (fast)
- **Output**: Transformed items collected automatically
**Factory automation vs manual work!**

**Or like SQL SELECT**:
```python
# SQL: SELECT name FROM students WHERE grade >= 80
# Python: [s["name"] for s in students if s["grade"] >= 80]
# Same declarative style!
```

**Or like mathematical functions**:
- **Math**: f(x) = x² for all x in domain
- **Python**: `[f(x) for x in domain]`
**Map mathematical transformations directly!**

### Comprehension vs map/filter

**Old functional style**: map() and filter():
```python
# Functional - verbose with lambda!
squares = list(map(lambda x: x**2, range(10)))
evens = list(filter(lambda x: x%2==0, range(10)))
```

**Comprehension style**: More Pythonic:
```python
# Pythonic - readable!
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x%2==0]
```

**Guido's preference**: Comprehensions over map/filter/lambda - **readability counts!**

---
### Syntax

```python
new_list = [expression for item in iterable]
new_list = [expression for item in iterable if condition]
```

## Basic List Comprehension

Traditional loop vs list comprehension:

```python
# Traditional approach
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List comprehension
squares = [i ** 2 for i in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## List Comprehension with Condition

Filter items while creating a new list:

```python
# Get even numbers from 0 to 19
evens = [n for n in range(20) if n % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Get numbers divisible by 3
divisible_by_3 = [n for n in range(30) if n % 3 == 0]
print(divisible_by_3)  # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

# Filter positive numbers
numbers = [-5, -2, 0, 3, 7, -1, 8]
positives = [n for n in numbers if n > 0]
print(positives)  # [3, 7, 8]
```

## Transforming Data

```python
# Convert strings to uppercase
names = ["alice", "bob", "charlie", "diana"]
upper_names = [name.upper() for name in names]
print(upper_names)  # ['ALICE', 'BOB', 'CHARLIE', 'DIANA']

# Get string lengths
words = ["hello", "world", "python", "programming"]
lengths = [len(word) for word in words]
print(lengths)  # [5, 5, 6, 11]

# Double each number
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print(doubled)  # [2, 4, 6, 8, 10]
```

## Real-World Examples

### Example 1: Processing Student Data

```python
students = [
    {"name": "Alice", "grade": 85, "age": 20},
    {"name": "Bob", "grade": 92, "age": 22},
    {"name": "Charlie", "grade": 78, "age": 21},
    {"name": "Diana", "grade": 95, "age": 20},
    {"name": "Eve", "grade": 88, "age": 23}
]

# Extract all grades
grades = [student["grade"] for student in students]
print(f"All grades: {grades}")
# All grades: [85, 92, 78, 95, 88]

# Get names of students who passed (grade >= 80)
passed_students = [student["name"] for student in students if student["grade"] >= 80]
print(f"Students who passed: {passed_students}")
# Students who passed: ['Alice', 'Bob', 'Diana', 'Eve']

# Get names of students aged 20
young_students = [student["name"] for student in students if student["age"] == 20]
print(f"Students aged 20: {young_students}")
# Students aged 20: ['Alice', 'Diana']

# Create formatted report strings
reports = [f"{s['name']}: {s['grade']}%" for s in students]
for report in reports:
    print(report)
# Alice: 85%
# Bob: 92%
# Charlie: 78%
# Diana: 95%
# Eve: 88%
```

### Example 2: Text Processing

```python
text = "Hello World! Python is amazing. Learn Python today."

# Split into words and convert to lowercase
words = text.split()
lowercase_words = [word.lower() for word in words]
print(lowercase_words)
# ['hello', 'world!', 'python', 'is', 'amazing.', 'learn', 'python', 'today.']

# Get words longer than 5 characters
long_words = [word for word in words if len(word) > 5]
print(long_words)
# ['Python', 'amazing.', 'Python']

# Remove punctuation from words
import string
cleaned_words = [word.strip(string.punctuation) for word in words]
print(cleaned_words)
# ['Hello', 'World', 'Python', 'is', 'amazing', 'Learn', 'Python', 'today']

# Get first letter of each word
initials = [word[0] for word in words if word]
print(initials)
# ['H', 'W', 'P', 'i', 'a', 'L', 'P', 't']

# Count vowels in each word
vowels = "aeiouAEIOU"
vowel_counts = [sum(1 for char in word if char in vowels) for word in words]
print(vowel_counts)
# [2, 1, 1, 1, 4, 2, 1, 2]
```

### Example 3: Number Processing

```python
# Generate multiplication table for 5
multiplication_table = [5 * i for i in range(1, 11)]
print("5's multiplication table:")
for i, result in enumerate(multiplication_table, 1):
    print(f"5 x {i} = {result}")
# 5 x 1 = 5
# 5 x 2 = 10
# ... up to 5 x 10 = 50

# Find perfect squares under 100
perfect_squares = [i ** 2 for i in range(1, 11)]
print(f"Perfect squares under 100: {perfect_squares}")
# Perfect squares under 100: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Generate Fahrenheit to Celsius conversions
fahrenheit_temps = [32, 68, 86, 104, 122]
celsius_temps = [(f - 32) * 5/9 for f in fahrenheit_temps]
print("Temperature conversions:")
for f, c in zip(fahrenheit_temps, celsius_temps):
    print(f"{f}°F = {c:.1f}°C")
# 32°F = 0.0°C
# 68°F = 20.0°C
# 86°F = 30.0°C
# 104°F = 40.0°C
# 122°F = 50.0°C

# Find numbers divisible by both 3 and 5
numbers = range(1, 101)
fizzbuzz_numbers = [n for n in numbers if n % 3 == 0 and n % 5 == 0]
print(f"Numbers divisible by both 3 and 5: {fizzbuzz_numbers}")
# Numbers divisible by both 3 and 5: [15, 30, 45, 60, 75, 90]
```

### Example 4: File and Path Processing

```python
# Process file names
files = ["document.txt", "image.png", "script.py", "data.csv", "photo.jpg"]

# Get only Python files
python_files = [f for f in files if f.endswith(".py")]
print(f"Python files: {python_files}")
# Python files: ['script.py']

# Get file names without extensions
names_only = [f.split(".")[0] for f in files]
print(f"File names: {names_only}")
# File names: ['document', 'image', 'script', 'data', 'photo']

# Get file extensions
extensions = [f.split(".")[-1] for f in files]
print(f"Extensions: {extensions}")
# Extensions: ['txt', 'png', 'py', 'csv', 'jpg']

# Create full paths
directory = "/home/user/documents"
full_paths = [f"{directory}/{file}" for file in files]
for path in full_paths:
    print(path)
# /home/user/documents/document.txt
# /home/user/documents/image.png
# /home/user/documents/script.py
# /home/user/documents/data.csv
# /home/user/documents/photo.jpg

# Filter image files
image_extensions = [".png", ".jpg", ".jpeg", ".gif"]
image_files = [f for f in files if any(f.endswith(ext) for ext in image_extensions)]
print(f"Image files: {image_files}")
# Image files: ['image.png', 'photo.jpg']
```

### Example 5: Nested List Comprehensions

```python
# Create a multiplication table (2D list)
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("Multiplication Table:")
for row in table:
    print(row)
# [1, 2, 3, 4, 5]
# [2, 4, 6, 8, 10]
# [3, 6, 9, 12, 15]
# [4, 8, 12, 16, 20]
# [5, 10, 15, 20, 25]

# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened: {flattened}")
# Flattened: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get all even numbers from a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
evens = [num for row in matrix for num in row if num % 2 == 0]
print(f"Even numbers: {evens}")
# Even numbers: [2, 4, 6, 8]

# Create coordinate pairs
coordinates = [(x, y) for x in range(3) for y in range(3)]
print("Coordinates:")
for coord in coordinates:
    print(coord)
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)
# (2, 0)
# (2, 1)
# (2, 2)

# Chess board squares
chess_squares = [f"{letter}{number}" for letter in "abcdefgh" for number in range(1, 9)]
print(f"First 10 chess squares: {chess_squares[:10]}")
# First 10 chess squares: ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2']
```

## Conditional Expressions in List Comprehensions

```python
# If-else in list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
categorized = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(categorized)
# ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']

# Replace negative numbers with 0
numbers = [-3, 5, -1, 8, -7, 2]
non_negative = [n if n >= 0 else 0 for n in numbers]
print(non_negative)
# [0, 5, 0, 8, 0, 2]
```

## Key Takeaways

1. **List comprehensions**: Concise syntax for creating lists
2. **Syntax**: `[expression for item in iterable if condition]`
3. **Filtering**: Use `if` condition to filter items
4. **Transformation**: Apply expression to transform items
5. **Readability**: More Pythonic than traditional loops
6. **Nested comprehensions**: Can create multi-dimensional lists
7. **Performance**: Generally faster than traditional loops
8. **Best practice**: Use for simple transformations, avoid complex logic
