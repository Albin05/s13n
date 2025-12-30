## Editorials: Understand Array Attributes (shape, dtype, ndim)

### Q1 Solution: Inspect 1D Array Attributes

```python
import numpy as np

# Create array from list
arr = np.array([15, 25, 35, 45, 55, 65])

# Print attributes
print(arr.shape)
print(arr.dtype)
print(arr.ndim)
print(arr.size)
```

**Explanation:**
- `shape` returns `(6,)` - a tuple with one element indicating 6 elements in 1D
- `dtype` shows `int64` - the default integer type on 64-bit systems
- `ndim` returns `1` - indicating a one-dimensional array
- `size` returns `6` - the total number of elements

---

### Q2 Solution: Inspect 2D Array Attributes

```python
import numpy as np

# Create 2D array
arr = np.array([[10, 20, 30, 40],
                [50, 60, 70, 80],
                [90, 100, 110, 120]])

# Print attributes
print(f"Shape: {arr.shape}")
print(f"Dimensions: {arr.ndim}")
print(f"Size: {arr.size}")
```

**Explanation:**
- `shape` returns `(3, 4)` - 3 rows and 4 columns
- `ndim` returns `2` - a two-dimensional array (matrix)
- `size` returns `12` - total elements (3 × 4 = 12)

---

### Q3 Solution: Extract Shape Components

```python
import numpy as np

# Create 5x3 array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12],
                [13, 14, 15]])

# Extract shape components
rows, cols = arr.shape

# Print results
print(f"Number of rows: {rows}")
print(f"Number of columns: {cols}")
```

**Explanation:**
- `arr.shape` returns a tuple `(5, 3)`
- We can unpack this tuple into two variables: `rows` and `cols`
- This technique is useful when you need to access dimensions separately

**Alternative solution:**
```python
print(f"Number of rows: {arr.shape[0]}")
print(f"Number of columns: {arr.shape[1]}")
```

---

### Q4 Solution: Compare Memory Usage

```python
import numpy as np

# Create arrays with different dtypes
arr_int32 = np.array([100, 200, 300, 400, 500], dtype=np.int32)
arr_int64 = np.array([100, 200, 300, 400, 500], dtype=np.int64)

# Print memory usage for int32
print("int32 array:")
print(f"  Item size: {arr_int32.itemsize} bytes")
print(f"  Total bytes: {arr_int32.nbytes} bytes")

# Print memory usage for int64
print("\nint64 array:")
print(f"  Item size: {arr_int64.itemsize} bytes")
print(f"  Total bytes: {arr_int64.nbytes} bytes")
```

**Explanation:**
- `itemsize` shows bytes per element: int32 uses 4 bytes, int64 uses 8 bytes
- `nbytes` shows total memory: calculated as size × itemsize
- int32 total: 5 elements × 4 bytes = 20 bytes
- int64 total: 5 elements × 8 bytes = 40 bytes
- **Key insight**: Using smaller data types can save memory when working with large datasets

---

### Q5 Solution: Array Type Analysis

```python
import numpy as np

def analyze_array(arr):
    """Analyze NumPy array attributes."""
    # Determine array type based on dimensions
    if arr.ndim == 1:
        array_type = 'vector'
    elif arr.ndim == 2:
        array_type = 'matrix'
    else:
        array_type = '3D+'

    # Create result dictionary
    result = {
        'type': array_type,
        'shape': arr.shape,
        'dtype': str(arr.dtype),
        'total_elements': arr.size
    }

    return result

# Test with array 1
arr1 = np.array([1, 2, 3, 4])
print(f"Array 1: {analyze_array(arr1)}")

# Test with array 2
arr2 = np.array([[1, 2], [3, 4], [5, 6]])
print(f"Array 2: {analyze_array(arr2)}")
```

**Explanation:**
- The function uses `ndim` to determine the array type
- Conditional logic classifies arrays as 'vector' (1D), 'matrix' (2D), or '3D+' (3+ dimensions)
- `str(arr.dtype)` converts the dtype object to a string for the dictionary
- This pattern is useful for validating array structure in real-world applications

**Key Concepts Covered:**
1. Using shape, dtype, ndim, and size attributes
2. Unpacking shape tuples to extract dimensions
3. Comparing memory usage with itemsize and nbytes
4. Writing functions that analyze array properties
5. Conditional logic based on array dimensions
