## Extracting List Portions Using Slicing

### Basic Slice Syntax

```python
# Syntax: list[start:stop:step]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
numbers[2:7]    # [2, 3, 4, 5, 6]
numbers[0:5]    # [0, 1, 2, 3, 4]

# Stop is exclusive!
numbers[3:6]    # [3, 4, 5] (not 6)
```

**Key:** Start is inclusive, stop is exclusive.

---

### Omitting Start and Stop

```python
data = [10, 20, 30, 40, 50, 60, 70]

# Omit start (from beginning)
data[:4]     # [10, 20, 30, 40]

# Omit stop (to end)
data[3:]     # [40, 50, 60, 70]

# Omit both (copy entire list)
data[:]      # [10, 20, 30, 40, 50, 60, 70]
```

**Common Patterns:**
- `[:n]` - First n elements
- `[n:]` - From n to end
- `[:]` - Shallow copy

---

### Negative Indices

```python
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Last 3 elements
items[-3:]      # [8, 9, 10]

# All except last 2
items[:-2]      # [1, 2, 3, 4, 5, 6, 7, 8]

# Mix positive and negative
items[2:-2]     # [3, 4, 5, 6, 7, 8]

# From -5 to -2
items[-5:-2]    # [6, 7, 8]
```

**Benefits:**
- Access from end without knowing length
- Clean syntax for "all except last n"

---

### Step Parameter

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Every 2nd element
numbers[::2]    # [0, 2, 4, 6, 8]

# Every 3rd element
numbers[::3]    # [0, 3, 6, 9]

# Every 2nd from index 1
numbers[1::2]   # [1, 3, 5, 7, 9]

# With range and step
numbers[1:8:2]  # [1, 3, 5, 7]
```

**Negative Step (Reverse):**
```python
numbers[::-1]   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
numbers[::-2]   # [9, 7, 5, 3, 1]
```

---

### Slice Assignment

```python
# Replace slice
nums = [1, 2, 3, 4, 5]
nums[1:3] = [20, 30]
# nums is now [1, 20, 30, 4, 5]

# Different length OK
nums = [1, 2, 3, 4, 5]
nums[1:3] = [20, 30, 40, 50]
# nums is now [1, 20, 30, 40, 50, 4, 5]

# Delete with empty list
nums = [1, 2, 3, 4, 5]
nums[1:3] = []
# nums is now [1, 4, 5]

# Insert (empty slice)
nums = [1, 2, 5]
nums[2:2] = [3, 4]
# nums is now [1, 2, 3, 4, 5]
```

**With Step:**
```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums[::2] = [10, 20, 30, 40, 50]
# nums is now [10, 1, 20, 3, 30, 5, 40, 7, 50, 9]

# Must match length when using step!
```

---

### Common Patterns

**Split List:**
```python
data = [1, 2, 3, 4, 5, 6, 7, 8]
mid = len(data) // 2

first_half = data[:mid]    # [1, 2, 3, 4]
second_half = data[mid:]   # [5, 6, 7, 8]
```

**Remove First/Last:**
```python
items = ['start', 'a', 'b', 'c', 'end']
core = items[1:-1]  # ['a', 'b', 'c']
```

**Reverse:**
```python
original = [1, 2, 3, 4, 5]
reversed = original[::-1]  # [5, 4, 3, 2, 1]

# Check palindrome
is_palindrome = lst == lst[::-1]
```

**Copy:**
```python
original = [1, 2, 3]
copy = original[:]

copy.append(4)
# original still [1, 2, 3]
# copy is [1, 2, 3, 4]
```

**Skip Elements:**
```python
# Every nth element
every_third = data[::3]

# Alternating
odds = data[1::2]
evens = data[::2]
```

---

### Processing Chunks

```python
data = list(range(20))
chunk_size = 5

for i in range(0, len(data), chunk_size):
    chunk = data[i:i+chunk_size]
    print(chunk)
# [0, 1, 2, 3, 4]
# [5, 6, 7, 8, 9]
# [10, 11, 12, 13, 14]
# [15, 16, 17, 18, 19]
```

**Sliding Window:**
```python
nums = [1, 2, 3, 4, 5, 6]
window_size = 3

for i in range(len(nums) - window_size + 1):
    window = nums[i:i+window_size]
    print(window)
# [1, 2, 3]
# [2, 3, 4]
# [3, 4, 5]
# [4, 5, 6]
```

---

### Quick Reference

```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic
lst[2:7]     # [2, 3, 4, 5, 6]
lst[:5]      # [0, 1, 2, 3, 4]
lst[5:]      # [5, 6, 7, 8, 9]
lst[:]       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Negative
lst[-3:]     # [7, 8, 9]
lst[:-3]     # [0, 1, 2, 3, 4, 5, 6]
lst[2:-2]    # [2, 3, 4, 5, 6, 7]

# Step
lst[::2]     # [0, 2, 4, 6, 8]
lst[1::2]    # [1, 3, 5, 7, 9]
lst[::-1]    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Assignment
lst[2:5] = [20, 30, 40]  # Replace
lst[2:2] = [10]          # Insert
lst[2:5] = []            # Delete
```

**Remember:**
- Creates new list (except assignment)
- Stop is exclusive
- Negative step reverses
- Empty slice for insertion
