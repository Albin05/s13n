## Lecture Notes: Creating and Initializing Sets for Unique Values

**Duration:** 10 minutes

---

### What Are Sets?

A **set** is an unordered collection of unique elements. Think of it like a bag where no item can appear twice.

```python
fruits = {'apple', 'banana', 'orange'}
print(fruits)       # {'apple', 'banana', 'orange'}
print(type(fruits)) # <class 'set'>
```

**Core Properties:**
1. **Unique elements only** — duplicates are silently removed
2. **Unordered** — no indexing, no guaranteed print order
3. **Mutable** — you can add/remove elements
4. **Elements must be immutable** — strings, numbers, tuples only

---

### Creating Sets — Three Methods

**Method 1: Curly Braces (Literal)**

```python
colors = {'red', 'green', 'blue'}
numbers = {10, 20, 30, 40}
mixed = {1, 'hello', 3.14, True}
```

**Method 2: `set()` Constructor**

```python
# From a list
nums = set([1, 2, 3, 4, 5])
print(nums)  # {1, 2, 3, 4, 5}

# From a string (each character becomes an element)
letters = set('hello')
print(letters)  # {'h', 'e', 'l', 'o'}

# From a tuple
coords = set((10, 20, 30))
print(coords)  # {10, 20, 30}

# From range
evens = set(range(0, 10, 2))
print(evens)  # {0, 2, 4, 6, 8}
```

**Method 3: Empty Set**

```python
# CORRECT way to create an empty set
empty = set()
print(type(empty))  # <class 'set'>

# WRONG — this creates an empty dictionary!
not_a_set = {}
print(type(not_a_set))  # <class 'dict'>
```

This is one of the most common mistakes in Python.

---

### Automatic Duplicate Removal

When you create a set, duplicates vanish automatically:

```python
numbers = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
print(numbers)  # {1, 2, 3, 4}
print(len(numbers))  # 4

# From a list with duplicates
scores = [85, 92, 78, 92, 85, 88, 95, 78]
unique_scores = set(scores)
print(unique_scores)  # {78, 85, 88, 92, 95}
print(f"Original: {len(scores)}, Unique: {len(unique_scores)}")
# Original: 8, Unique: 5
```

---

### What Can and Cannot Be in a Set?

**Allowed (immutable types):**
```python
valid_set = {
    42,           # int
    3.14,         # float
    'hello',      # str
    True,         # bool
    (1, 2, 3),    # tuple
    frozenset({1, 2})  # frozenset
}
```

**Not Allowed (mutable types):**
```python
# Lists — TypeError
# bad = {[1, 2, 3]}

# Dictionaries — TypeError
# bad = {{'a': 1}}

# Sets inside sets — TypeError
# bad = {{1, 2}}
```

**Why?** Sets use hash tables internally. Only hashable (immutable) objects can be hashed.

---

### Converting Between Types

```python
# List → Set (removes duplicates)
my_list = [1, 2, 2, 3, 4, 4]
my_set = set(my_list)
print(my_set)  # {1, 2, 3, 4}

# Set → List
back_to_list = list(my_set)
print(back_to_list)  # [1, 2, 3, 4] (order may vary)

# Set → Sorted List
sorted_list = sorted(my_set)
print(sorted_list)  # [1, 2, 3, 4]

# String → Set → Sorted String
word = "mississippi"
unique_chars = sorted(set(word))
print(unique_chars)  # ['i', 'm', 'p', 's']
```

---

### Practical Applications

**1. Remove Duplicates from a List:**
```python
data = [5, 3, 8, 3, 5, 1, 8, 2]
unique_data = list(set(data))
print(unique_data)  # [1, 2, 3, 5, 8] (order may vary)
```

**2. Count Unique Elements:**
```python
words = "the cat sat on the mat the cat".split()
unique_count = len(set(words))
print(f"Unique words: {unique_count}")  # Unique words: 5
```

**3. Track Unique Visitors:**
```python
visitors = set()
visitors.add('user_101')
visitors.add('user_205')
visitors.add('user_101')  # duplicate — ignored
print(f"Unique visitors: {len(visitors)}")  # 2
```

**4. Find Unique Characters:**
```python
password = "p@ssw0rd!"
unique_chars = set(password)
print(f"Uses {len(unique_chars)} unique characters out of {len(password)}")
# Uses 8 unique characters out of 9
```

---

### Common Pitfalls

**1. `{}` Creates a Dict, Not a Set:**
```python
a = {}
b = set()
print(type(a))  # <class 'dict'>
print(type(b))  # <class 'set'>
```

**2. Sets Are Unordered — No Indexing:**
```python
s = {10, 20, 30}
# s[0]  # TypeError: 'set' object is not subscriptable
```

**3. `set('hello')` Splits Into Characters:**
```python
result = set('hello')
print(result)  # {'h', 'e', 'l', 'o'} — NOT {'hello'}

# To put a whole string in a set:
result = {'hello'}
print(result)  # {'hello'}
```

**4. `True` and `1` Are Considered Equal:**
```python
s = {True, 1, 'one'}
print(s)  # {True, 'one'} — True and 1 collapse
```

---

### Quick Reference

| Task | Code |
|------|------|
| Create from values | `{1, 2, 3}` |
| Create from list | `set([1, 2, 3])` |
| Create empty | `set()` |
| Remove duplicates | `list(set(my_list))` |
| Count unique | `len(set(data))` |
| Check type | `type(x) == set` |

---

### Key Takeaways

1. Sets store **unique elements only** — duplicates are removed automatically
2. Three ways to create: `{values}`, `set(iterable)`, `set()` for empty
3. `{}` creates a **dict**, not a set — use `set()` for empty sets
4. Elements must be **immutable** — no lists or dicts inside sets
5. Sets are **unordered** — no indexing or slicing
6. Great for **deduplication** and **unique counting**
