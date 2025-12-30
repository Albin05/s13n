## Calculate Statistics and Aggregations

### Basic Statistical Functions

```python
import numpy as np

data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Central tendency
mean = np.mean(data)        # 55.0
median = np.median(data)    # 55.0
total = np.sum(data)        # 550

# Spread
std = np.std(data)          # 28.72
var = np.var(data)          # 825.00

# Extremes
min_val = np.min(data)      # 10
max_val = np.max(data)      # 100
min_idx = np.argmin(data)   # 0
max_idx = np.argmax(data)   # 9
```

---

### Axis Parameter

**axis=0: Column-wise (down)**
**axis=1: Row-wise (across)**

```python
sales = np.array([[100, 150, 200],
                  [120, 180, 220],
                  [90, 140, 190],
                  [110, 160, 210]])

# Column statistics (axis=0)
monthly_total = np.sum(sales, axis=0)
# [420 630 820]

# Row statistics (axis=1)
product_total = np.sum(sales, axis=1)
# [450 520 420 480]

# Overall
total_sales = np.sum(sales)
# 1870
```

**Visualization:**
```
axis=0 (↓):          axis=1 (→):
[[100, 150, 200]     [[100, 150, 200] → 450
 [120, 180, 220]      [120, 180, 220] → 520
 [90, 140, 190]       [90, 140, 190]  → 420
 [110, 160, 210]]     [110, 160, 210] → 480]
  ↓    ↓    ↓
[420, 630, 820]
```

---

### Percentiles and Quartiles

```python
scores = np.array([45, 67, 89, 23, 56, 78, 90, 34, 67, 45])

# Quartiles
q1 = np.percentile(scores, 25)    # Q1
q2 = np.percentile(scores, 50)    # Median
q3 = np.percentile(scores, 75)    # Q3

# Multiple percentiles
p = np.percentile(scores, [25, 50, 75, 90])
# [45.75 62.   78.   89.25]

# Quantiles (0-1 scale)
q = np.quantile(scores, [0.25, 0.5, 0.75])
# Same as percentiles [25, 50, 75]
```

**IQR for Outlier Detection:**

```python
q1 = np.percentile(scores, 25)
q3 = np.percentile(scores, 75)
iqr = q3 - q1

# Outlier bounds
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Find outliers
outliers = scores[(scores < lower) | (scores > upper)]
```

---

### Cumulative Functions

```python
# Cumulative sum
sales = np.array([100, 150, 200, 180, 220])
cumsum = np.cumsum(sales)
# [100 250 450 630 850]

# Cumulative product
growth = np.array([1.1, 1.2, 1.15])
cumprod = np.cumprod(growth)
# [1.1  1.32 1.52]

# Differences
prices = np.array([100, 105, 103, 108, 112])
changes = np.diff(prices)
# [ 5 -2  5  4]
```

---

### keepdims Parameter

```python
data = np.array([[10, 20, 30],
                 [40, 50, 60]])

# Without keepdims
mean1 = np.mean(data, axis=1)
# Shape: (2,)

# With keepdims
mean2 = np.mean(data, axis=1, keepdims=True)
# Shape: (2, 1)

# Useful for broadcasting
normalized = data - mean2
```

---

### Common Patterns

**Student Analysis:**

```python
scores = np.array([[85, 90, 78],
                   [92, 88, 95],
                   [76, 85, 80]])

# Subject averages
subject_avg = np.mean(scores, axis=0)
# [84.33 87.67 84.33]

# Student averages
student_avg = np.mean(scores, axis=1)
# [84.33 91.67 80.33]

# Rankings
rankings = np.argsort(student_avg)[::-1]
# [1 0 2] - Student 2, 1, 3
```

**Sales Analysis:**

```python
sales = np.array([[1200, 1300, 1400],
                  [1500, 1600, 1700]])

# Growth
growth = np.diff(sales, axis=1) / sales[:, :-1] * 100
# Percentage change

# Best performer
best = np.argmax(np.sum(sales, axis=1))
```

---

### Quick Reference

**Basic Stats:**
```python
np.mean(arr)      # Average
np.median(arr)    # Middle value
np.std(arr)       # Standard deviation
np.var(arr)       # Variance
np.min(arr)       # Minimum
np.max(arr)       # Maximum
np.argmin(arr)    # Index of min
np.argmax(arr)    # Index of max
```

**With Axis:**
```python
np.sum(arr, axis=0)     # Column sums
np.mean(arr, axis=1)    # Row means
np.max(arr, axis=0)     # Column max
```

**Percentiles:**
```python
np.percentile(arr, 50)         # Median
np.percentile(arr, [25, 75])   # Q1, Q3
np.quantile(arr, 0.75)         # 75th percentile
```

**Cumulative:**
```python
np.cumsum(arr)    # Running total
np.cumprod(arr)   # Running product
np.diff(arr)      # Differences
```

---

### Key Takeaways

1. **Use appropriate axis:**
   - axis=0: column-wise
   - axis=1: row-wise
   - None: overall

2. **Common operations:**
   - Mean/median for average
   - Std/var for spread
   - Min/max for range
   - Percentiles for distribution

3. **Practical tips:**
   - keepdims=True for broadcasting
   - argmin/argmax for indices
   - Combine functions for insights
   - Verify results make sense

4. **Applications:**
   - Performance analysis
   - Outlier detection
   - Trend identification
   - Distribution analysis
