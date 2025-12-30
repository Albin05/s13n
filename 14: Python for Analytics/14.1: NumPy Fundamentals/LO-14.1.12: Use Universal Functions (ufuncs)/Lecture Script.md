### Use Universal Functions (ufuncs)

### Hook (2 minutes)

"You know how to perform basic arithmetic on arrays, but what if you need to calculate square roots of all elements, or find sine values, or round numbers? NumPy provides universal functions - or ufuncs - which are optimized, pre-built functions that operate element-wise on arrays. These functions are incredibly fast because they're implemented in C, and they cover everything from basic math to trigonometry and statistics. Let's explore these powerful tools!"

### Section 1: What are Universal Functions? (2 minutes)

**Understanding ufuncs:**

```python
import numpy as np

# Traditional Python approach (slow)
numbers = [1, 4, 9, 16, 25]
sqrt_numbers = [num ** 0.5 for num in numbers]
print(sqrt_numbers)  # [1.0, 2.0, 3.0, 4.0, 5.0]

# NumPy ufunc approach (fast)
arr = np.array([1, 4, 9, 16, 25])
sqrt_arr = np.sqrt(arr)
print(sqrt_arr)  # [1. 2. 3. 4. 5.]
```

**Key characteristics:**
- Operate element-wise on arrays
- Vectorized (implemented in C for speed)
- Support broadcasting
- Return new arrays

### Section 2: Mathematical Universal Functions (3 minutes)

**Square root and power:**

```python
import numpy as np

arr = np.array([1, 4, 9, 16, 25])

# Square root
result = np.sqrt(arr)
print(result)  # [1. 2. 3. 4. 5.]

# Cube root
result = np.cbrt(arr)
print(result)  # [1.  1.59 2.08 2.52 2.92]

# Power
result = np.power(arr, 3)
print(result)  # [    1    64   729  4096 15625]

# Square (faster than power(arr, 2))
result = np.square(arr)
print(result)  # [  1  16  81 256 625]
```

**Exponential and logarithm:**

```python
arr = np.array([1, 2, 3, 4, 5])

# Exponential (e^x)
result = np.exp(arr)
print(result)  # [  2.72   7.39  20.09  54.6  148.41]

# Natural logarithm (log base e)
result = np.log(arr)
print(result)  # [0.   0.69 1.10 1.39 1.61]

# Log base 10
result = np.log10(arr)
print(result)  # [0.   0.30 0.48 0.60 0.70]

# Log base 2
result = np.log2(arr)
print(result)  # [0.   1.   1.58 2.   2.32]
```

### Section 3: Trigonometric Functions (3 minutes)

**Basic trig functions:**

```python
import numpy as np

# Angles in radians
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])

# Sine
result = np.sin(angles)
print(result)  # [0.   0.5  0.71 0.87 1.  ]

# Cosine
result = np.cos(angles)
print(result)  # [1.   0.87 0.71 0.5  0.  ]

# Tangent
result = np.tan(angles)
print(result)  # [0.   0.58 1.   1.73 inf]
```

**Converting degrees to radians:**

```python
# Degrees
degrees = np.array([0, 30, 45, 60, 90])

# Convert to radians
radians = np.radians(degrees)
print(radians)  # [0.   0.52 0.79 1.05 1.57]

# Or use deg2rad
radians = np.deg2rad(degrees)
print(radians)  # [0.   0.52 0.79 1.05 1.57]

# Calculate sine
result = np.sin(radians)
print(result)  # [0.   0.5  0.71 0.87 1.  ]
```

**Inverse trig functions:**

```python
values = np.array([0, 0.5, 0.707, 0.866, 1.0])

# Arcsine (returns radians)
result = np.arcsin(values)
print(result)  # [0.   0.52 0.79 1.05 1.57]

# Convert back to degrees
degrees = np.degrees(result)
print(degrees)  # [ 0.  30.  45.  60.  90.]
```

### Section 4: Rounding Functions (2 minutes)

**Different rounding methods:**

```python
import numpy as np

arr = np.array([1.2, 1.5, 1.8, 2.3, 2.7, -1.5, -2.3])

# Round to nearest integer
result = np.round(arr)
print(result)  # [ 1.  2.  2.  2.  3. -2. -2.]

# Floor (round down)
result = np.floor(arr)
print(result)  # [ 1.  1.  1.  2.  2. -2. -3.]

# Ceiling (round up)
result = np.ceil(arr)
print(result)  # [ 2.  2.  2.  3.  3. -1. -2.]

# Truncate (remove decimals)
result = np.trunc(arr)
print(result)  # [ 1.  1.  1.  2.  2. -1. -2.]
```

**Rounding to decimal places:**

```python
arr = np.array([1.23456, 2.34567, 3.45678])

# Round to 2 decimal places
result = np.round(arr, 2)
print(result)  # [1.23 2.35 3.46]

# Round to 1 decimal place
result = np.round(arr, 1)
print(result)  # [1.2 2.3 3.5]
```

### Section 5: Absolute Value and Sign (2 minutes)

**Absolute values:**

```python
import numpy as np

arr = np.array([-5, -3, 0, 2, 4])

# Absolute value
result = np.abs(arr)
print(result)  # [5 3 0 2 4]

# Also works as:
result = np.absolute(arr)
print(result)  # [5 3 0 2 4]
```

**Sign function:**

```python
arr = np.array([-5, -2, 0, 3, 7])

# Sign: returns -1, 0, or 1
result = np.sign(arr)
print(result)  # [-1 -1  0  1  1]
```

### Section 6: Comparison Functions (2 minutes)

**Element-wise maximum and minimum:**

```python
import numpy as np

arr1 = np.array([10, 25, 15, 30, 20])
arr2 = np.array([15, 20, 25, 10, 30])

# Element-wise maximum
result = np.maximum(arr1, arr2)
print(result)  # [15 25 25 30 30]

# Element-wise minimum
result = np.minimum(arr1, arr2)
print(result)  # [10 20 15 10 20]
```

**How it works:**
```
arr1:    [10, 25, 15, 30, 20]
arr2:    [15, 20, 25, 10, 30]
maximum: [15, 25, 25, 30, 30]
         (max at each position)
```

### Section 7: Aggregate Functions (2 minutes)

**Statistical ufuncs:**

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Sum of all elements
result = np.sum(arr)
print(result)  # 150

# Mean (average)
result = np.mean(arr)
print(result)  # 30.0

# Standard deviation
result = np.std(arr)
print(result)  # 14.14

# Variance
result = np.var(arr)
print(result)  # 200.0

# Minimum and maximum
print(np.min(arr))  # 10
print(np.max(arr))  # 50
```

**Aggregate along axis:**

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Sum of entire array
print(np.sum(matrix))  # 45

# Sum along rows (axis=0)
print(np.sum(matrix, axis=0))  # [12 15 18]

# Sum along columns (axis=1)
print(np.sum(matrix, axis=1))  # [ 6 15 24]
```

### Section 8: Practical Applications (2 minutes)

**Example 1: Calculate compound interest:**

```python
import numpy as np

# Principal amounts
principal = np.array([1000, 2000, 3000, 5000])

# Calculate final amount with 5% annual interest for 10 years
# A = P(1 + r)^t
rate = 0.05
years = 10

final_amount = principal * np.power((1 + rate), years)
print(f"Principal: {principal}")
print(f"Final amount: {final_amount}")
# [1628.89 3257.79 4886.68 8144.47]

# Interest earned
interest = final_amount - principal
print(f"Interest earned: {interest}")
# [ 628.89 1257.79 1886.68 3144.47]
```

**Example 2: Normalize data:**

```python
data = np.array([23, 45, 67, 89, 12, 34, 56, 78])

# Z-score normalization: (x - mean) / std
mean = np.mean(data)
std = np.std(data)
normalized = (data - mean) / std

print(f"Original: {data}")
print(f"Mean: {mean:.2f}")
print(f"Std: {std:.2f}")
print(f"Normalized: {normalized}")
# [-0.99  0.06  1.11  2.16 -1.47 -0.52  0.63  1.68]
```

**Example 3: Calculate distance:**

```python
# Coordinates
x1, y1 = 3, 4
x2, y2 = 7, 1

# Euclidean distance: sqrt((x2-x1)^2 + (y2-y1)^2)
distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distance: {distance}")  # 5.0

# For arrays of points
points1 = np.array([[0, 0], [1, 1], [2, 2]])
points2 = np.array([[1, 1], [2, 2], [3, 3]])

# Distances
distances = np.sqrt(np.sum((points2 - points1)**2, axis=1))
print(f"Distances: {distances}")  # [1.41 1.41 1.41]
```

### Summary (1 minute)

**Key Takeaways:**

1. **What are ufuncs:**
   - Universal functions
   - Element-wise operations
   - Optimized for speed (C implementation)

2. **Mathematical ufuncs:**
   - `np.sqrt()`, `np.square()`, `np.power()`
   - `np.exp()`, `np.log()`, `np.log10()`, `np.log2()`

3. **Trigonometric ufuncs:**
   - `np.sin()`, `np.cos()`, `np.tan()`
   - `np.radians()`, `np.degrees()`
   - `np.arcsin()`, `np.arccos()`, `np.arctan()`

4. **Rounding ufuncs:**
   - `np.round()`, `np.floor()`, `np.ceil()`, `np.trunc()`

5. **Statistical ufuncs:**
   - `np.sum()`, `np.mean()`, `np.std()`, `np.var()`
   - `np.min()`, `np.max()`

6. **Comparison ufuncs:**
   - `np.maximum()`, `np.minimum()`
   - Element-wise comparison

**Remember:**
- Ufuncs operate element-wise
- Much faster than Python loops
- Return new arrays (don't modify originals)
- Support axis parameter for multi-dimensional arrays

**Next Steps:**
You've mastered universal functions! Next, you'll learn about broadcasting - a powerful feature that lets you perform operations on arrays of different shapes.
