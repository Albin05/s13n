### Apply Broadcasting Rules

### Hook (2 minutes)

"You've learned to perform operations on arrays of the same shape, but what if you want to add a scalar to an array, or multiply a 1D array with a 2D matrix? NumPy's broadcasting is a powerful mechanism that allows you to perform operations on arrays of different shapes without creating copies. Understanding broadcasting rules is crucial for writing efficient, elegant NumPy code!"

### Section 1: What is Broadcasting? (3 minutes)

**Basic concept:**

```python
import numpy as np

# Scalar broadcasting
arr = np.array([1, 2, 3, 4, 5])
result = arr + 10
print(result)  # [11 12 13 14 15]
```

**How it works:**
```
Original array:  [1, 2, 3, 4, 5]
Scalar:           10

Broadcasting:    [10, 10, 10, 10, 10]  (stretched)
Result:          [11, 12, 13, 14, 15]
```

**Key point:**
- NumPy doesn't actually create copies
- Broadcasting happens virtually for efficiency
- Operations appear as if arrays had same shape

**Example with 2D array:**

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Add 10 to all elements
result = matrix + 10
print(result)
# [[11 12 13]
#  [14 15 16]
#  [17 18 19]]
```

### Section 2: Broadcasting Rule 1 - Scalar to Array (2 minutes)

**Scalar broadcasting:**

```python
import numpy as np

# 1D array
arr = np.array([10, 20, 30, 40])
result = arr * 5
print(result)  # [ 50 100 150 200]

# 2D array
matrix = np.array([[1, 2],
                   [3, 4]])
result = matrix * 10
print(result)
# [[10 20]
#  [30 40]]
```

**All arithmetic operations:**

```python
arr = np.array([10, 20, 30])

print(arr + 5)   # [15 25 35]
print(arr - 5)   # [ 5 15 25]
print(arr * 5)   # [ 50 100 150]
print(arr / 5)   # [2. 4. 6.]
print(arr ** 2)  # [ 100  400  900]
```

### Section 3: Broadcasting Rule 2 - 1D to 2D Arrays (4 minutes)

**Broadcasting along rows:**

```python
import numpy as np

# 2D array (3x4)
matrix = np.array([[10, 20, 30, 40],
                   [50, 60, 70, 80],
                   [90, 100, 110, 120]])

# 1D array (4 elements)
row_vector = np.array([1, 2, 3, 4])

# Broadcast along rows
result = matrix + row_vector
print(result)
# [[ 11  22  33  44]
#  [ 51  62  73  84]
#  [ 91 102 113 124]]
```

**How it works:**
```
Matrix (3x4):
[[10, 20, 30, 40],
 [50, 60, 70, 80],
 [90, 100, 110, 120]]

Row vector (4):
[1, 2, 3, 4]

Broadcasting (stretched to 3x4):
[[1, 2, 3, 4],
 [1, 2, 3, 4],
 [1, 2, 3, 4]]

Result: Element-wise addition
```

**Broadcasting along columns:**

```python
# 2D array (3x4)
matrix = np.array([[10, 20, 30, 40],
                   [50, 60, 70, 80],
                   [90, 100, 110, 120]])

# Column vector (3x1)
col_vector = np.array([[1],
                       [2],
                       [3]])

# Broadcast along columns
result = matrix + col_vector
print(result)
# [[ 11  21  31  41]
#  [ 52  62  72  82]
#  [ 93 103 113 123]]
```

### Section 4: Broadcasting Rules Explained (3 minutes)

**The three broadcasting rules:**

1. **If arrays have different dimensions, pad with 1s on the left**
2. **Arrays are compatible if dimensions are equal or one of them is 1**
3. **Stretch size-1 dimensions to match the larger array**

**Rule examples:**

```python
import numpy as np

# Shape (3,) and scalar
arr = np.array([1, 2, 3])  # Shape: (3,)
scalar = 5                  # Shape: ()

# Broadcasting works:
# () → (1,) → (3,)
result = arr + scalar  # [6 7 8]

# Shape (3, 4) and (4,)
matrix = np.ones((3, 4))   # Shape: (3, 4)
vector = np.array([1, 2, 3, 4])  # Shape: (4,)

# Broadcasting works:
# (4,) → (1, 4) → (3, 4)
result = matrix + vector
```

**Compatible shapes:**
```
(3, 4) + (4,)   → Compatible ✓
(3, 4) + (3, 1) → Compatible ✓
(3, 4) + (3, 4) → Compatible ✓
(3, 4) + (3,)   → NOT Compatible ✗
(3, 4) + (4, 3) → NOT Compatible ✗
```

### Section 5: Common Broadcasting Patterns (3 minutes)

**Pattern 1: Normalize rows**

```python
import numpy as np

# Data (3x4)
data = np.array([[10, 20, 30, 40],
                 [50, 60, 70, 80],
                 [90, 100, 110, 120]])

# Row means (3,) → (3, 1)
row_means = data.mean(axis=1, keepdims=True)
print(row_means)
# [[ 25.]
#  [ 65.]
#  [105.]]

# Normalize each row
normalized = data - row_means
print(normalized)
# [[-15. -5.   5.  15.]
#  [-15. -5.   5.  15.]
#  [-15. -5.   5.  15.]]
```

**Pattern 2: Normalize columns**

```python
# Column means (1, 4)
col_means = data.mean(axis=0, keepdims=True)
print(col_means)  # [[ 50.  60.  70.  80.]]

# Normalize each column
normalized = data - col_means
print(normalized)
# [[-40. -40. -40. -40.]
#  [  0.   0.   0.   0.]
#  [ 40.  40.  40.  40.]]
```

**Pattern 3: Outer product**

```python
a = np.array([1, 2, 3])      # Shape: (3,)
b = np.array([10, 20, 30, 40])  # Shape: (4,)

# Reshape for outer product
result = a.reshape(3, 1) * b.reshape(1, 4)
print(result)
# [[ 10  20  30  40]
#  [ 20  40  60  80]
#  [ 30  60  90 120]]
```

### Section 6: Broadcasting with newaxis (2 minutes)

**Using np.newaxis:**

```python
import numpy as np

# 1D array
arr = np.array([1, 2, 3])  # Shape: (3,)

# Add dimension
col = arr[:, np.newaxis]   # Shape: (3, 1)
print(col)
# [[1]
#  [2]
#  [3]]

# Add dimension at beginning
row = arr[np.newaxis, :]   # Shape: (1, 3)
print(row)  # [[1 2 3]]
```

**Using for broadcasting:**

```python
a = np.array([1, 2, 3])

# Create column and row vectors
col = a[:, np.newaxis]  # (3, 1)
row = a[np.newaxis, :]  # (1, 3)

# Outer product via broadcasting
result = col * row
print(result)
# [[1 2 3]
#  [2 4 6]
#  [3 6 9]]
```

### Section 7: Practical Applications (2 minutes)

**Example 1: Distance matrix**

```python
import numpy as np

# Points (x, y coordinates)
points = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])

# Calculate pairwise distances
# Reshape for broadcasting
p1 = points[:, np.newaxis, :]  # (3, 1, 2)
p2 = points[np.newaxis, :, :]  # (1, 3, 2)

# Euclidean distance
distances = np.sqrt(((p1 - p2) ** 2).sum(axis=2))
print(distances)
# [[0.   2.83 5.66]
#  [2.83 0.   2.83]
#  [5.66 2.83 0.  ]]
```

**Example 2: Apply different operations per row**

```python
# Data
data = np.array([[100, 200, 300],
                 [10, 20, 30],
                 [1, 2, 3]])

# Different multipliers per row
multipliers = np.array([[2],
                        [5],
                        [10]])

result = data * multipliers
print(result)
# [[200 400 600]
#  [ 50 100 150]
#  [ 10  20  30]]
```

### Summary (1 minute)

**Key Takeaways:**

1. **What is broadcasting:**
   - Operates on arrays of different shapes
   - Virtually stretches smaller arrays
   - No actual copying (memory efficient)

2. **Broadcasting rules:**
   - Pad shapes with 1s on left
   - Dimensions must be equal or one must be 1
   - Size-1 dimensions stretch to match

3. **Common patterns:**
   - Scalar to array: `arr + 5`
   - 1D to 2D: `matrix + vector`
   - Row/column operations with `keepdims=True`

4. **Tools for broadcasting:**
   - `np.newaxis` to add dimensions
   - `reshape()` to control shapes
   - `keepdims=True` in aggregations

5. **Compatible shapes:**
   - `(3, 4) + (4,)` ✓
   - `(3, 4) + (3, 1)` ✓
   - `(3, 4) + (3,)` ✗

**Remember:**
- Broadcasting avoids unnecessary copying
- Makes code cleaner and faster
- Understanding shapes is crucial
- Use `array.shape` to debug

**Next Steps:**
You've mastered broadcasting! Next, you'll learn about reshaping, transposing, and flattening arrays to manipulate array dimensions.
