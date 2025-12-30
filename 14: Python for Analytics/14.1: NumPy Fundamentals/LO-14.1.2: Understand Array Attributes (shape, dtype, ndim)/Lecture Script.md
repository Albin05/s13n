### Understand Array Attributes (shape, dtype, ndim)

### Hook (2 minutes)

"When working with large datasets, you need to quickly understand the structure of your data. Is it a vector or a matrix? What type of numbers does it contain? How many elements are there? NumPy provides powerful attributes that answer these questions instantly. Let's explore how to inspect and understand array properties!"

### Section 1: Introduction to Array Attributes (3 minutes)

**What are Array Attributes?**

Array attributes are properties that describe the characteristics of NumPy arrays. They provide essential information about:
- **Dimensions and shape** of the data
- **Data type** of elements
- **Size** and memory usage
- **Number of axes** (dimensions)

**Why are they important?**

Understanding array attributes helps you:
1. Debug array operations and prevent shape mismatches
2. Optimize memory usage by choosing appropriate data types
3. Verify data structure before performing operations
4. Write robust code that handles different array shapes

### Section 2: The shape Attribute (4 minutes)

**What is shape?**

The `shape` attribute returns a **tuple** representing the dimensions of the array.

**1D Array Shape:**
```python
import numpy as np

# 1D array
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d.shape)  # (5,)
```
- Output: `(5,)` means 5 elements in a single dimension
- Note the comma: it's a tuple with one element

**2D Array Shape:**
```python
# 2D array (matrix)
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(arr_2d.shape)  # (2, 3)
```
- Output: `(2, 3)` means 2 rows and 3 columns
- First number = rows, second number = columns

**3D Array Shape:**
```python
# 3D array
arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])
print(arr_3d.shape)  # (2, 2, 2)
```
- Output: `(2, 2, 2)` means 2 blocks, 2 rows, 2 columns

**Accessing shape components:**
```python
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
rows, cols = arr_2d.shape
print(f"Rows: {rows}, Columns: {cols}")  # Rows: 2, Columns: 3
```

### Section 3: The dtype Attribute (4 minutes)

**What is dtype?**

The `dtype` attribute tells you the **data type** of elements in the array.

**Common Data Types:**

```python
# Integer array
int_arr = np.array([1, 2, 3])
print(int_arr.dtype)  # int64 (64-bit integer)

# Float array
float_arr = np.array([1.5, 2.7, 3.9])
print(float_arr.dtype)  # float64 (64-bit float)

# Boolean array
bool_arr = np.array([True, False, True])
print(bool_arr.dtype)  # bool

# String array
str_arr = np.array(['a', 'b', 'c'])
print(str_arr.dtype)  # <U1 (Unicode string, 1 character)
```

**Type Upcasting:**

When mixing types, NumPy automatically converts to the most general type:

```python
# Mixed int and float
mixed = np.array([1, 2.5, 3])
print(mixed)       # [1.  2.5 3. ]
print(mixed.dtype) # float64
```

**Why dtype matters:**
- **Memory efficiency**: int32 uses half the memory of int64
- **Performance**: Some operations are faster with specific types
- **Precision**: float32 vs float64 affects decimal accuracy

**Checking dtype:**
```python
arr = np.array([1.1, 2.2, 3.3])
if arr.dtype == np.float64:
    print("Array contains 64-bit floats")
```

### Section 4: The ndim Attribute (3 minutes)

**What is ndim?**

The `ndim` attribute returns the **number of dimensions** (axes) of the array.

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

**Relationship between ndim and shape:**
```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(f"Dimensions: {arr.ndim}")       # 2
print(f"Shape: {arr.shape}")           # (2, 3)
print(f"Shape length: {len(arr.shape)}") # 2 (same as ndim)
```

**Use case:**
```python
# Check if array is suitable for matrix operations
if arr.ndim == 2:
    print("This is a matrix - can perform linear algebra")
elif arr.ndim == 1:
    print("This is a vector")
```

### Section 5: Additional Useful Attributes (2 minutes)

**size Attribute:**

Returns the total number of elements:

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr.size)  # 6 (2 rows × 3 columns)
```

**itemsize Attribute:**

Returns the size (in bytes) of each element:

```python
arr_int32 = np.array([1, 2, 3], dtype=np.int32)
print(arr_int32.itemsize)  # 4 bytes

arr_int64 = np.array([1, 2, 3], dtype=np.int64)
print(arr_int64.itemsize)  # 8 bytes
```

**nbytes Attribute:**

Returns total bytes consumed by array elements:

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]], dtype=np.int64)
print(arr.nbytes)  # 48 bytes (6 elements × 8 bytes)
```

### Practice Example (2 minutes)

**Comprehensive attribute inspection:**

```python
import numpy as np

# Create a sample array
data = np.array([[10, 20, 30, 40],
                 [50, 60, 70, 80],
                 [90, 100, 110, 120]])

# Inspect all attributes
print("Array:")
print(data)
print(f"\nShape: {data.shape}")           # (3, 4)
print(f"Data type: {data.dtype}")         # int64
print(f"Dimensions: {data.ndim}")         # 2
print(f"Total elements: {data.size}")     # 12
print(f"Bytes per element: {data.itemsize}") # 8
print(f"Total bytes: {data.nbytes}")      # 96
```

### Summary (2 minutes)

**Key Takeaways:**

1. **shape**: Tuple showing dimensions (e.g., `(2, 3)` for 2 rows, 3 columns)
2. **dtype**: Data type of array elements (int64, float64, bool, etc.)
3. **ndim**: Number of dimensions/axes (1 for vector, 2 for matrix, etc.)
4. **size**: Total number of elements in the array
5. **itemsize**: Memory size of each element in bytes
6. **nbytes**: Total memory consumed by array data

**Remember:**
- Always check `shape` before array operations to avoid dimension mismatches
- Use `dtype` to optimize memory and ensure correct numerical precision
- `ndim` helps verify if your array structure matches your expectations
- These attributes are read-only - you can't modify them directly

**Next Steps:**
In the next lesson, we'll learn how to create arrays using specialized functions like `zeros()`, `ones()`, `arange()`, and `linspace()` that give you more control over array attributes from the start.
