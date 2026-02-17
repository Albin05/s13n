## Accessing List Elements Using Indexing

### Hook (2 minutes)

**Scenario:**
You have a list of 100 student names. You need to:
- Get the first student's name for an award
- Check the last student on the list
- Find the 50th student
- Access the 3rd student from the end

Without indexing, you'd have no way to access specific elements in your list!

```python
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
# How do I get 'Charlie'?
# How do I get the last name?
# How do I get from the end?
```

**Indexing** is your tool to access individual elements by their position.

**What You'll Learn:**
1. Access elements using positive indices
2. Use negative indices to count from the end
3. Handle index errors gracefully
4. Access elements in nested lists
5. Check element existence
6. Find element positions

---

### CS Theory Bite

> **Origin**: **Zero-based indexing** comes from **C** (1972) — the index represents memory offset from the start. Negative indexing (`-1` for last) is Python's elegant addition.
>
> **Analogy**: Indexing is like **apartment numbers** — each element has a unique address. Negative indices count from the back entrance.
>
> **Why it matters**: O(1) random access by index is what makes lists powerful — instant access to any element.



### Section 1: Positive Indexing (4 minutes)

**Basic Indexing (Zero-Based):**

```python
fruits = ['apple', 'banana', 'orange', 'grape', 'mango']

# Index:    0        1         2        3       4
# Access first element
first = fruits[0]
print(first)  # apple

# Access second element
second = fruits[1]
print(second)  # banana

# Access third element
third = fruits[2]
print(third)  # orange

# Access last element (must know length)
last = fruits[4]
print(last)  # mango
```

**Key Points:**
- Indices start at 0, not 1
- First element: index 0
- Last element: index (length - 1)
- `fruits[0]` means "get item at position 0"

**Using with len():**

```python
fruits = ['apple', 'banana', 'orange']

# Get last element using length
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(f"Last fruit: {last_fruit}")  # orange

# Length is 3, so indices are 0, 1, 2
print(f"Length: {len(fruits)}")  # 3
print(f"Valid indices: 0 to {len(fruits)-1}")  # 0 to 2
```

**Visual Example:**

```
List: ['A', 'B', 'C', 'D', 'E']
Index:  0    1    2    3    4

fruits[0] → 'A'
fruits[2] → 'C'
fruits[4] → 'E'
```

---

### Section 2: Negative Indexing (3 minutes)

**Counting from the End:**

```python
numbers = [10, 20, 30, 40, 50]

# Negative indices count from the end
# Index:   -5  -4  -3  -2  -1
# Value:   10  20  30  40  50

# Last element
last = numbers[-1]
print(last)  # 50

# Second to last
second_last = numbers[-2]
print(second_last)  # 40

# Third from end
third_last = numbers[-3]
print(third_last)  # 30

# First element (from the end)
first = numbers[-5]
print(first)  # 10
```

**Why Use Negative Indexing:**

```python
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Without negative indexing (need to know length)
last = data[len(data) - 1]  # Verbose

# With negative indexing (clean and simple)
last = data[-1]  # Clean!

# Get last 3 elements
last_three = [data[-3], data[-2], data[-1]]
print(last_three)  # [8, 9, 10]
```

**Relationship Between Positive and Negative:**

```python
items = ['a', 'b', 'c', 'd', 'e']

# These are equivalent:
print(items[0])   # 'a'
print(items[-5])  # 'a'

print(items[4])   # 'e'
print(items[-1])  # 'e'

# Formula: negative_index = positive_index - len(list)
# items[2] = items[2 - 5] = items[-3]
```

---

### Section 3: Index Errors and Validation (3 minutes)

**IndexError - Out of Bounds:**

```python
colors = ['red', 'green', 'blue']

# Valid indices: 0, 1, 2 (or -3, -2, -1)

# This works
print(colors[0])  # red
print(colors[2])  # blue

# This fails - index too high
try:
    print(colors[3])
except IndexError as e:
    print(f"Error: {e}")
# Error: list index out of range

# This fails - index too low
try:
    print(colors[-4])
except IndexError as e:
    print(f"Error: {e}")
# Error: list index out of range
```

**Safe Access with Validation:**

```python
def safe_get(lst, index):
    """Safely get element with bounds checking"""
    if -len(lst) <= index < len(lst):
        return lst[index]
    else:
        return None  # Or raise custom error

scores = [85, 90, 78, 92]

print(safe_get(scores, 0))   # 85
print(safe_get(scores, 10))  # None (safe)
print(safe_get(scores, -1))  # 92
print(safe_get(scores, -10)) # None (safe)
```

**Using try-except:**

```python
def get_element(lst, index, default=None):
    """Get element or return default if out of bounds"""
    try:
        return lst[index]
    except IndexError:
        return default

numbers = [1, 2, 3]

print(get_element(numbers, 0))      # 1
print(get_element(numbers, 10))     # None
print(get_element(numbers, 10, -1)) # -1 (custom default)
```

---

### Section 4: Accessing Nested Lists (3 minutes)

**2D List Indexing:**

```python
# Matrix (2D list)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access rows (first index)
row0 = matrix[0]  # [1, 2, 3]
row1 = matrix[1]  # [4, 5, 6]
row2 = matrix[2]  # [7, 8, 9]

# Access specific elements (row, column)
element = matrix[0][0]  # 1 (row 0, col 0)
element = matrix[0][2]  # 3 (row 0, col 2)
element = matrix[1][1]  # 5 (row 1, col 1)
element = matrix[2][2]  # 9 (row 2, col 2)

# Using negative indices
last_row = matrix[-1]      # [7, 8, 9]
last_element = matrix[-1][-1]  # 9
```

**Practical Example - Student Data:**

```python
students = [
    ['Alice', 85, 90, 88],   # [name, math, science, english]
    ['Bob', 78, 82, 86],
    ['Charlie', 92, 89, 94]
]

# Access Alice's data
alice = students[0]
print(f"Student: {alice}")
# ['Alice', 85, 90, 88]

# Access Alice's name
name = students[0][0]
print(f"Name: {name}")  # Alice

# Access Alice's math grade
math_grade = students[0][1]
print(f"Math grade: {math_grade}")  # 85

# Access Charlie's English grade
english_grade = students[2][3]
print(f"Charlie's English: {english_grade}")  # 94

# Last student's first subject
last_student_first_subject = students[-1][1]
print(last_student_first_subject)  # 92
```

---

### Section 5: Finding Elements (2 minutes)

**Check if Element Exists:**

```python
fruits = ['apple', 'banana', 'orange']

# Using 'in' operator
if 'banana' in fruits:
    print("Banana is in the list")
# Banana is in the list

if 'grape' in fruits:
    print("Grape is in the list")
else:
    print("Grape not found")
# Grape not found
```

**Find Index of Element:**

```python
numbers = [10, 20, 30, 40, 50]

# Find index of value
index = numbers.index(30)
print(f"30 is at index {index}")  # 30 is at index 2

# Access using found index
value = numbers[index]
print(f"Value at index {index}: {value}")  # 30

# Error if not found
try:
    index = numbers.index(100)
except ValueError as e:
    print(f"Error: {e}")
# Error: 100 is not in list
```

**Safe Find:**

```python
def find_index(lst, value):
    """Find index or return -1 if not found"""
    try:
        return lst.index(value)
    except ValueError:
        return -1

colors = ['red', 'green', 'blue']

print(find_index(colors, 'green'))  # 1
print(find_index(colors, 'yellow')) # -1
```

---

### Section 6: Practical Applications (3 minutes)

**Application 1: Grade Lookup System**

```python
students = ['Alice', 'Bob', 'Charlie', 'Diana']
grades = [85, 92, 78, 88]

# Look up specific student grade
student_index = 2
student_name = students[student_index]
student_grade = grades[student_index]

print(f"{student_name}'s grade: {student_grade}")
# Charlie's grade: 78

# Find student by name
name_to_find = 'Diana'
if name_to_find in students:
    index = students.index(name_to_find)
    grade = grades[index]
    print(f"{name_to_find}'s grade: {grade}")
# Diana's grade: 88
```

**Application 2: Shopping Cart**

```python
cart_items = ['Laptop', 'Mouse', 'Keyboard', 'Monitor']
cart_prices = [999.99, 29.99, 79.99, 299.99]

# Display cart with numbers
for i in range(len(cart_items)):
    item = cart_items[i]
    price = cart_prices[i]
    print(f"{i+1}. {item}: ${price}")

# 1. Laptop: $999.99
# 2. Mouse: $29.99
# 3. Keyboard: $79.99
# 4. Monitor: $299.99

# Remove item by position (user sees 1-based, code uses 0-based)
remove_position = 2  # User input
remove_index = remove_position - 1  # Convert to 0-based

removed_item = cart_items[remove_index]
print(f"Removing: {removed_item}")
# Removing: Mouse
```

**Application 3: First and Last Analysis**

```python
temperatures = [72, 75, 68, 71, 73, 76, 74]

# First and last day
first_day = temperatures[0]
last_day = temperatures[-1]

print(f"First day: {first_day}°F")
print(f"Last day: {last_day}°F")

# Temperature change
change = last_day - first_day
print(f"Change: {change:+d}°F")  # +2°F

# Highest and lowest
highest = max(temperatures)
lowest = min(temperatures)

highest_index = temperatures.index(highest)
lowest_index = temperatures.index(lowest)

print(f"Highest: {highest}°F on day {highest_index + 1}")
print(f"Lowest: {lowest}°F on day {lowest_index + 1}")
```

---

### Summary (1 minute)

**Key Concepts Covered:**

1. **Positive Indexing:**
   - Starts at 0
   - `list[0]` - first element
   - `list[len(list)-1]` - last element

2. **Negative Indexing:**
   - Counts from end
   - `list[-1]` - last element
   - `list[-2]` - second to last

3. **Index Validation:**
   - Check bounds before access
   - Use try-except for safety
   - Valid range: `-len(list)` to `len(list)-1`

4. **Nested Lists:**
   - `list[row][col]` - 2D access
   - Multiple levels possible

5. **Finding Elements:**
   - `value in list` - check existence
   - `list.index(value)` - find position

**Quick Reference:**

```python
items = ['a', 'b', 'c', 'd', 'e']

# Positive indices
items[0]   # 'a' (first)
items[2]   # 'c' (third)
items[4]   # 'e' (last)

# Negative indices
items[-1]  # 'e' (last)
items[-2]  # 'd' (second to last)

# Nested
matrix = [[1,2], [3,4]]
matrix[0][1]  # 2

# Find
'b' in items  # True
items.index('c')  # 2
```

**Remember:**
- Indices start at 0
- Use negative for end access
- Always validate bounds
- `index()` raises error if not found
- Nested lists use multiple `[]`

Indexing is fundamental to working with lists - practice accessing elements!
