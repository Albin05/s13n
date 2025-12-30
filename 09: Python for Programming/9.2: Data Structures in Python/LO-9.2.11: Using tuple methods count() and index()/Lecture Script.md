## Lecture Script: Using Tuple Methods count() and index()

**Duration:** 18 minutes

---

### Hook (2 minutes)

**Scenario:**

You have a list of student test scores stored in a tuple (because scores shouldn't be modified after entry):

```python
scores = (85, 92, 78, 92, 85, 88, 95, 78, 92)
```

**Questions you might ask:**
- How many students scored 92?
- At what position did the first 85 appear?
- Did anyone score 100?

**Without tuple methods** (tedious):
```python
# Count 92s manually
count = 0
for score in scores:
    if score == 92:
        count += 1
print(f"Students who scored 92: {count}")  # 3

# Find position of 85
position = None
for i, score in enumerate(scores):
    if score == 85:
        position = i
        break
print(f"First 85 at position: {position}")  # 0
```

**With tuple methods** (clean):
```python
# Count 92s
print(f"Students who scored 92: {scores.count(92)}")  # 3

# Find position of 85
print(f"First 85 at position: {scores.index(85)}")  # 0
```

**Today's Focus:**

Master the two tuple methods that make searching and counting in tuples simple and efficient: `count()` and `index()`.

---

### Section 1: The count() Method (4 minutes)

**What does count() do?**

Returns the number of times a value appears in the tuple.

```python
numbers = (1, 2, 3, 2, 4, 2, 5)

# Count how many 2s
result = numbers.count(2)
print(result)  # 3
```

**Syntax:**
```python
tuple.count(value)
```

- **value**: The element to count
- **Returns**: Integer (number of occurrences)

**Examples:**

**1. Basic Counting:**
```python
fruits = ('apple', 'banana', 'apple', 'orange', 'apple')

apple_count = fruits.count('apple')
print(f"Apples: {apple_count}")  # 3

banana_count = fruits.count('banana')
print(f"Bananas: {banana_count}")  # 1

grape_count = fruits.count('grape')
print(f"Grapes: {grape_count}")  # 0 (not found)
```

**Key Point:** Returns 0 if element not found (no error!)

**2. Counting with Numbers:**
```python
scores = (85, 90, 85, 95, 85, 90, 85)

# How many 85s?
count_85 = scores.count(85)
print(f"Students who scored 85: {count_85}")  # 4

# How many 100s?
count_100 = scores.count(100)
print(f"Students who scored 100: {count_100}")  # 0
```

**3. Finding Most Common Element:**
```python
votes = ('Alice', 'Bob', 'Alice', 'Charlie', 'Alice', 'Bob', 'Alice')

alice_votes = votes.count('Alice')
bob_votes = votes.count('Bob')
charlie_votes = votes.count('Charlie')

print(f"Alice: {alice_votes}")    # 4
print(f"Bob: {bob_votes}")        # 2
print(f"Charlie: {charlie_votes}") # 1

# Find winner
candidates = ('Alice', 'Bob', 'Charlie')
max_votes = 0
winner = None

for candidate in candidates:
    votes_count = votes.count(candidate)
    if votes_count > max_votes:
        max_votes = votes_count
        winner = candidate

print(f"Winner: {winner} with {max_votes} votes")
# Winner: Alice with 4 votes
```

**4. Checking for Duplicates:**
```python
data = (1, 2, 3, 4, 5)

# Check if any element appears more than once
has_duplicates = False
for item in data:
    if data.count(item) > 1:
        has_duplicates = True
        break

print(f"Has duplicates: {has_duplicates}")  # False

# With duplicates
data2 = (1, 2, 3, 2, 4)
has_duplicates2 = any(data2.count(item) > 1 for item in data2)
print(f"Has duplicates: {has_duplicates2}")  # True
```

**Performance Note:**
- `count()` is O(n) - checks every element
- For large tuples with frequent counting, consider converting to Counter from collections module

---

### Section 2: The index() Method (4 minutes)

**What does index() do?**

Returns the index (position) of the first occurrence of a value.

```python
colors = ('red', 'blue', 'green', 'blue', 'yellow')

# Find position of 'blue'
position = colors.index('blue')
print(position)  # 1 (first occurrence)
```

**Syntax:**
```python
tuple.index(value)
tuple.index(value, start)
tuple.index(value, start, end)
```

- **value**: Element to find
- **start** (optional): Start searching from this index
- **end** (optional): Stop searching at this index
- **Returns**: Integer (index of first occurrence)
- **Raises**: ValueError if not found!

**Examples:**

**1. Basic Finding:**
```python
fruits = ('apple', 'banana', 'orange', 'grape')

# Find banana
banana_pos = fruits.index('banana')
print(f"Banana at index: {banana_pos}")  # 1

# Find orange
orange_pos = fruits.index('orange')
print(f"Orange at index: {orange_pos}")  # 2
```

**2. Finding with Error Handling:**
```python
fruits = ('apple', 'banana', 'orange')

# Element exists
try:
    pos = fruits.index('banana')
    print(f"Found at index: {pos}")  # 1
except ValueError:
    print("Not found")

# Element doesn't exist
try:
    pos = fruits.index('grape')
    print(f"Found at index: {pos}")
except ValueError:
    print("Not found")  # This executes
```

**Better Pattern:**
```python
def find_index(tup, value):
    """Safely find index or return -1 if not found"""
    try:
        return tup.index(value)
    except ValueError:
        return -1

fruits = ('apple', 'banana', 'orange')
print(find_index(fruits, 'banana'))  # 1
print(find_index(fruits, 'grape'))   # -1
```

**3. Finding from Start Position:**
```python
numbers = (10, 20, 30, 20, 40, 20, 50)

# Find first 20
first_20 = numbers.index(20)
print(f"First 20 at: {first_20}")  # 1

# Find next 20 (start searching after first)
second_20 = numbers.index(20, first_20 + 1)
print(f"Second 20 at: {second_20}")  # 3

# Find third 20
third_20 = numbers.index(20, second_20 + 1)
print(f"Third 20 at: {third_20}")  # 5
```

**4. Finding All Occurrences:**
```python
def find_all_indices(tup, value):
    """Find all indices where value appears"""
    indices = []
    start = 0
    
    while True:
        try:
            index = tup.index(value, start)
            indices.append(index)
            start = index + 1
        except ValueError:
            break
    
    return indices

numbers = (10, 20, 30, 20, 40, 20, 50)
all_20s = find_all_indices(numbers, 20)
print(f"All positions of 20: {all_20s}")
# All positions of 20: [1, 3, 5]

# Nothing found
all_100s = find_all_indices(numbers, 100)
print(f"All positions of 100: {all_100s}")
# All positions of 100: []
```

**5. Using start and end Parameters:**
```python
data = (1, 2, 3, 4, 5, 3, 6, 7, 3, 8)

# Find 3 in entire tuple
pos = data.index(3)
print(f"First 3 at: {pos}")  # 2

# Find 3 starting from index 5
pos = data.index(3, 5)
print(f"3 after index 5 at: {pos}")  # 5

# Find 3 between indices 6 and 9
pos = data.index(3, 6, 9)
print(f"3 between 6-9 at: {pos}")  # 8

# Not in range - raises ValueError
try:
    pos = data.index(3, 0, 2)  # Search only [0, 1]
except ValueError:
    print("Not found in range [0, 2]")
```

---

### Section 3: Combining count() and index() (3 minutes)

**Pattern 1: Verify Before Finding**

```python
def safe_find(tup, value):
    """Find value only if it exists"""
    if tup.count(value) > 0:
        return tup.index(value)
    else:
        return None

data = (10, 20, 30, 40)
print(safe_find(data, 20))   # 1
print(safe_find(data, 50))   # None
```

**Pattern 2: Find All Positions Efficiently**

```python
def find_all_with_count(tup, value):
    """Find all positions knowing count first"""
    count = tup.count(value)
    if count == 0:
        return []
    
    positions = []
    start = 0
    for _ in range(count):
        pos = tup.index(value, start)
        positions.append(pos)
        start = pos + 1
    
    return positions

numbers = (5, 10, 5, 15, 5, 20)
fives = find_all_with_count(numbers, 5)
print(f"All 5s at positions: {fives}")
# All 5s at positions: [0, 2, 4]
```

**Pattern 3: Frequency Analysis**

```python
def analyze_tuple(tup):
    """Analyze element frequencies and positions"""
    # Get unique elements
    unique = []
    for item in tup:
        if item not in unique:
            unique.append(item)
    
    # Analyze each
    for item in unique:
        count = tup.count(item)
        first_pos = tup.index(item)
        print(f"{item}: appears {count} time(s), first at index {first_pos}")

scores = (85, 92, 78, 92, 85, 88)
analyze_tuple(scores)
# 85: appears 2 time(s), first at index 0
# 92: appears 2 time(s), first at index 1
# 78: appears 1 time(s), first at index 2
# 88: appears 1 time(s), first at index 5
```

---

### Section 4: Practical Applications (3 minutes)

**Application 1: Voting System**

```python
votes = ('Alice', 'Bob', 'Alice', 'Charlie', 'Alice', 'Bob')

def count_votes(votes_tuple):
    """Count votes for each candidate"""
    candidates = []
    for vote in votes_tuple:
        if vote not in candidates:
            candidates.append(vote)
    
    results = {}
    for candidate in candidates:
        results[candidate] = votes_tuple.count(candidate)
    
    return results

results = count_votes(votes)
for candidate, count in results.items():
    print(f"{candidate}: {count} votes")
# Alice: 3 votes
# Bob: 2 votes
# Charlie: 1 votes
```

**Application 2: Data Validation**

```python
required_fields = ('name', 'email', 'age', 'city')
provided_fields = ('name', 'email', 'name', 'age')  # Duplicate!

# Check for duplicates
def has_duplicates(tup):
    for item in tup:
        if tup.count(item) > 1:
            return True, item
    return False, None

is_duplicate, field = has_duplicates(provided_fields)
if is_duplicate:
    print(f"Error: Duplicate field '{field}'")
    # Error: Duplicate field 'name'

# Check all required fields present
def check_required(provided, required):
    missing = []
    for field in required:
        if provided.count(field) == 0:
            missing.append(field)
    return missing

missing = check_required(provided_fields, required_fields)
if missing:
    print(f"Missing fields: {missing}")
    # Missing fields: ['city']
```

**Application 3: Finding Patterns**

```python
sequence = (1, 2, 3, 2, 1, 2, 3, 4, 2)

# Find all positions of a specific pattern element
def find_pattern_positions(seq, value):
    """Find all positions and analyze spacing"""
    positions = []
    count = seq.count(value)
    start = 0
    
    for _ in range(count):
        pos = seq.index(value, start)
        positions.append(pos)
        start = pos + 1
    
    # Calculate spacing
    if len(positions) > 1:
        spacings = []
        for i in range(len(positions) - 1):
            spacing = positions[i + 1] - positions[i]
            spacings.append(spacing)
        return positions, spacings
    
    return positions, []

positions, spacings = find_pattern_positions(sequence, 2)
print(f"Value 2 appears at positions: {positions}")
print(f"Spacing between occurrences: {spacings}")
# Value 2 appears at positions: [1, 3, 5, 8]
# Spacing between occurrences: [2, 2, 3]
```

**Application 4: Data Quality Check**

```python
expected_format = ('header', 'data', 'data', 'data', 'footer')
actual_data = ('header', 'data', 'data', 'footer')  # Missing one data

# Verify format
def verify_structure(actual, expected):
    """Check if structure matches expected format"""
    issues = []
    
    # Check each expected element
    for element in set(expected):  # Unique elements
        expected_count = expected.count(element)
        actual_count = actual.count(element)
        
        if actual_count != expected_count:
            issues.append(
                f"{element}: expected {expected_count}, got {actual_count}"
            )
    
    return issues

issues = verify_structure(actual_data, expected_format)
if issues:
    print("Structure issues:")
    for issue in issues:
        print(f"  - {issue}")
    # Structure issues:
    #   - data: expected 3, got 2
```

---

### Section 5: Common Pitfalls and Best Practices (1 minute)

**Pitfall 1: index() Raises ValueError**

```python
# Wrong - will crash
data = (1, 2, 3)
# pos = data.index(4)  # ValueError!

# Right - handle error
try:
    pos = data.index(4)
except ValueError:
    pos = -1
    print("Not found")
```

**Pitfall 2: index() Only Finds First**

```python
numbers = (10, 20, 10, 30)

# This only finds first 10
pos = numbers.index(10)  # Returns 0, not [0, 2]

# To find all, use custom function
def find_all(tup, value):
    return [i for i, v in enumerate(tup) if v == value]

all_tens = find_all(numbers, 10)
print(all_tens)  # [0, 2]
```

**Best Practice 1: Check Before Finding**

```python
# Safe approach
if data.count(value) > 0:
    pos = data.index(value)
else:
    pos = None
```

**Best Practice 2: Use enumerate() for Complex Searches**

```python
# For complex conditions, enumerate is better
numbers = (10, 20, 30, 40, 50)

# Find first number > 25
position = None
for i, num in enumerate(numbers):
    if num > 25:
        position = i
        break

print(f"First number > 25 at index: {position}")  # 2
```

---

### Summary (1 minute)

**Two Tuple Methods:**

**1. count(value)**
- Counts occurrences of value
- Returns integer (0 if not found)
- Never raises error
- O(n) time complexity

```python
scores = (85, 92, 85, 78)
count = scores.count(85)  # 2
```

**2. index(value, start, end)**
- Finds first occurrence position
- Returns integer index
- Raises ValueError if not found
- Optional start/end parameters
- O(n) time complexity

```python
colors = ('red', 'blue', 'green')
pos = colors.index('blue')  # 1
```

**Key Takeaways:**

1. **count()** - Safe, never errors, returns 0 if not found
2. **index()** - Fast for first occurrence, but raises ValueError
3. **Always handle ValueError** with index() or check with count() first
4. **For all occurrences** - use custom function with loop
5. **For complex searches** - consider enumerate() instead

**Common Patterns:**

```python
# Safe find
if tup.count(value) > 0:
    pos = tup.index(value)

# Find all
positions = [i for i, v in enumerate(tup) if v == value]

# Try-except
try:
    pos = tup.index(value)
except ValueError:
    pos = -1
```

**When to Use:**
- count(): Frequency analysis, duplicate checking
- index(): Finding position, validation, searching

**Remember:** Tuples have only 2 methods - keep it simple!
