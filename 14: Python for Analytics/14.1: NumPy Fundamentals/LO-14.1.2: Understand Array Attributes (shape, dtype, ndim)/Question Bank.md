## Question Bank: Understand Array Attributes (shape, dtype, ndim)

### Q1: Inspect 1D Array Attributes (3 minutes, Low Difficulty)

**Problem:**
Create a NumPy array from the list `[15, 25, 35, 45, 55, 65]`. Print the following attributes:
- shape
- dtype
- ndim
- size

**Expected Output:**
```
(6,)
int64
1
6
```

---

### Q2: Inspect 2D Array Attributes (3 minutes, Low Difficulty)

**Problem:**
Create a 3x4 NumPy array from the nested list:
```python
[[10, 20, 30, 40],
 [50, 60, 70, 80],
 [90, 100, 110, 120]]
```
Print the shape, number of dimensions, and total size of the array.

**Expected Output:**
```
Shape: (3, 4)
Dimensions: 2
Size: 12
```

---

### Q3: Extract Shape Components (5 minutes, Medium Difficulty)

**Problem:**
Create a 2D NumPy array with 5 rows and 3 columns containing any integer values. Extract the number of rows and columns from the shape attribute and print them separately.

**Expected Output:**
```
Number of rows: 5
Number of columns: 3
```

---

### Q4: Compare Memory Usage (5 minutes, Medium Difficulty)

**Problem:**
Create two arrays with the same values `[100, 200, 300, 400, 500]`:
- First array with dtype `int32`
- Second array with dtype `int64`

Print the itemsize and nbytes for both arrays to compare their memory usage.

**Expected Output:**
```
int32 array:
  Item size: 4 bytes
  Total bytes: 20 bytes

int64 array:
  Item size: 8 bytes
  Total bytes: 40 bytes
```

---

### Q5: Array Type Analysis (5 minutes, Medium Difficulty)

**Problem:**
Write a Python function called `analyze_array()` that takes a NumPy array as input and returns a dictionary containing:
- 'type': 'vector' if 1D, 'matrix' if 2D, or '3D+' if 3 or more dimensions
- 'shape': the shape tuple
- 'dtype': the data type as a string
- 'total_elements': the total number of elements

Test your function with the following arrays:
1. `np.array([1, 2, 3, 4])`
2. `np.array([[1, 2], [3, 4], [5, 6]])`

**Expected Output:**
```
Array 1: {'type': 'vector', 'shape': (4,), 'dtype': 'int64', 'total_elements': 4}
Array 2: {'type': 'matrix', 'shape': (3, 2), 'dtype': 'int64', 'total_elements': 6}
```
