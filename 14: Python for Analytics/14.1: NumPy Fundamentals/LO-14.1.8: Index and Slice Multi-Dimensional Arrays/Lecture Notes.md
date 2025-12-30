## Index and Slice Multi-Dimensional Arrays

### Indexing 2D Arrays

**Syntax:** `array[row, column]`

```python
import numpy as np

matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

# Access elements
print(matrix[0, 0])    # 10
print(matrix[1, 2])    # 60
print(matrix[-1, -1])  # 90

# Modify element
matrix[1, 1] = 999
```

---

### Slicing Rows and Columns

**Extract rows:** `array[row, :]`

**Extract columns:** `array[:, column]`

```python
# Get entire row
row_1 = matrix[1, :]   # [40, 50, 60]

# Get entire column
col_0 = matrix[:, 0]   # [10, 40, 70]

# Extract sub-matrix
sub = matrix[0:2, 1:3]
# [[20 30]
#  [50 60]]
```

---

### Advanced 2D Slicing

**Step parameter in both dimensions:**

```python
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

# Reverse rows
print(data[::-1, :])

# Reverse columns
print(data[:, ::-1])

# Remove borders
inner = data[1:-1, 1:-1]
# [[ 6  7]
#  [10 11]]
```

---

### 3D Array Indexing

**Syntax:** `array[layer, row, column]`

```python
arr_3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                   [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])

print(arr_3d.shape)  # (2, 3, 3) - 2 layers, 3 rows, 3 columns

# Access element
print(arr_3d[0, 0, 0])    # 1
print(arr_3d[1, 2, 3])    # Indexer

# Get entire layer
layer_0 = arr_3d[0, :, :]  # or arr_3d[0]

# Get row from specific layer
row = arr_3d[1, 0, :]      # [13, 14, 15]

# Get column from specific layer
col = arr_3d[0, :, 2]      # [3, 6, 9]
```

---

### Common Slicing Patterns

```python
matrix = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20]])

# First n rows
first_2_rows = matrix[:2, :]
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]

# Last n columns
last_2_cols = matrix[:, -2:]
# [[ 4  5]
#  [ 9 10]
#  [14 15]
#  [19 20]]

# Middle rows
middle = matrix[1:-1, :]

# Top-left quadrant
top_left = matrix[:2, :3]
# [[1 2 3]
#  [6 7 8]]
```

---

### Views vs Copies

**Slicing creates views:**

```python
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
```

**Use .copy() for independence:**

```python
row_copy = matrix[1, :].copy()
row_copy[0] = 777
# matrix unchanged
```

---

### Key Takeaways

1. **2D Indexing**: `array[row, column]`
   - Rows: `array[row, :]`
   - Columns: `array[:, column]`
   - Sub-matrices: `array[r1:r2, c1:c2]`

2. **3D Indexing**: `array[layer, row, column]`
   - Layer then row then column

3. **Advanced patterns:**
   - Step: `array[::2, ::2]`
   - Reverse: `array[::-1, :]`
   - Borders: `array[1:-1, 1:-1]`

4. **Important:** Slicing creates views
   - Use `.copy()` for independent data

**Remember:**
- Comma separates dimensions
- Colon (`:`) means "all"
- Negative indices work in all dimensions
