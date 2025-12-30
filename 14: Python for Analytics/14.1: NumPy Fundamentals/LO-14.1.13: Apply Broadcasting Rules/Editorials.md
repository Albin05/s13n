## Editorials: Apply Broadcasting Rules

### Q1 Solution: Basic Broadcasting Operations

```python
import numpy as np

# Create matrix
matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

print("Original:")
print(matrix)

# Add 5
result = matrix + 5
print("\nAfter +5:")
print(result)

# Multiply by 3
result = matrix * 3
print("\nAfter *3:")
print(result)

# Subtract 15
result = matrix - 15
print("\nAfter -15:")
print(result)

# Divide by 10
result = matrix / 10
print("\nAfter /10:")
print(result)
```

**Explanation:**
- Scalar broadcasts to all elements automatically
- `matrix + 5` adds 5 to every element
- Broadcasting works with all arithmetic operators
- No loops needed - NumPy handles it efficiently
- Original matrix remains unchanged

---

### Q2 Solution: Broadcasting with 1D Arrays

```python
import numpy as np

# Create arrays
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
row_vec = np.array([10, 20, 30, 40])

print("Matrix:")
print(matrix)
print(f"Row vector: {row_vec}")

# Add row vector
result = matrix + row_vec
print("\nAfter adding row_vec:")
print(result)

# Multiply by row vector
result = matrix * row_vec
print("\nAfter multiplying by row_vec:")
print(result)

# Column vector
col_vec = np.array([[100], [200], [300]])
print("\nColumn vector:")
print(col_vec)

# Add column vector
result = matrix + col_vec
print("\nAfter adding col_vec:")
print(result)
```

**Explanation:**
- Row vector (4,) broadcasts across rows to match (3, 4)
- Each row gets the same row_vec added/multiplied
- Column vector (3, 1) broadcasts across columns
- Each column gets corresponding col_vec value
- Broadcasting happens along compatible dimensions

---

### Q3 Solution: Normalize Data Using Broadcasting

```python
import numpy as np

# Student scores
scores = np.array([[85, 90, 78],
                   [92, 88, 95],
                   [76, 85, 80],
                   [88, 92, 87]])

print("Scores:")
print(scores)

# Subject means (column-wise)
subject_means = np.mean(scores, axis=0)
print(f"\nSubject means: {subject_means}")

# Subject std
subject_std = np.std(scores, axis=0)
print(f"Subject std: {np.round(subject_std, 2)}")

# Normalize (Z-score)
normalized = (scores - subject_means) / subject_std
print("\nNormalized scores (Z-score):")
print(np.round(normalized, 2))

# Student means (row-wise, keep dims for broadcasting)
student_means = np.mean(scores, axis=1, keepdims=True)
print("\nStudent means:")
print(np.round(student_means, 2))

# Center by student
centered = scores - student_means
print("\nCentered by student:")
print(np.round(centered, 2))
```

**Explanation:**
- `axis=0` calculates column-wise (per subject)
- `keepdims=True` preserves shape for broadcasting
- `(scores - subject_means)` broadcasts (1, 3) to (4, 3)
- Normalization: subtract mean, divide by std
- Row-wise operations need shape (4, 1) for broadcasting

---

### Q4 Solution: Temperature Conversion Matrix

```python
import numpy as np

# Celsius temperatures
celsius = np.array([[22, 25, 23, 24],
                    [18, 20, 19, 21],
                    [30, 32, 31, 29],
                    [15, 17, 16, 18],
                    [28, 27, 29, 30]])

print("Celsius temperatures:")
print(celsius)

# Convert to Fahrenheit
fahrenheit = celsius * 9/5 + 32
print("\nFahrenheit:")
print(fahrenheit)

# Above 25°C
above_25 = celsius > 25
print("\nAbove 25°C:")
print(above_25)

# City averages
city_avg = np.mean(celsius, axis=1)
print(f"\nCity averages: {city_avg}")

# Difference from city average
diff = celsius - city_avg[:, np.newaxis]
print("\nDifference from city avg:")
print(diff)

# Overall mean
overall_mean = np.mean(celsius)
print(f"\nOverall mean: {overall_mean}°C")

# Count above overall mean
count = np.sum(celsius > overall_mean)
print(f"Readings above overall mean: {count}")
```

**Explanation:**
- Formula broadcasts: `celsius * 9/5 + 32`
- Comparison creates boolean array
- `city_avg[:, np.newaxis]` reshapes (5,) to (5, 1) for broadcasting
- Broadcasting (5, 1) with (5, 4) works by stretching column
- `np.sum()` on boolean array counts True values

---

### Q5 Solution: Price Discount System

```python
import numpy as np

# Prices and discounts
prices = np.array([[100, 200, 150],
                   [250, 180, 220],
                   [90, 160, 130],
                   [300, 270, 240]])

discounts = np.array([0.10, 0.15, 0.20])
bulk_discount = np.array([[0.05], [0.10], [0.00], [0.15]])

print("Original prices:")
print(prices)

# Apply category discount
after_category = prices * (1 - discounts)
print("\nAfter category discount:")
print(after_category)

# Apply bulk discount
final_prices = after_category * (1 - bulk_discount)
print("\nAfter bulk discount:")
print(final_prices)

# Total savings
savings = prices - final_prices
print("\nTotal savings per product:")
print(savings)

# Under $150
under_150 = final_prices < 150
print("\nProducts under $150:")
print(under_150)

# Average per category
avg_per_category = np.mean(final_prices, axis=0)
print(f"\nAverage final price per category: {np.round(avg_per_category, 2)}")
```

**Explanation:**
- `discounts` shape (3,) broadcasts to (4, 3) for category discount
- `bulk_discount` shape (4, 1) broadcasts across columns
- Multiple broadcasting operations in sequence
- `prices * (1 - discounts)` applies percentage discount
- Final calculation combines both broadcasting patterns
- `axis=0` for column-wise average

**Key Concepts Covered:**
1. Scalar broadcasting to arrays
2. 1D array broadcasting to 2D (rows and columns)
3. Using `keepdims=True` for proper broadcasting shape
4. Using `np.newaxis` to add dimensions
5. Complex multi-step broadcasting operations
6. Combining broadcasting with statistical operations
