## Question Bank: Removing Dictionary Entries

---

### Q1: Basic Removal Methods (3 minutes, Low Difficulty)

Given:
```python
inventory = {'apple': 50, 'banana': 30, 'cherry': 0, 'date': 15, 'elderberry': 5}
```

1. Remove `'cherry'` using `del` (it's out of stock)
2. Remove `'date'` using `pop()` and print the removed value
3. Remove the last item using `popitem()` and print it
4. Print the remaining inventory

**Expected Output:**
```
Removed date with quantity: 15
Last item removed: ('elderberry', 5)
Remaining: {'apple': 50, 'banana': 30}
```

**Key Concepts:** `del`, `pop()`, `popitem()`

---

### Q2: Safe Key Removal (3 minutes, Low Difficulty)

Given a dictionary and a list of keys to remove:
```python
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
remove_keys = ['b', 'c', 'x', 'y', 'z']
```

Remove all keys from `remove_keys` that exist, without any errors for missing keys. Print which keys were actually removed and which weren't found.

**Expected Output:**
```
Removed: b=2
Removed: c=3
Not found: x
Not found: y
Not found: z
Final: {'a': 1, 'd': 4, 'e': 5}
```

**Key Concepts:** `pop()` with default value

---

### Q3: Data Sanitizer (5 minutes, Medium Difficulty)

Write a function `sanitize(data, keep_keys)` that:
- Takes a dictionary and a set of keys to keep
- Returns a new dictionary with ONLY the specified keys
- Also returns a dictionary of removed key-value pairs

```python
user = {
    'name': 'Alice', 'age': 25, 'email': 'alice@mail.com',
    'password': 'secret', 'ssn': '123-45-6789',
    'address': 'Mumbai', 'phone': '9876543210'
}
keep = {'name', 'age', 'email', 'address', 'phone'}
```

**Expected Output:**
```
Safe data: {'name': 'Alice', 'age': 25, 'email': 'alice@mail.com', 'address': 'Mumbai', 'phone': '9876543210'}
Removed: {'password': 'secret', 'ssn': '123-45-6789'}
```

**Key Concepts:** Selective removal, dictionary comprehension

---

### Q4: Task Queue (5 minutes, Medium Difficulty)

Implement a simple task queue using a dictionary:

```python
tasks = {
    'T001': {'desc': 'Fix login bug', 'priority': 'high'},
    'T002': {'desc': 'Update docs', 'priority': 'low'},
    'T003': {'desc': 'Add tests', 'priority': 'medium'},
    'T004': {'desc': 'Deploy v2', 'priority': 'high'},
    'T005': {'desc': 'Clean logs', 'priority': 'low'}
}
```

1. Process (remove) all high-priority tasks first, printing each
2. Process one more task using `popitem()`
3. Clear remaining tasks and print "Queue cleared"

**Expected Output:**
```
Processing HIGH: T001 - Fix login bug
Processing HIGH: T004 - Deploy v2
Processing next: T005 - Clean logs
Queue cleared. Tasks remaining: 0
```

**Key Concepts:** Conditional removal, `popitem()`, `clear()`

---

### Q5: Cache Manager (5 minutes, Medium Difficulty)

Build a simple cache with a maximum size:

```python
cache = {}
max_size = 3
```

Write functions:
1. `cache_set(key, value)` — adds to cache; if full, removes oldest entry first
2. `cache_get(key)` — returns value or `'MISS'`
3. `cache_delete(key)` — removes entry if exists
4. `cache_clear()` — empties cache

Test with this sequence:
- Set a=1, b=2, c=3 (cache full)
- Set d=4 (should evict 'a')
- Get 'a' (should be MISS)
- Get 'b' (should return 2)
- Delete 'c'
- Print cache state

**Key Concepts:** `popitem()` for eviction, `pop()` for deletion, cache pattern
