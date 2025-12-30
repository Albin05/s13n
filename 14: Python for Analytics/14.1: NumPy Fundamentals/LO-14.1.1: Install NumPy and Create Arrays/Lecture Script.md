### Install NumPy and Create Arrays

### Hook (2 minutes)

"Imagine you need to perform calculations on a million numbers. Using Python lists would be slow and memory-intensive. NumPy solves this problem by providing arrays that are 50-100x faster than Python lists!"

NumPy (Numerical Python) is the foundation of data science in Python - used by pandas, scikit-learn, TensorFlow, and more.

### Section 1: What is NumPy? (3 minutes)

**NumPy** is a Python library for numerical computing that provides:
- Fast, multi-dimensional arrays (ndarray)
- Mathematical functions for array operations
- Tools for linear algebra, statistics, and more

**Why NumPy over Python lists?**
- Speed: 50-100x faster due to C implementation
- Memory: More efficient storage
- Functionality: Built-in mathematical operations
- Broadcasting: Perform operations on arrays of different shapes

### Section 2: Installing NumPy (3 minutes)

**Installation using pip:**
```bash
pip install numpy
```

**Verify installation:**
```python
import numpy as np
print(np.__version__)  # Check NumPy version
```

**Common convention:**
```python
import numpy as np  # Standard alias
```

This `np` alias is used universally in the NumPy community.

### Section 3: Creating Arrays from Lists (4 minutes)

**1D array from list:**
```python
import numpy as np

# Python list
numbers = [1, 2, 3, 4, 5]

# Convert to NumPy array
arr = np.array(numbers)
print(arr)        # [1 2 3 4 5]
print(type(arr))  # <class 'numpy.ndarray'>
```

**2D array from nested lists:**
```python
# 2D list (matrix)
matrix = [[1, 2, 3],
          [4, 5, 6]]

arr_2d = np.array(matrix)
print(arr_2d)
# [[1 2 3]
#  [4 5 6]]
```

**3D array:**
```python
# 3D data
data_3d = [[[1, 2], [3, 4]],
           [[5, 6], [7, 8]]]

arr_3d = np.array(data_3d)
print(arr_3d.shape)  # (2, 2, 2)
```

### Section 4: Creating Arrays from Tuples (2 minutes)

```python
# From tuple
tuple_data = (10, 20, 30, 40)
arr = np.array(tuple_data)
print(arr)  # [10 20 30 40]

# From nested tuples
nested = ((1, 2), (3, 4), (5, 6))
arr_2d = np.array(nested)
print(arr_2d)
# [[1 2]
#  [3 4]
#  [5 6]]
```

### Section 5: Array vs List Differences (3 minutes)

**Key differences:**

```python
# Lists: Heterogeneous
python_list = [1, 'hello', 3.14, True]  # Different types OK

# Arrays: Homogeneous
arr = np.array([1, 2, 3, 4])  # All same type

# Type conversion happens automatically
mixed = np.array([1, 2.5, 3])
print(mixed)        # [1.  2.5 3. ]
print(mixed.dtype)  # float64 (all converted to float)
```

**Performance comparison:**
```python
import numpy as np

# Python list
list_nums = list(range(1000000))

# NumPy array
np_nums = np.array(list_nums)

# NumPy operations are much faster!
# list_sum = sum(list_nums)      # Slower
# np_sum = np.sum(np_nums)       # 50-100x faster
```

### Section 6: Specifying Data Types (2 minutes)

```python
# Default type (int64 or float64)
arr1 = np.array([1, 2, 3])
print(arr1.dtype)  # int64

# Specify type explicitly
arr2 = np.array([1, 2, 3], dtype=np.float32)
print(arr2)        # [1. 2. 3.]
print(arr2.dtype)  # float32

# Common data types
arr_int = np.array([1, 2, 3], dtype=np.int32)
arr_float = np.array([1, 2, 3], dtype=np.float64)
arr_bool = np.array([1, 0, 1], dtype=np.bool_)
```

### Section 7: Common Mistakes (2 minutes)

**Mistake 1: Forgetting to import**
```python
# Wrong
arr = array([1, 2, 3])  # NameError

# Correct
import numpy as np
arr = np.array([1, 2, 3])
```

**Mistake 2: Inconsistent dimensions**
```python
# Wrong - jagged array
inconsistent = [[1, 2, 3], [4, 5]]
arr = np.array(inconsistent)  # Creates object array, not ideal

# Correct - consistent dimensions
consistent = [[1, 2, 3], [4, 5, 6]]
arr = np.array(consistent)
```

### Section 8: Practice (2 minutes)

**Problem:** Create a 2D array representing a 3x3 matrix with values 1-9.

**Solution:**
```python
import numpy as np

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

arr = np.array(matrix)
print(arr)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print(arr.shape)  # (3, 3)
```

### Wrap-Up (2 minutes)

**Key takeaways:**
1. NumPy provides fast, efficient arrays for numerical computing
2. Install with `pip install numpy`, import as `np`
3. Create arrays from lists or tuples using `np.array()`
4. Arrays are homogeneous (single data type)
5. Arrays are much faster than Python lists for numerical operations

**Basic syntax:**
```python
import numpy as np

# 1D array
arr_1d = np.array([1, 2, 3])

# 2D array
arr_2d = np.array([[1, 2], [3, 4]])

# With specific dtype
arr_float = np.array([1, 2, 3], dtype=np.float64)
```

**Next lesson:** We'll explore array attributes like shape, dtype, and ndim!
