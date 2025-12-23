# Lecture Notes: Iterating Through Lists Using Loops

## Iterating Through Lists Using Loops

Master the art of processing list data efficiently using Python's iteration tools.

---

<div align="center">

![Circular pattern representing loops](https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=800&q=80)

*Loops allow you to repeat operations efficiently*

</div>

---

### Key Concepts

1. **for Loop**: Python's primary iteration tool
2. **enumerate()**: Access index and value simultaneously
3. **range()**: Iterate with indices
4. **zip()**: Combine multiple lists
5. **Loop Control**: break, continue statements
6. **Common Patterns**: Accumulation, filtering, transformation, search

## Basic Syntax

```python
# Basic for loop
for item in list_name:
    # Process each item

# With enumerate (index + value)
for index, item in enumerate(list_name):
    # Process with index

# With range (indices only)
for i in range(len(list_name)):
    # Access list_name[i]

# With zip (multiple lists)
for item1, item2 in zip(list1, list2):
    # Process pairs
```

---

## Examples

### Example 1: Basic Iteration

```python
# Print all items
fruits = ["apple", "banana", "cherry", "date"]

print("Available fruits:")
for fruit in fruits:
    print(f"- {fruit}")

# Output:
# Available fruits:
# - apple
# - banana
# - cherry
# - date
```

### Example 2: Calculate Statistics

```python
# Calculate sum and average
test_scores = [85, 92, 78, 95, 88, 76, 90, 84]

total = 0
count = 0

for score in test_scores:
    total += score
    count += 1

average = total / count

print(f"Total students: {count}")
print(f"Total points: {total}")
print(f"Average score: {average:.2f}")
print(f"Highest score: {max(test_scores)}")
print(f"Lowest score: {min(test_scores)}")

# Output:
# Total students: 8
# Total points: 688
# Average score: 86.00
# Highest score: 95
# Lowest score: 76
```

### Example 3: Using enumerate()

```python
# Numbered list with positions
tasks = ["Buy groceries", "Finish homework", "Call dentist", "Go for run"]

print("Today's Tasks:")
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")

# Output:
# Today's Tasks:
# 1. Buy groceries
# 2. Finish homework
# 3. Call dentist
# 4. Go for run
```

```python
# Find position of specific item
students = ["Alice", "Bob", "Charlie", "David", "Eve"]
search_name = "Charlie"

for i, student in enumerate(students):
    if student == search_name:
        print(f"{search_name} is at position {i} (or #{i+1} in the class)")
        break
# Output: Charlie is at position 2 (or #3 in the class)
```

### Example 4: Using range() for Modification

```python
# Modify list elements
prices = [10.00, 20.00, 15.00, 30.00, 25.00]

print("Original prices:", prices)

# Apply 10% discount
for i in range(len(prices)):
    prices[i] = prices[i] * 0.9  # 10% off

print("After 10% discount:", prices)

# Output:
# Original prices: [10.0, 20.0, 15.0, 30.0, 25.0]
# After 10% discount: [9.0, 18.0, 13.5, 27.0, 22.5]
```

### Example 5: Using zip() with Multiple Lists

```python
# Combine related data
students = ["Alice", "Bob", "Charlie", "David"]
math_scores = [85, 92, 78, 95]
english_scores = [88, 84, 90, 87]

print("Student Report Cards:")
print("-" * 40)

for student, math, english in zip(students, math_scores, english_scores):
    average = (math + english) / 2
    print(f"{student:10} | Math: {math:3} | English: {english:3} | Avg: {average:.1f}")

# Output:
# Student Report Cards:
# ----------------------------------------
# Alice      | Math:  85 | English:  88 | Avg: 86.5
# Bob        | Math:  92 | English:  84 | Avg: 88.0
# Charlie    | Math:  78 | English:  90 | Avg: 84.0
# David      | Math:  95 | English:  87 | Avg: 91.0
```

### Example 6: Filtering Data

```python
# Filter based on conditions
ages = [15, 22, 17, 30, 19, 14, 25, 18, 16, 21]

minors = []
adults = []

for age in ages:
    if age < 18:
        minors.append(age)
    else:
        adults.append(age)

print(f"Minors (< 18): {minors}")
print(f"Adults (>= 18): {adults}")
print(f"Total minors: {len(minors)}")
print(f"Total adults: {len(adults)}")

# Output:
# Minors (< 18): [15, 17, 19, 14, 16]
# Adults (>= 18): [22, 30, 25, 18, 21]
# Total minors: 5
# Total adults: 5
```

### Example 7: Building New Lists (Transformation)

```python
# Transform data
temperatures_celsius = [0, 10, 20, 30, 40]
temperatures_fahrenheit = []

for temp_c in temperatures_celsius:
    temp_f = (temp_c * 9/5) + 32
    temperatures_fahrenheit.append(temp_f)

print("Celsius to Fahrenheit Conversion:")
for c, f in zip(temperatures_celsius, temperatures_fahrenheit):
    print(f"{c}°C = {f}°F")

# Output:
# Celsius to Fahrenheit Conversion:
# 0°C = 32.0°F
# 10°C = 50.0°F
# 20°C = 68.0°F
# 30°C = 86.0°F
# 40°C = 104.0°F
```

### Example 8: Search with break

```python
# Find first match
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]
prices = [999.99, 25.50, 79.99, 299.99, 89.99]

budget = 100.00

print(f"Products under ${budget}:")
found = False

for i, product in enumerate(products):
    if prices[i] < budget:
        print(f"- {product}: ${prices[i]}")
        found = True

if not found:
    print("No products found within budget")

# Output:
# Products under $100.0:
# - Mouse: $25.5
# - Keyboard: $79.99
# - Headphones: $89.99
```

### Example 9: Skip with continue

```python
# Process only valid data
sensor_readings = [23.5, -999, 24.1, 23.8, -999, 25.0, 24.3]
# -999 represents sensor error

valid_readings = []

for reading in sensor_readings:
    if reading == -999:
        continue  # Skip error readings
    valid_readings.append(reading)

if valid_readings:
    average = sum(valid_readings) / len(valid_readings)
    print(f"Valid readings: {valid_readings}")
    print(f"Average temperature: {average:.2f}°C")
else:
    print("No valid readings")

# Output:
# Valid readings: [23.5, 24.1, 23.8, 25.0, 24.3]
# Average temperature: 24.14°C
```

### Example 10: Nested Lists (2D Data)

```python
# Process 2D data (list of lists)
gradebook = [
    ["Alice", 85, 90, 88],
    ["Bob", 92, 88, 95],
    ["Charlie", 78, 85, 80]
]

print("Student Averages:")
print("-" * 30)

for student_data in gradebook:
    name = student_data[0]
    scores = student_data[1:]  # Get all scores except name

    average = sum(scores) / len(scores)
    print(f"{name:10} | Average: {average:.2f}")

# Output:
# Student Averages:
# ------------------------------
# Alice      | Average: 87.67
# Bob        | Average: 91.67
# Charlie    | Average: 81.00
```

---

## Common Patterns

### Pattern 1: Accumulation (Sum, Product, Count)

```python
# Sum pattern
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")  # Sum: 150

# Product pattern
numbers = [2, 3, 4, 5]
product = 1
for num in numbers:
    product *= num
print(f"Product: {product}")  # Product: 120

# Count pattern
words = ["apple", "banana", "apricot", "cherry", "avocado"]
a_count = 0
for word in words:
    if word.startswith('a'):
        a_count += 1
print(f"Words starting with 'a': {a_count}")  # 3
```

### Pattern 2: Find Maximum/Minimum

```python
# Find maximum with position
scores = [78, 92, 85, 95, 88]

max_score = scores[0]
max_index = 0

for i, score in enumerate(scores):
    if score > max_score:
        max_score = score
        max_index = i

print(f"Highest score: {max_score} at position {max_index}")
# Output: Highest score: 95 at position 3
```

### Pattern 3: Filter and Collect

```python
# Collect items matching criteria
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
odds = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

print(f"Evens: {evens}")  # [2, 4, 6, 8, 10]
print(f"Odds: {odds}")    # [1, 3, 5, 7, 9]
```

### Pattern 4: Transform and Map

```python
# Transform each element
names = ["alice", "bob", "charlie"]
capitalized = []

for name in names:
    capitalized.append(name.title())

print(capitalized)  # ['Alice', 'Bob', 'Charlie']
```

### Pattern 5: Parallel Processing

```python
# Process multiple related lists
item_names = ["Apple", "Banana", "Cherry"]
quantities = [5, 3, 8]
prices = [1.20, 0.50, 2.00]

print("Shopping Receipt:")
print("-" * 35)

total_cost = 0

for name, qty, price in zip(item_names, quantities, prices):
    cost = qty * price
    total_cost += cost
    print(f"{name:10} x{qty} @ ${price:.2f} = ${cost:.2f}")

print("-" * 35)
print(f"{'Total:':10}              ${total_cost:.2f}")

# Output:
# Shopping Receipt:
# -----------------------------------
# Apple      x5 @ $1.20 = $6.00
# Banana     x3 @ $0.50 = $1.50
# Cherry     x8 @ $2.00 = $16.00
# -----------------------------------
# Total:                  $23.50
```

---

## Best Practices

1. **Choose the right loop type**
   - Use `for item in list` when you only need values
   - Use `enumerate()` when you need both index and value
   - Use `range(len(list))` when you need to modify elements
   - Use `zip()` for parallel lists

2. **Use descriptive variable names**
   ```python
   # Good
   for student in students:
       print(student)

   # Avoid
   for x in students:
       print(x)
   ```

3. **Avoid modifying list size during iteration**
   ```python
   # Bad - can cause issues
   for item in items:
       if condition:
           items.remove(item)  # Dangerous!

   # Good - create new list
   filtered = []
   for item in items:
       if condition:
           filtered.append(item)
   ```

4. **Use break for early exit**
   ```python
   # Stop when found
   for item in items:
       if item == target:
           print("Found!")
           break
   ```

5. **Use continue to skip**
   ```python
   # Skip invalid data
   for value in values:
       if value < 0:
           continue
       process(value)
   ```

---

## Common Mistakes

1. **Mistake 1: Modifying list while iterating**
   ```python
   # Wrong
   numbers = [1, 2, 3, 4, 5]
   for num in numbers:
       numbers.remove(num)  # Causes issues!

   # Correct
   numbers = [1, 2, 3, 4, 5]
   numbers_copy = numbers.copy()
   for num in numbers_copy:
       numbers.remove(num)
   ```

2. **Mistake 2: Forgetting to initialize accumulator**
   ```python
   # Wrong
   for num in numbers:
       total += num  # Error: total not defined

   # Correct
   total = 0
   for num in numbers:
       total += num
   ```

3. **Mistake 3: Using wrong index with enumerate**
   ```python
   # Wrong
   for i, item in enumerate(items):
       print(items[i])  # Works but unnecessary

   # Correct
   for i, item in enumerate(items):
       print(item)  # Use item directly
   ```

4. **Mistake 4: Assuming lists have same length with zip**
   ```python
   # Be aware: zip stops at shortest list
   list1 = [1, 2, 3, 4, 5]
   list2 = [10, 20, 30]

   for a, b in zip(list1, list2):
       print(a, b)
   # Only prints 3 pairs, not 5!
   ```

---

## Performance Tips

1. **Avoid repeated len() calls**
   ```python
   # Less efficient
   for i in range(len(items)):
       if i < len(items) - 1:  # len() called every iteration
           ...

   # Better
   n = len(items)
   for i in range(n):
       if i < n - 1:
           ...
   ```

2. **Use built-in functions when possible**
   ```python
   # Slower
   total = 0
   for num in numbers:
       total += num

   # Faster
   total = sum(numbers)
   ```

3. **List comprehensions (preview)**
   ```python
   # Traditional loop
   squares = []
   for num in numbers:
       squares.append(num ** 2)

   # List comprehension (faster, more Pythonic)
   squares = [num ** 2 for num in numbers]
   ```

---

## Key Takeaways

1. **for loop** is Python's primary iteration tool for lists
2. **enumerate()** provides index and value together
3. **range()** useful for index-based access and modification
4. **zip()** combines multiple lists elegantly
5. **break** exits loop early, **continue** skips to next iteration
6. Common patterns: accumulation, filtering, transformation, search
7. Always initialize accumulators before loops
8. Avoid modifying list structure during iteration
9. Choose appropriate loop style for your needs
10. Use descriptive variable names for readability
