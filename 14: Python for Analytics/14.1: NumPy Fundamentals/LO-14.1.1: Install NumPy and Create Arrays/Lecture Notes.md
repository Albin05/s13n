## Install NumPy and Create Arrays

### Introduction to NumPy

**What is NumPy?**
- Numerical Python - fundamental package for scientific computing
- Created by Travis Oliphant in 2005
- Foundation for pandas, scikit-learn, TensorFlow, and more

**Why NumPy?**
- 10-100x faster than Python lists
- Memory efficient
- Supports multi-dimensional arrays
- Rich set of mathematical functions

### Installation

**Using pip:**
```bash
pip install numpy
```

**Verify installation:**
```python
import numpy as np
print(np.__version__)
```

**Standard import convention:**
```python
import numpy as np  # Always use 'np' alias
```

### Creating 1D Arrays

**From Python list:**
```python
import numpy as np

numbers = [1, 2, 3, 4, 5]
arr = np.array(numbers)

print(arr)        # [1 2 3 4 5]
print(type(arr))  # <class 'numpy.ndarray'>
print(arr.dtype)  # int64
```

**From tuple:**
```python
tuple_data = (10, 20, 30)
arr = np.array(tuple_data)
print(arr)  # [10 20 30]
```

### Creating 2D Arrays

**From nested lists:**
```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

arr_2d = np.array(matrix)
print(arr_2d)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print(arr_2d.shape)  # (3, 3)
print(arr_2d.ndim)   # 2
```

### Creating 3D Arrays

```python
arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])

print(arr_3d.shape)  # (2, 2, 2)
print(arr_3d.size)   # 8 total elements
```

### Data Types

**Automatic type detection:**
```python
int_arr = np.array([1, 2, 3])
print(int_arr.dtype)  # int64

float_arr = np.array([1.0, 2.5, 3.7])
print(float_arr.dtype)  # float64

# Mixed types - automatic upcasting
mixed = np.array([1, 2.5, 3])
print(mixed)       # [1.  2.5 3. ]
print(mixed.dtype) # float64
```

**Explicit dtype:**
```python
# Force float
arr_float = np.array([1, 2, 3], dtype=np.float32)
print(arr_float)  # [1. 2. 3.]

# Force int (truncates decimals)
arr_int = np.array([1.7, 2.9], dtype=np.int32)
print(arr_int)  # [1 2]

# Boolean
arr_bool = np.array([0, 1, 0], dtype=np.bool_)
print(arr_bool)  # [False  True False]
```

### Arrays vs Lists

**Key differences:**

| Feature | Python List | NumPy Array |
|---------|-------------|-------------|
| Data types | Heterogeneous | Homogeneous |
| Speed | Slow | Fast (50-100x) |
| Memory | More | Less |
| Operations | Limited | Rich math functions |
| Size | Dynamic | Fixed |

**Performance example:**
```python
# Python list
py_list = list(range(1000000))
result = [x * 2 for x in py_list]  # Slow

# NumPy array
np_array = np.arange(1000000)
result = np_array * 2  # Much faster!
```

### Common Mistakes

**1. Inconsistent dimensions:**
```python
# Wrong - jagged array
bad = np.array([[1, 2, 3], [4, 5]])  # Creates object array

# Correct - consistent shape
good = np.array([[1, 2, 3], [4, 5, 6]])
```

**2. Forgetting import:**
```python
# Wrong
arr = array([1, 2, 3])  # NameError

# Correct
import numpy as np
arr = np.array([1, 2, 3])
```

### Key Takeaways

1. NumPy provides fast, efficient arrays for numerical computing
2. Install with `pip install numpy`, import as `np`
3. Create arrays using `np.array()` from lists or tuples
4. Arrays are homogeneous (single data type)
5. Use `dtype` parameter to control data types
6. Arrays can be 1D, 2D, 3D, or higher dimensions
