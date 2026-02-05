## Post-class Quiz: Accessing Dictionary Values

---

### Question 1
What happens when you access a non-existent key with `dict[key]`?

A) Returns `None`
B) Returns `0`
C) Raises `KeyError`
D) Returns an empty string

**Correct Answer: C**

*Explanation: Using square bracket notation to access a key that doesn't exist raises a `KeyError` exception, which crashes your program unless caught with try/except.*

---

### Question 2
What is the output?

```python
d = {'a': 1, 'b': 2}
print(d.get('c', 99))
```

A) `None`
B) `99`
C) `KeyError`
D) `0`

**Correct Answer: B**

*Explanation: `.get('c', 99)` looks for key 'c'. Since it doesn't exist, it returns the default value 99. Without the second argument, it would return None.*

---

### Question 3
What does `'hello' in {'hello': 'world'}` return?

A) `True` — checks if 'hello' is a key
B) `False` — checks if 'hello' is a value
C) `True` — checks if 'hello' is a value
D) Error

**Correct Answer: A**

*Explanation: The `in` operator for dictionaries checks **keys**, not values. Since 'hello' is a key in the dictionary, it returns True.*

---

### Question 4
What is the output?

```python
data = {'x': {'y': {'z': 42}}}
result = data.get('x', {}).get('y', {}).get('z', 0)
print(result)
```

A) `0`
B) `42`
C) `None`
D) `KeyError`

**Correct Answer: B**

*Explanation: Each `.get()` safely accesses the next level. 'x' exists → returns the nested dict. 'y' exists → returns the inner dict. 'z' exists → returns 42. If any key were missing, the `{}` default would prevent errors.*

---

### Question 5
What does `.get()` return when the key exists?

A) Always returns the default value
B) Returns the actual value associated with the key
C) Returns `None`
D) Returns both the key and value

**Correct Answer: B**

*Explanation: When the key exists, `.get()` returns the actual value — exactly like `dict[key]`. The default value is only used when the key is NOT found.*

---
