## Editorials: Stack, Split, and Concatenate Arrays

### Q1 Solution: Basic Array Concatenation

```python
import numpy as np

# Create arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# 1D concatenation
concat_1d = np.concatenate([arr1, arr2, arr3])
print("1D concatenation:", concat_1d)

# Vertical concatenation (axis=0)
vertical = np.concatenate([matrix1, matrix2], axis=0)
print("\nVertical concat:")
print(vertical)

# Horizontal concatenation (axis=1)
horizontal = np.concatenate([matrix1, matrix2], axis=1)
print("\nHorizontal concat:")
print(horizontal)
```

**Explanation:**
- `np.concatenate()` joins arrays along existing axis
- For 1D arrays, default concatenation creates longer array
- axis=0 stacks vertically (adds rows)
- axis=1 stacks horizontally (adds columns)
- Arrays must have compatible shapes except in concatenation axis

---

### Q2 Solution: Array Stacking Operations

```python
import numpy as np

# Create temperature arrays
city1 = np.array([22, 25, 23])
city2 = np.array([18, 20, 19])
city3 = np.array([30, 32, 31])

# vstack
vstacked = np.vstack([city1, city2, city3])
print("vstack (cities as rows):")
print(vstacked)

# hstack
hstacked = np.hstack([city1, city2, city3])
print("\nhstack (all temps):")
print(hstacked)

# stack with axis=0
stacked_0 = np.stack([city1, city2, city3], axis=0)
print("\nstack axis=0:")
print(stacked_0)

# stack with axis=1
stacked_1 = np.stack([city1, city2, city3], axis=1)
print("\nstack axis=1:")
print(stacked_1)
```

**Explanation:**
- `vstack()` stacks arrays vertically (row-wise)
- `hstack()` stacks arrays horizontally (element-wise for 1D)
- `stack()` with axis=0 creates new first dimension
- `stack()` with axis=1 transposes during stacking
- vstack result: cities as rows, days as columns
- stack axis=1: days as rows, cities as columns

---

### Q3 Solution: Array Splitting Operations

```python
import numpy as np

# Create arrays
arr = np.arange(1, 16)
matrix = np.arange(1, 25).reshape(6, 4)
uneven = np.arange(1, 11)

# Split into 3 equal parts
parts = np.split(arr, 3)
print("Split into 3:")
for i, part in enumerate(parts, 1):
    print(f"Part {i}: {part}")

# Vertical split (rows)
print("\nVertical split (3 parts):")
v_parts = np.vsplit(matrix, 3)
for i, part in enumerate(v_parts, 1):
    print(f"Part {i}:")
    print(part)

# Horizontal split (columns)
print("\nHorizontal split (2 parts):")
h_parts = np.hsplit(matrix, 2)
for i, part in enumerate(h_parts, 1):
    print(f"Part {i}:")
    print(part)

# Unequal split
print("\nUnequal split:")
unequal_parts = np.array_split(uneven, 3)
for i, part in enumerate(unequal_parts, 1):
    print(f"Part {i}: {part}")
```

**Explanation:**
- `np.split()` divides array into equal parts
- `np.vsplit()` splits along axis=0 (rows)
- `np.hsplit()` splits along axis=1 (columns)
- `np.array_split()` allows unequal splits when not evenly divisible
- For 15 elements split by 3: each part has 5 elements
- For 10 elements split by 3: sizes are [4, 3, 3]

---

### Q4 Solution: Student Grades Analysis

```python
import numpy as np

# Student scores
student1 = np.array([85, 90, 78])
student2 = np.array([92, 88, 95])
student3 = np.array([76, 85, 80])
student4 = np.array([88, 92, 87])

# Combine into single array
all_scores = np.vstack([student1, student2, student3, student4])
print("All scores:")
print(all_scores)

# Subject averages (column means)
subject_avg = np.mean(all_scores, axis=0)
print(f"\nSubject averages: {subject_avg}")

# Student averages (row means)
student_avg = np.mean(all_scores, axis=1)
print(f"Student averages: {np.round(student_avg, 2)}")

# Split back into individual arrays
split_scores = np.vsplit(all_scores, 4)
print("\nIndividual student scores after split:")
for i, scores in enumerate(split_scores, 1):
    print(f"Student {i}: {scores.flatten()}")

# Find highest scoring student
max_idx = np.argmax(student_avg)
max_avg = student_avg[max_idx]
print(f"\nHighest scoring student: Student {max_idx + 1} with average {max_avg:.2f}")
```

**Explanation:**
- `vstack()` combines student arrays into (4, 3) matrix
- `axis=0` for column means (per subject)
- `axis=1` for row means (per student)
- `vsplit()` with 4 splits each student back to separate array
- `argmax()` finds index of highest average
- Broadcasting and aggregation work seamlessly after stacking

---

### Q5 Solution: Time Series Data Pipeline

```python
import numpy as np

# Generate data
np.random.seed(42)
station1 = np.random.randint(15, 30, 24)
station2 = np.random.randint(12, 28, 24)
station3 = np.random.randint(18, 32, 24)

# Combine data
combined = np.vstack([station1, station2, station3])
print(f"Combined data shape: {combined.shape}")

# Split into 4 six-hour periods
periods_s1 = np.split(station1, 4)
periods_s2 = np.split(station2, 4)
periods_s3 = np.split(station3, 4)

# Calculate period averages
period_avgs = []
for i in range(4):
    avg_s1 = np.mean(periods_s1[i])
    avg_s2 = np.mean(periods_s2[i])
    avg_s3 = np.mean(periods_s3[i])
    period_avgs.append([avg_s1, avg_s2, avg_s3])

period_avgs = np.array(period_avgs)
print("\nPeriod averages (4 periods × 3 stations):")
print(np.round(period_avgs, 2))

# Warmest period per station
warmest_periods = np.argmax(period_avgs, axis=0)
print("\nWarmest period per station:")
for i, period in enumerate(warmest_periods, 1):
    print(f"Station {i}: Period {period + 1}")

# Morning and evening split
morning = combined[:, :12]
evening = combined[:, 12:]
print(f"\nMorning data (0-12h) shape: {morning.shape}")
print(f"Evening data (12-24h) shape: {evening.shape}")

# Additional analysis
morning_avg = np.mean(morning, axis=1)
evening_avg = np.mean(evening, axis=1)
print(f"\nMorning averages: {np.round(morning_avg, 2)}")
print(f"Evening averages: {np.round(evening_avg, 2)}")
```

**Explanation:**
- `vstack()` combines three stations into (3, 24) array
- `split()` divides each 24-hour array into 4 periods of 6 hours
- Calculate means for each period and station
- `argmax(axis=0)` finds warmest period per station
- Array slicing `[:, :12]` and `[:, 12:]` splits morning/evening
- Combining split and stack operations creates powerful pipelines

**Alternative Approach:**
```python
# More elegant period averaging
combined_reshaped = combined.reshape(3, 4, 6)  # 3 stations, 4 periods, 6 hours
period_avgs = combined_reshaped.mean(axis=2)   # Average over 6 hours
```

This uses reshape instead of split for cleaner period averaging.

---

### Key Concepts Demonstrated:

1. **Concatenation vs Stacking:**
   - concatenate: along existing axis
   - stack: creates new axis
   - vstack/hstack: shortcuts for common patterns

2. **Splitting Strategies:**
   - Equal splits: use split()
   - Unequal splits: use array_split()
   - By dimension: vsplit/hsplit

3. **Data Pipeline Patterns:**
   - Combine → Process → Split
   - Reshape + stack for batch operations
   - Split for cross-validation and train-test

4. **Practical Applications:**
   - Combining data from multiple sources
   - Batch processing
   - Time series windowing
   - Train-validation-test splits

5. **Best Practices:**
   - Check shapes before/after operations
   - Use appropriate method for task
   - Consider reshape as alternative to split
   - Combine operations for efficiency
