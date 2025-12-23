# Lecture Script: Writing Nested Loops for Multi-Level Iteration

**Duration:** 20-25 minutes
**Learning Objective:** Students will be able to write nested loops to create patterns and process multi-dimensional data.

---

## Hook (2 minutes)

"Imagine you're seating guests at a wedding with 5 tables, each with 6 chairs. How would you assign seat numbers? You'd go table by table: Table 1, seats 1 through 6. Table 2, seats 1 through 6. And so on.

That's exactly what nested loops do! The outer loop goes through each table, and for EACH table, the inner loop goes through every chair. We're looping INSIDE a loop!

Today, we'll learn how nested loops help us work with grids, create patterns, and process complex data structures. This is one of the most powerful programming techniques you'll learn!"

---

## Section 1: What are Nested Loops? (3 minutes)

### Definition

"A nested loop is a loop inside another loop. The inner loop runs completely for EACH iteration of the outer loop."

### Basic Structure

```python
for outer in range(3):      # Runs 3 times
    for inner in range(2):  # Runs 2 times FOR EACH outer
        print(f"Outer: {outer}, Inner: {inner}")
```

**Output:**
```
Outer: 0, Inner: 0
Outer: 0, Inner: 1
Outer: 1, Inner: 0
Outer: 1, Inner: 1
Outer: 2, Inner: 0
Outer: 2, Inner: 1
```

**Key Point:** Total iterations = 3 × 2 = 6

### Visual Explanation

"Think of it like a clock:
- The hour hand (outer loop) moves once
- For that ONE hour, the minute hand (inner loop) completes a FULL rotation
- Then the hour advances, and minutes start over"

---

## Section 2: Simple Patterns (5 minutes)

### Example 1: Rectangle Pattern

"Let's print a rectangle of stars!"

```python
# 4 rows, 6 columns
for row in range(4):
    for col in range(6):
        print('*', end=' ')
    print()  # New line after each row
```

**Output:**
```
* * * * * *
* * * * * *
* * * * * *
* * * * * *
```

**Discussion:** "Notice the `print()` after the inner loop! That's what creates a new line for each row."

### Example 2: Right Triangle

"Now a triangle where each row has more stars!"

```python
for row in range(1, 6):
    for col in range(row):
        print('*', end=' ')
    print()
```

**Output:**
```
*
* *
* * *
* * * *
* * * * *
```

**Key Insight:** "The inner loop's range DEPENDS on the outer loop variable! Row 1 prints 1 star, Row 2 prints 2 stars, etc."

### Example 3: Multiplication Table

"Let's create a 5×5 multiplication table!"

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=' ')
    print()
```

**Output:**
```
  1   2   3   4   5
  2   4   6   8  10
  3   6   9  12  15
  4   8  12  16  20
  5  10  15  20  25
```

**Teaching Tip:** "The `:3` formats numbers with 3 spaces for alignment!"

---

## Section 3: Working with 2D Lists (5 minutes)

### Creating a 2D List (Matrix)

"A 2D list is like a spreadsheet - rows and columns of data!"

```python
# Create a 3x3 matrix of zeros
matrix = []

for row in range(3):
    current_row = []
    for col in range(3):
        current_row.append(0)
    matrix.append(current_row)

print(matrix)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

**Explanation:**
- Outer loop: creates 3 rows
- Inner loop: adds 3 zeros to each row

### Processing a 2D List

"Let's sum all elements in a matrix!"

```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

total = 0
for row in matrix:
    for element in row:
        total += element

print(f"Sum: {total}")  # Sum: 45
```

**Key Point:** "We can iterate directly over rows, then over elements in each row!"

### With Indices

"Sometimes we need the position, not just the value!"

```python
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")
```

**Output:**
```
matrix[0][0] = 1
matrix[0][1] = 2
matrix[0][2] = 3
...
```

---

## Section 4: Advanced Patterns (5 minutes)

### Diagonal Pattern

"Let's print stars only on the diagonal!"

```python
for i in range(5):
    for j in range(5):
        if i == j:  # Diagonal condition
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()
```

**Output:**
```
* . . . .
. * . . .
. . * . .
. . . * .
. . . . *
```

**Discussion:** "When row index equals column index, we're on the diagonal!"

### Checkerboard Pattern

"Alternating pattern like a chessboard!"

```python
for i in range(5):
    for j in range(5):
        if (i + j) % 2 == 0:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()
```

**Output:**
```
* . * . *
. * . * .
* . * . *
. * . * .
* . * . *
```

**Math Insight:** "Sum of indices determines the pattern! Even sum = *, odd sum = ."

### Number Pyramid

"A pyramid centered with spaces!"

```python
for i in range(1, 6):
    # Print spaces first
    for space in range(5 - i):
        print(' ', end='')
    # Print numbers
    for num in range(i):
        print(i, end=' ')
    print()
```

**Output:**
```
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
```

**Key Pattern:** "Multiple inner loops! One for spaces, one for numbers."

---

## Section 5: Triple Nested Loops (3 minutes)

### All 3-Digit Combinations

"Sometimes we need THREE levels of nesting!"

```python
for hundreds in range(3):
    for tens in range(3):
        for ones in range(3):
            print(f"{hundreds}{tens}{ones}", end=' ')
        print()  # Newline after each tens iteration
```

**Output:**
```
000 001 002
010 011 012
020 021 022
100 101 102
...
```

**Warning:** "Triple nesting means complexity! 3 × 3 × 3 = 27 iterations. Be careful with large ranges!"

---

## Section 6: Control Flow in Nested Loops (3 minutes)

### Break from Nested Loops

"Breaking only exits the innermost loop!"

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target = 5
found = False

for row in matrix:
    for element in row:
        if element == target:
            print(f"Found {target}!")
            found = True
            break  # Exits inner loop only
    if found:
        break  # Exits outer loop
```

**Key Point:** "Need a flag variable to break out of BOTH loops!"

### Alternative: Function with Return

```python
def find_element(matrix, target):
    for row in matrix:
        for element in row:
            if element == target:
                return True  # Exits entire function
    return False
```

**Advantage:** "Return exits ALL loops at once! Cleaner than flags."

---

## Section 7: Real-World Applications (2 minutes)

### Where We Use Nested Loops

1. **Image Processing:** Every pixel in a photo (rows × columns)
2. **Game Boards:** Chess, tic-tac-toe (8×8 grid)
3. **Spreadsheets:** Processing every cell
4. **Seating Charts:** Rows and seats
5. **Calendars:** Weeks and days
6. **GPS Coordinates:** Latitude and longitude grids
7. **Matrix Math:** Linear algebra operations

### Example: Finding Seat

```python
seating = [["Alice", "Bob", "Carol"],
           ["David", "Emma", "Frank"],
           ["Grace", "Henry", "Iris"]]

target = "Emma"

for row_num, row in enumerate(seating):
    for seat_num, person in enumerate(row):
        if person == target:
            print(f"{target} is in row {row_num}, seat {seat_num}")
```

---

## Common Mistakes (2 minutes)

### Mistake 1: Forgetting Newline

```python
# WRONG - all on one line
for i in range(3):
    for j in range(3):
        print('*', end=' ')
# *** *** ***

# RIGHT - rows separated
for i in range(3):
    for j in range(3):
        print('*', end=' ')
    print()  # Newline after inner loop
```

### Mistake 2: Index Confusion

```python
matrix = [[1, 2], [3, 4], [5, 6]]

# WRONG
print(matrix[j][i])  # Swapped!

# RIGHT
print(matrix[i][j])  # Row first, then column
```

### Mistake 3: Same Range for Both Loops

```python
# This only works for SQUARE patterns!
for i in range(4):
    for j in range(4):  # 4×4 square
        print('*', end=' ')
    print()

# For rectangle, use different ranges
for i in range(3):   # 3 rows
    for j in range(5):   # 5 columns
        print('*', end=' ')
    print()
```

---

## Practice Problems (2 minutes)

### Problem 1

"What does this print?"

```python
for i in range(2):
    for j in range(3):
        print(i + j, end=' ')
    print()
```

**Answer:**
```
0 1 2
1 2 3
```

### Problem 2

"How many total iterations?"

```python
for i in range(5):
    for j in range(4):
        for k in range(3):
            pass  # Do something
```

**Answer:** 5 × 4 × 3 = 60 iterations

---

## Wrap-Up (1 minute)

### Key Takeaways

**Structure:**
- Outer loop runs first
- Inner loop completes FULLY for EACH outer iteration
- Total iterations = multiply all loop counts

**Patterns:**
- Rectangle: same range for both
- Triangle: inner range depends on outer variable
- Complex: use conditionals (i == j, (i+j) % 2, etc.)

**2D Lists:**
- Outer loop = rows
- Inner loop = columns
- Access with matrix[row][col]

**Best Practices:**
- Use `print()` after inner loop for new line
- Name variables clearly (row, col not i, j)
- Watch out for O(n²) or O(n³) complexity
- Test with small values (3×3) first

**Quick Reference:**

```python
# Basic pattern
for row in range(rows):
    for col in range(cols):
        print('*', end=' ')
    print()

# Triangle
for row in range(n):
    for col in range(row + 1):
        print('*', end=' ')
    print()

# 2D processing
for row in matrix:
    for element in row:
        process(element)
```

---

## Q&A (Time permitting)

**Q: Can I have more than 3 nested loops?**
A: Yes, but it gets complex fast! Each level multiplies iterations. Use wisely.

**Q: When should I use nested loops vs. other approaches?**
A: When working with multi-dimensional data or need all combinations. For 1D data, single loop is enough.

**Q: How do I break out of all nested loops?**
A: Use a flag variable or put code in a function and use return.

**Q: Why do we say matrix[row][col] not matrix[col][row]?**
A: Convention! First index is the row (which list), second is position within that row.

---

## Homework Preview

"Practice these concepts:
1. Create different patterns (triangle, diamond, etc.)
2. Build and process 2D lists
3. Find elements in matrices
4. Generate combinations with triple nested loops

Remember: Start simple, visualize the output, and test with small numbers first!"

---

**End of Lecture**

"Great work today! Nested loops open up a whole new world of possibilities. With practice, you'll master patterns, matrices, and complex data processing. Keep coding!"
