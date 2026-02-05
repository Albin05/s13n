## Lecture Notes: Performing Set Difference and Symmetric Difference Operations

**Duration:** 10 minutes

---

### Set Difference (`-`)

The **difference** of two sets returns elements that are in the first set but NOT in the second.

```python
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

result = set1 - set2
print(result)  # {1, 2}
```

**Using the method:**
```python
result = set1.difference(set2)
print(result)  # {1, 2}
```

**Order matters!**
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a - b)  # {1, 2} — in a, not in b
print(b - a)  # {5, 6} — in b, not in a
```

---

### Difference with Multiple Sets

```python
a = {1, 2, 3, 4, 5}
b = {2, 3}
c = {4, 5}

# Elements in a but not in b or c
result = a - b - c
print(result)  # {1}

# Using method
result = a.difference(b, c)
print(result)  # {1}
```

---

### Difference Update (`-=`)

Modifies the set **in place** instead of creating a new one:

```python
skills = {'Python', 'JavaScript', 'SQL', 'HTML', 'CSS'}
deprecated = {'HTML', 'CSS'}

skills -= deprecated
# OR: skills.difference_update(deprecated)
print(skills)  # {'Python', 'JavaScript', 'SQL'}
```

---

### Symmetric Difference (`^`)

Returns elements that are in **either** set but **not in both**. Think of it as "exclusive or" for sets.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1 ^ set2
print(result)  # {1, 2, 5, 6}
```

Elements 3 and 4 are in **both** sets, so they are excluded.

**Using the method:**
```python
result = set1.symmetric_difference(set2)
print(result)  # {1, 2, 5, 6}
```

---

### Symmetric Difference = Union Minus Intersection

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# These produce the same result:
print(a ^ b)              # {1, 2, 5, 6}
print((a | b) - (a & b))  # {1, 2, 5, 6}
```

---

### Symmetric Difference Update (`^=`)

```python
inventory = {'item_a', 'item_b', 'item_c'}
changes = {'item_b', 'item_d'}

inventory ^= changes
print(inventory)  # {'item_a', 'item_c', 'item_d'}
# item_b was in both — removed
# item_d was only in changes — added
```

---

### Practical Examples

**1. Find Missing and Extra Skills:**
```python
required = {'Python', 'SQL', 'Docker', 'Git'}
my_skills = {'Python', 'JavaScript', 'Git', 'React'}

missing = required - my_skills
print(f"Need to learn: {missing}")   # {'SQL', 'Docker'}

extra = my_skills - required
print(f"Bonus skills: {extra}")      # {'JavaScript', 'React'}

non_overlapping = required ^ my_skills
print(f"Differ on: {non_overlapping}")  # {'SQL', 'Docker', 'JavaScript', 'React'}
```

**2. Inventory Comparison:**
```python
warehouse_a = {'laptop', 'mouse', 'keyboard', 'monitor'}
warehouse_b = {'mouse', 'keyboard', 'webcam', 'headset'}

only_a = warehouse_a - warehouse_b
print(f"Only in A: {only_a}")  # {'laptop', 'monitor'}

only_b = warehouse_b - warehouse_a
print(f"Only in B: {only_b}")  # {'webcam', 'headset'}

exclusive = warehouse_a ^ warehouse_b
print(f"Not shared: {exclusive}")  # {'laptop', 'monitor', 'webcam', 'headset'}
```

**3. Survey Non-Respondents:**
```python
all_employees = {'Alice', 'Bob', 'Charlie', 'Diana', 'Eve'}
responded = {'Alice', 'Charlie', 'Eve'}

not_responded = all_employees - responded
print(f"Need to follow up: {not_responded}")  # {'Bob', 'Diana'}
```

---

### Operator vs Method Summary

| Operation | Operator | Method |
|-----------|----------|--------|
| Difference | `a - b` | `a.difference(b)` |
| Difference update | `a -= b` | `a.difference_update(b)` |
| Symmetric diff | `a ^ b` | `a.symmetric_difference(b)` |
| Symmetric diff update | `a ^= b` | `a.symmetric_difference_update(b)` |

---

### Key Takeaways

1. **Difference** (`-`): Elements in first set, not in second
2. **Order matters** for difference: `a - b ≠ b - a`
3. **Symmetric difference** (`^`): Elements in either but not both
4. **Order doesn't matter** for symmetric difference: `a ^ b == b ^ a`
5. Use `_update` variants to modify sets in place
6. Great for finding **gaps**, **extras**, and **non-overlapping** items
