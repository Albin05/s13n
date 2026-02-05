## Post-class Quiz: Removing Dictionary Entries

---

### Question 1
What is the output?

```python
d = {'a': 1, 'b': 2, 'c': 3}
val = d.pop('b')
print(val, d)
```

A) `2 {'a': 1, 'c': 3}`
B) `'b' {'a': 1, 'c': 3}`
C) `('b', 2) {'a': 1, 'c': 3}`
D) `None {'a': 1, 'c': 3}`

**Correct Answer: A**

*Explanation: `pop('b')` removes key 'b' and returns its value (2). The dictionary now has only 'a' and 'c'. `pop()` returns the value, not the key or a tuple.*

---

### Question 2
What happens with `d.pop('x')` when 'x' is not in `d`?

A) Returns None
B) Returns False
C) Raises KeyError
D) Does nothing

**Correct Answer: C**

*Explanation: Without a default argument, `pop()` raises KeyError when the key is missing. To avoid this, use `d.pop('x', None)` or `d.pop('x', default_value)`.*

---

### Question 3
What does `popitem()` remove?

A) The first item added
B) A random item
C) The last item added
D) The item with the smallest key

**Correct Answer: C**

*Explanation: In Python 3.7+, dictionaries maintain insertion order. `popitem()` removes and returns the last inserted key-value pair (LIFO — Last In, First Out).*

---

### Question 4
What is the difference between `del d` and `d.clear()`?

A) No difference
B) `del d` deletes the variable; `clear()` empties the dict
C) `del d` empties the dict; `clear()` deletes the variable
D) Both delete the variable

**Correct Answer: B**

*Explanation: `del d` removes the variable completely — accessing `d` afterward causes NameError. `d.clear()` empties the dictionary but the variable `d` still exists as an empty dict `{}`.*

---

### Question 5
What is the safe way to remove multiple keys?

A) `for k in keys: del d[k]`
B) `for k in keys: d.pop(k, None)`
C) `for k in d: d.pop(k)`
D) `d.remove(keys)`

**Correct Answer: B**

*Explanation: `pop(k, None)` skips missing keys safely. Option A crashes if any key is missing. Option C modifies the dict while iterating (RuntimeError). Option D doesn't exist — dicts have no `remove()` method.*

---
