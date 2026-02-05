## Post-class Quiz: Creating and Initializing Sets for Unique Values

---

### Question 1
What is the correct way to create an empty set in Python?

A) `empty = {}`
B) `empty = set()`
C) `empty = set({})`
D) `empty = {None}`

**Correct Answer: B**

*Explanation: `set()` is the only correct way to create an empty set. `{}` creates an empty dictionary, not a set. `set({})` also works but is redundant. `{None}` creates a set with one element (None), not an empty set.*

---

### Question 2
What is the output of the following code?

```python
numbers = {1, 2, 2, 3, 3, 3, 4}
print(len(numbers))
```

A) 7
B) 4
C) 3
D) Error

**Correct Answer: B**

*Explanation: Sets automatically remove duplicate elements. The set {1, 2, 2, 3, 3, 3, 4} stores only unique values: {1, 2, 3, 4}. Therefore len() returns 4.*

---

### Question 3
Which of the following CANNOT be an element in a set?

A) `(1, 2, 3)` (a tuple)
B) `"hello"` (a string)
C) `[1, 2, 3]` (a list)
D) `42` (an integer)

**Correct Answer: C**

*Explanation: Lists are mutable and therefore unhashable — they cannot be stored in a set. Sets require all elements to be immutable (hashable). Tuples, strings, and integers are all immutable and can be set elements.*

---

### Question 4
What is the output of `set("hello")`?

A) `{'hello'}`
B) `{'h', 'e', 'l', 'l', 'o'}`
C) `{'h', 'e', 'l', 'o'}`
D) `{'h', 'e', 'l', 'o', ' '}`

**Correct Answer: C**

*Explanation: When you pass a string to `set()`, it iterates over each character. Since 'l' appears twice but sets only keep unique elements, the duplicate 'l' is removed. The result is {'h', 'e', 'l', 'o'} with 4 elements.*

---

### Question 5
What does the following code print?

```python
a = {True, 1, 1.0}
print(len(a))
```

A) 3
B) 2
C) 1
D) Error

**Correct Answer: C**

*Explanation: In Python, `True == 1 == 1.0` are all considered equal and have the same hash value. Since sets only store unique values, all three collapse into a single element. The length is 1.*

---
