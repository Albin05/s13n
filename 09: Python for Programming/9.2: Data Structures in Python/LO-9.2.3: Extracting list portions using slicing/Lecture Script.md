## Lecture Script: Extracting List Portions Using Slicing


---

### CS Theory Bite

> **Origin**: Slicing syntax `[start:stop:step]` was inspired by **MATLAB** and **Fortran 90** array sections. Python creates a **new list** (copy), not a view.
>
> **Analogy**: Slicing is like **cutting a deck of cards** — pick any contiguous section, or take every Nth card with step.
>
> **Why it matters**: Slicing extracts subsequences in one expression — replacing verbose loop-based copying.



### Hook (2 minutes)

"Imagine you're working with a dataset containing sales data for the entire year - 365 days worth of numbers. Your manager asks you to analyze just the data for Q1, or maybe just the weekends, or perhaps every other day. Would you manually copy each individual value? Of course not! That's where slicing becomes your superpower.

Slicing is like having a smart knife that can cut exactly the portion you need from a list. Whether you want the first 10 items, the last 5, every third element, or even the entire list in reverse - slicing handles it all with a single, elegant syntax.

Today, we'll master list slicing - one of Python's most powerful and frequently used features. By the end, you'll be extracting, copying, and manipulating list portions with just a few keystrokes."

---

### Section 1: Slice Syntax Basics (3 minutes)

The slice syntax uses square brackets with colons to specify the portion you want:

```python
# Syntax: list[start:stop:step]
# start: index where slice begins (inclusive)
# stop: index where slice ends (exclusive)
# step: interval between elements (optional, default 1)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
first_five = numbers[0:5]
print(first_five)  # [0, 1, 2, 3, 4]

# From index 3 to 7
middle = numbers[3:7]
print(middle)  # [3, 4, 5, 6]

# Notice: stop index is NOT included
# numbers[3:7] gets indices 3, 4, 5, 6 (not 7)
```

**Key Points:**
- Start is inclusive, stop is exclusive
- `[start:stop]` gets elements from start up to (but not including) stop
- Original list remains unchanged - slicing creates a new list

**Why Exclusive Stop?**
```python
# Exclusive stop makes splitting easier
data = [1, 2, 3, 4, 5, 6, 7, 8]

first_half = data[0:4]   # [1, 2, 3, 4]
second_half = data[4:8]  # [5, 6, 7, 8]

# No overlap, no gaps - perfect split
```

---

### Section 2: Omitting Start and Stop (3 minutes)

You can omit start or stop to slice from the beginning or to the end:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Omit start - begins from index 0
first_five = numbers[:5]
print(first_five)  # [0, 1, 2, 3, 4]

# Omit stop - goes to the end
from_five = numbers[5:]
print(from_five)  # [5, 6, 7, 8, 9]

# Omit both - copies entire list
copy = numbers[:]
print(copy)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Verify it's a copy
copy[0] = 999
print(numbers[0])  # Still 0 - original unchanged
```

**Common Patterns:**

```python
fruits = ['apple', 'banana', 'orange', 'mango', 'grape']

# First 3 items
print(fruits[:3])  # ['apple', 'banana', 'orange']

# Last 2 items
print(fruits[-2:])  # ['mango', 'grape']

# Everything except first
print(fruits[1:])  # ['banana', 'orange', 'mango', 'grape']

# Everything except last
print(fruits[:-1])  # ['apple', 'banana', 'orange', 'mango']
```

**Creating Shallow Copies:**
```python
# [:] is the standard way to copy a list
original = [1, 2, 3, 4, 5]
copy = original[:]

# Modify copy
copy.append(6)

print(original)  # [1, 2, 3, 4, 5] - unchanged
print(copy)      # [1, 2, 3, 4, 5, 6]
```

---

### Section 3: Using Negative Indices in Slices (3 minutes)

Negative indices count from the end, making it easy to work with list tails:

```python
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#       0   1   2   3   4   5   6   7   8   9
#      -10 -9  -8  -7  -6  -5  -4  -3  -2  -1

# Last 3 elements
last_three = data[-3:]
print(last_three)  # [80, 90, 100]

# All except last 2
except_last_two = data[:-2]
print(except_last_two)  # [10, 20, 30, 40, 50, 60, 70, 80]

# From -7 to -3 (exclusive)
middle_portion = data[-7:-3]
print(middle_portion)  # [40, 50, 60, 70]

# Mix positive and negative
mixed = data[2:-2]
print(mixed)  # [30, 40, 50, 60, 70, 80]
```

**Practical Examples:**

```python
log_entries = ['entry1', 'entry2', 'entry3', 'entry4', 'entry5',
               'entry6', 'entry7', 'entry8', 'entry9', 'entry10']

# Get last 5 log entries
recent = log_entries[-5:]
print(recent)  # ['entry6', 'entry7', 'entry8', 'entry9', 'entry10']

# Remove first and last (trim)
trimmed = log_entries[1:-1]
print(trimmed)  # ['entry2', 'entry3', ..., 'entry9']

# Get everything except last 3
main_portion = log_entries[:-3]
print(main_portion)  # ['entry1', 'entry2', ..., 'entry7']
```

---

### Section 4: The Step Parameter (4 minutes)

The step parameter lets you skip elements at regular intervals:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Every second element
evens = numbers[0:10:2]
print(evens)  # [0, 2, 4, 6, 8]

# Every second element starting from index 1
odds = numbers[1:10:2]
print(odds)  # [1, 3, 5, 7, 9]

# Every third element
every_third = numbers[::3]
print(every_third)  # [0, 3, 6, 9]

# From index 2, every 2nd element
from_two = numbers[2::2]
print(from_two)  # [2, 4, 6, 8]
```

**Step with Range:**

```python
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Index 1 to 8, step 2
result = data[1:8:2]
print(result)  # [20, 40, 60, 80]

# First 6 elements, every 2nd
first_six_alternate = data[:6:2]
print(first_six_alternate)  # [10, 30, 50]
```

**Negative Step - Reversing:**

```python
numbers = [1, 2, 3, 4, 5]

# Reverse the entire list
reversed_list = numbers[::-1]
print(reversed_list)  # [5, 4, 3, 2, 1]

# Last 3 in reverse
last_three_rev = numbers[-3:][::-1]
# Or directly: numbers[:-4:-1]
print(last_three_rev)  # [5, 4, 3]

# Every second element in reverse
every_second_rev = numbers[::-2]
print(every_second_rev)  # [5, 3, 1]
```

**Practical Applications:**

```python
# Palindrome check
word = list("racecar")
is_palindrome = word == word[::-1]
print(is_palindrome)  # True

# Process every nth item
transactions = list(range(1, 101))  # 1 to 100

# Process every 10th transaction for audit
audit_sample = transactions[::10]
print(audit_sample)  # [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]

# Get alternating values
readings = [100, 98, 102, 99, 101, 97, 103, 98]
odd_position_readings = readings[::2]
even_position_readings = readings[1::2]
print(odd_position_readings)   # [100, 102, 101, 103]
print(even_position_readings)  # [98, 99, 97, 98]
```

---

### Section 5: Slice Assignment (3 minutes)

Slices can be used on the left side of assignment to modify list portions:

```python
# Replace a slice
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers[2:5] = [30, 40, 50]
print(numbers)  # [1, 2, 30, 40, 50, 6, 7, 8]

# Replace with different length
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = [20, 30, 40, 50]
print(numbers)  # [1, 20, 30, 40, 50, 4, 5]

# Delete elements using slice assignment
numbers = [1, 2, 3, 4, 5, 6, 7]
numbers[2:5] = []
print(numbers)  # [1, 2, 6, 7]

# Insert elements
numbers = [1, 2, 5, 6]
numbers[2:2] = [3, 4]  # Insert at index 2
print(numbers)  # [1, 2, 3, 4, 5, 6]
```

**Replacing with Step:**

```python
# Replace every second element
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[::2] = [10, 20, 30, 40, 50]
print(numbers)  # [10, 1, 20, 3, 30, 5, 40, 7, 50, 9]

# Must match number of elements when using step
# numbers[::2] = [1, 2]  # Error: attempting to replace 5 items with 2
```

**Practical Uses:**

```python
# Replace middle section
grades = [65, 70, 45, 50, 55, 85, 90]
# Teacher adjusts middle grades after curve
grades[2:5] = [60, 65, 70]
print(grades)  # [65, 70, 60, 65, 70, 85, 90]

# Clear portion of list
tasks = ['task1', 'task2', 'task3', 'task4', 'task5']
tasks[1:4] = []  # Remove tasks 2-4
print(tasks)  # ['task1', 'task5']

# Insert multiple items at once
menu = ['Appetizer', 'Main Course', 'Dessert']
menu[2:2] = ['Salad', 'Soup']  # Insert before dessert
print(menu)  # ['Appetizer', 'Main Course', 'Salad', 'Soup', 'Dessert']
```

---

### Section 6: Common Slicing Patterns (2 minutes)

**Split List:**
```python
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mid = len(data) // 2
first_half = data[:mid]
second_half = data[mid:]

print(first_half)   # [1, 2, 3, 4, 5]
print(second_half)  # [6, 7, 8, 9, 10]
```

**Remove Duplicates at Boundaries:**
```python
# Remove first and last
items = ['start', 'a', 'b', 'c', 'end']
core = items[1:-1]
print(core)  # ['a', 'b', 'c']
```

**Chunk Processing:**
```python
data = list(range(20))

# Process in chunks of 5
chunk_size = 5
for i in range(0, len(data), chunk_size):
    chunk = data[i:i+chunk_size]
    print(f"Chunk: {chunk}")
# Chunk: [0, 1, 2, 3, 4]
# Chunk: [5, 6, 7, 8, 9]
# Chunk: [10, 11, 12, 13, 14]
# Chunk: [15, 16, 17, 18, 19]
```

**Sliding Window:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
window_size = 3

for i in range(len(numbers) - window_size + 1):
    window = numbers[i:i+window_size]
    print(f"Window at {i}: {window}")
# Window at 0: [1, 2, 3]
# Window at 1: [2, 3, 4]
# Window at 2: [3, 4, 5]
# ...
```

**Interleave Lists:**
```python
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

combined = [None] * (len(list1) + len(list2))
combined[::2] = list1
combined[1::2] = list2

print(combined)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

### Section 7: Performance and Best Practices (1 minute)

**Memory Efficiency:**
```python
# Slicing creates a new list (shallow copy)
large_list = list(range(1000000))

# This creates a copy
portion = large_list[:1000]  # New list with 1000 elements

# For read-only access on large lists, consider itertools.islice
from itertools import islice

# No copy created - returns iterator
portion_iter = islice(large_list, 1000)
```

**Best Practices:**

1. **Use slicing for copying:**
```python
copy = original[:]  # Clear intent
```

2. **Prefer slicing over loops for extraction:**
```python
# Good
first_ten = data[:10]

# Less efficient
first_ten = []
for i in range(10):
    first_ten.append(data[i])
```

3. **Be cautious with negative step:**
```python
# Clear for reversal
reversed_list = items[::-1]

# Confusing
weird = items[10:2:-2]  # Hard to understand
```

---

### Summary (1 minute)

Today we mastered list slicing - Python's powerful syntax for extracting list portions:

**Key Concepts:**
- **Basic syntax:** `list[start:stop:step]`
- **Start is inclusive, stop is exclusive**
- **Omit start/stop:** `[:5]`, `[5:]`, `[:]`
- **Negative indices:** Count from end (`[-3:]`, `[:-2]`)
- **Step parameter:** Skip elements (`[::2]`), reverse (`[::-1]`)
- **Slice assignment:** Modify portions (`list[2:5] = [...]`)

**Common Patterns:**
- First n: `list[:n]`
- Last n: `list[-n:]`
- Copy: `list[:]`
- Reverse: `list[::-1]`
- Skip: `list[::step]`

**Remember:**
- Slicing always creates a new list
- Original list unchanged unless using slice assignment
- Use slicing for clean, readable code
- Perfect for splitting, sampling, and reversing

Slicing is fundamental to Python - master it, and you'll write more elegant, efficient code. Practice these patterns until they become second nature!
