## Lecture Notes: Creating and Using Sets

**Duration:** 12 minutes

---

### What Are Sets?

**Definition:** Unordered collection of unique elements.

```python
fruits = {'apple', 'banana', 'orange'}
print(fruits)  # {'apple', 'banana', 'orange'}
```

**Key Properties:**

1. **Unique elements only:**
```python
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)  # {1, 2, 3} - duplicates removed
```

2. **Unordered:**
```python
my_set = {5, 1, 3, 2}
# No guaranteed order
# my_set[0]  # Error - no indexing
```

3. **Mutable, but elements must be immutable:**
```python
numbers = {1, 2, 3}
numbers.add(4)  # ✓ Can modify set

# bad_set = {[1, 2]}  # ✗ Lists not allowed
good_set = {(1, 2)}   # ✓ Tuples allowed
```

---

### Creating Sets

**Method 1: Curly Braces**
```python
fruits = {'apple', 'banana', 'orange'}
```

**Method 2: set() Constructor**
```python
# From list
numbers = set([1, 2, 3, 2, 1])
print(numbers)  # {1, 2, 3}

# From string
letters = set('hello')
print(letters)  # {'h', 'e', 'l', 'o'}

# Empty set - must use set()!
empty = set()  # ✓ Correct
# empty = {}   # ✗ Creates dict!
```

---

### Adding and Removing

**Add Elements:**
```python
fruits = {'apple', 'banana'}

# Add single
fruits.add('orange')

# Add duplicate - no effect
fruits.add('apple')

# Add multiple
fruits.update(['mango', 'grape'])
```

**Remove Elements:**
```python
numbers = {1, 2, 3, 4, 5}

# remove() - error if not found
numbers.remove(3)
# numbers.remove(10)  # KeyError

# discard() - safe, no error
numbers.discard(3)
numbers.discard(10)  # No error

# pop() - remove arbitrary
item = numbers.pop()

# clear() - remove all
numbers.clear()
```

---

### Set Operations

**Union (|) - Combine All**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1 | set2
# {1, 2, 3, 4, 5}

# Or
result = set1.union(set2)
```

**Intersection (&) - Common Elements**
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1 & set2
# {3, 4}

# Or
result = set1.intersection(set2)
```

**Difference (-) - In First, Not Second**
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1 - set2
# {1, 2}

# Or
result = set1.difference(set2)
```

**Symmetric Difference (^) - Not in Both**
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1 ^ set2
# {1, 2, 5, 6}

# Or
result = set1.symmetric_difference(set2)
```

**Operation Summary:**
```python
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s1 | s2   # {1, 2, 3, 4, 5, 6} - All
s1 & s2   # {3, 4}             - Common
s1 - s2   # {1, 2}             - Only in s1
s1 ^ s2   # {1, 2, 5, 6}       - Not common
```

---

### Membership and Subsets

**Membership Testing (Fast!):**
```python
fruits = {'apple', 'banana', 'orange'}

'apple' in fruits     # True - O(1)
'grape' in fruits     # False
'banana' not in fruits  # False
```

**Subset Checks:**
```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# Is set1 subset of set2?
set1.issubset(set2)    # True
set1 <= set2           # True

# Is set2 superset of set1?
set2.issuperset(set1)  # True
set2 >= set1           # True

# Proper subset (not equal)
set1 < set2            # True
set1 < set1            # False
```

**Disjoint Sets:**
```python
set1 = {1, 2, 3}
set2 = {4, 5, 6}

set1.isdisjoint(set2)  # True (no common elements)
```

---

### Practical Applications

**1. Remove Duplicates:**
```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))
# [1, 2, 3, 4, 5]
```

**2. Find Unique Words:**
```python
text = "the quick brown fox jumps over the lazy fox"
unique_words = set(text.split())
# {'the', 'quick', 'brown', 'fox', 'jumps', 'over', 'lazy'}
```

**3. Find Mutual Friends:**
```python
alice_friends = {'Bob', 'Charlie', 'Diana'}
bob_friends = {'Alice', 'Charlie', 'Frank'}

mutual = alice_friends & bob_friends
# {'Charlie'}
```

**4. Fast Membership:**
```python
valid_users = {'alice', 'bob', 'charlie'}

if username in valid_users:  # O(1) lookup
    grant_access()
```

**5. Tag Filtering:**
```python
post_tags = {'python', 'web', 'tutorial'}
required = {'python', 'tutorial'}

# Has all required tags?
has_all = required.issubset(post_tags)  # True
```

**6. Permission Checking:**
```python
user_permissions = {'read', 'write'}
required_permissions = {'read', 'write', 'execute'}

# Missing permissions
missing = required_permissions - user_permissions
# {'execute'}
```

---

### Common Pitfalls

**1. Empty Set:**
```python
# Wrong
empty = {}  # This is a dict!

# Right
empty = set()
```

**2. No Indexing:**
```python
my_set = {1, 2, 3}
# my_set[0]  # Error - sets are unordered
```

**3. Elements Must Be Immutable:**
```python
# Wrong
# my_set = {[1, 2]}  # Error

# Right
my_set = {(1, 2)}  # Tuples OK
```

**4. Duplicates Automatically Removed:**
```python
my_set = {1, 2, 2, 3}
# Don't expect {1, 2, 2, 3}
# Actually: {1, 2, 3}
```

---

### Quick Reference

**Create:**
```python
fruits = {'apple', 'banana'}    # Literal
numbers = set([1, 2, 3])        # From list
empty = set()                   # Empty
```

**Add/Remove:**
```python
s.add(item)         # Add one
s.update(items)     # Add multiple
s.remove(item)      # Remove (error if missing)
s.discard(item)     # Remove (safe)
s.pop()             # Remove arbitrary
s.clear()           # Remove all
```

**Operations:**
```python
s1 | s2             # Union
s1 & s2             # Intersection
s1 - s2             # Difference
s1 ^ s2             # Symmetric difference
```

**Testing:**
```python
item in s           # Membership
s1.issubset(s2)     # Subset
s1.issuperset(s2)   # Superset
s1.isdisjoint(s2)   # No common elements
```

---

### When to Use Sets

**Use Sets:**
- ✓ Need unique elements only
- ✓ Fast membership testing
- ✓ Set operations (union, intersection)
- ✓ Remove duplicates
- ✓ Order doesn't matter

**Use Lists:**
- ✗ Need duplicates
- ✗ Need specific order
- ✗ Need indexing
- ✗ Elements are mutable

**Use Tuples:**
- ✗ Need order + immutability
- ✗ Use as dict keys
- ✗ Multiple returns

---

### Performance

**Time Complexity:**

| Operation | Set | List |
|-----------|-----|------|
| Membership (`in`) | O(1) | O(n) |
| Add | O(1) | O(1) |
| Remove | O(1) | O(n) |
| Union | O(len(s1) + len(s2)) | - |
| Intersection | O(min(len(s1), len(s2))) | - |

**Key Advantage:** Fast membership testing!

---

### Real-World Examples

**1. Social Network:**
```python
# Find mutual friends
mutual = alice_friends & bob_friends

# Suggest friends (friends of friends)
suggestions = bob_friends - alice_friends
```

**2. E-commerce:**
```python
# Items in stock at all warehouses
in_all = warehouse1 & warehouse2 & warehouse3

# Items in any warehouse
available = warehouse1 | warehouse2 | warehouse3
```

**3. Content System:**
```python
# Articles with required tags
if required_tags.issubset(article_tags):
    include_article()
```

**4. Access Control:**
```python
# Check permissions
if not required_perms.issubset(user_perms):
    deny_access()
```

---

### Key Takeaways

1. **Sets store unique elements** - duplicates automatically removed
2. **Unordered** - no indexing, no guaranteed order
3. **Fast membership** - O(1) instead of O(n)
4. **Powerful operations** - union, intersection, difference
5. **Elements must be immutable** - use tuples, not lists
6. **Empty set:** Use `set()`, not `{}`

**Master sets for efficient unique collection handling!**
