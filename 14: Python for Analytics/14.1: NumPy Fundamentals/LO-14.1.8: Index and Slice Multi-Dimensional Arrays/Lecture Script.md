### Index and Slice Multi-Dimensional Arrays

### Hook (2 minutes)

"Working with multi-dimensional data like matrices, images, or time-series datasets requires mastering 2D and 3D array indexing. Whether you're selecting specific rows and columns, extracting sub-matrices, or working with image pixels, understanding multi-dimensional indexing is crucial. NumPy makes this powerful with intuitive syntax that extends 1D slicing to multiple dimensions!"

### Section 1: Indexing 2D Arrays (3 minutes)

**Accessing elements in 2D arrays:**

```python
import numpy as np

# Create 2D array (matrix)
matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

# Access single element: array[row, column]
print(matrix[0, 0])   # 10 (first row, first column)
print(matrix[1, 2])   # 60 (second row, third column)
print(matrix[2, 1])   # 80 (third row, second column)

# Negative indexing
print(matrix[-1, -1])  # 90 (last row, last column)
print(matrix[-2, 0])   # 40 (second-to-last row, first column)
```

**2D array structure:**
```
       Col 0  Col 1  Col 2
Row 0:  10     20     30
Row 1:  40     50     60
Row 2:  70     80     90

matrix[1, 2] = 60  (row 1, column 2)
```

**Modifying elements:**

```python
matrix[1, 1] = 999
print(matrix)
# [[ 10  20  30]
#  [ 40 999  60]
#  [ 70  80  90]]
```

### Section 2: Slicing Rows and Columns (4 minutes)

**Extract entire rows:**

```python
import numpy as np

matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

# Get entire row
row_1 = matrix[1, :]   # [40, 50, 60] (second row)
row_0 = matrix[0, :]   # [10, 20, 30] (first row)

# Shorthand (: is optional for last dimension)
row_2 = matrix[2]      # [70, 80, 90] (third row)
```

**Extract entire columns:**

```python
# Get entire column
col_0 = matrix[:, 0]   # [10, 40, 70] (first column)
col_2 = matrix[:, 2]   # [30, 60, 90] (third column)
```

**Extract sub-matrices:**

```python
# Slice rows and columns
sub = matrix[0:2, 1:3]
print(sub)
# [[20 30]
#  [50 60]]

# First 2 rows, last 2 columns
sub2 = matrix[:2, -2:]
print(sub2)
# [[20 30]
#  [50 60]]
```

### Section 3: Advanced 2D Slicing (4 minutes)

**Combining slicing techniques:**

```python
import numpy as np

data = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]])

# Every other row
print(data[::2, :])
# [[ 1  2  3  4]
#  [ 9 10 11 12]]

# Every other column
print(data[:, ::2])
# [[ 1  3]
#  [ 5  7]
#  [ 9 11]
#  [13 15]]

# Every other row and column
print(data[::2, ::2])
# [[ 1  3]
#  [ 9 11]]

# Reverse rows
print(data[::-1, :])
# [[13 14 15 16]
#  [ 9 10 11 12]
#  [ 5  6  7  8]
#  [ 1  2  3  4]]

# Reverse columns
print(data[:, ::-1])
# [[ 4  3  2  1]
#  [ 8  7  6  5]
#  [12 11 10  9]
#  [16 15 14 13]]
```

**Exclude borders (remove first and last row/column):**

```python
inner = data[1:-1, 1:-1]
print(inner)
# [[ 6  7]
#  [10 11]]
```

### Section 4: 3D Array Indexing (3 minutes)

**Understanding 3D arrays:**

3D arrays have shape (depth, rows, columns) or (layers, rows, columns)

```python
import numpy as np

# Create 3D array (2 layers, 3 rows, 4 columns)
arr_3d = np.array([[[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]],

                   [[13, 14, 15, 16],
                    [17, 18, 19, 20],
                    [21, 22, 23, 24]]])

print(arr_3d.shape)  # (2, 3, 4)

# Access single element: array[layer, row, column]
print(arr_3d[0, 0, 0])    # 1 (layer 0, row 0, col 0)
print(arr_3d[1, 2, 3])    # 24 (layer 1, row 2, col 3)

# Get entire layer
layer_0 = arr_3d[0, :, :]  # or arr_3d[0]
print(layer_0)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# Get specific row from specific layer
row = arr_3d[1, 0, :]      # [13, 14, 15, 16]

# Get specific column from specific layer
col = arr_3d[0, :, 2]      # [3, 7, 11]
```

### Section 5: Practical Patterns (3 minutes)

**Common 2D slicing patterns:**

```python
import numpy as np

matrix = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20]])

# First n rows
first_2_rows = matrix[:2, :]
print(first_2_rows)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]

# Last n columns
last_2_cols = matrix[:, -2:]
print(last_2_cols)
# [[ 4  5]
#  [ 9 10]
#  [14 15]
#  [19 20]]

# Middle rows
middle = matrix[1:-1, :]
print(middle)
# [[ 6  7  8  9 10]
#  [11 12 13 14 15]]

# Diagonal elements (not slicing, but useful)
diagonal = np.diag(matrix)
print(diagonal)  # [ 1  7 13 19]

# Top-left quadrant
top_left = matrix[:2, :3]
print(top_left)
# [[1 2 3]
#  [6 7 8]]
```

### Section 6: Views vs Copies in Multi-Dimensional Arrays (2 minutes)

**Slicing creates views:**

```python
import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Extract row (view)
row = matrix[1, :]
row[0] = 999

print(matrix)
# [[  1   2   3]
#  [999   5   6]
#  [  7   8   9]]

# Extract sub-matrix (view)
sub = matrix[:2, :2]
sub[0, 0] = 111

print(matrix)
# [[111   2   3]
#  [999   5   6]
#  [  7   8   9]]
```

**Use .copy() for independence:**

```python
row_copy = matrix[1, :].copy()
row_copy[0] = 777
# matrix unchanged
```

### Summary (1 minute)

**Key Takeaways:**

1. **2D Indexing**: `array[row, column]`
   - Extract rows: `array[row, :]`
   - Extract columns: `array[:, column]`
   - Sub-matrices: `array[r1:r2, c1:c2]`

2. **3D Indexing**: `array[layer, row, column]`
   - Access by layer, then row, then column

3. **Advanced patterns:**
   - Step in any dimension: `array[::2, ::2]`
   - Reverse: `array[::-1, :]` or `array[:, ::-1]`
   - Borders: `array[1:-1, 1:-1]`

4. **Important:** Slicing creates views
   - Modifications affect original
   - Use `.copy()` for independent data

**Remember:**
- Comma separates dimensions: `[row, col]`
- Colon (`:`) means "all" in that dimension
- Slicing works same way in each dimension
- Negative indices work in all dimensions

**Next Steps:**
Now you'll learn Boolean indexing to select elements based on conditions!
