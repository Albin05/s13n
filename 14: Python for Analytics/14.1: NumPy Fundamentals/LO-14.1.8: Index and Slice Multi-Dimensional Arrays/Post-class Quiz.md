## Post-class Quiz: Index and Slice Multi-Dimensional Arrays

### Question 1
For a 2D array `matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])`, what does `matrix[1, 2]` return?

A) 3
B) 6
C) 5
D) [4, 5, 6]

**Correct Answer: B**
*Explanation: `matrix[1, 2]` accesses row 1, column 2, which is 6*

---

### Question 2
How do you extract the second column from a 2D array?

A) `array[2, :]`
B) `array[:, 1]`
C) `array[1]`
D) `array[:, 2]`

**Correct Answer: B**
*Explanation: `array[:, 1]` selects all rows (`:`) from column index 1 (second column)*

---

### Question 3
What does `matrix[:2, :3]` extract from a 2D array?

A) First 2 rows and first 3 columns
B) First 3 rows and first 2 columns
C) Rows 2-3 and columns 2-3
D) Second row and third column

**Correct Answer: A**
*Explanation: Slicing `[:2, :3]` extracts rows 0-1 and columns 0-2*

---

### Question 4
For a 3D array with shape `(2, 3, 4)`, what does the first dimension represent?

A) Rows
B) Columns
C) Layers/Depth
D) Height

**Correct Answer: C**
*Explanation: In 3D arrays with shape (d, r, c), first dimension is layers/depth*

---

### Question 5
What does `matrix[::2, ::2]` do?

A) Extract every element
B) Extract every 2nd row and every 2nd column
C) Extract first 2 rows and first 2 columns
D) Reverse the matrix

**Correct Answer: B**
*Explanation: `::2` means step=2 in both dimensions, taking every 2nd row and column*
