## Post-class Quiz: Iterating Through Dictionaries

---

### 
What does `for key in dict` iterate over?

A) Values
B) Keys
C) Key-value tuples
D) Indices

**Correct Answer: B**

*Explanation: By default, iterating over a dictionary yields its keys. Use `.values()` for values or `.items()` for key-value pairs.*

---

### 
How do you iterate over both keys and values?

A) `for k, v in dict`
B) `for k, v in dict.items()`
C) `for k, v in dict.values()`
D) `for k, v in dict.keys()`

**Correct Answer: B**

*Explanation: `.items()` returns key-value pairs as tuples, which can be unpacked into `k` and `v`. The other options either don't provide pairs or would cause errors.*

---

### 
What is the output?

```python
d = {'a': 1, 'b': 2, 'c': 3}
result = sum(d.values())
print(result)
```

A) `'abc'`
B) `6`
C) `3`
D) Error

**Correct Answer: B**

*Explanation: `d.values()` returns `[1, 2, 3]`. `sum()` adds them: 1 + 2 + 3 = 6.*

---

### 
What does `max(d, key=d.get)` return for `d = {'a': 3, 'b': 1, 'c': 5}`?

A) `5`
B) `'c'`
C) `('c', 5)`
D) `'a'`

**Correct Answer: B**

*Explanation: `max(d)` iterates over keys. `key=d.get` tells `max()` to compare keys by their values. Key 'c' has the highest value (5), so 'c' is returned — the key, not the value.*

---

### 
Why should you NOT modify a dict while iterating over it?

A) It's slower
B) It can cause RuntimeError
C) It's a syntax error
D) It deletes the dict

**Correct Answer: B**

*Explanation: Modifying a dictionary (adding/removing keys) during iteration causes `RuntimeError: dictionary changed size during iteration`. Instead, build a new dict or collect keys to modify, then apply changes after the loop.*

---
