## Editorials: Index and Slice Multi-Dimensional Arrays

### Q1 Solution: Access 2D Array Elements

```python
import numpy as np

# Create matrix
matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

# Access element at row 1, column 2
element = matrix[1, 2]
print(f"Element at (1, 2): {element}")

# Access last row, first column using negative indexing
last_first = matrix[-1, 0]
print(f"Element at last row, first column: {last_first}")

# Modify element at row 0, column 1
matrix[0, 1] = 999

# Print entire matrix
print("Modified matrix:")
print(matrix)
```

**Explanation:**
- `matrix[1, 2]` accesses row 1, column 2 (30)
- `matrix[-1, 0]` uses negative index for last row (35)
- Direct modification using `matrix[row, col] = value`
- Indexing syntax: `array[row, column]`

---

### Q2 Solution: Extract Rows and Columns

```python
import numpy as np

# Create array
data = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Extract second row
second_row = data[1, :]
print(f"Second row: {second_row}")

# Extract third column
third_col = data[:, 2]
print(f"Third column: {third_col}")

# Extract last row using negative indexing
last_row = data[-1, :]
print(f"Last row: {last_row}")

# Extract first column
first_col = data[:, 0]
print(f"First column: {first_col}")
```

**Explanation:**
- `data[1, :]` extracts all columns from row 1
- `data[:, 2]` extracts all rows from column 2
- `:` means "all" in that dimension
- Rows and columns are extracted as 1D arrays

---

### Q3 Solution: Slice Sub-Matrices

```python
import numpy as np

# Create matrix
matrix = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20]])

# First 2 rows, first 3 columns
sub1 = matrix[:2, :3]
print("First 2 rows, first 3 cols:")
print(sub1)

# Last 2 rows, last 2 columns
sub2 = matrix[-2:, -2:]
print("\nLast 2 rows, last 2 cols:")
print(sub2)

# Middle elements (exclude borders)
middle = matrix[1:-1, 1:-1]
print("\nMiddle elements:")
print(middle)

# Every other row
every_other_row = matrix[::2, :]
print("\nEvery other row:")
print(every_other_row)

# Every other column
every_other_col = matrix[:, ::2]
print("\nEvery other column:")
print(every_other_col)
```

**Explanation:**
- `matrix[:2, :3]` slices rows 0-1 and columns 0-2
- `matrix[-2:, -2:]` uses negative indices for last 2 rows/columns
- `matrix[1:-1, 1:-1]` excludes first and last row/column
- `matrix[::2, :]` takes every 2nd row (step=2)
- `matrix[:, ::2]` takes every 2nd column
- Slicing works independently in each dimension

---

### Q4 Solution: Manipulate 3D Arrays

```python
import numpy as np

# Create 3D array
arr_3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                   [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])

# Print shape
print(f"Shape: {arr_3d.shape}")

# Extract first layer
first_layer = arr_3d[0, :, :]
print("First layer:")
print(first_layer)

# Second row from second layer
second_row = arr_3d[1, 1, :]
print(f"Second row from second layer: {second_row}")

# Third column from first layer
third_col = arr_3d[0, :, 2]
print(f"Third column from first layer: {third_col}")

# Element at layer 1, row 2, column 1
element = arr_3d[1, 2, 1]
print(f"Element at (1, 2, 1): {element}")
```

**Explanation:**
- 3D arrays have shape `(layers, rows, columns)`
- `arr_3d[0, :, :]` extracts all rows and columns from layer 0
- `arr_3d[1, 1, :]` extracts all columns from layer 1, row 1
- `arr_3d[0, :, 2]` extracts all rows from layer 0, column 2
- `arr_3d[1, 2, 1]` accesses single element (layer 1, row 2, col 1)

---

### Q5 Solution: Analyze Student Grades

```python
import numpy as np

# Student grades
grades = np.array([[85, 92, 78, 90],
                   [88, 76, 95, 82],
                   [92, 88, 84, 89],
                   [78, 85, 88, 91],
                   [95, 89, 92, 87]])

# Student 3 scores (row 2)
student_3 = grades[2, :]
print(f"Student 3 scores: {student_3}")

# Test 2 scores (column 1)
test_2 = grades[:, 1]
print(f"Test 2 scores: {test_2}")

# First 3 students, last 2 tests
subset = grades[:3, -2:]
print("First 3 students, last 2 tests:")
print(subset)

# Student 1 average (row 0)
student_1_avg = grades[0, :].mean()
print(f"Student 1 average: {student_1_avg}")

# Test 4 average (column 3)
test_4_avg = grades[:, 3].mean()
print(f"Test 4 average: {test_4_avg}")
```

**Explanation:**
- `grades[2, :]` extracts all test scores for student 3
- `grades[:, 1]` extracts all student scores for test 2
- `grades[:3, -2:]` slices first 3 rows and last 2 columns
- `.mean()` calculates average of extracted row/column
- Practical application of slicing for data analysis

**Key Concepts Covered:**
1. 2D indexing with `[row, column]` syntax
2. Extracting rows, columns, and sub-matrices
3. Using step parameter in multiple dimensions
4. Working with 3D arrays
5. Practical data analysis with slicing
