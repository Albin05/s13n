## Editorials: Extracting List Portions Using Slicing

### Q1 Solution: Basic Slicing Operations

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 1. First 4 elements
first_4 = numbers[:4]
print(f"First 4: {first_4}")

# 2. Index 3 to 7
index_3_to_7 = numbers[3:7]
print(f"Index 3 to 7: {index_3_to_7}")

# 3. Last 3 elements
last_3 = numbers[-3:]
print(f"Last 3: {last_3}")

# 4. Except first and last
except_first_last = numbers[1:-1]
print(f"Except first and last: {except_first_last}")

# 5. From index 5 to end
from_5 = numbers[5:]
print(f"From index 5: {from_5}")
```

**Explanation:**
- `[:4]` - Start from beginning, stop at index 4 (exclusive)
- `[3:7]` - Start at index 3, stop at index 7 (exclusive)
- `[-3:]` - Last 3 elements using negative indexing
- `[1:-1]` - Skip first (index 0) and last (index -1)
- `[5:]` - From index 5 to the end

**Key Concept:**
- When start is omitted, defaults to 0
- When stop is omitted, goes to end
- Stop index is always exclusive

---

### Q2 Solution: Using Step in Slicing

```python
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# 1. Every second element
every_2nd = data[::2]
print(f"Every 2nd: {every_2nd}")

# 2. Every third element
every_3rd = data[::3]
print(f"Every 3rd: {every_3rd}")

# 3. Every second from index 1
every_2nd_from_1 = data[1::2]
print(f"Every 2nd from index 1: {every_2nd_from_1}")

# 4. Reversed
reversed_data = data[::-1]
print(f"Reversed: {reversed_data}")

# 5. Every second in reverse
every_2nd_rev = data[::-2]
print(f"Every 2nd reversed: {every_2nd_rev}")
```

**Explanation:**
- `[::2]` - Start at 0, go to end, step by 2
- `[::3]` - Step by 3 through entire list
- `[1::2]` - Start at index 1, step by 2
- `[::-1]` - Negative step reverses the list
- `[::-2]` - Reverse and take every 2nd element

**Step Parameter:**
- Positive step: left to right
- Negative step: right to left
- Default step is 1

---

### Q3 Solution: Slice Assignment and Modification

```python
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Initial: {items}")

# 1. Replace 2-5 with [30, 40, 50]
items[2:5] = [30, 40, 50]
print(f"After replacing 2-5 with [30,40,50]: {items}")

# 2. Delete 5-7
items[5:7] = []
print(f"After deleting 5-7: {items}")

# 3. Insert [100, 200] at index 3
items[3:3] = [100, 200]
print(f"After inserting at 3: {items}")

# 4. Replace every second with zeros
# First, determine how many elements
num_elements = len(items[::2])
items[::2] = [0] * num_elements
print(f"After replacing evens with 0: {items}")
```

**Explanation:**
- `items[2:5] = [30, 40, 50]` - Replaces indices 2, 3, 4
- `items[5:7] = []` - Deletes by replacing with empty list
- `items[3:3] = [100, 200]` - Inserts at index 3 (empty slice)
- `items[::2] = [0] * num_elements` - Replaces every 2nd element

**Slice Assignment Rules:**
- Can replace with different length (except with step)
- Empty list deletes elements
- Zero-length slice (like [3:3]) inserts
- With step, replacement must be same length

---

### Q4 Solution: Temperature Data Analysis

```python
temps = [65, 66, 64, 63, 62, 61, 62, 64, 68, 72, 75, 78,
         80, 82, 83, 81, 79, 76, 73, 70, 68, 67, 66, 65]

# 1. Morning (6-12)
morning = temps[6:12]
morning_avg = sum(morning) / len(morning)
print(f"Morning (6-12): {morning}")
print(f"  Average: {morning_avg:.1f}°F\n")

# 2. Afternoon (12-18)
afternoon = temps[12:18]
afternoon_avg = sum(afternoon) / len(afternoon)
print(f"Afternoon (12-18): {afternoon}")
print(f"  Average: {afternoon_avg:.1f}°F\n")

# 3. Evening (18-24)
evening = temps[18:24]
evening_avg = sum(evening) / len(evening)
print(f"Evening (18-24): {evening}")
print(f"  Average: {evening_avg:.1f}°F\n")

# 4. Every 3rd hour
every_3rd = temps[::3]
every_3rd_avg = sum(every_3rd) / len(every_3rd)
print(f"Every 3rd hour: {every_3rd}")
print(f"  Average: {every_3rd_avg:.1f}°F")
```

**Explanation:**
- `temps[6:12]` - Hours 6-11 (indices 6-11)
- `temps[12:18]` - Hours 12-17 (indices 12-17)
- `temps[18:24]` - Hours 18-23 (indices 18-23)
- `temps[::3]` - Every 3rd reading (hours 0, 3, 6, 9, etc.)
- `sum(list) / len(list)` - Calculate average
- `.1f` format - Round to 1 decimal place

**Data Analysis Pattern:**
- Extract relevant time windows using slicing
- Process extracted data (sum, average, etc.)
- Present results clearly

---

### Q5 Solution: Sales Data Processing

```python
sales = [120, 135, 142, 128, 156, 189, 201, 145, 132, 128,
         167, 178, 192, 205, 198, 176, 188, 194, 203, 210,
         189, 176, 182, 195, 208, 215, 198, 187, 179, 165]

# 1. Week 1 and Week 4
week1 = sales[0:7]
week4 = sales[21:28]
print(f"Week 1 sales: {week1}")
print(f"  Total: ${sum(week1)}\n")
print(f"Week 4 sales: {week4}")
print(f"  Total: ${sum(week4)}\n")

# 2. Weekend sales (positions 5-6, 12-13, 19-20, 26-27)
# Extracting individually then combining
weekends = sales[5:7] + sales[12:14] + sales[19:21] + sales[26:28]
print(f"Weekend sales: {weekends}")
print(f"  Total: ${sum(weekends)}\n")

# 3. Weekly summary (every 7th day)
weekly = sales[::7]
print(f"Weekly summary (every 7th): {weekly}")
print(f"  Total: ${sum(weekly)}\n")

# 4. Second half
mid = len(sales) // 2
second_half = sales[mid:]
print(f"Second half: {second_half}")
print(f"  Total: ${sum(second_half)}\n")

# 5. Last 10 days reversed
last_10_rev = sales[-10:][::-1]
print(f"Last 10 days reversed: {last_10_rev}")
print(f"  Total: ${sum(last_10_rev)}")
```

**Explanation:**
- `sales[0:7]` - Days 0-6 (Week 1)
- `sales[21:28]` - Days 21-27 (Week 4)
- `sales[5:7] + sales[12:14] + ...` - Concatenate weekend slices
- `sales[::7]` - Every 7th day (day 0, 7, 14, 21)
- `sales[mid:]` - From middle to end
- `sales[-10:][::-1]` - Last 10 reversed (two operations)
  - First `[-10:]` gets last 10
  - Then `[::-1]` reverses them

**Advanced Patterns:**
- Concatenating multiple slices with `+`
- Using `len(sales) // 2` for dynamic midpoint
- Chaining slice operations: `sales[-10:][::-1]`
- Using `sum()` for totals

**Key Concepts:**
- Slicing extracts data without loops
- Can combine multiple slices
- Chain operations for complex transformations
- Perfect for time-series and sequential data analysis
