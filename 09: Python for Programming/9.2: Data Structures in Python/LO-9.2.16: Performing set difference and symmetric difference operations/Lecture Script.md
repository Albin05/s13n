## Lecture Script: Set Difference and Symmetric Difference Operations


---

### CS Theory Bite

> **Origin**: **Difference** (A - B) finds elements only in A. **Symmetric difference** (A △ B) finds elements in either but not both — the mathematical XOR operation.
>
> **Analogy**: Difference is like **"What do I have that you don't?"** Symmetric difference is **"What's unique to each of us?"**
>
> **Why it matters**: These operations compare datasets — finding new users, changed records, or exclusive items.



### Hook (2 minutes)

**Scenario:**

You're a hiring manager comparing job requirements against a candidate's resume:

```python
required = {'Python', 'SQL', 'Docker', 'AWS', 'Git'}
candidate = {'Python', 'JavaScript', 'Git', 'React', 'Node.js'}
```

How do you quickly find what skills are missing? What extra skills do they bring?

```python
missing = required - candidate
print(f"Missing: {missing}")   # {'SQL', 'Docker', 'AWS'}

bonus = candidate - required
print(f"Bonus: {bonus}")       # {'JavaScript', 'React', 'Node.js'}
```

Two lines of code. No loops, no conditionals. That's the power of set difference.

**Today:** We'll master two operations — **difference** and **symmetric difference** — that answer "what's unique to each side?"

---

### Section 1: Set Difference (3 minutes)

The difference operation returns elements in the first set that are NOT in the second.

```python
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

# Elements in a but not in b
result = a - b
print(result)  # {1, 2}

# Same using method
result = a.difference(b)
print(result)  # {1, 2}
```

**Order matters:**
```python
print(a - b)  # {1, 2} — in a, not b
print(b - a)  # {6, 7} — in b, not a
```

**Multiple sets:**
```python
a = {1, 2, 3, 4, 5, 6}
b = {2, 3}
c = {5, 6}
print(a - b - c)  # {1, 4}
```

---

### Section 2: Difference Update (2 minutes)

If you want to modify a set in place rather than creating a new one:

```python
cart = {'apple', 'banana', 'milk', 'bread', 'eggs'}
out_of_stock = {'milk', 'eggs'}

# Remove out of stock items
cart -= out_of_stock
print(cart)  # {'apple', 'banana', 'bread'}

# Same as:
# cart.difference_update(out_of_stock)
```

The original set is modified. No new set is created.

---

### Section 3: Symmetric Difference (3 minutes)

Symmetric difference returns elements in **either** set but **not in both**:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

result = a ^ b
print(result)  # {1, 2, 5, 6}
# 3, 4 are in BOTH sets — excluded
```

**Think of it as:** everything that's NOT shared.

**Order doesn't matter:**
```python
print(a ^ b)  # {1, 2, 5, 6}
print(b ^ a)  # {1, 2, 5, 6} — same!
```

**Equivalence:**
```python
# Symmetric difference equals union minus intersection
print(a ^ b)              # {1, 2, 5, 6}
print((a | b) - (a & b))  # {1, 2, 5, 6}
```

---

### Section 4: Practical Applications (3 minutes)

**Application 1: Finding Non-Respondents**
```python
all_students = {'Alice', 'Bob', 'Charlie', 'Diana', 'Eve'}
submitted = {'Alice', 'Diana', 'Eve'}

pending = all_students - submitted
print(f"Haven't submitted: {pending}")  # {'Bob', 'Charlie'}
```

**Application 2: Comparing Inventories**
```python
store_a = {'laptop', 'phone', 'tablet', 'charger'}
store_b = {'phone', 'tablet', 'headphones', 'case'}

only_a = store_a - store_b  # {'laptop', 'charger'}
only_b = store_b - store_a  # {'headphones', 'case'}
not_shared = store_a ^ store_b  # all four above
```

**Application 3: Config Changes**
```python
old_settings = {'dark_mode', 'notifications', 'auto_save'}
new_settings = {'dark_mode', 'auto_save', 'cloud_sync'}

added = new_settings - old_settings    # {'cloud_sync'}
removed = old_settings - new_settings  # {'notifications'}
changed = old_settings ^ new_settings  # {'notifications', 'cloud_sync'}
print(f"Changed settings: {changed}")
```

---

### Section 5: Key Comparisons (1 minute)

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# All four operations side by side:
print(a | b)   # {1, 2, 3, 4, 5, 6}  Union — everything
print(a & b)   # {3, 4}              Intersection — shared
print(a - b)   # {1, 2}              Difference — only in a
print(a ^ b)   # {1, 2, 5, 6}        Symmetric diff — not shared
```

---

### Summary (1 minute)

1. **Difference** (`-`): "What do I have that they don't?"
2. **Symmetric difference** (`^`): "What's different between us?"
3. Order matters for `-` but not for `^`
4. Use `_update` variants for in-place modification
5. These operations make comparison tasks clean and readable
