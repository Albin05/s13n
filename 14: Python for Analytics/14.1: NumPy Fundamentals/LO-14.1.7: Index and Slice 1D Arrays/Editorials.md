## Editorials: Index and Slice 1D Arrays

### Q1 Solution: Access and Modify Elements

```python
import numpy as np

# Create array
arr = np.array([100, 200, 300, 400, 500])

# Access first element
first = arr[0]
print(f"First element: {first}")

# Access last element using negative indexing
last = arr[-1]
print(f"Last element: {last}")

# Modify third element (index 2)
arr[2] = 999

# Print entire array
print(f"Modified array: {arr}")
```

**Explanation:**
- `arr[0]` accesses the first element (index 0)
- `arr[-1]` accesses the last element using negative indexing
- `arr[2] = 999` modifies the element at index 2
- Indexing in NumPy is zero-based, same as Python lists
- Negative indices count backward from the end

---

### Q2 Solution: Practice Negative Indexing

```python
import numpy as np

# Create array
numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Print last 3 elements using slicing
last_3 = numbers[-3:]
print(f"Last 3 elements: {last_3}")

# Print element at index -5
element = numbers[-5]
print(f"Element at index -5: {element}")

# Modify second-to-last element
numbers[-2] = 888

# Print final array
print(f"Final array: {numbers}")
```

**Explanation:**
- `numbers[-3:]` slices from the 3rd-to-last element to the end
- `numbers[-5]` accesses the 5th element from the end (which is 60)
- `numbers[-2]` refers to the second-to-last element (90 → 888)
- Negative indexing: `-1` = last, `-2` = second-to-last, etc.

---

### Q3 Solution: Basic Slicing Operations

```python
import numpy as np

# Create array
data = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

# Elements from index 2 to 5 (exclusive)
slice_2_to_5 = data[2:5]
print(f"Elements 2 to 5: {slice_2_to_5}")

# First 4 elements
first_4 = data[:4]
print(f"First 4 elements: {first_4}")

# From index 6 to end
from_6 = data[6:]
print(f"From index 6 to end: {from_6}")

# All except first and last
middle = data[1:-1]
print(f"Except first and last: {middle}")

# Entire array using slicing
entire = data[:]
print(f"Entire array: {entire}")
```

**Explanation:**
- `data[2:5]` extracts indices 2, 3, 4 (5 is exclusive)
- `data[:4]` omits start, defaults to 0
- `data[6:]` omits stop, goes to end
- `data[1:-1]` excludes index 0 and last index
- `data[:]` creates a view of the entire array
- **Remember**: Slicing is `[inclusive:exclusive]`

---

### Q4 Solution: Slicing with Step Parameter

```python
import numpy as np

# Create array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Every 2nd element
every_2nd = arr[::2]
print(f"Every 2nd element: {every_2nd}")

# Every 3rd element
every_3rd = arr[::3]
print(f"Every 3rd element: {every_3rd}")

# Index 1 to 8 with step 2
slice_step = arr[1:8:2]
print(f"Index 1 to 8, step 2: {slice_step}")

# Reverse entire array
reversed_arr = arr[::-1]
print(f"Reversed array: {reversed_arr}")

# Every 2nd element in reverse
reverse_2nd = arr[::-2]
print(f"Every 2nd in reverse: {reverse_2nd}")
```

**Explanation:**
- `arr[::2]` uses syntax `[start:stop:step]` with step=2
- `arr[::3]` takes every 3rd element (indices 0, 3, 6, 9)
- `arr[1:8:2]` starts at 1, stops before 8, step 2 (indices 1, 3, 5, 7)
- `arr[::-1]` negative step reverses the array
- `arr[::-2]` reverses and takes every 2nd element
- **Step parameter** controls the increment between indices

---

### Q5 Solution: Analyze Temperature Data

```python
import numpy as np

# Temperature data
temps = np.array([18, 18, 17, 17, 18, 19, 21, 23,
                  26, 28, 30, 31, 32, 32, 31, 30,
                  28, 26, 24, 22, 21, 20, 19, 18])

# First 6 hours (midnight to 6 AM)
first_6 = temps[:6]
print(f"First 6 hours: {first_6}")

# Hours 12-18 (noon to 6 PM)
hours_12_18 = temps[12:18]
print(f"Hours 12-18: {hours_12_18}")

# Every 4th hour
every_4th = temps[::4]
print(f"Every 4th hour: {every_4th}")

# Last 3 hours
last_3 = temps[-3:]
print(f"Last 3 hours: {last_3}")

# Average of afternoon temps (hours 12-17)
afternoon = temps[12:17]
afternoon_avg = afternoon.mean()
print(f"Afternoon average: {afternoon_avg}")
```

**Explanation:**
- `temps[:6]` gets hours 0-5 (midnight to 6 AM)
- `temps[12:18]` gets hours 12-17 (noon to 6 PM, 18 is exclusive)
- `temps[::4]` takes every 4th hour (hours 0, 4, 8, 12, 16, 20)
- `temps[-3:]` gets last 3 hours (hours 21, 22, 23)
- `temps[12:17]` gets hours 12-16 for afternoon average
- `.mean()` calculates the average of the afternoon temperatures

**Practical insight:**
- Slicing is very efficient for extracting time-based data
- Can easily get specific time ranges without loops
- Combining slicing with aggregation methods (like `.mean()`) is powerful

**Key Concepts Covered:**
1. Basic indexing with positive and negative indices
2. Slicing with `[start:stop]` syntax
3. Step parameter for advanced patterns
4. Practical data analysis using slicing
5. Understanding inclusive/exclusive behavior
6. Combining slicing with NumPy methods
