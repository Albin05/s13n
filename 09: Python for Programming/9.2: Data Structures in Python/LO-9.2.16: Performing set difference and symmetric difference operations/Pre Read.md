## Pre-Read: Set Difference and Symmetric Difference

**Duration:** 5 minutes

---

## What Are These Operations?

These are Python's **"what's missing?"** and **"what's different?"** operations - like finding gaps in your knowledge or disagreements between two lists!

### Simple Analogies

**Difference (A - B) like comparing checklists**:
- **Your packing list**: Clothes, Laptop, Charger, Book
- **Friend's packing list**: Laptop, Charger, Snacks, Camera
- **Just yours (You - Friend)**: Clothes, Book
- **Just theirs (Friend - You)**: Snacks, Camera
- **Key point**: ORDER MATTERS! (A - B) ≠ (B - A)

**Symmetric difference (A ^ B) like "total disagreements"**:
- **Team A wants**: Pizza, Burgers, Tacos
- **Team B wants**: Burgers, Tacos, Sushi
- **Everyone agrees**: Burgers, Tacos (intersection)
- **Disagreements (A ^ B)**: Pizza, Sushi (symmetric diff!)
- **Meaning**: Items where teams DON'T agree

### The "Subtraction" vs "XOR" Mental Model

**Difference is like SUBTRACTION**:
```python
my_cart = {'shirt', 'pants', 'shoes', 'hat'}
remove_these = {'shoes', 'hat'}
final_cart = my_cart - remove_these
# Result: {'shirt', 'pants'} - subtraction!
```

**Symmetric difference is like LIGHT SWITCH XOR**:
```python
yesterday = {'task_a', 'task_b', 'task_c'}
today = {'task_b', 'task_c', 'task_d'}
changed = yesterday ^ today
# Result: {'task_a', 'task_d'} - what changed!
```

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
