## Post-class Quiz: Checking for Key Existence

---

### Question 1
What does `'hello' in {'hello': 'world'}` return?

A) True — 'hello' is a key
B) False — 'hello' is a value
C) True — 'hello' is a value
D) Error

**Correct Answer: A**

*Explanation: The `in` operator checks dictionary **keys**. 'hello' is a key in this dictionary, so it returns True.*

---

### Question 2
How do you check if a VALUE exists in a dictionary?

A) `value in dict`
B) `value in dict.keys()`
C) `value in dict.values()`
D) `dict.has_value(value)`

**Correct Answer: C**

*Explanation: `dict.values()` returns a view of all values. Using `in` on this view checks if the value exists. `in dict` only checks keys. `has_value()` doesn't exist.*

---

### Question 3
What is the output?

```python
d = {1: 'one', 2: 'two', 3: 'three'}
print(1 in d, 'one' in d)
```

A) `True True`
B) `True False`
C) `False True`
D) `False False`

**Correct Answer: B**

*Explanation: `1 in d` checks if 1 is a key — True. `'one' in d` checks if 'one' is a key — False (it's a value, not a key).*

---

### Question 4
Which is the correct way to safely access a possibly missing key?

A) `if key in d: val = d[key]`
B) `val = d.get(key, default)`
C) Both A and B are correct
D) Neither is correct

**Correct Answer: C**

*Explanation: Both approaches are valid. `in` is better when you need different logic paths. `.get()` is more concise when you just need a fallback value.*

---

### Question 5
What is the time complexity of `key in dict`?

A) O(n)
B) O(log n)
C) O(1) average
D) O(n²)

**Correct Answer: C**

*Explanation: Dictionaries use hash tables, so key lookup is O(1) on average — constant time regardless of dictionary size.*

---
