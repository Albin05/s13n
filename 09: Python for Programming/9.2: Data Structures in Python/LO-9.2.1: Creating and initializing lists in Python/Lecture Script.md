## Creating and Initializing Lists in Python

### Hook (2 minutes)

**Scenario:**
You're building a shopping app and need to store a user's cart items. Or tracking daily temperatures for a week. Managing student grades for a class. Collecting user responses in a survey.

All these scenarios require storing multiple related values. You could create separate variables:

```python
temp_monday = 72
temp_tuesday = 75
temp_wednesday = 68
temp_thursday = 71
temp_friday = 73
temp_saturday = 76
temp_sunday = 74
```

But this is tedious, error-prone, and doesn't scale. What if you need to track 365 days?

**Enter lists** - Python's most versatile data structure for storing ordered collections of items.

**What You'll Learn:**
1. Create empty lists and lists with initial values
2. Understand list syntax and structure
3. Create lists with different data types
4. Use list() constructor
5. Create lists from strings and ranges
6. Build nested lists for multi-dimensional data

---

### Section 1: Creating Empty Lists (3 minutes)

**Method 1: Square Brackets**

```python
# Empty list using []
shopping_cart = []
print(shopping_cart)  # []
print(type(shopping_cart))  # <class 'list'>
```

**Method 2: list() Constructor**

```python
# Empty list using list()
tasks = list()
print(tasks)  # []
print(type(tasks))  # <class 'list'>
```

**When to Use Each:**
- `[]` - Most common, concise, preferred
- `list()` - Useful for converting other types to lists

**Checking if Empty:**

```python
cart = []

if cart:
    print("Cart has items")
else:
    print("Cart is empty")
# Output: Cart is empty

# Or explicitly check length
if len(cart) == 0:
    print("No items")
# Output: No items
```

---

### Section 2: Creating Lists with Initial Values (4 minutes)

**List Literals:**

```python
# List of integers
scores = [85, 92, 78, 95, 88]
print(scores)  # [85, 92, 78, 95, 88]

# List of strings
fruits = ['apple', 'banana', 'orange', 'grape']
print(fruits)  # ['apple', 'banana', 'orange', 'grape']

# List of floats
prices = [19.99, 29.99, 9.99, 49.99]
print(prices)  # [19.99, 29.99, 9.99, 49.99]

# List of booleans
flags = [True, False, True, True]
print(flags)  # [True, False, True, True]
```

**Mixed Data Types:**

```python
# Lists can contain different types
student = ['Alice', 21, 3.8, True]
print(student)
# ['Alice', 21, 3.8, True]
# Name, age, GPA, is_enrolled
```

**Single Element Lists:**

```python
# Single element (note the comma is optional but clear)
single = [42]
print(single)  # [42]
print(len(single))  # 1
```

**Lists with Duplicates:**

```python
# Duplicates are allowed
numbers = [1, 2, 2, 3, 3, 3, 4]
print(numbers)  # [1, 2, 2, 3, 3, 3, 4]
print(len(numbers))  # 7
```

---

### Section 3: Creating Lists from Other Sequences (3 minutes)

**From Strings:**

```python
# Convert string to list of characters
word = "Python"
letters = list(word)
print(letters)
# ['P', 'y', 't', 'h', 'o', 'n']

# Split string into list of words
sentence = "Hello world from Python"
words = sentence.split()
print(words)
# ['Hello', 'world', 'from', 'Python']

# Split with custom delimiter
csv_data = "apple,banana,orange"
fruits = csv_data.split(',')
print(fruits)
# ['apple', 'banana', 'orange']
```

**From Range:**

```python
# Create list from range
numbers = list(range(5))
print(numbers)  # [0, 1, 2, 3, 4]

# Range with start and stop
evens = list(range(2, 11, 2))
print(evens)  # [2, 4, 6, 8, 10]

# Countdown
countdown = list(range(10, 0, -1))
print(countdown)
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

**From Tuples:**

```python
# Convert tuple to list
coordinates = (10, 20, 30)
coord_list = list(coordinates)
print(coord_list)  # [10, 20, 30]
```

---

### Section 4: Nested Lists (3 minutes)

**2D Lists (Lists of Lists):**

```python
# Matrix (2D list)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Access rows
print(matrix[0])  # [1, 2, 3]
print(matrix[1])  # [4, 5, 6]

# Access elements
print(matrix[0][0])  # 1
print(matrix[1][2])  # 6
print(matrix[2][1])  # 8
```

**Practical Example - Student Grades:**

```python
# Each inner list: [name, math, science, english]
students = [
    ['Alice', 85, 90, 88],
    ['Bob', 78, 82, 86],
    ['Charlie', 92, 89, 94]
]

# Access student data
print(students[0])  # ['Alice', 85, 90, 88]
print(students[0][0])  # 'Alice'
print(students[0][1])  # 85 (math score)

# Calculate average for first student
math, sci, eng = students[0][1], students[0][2], students[0][3]
average = (math + sci + eng) / 3
print(f"Alice's average: {average}")  # 87.67
```

**Jagged Lists (Uneven Nested Lists):**

```python
# Not all sublists need same length
shopping_lists = [
    ['milk', 'eggs', 'bread'],
    ['apples', 'bananas'],
    ['chicken', 'rice', 'beans', 'cheese']
]

for i, items in enumerate(shopping_lists):
    print(f"List {i+1} has {len(items)} items: {items}")
# List 1 has 3 items: ['milk', 'eggs', 'bread']
# List 2 has 2 items: ['apples', 'bananas']
# List 3 has 4 items: ['chicken', 'rice', 'beans', 'cheese']
```

---

### Section 5: Special List Creation Patterns (2 minutes)

**Repeated Elements:**

```python
# Create list with repeated values
zeros = [0] * 5
print(zeros)  # [0, 0, 0, 0, 0]

# Repeated strings
dashes = ['-'] * 10
print(dashes)
# ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']

# Repeated lists (be careful!)
matrix = [[0] * 3] * 3  # DON'T DO THIS!
print(matrix)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Problem: All rows reference same list
matrix[0][0] = 1
print(matrix)
# [[1, 0, 0], [1, 0, 0], [1, 0, 0]]  # All rows changed!

# Correct way (covered in comprehensions later)
matrix = [[0] * 3 for _ in range(3)]
matrix[0][0] = 1
print(matrix)
# [[1, 0, 0], [0, 0, 0], [0, 0, 0]]  # Only first row changed
```

**Concatenation:**

```python
# Combine lists with +
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]

# Multiple lists
odds = [1, 3, 5]
evens = [2, 4, 6]
tens = [10, 20, 30]
all_numbers = odds + evens + tens
print(all_numbers)
# [1, 3, 5, 2, 4, 6, 10, 20, 30]
```

---

### Section 6: Practical Applications (3 minutes)

**Application 1: Temperature Tracking**

```python
# Week of temperatures
temperatures = [72, 75, 68, 71, 73, 76, 74]

print(f"Temperatures for the week: {temperatures}")
print(f"Number of days: {len(temperatures)}")

# Find average temperature
average_temp = sum(temperatures) / len(temperatures)
print(f"Average temperature: {average_temp:.1f}°F")
# Average temperature: 72.7°F
```

**Application 2: Shopping Cart**

```python
# Items with prices
cart = [
    ['Laptop', 999.99],
    ['Mouse', 29.99],
    ['Keyboard', 79.99],
    ['Monitor', 299.99]
]

print("Shopping Cart:")
total = 0
for item in cart:
    name, price = item[0], item[1]
    print(f"  {name}: ${price}")
    total += price

print(f"\nTotal: ${total}")
# Total: $1409.96
```

**Application 3: Survey Responses**

```python
# Collect responses
responses = []

# Simulate adding responses
responses = [5, 4, 5, 3, 4, 5, 4, 5, 3, 5]

print(f"Total responses: {len(responses)}")

# Count 5-star ratings
five_stars = responses.count(5)
print(f"5-star ratings: {five_stars}")

# Calculate satisfaction rate
satisfaction_rate = (five_stars / len(responses)) * 100
print(f"Satisfaction rate: {satisfaction_rate}%")
# Satisfaction rate: 50.0%
```

**Application 4: Course Schedule**

```python
# Days and times for classes
schedule = [
    ['Monday', '9:00 AM', 'Math'],
    ['Monday', '11:00 AM', 'English'],
    ['Tuesday', '10:00 AM', 'Science'],
    ['Wednesday', '9:00 AM', 'Math'],
    ['Thursday', '2:00 PM', 'History'],
    ['Friday', '10:00 AM', 'Science']
]

print("Weekly Schedule:")
for class_info in schedule:
    day, time, subject = class_info
    print(f"{day} at {time}: {subject}")
```

---

### Summary (1 minute)

**Key Concepts Covered:**

1. **Creating Empty Lists:**
   - `[]` - preferred
   - `list()` - constructor

2. **Lists with Values:**
   - `[1, 2, 3]` - direct initialization
   - Can hold any type
   - Duplicates allowed
   - Order matters

3. **From Other Types:**
   - `list(string)` - characters
   - `string.split()` - words
   - `list(range(n))` - numbers
   - `list(tuple)` - from tuple

4. **Nested Lists:**
   - Lists within lists
   - Access with multiple indices
   - 2D matrices, tables

5. **Special Patterns:**
   - `[0] * 5` - repeated elements
   - `list1 + list2` - concatenation

**Quick Reference:**

```python
# Empty
empty = []
empty = list()

# With values
numbers = [1, 2, 3, 4, 5]
mixed = ['text', 42, True, 3.14]

# From range
nums = list(range(1, 11))  # 1-10

# From string
chars = list("hello")
words = "a b c".split()

# Nested
matrix = [[1, 2], [3, 4]]

# Repeated
zeros = [0] * 10

# Combined
result = [1, 2] + [3, 4]
```

**Remember:**
- Lists are mutable (can be changed)
- Lists are ordered (maintain sequence)
- Lists allow duplicates
- Lists can contain any type
- Use `len()` for size
- Use `[]` for creation (most common)

**Next Steps:**
- Learn list indexing (accessing elements)
- Master list slicing (extracting portions)
- Explore list methods (append, insert, remove)
- Practice with real data

Lists are the foundation of Python data structures - master them!
