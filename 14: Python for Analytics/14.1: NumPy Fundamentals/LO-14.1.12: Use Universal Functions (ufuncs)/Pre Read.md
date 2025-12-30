## Pre-Read: Use Universal Functions (ufuncs)

### What You'll Learn

In this session, you'll explore NumPy's universal functions (ufuncs) - pre-built, optimized functions that operate element-wise on arrays. These functions cover mathematical operations, trigonometry, statistics, and more, providing powerful tools for scientific computing and data analysis.

### Why It Matters

Universal functions are essential for:

1. **Performance**: Ufuncs are implemented in C, making them much faster than Python loops
2. **Convenience**: Pre-built functions for common operations (sqrt, sin, log, etc.)
3. **Mathematical computing**: Essential for scientific and statistical calculations
4. **Data transformation**: Apply complex transformations efficiently

Real-world examples:
- Calculate compound interest for multiple investments
- Convert temperature datasets between Celsius and Fahrenheit
- Normalize data for machine learning
- Calculate trigonometric values for physics simulations
- Statistical analysis of large datasets

### Key Concepts Preview

**Universal Functions (ufuncs):**
- Operate element-wise on arrays
- Optimized C implementations
- Support broadcasting
- Return new arrays (don't modify originals)

**Categories of ufuncs:**
```python
# Mathematical
np.sqrt([1, 4, 9])  # [1., 2., 3.]
np.log([1, 10, 100])  # [0., 2.3, 4.6]
np.power([2, 3, 4], 2)  # [4, 9, 16]

# Trigonometric
np.sin([0, np.pi/2, np.pi])  # [0., 1., 0.]
np.radians([0, 90, 180])  # [0., 1.57, 3.14]

# Rounding
np.round([1.4, 1.5, 1.6])  # [1., 2., 2.]
np.floor([1.9, 2.1, 2.9])  # [1., 2., 2.]

# Statistical
np.mean([10, 20, 30])  # 20.0
np.std([10, 20, 30])  # 8.16

# Comparison
np.maximum([1, 5, 3], [4, 2, 6])  # [4, 5, 6]
```

### What to Expect

You'll learn:
1. Mathematical ufuncs (sqrt, power, log, exp)
2. Trigonometric ufuncs (sin, cos, tan, radians, degrees)
3. Rounding ufuncs (round, floor, ceil, trunc)
4. Absolute value and sign functions
5. Comparison functions (maximum, minimum)
6. Statistical aggregate functions (sum, mean, std, var)
7. Using axis parameter for multi-dimensional arrays

### Prepare

Make sure you have:
- NumPy installed
- Understanding of element-wise operations
- Basic knowledge of mathematical functions
- Familiarity with statistical concepts (mean, standard deviation)

### Quick Example

Try to predict the output:
```python
import numpy as np

# Square root
arr = np.array([4, 9, 16, 25])
result1 = np.sqrt(arr)  # ?

# Rounding
arr2 = np.array([1.4, 2.5, 3.6, 4.7])
result2 = np.round(arr2)  # ?

# Maximum
a = np.array([10, 20, 30])
b = np.array([15, 18, 35])
result3 = np.maximum(a, b)  # ?

# Mean with axis
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
result4 = np.mean(matrix, axis=1)  # ?
```

Answers:
- result1: [2., 3., 4., 5.]
- result2: [1., 2., 4., 5.]
- result3: [15, 20, 35] (element-wise max)
- result4: [2., 5.] (mean of each row)

### Why Ufuncs?

**Traditional Python (slow):**
```python
numbers = [1, 4, 9, 16, 25]
sqrt_numbers = [num ** 0.5 for num in numbers]
# Slow, verbose
```

**NumPy ufunc (fast):**
```python
arr = np.array([1, 4, 9, 16, 25])
sqrt_arr = np.sqrt(arr)
# Fast, concise, readable
```

Universal functions are the foundation of efficient numerical computing in Python!
