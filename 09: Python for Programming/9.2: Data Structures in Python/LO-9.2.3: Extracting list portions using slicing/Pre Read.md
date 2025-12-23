# Pre-Read: Extracting List Portions Using Slicing

## What You'll Learn
In this lesson, you'll learn how to extract portions (subsets) of lists using slicing - a powerful Python feature for getting multiple items at once.

## Why This Matters
Slicing is essential for:
- Getting the top 10 scores from a leaderboard
- Extracting this week's data from a month of readings
- Displaying the first 5 search results
- Grabbing the last 3 items added to a cart
- Splitting data into training and testing sets in data science

Slicing lets you work with portions of data without manually accessing individual items.

---

## What is Slicing?

**Slicing** extracts a portion of a list by specifying a start and end position. The result is a new list.

**Basic syntax:**
```python
list[start:stop]
```

**Key rule:** Gets items from `start` up to (but NOT including) `stop`

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
portion = numbers[2:6]  # [2, 3, 4, 5] (stops BEFORE index 6)
```

---

## Basic Slicing Examples

### Get Items from Index 1 to 4

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#         0        1         2         3      4

subset = fruits[1:4]
print(subset)  # ["banana", "cherry", "date"]
# Gets indices 1, 2, 3 (NOT 4)
```

### First N Items

```python
numbers = [10, 20, 30, 40, 50, 60]

first_three = numbers[:3]  # [10, 20, 30]
# Omitting start means "from beginning"
```

### Last N Items

```python
numbers = [10, 20, 30, 40, 50, 60]

last_three = numbers[-3:]  # [40, 50, 60]
# Negative index with omitted stop means "to end"
```

### From Index to End

```python
colors = ["red", "green", "blue", "yellow", "purple"]

from_index_2 = colors[2:]  # ["blue", "yellow", "purple"]
# From index 2 to end
```

---

## Slicing with Step

**Extended syntax:**
```python
list[start:stop:step]
```

The `step` determines how many items to skip.

### Every Second Item

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = numbers[::2]  # [0, 2, 4, 6, 8]
# Start=0 (default), stop=end (default), step=2

odds = numbers[1::2]  # [1, 3, 5, 7, 9]
# Start=1, stop=end, step=2
```

### Every Third Item

```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

every_third = letters[::3]  # ['a', 'd', 'g']
```

---

## Reverse a List

Use a negative step to reverse:

```python
numbers = [1, 2, 3, 4, 5]

reversed_nums = numbers[::-1]  # [5, 4, 3, 2, 1]
# Start=end, stop=beginning, step=-1 (backwards)
```

---

## Real-World Examples

### Example 1: Top 5 Scores

```python
high_scores = [9500, 8700, 8200, 7900, 7500, 7200, 6800, 6500]

top_5 = high_scores[:5]
print("Top 5:", top_5)  # [9500, 8700, 8200, 7900, 7500]
```

### Example 2: Recent Activity

```python
# Last 7 days of temperatures
all_temps = [72, 71, 73, 75, 76, 78, 77, 79, 80, 81, 79, 78, 76, 75]

last_week = all_temps[-7:]
print("Last 7 days:", last_week)  # [79, 80, 81, 79, 78, 76, 75]
```

### Example 3: Pagination

```python
all_results = list(range(1, 101))  # 100 items

page_size = 10
page_1 = all_results[0:10]    # Items 1-10
page_2 = all_results[10:20]   # Items 11-20
page_3 = all_results[20:30]   # Items 21-30
```

### Example 4: Skip Header Row

```python
data_with_header = ["Name,Age,City", "Alice,25,NYC", "Bob,30,LA", "Charlie,22,SF"]

data_only = data_with_header[1:]  # Skip first row
print(data_only)  # ["Alice,25,NYC", "Bob,30,LA", "Charlie,22,SF"]
```

---

## Omitting Start, Stop, or Step

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers[:]      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (entire list, creates copy)
numbers[3:]     # [3, 4, 5, 6, 7, 8, 9] (from index 3 to end)
numbers[:5]     # [0, 1, 2, 3, 4] (from start to index 5)
numbers[2:7]    # [2, 3, 4, 5, 6] (from index 2 to 7)
numbers[::2]    # [0, 2, 4, 6, 8] (every second item)
numbers[1::2]   # [1, 3, 5, 7, 9] (every second, starting at 1)
numbers[::-1]   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed)
```

---

## Slicing Creates a Copy

Slicing creates a **new list**, not a reference:

```python
original = [1, 2, 3, 4, 5]
sliced = original[1:4]  # [2, 3, 4]

sliced[0] = 99
print(sliced)    # [99, 3, 4]
print(original)  # [1, 2, 3, 4, 5] (unchanged!)
```

**Copy entire list:**
```python
original = [1, 2, 3, 4, 5]
copy = original[:]  # Creates a complete copy
```

---

## Negative Indices in Slicing

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers[-5:]     # [5, 6, 7, 8, 9] (last 5 items)
numbers[:-3]     # [0, 1, 2, 3, 4, 5, 6] (all except last 3)
numbers[-7:-2]   # [3, 4, 5, 6, 7] (from -7 to -2, not including -2)
```

---

## Try It Yourself (Before Class)

Run this code:

```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Try these slices
print(letters[2:7])    # What do you get?
print(letters[:4])     # First four?
print(letters[5:])     # From index 5 onwards?
print(letters[::2])    # Every second?
print(letters[::-1])   # Reversed?
print(letters[-3:])    # Last three?

# Practice
numbers = list(range(20))  # [0, 1, 2, ..., 19]
# Get: [5, 6, 7, 8, 9]
# Get: [10, 12, 14, 16, 18] (evens from 10-18)
# Get: [15, 16, 17, 18, 19] (last 5)
```

**Questions:**
1. How do you get the first 3 items?
2. How do you get the last 5 items?
3. How do you reverse a list?
4. What's the difference between `[2:5]` and `[2:5:1]`?

---

## Common Slicing Patterns

### Get Middle Portion

```python
items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
middle = items[3:6]  # [4, 5, 6]
```

### Remove First and Last

```python
data = [10, 20, 30, 40, 50]
middle_only = data[1:-1]  # [20, 30, 40]
```

### Split in Half

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mid = len(numbers) // 2

first_half = numbers[:mid]   # [1, 2, 3, 4, 5]
second_half = numbers[mid:]  # [6, 7, 8, 9, 10]
```

---

## Key Takeaways

Before class, remember:
1. **Syntax: list[start:stop:step]** - extracts portion of list
2. **Excludes stop index** - goes up to but not including stop
3. **Omit for defaults** - [:5] means [0:5], [3:] means [3:end]
4. **Negative step reverses** - [::-1] reverses list
5. **Creates new list** - slicing doesn't modify original

## What's Next?

In the live session, we'll:
- Practice complex slicing scenarios
- Combine slicing with list methods
- Use slicing for data manipulation
- Learn advanced slicing techniques
- Apply slicing to solve real problems

See you in class!
