## Pre-Read: Removing Dictionary Entries

**Duration:** 5 minutes

---

### Four Ways to Remove

```python
d = {'a': 1, 'b': 2, 'c': 3}

# 1. del — remove by key
del d['a']       # d = {'b': 2, 'c': 3}

# 2. pop() — remove and return
val = d.pop('b') # val = 2, d = {'c': 3}

# 3. popitem() — remove last pair
pair = d.popitem()  # pair = ('c', 3), d = {}

# 4. clear() — remove everything
d = {'x': 1, 'y': 2}
d.clear()  # d = {}
```

---

### Safe Removal

```python
d = {'a': 1}

# pop() with default — no error
val = d.pop('z', None)  # val = None, no crash
```

---

### Key Point

`del` and `pop()` without default raise `KeyError` if the key is missing. Use `pop(key, default)` for safe removal.
