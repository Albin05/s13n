## Editorials: Calculate Statistics and Aggregations

### Q1 Solution: Basic Statistical Operations

```python
import numpy as np

# Create array
np.random.seed(42)
data = np.random.randint(50, 101, 10)

print(f"Data: {data}")

# Mean
mean = np.mean(data)
print(f"Mean: {mean:.2f}")

# Median
median = np.median(data)
print(f"Median: {median:.2f}")

# Standard deviation
std = np.std(data)
print(f"Std Dev: {std:.2f}")

# Variance
var = np.var(data)
print(f"Variance: {var:.2f}")

# Min and Max
min_val = np.min(data)
max_val = np.max(data)
print(f"Min: {min_val}, Max: {max_val}")

# Range
range_val = max_val - min_val
print(f"Range: {range_val}")
```

**Explanation:**
- `np.mean()` calculates arithmetic average
- `np.median()` finds middle value when sorted
- `np.std()` measures spread from mean
- `np.var()` is squared standard deviation
- `np.min()` and `np.max()` find extremes
- Range shows data spread

---

### Q2 Solution: Axis-based Aggregations

```python
import numpy as np

# Create data
np.random.seed(42)
data = np.random.randint(1, 101, (4, 5))

print("Data:")
print(data)

# Row sums (axis=1)
row_sums = np.sum(data, axis=1)
print(f"\nRow sums: {row_sums}")

# Column means (axis=0)
col_means = np.mean(data, axis=0)
print(f"Column means: {col_means}")

# Row max (axis=1)
row_max = np.max(data, axis=1)
print(f"Row max: {row_max}")

# Column min (axis=0)
col_min = np.min(data, axis=0)
print(f"Column min: {col_min}")

# Overall statistics
overall_sum = np.sum(data)
overall_mean = np.mean(data)
print(f"Overall sum: {overall_sum}")
print(f"Overall mean: {overall_mean:.2f}")
```

**Explanation:**
- `axis=0` operates down columns (vertical)
- `axis=1` operates across rows (horizontal)
- No axis parameter gives overall statistic
- Each function returns array matching non-aggregated dimension
- Row operations: (4, 5) → (4,)
- Column operations: (4, 5) → (5,)

---

### Q3 Solution: Percentile and Quartile Analysis

```python
import numpy as np

# Create data
np.random.seed(123)
data = np.random.randint(20, 101, 50)

# Quartiles
q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)  # Median
q3 = np.percentile(data, 75)

print(f"Q1: {q1:.2f}")
print(f"Q2 (Median): {q2:.2f}")
print(f"Q3: {q3:.2f}")

# IQR
iqr = q3 - q1
print(f"IQR: {iqr:.2f}")

# Outlier bounds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
print(f"\nOutlier bounds: [{lower_bound:.2f}, {upper_bound:.2f}]")

# Find outliers
outliers = data[(data < lower_bound) | (data > upper_bound)]
print(f"Outliers found: {outliers}")

# Multiple percentiles
percentiles = np.percentile(data, [10, 25, 50, 75, 90])
print(f"\nPercentiles [10, 25, 50, 75, 90]:")
print(np.round(percentiles, 2))
```

**Explanation:**
- Quartiles divide data into 4 equal parts
- Q1 (25th percentile): 25% of data below
- Q2 (50th percentile): median, 50% below
- Q3 (75th percentile): 75% of data below
- IQR = Q3 - Q1, measures middle 50% spread
- Outliers typically beyond Q1-1.5*IQR or Q3+1.5*IQR
- Can calculate multiple percentiles at once

---

### Q4 Solution: Sales Performance Analysis

```python
import numpy as np

# Create sales data
np.random.seed(456)
sales = np.random.randint(5000, 15000, (6, 12))

print("Sales data shape:", sales.shape)

# Annual sales per salesperson (row sums)
annual_sales = np.sum(sales, axis=1)
print("\nAnnual sales per salesperson:")
print(annual_sales)

# Monthly averages per salesperson
monthly_avg = np.mean(sales, axis=1)
print("\nMonthly averages per salesperson:")
print(np.round(monthly_avg, 2))

# Best month for each salesperson (argmax per row)
best_months = np.argmax(sales, axis=1)
print("\nBest month for each salesperson:")
for i, month in enumerate(best_months, 1):
    print(f"Salesperson {i}: Month {month+1} (${sales[i-1, month]})")

# Monthly sales trends (column sums)
monthly_totals = np.sum(sales, axis=0)
print("\nMonthly sales trends:")
for month, total in enumerate(monthly_totals, 1):
    print(f"Month {month}: ${total}")

# Top 3 salespersons
top_3_idx = np.argsort(annual_sales)[::-1][:3]
print("\nTop 3 salespersons:")
for rank, idx in enumerate(top_3_idx, 1):
    print(f"{rank}. Salesperson {idx+1}: ${annual_sales[idx]}")

# Most consistent (lowest std)
sales_std = np.std(sales, axis=1)
most_consistent = np.argmin(sales_std)
print(f"\nMost consistent: Salesperson {most_consistent+1} (Std: ${sales_std[most_consistent]:.2f})")
```

**Explanation:**
- `np.sum(axis=1)` gives annual sales per person
- `np.mean(axis=1)` calculates monthly average per person
- `np.argmax(axis=1)` finds best month index for each person
- `np.sum(axis=0)` shows monthly trends across all salespeople
- `np.argsort()[::-1]` sorts indices in descending order
- `np.std(axis=1)` measures consistency (lower = more consistent)
- Combining multiple aggregations provides comprehensive analysis

---

### Q5 Solution: Student Grade Analytics System

```python
import numpy as np

# Create scores
np.random.seed(789)
scores = np.random.randint(55, 100, (20, 5))
subjects = ['Math', 'Science', 'English', 'History', 'Art']

print("Scores shape:", scores.shape)

# Subject-wise statistics (axis=0)
subject_means = np.mean(scores, axis=0)
subject_stds = np.std(scores, axis=0)
subject_mins = np.min(scores, axis=0)
subject_maxs = np.max(scores, axis=0)

print("\nSubject Statistics:")
for i, subj in enumerate(subjects):
    print(f"{subj}: Mean={subject_means[i]:.2f}, Std={subject_stds[i]:.2f}, "
          f"Min={subject_mins[i]}, Max={subject_maxs[i]}")

# Student rankings
student_avgs = np.mean(scores, axis=1)
rankings = np.argsort(student_avgs)[::-1]

print("\nStudent Rankings:")
for rank, student_idx in enumerate(rankings[:5], 1):
    print(f"Rank {rank}: Student {student_idx+1} (Avg: {student_avgs[student_idx]:.2f})")

# Grade distribution
def get_grade(avg):
    if avg >= 90: return 'A'
    elif avg >= 80: return 'B'
    elif avg >= 70: return 'C'
    elif avg >= 60: return 'D'
    else: return 'F'

grades = [get_grade(avg) for avg in student_avgs]
print("\nGrade Distribution:")
for grade in ['A', 'B', 'C', 'D', 'F']:
    count = grades.count(grade)
    print(f"{grade} (90+ if A, etc.): {count} students")

# Students needing improvement
struggling = np.where(student_avgs < 70)[0]
print("\nStudents needing improvement (avg < 70):")
for idx in struggling:
    print(f"Student {idx+1} (Avg: {student_avgs[idx]:.2f})")

# Most challenging subject
most_challenging = np.argmin(subject_means)
print(f"\nMost challenging subject: {subjects[most_challenging]} "
      f"(Mean: {subject_means[most_challenging]:.2f})")

# Percentile ranks
print("\nPercentile ranks calculated:")
for i, avg in enumerate(student_avgs[:5], 1):
    percentile = (np.sum(student_avgs < avg) / len(student_avgs)) * 100
    print(f"Student {i}: {avg:.2f} (Percentile: {percentile:.1f}%)")
```

**Explanation:**
- `axis=0` aggregates across students for subject stats
- `axis=1` aggregates across subjects for student performance
- `np.argsort()[::-1]` ranks students from highest to lowest
- List comprehension applies grading logic to all students
- `np.where()` finds indices meeting condition
- `np.argmin()` identifies most challenging subject
- Percentile rank = (# scores below / total) × 100
- Comprehensive analysis combines multiple statistical operations

---

### Key Concepts Demonstrated:

1. **Basic Statistics:**
   - Mean, median for central tendency
   - Std, var for spread
   - Min, max, range for bounds

2. **Axis Operations:**
   - axis=0: column-wise (across students, per subject)
   - axis=1: row-wise (across subjects, per student)
   - No axis: overall statistics

3. **Percentiles:**
   - Quartiles divide into 4 parts
   - IQR for outlier detection
   - Multiple percentiles at once

4. **Practical Applications:**
   - Rankings using argsort
   - Distribution analysis
   - Performance identification
   - Trend analysis

5. **Best Practices:**
   - Use appropriate axis for aggregation
   - Combine multiple statistics for insights
   - Round outputs for readability
   - Validate results make sense
