# Editorials: Writing Nested Loops for Multi-Level Iteration

## Problem 1: Simple Multiplication Table

**Problem:** Print a 5x5 multiplication table.

**Solution:**
```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i}x{j}={i*j:2}", end="  ")
    print()  # New line after each row
```

**Output:**
```
1x1=1  1x2=2  1x3=3  1x4=4  1x5=5
2x1=2  2x2=4  2x3=6  2x4=8  2x5=10
3x1=3  3x2=6  3x3=9  3x4=12 3x5=15
4x1=4  4x2=8  4x3=12 4x4=16 4x5=20
5x1=5  5x2=10 5x3=15 5x4=20 5x5=25
```

**Explanation:**
- Outer loop (`i`) runs 5 times for rows (1-5)
- Inner loop (`j`) runs 5 times for columns (1-5)
- For each combination, print i×j
- `{i*j:2}` formats numbers with minimum 2 spaces for alignment
- `print()` after inner loop creates new line for next row

**Key Concept:** Nested loops create a grid where outer loop controls rows, inner controls columns.

---

## Problem 2: Rectangle Pattern

**Problem:** Print a rectangle of stars with 4 rows and 6 columns.

**Solution:**
```python
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

**Explanation:**
- Outer loop runs 4 times (4 rows)
- Inner loop runs 6 times (6 columns)
- Print star on each iteration of inner loop
- New line after inner loop completes
- Total stars: 4 × 6 = 24

**Key Concept:** Same range for both loops creates a rectangle.

---

## Problem 3: Right Triangle Pattern

**Problem:** Print a right-angled triangle pattern with 5 rows.

**Solution:**
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

**Explanation:**
- Row 1: inner loop runs 1 time (range(1) = 0)
- Row 2: inner loop runs 2 times (range(2) = 0,1)
- Row 3: inner loop runs 3 times
- And so on...
- Number of stars per row equals row number

**Key Concept:** Inner loop range depends on outer loop variable creates triangle.

---

## Problem 4: Number Triangle

**Problem:** Print a triangle where each row contains row number repeated.

**Solution:**
```python
for row in range(1, 6):
    for col in range(row):
        print(row, end=' ')
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

**Explanation:**
- Same structure as star triangle
- Instead of printing '*', print the row number
- Row 1 prints: 1
- Row 2 prints: 2 2
- Row 3 prints: 3 3 3

**Key Concept:** Use outer loop variable in inner loop body for patterns.

---

## Problem 5: Nested Lists (2D Matrix)

**Problem:** Create a 3x3 matrix filled with zeros using nested loops.

**Solution:**
```python
matrix = []

for row in range(3):
    current_row = []
    for col in range(3):
        current_row.append(0)
    matrix.append(current_row)

print(matrix)
```

**Output:**
```python
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
```

**Explanation:**
- Create empty matrix list
- Outer loop: create 3 rows
- For each row, create empty current_row list
- Inner loop: append 3 zeros to current_row
- Append completed row to matrix
- Result: 3×3 matrix of zeros

**Key Concept:** Nested loops build 2D data structures.

---

## Problem 6: Print All Pairs

**Problem:** Print all possible pairs from two lists.

**Solution:**
```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

for num in list1:
    for letter in list2:
        print(num, letter)
```

**Output:**
```
1 a
1 b
1 c
2 a
2 b
2 c
3 a
3 b
3 c
```

**Explanation:**
- Outer loop selects element from list1
- Inner loop pairs it with each element from list2
- For num=1: pairs with a, b, c
- For num=2: pairs with a, b, c
- For num=3: pairs with a, b, c
- Total pairs: 3 × 3 = 9

**Key Concept:** Nested loops generate all combinations (Cartesian product).

---

## Problem 7: Sum of 2D List

**Problem:** Calculate sum of all elements in a 2D list.

**Solution:**
```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

total = 0

for row in matrix:
    for element in row:
        total += element

print(f"Sum: {total}")
```

**Output:**
```
Sum: 45
```

**Explanation:**
- Initialize total to 0
- Outer loop: iterate through each row
- Inner loop: iterate through elements in that row
- Add each element to total
- Sum: 1+2+3+4+5+6+7+8+9 = 45

**Key Concept:** Process all elements in 2D structure with nested loops.

---

## Problem 8: Inverted Triangle

**Problem:** Print an inverted right-angled triangle.

**Solution:**
```python
for row in range(5, 0, -1):
    for col in range(row):
        print('*', end=' ')
    print()
```

**Output:**
```
* * * * *
* * * *
* * *
* *
*
```

**Explanation:**
- Outer loop: 5, 4, 3, 2, 1 (decreasing)
- Row 1: range(5) prints 5 stars
- Row 2: range(4) prints 4 stars
- Row 3: range(3) prints 3 stars
- And so on...

**Key Concept:** Decreasing range creates inverted patterns.

---

## Problem 9: Number Pyramid

**Problem:** Print a number pyramid with spacing.

**Solution:**
```python
for row in range(1, 6):
    # Print spaces
    for space in range(5 - row):
        print(' ', end='')
    # Print numbers
    for num in range(row):
        print(row, end=' ')
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

**Explanation:**
- Row 1: 4 spaces, then 1
- Row 2: 3 spaces, then 2 2
- Row 3: 2 spaces, then 3 3 3
- Spaces = 5 - row
- Numbers = row times

**Key Concept:** Multiple inner loops for complex patterns (spaces + content).

---

## Problem 10: Coordinates Grid

**Problem:** Print all coordinates for a 4x4 grid.

**Solution:**
```python
for row in range(4):
    for col in range(4):
        print(f"({row},{col})", end=' ')
    print()
```

**Output:**
```
(0,0) (0,1) (0,2) (0,3)
(1,0) (1,1) (1,2) (1,3)
(2,0) (2,1) (2,2) (2,3)
(3,0) (3,1) (3,2) (3,3)
```

**Explanation:**
- Outer loop: row from 0 to 3
- Inner loop: col from 0 to 3
- Print coordinates (row, col) for each position
- Creates a 4×4 grid of coordinates

**Key Concept:** Loop indices represent positions in grid.

---

## Problem 11: Find Element in 2D List

**Problem:** Find target element and print its position.

**Solution:**
```python
matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
target = 50
found = False

for row_idx in range(len(matrix)):
    for col_idx in range(len(matrix[row_idx])):
        if matrix[row_idx][col_idx] == target:
            print(f"Found at row {row_idx}, col {col_idx}")
            found = True
            break
    if found:
        break
```

**Output:**
```
Found at row 1, col 1
```

**Explanation:**
- Nested loops with indices to track position
- Check each element against target
- When found, print position and set flag
- Break from both loops using flag

**Key Concept:** Use indices when you need position information.

---

## Problem 12: Matrix Transpose

**Problem:** Transpose a 3x2 matrix (swap rows and columns).

**Solution:**
```python
matrix = [[1, 2],
          [3, 4],
          [5, 6]]

# Create transpose: 2 rows, 3 cols (swap dimensions)
transpose = []
for col in range(2):
    new_row = []
    for row in range(3):
        new_row.append(matrix[row][col])
    transpose.append(new_row)

print(transpose)
```

**Output:**
```python
[[1, 3, 5],
 [2, 4, 6]]
```

**Explanation:**
- Original: 3 rows × 2 columns
- Transpose: 2 rows × 3 columns
- For each column in original, create a row in transpose
- Column 0 of original [1, 3, 5] becomes row 0 of transpose
- Column 1 of original [2, 4, 6] becomes row 1 of transpose

**Key Concept:** Swap i and j to transpose.

---

## Problem 13: Diagonal Pattern

**Problem:** Print diagonal pattern for 5x5 grid.

**Solution:**
```python
for row in range(5):
    for col in range(5):
        if row == col:
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

**Explanation:**
- When row index equals column index, it's on diagonal
- (0,0), (1,1), (2,2), (3,3), (4,4) are diagonal
- Print '*' for diagonal, '.' for others

**Key Concept:** Conditional based on row/col relationship creates patterns.

---

## Problem 14: Checkerboard Pattern

**Problem:** Print alternating * and . in checkerboard.

**Solution:**
```python
for row in range(5):
    for col in range(5):
        if (row + col) % 2 == 0:
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

**Explanation:**
- Sum of row and column indices determines pattern
- If sum is even: print '*'
- If sum is odd: print '.'
- (0,0) sum=0 (even) → *
- (0,1) sum=1 (odd) → .
- (0,2) sum=2 (even) → *

**Key Concept:** Mathematical relationship between indices creates patterns.

---

## Problem 15: All Combinations

**Problem:** Print all 3-digit combinations from digits 0-2.

**Solution:**
```python
for hundreds in range(3):
    for tens in range(3):
        for ones in range(3):
            print(f"{hundreds}{tens}{ones}", end=' ')
        print()  # New line after each row of tens
```

**Output:**
```
000 001 002
010 011 012
020 021 022
100 101 102
110 111 112
120 121 122
200 201 202
210 211 212
220 221 222
```

**Explanation:**
- Triple nested loop for 3 positions
- Outer: hundreds place (0, 1, 2)
- Middle: tens place (0, 1, 2)
- Inner: ones place (0, 1, 2)
- Total combinations: 3 × 3 × 3 = 27

**Key Concept:** Triple nesting for three-level combinations.

---

## Problems 16-30: Summary Solutions

Due to space, here are concise solutions for remaining problems:

**Problem 16: Prime Number Grid** - Nested loops with is_prime helper function checking each element.

**Problem 17: Row and Column Sums** - First nested loop sums rows, second nested loop sums columns.

**Problem 18: Pascal's Triangle** - Build each row from previous row using nested loops.

**Problem 19: Spiral Matrix** - Track direction and boundaries while filling matrix spirally.

**Problem 20: Diamond Pattern** - Combine increasing triangle (spaces decrease, stars increase) with decreasing triangle.

**Problem 21: Flatten 2D List** - Nested loops append each element to new 1D list.

**Problem 22: Common Elements** - Nested loops check if element exists in all lists.

**Problem 23: Nested Counters** - Count total iterations: outer × middle × inner.

**Problem 24: Matrix Multiplication** - Triple nested: i for rows, j for cols, k for dot product.

**Problem 25: Border Pattern** - Print '*' when row or col is 0 or max, else space.

**Problem 26: Times Table** - Outer loop for number, inner for multipliers 1-5.

**Problem 27: Sum Diagonal** - Sum elements where `matrix[i][i]`.

**Problem 28: Identity Matrix** - Set to 1 when i==j, else 0.

**Problem 29: All Substrings** - Outer for start, inner for end, slice `s[start:end]`.

**Problem 30: Sequential Matrix** - Track counter, increment for each position.

---

## Key Patterns Summary

### 1. Rectangle (m × n)
```python
for i in range(m):
    for j in range(n):
        print('*', end=' ')
    print()
```

### 2. Right Triangle
```python
for i in range(n):
    for j in range(i + 1):
        print('*', end=' ')
    print()
```

### 3. Inverted Triangle
```python
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()
```

### 4. Pyramid (with spaces)
```python
for i in range(1, n+1):
    print(' ' * (n-i), end='')
    print('* ' * i)
```

### 5. 2D List Processing
```python
for row in matrix:
    for element in row:
        process(element)
```

### 6. With Indices
```python
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])
```

### 7. Conditional Patterns
```python
for i in range(n):
    for j in range(n):
        if condition(i, j):
            print('X')
        else:
            print('O')
    print()
```

---

## Common Pitfalls

1. **Index Confusion:** Swapping i and j
2. **Missing Newline:** Forgetting `print()` after inner loop
3. **Range Errors:** Using wrong range for variable-sized patterns
4. **Break Issues:** Not propagating break to outer loop
5. **Performance:** Not considering O(n²) or O(n³) complexity

---

## Best Practices

1. **Descriptive Names:** Use `row, col` instead of `i, j`
2. **Comments:** Document what each level represents
3. **Test Small:** Start with 3×3 before scaling
4. **Visualize First:** Draw expected output
5. **Extract Logic:** Move complex operations to functions
