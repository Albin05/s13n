## Editorials: Creating and Initializing Lists in Python

### Q1 Solution: Create Different Types of Lists

```python
# 1. Empty list
empty = []
print("Empty list:", empty)

# 2. Integers 1-5
integers = [1, 2, 3, 4, 5]
print("Integers:", integers)

# 3. String list
colors = ["red", "green", "blue"]
print("Colors:", colors)

# 4. Float list
floats = [1.5, 2.5, 3.5]
print("Floats:", floats)

# 5. Mixed list
mixed = ["Python", 42, 3.14, True]
print("Mixed:", mixed)
```

**Explanation:**
- Empty list created with `[]`
- Lists use square brackets `[]`
- Elements separated by commas
- Lists can hold any data type
- Mixed lists combine different types
- No limit on list size

---

### Q2 Solution: Create Lists from Range and String

```python
# 1. Numbers 0-9
numbers = list(range(10))
print("Numbers 0-9:", numbers)

# 2. Even numbers 2-20
evens = list(range(2, 21, 2))
print("Even numbers 2-20:", evens)

# 3. String to characters
word = "PYTHON"
characters = list(word)
print("Characters:", characters)

# 4. Sentence to words
sentence = "I love programming"
words = sentence.split()
print("Words:", words)
```

**Explanation:**
- `range(10)` creates 0-9 (stop is exclusive)
- `range(2, 21, 2)` starts at 2, stops before 21, steps by 2
- `list()` converts range object to list
- `list(string)` creates list of characters
- `.split()` splits string on whitespace by default
- Can split on custom delimiter: `.split(',')`

---

### Q3 Solution: Create and Work with Nested Lists

```python
# Create tic-tac-toe board
board = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['X', 'O', 'X']
]

# Print entire board
print("Board:", board)

# Center element (row 1, column 1)
center = board[1][1]
print("Center:", center)

# Top row (first list)
top_row = board[0]
print("Top row:", top_row)

# Bottom-right (last row, last column)
bottom_right = board[2][2]
print("Bottom-right:", bottom_right)
```

**Explanation:**
- Nested list: list containing lists
- Each inner list is a row
- First index selects row, second selects column
- `board[0]` gets first row
- `board[1][1]` gets center (row 1, col 1)
- `board[2][2]` gets bottom-right (row 2, col 2)
- Indices start at 0

---

### Q4 Solution: Student Grade Management

```python
# Create student list
students = [
    ['Alice', 85, 90, 88],
    ['Bob', 78, 82, 86],
    ['Charlie', 92, 89, 94],
    ['Diana', 88, 91, 87]
]

# Print all students
print("All students:")
print(students)

# Calculate averages
print("\nStudent Averages:")
for student in students:
    name = student[0]
    grades = student[1:4]  # Math, Science, English
    average = sum(grades) / len(grades)
    print(f"{name}: {average:.2f}")

# Find highest math grade
highest_math = students[0]
for student in students:
    if student[1] > highest_math[1]:
        highest_math = student

print(f"\nHighest math grade: {highest_math[0]} with {highest_math[1]}")
```

**Explanation:**
- Each student is a nested list
- `student[0]` is name, `student[1:4]` are grades
- `sum(grades)` adds all grades
- Loop through to find maximum
- Compare `student[1]` (math grade)
- Track student with highest math score

---

### Q5 Solution: Shopping Cart System

```python
# Create shopping cart
cart = [
    ['Laptop', 999.99, 1],
    ['Mouse', 29.99, 2],
    ['Keyboard', 79.99, 1],
    ['USB Cable', 9.99, 3]
]

# Display cart
print("Shopping Cart:")
grand_total = 0
total_products = 0

for i, item in enumerate(cart, 1):
    product, price, qty = item
    subtotal = price * qty
    grand_total += subtotal
    total_products += qty
    
    print(f"Item {i}: {product} - ${price} x {qty} = ${subtotal:.2f}")

# Summary
print(f"\nUnique items: {len(cart)}")
print(f"Total products: {total_products}")
print(f"Grand Total: ${grand_total:.2f}")
```

**Explanation:**
- Each item: [name, price, quantity]
- `enumerate(cart, 1)` provides index starting at 1
- Unpack with `product, price, qty = item`
- Subtotal = price × quantity
- Grand total accumulates subtotals
- Total products sums quantities
- `len(cart)` counts unique items

**Key Concepts:**
- List creation with `[]`
- Mixed data types allowed
- Nested lists for tabular data
- `range()` for number sequences
- `list()` for type conversion
- `.split()` for string to list
- Accessing with indices `[0][1]`
- Iteration with `for` loop
- List unpacking
