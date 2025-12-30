## Post-class Quiz: Performing Set Union and Intersection Operations

**Duration:** 5 minutes

---

### Q1: Union Result

What will be the output?

```python
A = {1, 2, 3}
B = {3, 4, 5}
result = A | B
print(len(result))
```

**A)** 5
**B)** 6
**C)** 3
**D)** Error

**Correct Answer:** A) 5

**Explanation:** Union (`|`) combines all unique elements from both sets. A has {1,2,3} and B has {3,4,5}. Combined uniquely: {1,2,3,4,5} = 5 elements. The duplicate 3 appears only once.

---

### Q2: Intersection Result

What will be the output?

```python
users_web = {'alice', 'bob', 'charlie'}
users_mobile = {'bob', 'charlie', 'diana'}
both = users_web & users_mobile
print(both)
```

**A)** {'alice', 'bob', 'charlie', 'diana'}
**B)** {'bob', 'charlie'}
**C)** {'alice', 'diana'}
**D)** set()

**Correct Answer:** B) {'bob', 'charlie'}

**Explanation:** Intersection (`&`) finds elements present in ALL sets. Only 'bob' and 'charlie' appear in both users_web and users_mobile, so the result is {'bob', 'charlie'}.

---

### Q3: Empty Intersection

What happens when two sets have no common elements?

```python
A = {1, 2, 3}
B = {4, 5, 6}
result = A & B
```

**A)** Returns None
**B)** Returns empty set: set()
**C)** Raises ValueError
**D)** Returns {1,2,3,4,5,6}

**Correct Answer:** B) Returns empty set: set()

**Explanation:** When sets have no common elements, intersection returns an empty set `set()`, not None or an error. This is a valid result indicating no overlap.

---

### Q4: Multiple Set Operations

What will be the output?

```python
A = {1, 2, 3}
B = {2, 3, 4}
C = {3, 4, 5}
result = A & B & C
print(result)
```

**A)** {1, 2, 3, 4, 5}
**B)** {2, 3, 4}
**C)** {3}
**D)** {3, 4}

**Correct Answer:** C) {3}

**Explanation:** Intersection of multiple sets finds elements common to ALL sets. Only 3 appears in all three sets (A, B, and C), so the result is {3}.

---

### Q5: Original Sets Unchanged

After these operations, what are the values of A and B?

```python
A = {1, 2, 3}
B = {3, 4, 5}
result = A | B
```

**A)** A = {1,2,3,4,5}, B = {3,4,5}
**B)** A = {1,2,3}, B = {3,4,5}
**C)** A = {1,2,3}, B = {1,2,3,4,5}
**D)** Both A and B are empty

**Correct Answer:** B) A = {1,2,3}, B = {3,4,5}

**Explanation:** Set operations (union, intersection) return NEW sets and do NOT modify the original sets. A and B remain unchanged after the operation.

---

## Answer Key

| Question | Correct Answer | Key Concept                    |
| -------- | -------------- | ------------------------------ |
| Q1       | A              | Union combines, removes dupes  |
| Q2       | B              | Intersection finds common      |
| Q3       | B              | Empty set when no overlap      |
| Q4       | C              | Multiple set intersection      |
| Q5       | B              | Operations don't modify originals |
