### Create Arrays with arange, linspace, zeros, ones

### Hook (2 minutes)

"Imagine you need to create a 1000x1000 matrix filled with zeros for image processing, or generate exactly 100 evenly-spaced points between 0 and 10 for scientific plotting. Manually typing these values would be impossible! NumPy provides powerful built-in functions that create arrays efficiently with just one line of code. Let's explore these array creation tools!"

### Section 1: Introduction to Array Creation Functions (3 minutes)

**Why use specialized array creation functions?**

Instead of manually creating arrays from lists, NumPy provides functions to:
- Generate sequences of numbers automatically
- Create arrays filled with specific values (0s, 1s)
- Initialize arrays for mathematical computations
- Set up grids for scientific simulations

**Key Functions:**
1. **np.arange()**: Create evenly spaced values within a range (like Python's range)
2. **np.linspace()**: Create evenly spaced values with specified count
3. **np.zeros()**: Create arrays filled with zeros
4. **np.ones()**: Create arrays filled with ones

**Common use cases:**
- Initializing weights in machine learning (zeros/ones)
- Creating coordinate grids for plotting (arange/linspace)
- Setting up iteration ranges for numerical methods
- Preparing empty containers for data storage

### Section 2: Using np.arange() (4 minutes)

**What is arange?**

`np.arange()` creates an array with evenly spaced values within a given range.

**Syntax:**
```python
np.arange(start, stop, step)
```
- **start**: Starting value (inclusive)
- **stop**: Ending value (exclusive)
- **step**: Spacing between values (default: 1)

**Basic examples:**

```python
import numpy as np

# arange with stop only (0 to 9)
arr1 = np.arange(10)
print(arr1)  # [0 1 2 3 4 5 6 7 8 9]

# arange with start and stop
arr2 = np.arange(5, 15)
print(arr2)  # [ 5  6  7  8  9 10 11 12 13 14]

# arange with start, stop, and step
arr3 = np.arange(0, 20, 3)
print(arr3)  # [ 0  3  6  9 12 15 18]
```

**Float steps:**
```python
# arange with decimal step
arr4 = np.arange(0, 1, 0.2)
print(arr4)  # [0.  0.2 0.4 0.6 0.8]
```

**Important notes:**
- Like Python's `range()`, stop value is **not included**
- Can use negative steps for descending sequences
- Returns int by default; use float if any parameter is float

**Comparison with Python range:**
```python
# Python range (only integers)
py_range = list(range(0, 10, 2))  # [0, 2, 4, 6, 8]

# NumPy arange (supports floats)
np_arange = np.arange(0, 10, 2.5)  # [0.  2.5 5.  7.5]
```

### Section 3: Using np.linspace() (4 minutes)

**What is linspace?**

`np.linspace()` creates an array with a specified number of evenly spaced values between start and stop.

**Syntax:**
```python
np.linspace(start, stop, num=50, endpoint=True)
```
- **start**: Starting value (inclusive)
- **stop**: Ending value (inclusive by default)
- **num**: Number of values to generate (default: 50)
- **endpoint**: Whether to include stop value (default: True)

**Basic examples:**

```python
import numpy as np

# 5 evenly spaced values between 0 and 10
arr1 = np.linspace(0, 10, 5)
print(arr1)  # [ 0.   2.5  5.   7.5 10. ]

# 10 values between 1 and 2
arr2 = np.linspace(1, 2, 10)
print(arr2)  # [1.   1.1  1.2  1.3  1.4  1.5  1.6  1.7  1.8  1.9  2.  ]
```

**Without endpoint:**
```python
# Exclude the endpoint
arr3 = np.linspace(0, 10, 5, endpoint=False)
print(arr3)  # [0. 2. 4. 6. 8.]
```

**When to use linspace vs arange:**

| Scenario | Use |
|----------|-----|
| You know the step size | `arange(0, 10, 0.5)` |
| You know the number of points | `linspace(0, 10, 20)` |
| Need exact endpoint included | `linspace(0, 10, 5)` |
| Working with integers | `arange(0, 10)` |

**Practical example:**
```python
# Create 100 points for smooth plotting
x = np.linspace(0, 2*np.pi, 100)
# Now you have exactly 100 evenly-spaced points for a sine wave
```

### Section 4: Using np.zeros() (3 minutes)

**What is zeros?**

`np.zeros()` creates an array filled with zeros.

**Syntax:**
```python
np.zeros(shape, dtype=float)
```
- **shape**: Tuple defining array dimensions
- **dtype**: Data type (default: float64)

**Examples:**

```python
import numpy as np

# 1D array of 5 zeros
arr1 = np.zeros(5)
print(arr1)  # [0. 0. 0. 0. 0.]

# 2D array: 3 rows, 4 columns
arr2 = np.zeros((3, 4))
print(arr2)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# 3D array
arr3 = np.zeros((2, 3, 2))
print(arr3.shape)  # (2, 3, 2)
```

**Specifying dtype:**
```python
# Integer zeros
int_zeros = np.zeros(5, dtype=int)
print(int_zeros)  # [0 0 0 0 0]

# Boolean zeros (False)
bool_zeros = np.zeros(3, dtype=bool)
print(bool_zeros)  # [False False False]
```

**Common use cases:**
- Initializing arrays before filling with calculated values
- Creating placeholder matrices for linear algebra
- Setting up neural network weights

### Section 5: Using np.ones() (3 minutes)

**What is ones?**

`np.ones()` creates an array filled with ones.

**Syntax:**
```python
np.ones(shape, dtype=float)
```

**Examples:**

```python
import numpy as np

# 1D array of 4 ones
arr1 = np.ones(4)
print(arr1)  # [1. 1. 1. 1.]

# 2D array: 2 rows, 3 columns
arr2 = np.ones((2, 3))
print(arr2)
# [[1. 1. 1.]
#  [1. 1. 1.]]

# Integer ones
int_ones = np.ones(5, dtype=int)
print(int_ones)  # [1 1 1 1 1]
```

**Practical applications:**
```python
# Create a matrix of 10s (multiply ones by 10)
tens = np.ones((3, 3)) * 10
print(tens)
# [[10. 10. 10.]
#  [10. 10. 10.]
#  [10. 10. 10.]]

# Create a constant array
constants = np.ones(5) * 3.14
print(constants)  # [3.14 3.14 3.14 3.14 3.14]
```

### Section 6: Comparison and Best Practices (3 minutes)

**Quick comparison:**

| Function | Purpose | Example Output |
|----------|---------|----------------|
| `arange(0, 10, 2)` | Sequence with step size | `[0, 2, 4, 6, 8]` |
| `linspace(0, 10, 5)` | Fixed number of points | `[0, 2.5, 5, 7.5, 10]` |
| `zeros((2, 3))` | Initialize with 0s | `[[0, 0, 0], [0, 0, 0]]` |
| `ones((2, 3))` | Initialize with 1s | `[[1, 1, 1], [1, 1, 1]]` |

**Best practices:**

1. **Use arange for:**
   - Integer sequences
   - When you know the step size
   - Loop-like iterations

2. **Use linspace for:**
   - Scientific/mathematical applications
   - Plotting smooth curves
   - When you need exact number of points

3. **Use zeros/ones for:**
   - Initializing arrays for computation
   - Creating placeholder matrices
   - Setting up default values

**Common patterns:**
```python
# Initialize then fill
result = np.zeros(10)
for i in range(10):
    result[i] = i ** 2

# Create coordinate grid
x = np.linspace(0, 10, 100)
y = np.linspace(0, 5, 50)

# Matrix operations
identity_matrix = np.eye(3)  # (We'll learn this later!)
```

### Summary (2 minutes)

**Key Takeaways:**

1. **np.arange(start, stop, step)**: Like range(), creates sequences with defined step
   - Stop value is excluded
   - Supports float steps

2. **np.linspace(start, stop, num)**: Creates exact number of evenly-spaced points
   - Stop value included by default
   - Better for scientific computing

3. **np.zeros(shape)**: Creates arrays filled with zeros
   - Useful for initialization
   - Default dtype is float64

4. **np.ones(shape)**: Creates arrays filled with ones
   - Can multiply to get any constant
   - Useful for masks and weights

**Remember:**
- Choose arange when you know the step, linspace when you know the count
- Use zeros/ones for initialization instead of empty arrays
- Specify dtype when you need specific data types (int, float, bool)

**Next Steps:**
In the next lesson, we'll learn how to create random arrays and use them for simulations and testing!
