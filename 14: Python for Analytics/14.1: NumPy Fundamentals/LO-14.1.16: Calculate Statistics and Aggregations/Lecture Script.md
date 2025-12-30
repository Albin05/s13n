## Calculate Statistics and Aggregations

### Hook (2 minutes)

**Scenario:**
You have sales data for 100 products across 12 months. Your manager asks: "What's the average monthly revenue? Which product performs best? What's the total Q4 sales?"

Or you're analyzing student test scores for 500 students across 5 subjects. You need mean scores, standard deviations, median performance, and percentile rankings.

These questions require statistical calculations and aggregations - fundamental operations in data analysis. NumPy provides powerful functions to answer them efficiently.

**What You'll Learn:**
1. Calculate basic statistics (mean, median, sum, std, var)
2. Find minimum and maximum values
3. Use aggregation functions with axis parameter
4. Compute percentiles and quantiles
5. Apply cumulative functions
6. Perform statistical analysis on real data

---

### Section 1: Basic Statistical Functions (4 minutes)

**Mean, Median, and Sum:**

```python
import numpy as np

data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Mean (average)
mean = np.mean(data)
print(f"Mean: {mean}")  # 55.0

# Median (middle value)
median = np.median(data)
print(f"Median: {median}")  # 55.0

# Sum
total = np.sum(data)
print(f"Sum: {total}")  # 550
```

**Standard Deviation and Variance:**

```python
# Standard deviation
std = np.std(data)
print(f"Std Dev: {std:.2f}")  # 28.72

# Variance
var = np.var(data)
print(f"Variance: {var:.2f}")  # 825.00

# Relationship: variance = std^2
print(f"Std^2: {std**2:.2f}")  # 825.00
```

**Min and Max:**

```python
data = np.array([45, 23, 67, 12, 89, 34, 56, 78, 90, 21])

# Minimum
min_val = np.min(data)
print(f"Min: {min_val}")  # 12

# Maximum
max_val = np.max(data)
print(f"Max: {max_val}")  # 90

# Range
range_val = max_val - min_val
print(f"Range: {range_val}")  # 78
```

**Index of Min/Max:**

```python
# Index of minimum
min_idx = np.argmin(data)
print(f"Min at index: {min_idx}")  # 3

# Index of maximum
max_idx = np.argmax(data)
print(f"Max at index: {max_idx}")  # 8

print(f"Min value: {data[min_idx]}")  # 12
print(f"Max value: {data[max_idx]}")  # 90
```

---

### Section 2: Aggregations with Axis Parameter (5 minutes)

**2D Array Statistics:**

```python
import numpy as np

# Sales data: 4 products × 3 months
sales = np.array([[100, 150, 200],
                  [120, 180, 220],
                  [90, 140, 190],
                  [110, 160, 210]])

print("Sales data (products × months):")
print(sales)
```

**Column-wise Aggregations (axis=0):**

```python
# Sum per month (column totals)
monthly_total = np.sum(sales, axis=0)
print(f"Monthly totals: {monthly_total}")
# [420 630 820]

# Average per month
monthly_avg = np.mean(sales, axis=0)
print(f"Monthly averages: {monthly_avg}")
# [105. 157.5 205.]

# Max per month
monthly_max = np.max(sales, axis=0)
print(f"Monthly max: {monthly_max}")
# [120 180 220]
```

**Row-wise Aggregations (axis=1):**

```python
# Total per product (row totals)
product_total = np.sum(sales, axis=1)
print(f"Product totals: {product_total}")
# [450 520 420 480]

# Average per product
product_avg = np.mean(sales, axis=1)
print(f"Product averages: {product_avg}")
# [150. 173.33 140. 160.]

# Min per product
product_min = np.min(sales, axis=1)
print(f"Product min: {product_min}")
# [100 120 90 110]
```

**Overall Statistics (no axis):**

```python
# Overall statistics
total_sales = np.sum(sales)
print(f"Total sales: {total_sales}")  # 1870

overall_avg = np.mean(sales)
print(f"Overall average: {overall_avg:.2f}")  # 155.83

overall_std = np.std(sales)
print(f"Overall std: {overall_std:.2f}")  # 40.62
```

**Visualizing Axis:**

```
axis=0 (down columns):
[[100, 150, 200],
 [120, 180, 220],
 [90, 140, 190],
 [110, 160, 210]]
  ↓    ↓    ↓
[420, 630, 820]

axis=1 (across rows):
[[100, 150, 200] → 450
 [120, 180, 220] → 520
 [90, 140, 190]  → 420
 [110, 160, 210] → 480]
```

---

### Section 3: Percentiles and Quantiles (3 minutes)

**Percentiles:**

```python
import numpy as np

scores = np.array([45, 67, 89, 23, 56, 78, 90, 34, 67, 45, 
                   78, 89, 56, 67, 45, 78, 89, 67, 56, 78])

# 25th percentile (Q1)
q1 = np.percentile(scores, 25)
print(f"25th percentile: {q1}")  # 52.75

# 50th percentile (median, Q2)
q2 = np.percentile(scores, 50)
print(f"50th percentile (median): {q2}")  # 67.0

# 75th percentile (Q3)
q3 = np.percentile(scores, 75)
print(f"75th percentile: {q3}")  # 78.0

# 90th percentile
p90 = np.percentile(scores, 90)
print(f"90th percentile: {p90}")  # 89.0
```

**Multiple Percentiles:**

```python
# Calculate multiple percentiles at once
percentiles = np.percentile(scores, [10, 25, 50, 75, 90])
print("Percentiles [10, 25, 50, 75, 90]:")
print(percentiles)
# [39.  52.75 67.  78.  89. ]
```

**Quantiles:**

```python
# Quantiles (0 to 1 scale)
q = np.quantile(scores, [0.25, 0.5, 0.75])
print("Quantiles [0.25, 0.5, 0.75]:")
print(q)
# [52.75 67.   78.  ]
```

**IQR (Interquartile Range):**

```python
# IQR for outlier detection
q1 = np.percentile(scores, 25)
q3 = np.percentile(scores, 75)
iqr = q3 - q1

print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")  # 25.25

# Outlier bounds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
print(f"Outlier bounds: [{lower_bound:.2f}, {upper_bound:.2f}]")
```

---

### Section 4: Cumulative Functions (3 minutes)

**Cumulative Sum:**

```python
import numpy as np

monthly_sales = np.array([100, 150, 200, 180, 220, 250])

# Cumulative sum
cumsum = np.cumsum(monthly_sales)
print("Monthly sales:", monthly_sales)
print("Cumulative sales:", cumsum)
# [100 250 450 630 850 1100]
```

```python
# 2D cumulative sum
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Cumulative sum along axis 1
cumsum_row = np.cumsum(matrix, axis=1)
print("Cumulative sum (rows):")
print(cumsum_row)
# [[ 1  3  6]
#  [ 4  9 15]]
```

**Cumulative Product:**

```python
# Growth rates
growth = np.array([1.1, 1.2, 1.15, 1.05, 1.08])

# Cumulative product
cumprod = np.cumprod(growth)
print("Growth rates:", growth)
print("Cumulative growth:", np.round(cumprod, 2))
# [1.1  1.32 1.52 1.6  1.72]
```

**Differences:**

```python
prices = np.array([100, 105, 103, 108, 112, 110])

# Day-to-day changes
changes = np.diff(prices)
print("Prices:", prices)
print("Changes:", changes)
# [ 5 -2  5  4 -2]
```

---

### Section 5: Multi-dimensional Statistics (2 minutes)

**Statistics on 3D Arrays:**

```python
import numpy as np

# Test scores: 3 classes × 4 students × 5 subjects
np.random.seed(42)
scores = np.random.randint(60, 100, (3, 4, 5))

print(f"Shape: {scores.shape}")  # (3, 4, 5)

# Average per class
class_avg = np.mean(scores, axis=(1, 2))
print(f"Class averages: {np.round(class_avg, 2)}")

# Average per student across all classes and subjects
student_avg = np.mean(scores, axis=2)
print("Student averages per class:")
print(np.round(student_avg, 2))

# Overall statistics
print(f"Overall mean: {np.mean(scores):.2f}")
print(f"Overall std: {np.std(scores):.2f}")
```

**keepdims Parameter:**

```python
data = np.array([[10, 20, 30],
                 [40, 50, 60]])

# Without keepdims
mean1 = np.mean(data, axis=1)
print(f"Shape without keepdims: {mean1.shape}")  # (2,)

# With keepdims
mean2 = np.mean(data, axis=1, keepdims=True)
print(f"Shape with keepdims: {mean2.shape}")  # (2, 1)

# Useful for broadcasting
normalized = data - mean2
print("Normalized:")
print(normalized)
```

---

### Section 6: Practical Applications (3 minutes)

**Application 1: Student Performance Analysis**

```python
import numpy as np

# Student scores: 5 students × 4 subjects
scores = np.array([[85, 90, 78, 88],
                   [92, 88, 95, 90],
                   [76, 85, 80, 82],
                   [88, 92, 87, 89],
                   [95, 89, 92, 94]])

subjects = ['Math', 'Science', 'English', 'History']

# Subject statistics
subject_means = np.mean(scores, axis=0)
subject_stds = np.std(scores, axis=0)

print("Subject Statistics:")
for i, subj in enumerate(subjects):
    print(f"{subj}: Mean={subject_means[i]:.2f}, Std={subject_stds[i]:.2f}")

# Student rankings
student_avgs = np.mean(scores, axis=1)
rankings = np.argsort(student_avgs)[::-1]

print("\nStudent Rankings:")
for rank, student_idx in enumerate(rankings, 1):
    print(f"Rank {rank}: Student {student_idx+1} (Avg: {student_avgs[student_idx]:.2f})")

# Top performer per subject
top_per_subject = np.argmax(scores, axis=0)
print("\nTop performer per subject:")
for i, subj in enumerate(subjects):
    print(f"{subj}: Student {top_per_subject[i]+1}")
```

**Application 2: Sales Trend Analysis**

```python
# Quarterly sales: 4 quarters × 6 products
sales = np.array([[1200, 1500, 1300, 1100, 1400, 1600],
                  [1300, 1600, 1400, 1200, 1500, 1700],
                  [1400, 1700, 1500, 1300, 1600, 1800],
                  [1500, 1800, 1600, 1400, 1700, 1900]])

# Quarter-over-quarter growth
qoq_growth = np.diff(sales, axis=0) / sales[:-1] * 100
print("QoQ Growth (%):")
print(np.round(qoq_growth, 2))

# Best performing product
product_totals = np.sum(sales, axis=0)
best_product = np.argmax(product_totals)
print(f"\nBest product: Product {best_product+1}")
print(f"Total sales: ${product_totals[best_product]}")

# Most consistent product (lowest std)
product_stds = np.std(sales, axis=0)
most_consistent = np.argmin(product_stds)
print(f"\nMost consistent: Product {most_consistent+1}")
print(f"Std Dev: ${product_stds[most_consistent]:.2f}")
```

**Application 3: Outlier Detection**

```python
data = np.array([23, 45, 67, 89, 34, 56, 78, 90, 1000, 45, 67, 89])

# Calculate IQR bounds
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Find outliers
outliers = data[(data < lower) | (data > upper)]
print(f"Outliers: {outliers}")  # [1000]

# Clean data
clean_data = data[(data >= lower) & (data <= upper)]
print(f"Original mean: {np.mean(data):.2f}")
print(f"Clean mean: {np.mean(clean_data):.2f}")
```

---

### Summary (1 minute)

**Key Functions Covered:**

1. **Basic Statistics:**
   - `np.mean()`, `np.median()`, `np.sum()`
   - `np.std()`, `np.var()`
   - `np.min()`, `np.max()`
   - `np.argmin()`, `np.argmax()`

2. **Percentiles:**
   - `np.percentile(arr, q)` - percentile value
   - `np.quantile(arr, q)` - quantile (0-1 scale)
   - Use for quartiles, IQR, outlier detection

3. **Cumulative:**
   - `np.cumsum()` - cumulative sum
   - `np.cumprod()` - cumulative product
   - `np.diff()` - differences

4. **Axis Parameter:**
   - `axis=0` - column-wise (down)
   - `axis=1` - row-wise (across)
   - `axis=None` - overall (default)
   - `keepdims=True` - preserve dimensions

**Quick Reference:**

```python
# Basic stats
np.mean(arr)           # Average
np.std(arr)            # Standard deviation
np.min(arr)            # Minimum
np.max(arr)            # Maximum

# With axis
np.sum(arr, axis=0)    # Column sums
np.mean(arr, axis=1)   # Row means

# Percentiles
np.percentile(arr, 50)  # Median
np.percentile(arr, [25, 50, 75])  # Quartiles

# Cumulative
np.cumsum(arr)         # Running total
np.diff(arr)           # Changes
```

**Remember:**
- Use axis parameter for multi-dimensional data
- keepdims=True for broadcasting
- Percentiles for distribution analysis
- Combine functions for insights

**Next Steps:**
- Practice with real datasets
- Combine with filtering
- Create statistical reports
- Build analysis pipelines

Statistical analysis is fundamental to data science - master these functions!
