## Pre-Read: Using Tuple Methods count() and index()

**Duration:** 5 minutes

---

## What Are Tuple Methods?

Tuple methods are the **only 2 tools** you get with tuples: `count()` and `index()`. Think of them as **"Where?" and "How many?"** - the two questions you can ask about immutable data!

### Simple Analogy

Think of tuple methods like **asking about a printed book**:
- **count()**: "How many times does 'Python' appear?" - Count occurrences
- **index()**: "On what page is 'Chapter 5'?" - Find location
- **Can't edit**: No erase, add pages, or reorder
- **Just search**: Read-only access to information

Or like **searching in a history textbook**:
- **count()**: "How many times is 'Lincoln' mentioned?" (frequency)
- **index()**: "What page first mentions 'Lincoln'?" (location)
- **Permanent**: Content can't change (it's published!)
- **Two operations**: Count and find - that's all you need!

### Why So Few Methods?

**Lists have 11 methods**. Tuples have 2. Why?

**The answer**: Lists can change, tuples can't!

**List methods** (need to modify):
- `append()` - Adds item → Changes list
- `remove()` - Deletes item → Changes list
- `sort()` - Reorders → Changes list
- `reverse()` - Flips order → Changes list

**Tuple methods** (read-only):
- `count()` - Just looks and counts → Safe!
- `index()` - Just looks and finds → Safe!

**Philosophy**: **"Can't change? Don't offer change methods!"**

It's not missing features - it's **design by subtraction**! Fewer methods = fewer ways to make mistakes.

### The Dynamic Duo

**count()** and **index()** are perfect partners:

**count() is the friendly one**:
- "How many 2s?" → Tells you (even if zero)
- Never crashes, always answers
- Returns `0` for "not found" (safe!)

**index() is the strict one**:
- "Where is 5?" → Tells you the position
- Crashes if not found (careful!)
- Needs error handling (try-except)

**Together**: Answer all search questions!

---

### What You'll Learn

Tuples have only **2 methods**: `count()` and `index()`. That's it! Simple but powerful.

---

### Why Only 2 Methods?

Remember: Tuples are **immutable**. They can't be changed after creation.

**No modification methods:**
- ❌ No `append()`, `remove()`, `insert()`
- ❌ No `sort()`, `reverse()`
- ✅ Only `count()` and `index()`

This simplicity makes tuples fast and safe!

---

### Method 1: count()

**What it does:** Counts how many times a value appears.

```python
numbers = (1, 2, 3, 2, 4, 2, 5)

# Count how many 2s
count = numbers.count(2)
print(count)  # 3
```

**Key Points:**
- Never raises an error
- Returns 0 if value not found
- Safe to use anywhere

```python
fruits = ('apple', 'banana', 'orange')

print(fruits.count('banana'))  # 1
print(fruits.count('grape'))   # 0 (not found - no error!)
```

---

### Method 2: index()

**What it does:** Finds the position (index) of a value.

```python
colors = ('red', 'blue', 'green', 'yellow')

# Find position of 'blue'
position = colors.index('blue')
print(position)  # 1
```

**Important Warning:** Raises error if not found!

```python
colors = ('red', 'blue', 'green')

# This works
pos = colors.index('blue')  # 1

# This crashes!
# pos = colors.index('purple')  # ValueError!
```

**Safe way:**
```python
try:
    pos = colors.index('purple')
except ValueError:
    print("Not found")
```

---

### The Difference

```python
scores = (85, 92, 78, 92, 85, 88)

# count() - How many?
count_92 = scores.count(92)
print(f"92 appears {count_92} times")  # 2 times

# index() - Where is it?
position = scores.index(92)
print(f"First 92 at position {position}")  # position 1
```

**Remember:**
- `count()` → How many times?
- `index()` → Where is it?

---

### Finding Multiple Occurrences

**Problem:** index() only finds the FIRST occurrence.

```python
numbers = (10, 20, 10, 30, 10)

first = numbers.index(10)
print(first)  # 0 (only the first one!)
```

**Solution:** Use start parameter

```python
numbers = (10, 20, 10, 30, 10)

# Find first
first = numbers.index(10)        # 0

# Find second (start after first)
second = numbers.index(10, first + 1)  # 2

# Find third
third = numbers.index(10, second + 1)  # 4
```

---

### Practical Example: Voting

```python
votes = ('Alice', 'Bob', 'Alice', 'Charlie', 'Alice')

# Count votes for Alice
alice_votes = votes.count('Alice')
print(f"Alice: {alice_votes} votes")  # 3 votes

# Find where Alice's first vote was
first_vote = votes.index('Alice')
print(f"Alice's first vote at position {first_vote}")  # 0
```

---

### Try to Predict

```python
# Question 1
data = (5, 10, 15, 10, 20)
result = data.count(10)
# What is result?

# Question 2
colors = ('red', 'blue', 'green')
pos = colors.index('blue')
# What is pos?

# Question 3
numbers = (1, 2, 3)
val = numbers.count(5)
# What is val?

# Question 4
items = ('a', 'b', 'c')
# items.index('d')
# What happens?
```

**Answers:**
1. `2` (two 10s in the tuple)
2. `1` (blue is at index 1)
3. `0` (5 not found, count returns 0)
4. `ValueError` (d not found, index raises error)

---

### Safe Usage Pattern

**Always do this with index():**

```python
# Pattern 1: Try-except
try:
    pos = my_tuple.index(value)
    print(f"Found at {pos}")
except ValueError:
    print("Not found")

# Pattern 2: Check first with count
if my_tuple.count(value) > 0:
    pos = my_tuple.index(value)
    print(f"Found at {pos}")
else:
    print("Not found")
```

---

### What Makes Them Useful?

**count() is great for:**
- Checking if something exists
- Finding duplicates
- Counting frequency
- Voting systems

**index() is great for:**
- Finding position
- Locating data
- Validation
- Pattern matching

**Together they're powerful:**
```python
# Check if value exists, then find it
if scores.count(100) > 0:
    position = scores.index(100)
    print(f"Perfect score at position {position}!")
```

---

### Remember

**Two Methods:**
- `count(value)` - How many? (Safe)
- `index(value)` - Where? (Use with care)

**Key Differences:**
- count() never errors → Always safe
- index() may error → Need try-except or check first

**Only First:**
- index() finds only first occurrence
- Need loop for finding all

---

### Get Ready!

In the lesson, you'll learn:
- Using count() for frequency analysis
- Using index() safely with error handling
- Finding all occurrences with loops
- Combining both methods effectively
- Real-world applications

**Simple methods, powerful results!**
