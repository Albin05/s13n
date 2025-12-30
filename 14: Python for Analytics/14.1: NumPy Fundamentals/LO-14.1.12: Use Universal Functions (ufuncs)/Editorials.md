## Editorials: Use Universal Functions (ufuncs)

### Q1 Solution: Basic Mathematical Ufuncs

```python
import numpy as np

# Create array
arr = np.array([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
print(f"Original: {arr}")

# Square root
sqrt_arr = np.sqrt(arr)
print(f"Square root: {sqrt_arr}")

# Square
square_arr = np.square(arr)
print(f"Square: {square_arr}")

# Cube (power of 3)
cube_arr = np.power(arr, 3)
print(f"Cube: {cube_arr}")

# Natural logarithm
log_arr = np.log(arr)
print(f"Natural log: {log_arr}")

# Round logarithm to 2 decimals
log_rounded = np.round(log_arr, 2)
print(f"Log rounded: {log_rounded}")
```

**Explanation:**
- `np.sqrt()` calculates square root element-wise
- `np.square()` is optimized for squaring (faster than `**2`)
- `np.power(arr, 3)` raises each element to power 3
- `np.log()` calculates natural logarithm (base e)
- `np.round(arr, 2)` rounds to 2 decimal places
- All operations return new arrays

---

### Q2 Solution: Trigonometric Functions

```python
import numpy as np

# Degrees
degrees = np.array([0, 30, 45, 60, 90, 180, 270, 360])
print(f"Degrees: {degrees}")

# Convert to radians
radians = np.radians(degrees)
print(f"Radians: {np.round(radians, 2)}")

# Calculate sine
sine = np.sin(radians)
print(f"Sine: {np.round(sine, 2)}")

# Calculate cosine
cosine = np.cos(radians)
print(f"Cosine: {np.round(cosine, 2)}")

# Tangent for first 4 angles only
tangent = np.tan(radians[:4])
print(f"Tangent (0-60°): {np.round(tangent, 2)}")
```

**Explanation:**
- `np.radians()` converts degrees to radians
- `np.sin()`, `np.cos()`, `np.tan()` require radians as input
- `radians[:4]` selects first 4 elements
- `np.round()` formats output for readability
- Trig functions operate element-wise on entire array

---

### Q3 Solution: Rounding and Comparison Functions

```python
import numpy as np

# Create arrays
prices = np.array([23.456, 45.678, 12.345, 67.890, 34.567])
discounts = np.array([5.123, 10.789, 3.456, 15.234, 8.901])

print(f"Prices: {prices}")
print(f"Discounts: {discounts}")

# Round prices to 2 decimals
rounded_prices = np.round(prices, 2)
print(f"Rounded prices: {rounded_prices}")

# Floor discounts
floor_discounts = np.floor(discounts)
print(f"Floor discounts: {floor_discounts}")

# Ceiling discounts
ceil_discounts = np.ceil(discounts)
print(f"Ceiling discounts: {ceil_discounts}")

# Final prices
final_prices = prices - discounts
print(f"Final prices: {np.round(final_prices, 2)}")

# Maximum with 30
max_30 = np.maximum(rounded_prices, 30)
print(f"Max with 30: {max_30}")

# Minimum final with 50
min_50 = np.minimum(final_prices, 50)
print(f"Min final with 50: {np.round(min_50, 2)}")

# Absolute difference from 40
abs_diff = np.abs(prices - 40)
print(f"Abs diff from 40: {np.round(abs_diff, 2)}")
```

**Explanation:**
- `np.round(arr, 2)` rounds to 2 decimal places
- `np.floor()` rounds down to nearest integer
- `np.ceil()` rounds up to nearest integer
- `np.maximum(a, b)` returns element-wise maximum
- `np.minimum(a, b)` returns element-wise minimum
- `np.abs()` calculates absolute values
- All functions work element-wise

---

### Q4 Solution: Statistical Analysis with Ufuncs

```python
import numpy as np

# Scores array
scores = np.array([[85, 90, 78, 92],
                   [88, 76, 95, 82],
                   [92, 88, 84, 89],
                   [78, 85, 88, 91],
                   [95, 89, 92, 87]])

print("Scores:")
print(scores)

# Student means (across columns, axis=1)
student_means = np.mean(scores, axis=1)
print(f"Student means: {student_means}")

# Subject means (across rows, axis=0)
subject_means = np.mean(scores, axis=0)
print(f"Subject means: {subject_means}")

# Maximum per student
student_max = np.max(scores, axis=1)
print(f"Student max: {student_max}")

# Minimum per subject
subject_min = np.min(scores, axis=0)
print(f"Subject min: {subject_min}")

# Standard deviation per student
student_std = np.std(scores, axis=1)
print(f"Student std: {np.round(student_std, 2)}")

# Students with mean >= 87
high_performers = student_means >= 87
print(f"Students with mean >= 87: {high_performers}")

# Overall mean
overall_mean = np.mean(scores)
print(f"Overall mean: {overall_mean}")
```

**Explanation:**
- `np.mean(arr, axis=1)` calculates mean across columns (per row)
- `np.mean(arr, axis=0)` calculates mean across rows (per column)
- `axis=1` operates horizontally, `axis=0` operates vertically
- `np.max()` and `np.min()` work similarly with axis parameter
- `np.std()` calculates standard deviation
- `np.mean(scores)` without axis calculates mean of all elements
- Comparison `>=` creates boolean array

---

### Q5 Solution: Compound Interest Calculator

```python
import numpy as np

# Investment data
principals = np.array([5000, 10000, 15000, 20000, 25000])
rate = 0.06
years = np.array([5, 10, 15, 20, 25])

print(f"Principals: {principals}")
print(f"Years: {years}")

# Calculate final amounts: A = P * (1 + r)^t
final_amounts = principals * np.power((1 + rate), years)
print(f"Final amounts: {np.round(final_amounts, 2)}")

# Interest earned
interest = final_amounts - principals
print(f"Interest earned: {np.round(interest, 2)}")

# Exceeds $50,000
exceeds_50k = final_amounts > 50000
print(f"Exceeds $50,000: {exceeds_50k}")

# Percentage gain
pct_gain = ((final_amounts - principals) / principals) * 100
print(f"Percentage gain: {np.round(pct_gain, 2)}")

# Mean final amount
mean_final = np.mean(final_amounts)
print(f"Mean final amount: ${mean_final:.2f}")

# Square root of final amounts
sqrt_finals = np.sqrt(final_amounts)
print(f"Square root of finals: {np.round(sqrt_finals, 2)}")

# Rounded final amounts
final_rounded = np.round(final_amounts, 2)
print(f"Final rounded: {final_rounded}")
```

**Explanation:**
- `np.power((1 + rate), years)` raises (1.06) to different powers element-wise
- Element-wise multiplication: `principals * power_result`
- `final_amounts - principals` calculates interest
- `> 50000` creates boolean array for comparison
- Percentage calculation uses element-wise operations
- `np.mean()` calculates average across all elements
- `np.sqrt()` calculates square root element-wise
- All ufuncs handle arrays efficiently without loops

**Key Concepts Covered:**
1. Mathematical ufuncs (sqrt, power, log, square)
2. Trigonometric ufuncs (sin, cos, tan, radians, degrees)
3. Rounding ufuncs (round, floor, ceil)
4. Comparison ufuncs (maximum, minimum, abs)
5. Statistical ufuncs (mean, std, min, max) with axis parameter
6. Practical applications combining multiple ufuncs
