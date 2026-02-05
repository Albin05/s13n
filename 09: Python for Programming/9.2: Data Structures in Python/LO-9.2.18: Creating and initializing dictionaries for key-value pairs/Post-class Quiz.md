## Post-class Quiz: Creating and Initializing Dictionaries

---

### Question 1
Which of the following correctly creates a dictionary?

A) `d = ['name': 'Alice']`
B) `d = {'name': 'Alice'}`
C) `d = ('name': 'Alice')`
D) `d = {name: Alice}`

**Correct Answer: B**

*Explanation: Dictionaries use curly braces `{}` with key-value pairs separated by colons. Option A uses list brackets, C uses tuple parentheses, and D is missing quotes around the strings.*

---

### Question 2
What is the output?

```python
d = {'a': 1, 'b': 2, 'a': 3}
print(d)
```

A) `{'a': 1, 'b': 2, 'a': 3}`
B) `{'a': 1, 'b': 2}`
C) `{'a': 3, 'b': 2}`
D) Error — duplicate keys

**Correct Answer: C**

*Explanation: Dictionary keys must be unique. When the same key 'a' is used twice, the last value (3) overwrites the first (1). No error is raised — it's silently overwritten.*

---

### Question 3
Which CANNOT be used as a dictionary key?

A) `'hello'` (string)
B) `(1, 2)` (tuple)
C) `[1, 2]` (list)
D) `42` (integer)

**Correct Answer: C**

*Explanation: Dictionary keys must be hashable (immutable). Lists are mutable, so they cannot be used as keys. Strings, tuples, and integers are all immutable and work fine as keys.*

---

### Question 4
What does `dict.fromkeys(['x', 'y', 'z'], 0)` return?

A) `{'x': 0, 'y': 0, 'z': 0}`
B) `{0: ['x', 'y', 'z']}`
C) `[('x', 0), ('y', 0), ('z', 0)]`
D) Error

**Correct Answer: A**

*Explanation: `fromkeys()` creates a dictionary where all the specified keys share the same value. It takes a list of keys and a default value, producing a dict with each key mapped to that value.*

---

### Question 5
What is the output?

```python
d = {x: x**2 for x in range(4)}
print(d)
```

A) `[0, 1, 4, 9]`
B) `{0: 0, 1: 1, 2: 4, 3: 9}`
C) `{0, 1, 4, 9}`
D) `{(0,0), (1,1), (2,4), (3,9)}`

**Correct Answer: B**

*Explanation: This is a dictionary comprehension. For each x in range(4) (0, 1, 2, 3), it creates a key-value pair where the key is x and the value is x squared.*

---
