## Pre-Read: Calculate Statistics and Aggregations

### What You'll Learn

In this session, you'll master NumPy's statistical and aggregation functions - essential tools for analyzing data, identifying trends, and extracting insights from numerical datasets.

### Why It Matters

Statistical analysis is fundamental for:

1. **Data Understanding**: Summarize large datasets quickly
2. **Performance Metrics**: Track KPIs and business metrics
3. **Quality Control**: Identify outliers and anomalies
4. **Decision Making**: Base decisions on quantitative analysis
5. **Machine Learning**: Feature engineering and model evaluation

Real-world examples:
- Analyzing sales performance across regions and time
- Evaluating student test scores and identifying struggling students
- Detecting fraudulent transactions using statistical thresholds
- Monitoring system performance metrics (CPU, memory, latency)
- A/B testing results analysis

### Key Concepts Preview

**Basic Statistics:**
- Mean: average value
- Median: middle value
- Standard deviation: measure of spread
- Variance: squared deviation
- Min/Max: extreme values

**Aggregations:**
- Combine multiple values into single summary
- Apply along specific dimensions (rows/columns)
- Useful for multi-dimensional data

**Basic examples:**
```python
import numpy as np

# Simple statistics
data = np.array([10, 20, 30, 40, 50])
print(f"Mean: {np.mean(data)}")      # 30.0
print(f"Std: {np.std(data)}")        # 14.14
print(f"Max: {np.max(data)}")        # 50

# With 2D array
sales = np.array([[100, 150, 200],
                  [120, 180, 220]])

# Column totals
totals = np.sum(sales, axis=0)
# [220 330 420]
```

### What to Expect

You'll learn:
1. Calculate mean, median, sum, std, var
2. Find min, max, and their indices
3. Use axis parameter for multi-dimensional aggregations
4. Compute percentiles and quartiles
5. Apply cumulative functions
6. Analyze real-world datasets
7. Detect outliers using IQR method

### Prepare

Make sure you have:
- NumPy installed
- Understanding of array shapes
- Knowledge of basic statistics concepts
- Familiarity with array indexing

### Quick Examples

**Basic Statistics:**
```python
import numpy as np

scores = np.array([85, 90, 78, 92, 88, 76, 95, 82])

print(f"Average: {np.mean(scores)}")     # 85.75
print(f"Median: {np.median(scores)}")    # 86.5
print(f"Std Dev: {np.std(scores):.2f}")  # 6.12
print(f"Highest: {np.max(scores)}")      # 95
print(f"Lowest: {np.min(scores)}")       # 76
```

**Axis Parameter:**
```python
# 3 products × 4 quarters
sales = np.array([[100, 120, 150, 180],
                  [90, 110, 140, 170],
                  [110, 130, 160, 190]])

# Total per quarter (column sums)
quarterly = np.sum(sales, axis=0)
print(f"Quarterly totals: {quarterly}")
# [300 360 450 540]

# Total per product (row sums)
products = np.sum(sales, axis=1)
print(f"Product totals: {products}")
# [550 510 590]
```

**Percentiles:**
```python
data = np.array([23, 45, 67, 89, 34, 56, 78, 90, 45, 67])

# Quartiles
q1 = np.percentile(data, 25)   # 45.0
q2 = np.percentile(data, 50)   # 61.5 (median)
q3 = np.percentile(data, 75)   # 78.0

print(f"Q1: {q1}, Median: {q2}, Q3: {q3}")
```

### Understanding Axis

The axis parameter is crucial for multi-dimensional aggregations:

```
axis=0 (operate down columns):
[[10, 20, 30],
 [40, 50, 60]]
  ↓   ↓   ↓
[50, 70, 90]  ← sums

axis=1 (operate across rows):
[[10, 20, 30] → 60
 [40, 50, 60] → 150

axis=None (overall):
All elements → 210
```

### Common Functions

**Measures of Central Tendency:**
- `np.mean()` - arithmetic average
- `np.median()` - middle value
- `np.average()` - weighted average

**Measures of Spread:**
- `np.std()` - standard deviation
- `np.var()` - variance
- `np.ptp()` - peak-to-peak (range)

**Extremes:**
- `np.min()` - minimum value
- `np.max()` - maximum value
- `np.argmin()` - index of minimum
- `np.argmax()` - index of maximum

**Distribution:**
- `np.percentile()` - percentile values
- `np.quantile()` - quantile values
- `np.histogram()` - frequency distribution

**Cumulative:**
- `np.cumsum()` - cumulative sum
- `np.cumprod()` - cumulative product
- `np.diff()` - differences between elements

### Try to Predict

```python
import numpy as np

data = np.array([[10, 20, 30],
                 [40, 50, 60]])

# What will these return?
result1 = np.mean(data)           # ?
result2 = np.mean(data, axis=0)   # ?
result3 = np.mean(data, axis=1)   # ?

arr = np.array([10, 20, 30, 40, 50])
result4 = np.argmax(arr)          # ?
result5 = np.max(arr)             # ?
```

Answers:
- result1: 35.0 (overall mean)
- result2: [25. 35. 45.] (column means)
- result3: [20. 50.] (row means)
- result4: 4 (index of max)
- result5: 50 (max value)

### Practical Applications

**Sales Analysis:**
```python
monthly_sales = np.array([10000, 12000, 11000, 15000])
average = np.mean(monthly_sales)      # Monthly average
growth = np.diff(monthly_sales)       # Month-to-month change
total = np.sum(monthly_sales)         # Total sales
```

**Student Performance:**
```python
exam_scores = np.array([85, 90, 78, 92, 88])
class_avg = np.mean(exam_scores)      # Class average
top_score = np.max(exam_scores)       # Highest score
std_dev = np.std(exam_scores)         # Score spread
```

**Outlier Detection:**
```python
data = np.array([23, 45, 67, 89, 34, 56, 1000, 78])
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1
outliers = data[data > q3 + 1.5 * iqr]  # [1000]
```

Statistical analysis transforms raw data into actionable insights!
