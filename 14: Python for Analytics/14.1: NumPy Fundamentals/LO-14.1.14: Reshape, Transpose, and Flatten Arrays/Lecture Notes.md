## Reshape, Transpose, and Flatten Arrays

### Understanding Array Shape

```python
import numpy as np

# 1D array
arr1d = np.array([1, 2, 3, 4, 5, 6])
print(arr1d.shape)  # (6,)

# 2D array
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])
print(arr2d.shape)  # (2, 3)

# Check properties
print(arr2d.size)   # 6 (total elements)
print(arr2d.ndim)   # 2 (number of dimensions)
```

---

### Reshaping Arrays

**Basic reshape:**

```python
arr = np.array([1, 2, 3, 4, 5, 6])

# 1D to 2D
arr.reshape(2, 3)
# [[1 2 3]
#  [4 5 6]]

arr.reshape(3, 2)
# [[1 2]
#  [3 4]
#  [5 6]]
```

**Using -1 for automatic dimension:**

```python
arr = np.arange(1, 13)  # [1, 2, ..., 12]

# NumPy calculates the dimension
arr.reshape(3, -1)   # (3, 4)
arr.reshape(-1, 4)   # (3, 4)
arr.reshape(2, 2, -1)  # (2, 2, 3)
```

**Rules:**
- Total elements must match
- Can only use -1 once
- Returns view when possible

---

### Transpose

**Swap axes:**

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr.shape)  # (2, 3)

# Transpose
transposed = arr.T
print(transposed)
# [[1 4]
#  [2 5]
#  [3 6]]
print(transposed.shape)  # (3, 2)
```

**Transpose returns a view:**

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

---

### Flattening Arrays

**flatten() - creates copy:**

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

flat = arr.flatten()
print(flat)  # [1 2 3 4 5 6]

# Modifying doesn't affect original
flat[0] = 999
print(arr)  # [[1 2 3] [4 5 6]] - unchanged
```

**ravel() - returns view:**

```python
raveled = arr.ravel()
print(raveled)  # [1 2 3 4 5 6]

# Modifying affects original
raveled[0] = 999
print(arr)  # [[999 2 3] [4 5 6]] - changed!
```

**reshape(-1) - also flattens:**

```python
flat = arr.reshape(-1)
print(flat)  # [1 2 3 4 5 6]
```

**Comparison:**
- `flatten()`: Copy (safe, independent)
- `ravel()`: View (fast, modifies original)
- `reshape(-1)`: View (fast, modifies original)

---

### Order Parameter

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# C order (row-major, default)
arr.flatten(order='C')  # [1 2 3 4 5 6]

# F order (column-major)
arr.flatten(order='F')  # [1 4 2 5 3 6]
```

---

### Practical Applications

**Prepare data for ML:**

```python
# Image data (64x64 pixels)
image = np.random.rand(64, 64)

# Flatten for model
flat_image = image.reshape(-1)  # (4096,)
```

**Reshape time series:**

```python
# 28 daily temperatures
temps = np.random.randint(15, 35, 28)

# Reshape to weeks
weekly = temps.reshape(4, 7)

# Weekly averages
weekly_avg = weekly.mean(axis=1)
```

**Matrix operations:**

```python
# Feature matrix
features = np.random.randn(100, 5)

# Transpose for calculations
features_T = features.T  # (5, 100)
```

---

### Key Takeaways

1. **Reshape:**
   - Changes shape without changing data
   - Use `-1` for automatic dimension
   - Total elements must match
   - Returns view when possible

2. **Transpose:**
   - `.T` swaps axes
   - Rows ↔ Columns
   - Returns view

3. **Flatten:**
   - `flatten()` → copy
   - `ravel()` → view
   - `reshape(-1)` → view

**Remember:**
- Views share memory with original
- Copies are independent
- Check shapes with `.shape`
- Use `-1` for flexibility
