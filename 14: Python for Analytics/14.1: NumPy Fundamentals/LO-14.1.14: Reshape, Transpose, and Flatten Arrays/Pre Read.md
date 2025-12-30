## Pre-Read: Reshape, Transpose, and Flatten Arrays

### What You'll Learn

In this session, you'll master array shape manipulation - reshaping arrays to different dimensions, transposing matrices, and flattening multi-dimensional arrays to 1D. These operations are fundamental for data preparation and transformation.

### Why It Matters

Shape manipulation is essential for:

1. **Data preparation**: Prepare data for machine learning models
2. **Matrix operations**: Align arrays for mathematical operations
3. **Data transformation**: Convert between different representations
4. **Memory efficiency**: Use views instead of copies when possible

Real-world examples:
- Reshape image data for neural networks
- Transpose matrices for matrix multiplication
- Flatten multi-dimensional data for algorithms requiring 1D input
- Reorganize time series data into weekly/monthly chunks

### Key Concepts Preview

**Reshape:**
```python
arr = np.array([1, 2, 3, 4, 5, 6])

# 1D to 2D
arr.reshape(2, 3)
# [[1 2 3]
#  [4 5 6]]

# Use -1 for automatic
arr.reshape(-1, 3)  # (2, 3)
```

**Transpose:**
```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

matrix.T
# [[1 4]
#  [2 5]
#  [3 6]]
```

**Flatten:**
```python
arr = np.array([[1, 2], [3, 4]])

arr.flatten()  # [1 2 3 4] (copy)
arr.ravel()    # [1 2 3 4] (view)
```

### What to Expect

You'll learn:
1. Understanding array shape and dimensions
2. Reshaping arrays with reshape()
3. Using -1 for automatic dimension calculation
4. Transposing matrices
5. Flattening with flatten(), ravel(), reshape(-1)
6. Difference between views and copies
7. Practical applications

### Prepare

Make sure you have:
- NumPy installed
- Understanding of array dimensions
- Knowledge of array indexing
- Familiarity with shape concept

### Quick Example

Predict the output:
```python
import numpy as np

arr = np.arange(1, 13)

# What shapes?
shape1 = arr.reshape(3, 4).shape  # ?
shape2 = arr.reshape(-1, 6).shape  # ?
shape3 = arr.reshape(2, 2, 3).shape  # ?

# What happens?
matrix = np.array([[1, 2], [3, 4]])
trans = matrix.T
trans.shape  # ?
```

Answers:
- shape1: (3, 4)
- shape2: (2, 6)
- shape3: (2, 2, 3)
- trans.shape: (2, 2)

### View vs Copy

**Important distinction:**
- **View**: Shares data with original (modifying affects original)
- **Copy**: Independent data (modifying doesn't affect original)

```python
arr = np.array([[1, 2], [3, 4]])

# View operations
arr.T          # View
arr.ravel()    # View
arr.reshape()  # Usually view

# Copy operations
arr.flatten()  # Always copy
```

Shape manipulation is a fundamental skill for effective NumPy usage!
