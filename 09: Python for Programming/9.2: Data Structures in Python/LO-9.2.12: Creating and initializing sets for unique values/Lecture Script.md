## Lecture Script: Creating and Initializing Sets for Unique Values

**Duration:** 18 minutes

---

### Hook (2 minutes)

**Scenario:**

You're analyzing customer IDs from multiple data sources. The data has duplicates:

```python
source1_customers = [101, 102, 103, 104, 105]
source2_customers = [103, 104, 106, 107, 108]
source3_customers = [102, 105, 108, 109, 110]

# Combine all - has duplicates!
all_customers = source1_customers + source2_customers + source3_customers
print(len(all_customers))  # 15 entries
# But how many unique customers?
```

**Without sets** (tedious):
```python
unique = []
for customer in all_customers:
    if customer not in unique:
        unique.append(customer)
print(len(unique))  # 10 unique customers
```

**With sets** (instant):
```python
unique_customers = set(all_customers)
print(len(unique_customers))  # 10 unique customers
# Automatic deduplication!
```

**Today's Focus:**

Learn how to create and initialize sets—Python's built-in data structure for storing unique values efficiently.

---

### Section 1: What Are Sets? (3 minutes)

**Definition:**

A set is an **unordered collection of unique elements**.

**Key Properties:**
1. **Unique only** - No duplicates allowed
2. **Unordered** - No guaranteed order
3. **Mutable** - Can add/remove items
4. **Elements must be immutable** - Hashable types only

**Basic Creation:**
```python
# Using curly braces
fruits = {'apple', 'banana', 'orange'}
print(fruits)
# Output: {'apple', 'banana', 'orange'} (order may vary)
```

**Automatic Deduplication:**
```python
numbers = {1, 2, 3, 2, 1, 4, 3, 5}
print(numbers)
# Output: {1, 2, 3, 4, 5} - duplicates removed!
```

**Why Sets?**
- Fast membership testing: O(1)
- Automatic uniqueness
- Mathematical set operations
- Memory efficient for unique data

---

### Section 2: Creating Sets with Curly Braces (3 minutes)

**Method 1: Literal Syntax**

```python
# Basic set
colors = {'red', 'blue', 'green'}

# Numbers
primes = {2, 3, 5, 7, 11}

# Mixed types (avoid in practice)
mixed = {1, 'hello', 3.14, True}

# Duplicates ignored
data = {1, 2, 2, 3, 3, 3}
print(data)  # {1, 2, 3}
```

**Important: Empty Set**

```python
# WRONG - This creates a dictionary!
empty_wrong = {}
print(type(empty_wrong))  # <class 'dict'>

# RIGHT - Use set() constructor
empty_right = set()
print(type(empty_right))  # <class 'set'>
```

**Single Element:**
```python
# Works fine (unlike tuples, no comma needed)
single = {5}
print(type(single))  # <class 'set'>
print(single)  # {5}
```

---

### Section 3: Creating Sets with set() Constructor (4 minutes)

**From Lists:**
```python
# List with duplicates
numbers_list = [1, 2, 3, 2, 1, 4, 3, 5]

# Convert to set - removes duplicates
numbers_set = set(numbers_list)
print(numbers_set)  # {1, 2, 3, 4, 5}
```

**From Strings:**
```python
# String to set of characters
text = "hello"
chars = set(text)
print(chars)  # {'h', 'e', 'l', 'o'} - duplicate 'l' removed
```

**From Tuples:**
```python
# Tuple to set
coordinates = (10, 20, 30, 20, 10)
unique_coords = set(coordinates)
print(unique_coords)  # {10, 20, 30}
```

**From Range:**
```python
# Create set from range
numbers = set(range(5))
print(numbers)  # {0, 1, 2, 3, 4}

# Even numbers 0-10
evens = set(range(0, 11, 2))
print(evens)  # {0, 2, 4, 6, 8, 10}
```

**From Dictionary Keys:**
```python
scores = {'Alice': 95, 'Bob': 88, 'Charlie': 92}

# Get unique keys as set
students = set(scores.keys())
print(students)  # {'Alice', 'Bob', 'Charlie'}
```

**Empty Set:**
```python
# Must use set(), not {}
empty = set()
print(empty)  # set()
print(type(empty))  # <class 'set'>
```

---

### Section 4: Sets for Removing Duplicates (3 minutes)

**Pattern: Remove Duplicates from List**

```python
# Original list with duplicates
scores = [85, 92, 78, 92, 85, 88, 95, 78, 92]

# Remove duplicates
unique_scores = list(set(scores))
print(unique_scores)  # [78, 85, 88, 92, 95] (order may vary)

# Sorted unique values
sorted_unique = sorted(set(scores))
print(sorted_unique)  # [78, 85, 88, 92, 95]
```

**Preserving Order (Python 3.7+):**
```python
def remove_duplicates_preserve_order(lst):
    """Remove duplicates while preserving order"""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

data = [1, 2, 3, 2, 1, 4, 3, 5]
unique = remove_duplicates_preserve_order(data)
print(unique)  # [1, 2, 3, 4, 5] (order preserved)
```

**Finding Unique Words:**
```python
text = "the quick brown fox jumps over the lazy dog the fox"
words = text.split()

unique_words = set(words)
print(f"Total words: {len(words)}")  # 12
print(f"Unique words: {len(unique_words)}")  # 8
print(f"Words: {sorted(unique_words)}")
# ['brown', 'dog', 'fox', 'jumps', 'lazy', 'over', 'quick', 'the']
```

---

### Section 5: Element Type Restrictions (2 minutes)

**Hashable Types Only:**

```python
# Works - immutable types
valid_set = {1, 2.5, 'hello', (1, 2), True}

# Fails - mutable types
# invalid_set = {[1, 2], [3, 4]}  # TypeError: unhashable type: 'list'
# invalid_set = {{1, 2}}  # TypeError: unhashable type: 'set'
# invalid_set = {{'a': 1}}  # TypeError: unhashable type: 'dict'
```

**Use Tuples Instead of Lists:**
```python
# Wrong - lists in set
# points = {[0, 0], [1, 1], [2, 2]}  # Error!

# Right - tuples in set
points = {(0, 0), (1, 1), (2, 2)}
print(points)  # {(0, 0), (1, 1), (2, 2)}
```

**Nested Tuples Work:**
```python
# Complex immutable structures
data = {
    (1, 2, 3),
    (4, (5, 6)),
    ('a', 'b', ('c', 'd'))
}
print(data)  # Works!
```

---

### Section 6: Practical Applications (3 minutes)

**Application 1: Unique Visitor Tracking**

```python
# Visitor IDs throughout the day
morning_visitors = [101, 102, 103, 102, 104]
afternoon_visitors = [103, 105, 106, 102]
evening_visitors = [104, 107, 103, 108]

# Combine all visits
all_visits = morning_visitors + afternoon_visitors + evening_visitors
print(f"Total visits: {len(all_visits)}")  # 13

# Unique visitors
unique_visitors = set(all_visits)
print(f"Unique visitors: {len(unique_visitors)}")  # 8

# Who visited?
print(f"Visitors: {sorted(unique_visitors)}")
# [101, 102, 103, 104, 105, 106, 107, 108]
```

**Application 2: Email Validation**

```python
# Email list with potential duplicates
emails = [
    'alice@example.com',
    'bob@example.com',
    'alice@example.com',  # duplicate
    'charlie@example.com',
    'bob@example.com'  # duplicate
]

# Get unique emails
unique_emails = set(emails)
print(f"Total submissions: {len(emails)}")  # 5
print(f"Unique emails: {len(unique_emails)}")  # 3

# Find duplicates
if len(emails) != len(unique_emails):
    print(f"Found {len(emails) - len(unique_emails)} duplicate(s)")
```

**Application 3: Tag Management**

```python
# Tags from different articles
article1_tags = {'python', 'programming', 'tutorial'}
article2_tags = {'python', 'web', 'django'}
article3_tags = {'javascript', 'web', 'frontend'}

# All unique tags across articles
all_tags = set()
all_tags.update(article1_tags)
all_tags.update(article2_tags)
all_tags.update(article3_tags)

# Or using union (covered later)
# all_tags = article1_tags | article2_tags | article3_tags

print(f"All tags: {sorted(all_tags)}")
# ['django', 'frontend', 'javascript', 'programming', 'python', 'tutorial', 'web']
```

---

### Common Pitfalls (1 minute)

**Pitfall 1: Empty Set**
```python
# Wrong
empty = {}  # This is a dict!

# Right
empty = set()
```

**Pitfall 2: Order Not Guaranteed**
```python
numbers = {5, 1, 3, 2, 4}
# Don't assume order!
# May print: {1, 2, 3, 4, 5} or different order
```

**Pitfall 3: Mutable Elements**
```python
# Wrong
# my_set = {[1, 2], [3, 4]}  # Error!

# Right
my_set = {(1, 2), (3, 4)}
```

**Pitfall 4: No Indexing**
```python
fruits = {'apple', 'banana', 'orange'}
# fruits[0]  # TypeError: 'set' object is not subscriptable
```

---

### Summary (1 minute)

**Creating Sets:**

1. **Curly braces:** `{1, 2, 3}`
2. **set() constructor:** `set([1, 2, 3])`
3. **Empty set:** `set()` (not `{}`)

**Key Features:**
- Automatic deduplication
- Unordered collection
- Elements must be immutable
- Fast membership testing

**Common Uses:**
- Remove duplicates
- Unique value tracking
- Tag management
- Data validation

**Remember:**
```python
# Create
my_set = {1, 2, 3}
my_set = set([1, 2, 3])

# Empty
empty = set()  # Not {}

# Remove duplicates
unique = set(my_list)

# Elements must be hashable
valid = {1, 'hello', (1, 2)}
# invalid = {[1, 2]}  # Error!
```

**Master set creation for efficient unique value handling!**
