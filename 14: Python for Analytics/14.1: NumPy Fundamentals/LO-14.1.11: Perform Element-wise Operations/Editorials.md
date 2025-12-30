## Editorials: Perform Element-wise Operations

### Q1 Solution: Basic Arithmetic Operations

```python
import numpy as np

# Create array
arr = np.array([5, 10, 15, 20, 25])
print(f"Original: {arr}")

# Add 10
result = arr + 10
print(f"After +10: {result}")

# Multiply by 3
result = arr * 3
print(f"After *3: {result}")

# Divide by 5
result = arr / 5
print(f"After /5: {result}")

# Square all elements
result = arr ** 2
print(f"Squared: {result}")
```

**Explanation:**
- Element-wise operations apply to all elements automatically
- `arr + 10` adds 10 to each element
- `arr * 3` multiplies each element by 3
- `arr / 5` divides each element by 5
- `arr ** 2` squares each element
- Original array remains unchanged

---

### Q2 Solution: Array-to-Array Operations

```python
import numpy as np

# Create arrays
prices = np.array([100, 200, 150, 250, 300])
quantities = np.array([2, 1, 3, 2, 1])

print(f"Prices: {prices}")
print(f"Quantities: {quantities}")

# Calculate revenue
revenue = prices * quantities
print(f"Revenue: {revenue}")

# 10% price increase
new_prices = prices * 1.10
print(f"New prices (10% increase): {new_prices}")

# Price difference
difference = new_prices - prices
print(f"Price difference: {difference}")

# Items with price > 180
mask = prices > 180
print(f"Price > 180: {mask}")
```

**Explanation:**
- `prices * quantities` multiplies corresponding elements
- `prices * 1.10` multiplies all prices by 1.10 (10% increase)
- `new_prices - prices` calculates element-wise difference
- `prices > 180` creates boolean array for comparison
- Arrays must have same shape for element-wise operations

---

### Q3 Solution: In-Place Operations and Comparisons

```python
import numpy as np

# Create array
scores = np.array([75, 88, 92, 65, 78, 95, 82, 70])
print(f"Original scores: {scores}")

# In-place addition of 5
scores += 5
print(f"After adding 5 bonus points: {scores}")

# Boolean array for scores >= 80
passing = scores >= 80
print(f"Scores >= 80: {passing}")

# Count passing students
count = np.sum(passing)
print(f"Number of students with >= 80: {count}")

# Apply curve (reset scores first for demonstration)
scores = np.array([75, 88, 92, 65, 78, 95, 82, 70])
curved = (scores * 1.1) // 1
print(f"Curved scores: {curved.astype(int)}")
```

**Explanation:**
- `scores += 5` modifies array in-place (memory efficient)
- `scores >= 80` creates boolean array
- `np.sum(passing)` counts True values (True = 1, False = 0)
- `scores * 1.1` multiplies all by 1.1
- `// 1` performs floor division to get integers
- `.astype(int)` ensures integer display

---

### Q4 Solution: Temperature Analysis

```python
import numpy as np

# Temperature data
celsius = np.array([22, 25, 28, 24, 20, 23, 26])
print(f"Celsius: {celsius}")

# Convert to Fahrenheit
fahrenheit = celsius * 9/5 + 32
print(f"Fahrenheit: {fahrenheit}")

# Days with temp > 24°C
hot_days = celsius > 24
print(f"Days with temp > 24°C: {hot_days}")

# Calculate averages
avg_celsius = celsius.mean()
avg_fahrenheit = fahrenheit.mean()
print(f"Average Celsius: {avg_celsius}°C")
print(f"Average Fahrenheit: {avg_fahrenheit}°F")

# Difference from average
difference = celsius - avg_celsius
print(f"Difference from average: {difference}")
```

**Explanation:**
- `celsius * 9/5 + 32` converts to Fahrenheit using formula
- Operations follow mathematical order: multiply first, then add
- `celsius.mean()` calculates average temperature
- `celsius - avg_celsius` subtracts scalar from array (element-wise)
- Element-wise operations work with formulas involving multiple steps

---

### Q5 Solution: Financial Calculations

```python
import numpy as np

# Sales data
sales = np.array([50000, 55000, 48000, 62000, 58000, 65000])
print(f"Sales: {sales}")

# Calculate commission (7%)
commission = sales * 0.07
print(f"Monthly commission (7%): {commission}")

# Total commission
total_commission = commission.sum()
print(f"Total commission: ${total_commission}")

# Percentage change from first month
first_month = sales[0]
change = ((sales - first_month) / first_month) * 100
print(f"% Change from month 1: {change}")

# Target (10% above sales)
target = sales * 1.10
print(f"Target (10% above sales): {target}")

# 90% of target
ninety_percent = target * 0.90
print(f"90% of target: {ninety_percent}")

# Met 90% of target
met_target = sales >= ninety_percent
print(f"Met 90% of target: {met_target}")

# Average of sales > 55000
high_sales = sales[sales > 55000]
average_high = high_sales.mean()
print(f"Average of sales > 55000: ${average_high:.2f}")
```

**Explanation:**
- `sales * 0.07` calculates 7% commission for all months
- `commission.sum()` totals all commission values
- `((sales - first_month) / first_month) * 100` calculates percentage change
- `sales[0]` gets first element, broadcasts to all elements in subtraction
- `sales >= ninety_percent` compares arrays element-wise
- `sales[sales > 55000]` filters using boolean indexing
- `.mean()` calculates average of filtered values

**Key Concepts Covered:**
1. Basic element-wise arithmetic operations
2. Array-to-array operations
3. In-place modifications with `+=`, `-=`, etc.
4. Comparison operations creating boolean arrays
5. Combining operations with formulas
6. Using boolean indexing with element-wise operations
