### **1. Simple Multiplication Table**

Print a 5x5 multiplication table.

**Expected Output:**
```
1x1=1  1x2=2  1x3=3  1x4=4  1x5=5
2x1=2  2x2=4  2x3=6  2x4=8  2x5=10
3x1=3  3x2=6  3x3=9  3x4=12 3x5=15
4x1=4  4x2=8  4x3=12 4x4=16 4x5=20
5x1=5  5x2=10 5x3=15 5x4=20 5x5=25
```

**Hint:** Use nested for loops with `range(1, 6)` for both i and j.

---

---

### **2. Rectangle Pattern**

Print a rectangle of stars with 4 rows and 6 columns.

**Expected Output:**
```
* * * * * *
* * * * * *
* * * * * *
* * * * * *
```

**Hint:** Outer loop for rows, inner loop for columns.

---

---

### **3. Right Triangle Pattern**

Print a right-angled triangle pattern with 5 rows.

**Expected Output:**
```
*
* *
* * *
* * * *
* * * * *
```

**Hint:** Inner loop should go from 1 to row_number + 1.

---

---

### **4. Number Triangle**

Print a triangle where each row contains row number repeated.

**Expected Output:**
```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

**Hint:** Print row number in inner loop, repeat based on row count.

---

---

### **5. Nested Lists**

Create a 3x3 matrix (2D list) filled with zeros using nested loops.

**Expected Output:**
```python
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
```

**Hint:** Outer loop creates rows, inner loop creates columns, append to lists.

---

---

### **6. Print All Pairs**

Print all possible pairs from two lists.

Given lists: `[1, 2, 3]` and `['a', 'b', 'c']`

**Expected Output:**
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

**Hint:** Outer loop for first list, inner loop for second list.

---

---

### **7. Sum of 2D List**

Calculate the sum of all elements in a 2D list.

Given matrix:
```python
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```

**Expected Output:**
```
Sum: 45
```

**Hint:** Outer loop for rows, inner loop for elements, accumulate sum.

---

---

### **8. Inverted Triangle**

Print an inverted right-angled triangle.

**Expected Output:**
```
* * * * *
* * * *
* * *
* *
*
```

**Hint:** Start from 5 and decrease, or use `range(5, 0, -1)`.

---

---

### **9. Number Pyramid**

Print a number pyramid.

**Expected Output:**
```
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
```

**Hint:** Add spaces before numbers based on row position.

---

---

### **10. Coordinates Grid**

Print all coordinates for a 4x4 grid in (row, col) format.

**Expected Output:**
```
(0,0) (0,1) (0,2) (0,3)
(1,0) (1,1) (1,2) (1,3)
(2,0) (2,1) (2,2) (2,3)
(3,0) (3,1) (3,2) (3,3)
```

**Hint:** Use nested enumerate or nested range loops.

---

---

### **11. Find Element in 2D List**

Find if a target element exists in a 2D list and print its position.

Given matrix: `[[10, 20, 30], [40, 50, 60], [70, 80, 90]]`
Target: `50`

**Expected Output:**
```
Found at row 1, col 1
```

**Hint:** Nested loops with condition, track indices.

---

---

### **12. Matrix Transpose**

Transpose a 3x2 matrix (swap rows and columns).

Given matrix:
```python
[[1, 2],
 [3, 4],
 [5, 6]]
```

**Expected Output:**
```python
[[1, 3, 5],
 [2, 4, 6]]
```

**Hint:** Create new matrix, swap i and j indices.

---

---

### **13. Diagonal Pattern**

Print a diagonal pattern for a 5x5 grid.

**Expected Output:**
```
* . . . .
. * . . .
. . * . .
. . . * .
. . . . *
```

**Hint:** Print '*' when row index equals column index.

---

---

### **14. Checkerboard Pattern**

Print a checkerboard pattern (alternating * and .).

**Expected Output:**
```
* . * . *
. * . * .
* . * . *
. * . * .
* . * . *
```

**Hint:** Use `(row + col) % 2` to determine pattern.

---

---

### **15. All Combinations**

Print all possible 3-digit combinations from digits 0-2.

**Expected Output:**
```
000 001 002 010 011 012 020 021 022
100 101 102 110 111 112 120 121 122
200 201 202 210 211 212 220 221 222
```

**Hint:** Use three nested loops for hundreds, tens, and ones place.

---

---

### **16. Prime Number Grid**

Check which positions in a 2D list contain prime numbers.

Given matrix: `[[2, 4, 5], [6, 7, 9], [10, 11, 13]]`

**Expected Output:**
```
Prime at (0, 0): 2
Prime at (0, 2): 5
Prime at (1, 1): 7
Prime at (2, 1): 11
Prime at (2, 2): 13
```

**Hint:** Nested loops with is_prime helper function.

---

---

### **17. Row and Column Sums**

Calculate sum of each row and each column in a matrix.

Given matrix:
```python
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```

**Expected Output:**
```
Row 0 sum: 6
Row 1 sum: 15
Row 2 sum: 24
Col 0 sum: 12
Col 1 sum: 15
Col 2 sum: 18
```

**Hint:** First loop for row sums, second nested loop for column sums.

---

---

### **18. Pascal's Triangle**

Print first 5 rows of Pascal's Triangle.

**Expected Output:**
```
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
```

**Hint:** Use formula: `value = prev_row[j-1] + prev_row[j]`, or combinatorics.

---

---

### **19. Spiral Matrix**

Create a 3x3 spiral matrix.

**Expected Output:**
```
1 2 3
8 9 4
7 6 5
```

**Hint:** Track direction (right, down, left, up) and boundaries.

---

---

### **20. Diamond Pattern**

Print a diamond pattern.

**Expected Output:**
```
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
```

**Hint:** Combine increasing triangle and decreasing triangle.

---

---

### **21. Flatten 2D List**

Convert a 2D list to a 1D list.

Given matrix: `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`

**Expected Output:**
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Hint:** Nested loops to append each element to new list.

---

---

### **22. Common Elements in Lists**

Find common elements between multiple lists using nested loops.

Given lists: `[1, 2, 3, 4]`, `[3, 4, 5, 6]`, `[4, 5, 6, 7]`

**Expected Output:**
```
Common element: 4
```

**Hint:** Use nested loops to check if element exists in all lists.

---

---

### **23. Nested Counters**

Count total iterations in nested loops.

Use 3 nested loops: outer 1-3, middle 1-4, inner 1-2.

**Expected Output:**
```
Total iterations: 24
```

**Hint:** Increment counter in innermost loop: 3 × 4 × 2 = 24.

---

---

### **24. Matrix Multiplication**

Multiply two 2x2 matrices.

Given:
```python
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
```

**Expected Output:**
```python
[[19, 22],
 [43, 50]]
```

**Hint:** Triple nested loop: i for rows of A, j for cols of B, k for multiplication.

---

---

### **25. Border Pattern**

Print a bordered rectangle.

**Expected Output:**
```
* * * * * *
*         *
*         *
*         *
* * * * * *
```

**Hint:** Print '*' when row or col is at edge, else print space.

---

---

### **26. Times Table**

Print multiplication table for numbers 1-3 (1 to 5 for each).

**Expected Output:**
```
1: 1 2 3 4 5
2: 2 4 6 8 10
3: 3 6 9 12 15
```

**Hint:** Outer loop for number, inner for multipliers.

---

---

### **27. Sum Diagonal Elements**

Calculate sum of diagonal elements in a square matrix.

Given matrix:
```python
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```

**Expected Output:**
```
Main diagonal sum: 15
```

**Hint:** Sum elements where row index equals column index.

---

---

### **28. Identity Matrix**

Create a 4x4 identity matrix (1s on diagonal, 0s elsewhere).

**Expected Output:**
```python
[[1, 0, 0, 0],
 [0, 1, 0, 0],
 [0, 0, 1, 0],
 [0, 0, 0, 1]]
```

**Hint:** Set value to 1 when i == j, else 0.

---

---

### **29. All Substrings**

Generate all substrings of a string using nested loops.

Given string: `"abc"`

**Expected Output:**
```
a ab abc
b bc
c
```

**Hint:** Outer loop for start index, inner for end index, slice string.

---

---

### **30. Nested List Comprehension Alternative**

Create same 3x3 matrix using nested loops (not comprehension).

**Expected Output:**
```python
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```

**Hint:** Track counter across nested loops, append to row, row to matrix.

---

## Key Concepts

### Basic Structure

```python
# Simple nested loop
for i in range(rows):
    for j in range(cols):
        # Inner loop body
```

### Common Patterns

1. **Rectangular Grid:**
   ```python
   for row in range(rows):
       for col in range(cols):
           print('*', end=' ')
       print()  # New line
   ```

2. **Triangle Pattern:**
   ```python
   for row in range(n):
       for col in range(row + 1):
           print('*', end=' ')
       print()
   ```

3. **2D List Processing:**
   ```python
   for row in matrix:
       for element in row:
           process(element)
   ```

4. **With Indices:**
   ```python
   for i in range(len(matrix)):
       for j in range(len(matrix[i])):
           print(matrix[i][j])
   ```

### Performance Considerations

- **Time Complexity:** Nested loops multiply complexity
  - One loop: O(n)
  - Two nested: O(n²)
  - Three nested: O(n³)

- **When to Use:**
  - Multi-dimensional data (matrices, grids)
  - Combinatorial problems (all pairs, combinations)
  - Pattern printing
  - Searching in 2D structures

- **When to Avoid:**
  - If same result possible with single loop
  - Very large datasets (consider alternatives)
  - Deep nesting (> 3 levels gets complex)

### Control Flow

```python
# Break from nested loops
found = False
for i in range(n):
    for j in range(m):
        if condition:
            found = True
            break
    if found:
        break

# Continue in nested loops
for i in range(n):
    for j in range(m):
        if skip_condition:
            continue  # Skips to next j
        process(i, j)
```

### Common Mistakes

1. **Wrong Range:** Using same range for both loops when they should differ
2. **Index Errors:** Accessing matrix[j][i] instead of matrix[i][j]
3. **Missing New Line:** Forgetting print() after inner loop
4. **Infinite Loops:** Not updating loop variables correctly
5. **Breaking Outer Loop:** Forgetting to check flag after inner loop

### Best Practices

1. **Clear Variable Names:** Use `row, col` instead of `i, j` for clarity
2. **Comments:** Explain what each loop level represents
3. **Keep It Simple:** Limit nesting depth to 2-3 levels
4. **Extract Functions:** Move complex inner logic to functions
5. **Test Edge Cases:** Empty lists, single element, etc.

### Real-World Applications

1. **Image Processing:** Iterate through pixels (rows × columns)
2. **Game Boards:** Chess, tic-tac-toe, etc.
3. **Spreadsheets:** Process cells in tables
4. **Data Analysis:** Multi-dimensional data structures
5. **Graph Algorithms:** Adjacency matrices
6. **Scientific Computing:** Matrix operations
7. **Pattern Generation:** ASCII art, designs
8. **Combinatorics:** Generate all combinations/permutations

### Practice Tips

1. **Start Simple:** Begin with basic rectangles, then triangles
2. **Visualize:** Draw what you want before coding
3. **Trace Execution:** Manually follow loop iterations
4. **Use Print:** Debug by printing i, j values
5. **Build Incrementally:** Start with outer loop, add inner loop
6. **Test Patterns:** Use small values (3x3) before scaling up
7. **Understand Indices:** Know what each loop variable represents
8. **Practice Variations:** Same pattern in different ways

## Additional Challenges

### Challenge 1: Hourglass Pattern
Print an hourglass shape.

### Challenge 2: Zigzag Pattern
Create a zigzag pattern across rows.

### Challenge 3: Rotating Matrix
Rotate a matrix 90 degrees clockwise.

### Challenge 4: Finding Saddle Point
Find element that is max in row and min in column.

### Challenge 5: Generating Fibonacci Matrix
Each element is sum of element above and to the left.

---

## Summary

Nested loops are essential for:
- Working with multi-dimensional data
- Creating patterns and shapes
- Processing grids and matrices
- Generating combinations
- Implementing complex algorithms

Master nested loops by:
1. Understanding loop execution order
2. Tracking multiple indices correctly
3. Visualizing the output structure
4. Managing control flow (break/continue)
5. Considering performance implications

Remember: The outer loop runs completely before inner loop, and inner loop completes fully for each outer loop iteration!

---

