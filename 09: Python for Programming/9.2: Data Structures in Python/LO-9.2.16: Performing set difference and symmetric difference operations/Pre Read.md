## Pre-Read: Set Difference and Symmetric Difference

**Duration:** 5 minutes

---

### What You'll Learn

Two powerful set operations that answer:
- **Difference** (`-`): "What's in set A that isn't in set B?"
- **Symmetric Difference** (`^`): "What's NOT shared between A and B?"

---

### Quick Preview

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Difference: in a but not b
print(a - b)  # {1, 2}

# Symmetric difference: in either but not both
print(a ^ b)  # {1, 2, 5, 6}
```

---

### Real-World Analogy

Imagine two shopping lists:
- **Your list:** milk, bread, eggs, butter
- **Partner's list:** bread, eggs, cheese, fruit

**Difference** (yours - theirs): milk, butter → items only you need
**Symmetric difference**: milk, butter, cheese, fruit → items not on both lists

---

### Key Distinction

```python
a = {1, 2, 3}
b = {2, 3, 4}

# Difference — order matters!
print(a - b)  # {1}
print(b - a)  # {4}

# Symmetric difference — order doesn't matter
print(a ^ b)  # {1, 4}
print(b ^ a)  # {1, 4}
```

---

### Try This

```python
required = {'Python', 'SQL', 'Git'}
have = {'Python', 'JavaScript', 'Git'}

missing = required - have
extra = have - required
print(f"Need: {missing}")   # ?
print(f"Bonus: {extra}")    # ?
```

**Answers:** `{'SQL'}` and `{'JavaScript'}`
