## Post-class Quiz: Merging Dictionaries

---

### Question 1
What is the output?

```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d1.update(d2)
print(d1)
```

A) `{'a': 1, 'b': 2}`
B) `{'a': 1, 'b': 3, 'c': 4}`
C) `{'a': 1, 'b': 2, 'c': 4}`
D) `{'b': 3, 'c': 4}`

**Correct Answer: B**

*Explanation: `update()` adds new keys ('c') and overwrites existing ones with the new values ('b' becomes 3). All original keys that aren't in d2 remain unchanged ('a' stays 1).*

---

### Question 2
What is the difference between `d1.update(d2)` and `{**d1, **d2}`?

A) No difference
B) `update()` modifies d1 in place; `{**d1, **d2}` creates a new dict
C) `{**d1, **d2}` modifies d1 in place; `update()` creates a new dict
D) `update()` keeps d1 values; `{**d1, **d2}` keeps d2 values

**Correct Answer: B**

*Explanation: `update()` modifies the dictionary it's called on. Unpacking `{**d1, **d2}` creates a brand new dictionary, leaving both originals unchanged.*

---

### Question 3
In `{**d1, **d2, **d3}`, which dict's values take priority for shared keys?

A) d1 (first one)
B) d2 (middle one)
C) d3 (last one)
D) It raises an error for duplicate keys

**Correct Answer: C**

*Explanation: The last dictionary in the unpacking wins for shared keys. It's evaluated left to right — each subsequent dict overwrites values from earlier ones.*

---

### Question 4
What is the output?

```python
d1 = {'x': {'a': 1, 'b': 2}}
d2 = {'x': {'c': 3}}
result = {**d1, **d2}
print(result)
```

A) `{'x': {'a': 1, 'b': 2, 'c': 3}}`
B) `{'x': {'c': 3}}`
C) `{'x': {'a': 1, 'b': 2}, 'x': {'c': 3}}`
D) Error

**Correct Answer: B**

*Explanation: Dictionary merging is **shallow**. The entire value for key 'x' from d2 replaces d1's value. Nested dicts are not recursively merged — the inner dict `{'a': 1, 'b': 2}` is completely replaced by `{'c': 3}`.*

---

### Question 5
Which creates a merged dict WITHOUT modifying the originals?

A) `d1.update(d2)`
B) `d1 |= d2`
C) `{**d1, **d2}`
D) Both A and B

**Correct Answer: C**

*Explanation: `{**d1, **d2}` creates a new dict. Both `update()` and `|=` modify d1 in place. If you need the originals unchanged, use unpacking or the `|` operator (without `=`): `d1 | d2`.*

---
