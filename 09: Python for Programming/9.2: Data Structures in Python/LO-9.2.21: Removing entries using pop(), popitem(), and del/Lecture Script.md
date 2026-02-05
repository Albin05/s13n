## Lecture Script: Removing Dictionary Entries

**Duration:** 15 minutes

---

### Hook (2 minutes)

You're processing user data before sending it to a third-party API:

```python
user = {'name': 'Alice', 'email': 'alice@mail.com',
        'password': 'secret123', 'credit_card': '4111-1111-1111-1111'}
```

You need to remove sensitive fields. How?

```python
safe_user = user.copy()
safe_user.pop('password', None)
safe_user.pop('credit_card', None)
print(safe_user)  # {'name': 'Alice', 'email': 'alice@mail.com'}
```

Removing entries is as important as adding them. Today we learn every way to do it.

---

### Section 1: del Statement (2 minutes)

```python
d = {'a': 1, 'b': 2, 'c': 3}

del d['b']
print(d)  # {'a': 1, 'c': 3}

# Missing key → error
# del d['z']  # KeyError: 'z'

# Safe pattern
if 'z' in d:
    del d['z']
```

---

### Section 2: pop() Method (3 minutes)

```python
d = {'a': 1, 'b': 2, 'c': 3}

# Remove and get value
val = d.pop('b')
print(val)  # 2
print(d)    # {'a': 1, 'c': 3}

# With default — no error
val = d.pop('z', -1)
print(val)  # -1

# Without default — error
# d.pop('z')  # KeyError
```

**pop() is preferred** when you need the removed value or want safe removal.

---

### Section 3: popitem() (2 minutes)

Removes the **last** inserted pair:

```python
d = {'x': 10, 'y': 20, 'z': 30}

pair = d.popitem()
print(pair)  # ('z', 30)
print(d)     # {'x': 10, 'y': 20}

# Process all items
while d:
    key, val = d.popitem()
    print(f"Processed {key}: {val}")
```

---

### Section 4: clear() (1 minute)

```python
d = {'a': 1, 'b': 2, 'c': 3}
d.clear()
print(d)  # {}
```

Dict still exists, just empty.

---

### Section 5: Practical Patterns (4 minutes)

**Remove multiple keys safely:**
```python
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for key in ['b', 'd', 'f']:
    data.pop(key, None)
print(data)  # {'a': 1, 'c': 3}
```

**Filter by condition (collect then remove):**
```python
scores = {'Alice': 90, 'Bob': 40, 'Charlie': 75, 'Diana': 30}
failing = [k for k, v in scores.items() if v < 50]
for k in failing:
    del scores[k]
print(scores)  # {'Alice': 90, 'Charlie': 75}
```

**Never modify while iterating:**
```python
# WRONG — RuntimeError
# for k in d:
#     if condition:
#         del d[k]

# RIGHT — collect first, then delete
to_remove = [k for k in d if condition(k)]
for k in to_remove:
    del d[k]
```

---

### Summary (1 minute)

| Method | Use When |
|--------|----------|
| `del d[key]` | Simple removal, don't need the value |
| `d.pop(key, default)` | Need the value or want safe removal |
| `d.popitem()` | Processing items one at a time (LIFO) |
| `d.clear()` | Reset the entire dictionary |
