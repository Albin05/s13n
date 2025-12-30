## Editorials: Use Boolean Indexing

### Q1 Solution: Filter Array with Simple Condition

```python
import numpy as np

# Create array
arr = np.array([12, 45, 23, 51, 34, 18, 67, 8, 92])

# Values > 30
greater_30 = arr[arr > 30]
print(f"Values > 30: {greater_30}")

# Values <= 20
less_equal_20 = arr[arr <= 20]
print(f"Values <= 20: {less_equal_20}")

# Values == 45
equal_45 = arr[arr == 45]
print(f"Values == 45: {equal_45}")

# Count > 50
count = len(arr[arr > 50])
print(f"Count > 50: {count}")
```

**Explanation:**
- `arr[arr > 30]` creates boolean mask and filters in one step
- Each comparison operator creates a boolean array
- `len()` counts filtered elements
- Boolean indexing returns new array with matching elements

---

### Q2 Solution: Create and Use Boolean Masks

```python
import numpy as np

# Create array
temps = np.array([28, 32, 25, 35, 22, 38, 30, 19])

# Create mask for < 30
mask_cold = temps < 30
print(f"Mask for temps < 30: {mask_cold}")

# Use mask to extract
cold_temps = temps[mask_cold]
print(f"Cold temps: {cold_temps}")

# Mask for range 25-35
mask_range = (temps >= 25) & (temps <= 35)
print(f"Mask for 25-35 range: {mask_range}")

# Extract using mask
temps_range = temps[mask_range]
print(f"Temps in range: {temps_range}")
```

**Explanation:**
- Mask is boolean array: `temps < 30` → `[True, False, ...]`
- Store mask in variable for reuse
- For ranges, use `&` (AND) with parentheses
- `(temps >= 25) & (temps <= 35)` both conditions must be True

---

### Q3 Solution: Combine Multiple Conditions

```python
import numpy as np

# Create array
scores = np.array([85, 92, 67, 78, 95, 88, 73, 81, 90, 65])

# Between 70 and 85 (AND)
range_70_85 = scores[(scores >= 70) & (scores <= 85)]
print(f"Scores 70-85: {range_70_85}")

# < 70 OR > 90 (OR)
outside = scores[(scores < 70) | (scores > 90)]
print(f"Scores < 70 or > 90: {outside}")

# NOT in range 75-85 (NOT)
not_in_range = scores[~((scores >= 75) & (scores <= 85))]
print(f"Scores NOT 75-85: {not_in_range}")

# == 85 or == 95 (OR with equality)
exact = scores[(scores == 85) | (scores == 95)]
print(f"Scores == 85 or == 95: {exact}")

# Between 80 and 90 (exclusive)
count = len(scores[(scores > 80) & (scores < 90)])
print(f"Count 80-90 (exclusive): {count}")
```

**Explanation:**
- `&` = AND (both conditions True)
- `|` = OR (at least one condition True)
- `~` = NOT (inverts condition)
- **Must use parentheses** around each condition
- Exclusive range uses `>` and `<`, inclusive uses `>=` and `<=`

---

### Q4 Solution: Filter and Modify Values

```python
import numpy as np

# Create array
prices = np.array([25, 150, 75, 200, 50, 180, 30, 120])

# Print original
print(f"Original: {prices}")

# Apply 10% discount to prices > 100
prices[prices > 100] = prices[prices > 100] * 0.9
print(f"After 10% discount on >100: {prices}")

# Cap at 150
prices[prices > 150] = 150
print(f"After cap at 150: {prices}")

# Floor at 40
prices[prices < 40] = 40
print(f"After floor at 40: {prices}")
```

**Explanation:**
- `prices[prices > 100] = prices[prices > 100] * 0.9` modifies in-place
- Filter on left side selects elements to modify
- Filter on right side gets current values to compute new values
- `prices[prices > 150] = 150` caps all high values
- Boolean indexing allows conditional modification without loops

---

### Q5 Solution: Analyze Sales Data

```python
import numpy as np

# Sales data
sales = np.array([1200, 1500, 800, 2000, 1800, 950, 1100, 2200, 1600, 1300])

# High-performing days (>= 1500)
high = sales[sales >= 1500]
print(f"High-performing days: {high}")

# Average of high-performing
avg_high = high.mean()
print(f"Average high performance: {avg_high}")

# Low-performing days (< 1200)
low = sales[sales < 1200]
print(f"Low-performing days: {low}")

# Count between 1000-1500
count = len(sales[(sales >= 1000) & (sales <= 1500)])
print(f"Days with sales 1000-1500: {count}")

# Exceptional performance (>= 2000)
exceptional = sales[sales >= 2000]
print(f"Exceptional days: {exceptional}")

# Percentage high-performing
percentage = (len(high) / len(sales)) * 100
print(f"High-performance percentage: {percentage}%")
```

**Explanation:**
- Filter first: `sales[sales >= 1500]`
- Then analyze filtered data: `.mean()`
- Combine filtering with aggregation
- `len()` counts filtered elements
- Calculate percentage: `(filtered_count / total_count) * 100`
- Boolean indexing enables complex data analysis without loops

**Key Concepts Covered:**
1. Simple boolean indexing with comparison operators
2. Creating and reusing boolean masks
3. Combining conditions with `&`, `|`, `~`
4. Modifying values through boolean indexing
5. Practical data analysis with filtering and aggregation
