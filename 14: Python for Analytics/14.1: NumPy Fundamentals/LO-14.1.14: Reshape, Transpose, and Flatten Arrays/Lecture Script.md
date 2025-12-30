### Reshape, Transpose, and Flatten Arrays

### Hook (2 minutes)

"Imagine you have a 1D array of 12 elements but need it as a 3x4 matrix, or you have a matrix that needs to be transposed for matrix multiplication. NumPy provides powerful tools to reshape, transpose, and flatten arrays without copying data. These operations are fundamental for data manipulation, especially in machine learning and data science!"

### Section 1: Understanding Array Shape (2 minutes)

**Array shape basics:**

```python
import numpy as np

# 1D array
arr1d = np.array([1, 2, 3, 4, 5, 6])
print(f"1D shape: {arr1d.shape}")  # (6,)

# 2D array
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])
print(f"2D shape: {arr2d.shape}")  # (2, 3)

# 3D array
arr3d = np.array([[[1, 2], [3, 4]],
                  [[5, 6], [7, 8]]])
print(f"3D shape: {arr3d.shape}")  # (2, 2, 2)
```

**Total elements:**

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(f"Shape: {arr.shape}")  # (2, 3)
print(f"Size: {arr.size}")    # 6
print(f"Ndim: {arr.ndim}")    # 2
```

### Section 2: Reshaping Arrays (4 minutes)

**Basic reshape:**

```python
import numpy as np

# 1D to 2D
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)
print(reshaped)
# [[1 2 3]
#  [4 5 6]]

# Different reshape
reshaped = arr.reshape(3, 2)
print(reshaped)
# [[1 2]
#  [3 4]
#  [5 6]]
```

**Rules for reshaping:**
- Total elements must match
- `reshape(2, 3)` needs 6 elements
- `reshape(2, 4)` would error with 6 elements

**Using -1 for automatic dimension:**

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Let NumPy calculate one dimension
reshaped = arr.reshape(2, -1)  # (2, 4)
print(reshaped)
# [[1 2 3 4]
#  [5 6 7 8]]

# Or
reshaped = arr.reshape(-1, 4)  # (2, 4)

# Or
reshaped = arr.reshape(-1, 2)  # (4, 2)
```

**Reshaping to higher dimensions:**

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# 1D to 3D
reshaped = arr.reshape(2, 2, 2)
print(reshaped)
# [[[1 2]
#   [3 4]]
#  [[5 6]
#   [7 8]]]
```

### Section 3: Transpose Operation (3 minutes)

**Basic transpose:**

```python
import numpy as np

# 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(f"Original shape: {arr.shape}")  # (2, 3)

# Transpose
transposed = arr.T
print(transposed)
# [[1 4]
#  [2 5]
#  [3 6]]
print(f"Transposed shape: {transposed.shape}")  # (3, 2)
```

**How transpose works:**
```
Original (2x3):     Transposed (3x2):
[[1, 2, 3],         [[1, 4],
 [4, 5, 6]]          [2, 5],
                     [3, 6]]

Rows become columns
Columns become rows
```

**Using transpose() method:**

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Same as .T
transposed = arr.transpose()
print(transposed)
```

**Transpose is a view:**

```python
arr = np.array([[1, 2],
                [3, 4]])

trans = arr.T
trans[0, 0] = 999

print(arr)
# [[999   2]
#  [  3   4]]
# Original changed!
```

### Section 4: Flattening Arrays (3 minutes)

**Using flatten():**

```python
import numpy as np

# 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Flatten to 1D (creates copy)
flat = arr.flatten()
print(flat)  # [1 2 3 4 5 6]

# Modifying doesn't affect original
flat[0] = 999
print(arr)
# [[1 2 3]
#  [4 5 6]]
# Original unchanged
```

**Using ravel():**

```python
# Ravel to 1D (returns view when possible)
raveled = arr.ravel()
print(raveled)  # [1 2 3 4 5 6]

# Modifying affects original
raveled[0] = 999
print(arr)
# [[999   2   3]
#  [  4   5   6]]
# Original changed!
```

**flatten() vs ravel():**
- `flatten()`: Always creates a copy
- `ravel()`: Returns view when possible (faster)

**Using reshape(-1):**

```python
# Another way to flatten
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

flat = arr.reshape(-1)
print(flat)  # [1 2 3 4 5 6]
```

### Section 5: Advanced Reshaping (2 minutes)

**Reshape with order parameter:**

```python
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# C order (row-major, default)
flat_c = arr.flatten(order='C')
print(flat_c)  # [1 2 3 4 5 6]

# F order (column-major)
flat_f = arr.flatten(order='F')
print(flat_f)  # [1 4 2 5 3 6]
```

**Adding dimensions:**

```python
arr = np.array([1, 2, 3])  # Shape: (3,)

# Add dimension
reshaped = arr.reshape(1, 3)   # (1, 3)
reshaped = arr.reshape(3, 1)   # (3, 1)
reshaped = arr.reshape(1, 3, 1)  # (1, 3, 1)
```

### Section 6: Practical Applications (3 minutes)

**Example 1: Prepare data for machine learning**

```python
import numpy as np

# Image data (64x64 pixels, RGB)
image = np.random.randint(0, 256, (64, 64, 3))
print(f"Image shape: {image.shape}")  # (64, 64, 3)

# Flatten for ML model
flat_image = image.reshape(-1)
print(f"Flattened shape: {flat_image.shape}")  # (12288,)

# Or flatten but keep RGB channels
flat_image = image.reshape(-1, 3)
print(f"Alternative shape: {flat_image.shape}")  # (4096, 3)
```

**Example 2: Reshape time series data**

```python
# Daily temperatures for 4 weeks (28 days)
temps = np.random.randint(15, 35, 28)

# Reshape to weeks x days
weekly = temps.reshape(4, 7)
print("Weekly temperatures:")
print(weekly)

# Calculate weekly averages
weekly_avg = weekly.mean(axis=1)
print(f"Weekly averages: {weekly_avg}")
```

**Example 3: Matrix operations**

```python
# Feature matrix (100 samples, 5 features)
features = np.random.randn(100, 5)

# Transpose for different calculation
features_T = features.T  # (5, 100)

# Covariance matrix
cov = features_T @ features / 100  # (5, 5)
```

### Summary (1 minute)

**Key Takeaways:**

1. **Reshape:**
   - `reshape(rows, cols)` changes shape
   - Total elements must match
   - Use `-1` for automatic dimension
   - Returns view when possible

2. **Transpose:**
   - `.T` or `.transpose()` swaps axes
   - Rows become columns
   - Returns view (modifies original)

3. **Flatten:**
   - `flatten()` creates 1D copy
   - `ravel()` creates 1D view (faster)
   - `reshape(-1)` also flattens

4. **Important notes:**
   - Check shapes with `.shape`
   - Transpose and ravel return views
   - Flatten creates copy
   - Use `-1` for flexibility

**Remember:**
- Reshaping doesn't change data, only view
- Total elements must be conserved
- Views share memory with original
- Useful for data preparation and transformation

**Next Steps:**
You've learned to manipulate array shapes! Next, you'll learn to combine and split arrays using stack, concatenate, and split operations.
