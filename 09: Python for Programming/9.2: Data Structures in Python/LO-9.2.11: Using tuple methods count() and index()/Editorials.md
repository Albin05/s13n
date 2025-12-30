## Editorials: Using Tuple Methods count() and index()

---

### Q1 Solution: Basic count() and index() Usage

```python
# 1. Create tuple
numbers = (5, 10, 5, 15, 20, 5, 25)

# 2. Count 5s
count_5 = numbers.count(5)
print(f"Count of 5: {count_5}")

# 3. Find first occurrence of 10
index_10 = numbers.index(10)
print(f"First occurrence of 10 at index: {index_10}")

# 4. Find second occurrence of 5
first_5 = numbers.index(5)  # First at 0
second_5 = numbers.index(5, first_5 + 1)  # Search after first
print(f"Second occurrence of 5 at index: {second_5}")

# 5. Try to find 30 with error handling
try:
    index_30 = numbers.index(30)
    print(f"30 found at index: {index_30}")
except ValueError:
    print("30 not found in tuple")
```

**Key Concepts:**
- count() returns number of occurrences
- index() finds first occurrence
- Use index(value, start) to find next occurrence
- index() raises ValueError if not found - use try-except

---

### Q2 Solution: Safe Index Finding

```python
def safe_index(tup, value):
    """Returns index of value or -1 if not found"""
    if tup.count(value) > 0:
        return tup.index(value)
    else:
        return -1

# Test
colors = ('red', 'blue', 'green', 'yellow')
print(safe_index(colors, 'blue'))    # 1
print(safe_index(colors, 'purple'))  # -1
```

**Explanation:**
- Check count() first - returns 0 if not found
- Only call index() if count > 0
- Return -1 as "not found" indicator
- No exceptions raised - safe for all cases

---

### Q3 Solution: Find All Occurrences

```python
def find_all_indices(tup, value):
    """Find all indices where value appears"""
    indices = []
    start = 0
    
    while True:
        try:
            # Find next occurrence starting from 'start'
            index = tup.index(value, start)
            indices.append(index)
            start = index + 1  # Search after this one
        except ValueError:
            # No more occurrences found
            break
    
    return indices

# Test
data = (10, 20, 10, 30, 10, 40, 10)
print(find_all_indices(data, 10))  # [0, 2, 4, 6]
print(find_all_indices(data, 20))  # [1]
print(find_all_indices(data, 50))  # []
```

**Explanation:**
- Use while True loop with try-except
- index(value, start) searches from 'start' position
- After finding, update start to index + 1
- ValueError breaks loop when no more found
- Returns empty list if value never appears

---

### Q4 Solution: Voting System

```python
votes = ('Alice', 'Bob', 'Alice', 'Charlie', 'Alice', 'Bob', 'Alice')

def count_votes(votes):
    """Count votes for each candidate"""
    # Get unique candidates
    candidates = []
    for vote in votes:
        if vote not in candidates:
            candidates.append(vote)
    
    # Count votes for each
    results = {}
    for candidate in candidates:
        results[candidate] = votes.count(candidate)
    
    return results

def find_winner(votes):
    """Find candidate with most votes"""
    vote_counts = count_votes(votes)
    max_votes = max(vote_counts.values())
    
    for candidate, count in vote_counts.items():
        if count == max_votes:
            return candidate, count

def get_vote_positions(votes, candidate):
    """Get all positions where candidate received votes"""
    positions = []
    start = 0
    
    while True:
        try:
            pos = votes.index(candidate, start)
            positions.append(pos)
            start = pos + 1
        except ValueError:
            break
    
    return positions

# Execute
print(f"Vote counts: {count_votes(votes)}")

winner, count = find_winner(votes)
print(f"Winner: {winner} with {count} votes")

# Show positions
for candidate in ('Alice', 'Bob', 'Charlie'):
    positions = get_vote_positions(votes, candidate)
    print(f"{candidate} received votes at positions: {positions}")
```

**Key Points:**
- count() efficiently tallies votes
- max() finds highest vote count
- index() with loop tracks all vote positions
- Combining methods provides complete analysis

---

### Q5 Solution: Data Validation System

```python
def check_duplicates(fields):
    """Find duplicate fields"""
    duplicates = []
    checked = []
    
    for field in fields:
        if field not in checked:
            checked.append(field)
            if fields.count(field) > 1:
                duplicates.append(field)
    
    return duplicates

def check_required(provided, required):
    """Find missing required fields"""
    missing = []
    for field in required:
        if provided.count(field) == 0:
            missing.append(field)
    return missing

def get_duplicate_positions(fields):
    """Get positions of all duplicates"""
    duplicates = check_duplicates(fields)
    positions = {}
    
    for dup in duplicates:
        dup_positions = []
        start = 0
        while True:
            try:
                pos = fields.index(dup, start)
                dup_positions.append(pos)
                start = pos + 1
            except ValueError:
                break
        positions[dup] = dup_positions
    
    return positions

# Test
provided = ('name', 'email', 'name', 'age', 'email')
required = ('name', 'email', 'age', 'city')

# Check duplicates
dups = check_duplicates(provided)
print(f"Duplicates found: {dups}")

dup_positions = get_duplicate_positions(provided)
for field, positions in dup_positions.items():
    print(f"{field} appears at positions: {positions}")

# Check missing
missing = check_required(provided, required)
print(f"\nMissing required fields: {missing}")
```

**Validation Flow:**
1. Use count() to detect duplicates (count > 1)
2. Use count() to check required fields (count == 0 means missing)
3. Use index() loop to find all duplicate positions
4. Provides complete validation report

---

### Key Takeaways

**count() Method:**
- Never raises exceptions
- Returns 0 if not found
- O(n) complexity
- Use for: frequency, duplicates, existence check

**index() Method:**
- Raises ValueError if not found
- Returns only first occurrence
- Use with start parameter for subsequent occurrences
- O(n) complexity
- Use for: position finding, searching

**Best Patterns:**
```python
# Safe find
if tup.count(value) > 0:
    pos = tup.index(value)

# Find all
positions = []
start = 0
while True:
    try:
        pos = tup.index(value, start)
        positions.append(pos)
        start = pos + 1
    except ValueError:
        break
```

**Remember:** Tuples have only 2 methods - master them!
