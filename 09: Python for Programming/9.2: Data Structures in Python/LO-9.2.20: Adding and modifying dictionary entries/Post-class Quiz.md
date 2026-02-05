## Post-class Quiz: Adding and Modifying Dictionary Entries

---

### Question 1
What is the output?

```python
d = {'a': 1}
d['b'] = 2
d['a'] = 10
print(d)
```

A) `{'a': 1, 'b': 2}`
B) `{'a': 10, 'b': 2}`
C) `{'a': 1, 'a': 10, 'b': 2}`
D) Error

**Correct Answer: B**

*Explanation: `d['b'] = 2` adds a new key. `d['a'] = 10` overwrites the existing value for key 'a'. The result is `{'a': 10, 'b': 2}`. Dictionaries cannot have duplicate keys.*

---

### Question 2
What does `setdefault()` do when the key already exists?

A) Raises an error
B) Overwrites the existing value
C) Does nothing — keeps the existing value
D) Deletes the key

**Correct Answer: C**

*Explanation: `setdefault()` only sets the value if the key doesn't already exist. If the key is present, it leaves the existing value unchanged and returns it.*

---

### Question 3
What is the output?

```python
d = {'x': 5}
d.update({'x': 10, 'y': 20})
print(d)
```

A) `{'x': 5, 'y': 20}`
B) `{'x': 10, 'y': 20}`
C) `{'x': 5, 'x': 10, 'y': 20}`
D) Error — cannot update existing keys

**Correct Answer: B**

*Explanation: `update()` overwrites existing keys and adds new ones. Key 'x' is updated from 5 to 10, and key 'y' is added with value 20.*

---

### Question 4
What pattern correctly counts occurrences?

A) `counts[item] = counts[item] + 1`
B) `counts[item] = counts.get(item, 0) + 1`
C) `counts.add(item)`
D) `counts.append(item)`

**Correct Answer: B**

*Explanation: `.get(item, 0)` returns 0 for new keys (avoiding KeyError), then adds 1. Option A would crash with KeyError for new keys. Options C and D are list/set methods, not dict methods.*

---

### Question 5
What is the output?

```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
merged = {**d1, **d2}
print(merged)
```

A) `{'a': 1, 'b': 2, 'c': 4}`
B) `{'a': 1, 'b': 3, 'c': 4}`
C) `{'a': 1, 'b': 2, 'b': 3, 'c': 4}`
D) Error

**Correct Answer: B**

*Explanation: `{**d1, **d2}` merges both dicts. When keys overlap, the later dict wins. 'b' appears in both — d2's value (3) overrides d1's value (2).*

---
