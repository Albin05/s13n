## Pre-Read: Merging Dictionaries

**Duration:** 5 minutes

---

### Why Merge Dictionaries?

Combining data from multiple sources into one dictionary:

```python
defaults = {'color': 'blue', 'size': 'medium'}
user_choice = {'color': 'red'}

# User choice overrides defaults
final = {**defaults, **user_choice}
print(final)  # {'color': 'red', 'size': 'medium'}
```

---

### Two Main Methods

**`update()` — modifies in place:**
```python
d1 = {'a': 1}
d1.update({'b': 2})
print(d1)  # {'a': 1, 'b': 2}
```

**`{**d1, **d2}` — creates a new dict:**
```python
d1 = {'a': 1}
d2 = {'b': 2}
merged = {**d1, **d2}  # d1 unchanged
```

---

### The Rule: Last One Wins

```python
d1 = {'x': 1}
d2 = {'x': 99}
print({**d1, **d2})  # {'x': 99}
print({**d2, **d1})  # {'x': 1}
```

---

### Try This

```python
base = {'a': 1, 'b': 2}
override = {'b': 20, 'c': 30}
result = {**base, **override}
print(result)  # ?
```

**Answer:** `{'a': 1, 'b': 20, 'c': 30}`
