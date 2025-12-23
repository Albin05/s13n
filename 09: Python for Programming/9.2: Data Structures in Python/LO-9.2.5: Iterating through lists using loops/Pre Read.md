# Pre-Read: Iterating Through Lists Using Loops

## What You'll Learn
In this lesson, you'll learn how to iterate through lists using loops - one of the most fundamental and powerful operations in Python programming.

## Why This Matters
Looping through lists is essential for:
- Processing every student's grade in a class
- Analyzing temperature data from sensors
- Displaying all products in a shopping cart
- Validating form inputs from users
- Calculating statistics (sum, average, max, min)
- Transforming data (converting, filtering, mapping)

Almost every real-world program needs to process collections of data, making list iteration a critical skill.

---

## What is List Iteration?

**Iteration** means going through each item in a list one by one and performing some operation.

```python
fruits = ["apple", "banana", "cherry"]

# Visit each fruit and print it
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry
```

---

## The for Loop - Most Common Method

The `for` loop is Python's primary way to iterate through lists:

```python
for item in list_name:
    # Do something with item
```

### Basic Example

```python
scores = [85, 92, 78, 95, 88]

for score in scores:
    print(f"Score: {score}")
# Output:
# Score: 85
# Score: 92
# Score: 78
# Score: 95
# Score: 88
```

**How it works:**
1. Loop takes the first item from the list
2. Assigns it to the variable (`score`)
3. Executes the indented code block
4. Repeats for the next item
5. Stops when all items are processed

---

## Processing Items While Iterating

### Calculate Sum

```python
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print(f"Sum: {total}")  # Sum: 150
```

### Find Maximum

```python
scores = [85, 92, 78, 95, 88]
highest = scores[0]

for score in scores:
    if score > highest:
        highest = score

print(f"Highest score: {highest}")  # Highest score: 95
```

### Count Specific Items

```python
grades = ["A", "B", "A", "C", "A", "B"]
a_count = 0

for grade in grades:
    if grade == "A":
        a_count += 1

print(f"Number of A's: {a_count}")  # Number of A's: 3
```

---

## Using enumerate() for Index and Value

Sometimes you need both the index (position) and the value:

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry
```

**Use cases:**
- Displaying numbered lists
- Tracking positions
- Modifying items by index

```python
# Start counting from 1 instead of 0
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
# Output:
# 1. apple
# 2. banana
# 3. cherry
```

---

## Using range() with Indices

Access items by index using `range()`:

```python
colors = ["red", "green", "blue"]

for i in range(len(colors)):
    print(f"Index {i}: {colors[i]}")
# Output:
# Index 0: red
# Index 1: green
# Index 2: blue
```

**When to use this pattern:**
- Need to modify list items
- Need to access multiple lists simultaneously
- Need precise index control

### Modifying List Items

```python
numbers = [1, 2, 3, 4, 5]

# Double each number
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)  # [2, 4, 6, 8, 10]
```

---

## Iterating Through Multiple Lists Together

Use `zip()` to iterate through multiple lists simultaneously:

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Output:
# Alice: 85
# Bob: 92
# Charlie: 78
```

**Practical example:**

```python
products = ["Laptop", "Mouse", "Keyboard"]
prices = [999.99, 25.50, 79.99]
quantities = [1, 2, 1]

for product, price, quantity in zip(products, prices, quantities):
    total = price * quantity
    print(f"{product}: ${price} x {quantity} = ${total:.2f}")
# Output:
# Laptop: $999.99 x 1 = $999.99
# Mouse: $25.50 x 2 = $51.00
# Keyboard: $79.99 x 1 = $79.99
```

---

## Real-World Examples

### Example 1: Grade Calculator

```python
grades = [85, 92, 78, 95, 88, 76, 90]

total = 0
count = 0

for grade in grades:
    total += grade
    count += 1

average = total / count
print(f"Average grade: {average:.2f}")  # Average grade: 86.29
```

### Example 2: Temperature Analysis

```python
temperatures = [72, 75, 68, 70, 73, 69, 71]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Weekly Temperature Report:")
for day, temp in zip(days, temperatures):
    print(f"{day}: {temp}°F")

# Find hottest day
hottest_temp = temperatures[0]
hottest_day = days[0]

for i in range(len(temperatures)):
    if temperatures[i] > hottest_temp:
        hottest_temp = temperatures[i]
        hottest_day = days[i]

print(f"\nHottest day: {hottest_day} ({hottest_temp}°F)")
```

### Example 3: Shopping Cart Total

```python
cart_items = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [999.99, 25.50, 79.99, 299.99]

print("Shopping Cart:")
total = 0

for i, item in enumerate(cart_items):
    price = prices[i]
    print(f"{i+1}. {item}: ${price:.2f}")
    total += price

print(f"\nTotal: ${total:.2f}")
# Output:
# Shopping Cart:
# 1. Laptop: $999.99
# 2. Mouse: $25.50
# 3. Keyboard: $79.99
# 4. Monitor: $299.99
#
# Total: $1405.47
```

### Example 4: Data Validation

```python
user_ages = [25, 17, 30, 15, 22, 19]

valid_ages = []
invalid_ages = []

for age in user_ages:
    if age >= 18:
        valid_ages.append(age)
    else:
        invalid_ages.append(age)

print(f"Valid ages (18+): {valid_ages}")
print(f"Invalid ages: {invalid_ages}")
# Output:
# Valid ages (18+): [25, 30, 22, 19]
# Invalid ages: [17, 15]
```

---

## Building New Lists While Iterating

```python
numbers = [1, 2, 3, 4, 5]

# Create a list of squares
squares = []
for num in numbers:
    squares.append(num ** 2)

print(squares)  # [1, 4, 9, 16, 25]
```

```python
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(evens)  # [2, 4, 6, 8, 10]
```

---

## While Loops with Lists (Less Common)

You can also use `while` loops, though `for` loops are preferred:

```python
fruits = ["apple", "banana", "cherry"]
i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1
# Output:
# apple
# banana
# cherry
```

**When to use while loops:**
- Processing list while removing items
- Need more complex loop control
- Condition-based iteration

---

## Common Patterns

### Pattern 1: Accumulation (Sum, Product)

```python
prices = [19.99, 5.50, 12.00, 8.75]
total = 0

for price in prices:
    total += price

print(f"Total: ${total:.2f}")  # Total: $46.24
```

### Pattern 2: Filtering

```python
scores = [45, 78, 92, 65, 88, 73, 95]
passing_scores = []

for score in scores:
    if score >= 70:
        passing_scores.append(score)

print(passing_scores)  # [78, 92, 88, 73, 95]
```

### Pattern 3: Transformation

```python
names = ["alice", "bob", "charlie"]
capitalized = []

for name in names:
    capitalized.append(name.capitalize())

print(capitalized)  # ['Alice', 'Bob', 'Charlie']
```

### Pattern 4: Search

```python
students = ["Alice", "Bob", "Charlie", "David"]
target = "Charlie"

found = False
for student in students:
    if student == target:
        found = True
        break

if found:
    print(f"{target} is in the list")
else:
    print(f"{target} not found")
```

---

## Break and Continue in Loops

### break - Exit Loop Early

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Find first number greater than 5
for num in numbers:
    if num > 5:
        print(f"Found: {num}")
        break  # Stop searching
# Output: Found: 6
```

### continue - Skip to Next Iteration

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print only odd numbers
for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)
# Output: 1, 3, 5, 7, 9
```

---

## Try It Yourself (Before Class)

Run this code:

```python
# Example 1: Basic iteration
colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(f"I like {color}")

# Example 2: Calculate sum
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")

# Example 3: With enumerate
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# Example 4: With zip
students = ["Alice", "Bob", "Charlie"]
grades = [85, 92, 78]
for student, grade in zip(students, grades):
    print(f"{student}: {grade}")
```

**Questions:**
1. What gets printed in each example?
2. How would you find the average of the numbers list?
3. How would you print only fruits that start with 'a'?
4. Can you modify the grades example to show pass/fail (70+ is pass)?

---

## Key Takeaways

Before class, remember:
1. **for loop is primary tool** - `for item in list:`
2. **enumerate()** - get both index and value
3. **range(len(list))** - when you need indices
4. **zip()** - iterate multiple lists together
5. **break/continue** - control loop flow
6. **Common patterns** - accumulation, filtering, transformation, search

## What's Next?

In the live session, we'll:
- Practice all iteration patterns
- Build complex data processing programs
- Combine loops with conditionals
- Use nested loops for 2D data
- Learn about list comprehensions (advanced iteration)
- Optimize loop performance

See you in class!
