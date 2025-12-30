## Lecture Notes: Using Tuple Methods count() and index()

**Duration:** 12 minutes

---

### Tuple Methods Overview

**Tuples have only 2 methods:**
1. `count(value)` - Count occurrences
2. `index(value)` - Find position

That's it! Simple and focused.

---

### count() Method

**Syntax:**
```python
tuple.count(value)
```

**Returns:** Number of occurrences (integer)

**Examples:**
```python
numbers = (1, 2, 3, 2, 4, 2)

numbers.count(2)    # 3
numbers.count(5)    # 0 (not found - no error!)
```

**Key Points:**
- Never raises exception
- Returns 0 if not found
- O(n) complexity

**Use Cases:**
```python
# Check if value exists
if scores.count(100) > 0:
    print("Perfect score!")

# Find duplicates
for item in data:
    if data.count(item) > 1:
        print(f"Duplicate: {item}")

# Frequency analysis
votes_for_alice = votes.count('Alice')
```

---

### index() Method

**Syntax:**
```python
tuple.index(value)
tuple.index(value, start)
tuple.index(value, start, end)
```

**Returns:** Index of first occurrence

**Raises:** ValueError if not found!

**Examples:**
```python
colors = ('red', 'blue', 'green', 'blue')

colors.index('blue')       # 1 (first occurrence)
colors.index('blue', 2)    # 3 (start from index 2)
# colors.index('purple')   # ValueError!
```

**Key Points:**
- Only finds FIRST occurrence
- Raises ValueError if not found
- O(n) complexity

**Safe Usage:**
```python
# Method 1: try-except
try:
    pos = tup.index(value)
except ValueError:
    pos = -1

# Method 2: check with count first
if tup.count(value) > 0:
    pos = tup.index(value)
```

---

### Finding All Occurrences

**Problem:** index() only finds first

**Solution:** Loop with start parameter

```python
def find_all(tup, value):
    positions = []
    start = 0
    
    while True:
        try:
            pos = tup.index(value, start)
            positions.append(pos)
            start = pos + 1
        except ValueError:
            break
    
    return positions

numbers = (10, 20, 10, 30, 10)
all_tens = find_all(numbers, 10)
# [0, 2, 4]
```

---

### Combining Both Methods

**Pattern 1: Safe Find**
```python
def safe_find(tup, value):
    if tup.count(value) > 0:
        return tup.index(value)
    return -1
```

**Pattern 2: Verify Count Before Loop**
```python
def find_all_optimized(tup, value):
    count = tup.count(value)
    if count == 0:
        return []
    
    positions = []
    start = 0
    for _ in range(count):  # Know exactly how many
        pos = tup.index(value, start)
        positions.append(pos)
        start = pos + 1
    
    return positions
```

---

### Practical Applications

**1. Voting System:**
```python
votes = ('Alice', 'Bob', 'Alice', 'Charlie', 'Alice')

# Count votes
alice_votes = votes.count('Alice')  # 3

# Find winner
candidates = set(votes)
winner = max(candidates, key=lambda c: votes.count(c))
```

**2. Data Validation:**
```python
fields = ('name', 'email', 'name', 'age')

# Check duplicates
has_dup = any(fields.count(f) > 1 for f in fields)

# Find duplicate positions
if fields.count('name') > 1:
    positions = find_all(fields, 'name')
```

**3. Frequency Analysis:**
```python
data = (5, 10, 5, 15, 5, 20)

# Get unique values
unique = []
for item in data:
    if item not in unique:
        unique.append(item)

# Count each
for item in unique:
    count = data.count(item)
    first_pos = data.index(item)
    print(f"{item}: {count} times, first at {first_pos}")
```

---

### Common Pitfalls

**1. index() Raises Error:**
```python
# Wrong
pos = data.index(100)  # May crash!

# Right
try:
    pos = data.index(100)
except ValueError:
    pos = -1
```

**2. Only Finds First:**
```python
numbers = (10, 20, 10)

# This is NOT [0, 2]
pos = numbers.index(10)  # Just 0

# Need loop for all
all_pos = find_all(numbers, 10)  # [0, 2]
```

**3. Performance:**
```python
# Inefficient - counts every time
for item in big_tuple:
    if big_tuple.count(item) > 1:  # O(n) each time!
        print("Duplicate")

# Better - count once
counted = {}
for item in big_tuple:
    if item not in counted:
        counted[item] = big_tuple.count(item)
```

---

### Quick Reference

**count(value):**
```python
tup.count(value)          # Returns integer
tup.count(missing_value)  # Returns 0 (safe)
```

**index(value):**
```python
tup.index(value)              # First occurrence
tup.index(value, start)       # Start from index
tup.index(value, start, end)  # Search range
# Raises ValueError if not found
```

**Best Practices:**
1. Use count() to check existence before index()
2. Always handle ValueError with index()
3. Use loop with start parameter to find all
4. For complex searches, use enumerate()

**Comparison:**

| Feature | count() | index() |
|---------|---------|---------|
| Returns | Integer | Integer |
| Not found | 0 | ValueError |
| Safe | Yes | No |
| Finds | All | First |
| Parameters | 1 | 1-3 |

---

### Key Takeaways

1. **Only 2 methods** - count() and index()
2. **count()** - Safe, returns 0 if not found
3. **index()** - Unsafe, raises ValueError
4. **First occurrence** - index() finds only first
5. **Use together** - count() to verify, index() to find

**Master these two methods and you master tuple searching!**
