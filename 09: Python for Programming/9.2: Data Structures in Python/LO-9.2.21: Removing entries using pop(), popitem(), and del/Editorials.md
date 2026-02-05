## Editorials: Removing Dictionary Entries

---

### Q1 Solution: Basic Removal Methods

```python
inventory = {'apple': 50, 'banana': 30, 'cherry': 0, 'date': 15, 'elderberry': 5}

del inventory['cherry']
date_qty = inventory.pop('date')
print(f"Removed date with quantity: {date_qty}")

last = inventory.popitem()
print(f"Last item removed: {last}")

print(f"Remaining: {inventory}")
```

**Explanation:** `del` removes without returning. `pop()` removes and returns the value. `popitem()` removes and returns the last key-value pair as a tuple.

---

### Q2 Solution: Safe Key Removal

```python
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
remove_keys = ['b', 'c', 'x', 'y', 'z']

for key in remove_keys:
    val = data.pop(key, None)
    if val is not None:
        print(f"Removed: {key}={val}")
    else:
        print(f"Not found: {key}")

print(f"Final: {data}")
```

**Explanation:** `pop(key, None)` returns `None` for missing keys instead of raising an error. We check the return value to report whether the key was found.

---

### Q3 Solution: Data Sanitizer

```python
def sanitize(data, keep_keys):
    safe = {k: v for k, v in data.items() if k in keep_keys}
    removed = {k: v for k, v in data.items() if k not in keep_keys}
    return safe, removed

user = {
    'name': 'Alice', 'age': 25, 'email': 'alice@mail.com',
    'password': 'secret', 'ssn': '123-45-6789',
    'address': 'Mumbai', 'phone': '9876543210'
}
keep = {'name', 'age', 'email', 'address', 'phone'}

safe, removed = sanitize(user, keep)
print(f"Safe data: {safe}")
print(f"Removed: {removed}")
```

**Explanation:** Dictionary comprehensions with set membership filtering. We create two new dicts — one with keys in `keep`, one with keys not in `keep`.

---

### Q4 Solution: Task Queue

```python
tasks = {
    'T001': {'desc': 'Fix login bug', 'priority': 'high'},
    'T002': {'desc': 'Update docs', 'priority': 'low'},
    'T003': {'desc': 'Add tests', 'priority': 'medium'},
    'T004': {'desc': 'Deploy v2', 'priority': 'high'},
    'T005': {'desc': 'Clean logs', 'priority': 'low'}
}

# 1. Remove all high priority
high = [tid for tid, t in tasks.items() if t['priority'] == 'high']
for tid in high:
    task = tasks.pop(tid)
    print(f"Processing HIGH: {tid} - {task['desc']}")

# 2. Process next with popitem
tid, task = tasks.popitem()
print(f"Processing next: {tid} - {task['desc']}")

# 3. Clear remaining
tasks.clear()
print(f"Queue cleared. Tasks remaining: {len(tasks)}")
```

---

### Q5 Solution: Cache Manager

```python
cache = {}
max_size = 3

def cache_set(key, value):
    global cache
    if len(cache) >= max_size and key not in cache:
        # Evict oldest (first inserted)
        oldest = next(iter(cache))
        cache.pop(oldest)
        print(f"Evicted: {oldest}")
    cache[key] = value

def cache_get(key):
    return cache.get(key, 'MISS')

def cache_delete(key):
    return cache.pop(key, None)

def cache_clear():
    cache.clear()

cache_set('a', 1)
cache_set('b', 2)
cache_set('c', 3)
print(f"Cache full: {cache}")

cache_set('d', 4)  # Evicts 'a'
print(f"After adding d: {cache}")

print(f"Get a: {cache_get('a')}")  # MISS
print(f"Get b: {cache_get('b')}")  # 2

cache_delete('c')
print(f"After deleting c: {cache}")
```

**Explanation:** We use `next(iter(cache))` to get the first (oldest) key for eviction. `pop()` removes it safely. This implements a simple FIFO cache eviction policy.
