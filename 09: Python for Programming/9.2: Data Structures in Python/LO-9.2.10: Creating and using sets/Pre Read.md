## Pre-Read: Creating and Using Sets

**Duration:** 5 minutes

---

### What You'll Learn

Sets are Python's way of working with unique collections—like mathematical sets. They're incredibly powerful for removing duplicates, finding common elements, and fast membership testing.

---

### The Uniqueness Problem

**Without sets:**
```python
# List with duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]

# Remove duplicates manually
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)  # [1, 2, 3, 4, 5]
# But checking "if num not in unique" is slow!
```

**With sets:**
```python
# Automatic duplicate removal
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = set(numbers)

print(unique)  # {1, 2, 3, 4, 5}
# Fast and simple!
```

---

### What Are Sets?

A **set** is an unordered collection of unique elements.

```python
# Create a set
fruits = {'apple', 'banana', 'orange'}

print(fruits)
# Output: {'apple', 'banana', 'orange'}
```

**Key Properties:**

1. **Unique elements only** - duplicates automatically removed
2. **Unordered** - no guaranteed order, no indexing
3. **Fast** - membership testing is lightning fast

---

### Creating Sets

**Two ways to create sets:**

```python
# Way 1: Curly braces
fruits = {'apple', 'banana', 'orange'}

# Way 2: set() constructor
numbers = set([1, 2, 3])
```

**Important: Empty sets!**
```python
# Wrong - this creates a dictionary!
empty = {}

# Right - use set()
empty = set()
```

**From other collections:**
```python
# From list (removes duplicates)
my_list = [1, 2, 2, 3]
my_set = set(my_list)
# {1, 2, 3}

# From string (splits into characters)
letters = set('hello')
# {'h', 'e', 'l', 'o'}  - only one 'l'
```

---

### Sets Automatically Remove Duplicates

**This is the magic of sets:**

```python
# Create set with duplicates
numbers = {1, 2, 2, 3, 3, 3, 4}

# Duplicates removed automatically
print(numbers)  # {1, 2, 3, 4}

# Try to add duplicate
numbers.add(2)
print(numbers)  # {1, 2, 3, 4} - no change!
```

---

### Set Operations

Sets support mathematical set operations:

**1. Union (|) - Combine sets**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

combined = set1 | set2
# {1, 2, 3, 4, 5} - all elements
```

**2. Intersection (&) - Common elements**
```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}

common = set1 & set2
# {2, 3} - elements in both
```

**3. Difference (-) - Elements in first, not second**
```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}

only_in_set1 = set1 - set2
# {1} - only in set1
```

---

### Real-World Example: Mutual Friends

```python
# Alice's friends
alice_friends = {'Bob', 'Charlie', 'Diana', 'Eve'}

# Bob's friends
bob_friends = {'Alice', 'Charlie', 'Frank', 'Diana'}

# Find mutual friends (intersection)
mutual = alice_friends & bob_friends
print(mutual)
# {'Charlie', 'Diana'}

# Friends only Alice has (difference)
only_alice = alice_friends - bob_friends
print(only_alice)
# {'Eve'}
```

Clean and simple!

---

### Fast Membership Testing

**This is a superpower of sets:**

```python
# Create set
valid_users = {'alice', 'bob', 'charlie'}

# Check membership - very fast!
if 'alice' in valid_users:
    print("Valid user!")

if 'eve' not in valid_users:
    print("Invalid user!")
```

**Why so fast?**
- List: O(n) - checks each element
- Set: O(1) - instant lookup using hash table

For large collections, this is **much** faster!

---

### Basic Operations

**Adding:**
```python
fruits = {'apple', 'banana'}
fruits.add('orange')
# {'apple', 'banana', 'orange'}
```

**Removing:**
```python
fruits = {'apple', 'banana', 'orange'}
fruits.remove('banana')
# {'apple', 'orange'}
```

---

### Try to Predict

```python
# Question 1
my_set = {1, 2, 3, 2, 1}
print(len(my_set))
# What's the length?

# Question 2
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 & set2
# What's in result?

# Question 3
empty = {}
print(type(empty))
# What's the type?
```

**Answers:**
1. `3` (duplicates removed: {1, 2, 3})
2. `{3}` (only common element)
3. `<class 'dict'>` (not a set!)

---

### When to Use Sets

**Use sets when you need:**
- ✓ Unique elements only
- ✓ Fast membership testing
- ✓ Set operations (find common, differences)
- ✓ Remove duplicates

**Don't use sets when you need:**
- ✗ Specific order (use list)
- ✗ Duplicates (use list)
- ✗ Indexing (use list/tuple)

---

### Common Patterns

**1. Remove duplicates:**
```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))
```

**2. Find common elements:**
```python
common = set1 & set2
```

**3. Check if subset:**
```python
if required_items.issubset(available_items):
    print("All items available!")
```

**4. Fast lookup:**
```python
valid_codes = {'ABC', 'DEF', 'GHI'}
if code in valid_codes:  # Instant!
    process()
```

---

### Quick Exercise

Before the lesson, try this:

```python
# Create two sets
skills_needed = {'Python', 'SQL', 'Git'}
skills_you_have = {'Python', 'JavaScript', 'Git'}

# Find common skills (intersection)
common = skills_needed & skills_you_have
print(f"You have: {common}")

# Find missing skills (difference)
missing = skills_needed - skills_you_have
print(f"You need to learn: {missing}")

# Find extra skills (what you have but not needed)
extra = skills_you_have - skills_needed
print(f"Bonus skills: {extra}")
```

Expected output:
```
You have: {'Python', 'Git'}
You need to learn: {'SQL'}
Bonus skills: {'JavaScript'}
```

---

### What Makes Sets Special?

**Automatic Uniqueness:**
- No need to check for duplicates
- Set handles it automatically

**Fast Operations:**
- Membership testing: O(1)
- Much faster than lists for lookups

**Mathematical Operations:**
- Union, intersection, difference
- Just like math class sets!

**Clean Code:**
```python
# Instead of:
common = []
for item in list1:
    if item in list2:
        common.append(item)

# Simply:
common = set1 & set2
```

---

### Get Ready!

In the lesson, you'll learn:
- Creating and manipulating sets
- All set operations in detail
- Adding and removing elements
- Membership testing and subsets
- Real-world applications
- When to use sets vs other data structures

**Sets are powerful tools for handling unique collections efficiently!**

**Think of sets whenever you hear:**
- "Remove duplicates"
- "Find common elements"
- "Check if exists" (for large collections)
- "Unique values"

**Master sets and your code becomes cleaner and faster!**
