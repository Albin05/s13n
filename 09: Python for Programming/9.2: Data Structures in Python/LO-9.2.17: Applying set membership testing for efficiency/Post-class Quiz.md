## Post-class Quiz: Set Membership Testing for Efficiency

---

### Question 1
What is the time complexity of checking `x in my_set`?

A) O(n)
B) O(log n)
C) O(1) average case
D) O(n log n)

**Correct Answer: C**

*Explanation: Sets use hash tables internally. Looking up an element involves computing its hash and checking the corresponding bucket, which takes O(1) on average regardless of the set size.*

---

### Question 2
When should you convert a list to a set?

A) When you need to preserve element order
B) When you need to check membership multiple times
C) When you need to access elements by index
D) When you need duplicate elements

**Correct Answer: B**

*Explanation: Converting a list to a set costs O(n) once, but then each membership check becomes O(1) instead of O(n). This pays off when you check membership multiple times. Sets don't preserve order, don't support indexing, and don't allow duplicates.*

---

### Question 3
What does `a.issubset(b)` return?

A) True if `a` and `b` have the same elements
B) True if all elements of `a` are in `b`
C) True if `a` and `b` have no common elements
D) True if `a` has more elements than `b`

**Correct Answer: B**

*Explanation: `issubset()` returns True if every element in set `a` is also in set `b`. For example, `{1, 2}.issubset({1, 2, 3})` is True because both 1 and 2 are in the second set.*

---

### Question 4
What is the output?

```python
a = {1, 2, 3}
b = {4, 5, 6}
print(a.isdisjoint(b))
```

A) True
B) False
C) {1, 2, 3, 4, 5, 6}
D) Error

**Correct Answer: A**

*Explanation: `isdisjoint()` returns True when two sets have NO common elements. Sets {1, 2, 3} and {4, 5, 6} share nothing, so the result is True.*

---

### Question 5
What does `len(data) != len(set(data))` check?

A) If data is empty
B) If data has duplicates
C) If data is sorted
D) If data contains only unique elements

**Correct Answer: B**

*Explanation: `set(data)` removes duplicates. If the length changes after converting to a set, duplicates existed. If lengths are equal, all elements were already unique. So `!=` means "data has duplicates".*

---
