## Post-class Quiz: Set Difference and Symmetric Difference

---

### Question 1
What is the output of the following code?

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}
print(a - b)
```

A) `{1, 2, 3}`
B) `{6, 7}`
C) `{1, 2, 3, 6, 7}`
D) `{4, 5}`

**Correct Answer: A**

*Explanation: `a - b` returns elements in `a` that are NOT in `b`. Elements 1, 2, 3 are in `a` but not in `b`. Elements 4, 5 are in both so they're excluded from the result.*

---

### Question 2
What is the output?

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a ^ b)
```

A) `{2, 3}`
B) `{1, 4}`
C) `{1, 2, 3, 4}`
D) `{1}`

**Correct Answer: B**

*Explanation: `a ^ b` (symmetric difference) returns elements in either set but NOT in both. 1 is only in `a`, 4 is only in `b`. Elements 2, 3 are in both sets and therefore excluded.*

---

### Question 3
Which statement is TRUE about set difference?

A) `a - b` always equals `b - a`
B) `a - b` returns elements common to both sets
C) `a - b` returns elements in `a` that are not in `b`
D) `a - b` modifies `a` in place

**Correct Answer: C**

*Explanation: Difference returns elements from the first set that aren't in the second. It's not commutative (A is wrong). It doesn't find common elements (B is wrong, that's intersection). It creates a new set without modifying the originals (D is wrong; `difference_update` modifies in place).*

---

### Question 4
What is the output?

```python
x = {10, 20, 30}
y = {20, 30, 40}
x -= y
print(x)
```

A) `{10, 20, 30}`
B) `{10}`
C) `{40}`
D) `{10, 40}`

**Correct Answer: B**

*Explanation: `x -= y` is the difference update operation. It modifies `x` in place, removing any elements that are also in `y`. Elements 20 and 30 are in `y`, so they're removed from `x`, leaving only `{10}`.*

---

### Question 5
Which expression is equivalent to `a ^ b`?

A) `a - b`
B) `(a | b) - (a & b)`
C) `a & b`
D) `a | b`

**Correct Answer: B**

*Explanation: Symmetric difference (`a ^ b`) equals the union minus the intersection — everything from both sets, excluding what they share. `(a | b)` gives all elements, `(a & b)` gives shared elements, subtracting shared from all gives the symmetric difference.*

---
