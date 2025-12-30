## Editorials: Install NumPy and Create Arrays

### Q1 Solution: Create a 1D Array

```python
import numpy as np

# Create array from list
numbers = [10, 20, 30, 40, 50]
arr = np.array(numbers)

# Print array and dtype
print(arr)
print(arr.dtype)
```

**Explanation:**
- `np.array()` converts a Python list to a NumPy array
- `.dtype` attribute shows the data type (int64 by default for integers)

---

### Q2 Solution: Create a 2D Array

```python
import numpy as np

# Create 2D array from nested list
matrix = [[1, 2, 3], [4, 5, 6]]
arr_2d = np.array(matrix)

# Print array and shape
print(arr_2d)
print(arr_2d.shape)
```

**Explanation:**
- Nested lists create multi-dimensional arrays
- `.shape` returns a tuple showing dimensions (2 rows, 3 columns)

---

### Q3 Solution: Array from Tuple with Specific dtype

```python
import numpy as np

# Create array with specific dtype
data = (5, 10, 15, 20)
arr = np.array(data, dtype=np.float32)

# Print and verify
print(arr)
print(arr.dtype)
```

**Explanation:**
- `dtype=np.float32` parameter forces 32-bit float type
- NumPy automatically converts integers to floats
- Common dtypes: `np.int32`, `np.float64`, `np.bool_`

---

### Q4 Solution: Temperature Data Conversion

```python
import numpy as np

# Create array from temperature list
celsius = [25, 30, 22, 28, 35]
celsius_arr = np.array(celsius)

# Convert to Fahrenheit
fahrenheit = (celsius_arr * 9/5) + 32

# Print result
print(fahrenheit)
```

**Explanation:**
- NumPy arrays support vectorized operations
- Mathematical operations apply to all elements automatically
- No need for loops - much faster than Python lists

---

### Q5 Solution: Create and Analyze Student Scores

```python
import numpy as np

# Create 2D array of scores
scores = [[85, 90, 78],
          [92, 88, 95],
          [78, 85, 80],
          [90, 92, 88]]

scores_array = np.array(scores)

# Print required information
print(scores_array)
print(scores_array.shape)
print(scores_array.dtype)
```

**Explanation:**
- 2D array represents a matrix: rows = students, columns = subjects
- Shape (4, 3) means 4 rows and 3 columns
- dtype is int64 (default for integer data on 64-bit systems)

**Key Concepts Covered:**
1. Array creation from lists and tuples
2. Multi-dimensional arrays
3. Data type specification
4. Vectorized operations (Q4)
5. Array attributes (shape, dtype)
