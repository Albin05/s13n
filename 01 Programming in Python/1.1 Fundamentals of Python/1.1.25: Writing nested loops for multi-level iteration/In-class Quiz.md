# Post-class Quiz: Writing Nested Loops for Multi-Level Iteration

## Question 1

What will be the output of this code?

```python
for i in range(3):
    for j in range(2):
        print('*', end=' ')
    print()
```

A) 6 stars in one line
B) 3 rows with 2 stars each
C) 2 rows with 3 stars each
D) Error

**Answer: B) 3 rows with 2 stars each**

**Explanation:** The outer loop runs 3 times (for rows), and the inner loop runs 2 times (for columns). After each inner loop completes, `print()` creates a new line. This produces 3 rows, each containing 2 stars.

---

## Question 2

How many total iterations occur in this nested loop?

```python
for i in range(4):
    for j in range(3):
        print(i, j)
```

A) 4
B) 7
C) 12
D) 16

**Answer: C) 12**

**Explanation:** Total iterations = outer iterations × inner iterations = 4 × 3 = 12. The inner loop runs completely for each iteration of the outer loop.

---

## Question 3

What pattern will this code create?

```python
for i in range(1, 5):
    for j in range(i):
        print('*', end=' ')
    print()
```

A) Rectangle
B) Right triangle
C) Inverted triangle
D) Diamond

**Answer: B) Right triangle**

**Explanation:** Row 1 prints 1 star (range(1)), Row 2 prints 2 stars (range(2)), Row 3 prints 3 stars (range(3)), Row 4 prints 4 stars (range(4)). This creates a right-angled triangle pattern.

---

## Question 4

What does this code print?

```python
for i in range(2):
    for j in range(2):
        print(i + j, end=' ')
    print()
```

A) 0 1 1 2
B) 0 1<br>1 2
C) 0 2<br>1 3
D) 0 0<br>1 1

**Answer: B) 0 1<br>1 2**

**Explanation:**
- i=0, j=0: print 0
- i=0, j=1: print 1, then newline
- i=1, j=0: print 1
- i=1, j=1: print 2, then newline
Output: First row "0 1", second row "1 2"

---

## Question 5

Which loop controls the number of rows in a nested loop pattern?

A) The innermost loop
B) The outer loop
C) Both loops equally
D) Neither loop

**Answer: B) The outer loop**

**Explanation:** In nested loops for printing patterns, the outer loop typically controls how many rows are printed, while the inner loop controls what gets printed in each row.

---

## Question 6

What will this create?

```python
for i in range(3):
    for j in range(3):
        if i == j:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()
```

A) All stars
B) All dots
C) Diagonal line of stars
D) Checkerboard pattern

**Answer: C) Diagonal line of stars**

**Explanation:** The condition `i == j` is true only on the diagonal: (0,0), (1,1), (2,2). These positions get '*', all others get '.', creating a diagonal pattern.

---

## Question 7

What is the time complexity of a simple nested loop with both loops running n times?

A) O(n)
B) O(n²)
C) O(2n)
D) O(n log n)

**Answer: B) O(n²)**

**Explanation:** When you have two nested loops both running n times, the total number of iterations is n × n = n². This is quadratic time complexity, written as O(n²).

---

## Question 8

How do you create an inverted triangle (5 rows, decreasing stars)?

A) `for i in range(5, 0, -1): for j in range(i): print('*')`
B) `for i in range(5): for j in range(5-i): print('*')`
C) Both A and B
D) Neither A nor B

**Answer: C) Both A and B**

**Explanation:** Both approaches work:
- A: i goes 5,4,3,2,1, j range uses i directly
- B: i goes 0,1,2,3,4, j range is 5-i which gives 5,4,3,2,1
Both produce the same inverted triangle pattern.

---

## Question 9

What is the purpose of `print()` after the inner loop in pattern printing?

A) Print the pattern
B) End the program
C) Move to the next line/row
D) Clear the screen

**Answer: C) Move to the next line/row**

**Explanation:** The `print()` statement with no arguments outputs a newline character, moving the cursor to the next line. This separates rows in the pattern.

---

## Question 10

How do you access an element in a 2D list at row 2, column 3?

A) `matrix[2][3]`
B) `matrix[3][2]`
C) `matrix(2, 3)`
D) `matrix[2, 3]`

**Answer: A) `matrix[2][3]`**

**Explanation:** Use two sets of square brackets: first for row index, second for column index. `matrix[2][3]` accesses row 2 (third row), column 3 (fourth column) since indexing starts at 0.

---

## Question 11

What creates a checkerboard pattern?

A) `if i == j:`
B) `if (i + j) % 2 == 0:`
C) `if i != j:`
D) `if i < j:`

**Answer: B) `if (i + j) % 2 == 0:`**

**Explanation:** When the sum of indices is even, print one character; when odd, print another. This creates the alternating pattern of a checkerboard.

---

## Question 12

How many nested loops are needed to generate all 3-digit combinations (000-999)?

A) 1
B) 2
C) 3
D) 4

**Answer: C) 3**

**Explanation:** One loop for each digit position: hundreds, tens, and ones. Three nested loops allow iteration through all combinations of three digits.

---

## Question 13

What's the correct way to break out of both nested loops?

A) Use double break
B) Use a flag variable
C) Use return (in a function)
D) Both B and C

**Answer: D) Both B and C**

**Explanation:** Break only exits the innermost loop. To exit both:
- Set a flag in inner loop, check flag after inner loop to break outer
- Or use return if code is in a function, which exits the entire function

---

## Question 14

What does this nested loop create?

```python
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(0)
    matrix.append(row)
```

A) A 1D list of zeros
B) A 3x3 matrix of zeros
C) An empty list
D) Error

**Answer: B) A 3x3 matrix of zeros**

**Explanation:** The outer loop creates 3 rows. For each row, the inner loop appends 3 zeros. The result is a 2D list (matrix) with 3 rows and 3 columns, all filled with zeros.

---

## Question 15

Which is TRUE about nested loops?

A) Inner loop runs once per outer loop iteration
B) Outer loop runs once per inner loop iteration
C) Both loops run simultaneously
D) Only one loop runs at a time

**Answer: A) Inner loop runs once per outer loop iteration**

**Explanation:** For each single iteration of the outer loop, the entire inner loop runs from start to finish. If outer loop has 3 iterations and inner has 4, the inner loop runs completely 3 times (total 12 iterations).

---

## Summary

### Key Concepts Tested:

1. **Basic Structure**: Outer loop for rows, inner for columns
2. **Total Iterations**: Multiply loop counts (m × n)
3. **Patterns**: Triangle, rectangle, diagonal, checkerboard
4. **Indexing**: matrix[row][col] syntax
5. **Control Flow**: Breaking from nested loops
6. **Time Complexity**: O(n²) for double nested
7. **Newline Handling**: `print()` after inner loop
8. **Conditional Patterns**: Using i and j relationships
9. **2D Data Structures**: Creating matrices with nested loops
10. **Multiple Levels**: Triple nesting for 3D iterations

### Common Patterns to Remember:

```python
# Rectangle: m rows, n columns
for i in range(m):
    for j in range(n):
        print('*', end=' ')
    print()

# Right Triangle: increasing
for i in range(n):
    for j in range(i + 1):
        print('*', end=' ')
    print()

# Inverted Triangle: decreasing
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()

# Diagonal pattern
for i in range(n):
    for j in range(n):
        if i == j:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()

# Checkerboard pattern
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()
```

### Best Practices:

1. **Start Small**: Test with 3×3 before scaling
2. **Visualize**: Draw the pattern before coding
3. **Name Variables**: Use `row, col` for clarity
4. **Don't Forget Newlines**: Add `print()` after inner loop
5. **Watch Indices**: Ensure correct [row][col] order
6. **Consider Performance**: Nested loops multiply complexity
7. **Test Edge Cases**: Empty lists, single elements
8. **Use Functions**: Extract complex logic from loops
