## Understand Array Attributes (shape, dtype, ndim)

### Introduction to Array Attributes

**What are Array Attributes?**
- Properties that describe characteristics of NumPy arrays
- Provide information about dimensions, data type, and size
- Essential for debugging and optimizing array operations

**Key Attributes:**
- **shape**: Dimensions of the array
- **dtype**: Data type of elements
- **ndim**: Number of dimensions
- **size**: Total number of elements
- **itemsize**: Memory per element
- **nbytes**: Total memory usage

### The shape Attribute

**Definition:**
Returns a tuple representing the dimensions of the array

**Examples:**
```python
import numpy as np

# 1D array
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d.shape)  # (5,)

# 2D array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(arr_2d.shape)  # (2, 3) - 2 rows, 3 columns

# 3D array
arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])
print(arr_3d.shape)  # (2, 2, 2)
```

**Accessing shape components:**
```python
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
rows, cols = arr_2d.shape
print(f"Rows: {rows}, Columns: {cols}")  # Rows: 2, Columns: 3
```

### The dtype Attribute

**Definition:**
Shows the data type of array elements

**Common data types:**
```python
# Integer
int_arr = np.array([1, 2, 3])
print(int_arr.dtype)  # int64

# Float
float_arr = np.array([1.5, 2.7, 3.9])
print(float_arr.dtype)  # float64

# Boolean
bool_arr = np.array([True, False, True])
print(bool_arr.dtype)  # bool

# String
str_arr = np.array(['a', 'b', 'c'])
print(str_arr.dtype)  # <U1
```

**Type upcasting:**
```python
# Mixed types automatically convert
mixed = np.array([1, 2.5, 3])
print(mixed)       # [1.  2.5 3. ]
print(mixed.dtype) # float64
```

**Why dtype matters:**
- **Memory efficiency**: Smaller types use less memory
- **Performance**: Some operations faster with specific types
- **Precision**: Different decimal accuracy

### The ndim Attribute

**Definition:**
Returns the number of dimensions (axes)

**Examples:**
```python
# 1D array
arr_1d = np.array([1, 2, 3, 4])
print(arr_1d.ndim)  # 1

# 2D array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(arr_2d.ndim)  # 2

# 3D array
arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])
print(arr_3d.ndim)  # 3
```

**Use case:**
```python
# Check array structure
if arr.ndim == 2:
    print("This is a matrix")
elif arr.ndim == 1:
    print("This is a vector")
```

### Additional Useful Attributes

**size attribute:**
```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr.size)  # 6 (total elements)
```

**itemsize attribute:**
```python
arr_int32 = np.array([1, 2, 3], dtype=np.int32)
print(arr_int32.itemsize)  # 4 bytes

arr_int64 = np.array([1, 2, 3], dtype=np.int64)
print(arr_int64.itemsize)  # 8 bytes
```

**nbytes attribute:**
```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]], dtype=np.int64)
print(arr.nbytes)  # 48 bytes (6 elements × 8 bytes)
```

### Comprehensive Example

```python
import numpy as np

# Create array
data = np.array([[10, 20, 30, 40],
                 [50, 60, 70, 80],
                 [90, 100, 110, 120]])

# Inspect attributes
print(f"Shape: {data.shape}")           # (3, 4)
print(f"Data type: {data.dtype}")       # int64
print(f"Dimensions: {data.ndim}")       # 2
print(f"Total elements: {data.size}")   # 12
print(f"Bytes per element: {data.itemsize}")  # 8
print(f"Total bytes: {data.nbytes}")    # 96
```

### Key Takeaways

1. **shape**: Tuple showing array dimensions
2. **dtype**: Data type of elements (int64, float64, bool, etc.)
3. **ndim**: Number of dimensions/axes
4. **size**: Total number of elements
5. **itemsize**: Bytes per element
6. **nbytes**: Total memory consumption
7. All attributes are read-only
8. Check shape before operations to avoid dimension errors
