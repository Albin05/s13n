## Pre-Read: Index and Slice Multi-Dimensional Arrays

### What You'll Learn

In this session, you'll learn to work with multi-dimensional arrays - the foundation for working with matrices, images, and complex datasets. You'll master 2D and 3D array indexing and slicing techniques.

### Why It Matters

Multi-dimensional arrays are everywhere in data analysis:

1. **Tabular data**: Rows = records, columns = features
2. **Images**: Height × Width × Color channels (RGB)
3. **Time-series**: Time × Features × Locations
4. **Scientific computing**: Matrices, tensors, simulations

### Key Concepts Preview

**2D Arrays (Matrices):**
- Access elements: `array[row, column]`
- Extract rows: `array[row, :]`
- Extract columns: `array[:, column]`
- Sub-matrices: `array[r1:r2, c1:c2]`

**3D Arrays:**
- Think of them as stacks of 2D arrays (layers)
- Access: `array[layer, row, column]`
- Common in image processing and video data

**Examples:**
```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

matrix[0, 0]      # 1 (first row, first column)
matrix[1, :]      # [4, 5, 6] (entire second row)
matrix[:, 2]      # [3, 6, 9] (entire third column)
matrix[:2, :2]    # [[1, 2], [4, 5]] (top-left 2x2)
```

### What to Expect

You'll learn:
1. 2D array indexing with `[row, column]` syntax
2. Extracting rows, columns, and sub-matrices
3. Advanced slicing with step parameter
4. Working with 3D arrays
5. Practical patterns for data analysis

### Prepare

Make sure you have:
- Completed the 1D array slicing lesson
- NumPy installed
- Understanding of array shapes

### Quick Exercise

Predict the output:
```python
data = np.array([[10, 20], [30, 40], [50, 60]])

data[1, 0]      # ?
data[:, 1]      # ?
data[0:2, :]    # ?
```

Answers: 30, [20 40 60], [[10 20] [30 40]]

Understanding multi-dimensional indexing is crucial for effective data manipulation!
