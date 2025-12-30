## Create Arrays with arange, linspace, zeros, ones

### Introduction to Array Creation Functions

**Why use specialized functions?**
- Generate sequences automatically
- Initialize arrays efficiently
- Create arrays filled with specific values
- Better performance than manual creation

**Key functions:**
- **np.arange()**: Evenly spaced values with step size
- **np.linspace()**: Fixed number of evenly spaced values
- **np.zeros()**: Arrays filled with zeros
- **np.ones()**: Arrays filled with ones

### Using np.arange()

**Syntax:**
```python
np.arange(start, stop, step)
```

**Examples:**
```python
import numpy as np

# Single argument (0 to n-1)
arr1 = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]

# Start and stop
arr2 = np.arange(5, 15)  # [ 5  6  7  8  9 10 11 12 13 14]

# With step
arr3 = np.arange(0, 20, 3)  # [ 0  3  6  9 12 15 18]

# Float step
arr4 = np.arange(0, 1, 0.2)  # [0.  0.2 0.4 0.6 0.8]
```

**Key points:**
- Stop value is **excluded** (like Python range)
- Supports float steps
- Default step = 1

### Using np.linspace()

**Syntax:**
```python
np.linspace(start, stop, num=50, endpoint=True)
```

**Examples:**
```python
import numpy as np

# 5 values from 0 to 10
arr1 = np.linspace(0, 10, 5)  # [ 0.   2.5  5.   7.5 10. ]

# 10 values from 1 to 2
arr2 = np.linspace(1, 2, 10)
# [1.   1.1  1.2  1.3  1.4  1.5  1.6  1.7  1.8  1.9  2.  ]

# Without endpoint
arr3 = np.linspace(0, 10, 5, endpoint=False)  # [0. 2. 4. 6. 8.]
```

**Key points:**
- Stop value is **included** by default
- Specify number of points, not step size
- Better for scientific/mathematical applications

### When to Use arange vs linspace

| Scenario | Use |
|----------|-----|
| Know step size | `arange(0, 10, 0.5)` |
| Know number of points | `linspace(0, 10, 20)` |
| Need endpoint included | `linspace(0, 10, 5)` |
| Integer sequences | `arange(0, 10)` |

### Using np.zeros()

**Syntax:**
```python
np.zeros(shape, dtype=float)
```

**Examples:**
```python
import numpy as np

# 1D array
arr1 = np.zeros(5)  # [0. 0. 0. 0. 0.]

# 2D array
arr2 = np.zeros((3, 4))
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# Integer zeros
int_zeros = np.zeros(5, dtype=int)  # [0 0 0 0 0]

# Boolean zeros (False)
bool_zeros = np.zeros(3, dtype=bool)  # [False False False]
```

**Use cases:**
- Initialize arrays before filling with values
- Create placeholder matrices
- Set up default values

### Using np.ones()

**Syntax:**
```python
np.ones(shape, dtype=float)
```

**Examples:**
```python
import numpy as np

# 1D array
arr1 = np.ones(4)  # [1. 1. 1. 1.]

# 2D array
arr2 = np.ones((2, 3))
# [[1. 1. 1.]
#  [1. 1. 1.]]

# Create constant arrays
tens = np.ones((3, 3)) * 10
# [[10. 10. 10.]
#  [10. 10. 10.]
#  [10. 10. 10.]]
```

**Use cases:**
- Initialize with non-zero values
- Create masks for filtering
- Generate constant arrays by multiplication

### Function Comparison

| Function | Purpose | Example Output |
|----------|---------|----------------|
| `arange(0, 10, 2)` | Sequence with step | `[0, 2, 4, 6, 8]` |
| `linspace(0, 10, 5)` | Fixed points | `[0, 2.5, 5, 7.5, 10]` |
| `zeros((2, 3))` | Initialize with 0s | `[[0, 0, 0], [0, 0, 0]]` |
| `ones((2, 3))` | Initialize with 1s | `[[1, 1, 1], [1, 1, 1]]` |

### Best Practices

1. **Use arange for:**
   - Integer sequences
   - Known step sizes
   - Loop-like iterations

2. **Use linspace for:**
   - Scientific computing
   - Plotting curves
   - Exact number of points needed

3. **Use zeros/ones for:**
   - Array initialization
   - Creating templates
   - Setting default values

### Key Takeaways

1. **arange(start, stop, step)**: Creates sequences with defined step (stop excluded)
2. **linspace(start, stop, num)**: Creates exact number of points (stop included)
3. **zeros(shape)**: Initializes arrays with zeros (default float64)
4. **ones(shape)**: Initializes arrays with ones (can multiply for constants)
5. Choose based on what you know: step size (arange) or point count (linspace)
6. Specify dtype when needed for memory efficiency or specific data types
