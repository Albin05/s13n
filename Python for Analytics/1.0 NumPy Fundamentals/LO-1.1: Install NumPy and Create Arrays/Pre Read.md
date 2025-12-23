# Install NumPy and Create Arrays - Pre Read

## Introduction to NumPy

NumPy (Numerical Python) is the fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.

## Why NumPy?

### Advantages over Python Lists
1. **Performance**: NumPy arrays are up to 50x faster than Python lists
2. **Memory Efficiency**: Uses less memory than lists
3. **Vectorization**: Enables operations on entire arrays without loops
4. **Broadcasting**: Automatic element-wise operations on arrays of different shapes
5. **Rich Functionality**: Extensive mathematical and statistical functions

### Real-World Applications
- Data Analysis and Manipulation
- Machine Learning and AI
- Scientific Computing
- Image Processing
- Financial Modeling
- Signal Processing

## Installing NumPy

### Using pip (Recommended)
```bash
pip install numpy
```

### Using conda (Anaconda/Miniconda)
```bash
conda install numpy
```

### Verifying Installation
```python
import numpy as np
print(np.__version__)  # Should print version number like '1.24.3'
```

## Creating NumPy Arrays

### 1. From Python Lists

**1D Array (Vector)**
```python
import numpy as np

# From a list
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d)  # Output: [1 2 3 4 5]
print(type(arr_1d))  # Output: <class 'numpy.ndarray'>
```

**2D Array (Matrix)**
```python
# From nested lists
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(arr_2d)
# Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
```

**3D Array**
```python
# From deeply nested lists
arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])
print(arr_3d.shape)  # Output: (2, 2, 2)
```

### 2. From Python Tuples

```python
# Tuples work just like lists
arr_from_tuple = np.array((10, 20, 30, 40))
print(arr_from_tuple)  # Output: [10 20 30 40]
```

### 3. Data Type Specification

```python
# Specify data type explicitly
int_array = np.array([1.5, 2.7, 3.9], dtype=int)
print(int_array)  # Output: [1 2 3]

float_array = np.array([1, 2, 3], dtype=float)
print(float_array)  # Output: [1. 2. 3.]

complex_array = np.array([1, 2, 3], dtype=complex)
print(complex_array)  # Output: [1.+0.j 2.+0.j 3.+0.j]
```

## Key Differences: Lists vs NumPy Arrays

| Feature | Python List | NumPy Array |
|---------|------------|-------------|
| Data Types | Can store mixed types | Homogeneous (single type) |
| Memory | More memory overhead | Memory efficient |
| Speed | Slower for numerical operations | Much faster (vectorized) |
| Size | Dynamic (can grow/shrink) | Fixed size |
| Operations | Limited mathematical operations | Rich mathematical functions |
| Dimensions | 1D only (nested for 2D+) | True multi-dimensional |

## Common Pitfalls to Avoid

1. **Forgetting to import NumPy**
   ```python
   # ❌ Wrong
   arr = array([1, 2, 3])  # NameError

   # ✅ Correct
   import numpy as np
   arr = np.array([1, 2, 3])
   ```

2. **Modifying arrays accidentally**
   ```python
   arr1 = np.array([1, 2, 3])
   arr2 = arr1  # This is a reference, not a copy!
   arr2[0] = 99
   print(arr1)  # Output: [99 2 3] - arr1 is also changed!

   # Use .copy() to create an independent copy
   arr2 = arr1.copy()
   ```

3. **Mixed data types in arrays**
   ```python
   # NumPy will upcast to accommodate all types
   mixed = np.array([1, 2.5, 'three'])
   print(mixed.dtype)  # Output: <U32 (Unicode string)
   print(mixed)  # Output: ['1' '2.5' 'three']
   ```

## Best Practices

1. **Always use the alias `np`**
   ```python
   import numpy as np  # Standard convention
   ```

2. **Check array properties before operations**
   ```python
   arr = np.array([[1, 2], [3, 4]])
   print(f"Shape: {arr.shape}")
   print(f"Size: {arr.size}")
   print(f"Type: {arr.dtype}")
   ```

3. **Use appropriate data types**
   - Use `int32` or `int64` for integers
   - Use `float32` or `float64` for decimals
   - Choose based on memory constraints and precision needs

## What's Next?

After mastering array creation, you'll learn about:
- Array attributes (shape, dtype, ndim, size)
- Specialized array creation functions (zeros, ones, arange, linspace)
- Array indexing and slicing
- Array operations and broadcasting

## Additional Resources

- [NumPy Official Documentation](https://numpy.org/doc/stable/)
- [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
- [NumPy for Absolute Beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)
