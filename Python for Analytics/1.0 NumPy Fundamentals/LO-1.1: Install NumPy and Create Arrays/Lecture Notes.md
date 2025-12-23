# Install NumPy and Create Arrays - Lecture Notes

## Session Overview
- **Duration**: 45 minutes
- **Format**: Interactive coding session
- **Tools Needed**: Python 3.x, Jupyter Notebook or IDE

---

## Part 1: Introduction to NumPy (10 minutes)

### What is NumPy?
- **Numerical Python** - fundamental package for scientific computing
- Created by Travis Oliphant in 2005
- Foundation for pandas, scikit-learn, TensorFlow, and more

### Why NumPy Matters
```python
# Performance comparison
import time
import numpy as np

# Python list approach
start = time.time()
py_list = list(range(1000000))
result = [x * 2 for x in py_list]
print(f"Python list: {time.time() - start:.4f} seconds")

# NumPy array approach
start = time.time()
np_array = np.arange(1000000)
result = np_array * 2
print(f"NumPy array: {time.time() - start:.4f} seconds")
# NumPy is typically 10-50x faster!
```

---

## Part 2: Installation (5 minutes)

### Step-by-Step Installation

**Method 1: Using pip**
```bash
# Install NumPy
pip install numpy

# Install specific version
pip install numpy==1.24.3

# Upgrade existing installation
pip install --upgrade numpy
```

**Method 2: Using conda**
```bash
conda install numpy
```

### Verification
```python
import numpy as np

# Check version
print(f"NumPy version: {np.__version__}")

# Check installation path
print(f"Installed at: {np.__file__}")
```

**Expected Output:**
```
NumPy version: 1.24.3
Installed at: /path/to/site-packages/numpy/__init__.py
```

---

## Part 3: Creating Arrays from Lists (15 minutes)

### 3.1 One-Dimensional Arrays

**Basic 1D Array**
```python
import numpy as np

# From a Python list
numbers = [1, 2, 3, 4, 5]
arr = np.array(numbers)

print(f"Array: {arr}")
print(f"Type: {type(arr)}")
print(f"Data type: {arr.dtype}")
```

**Output:**
```
Array: [1 2 3 4 5]
Type: <class 'numpy.ndarray'>
Data type: int64
```

### 3.2 Two-Dimensional Arrays

**Creating a Matrix**
```python
# 3x3 matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix)
print(f"Shape: {matrix.shape}")  # (rows, columns)
print(f"Dimensions: {matrix.ndim}")
```

**Output:**
```
[[1 2 3]
 [4 5 6]
 [7 8 9]]
Shape: (3, 3)
Dimensions: 2
```

### 3.3 Three-Dimensional Arrays

**Creating a 3D Array**
```python
# 2x3x4 array
arr_3d = np.array([[[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]],

                   [[13, 14, 15, 16],
                    [17, 18, 19, 20],
                    [21, 22, 23, 24]]])

print(f"Shape: {arr_3d.shape}")  # (2, 3, 4)
print(f"Total elements: {arr_3d.size}")  # 24
```

---

## Part 4: Data Types (10 minutes)

### 4.1 Automatic Type Detection

```python
# Integer array
int_arr = np.array([1, 2, 3])
print(f"Integer dtype: {int_arr.dtype}")  # int64

# Float array
float_arr = np.array([1.0, 2.5, 3.7])
print(f"Float dtype: {float_arr.dtype}")  # float64

# Mixed types (automatic upcasting)
mixed_arr = np.array([1, 2.5, 3])
print(f"Mixed dtype: {mixed_arr.dtype}")  # float64 (all become floats)
```

### 4.2 Explicit Type Specification

```python
# Force integer type
arr_int = np.array([1.7, 2.9, 3.1], dtype=int)
print(arr_int)  # [1 2 3] - values truncated

# Force float type
arr_float = np.array([1, 2, 3], dtype=float)
print(arr_float)  # [1. 2. 3.]

# Complex numbers
arr_complex = np.array([1, 2, 3], dtype=complex)
print(arr_complex)  # [1.+0.j 2.+0.j 3.+0.j]

# Boolean array
arr_bool = np.array([0, 1, 0, 1], dtype=bool)
print(arr_bool)  # [False  True False  True]
```

---

## Key Takeaways

1. **NumPy is essential** for numerical computing in Python
2. **ndarray** is the core NumPy data structure
3. Arrays are **homogeneous** (all elements same type)
4. Arrays can be **multi-dimensional**
5. Use **dtype** parameter to control data types
6. NumPy is **significantly faster** than Python lists

---

## Homework Assignment

1. Install NumPy on your system
2. Create a 4x4 array representing a Tic-Tac-Toe board
3. Create a 10x10 multiplication table using NumPy
4. Research the difference between `np.array()` and `np.asarray()`
