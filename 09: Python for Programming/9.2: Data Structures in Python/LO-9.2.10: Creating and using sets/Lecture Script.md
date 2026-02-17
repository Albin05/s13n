## Lecture Script: Creating and Using Sets


---

### CS Theory Bite

> **Origin**: Sets implement **mathematical set theory** (Georg Cantor, 1874). Python sets use **hash tables** for O(1) membership testing — checking `x in my_set` is near-instant regardless of size.
>
> **Analogy**: A set is like a **guest list with no duplicates** — each name appears exactly once, and checking if someone's on the list is instant.
>
> **Why it matters**: Sets eliminate duplicates automatically and provide the fastest membership testing of any Python collection.



### Hook (2 minutes)

**Scenario:**

You're building a social media app and need to find mutual friends between two users:

```python
# Traditional approach with lists
alice_friends = ['Bob', 'Charlie', 'Diana', 'Eve']
bob_friends = ['Alice', 'Charlie', 'Frank', 'Diana']

# Find mutual friends (inefficient)
mutual = []
for friend in alice_friends:
    if friend in bob_friends:
        mutual.append(friend)

print(mutual)  # ['Charlie', 'Diana']
```

**The Problem:** This is slow! For large friend lists, checking `if friend in bob_friends` is O(n) for each friend.

**The Solution: Sets!**

```python
# Convert to sets
alice_friends = {'Bob', 'Charlie', 'Diana', 'Eve'}
bob_friends = {'Alice', 'Charlie', 'Frank', 'Diana'}

# Find mutual friends (efficient)
mutual = alice_friends & bob_friends  # Intersection

print(mutual)  # {'Charlie', 'Diana'}
```

**The Magic:**
- Set intersection is O(min(len(s1), len(s2)))
- Much faster for large collections
- One line instead of a loop!

**Real-World Impact:**

Sets power:
- Database query optimization
- Duplicate removal
- Tag systems
- Permission checking
- Graph algorithms

**Today's Journey:**

Learn how sets—Python's implementation of mathematical sets—make your code faster and more elegant when working with unique collections.

---

### Section 1: What Are Sets? (3 minutes)

**Definition:**

A **set** is an unordered collection of unique elements. Think of it like a mathematical set.

```python
# Create a set
fruits = {'apple', 'banana', 'orange'}

print(fruits)  # {'apple', 'banana', 'orange'}
print(type(fruits))  # <class 'set'>
```

**Key Properties:**

**1. Unique Elements Only:**
```python
# Duplicates automatically removed
numbers = {1, 2, 2, 3, 3, 3, 4}
print(numbers)  # {1, 2, 3, 4}

# Same element, only stored once
colors = {'red', 'blue', 'red', 'green'}
print(colors)  # {'red', 'blue', 'green'}
```

**2. Unordered:**
```python
# No guaranteed order
my_set = {5, 1, 3, 2, 4}
print(my_set)  # Might print: {1, 2, 3, 4, 5} or different order!

# Cannot access by index
# my_set[0]  # TypeError: 'set' object is not subscriptable
```

**3. Mutable (but elements must be immutable):**
```python
# Can add/remove from set
numbers = {1, 2, 3}
numbers.add(4)  # ✓ Can modify

# But elements must be immutable
# bad_set = {[1, 2], [3, 4]}  # TypeError: unhashable type: 'list'

# This works
good_set = {(1, 2), (3, 4)}  # ✓ Tuples are immutable
```

**Why Use Sets?**

1. **Fast membership testing:** O(1) instead of O(n)
2. **Automatic duplicate removal**
3. **Mathematical set operations**
4. **Memory efficient for unique items**

---

### Section 2: Creating Sets (2 minutes)

**Method 1: Curly Braces (Literal)**

```python
# Basic creation
fruits = {'apple', 'banana', 'orange'}

# Mixed types (but usually avoid)
mixed = {1, 'hello', 3.14, True}

# Empty set? NO!
# empty = {}  # This creates a dict, not a set!
```

**Method 2: set() Constructor**

```python
# From list
numbers_list = [1, 2, 3, 2, 1]
numbers_set = set(numbers_list)
print(numbers_set)  # {1, 2, 3} - duplicates removed

# From string (splits into characters)
letters = set('hello')
print(letters)  # {'h', 'e', 'l', 'o'} - duplicate 'l' removed

# From tuple
tuple_data = (1, 2, 3, 2)
set_data = set(tuple_data)
print(set_data)  # {1, 2, 3}

# Empty set
empty = set()  # Must use set(), not {}
print(type(empty))  # <class 'set'>
```

**Important: Empty Set**

```python
# Wrong - creates dictionary!
empty_wrong = {}
print(type(empty_wrong))  # <class 'dict'>

# Right - creates set
empty_right = set()
print(type(empty_right))  # <class 'set'>
```

**From Range:**
```python
# Create set from range
nums = set(range(5))
print(nums)  # {0, 1, 2, 3, 4}
```

---

### Section 3: Adding and Removing Elements (2 minutes)

**Adding Elements:**

```python
fruits = {'apple', 'banana'}

# Add single element
fruits.add('orange')
print(fruits)  # {'apple', 'banana', 'orange'}

# Adding duplicate has no effect
fruits.add('apple')
print(fruits)  # {'apple', 'banana', 'orange'} - no change!

# Add multiple elements
fruits.update(['mango', 'grape'])
print(fruits)  # {'apple', 'banana', 'orange', 'mango', 'grape'}

# update() with any iterable
fruits.update('kiwi')  # Adds each character as element!
print(fruits)  # {..., 'k', 'i', 'w'} - probably not what you want
```

**Removing Elements:**

**Method 1: remove() - Raises error if not found**
```python
numbers = {1, 2, 3, 4, 5}

numbers.remove(3)
print(numbers)  # {1, 2, 4, 5}

# Error if element doesn't exist
# numbers.remove(10)  # KeyError: 10
```

**Method 2: discard() - Safe removal**
```python
numbers = {1, 2, 3, 4, 5}

numbers.discard(3)
print(numbers)  # {1, 2, 4, 5}

# No error if element doesn't exist
numbers.discard(10)  # No error, just does nothing
print(numbers)  # {1, 2, 4, 5}
```

**Method 3: pop() - Remove arbitrary element**
```python
numbers = {1, 2, 3, 4, 5}

removed = numbers.pop()  # Removes and returns arbitrary element
print(f"Removed: {removed}")
print(numbers)

# Error on empty set
# empty = set()
# empty.pop()  # KeyError: 'pop from an empty set'
```

**Method 4: clear() - Remove all**
```python
numbers = {1, 2, 3}
numbers.clear()
print(numbers)  # set()
```

---

### Section 4: Set Operations - Union and Intersection (3 minutes)

**Union (Combine Sets):**

Combine all elements from both sets (no duplicates).

**Operator: `|` or method: `.union()`**

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using operator
result = set1 | set2
print(result)  # {1, 2, 3, 4, 5}

# Using method
result = set1.union(set2)
print(result)  # {1, 2, 3, 4, 5}

# Original sets unchanged
print(set1)  # {1, 2, 3}
print(set2)  # {3, 4, 5}
```

**Multiple Sets:**
```python
s1 = {1, 2}
s2 = {2, 3}
s3 = {3, 4}

result = s1 | s2 | s3
print(result)  # {1, 2, 3, 4}

# Or with method
result = s1.union(s2, s3)
print(result)  # {1, 2, 3, 4}
```

**Intersection (Common Elements):**

Get only elements present in both sets.

**Operator: `&` or method: `.intersection()`**

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using operator
result = set1 & set2
print(result)  # {3, 4}

# Using method
result = set1.intersection(set2)
print(result)  # {3, 4}
```

**Real-World Example:**
```python
# Find mutual interests
alice_hobbies = {'reading', 'gaming', 'cooking', 'hiking'}
bob_hobbies = {'gaming', 'hiking', 'photography', 'music'}

mutual = alice_hobbies & bob_hobbies
print(f"Mutual hobbies: {mutual}")
# Mutual hobbies: {'gaming', 'hiking'}
```

**Multiple Sets:**
```python
s1 = {1, 2, 3, 4}
s2 = {2, 3, 4, 5}
s3 = {3, 4, 5, 6}

# Elements in ALL sets
result = s1 & s2 & s3
print(result)  # {3, 4}
```

---

### Section 5: Set Operations - Difference and Symmetric Difference (3 minutes)

**Difference (Elements in First, Not in Second):**

**Operator: `-` or method: `.difference()`**

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Elements in set1 but not in set2
result = set1 - set2
print(result)  # {1, 2}

# Using method
result = set1.difference(set2)
print(result)  # {1, 2}

# Order matters!
result = set2 - set1
print(result)  # {5, 6}
```

**Real-World Example:**
```python
# Find unique skills
my_skills = {'Python', 'JavaScript', 'SQL', 'Git'}
required_skills = {'Python', 'SQL', 'Docker', 'Kubernetes'}

# Skills I have but not required
extra = my_skills - required_skills
print(f"Extra skills: {extra}")
# Extra skills: {'JavaScript', 'Git'}

# Skills required but I don't have
missing = required_skills - my_skills
print(f"Missing skills: {missing}")
# Missing skills: {'Docker', 'Kubernetes'}
```

**Symmetric Difference (Elements in Either, Not Both):**

Elements that are in one set or the other, but not in both.

**Operator: `^` or method: `.symmetric_difference()`**

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using operator
result = set1 ^ set2
print(result)  # {1, 2, 5, 6}

# Using method
result = set1.symmetric_difference(set2)
print(result)  # {1, 2, 5, 6}
```

**Think of it as:** (set1 - set2) | (set2 - set1)

**Real-World Example:**
```python
# Find tasks only one person is working on
alice_tasks = {'A', 'B', 'C', 'D'}
bob_tasks = {'C', 'D', 'E', 'F'}

unique_tasks = alice_tasks ^ bob_tasks
print(f"Tasks only one person has: {unique_tasks}")
# Tasks only one person has: {'A', 'B', 'E', 'F'}
# (Not 'C' or 'D' as both have them)
```

**Summary of Operators:**

```python
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1 | s2)   # {1, 2, 3, 4, 5, 6} - Union (all)
print(s1 & s2)   # {3, 4}             - Intersection (common)
print(s1 - s2)   # {1, 2}             - Difference (in s1, not s2)
print(s1 ^ s2)   # {1, 2, 5, 6}       - Symmetric diff (not common)
```

---

### Section 6: Set Membership and Subsets (2 minutes)

**Membership Testing:**

**Very fast - O(1) average case!**

```python
fruits = {'apple', 'banana', 'orange'}

# Check membership
print('apple' in fruits)    # True
print('grape' in fruits)    # False
print('banana' not in fruits)  # False
```

**Compare with list (slower):**
```python
# List - O(n) time
fruits_list = ['apple', 'banana', 'orange']
'apple' in fruits_list  # Checks each element

# Set - O(1) time
fruits_set = {'apple', 'banana', 'orange'}
'apple' in fruits_set  # Hash lookup, instant!
```

**Subset and Superset:**

```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# Is set1 a subset of set2?
print(set1.issubset(set2))  # True
print(set1 <= set2)         # True (operator form)

# Is set2 a superset of set1?
print(set2.issuperset(set1))  # True
print(set2 >= set1)           # True (operator form)

# Proper subset (subset but not equal)
print(set1 < set2)   # True
print(set1 < set1)   # False (not proper subset of itself)
```

**Disjoint Sets:**

Two sets are disjoint if they have no common elements.

```python
set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(set1.isdisjoint(set2))  # True (no common elements)

set3 = {3, 4, 5}
print(set1.isdisjoint(set3))  # False (3 is common)
```

---

### Section 7: Practical Applications (3 minutes)

**Application 1: Remove Duplicates**

```python
# List with duplicates
numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1]

# Remove duplicates
unique_numbers = list(set(numbers))
print(unique_numbers)  # [1, 2, 3, 4, 5] (order may vary)

# If order matters, preserve it
def remove_duplicates_preserve_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1]
unique = remove_duplicates_preserve_order(numbers)
print(unique)  # [1, 2, 3, 4, 5] (order preserved)
```

**Application 2: Find Unique Words**

```python
text = "the quick brown fox jumps over the lazy dog the fox"

# Split and convert to set
words = set(text.split())
print(f"Unique words: {words}")
print(f"Count: {len(words)}")
# Unique words: {'the', 'quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog'}
# Count: 8
```

**Application 3: Tag System**

```python
# Blog posts with tags
post1_tags = {'python', 'programming', 'tutorial', 'beginner'}
post2_tags = {'python', 'web', 'django', 'tutorial'}
post3_tags = {'javascript', 'web', 'frontend'}

# Find posts with Python
python_posts = []
all_posts = [
    ('Post 1', post1_tags),
    ('Post 2', post2_tags),
    ('Post 3', post3_tags)
]

for title, tags in all_posts:
    if 'python' in tags:
        python_posts.append(title)

print(f"Python posts: {python_posts}")
# Python posts: ['Post 1', 'Post 2']

# Find common tags between post1 and post2
common_tags = post1_tags & post2_tags
print(f"Common tags: {common_tags}")
# Common tags: {'python', 'tutorial'}

# Find all unique tags
all_tags = post1_tags | post2_tags | post3_tags
print(f"All tags: {all_tags}")
```

**Application 4: Access Control**

```python
# User permissions
alice_permissions = {'read', 'write', 'delete'}
bob_permissions = {'read', 'write'}
required_permissions = {'read', 'write', 'execute'}

# Check if Alice has all required permissions
has_access = required_permissions.issubset(alice_permissions)
print(f"Alice has access: {has_access}")  # False (missing 'execute')

# Check if Bob has all required permissions
has_access = required_permissions.issubset(bob_permissions)
print(f"Bob has access: {has_access}")  # False

# Find missing permissions
missing = required_permissions - alice_permissions
print(f"Alice missing: {missing}")  # {'execute'}
```

**Application 5: Data Analysis**

```python
# Analyze survey responses
survey1_respondents = {101, 102, 103, 104, 105}
survey2_respondents = {103, 104, 105, 106, 107}

# Who responded to both?
both_surveys = survey1_respondents & survey2_respondents
print(f"Responded to both: {both_surveys}")
# {103, 104, 105}

# Who responded to only one?
only_one = survey1_respondents ^ survey2_respondents
print(f"Only one survey: {only_one}")
# {101, 102, 106, 107}

# Total unique respondents
total = survey1_respondents | survey2_respondents
print(f"Total unique: {len(total)}")
# 7
```

**Application 6: Finding Common Elements**

```python
# Multiple student course enrollments
alice_courses = {'Math', 'Physics', 'Chemistry', 'English'}
bob_courses = {'Math', 'Chemistry', 'Biology', 'History'}
charlie_courses = {'Math', 'English', 'Art', 'Music'}

# Courses all three take
common_courses = alice_courses & bob_courses & charlie_courses
print(f"All three take: {common_courses}")
# {'Math'}

# Courses at least one takes
all_courses = alice_courses | bob_courses | charlie_courses
print(f"All available courses: {all_courses}")
```

---

### Common Pitfalls and Best Practices (1 minute)

**Pitfall 1: Empty Set**

```python
# Wrong - creates dict!
empty = {}
print(type(empty))  # <class 'dict'>

# Right
empty = set()
print(type(empty))  # <class 'set'>
```

**Pitfall 2: Sets Are Unordered**

```python
# Don't rely on order!
my_set = {3, 1, 2}
# print(my_set[0])  # TypeError

# If you need order, use list
my_list = sorted(my_set)
```

**Pitfall 3: Elements Must Be Immutable**

```python
# Wrong
# my_set = {[1, 2], [3, 4]}  # TypeError

# Right - use tuples
my_set = {(1, 2), (3, 4)}
```

**Best Practice 1: Use Sets for Membership Testing**

```python
# Fast membership testing
valid_users = {'alice', 'bob', 'charlie'}

# O(1) lookup
if username in valid_users:
    grant_access()
```

**Best Practice 2: Remove Duplicates**

```python
# Quick duplicate removal
unique_items = list(set(items))
```

**Best Practice 3: Use Operators for Readability**

```python
# Clear and concise
mutual_friends = alice_friends & bob_friends
all_friends = alice_friends | bob_friends
alice_only = alice_friends - bob_friends
```

---

### Summary (1 minute)

**What We Learned:**

1. **Sets are:** Unordered collections of unique elements
2. **Create sets:** `{1, 2, 3}` or `set([1, 2, 3])`
3. **Empty set:** Must use `set()`, not `{}`

4. **Add/Remove:**
   - `add()` - add single element
   - `update()` - add multiple
   - `remove()` - error if not found
   - `discard()` - safe removal
   - `pop()` - remove arbitrary
   - `clear()` - remove all

5. **Set Operations:**
   - **Union** (`|`): All elements from both
   - **Intersection** (`&`): Common elements
   - **Difference** (`-`): In first, not second
   - **Symmetric Difference** (`^`): Not in both

6. **Testing:**
   - `in` - membership (very fast!)
   - `issubset()` / `<=` - subset check
   - `issuperset()` / `>=` - superset check
   - `isdisjoint()` - no common elements

**Key Takeaways:**

- **Sets guarantee uniqueness** - duplicates automatically removed
- **Fast membership testing** - O(1) instead of O(n)
- **Mathematical operations** - union, intersection, difference
- **Elements must be immutable** - no lists, only tuples
- **Unordered** - don't rely on element order

**When to Use Sets:**

✓ Need unique elements only  
✓ Fast membership testing  
✓ Set operations (finding common elements, differences)  
✓ Removing duplicates  
✓ Tag systems, permissions  
✗ Need ordered elements (use list)  
✗ Need duplicates (use list)  
✗ Need indexing (use list/tuple)

**Real-World Applications:**

- Duplicate removal
- Tag and category systems
- Permission checking
- Finding mutual friends/interests
- Data analysis (unique values, intersections)
- Graph algorithms

**Master sets for efficient data manipulation in Python!**
