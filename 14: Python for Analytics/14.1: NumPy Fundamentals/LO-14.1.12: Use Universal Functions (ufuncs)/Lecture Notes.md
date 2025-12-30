## Use Universal Functions (ufuncs)

### What are Universal Functions?

**Key characteristics:**
- Operate element-wise on arrays
- Vectorized (implemented in C for speed)
- Support broadcasting
- Return new arrays

```python
import numpy as np

# Fast NumPy approach
arr = np.array([1, 4, 9, 16, 25])
result = np.sqrt(arr)  # [1. 2. 3. 4. 5.]
```

---

### Mathematical Universal Functions

**Square root and power:**

```python
arr = np.array([1, 4, 9, 16, 25])

# Square root
np.sqrt(arr)  # [1. 2. 3. 4. 5.]

# Cube root
np.cbrt(arr)  # [1.  1.59 2.08 2.52 2.92]

# Power
np.power(arr, 3)  # [    1    64   729  4096 15625]

# Square
np.square(arr)  # [  1  16  81 256 625]
```

**Exponential and logarithm:**

```python
arr = np.array([1, 2, 3, 4, 5])

# Exponential (e^x)
np.exp(arr)  # [  2.72   7.39  20.09  54.6  148.41]

# Natural logarithm
np.log(arr)  # [0.   0.69 1.10 1.39 1.61]

# Log base 10
np.log10(arr)  # [0.   0.30 0.48 0.60 0.70]

# Log base 2
np.log2(arr)  # [0.   1.   1.58 2.   2.32]
```

---

### Trigonometric Functions

**Basic trig functions:**

```python
# Angles in radians
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])

# Sine, Cosine, Tangent
np.sin(angles)  # [0.   0.5  0.71 0.87 1.  ]
np.cos(angles)  # [1.   0.87 0.71 0.5  0.  ]
np.tan(angles)  # [0.   0.58 1.   1.73 inf]
```

**Converting degrees and radians:**

```python
degrees = np.array([0, 30, 45, 60, 90])

# Convert to radians
radians = np.radians(degrees)  # [0.   0.52 0.79 1.05 1.57]

# Or use deg2rad
radians = np.deg2rad(degrees)

# Convert back to degrees
np.degrees(radians)  # [ 0. 30. 45. 60. 90.]
```

**Inverse trig functions:**

```python
values = np.array([0, 0.5, 0.707, 0.866, 1.0])

# Arcsine (returns radians)
result = np.arcsin(values)  # [0.   0.52 0.79 1.05 1.57]

# Convert to degrees
np.degrees(result)  # [ 0.  30.  45.  60.  90.]
```

---

### Rounding Functions

**Different rounding methods:**

```python
arr = np.array([1.2, 1.5, 1.8, 2.3, 2.7, -1.5, -2.3])

# Round to nearest
np.round(arr)  # [ 1.  2.  2.  2.  3. -2. -2.]

# Floor (round down)
np.floor(arr)  # [ 1.  1.  1.  2.  2. -2. -3.]

# Ceiling (round up)
np.ceil(arr)  # [ 2.  2.  2.  3.  3. -1. -2.]

# Truncate (remove decimals)
np.trunc(arr)  # [ 1.  1.  1.  2.  2. -1. -2.]
```

**Rounding to decimal places:**

```python
arr = np.array([1.23456, 2.34567, 3.45678])

# Round to 2 decimal places
np.round(arr, 2)  # [1.23 2.35 3.46]
```

---

### Absolute Value and Sign

**Absolute values:**

```python
arr = np.array([-5, -3, 0, 2, 4])

# Absolute value
np.abs(arr)  # [5 3 0 2 4]
# or
np.absolute(arr)  # [5 3 0 2 4]
```

**Sign function:**

```python
arr = np.array([-5, -2, 0, 3, 7])

# Returns -1, 0, or 1
np.sign(arr)  # [-1 -1  0  1  1]
```

---

### Comparison Functions

**Element-wise maximum and minimum:**

```python
arr1 = np.array([10, 25, 15, 30, 20])
arr2 = np.array([15, 20, 25, 10, 30])

# Element-wise maximum
np.maximum(arr1, arr2)  # [15 25 25 30 30]

# Element-wise minimum
np.minimum(arr1, arr2)  # [10 20 15 10 20]
```

---

### Statistical Aggregate Functions

**Statistical ufuncs:**

```python
arr = np.array([10, 20, 30, 40, 50])

# Sum, mean, std, var
np.sum(arr)  # 150
np.mean(arr)  # 30.0
np.std(arr)  # 14.14
np.var(arr)  # 200.0

# Min and max
np.min(arr)  # 10
np.max(arr)  # 50
```

**Aggregate along axis:**

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Sum of entire array
np.sum(matrix)  # 45

# Sum along rows (axis=0)
np.sum(matrix, axis=0)  # [12 15 18]

# Sum along columns (axis=1)
np.sum(matrix, axis=1)  # [ 6 15 24]
```

---

### Practical Applications

**Temperature conversion:**

```python
fahrenheit = np.array([32, 68, 86, 104, 122])
celsius = (fahrenheit - 32) * 5 / 9
# [  0.  20.  30.  40.  50.]
```

**Compound interest:**

```python
principal = np.array([1000, 2000, 3000, 5000])
rate = 0.05
years = 10

final = principal * np.power((1 + rate), years)
# [1628.89 3257.79 4886.68 8144.47]
```

**Data normalization:**

```python
data = np.array([23, 45, 67, 89, 12, 34, 56, 78])

# Z-score normalization
mean = np.mean(data)
std = np.std(data)
normalized = (data - mean) / std
```

---

### Key Takeaways

1. **Mathematical ufuncs:**
   - `np.sqrt()`, `np.square()`, `np.power()`
   - `np.exp()`, `np.log()`, `np.log10()`, `np.log2()`

2. **Trigonometric ufuncs:**
   - `np.sin()`, `np.cos()`, `np.tan()`
   - `np.radians()`, `np.degrees()`
   - `np.arcsin()`, `np.arccos()`, `np.arctan()`

3. **Rounding ufuncs:**
   - `np.round()`, `np.floor()`, `np.ceil()`, `np.trunc()`

4. **Statistical ufuncs:**
   - `np.sum()`, `np.mean()`, `np.std()`, `np.var()`
   - `np.min()`, `np.max()`
   - Support `axis` parameter for multi-dimensional arrays

5. **Comparison ufuncs:**
   - `np.maximum()`, `np.minimum()`
   - `np.abs()`, `np.sign()`

**Remember:**
- Ufuncs operate element-wise
- Much faster than Python loops
- Return new arrays
- Support broadcasting and axis operations
