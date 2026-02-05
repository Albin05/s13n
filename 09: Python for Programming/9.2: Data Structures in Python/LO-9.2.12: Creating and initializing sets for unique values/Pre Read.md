## Pre-Read: Creating and Initializing Sets for Unique Values

**Duration:** 5 minutes

---

### What You'll Learn

In this lesson, you'll learn about **sets** — Python's built-in data structure for storing unique values. Sets automatically remove duplicates and provide very fast lookups.

---

### The Problem: Duplicates

Imagine you have a list of user IDs and want only the unique ones:

```python
# With a list — manual work
ids = [101, 203, 101, 305, 203]
unique = []
for id in ids:
    if id not in unique:
        unique.append(id)
print(unique)  # [101, 203, 305]
```

This works, but it's slow and verbose.

**With a set — one line:**
```python
ids = [101, 203, 101, 305, 203]
unique = set(ids)
print(unique)  # {101, 203, 305}
```

---

### What Is a Set?

A set is an **unordered collection of unique elements**.

```python
# Create a set
fruits = {'apple', 'banana', 'orange'}

# Duplicates are removed automatically
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)  # {1, 2, 3}
```

**Three key rules:**
1. **No duplicates** — each element appears once
2. **No order** — you cannot access elements by index
3. **Immutable elements** — elements must be strings, numbers, or tuples

---

### Creating Sets

```python
# Method 1: Curly braces
colors = {'red', 'green', 'blue'}

# Method 2: From a list
data = set([1, 2, 3, 2, 1])  # {1, 2, 3}

# Method 3: Empty set
empty = set()  # NOT {} — that creates a dict!
```

---

### Why Sets Matter

Sets are useful when you need to:
- Remove duplicates from data
- Count unique items
- Check if something exists (very fast — O(1))
- Compare groups of items

---

### Quick Preview

```python
# Remove duplicates
scores = [85, 92, 78, 92, 85]
unique_scores = set(scores)
print(unique_scores)  # {78, 85, 92}

# Count unique words
text = "the cat the dog the bird"
words = set(text.split())
print(len(words))  # 4 unique words
```

---

### Try Before Class

```python
# What will this print?
my_set = {3, 1, 4, 1, 5, 9, 2, 6, 5}
print(len(my_set))  # ?

# What type is this?
mystery = {}
print(type(mystery))  # ?

# What about this?
letters = set("banana")
print(letters)  # ?
```

**Answers:** `7`, `<class 'dict'>`, `{'b', 'a', 'n'}`

---

### Get Ready

In class, you'll learn:
- All the ways to create sets
- What can and cannot be stored in a set
- How to convert between sets and other types
- Practical uses like deduplication and unique counting
