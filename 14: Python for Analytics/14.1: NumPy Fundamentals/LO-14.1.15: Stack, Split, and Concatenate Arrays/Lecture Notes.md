## Stack, Split, and Concatenate Arrays

### Concatenating Arrays

Joins arrays along existing axis:

```python
import numpy as np

# 1D concatenation
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.concatenate([arr1, arr2])
# [1 2 3 4 5 6]

# 2D vertical (axis=0)
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
v_result = np.concatenate([mat1, mat2], axis=0)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# 2D horizontal (axis=1)
h_result = np.concatenate([mat1, mat2], axis=1)
# [[1 2 5 6]
#  [3 4 7 8]]
```

**Key Points:**
- Arrays must have compatible shapes
- axis=0: vertical (add rows)
- axis=1: horizontal (add columns)

---

### Stacking Arrays

**vstack - Vertical Stacking:**

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.vstack([arr1, arr2])
# [[1 2 3]
#  [4 5 6]]
```

**hstack - Horizontal Stacking:**

```python
result = np.hstack([arr1, arr2])
# [1 2 3 4 5 6]
```

**stack - General Stacking:**

```python
# Creates new dimension
result = np.stack([arr1, arr2], axis=0)
# [[1 2 3]
#  [4 5 6]]

result = np.stack([arr1, arr2], axis=1)
# [[1 4]
#  [2 5]
#  [3 6]]
```

**Difference:**
- concatenate: uses existing axis
- stack: creates new axis
- vstack/hstack: shortcuts for common cases

---

### Splitting Arrays

**Equal Splits:**

```python
arr = np.array([1, 2, 3, 4, 5, 6])

# Split into 3 parts
parts = np.split(arr, 3)
# [array([1, 2]), array([3, 4]), array([5, 6])]

# Split at indices
parts = np.split(arr, [2, 4])
# [array([1, 2]), array([3, 4]), array([5, 6])]
```

**2D Splits:**

```python
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])

# Vertical split (rows)
v_parts = np.vsplit(matrix, 2)
# [array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]])]

# Horizontal split (columns)
h_parts = np.hsplit(matrix, 2)
# [array([[1, 2], [5, 6]]), array([[3, 4], [7, 8]])]
```

---

### Unequal Splits

**array_split:**

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Split into 3 (not evenly divisible)
parts = np.array_split(arr, 3)
# [array([1, 2, 3, 4]), array([5, 6, 7]), array([8, 9, 10])]
```

**Comparison:**

| Function | Requirement | Error on Unequal |
|----------|-------------|------------------|
| split() | Even division | Yes |
| array_split() | Any division | No |

---

### Common Patterns

**Combine Data:**

```python
# Multiple sources
data1 = np.array([100, 200, 300])
data2 = np.array([150, 250, 350])
data3 = np.array([120, 220, 320])

combined = np.vstack([data1, data2, data3])
# [[100 200 300]
#  [150 250 350]
#  [120 220 320]]
```

**Train-Test Split:**

```python
data = np.arange(100)

# 80-20 split
train, test = np.split(data, [80])
# train: 80 samples, test: 20 samples

# 70-15-15 split
train, val, test = np.split(data, [70, 85])
```

**Batch Processing:**

```python
samples = [np.array([1, 2, 3]),
           np.array([4, 5, 6]),
           np.array([7, 8, 9])]

batch = np.stack(samples)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
```

---

### Quick Reference

**Combine:**
```python
np.concatenate([a, b], axis=0)  # Existing axis
np.vstack([a, b])               # Vertical
np.hstack([a, b])               # Horizontal
np.stack([a, b], axis=0)        # New axis
```

**Split:**
```python
np.split(arr, 3)                # 3 equal parts
np.split(arr, [2, 5])           # At indices 2 and 5
np.vsplit(arr, 2)               # Split rows
np.hsplit(arr, 2)               # Split columns
np.array_split(arr, 3)          # Allow unequal
```

---

### Key Takeaways

1. **Concatenate:**
   - Joins along existing axis
   - Shapes must match in other dimensions
   - Use axis parameter for control

2. **Stack:**
   - Creates new dimension
   - vstack: rows, hstack: columns
   - stack() for custom axis

3. **Split:**
   - Divide into parts
   - split(): equal parts
   - array_split(): unequal OK
   - vsplit/hsplit: by dimension

4. **Applications:**
   - Data combination
   - Batch processing
   - Train-test splits
   - Feature engineering

**Remember:**
- Choose method based on task
- Check shapes before/after
- Use array_split for flexibility
- Combine with reshape for power
