## Pre-Read: Apply Broadcasting Rules

### What You'll Learn

In this session, you'll master broadcasting - NumPy's powerful mechanism for performing operations on arrays of different shapes without creating unnecessary copies. This feature makes NumPy code both elegant and efficient.

### Why It Matters

Broadcasting is essential for:

1. **Memory efficiency**: No need to create duplicate data
2. **Code simplicity**: Clean, readable operations without explicit loops
3. **Performance**: Faster than manually expanding arrays
4. **Flexibility**: Work with arrays of different shapes seamlessly

Real-world examples:
- Normalize datasets by subtracting means
- Apply different transformations to different rows/columns
- Calculate pairwise distances between points
- Apply category-specific discounts to products
- Center data for machine learning

### Key Concepts Preview

**Broadcasting:**
- Operates on arrays of different shapes
- Virtually stretches smaller arrays to match larger ones
- No actual data copying (memory efficient)

**Basic examples:**
```python
import numpy as np

# Scalar broadcasting
arr = np.array([1, 2, 3])
result = arr + 10  # [11, 12, 13]

# 1D to 2D broadcasting
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
row = np.array([10, 20, 30])
result = matrix + row
# [[11, 22, 33],
#  [14, 26, 36]]
```

**Broadcasting rules:**
1. Pad shapes with 1s on the left
2. Dimensions must be equal or one must be 1
3. Stretch size-1 dimensions

### What to Expect

You'll learn:
1. What broadcasting is and how it works
2. The three broadcasting rules
3. Scalar to array broadcasting
4. 1D to 2D array broadcasting
5. Using `np.newaxis` to control dimensions
6. Using `keepdims=True` for easy broadcasting
7. Common broadcasting patterns
8. Practical applications

### Prepare

Make sure you have:
- NumPy installed
- Understanding of array shapes
- Knowledge of element-wise operations
- Familiarity with array dimensions

### Quick Example

Try to predict the results:
```python
import numpy as np

# What shape will these have?
a = np.array([1, 2, 3])  # Shape: ?
b = a[:, np.newaxis]      # Shape: ?

# Will these work?
matrix = np.ones((3, 4))
vec1 = np.array([1, 2, 3, 4])
result1 = matrix + vec1   # Works? Shape?

vec2 = np.array([1, 2, 3])
result2 = matrix + vec2   # Works? Shape?

vec3 = np.array([[1], [2], [3]])
result3 = matrix + vec3   # Works? Shape?
```

Answers:
- a shape: (3,)
- b shape: (3, 1)
- result1: Works ✓, shape (3, 4)
- result2: Doesn't work ✗ (incompatible shapes)
- result3: Works ✓, shape (3, 4)

### Compatible Shapes

```
✓ Compatible:
(3, 4) + (4,)    → (3, 4)
(3, 4) + (3, 1)  → (3, 4)
(3, 4) + (1, 4)  → (3, 4)
(3, 1) + (1, 4)  → (3, 4)

✗ Incompatible:
(3, 4) + (3,)    → Error
(3, 4) + (4, 3)  → Error
(3, 4) + (2, 4)  → Error
```

Broadcasting makes NumPy code elegant and efficient - mastering it is essential for effective data manipulation!
