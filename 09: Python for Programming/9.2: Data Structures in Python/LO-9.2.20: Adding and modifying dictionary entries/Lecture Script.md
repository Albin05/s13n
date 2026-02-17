## Lecture Script: Adding and Modifying Dictionary Entries


---

### CS Theory Bite

> **Origin**: Dict insertion and update are both O(1) average. Python dicts use **dynamic resizing** — when the **load factor** exceeds ~2/3, the hash table doubles in size and rehashes all entries.
>
> **Analogy**: Adding to a dict is like **filing a document** — place it in the right folder (hash bucket). Updating is like **replacing the document** in the same folder.
>
> **Why it matters**: Dicts are mutable by design — build them incrementally as data arrives.



### Hook (2 minutes)

You're building a user registration system. Users fill out a form step by step:

```python
user = {}
user['name'] = 'Alice'          # Step 1
user['email'] = 'alice@mail.com' # Step 2
user['plan'] = 'free'           # Step 3

# User upgrades their plan
user['plan'] = 'premium'        # Overwrite!
```

Dictionaries grow and change — just like real data. Today we learn every way to add and modify entries.

---

### Section 1: Basic Assignment (2 minutes)

```python
d = {'a': 1}

# Add new key
d['b'] = 2
print(d)  # {'a': 1, 'b': 2}

# Modify existing key
d['a'] = 10
print(d)  # {'a': 10, 'b': 2}
```

Same syntax for both — Python decides based on whether the key exists.

---

### Section 2: update() (3 minutes)

```python
user = {'name': 'Alice'}

# Add/modify multiple at once
user.update({'age': 25, 'city': 'Mumbai', 'name': 'Alice B.'})
print(user)  # {'name': 'Alice B.', 'age': 25, 'city': 'Mumbai'}

# With keyword arguments
user.update(email='alice@mail.com')
```

`update()` is like batch processing — one call, many changes.

---

### Section 3: setdefault() (3 minutes)

"Set this value, but ONLY if the key doesn't exist yet."

```python
config = {'port': 8080}

config.setdefault('port', 3000)    # Key exists — no change
config.setdefault('host', 'localhost')  # Key missing — sets it

print(config)  # {'port': 8080, 'host': 'localhost'}
```

**Killer use case — grouping:**
```python
words = ['apple', 'ant', 'banana', 'avocado', 'berry']
groups = {}

for word in words:
    groups.setdefault(word[0], []).append(word)

print(groups)
# {'a': ['apple', 'ant', 'avocado'], 'b': ['banana', 'berry']}
```

---

### Section 4: Counter Pattern (3 minutes)

The most common dict modification pattern:

```python
text = "the cat sat on the mat"
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1
print(counts)  # {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
```

Also works for accumulating totals:
```python
sales = {}
data = [('Alice', 100), ('Bob', 200), ('Alice', 50)]
for name, amount in data:
    sales[name] = sales.get(name, 0) + amount
print(sales)  # {'Alice': 150, 'Bob': 200}
```

---

### Section 5: Merging Dicts (1 minute)

```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

# Unpacking (creates new dict)
merged = {**d1, **d2}
print(merged)  # {'a': 1, 'b': 3, 'c': 4}

# |= operator (modifies in place, Python 3.9+)
d1 |= d2
print(d1)  # {'a': 1, 'b': 3, 'c': 4}
```

---

### Summary (1 minute)

1. `d[key] = value` — add or overwrite one entry
2. `d.update(...)` — add/overwrite multiple at once
3. `d.setdefault(key, val)` — set only if key is new
4. `.get(key, 0) + 1` — the counter pattern
5. `{**d1, **d2}` — merge dicts (last wins)
