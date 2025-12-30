## Editorials: Accessing List Elements Using Indexing

### Q1 Solution: Basic Positive and Negative Indexing

```python
colors = ['red', 'green', 'blue', 'yellow', 'purple']

# 1. First element
first = colors[0]
print(f"First: {first}")

# 2. Third element
third = colors[2]
print(f"Third: {third}")

# 3. Last (positive)
last_pos = colors[4]  # or colors[len(colors)-1]
print(f"Last (positive): {last_pos}")

# 4. Last (negative)
last_neg = colors[-1]
print(f"Last (negative): {last_neg}")

# 5. Second to last
second_last = colors[-2]
print(f"Second to last: {second_last}")
```

**Explanation:**
- Index 0 is first element
- Index 2 is third element (0, 1, 2)
- Positive last: length - 1
- Negative -1 is always last
- Negative -2 is second to last
- Negative indices count from end

---

### Q2 Solution: Accessing Nested List Elements

```python
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# 1. First row
first_row = matrix[0]
print(f"First row: {first_row}")

# 2. Row 1, Col 2
element = matrix[1][2]
print(f"Row 1, Col 2: {element}")

# 3. Center (row 1, col 1)
center = matrix[1][1]
print(f"Center: {center}")

# 4. Last element of last row
last = matrix[-1][-1]
print(f"Last element: {last}")

# 5. First element of last row
last_row_first = matrix[-1][0]
print(f"Last row, first element: {last_row_first}")
```

**Explanation:**
- `matrix[0]` gets first row
- `matrix[1][2]` gets row 1, column 2
- First index selects row, second selects column
- `matrix[-1]` gets last row
- `matrix[-1][-1]` gets last element of last row
- Combine negative indices for end access

---

### Q3 Solution: Safe Element Access with Error Handling

```python
def safe_access(lst, index):
    """Safely access list element"""
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"

# Test
numbers = [10, 20, 30, 40, 50]

test_indices = [0, 3, -1, 10, -10]

for idx in test_indices:
    result = safe_access(numbers, idx)
    print(f"Index {idx}: {result}")
```

**Explanation:**
- Use try-except to catch IndexError
- Valid indices won't raise error
- Invalid indices caught and handled
- Returns custom message instead of crashing
- Works with both positive and negative indices
- Alternative: check bounds with if statement

---

### Q4 Solution: Student Grade Lookup System

```python
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
grades = [85, 92, 78, 88, 95]

def lookup_student(name):
    """Find student grade and info"""
    if name in students:
        index = students.index(name)
        grade = grades[index]
        rank = index + 1  # Convert 0-based to 1-based
        
        # Determine rank suffix
        if rank == 1:
            rank_str = "1st"
        elif rank == 2:
            rank_str = "2nd"
        elif rank == 3:
            rank_str = "3rd"
        else:
            rank_str = f"{rank}th"
        
        above_85 = "Yes" if grade > 85 else "No"
        
        print(f"Student: {name}")
        print(f"Grade: {grade}")
        print(f"Rank: {rank_str}")
        print(f"Above 85: {above_85}")
    else:
        print(f"Student: {name}")
        print("Student not found")

# Test
lookup_student('Charlie')
print()
lookup_student('Frank')
```

**Explanation:**
- Check if name exists with `in`
- Use `.index()` to find position
- Access parallel list at same index
- Rank is index + 1 (1-based)
- Handle ordinal suffixes (1st, 2nd, 3rd, th)
- Compare grade to threshold

---

### Q5 Solution: Product Inventory Access

```python
inventory = [
    ['Laptop', 5, 999.99],
    ['Mouse', 50, 29.99],
    ['Keyboard', 30, 79.99],
    ['Monitor', 10, 299.99],
    ['USB Cable', 100, 9.99]
]

# 1. First product
first = inventory[0]
print("First product:")
print(f"  Name: {first[0]}")
print(f"  Quantity: {first[1]}")
print(f"  Price: ${first[2]}")

# 2. Last product
last = inventory[-1]
print("\nLast product:")
print(f"  Name: {last[0]}")
print(f"  Quantity: {last[1]}")
print(f"  Price: ${last[2]}")

# 3. Position 3 (1-based)
position = 3
product = inventory[position - 1]  # Convert to 0-based
print(f"\nPosition {position}: {product[0]}")

# 4. Total value of first
qty, price = inventory[0][1], inventory[0][2]
total = qty * price
print(f"\nFirst product total value: ${total:.2f}")

# 5. All product names
names = [item[0] for item in inventory]
print(f"\nAll products: {', '.join(names)}")
```

**Explanation:**
- `inventory[0]` gets first product list
- Access nested elements: `first[0]`, `first[1]`, `first[2]`
- `inventory[-1]` gets last product
- Convert 1-based position to 0-based index
- Access quantity and price separately
- List comprehension extracts all names
- `join()` creates comma-separated string

**Key Concepts:**
- Zero-based indexing
- Negative indices from end
- Nested list access with `[i][j]`
- Parallel lists at same index
- Error handling with try-except
- Converting between 1-based and 0-based
