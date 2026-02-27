## Lecture Notes: Checking for Key Existence Using the 'in' Keyword


---

## Introduction

The `in` operator provides **O(1) membership testing** for dictionaries - same hash table magic as sets! This enables **defensive programming**: check before access to prevent crashes. It's the **look before you leap (LBYL)** approach vs. Python's preferred **easier to ask forgiveness (EAFP)** with try-except.

---

<div align="center">

![Python Dictionary Key Existence Check](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.2/LO-9.2.22.jpg)

*The `in` keyword uses hash lookup — O(1) for dicts/sets vs O(n) for lists, making it ideal for membership checks*

</div>

---

### Why Key Checking Matters

**LBYL** (Look Before You Leap): Check first, act second
```python
if key in dict:  # Check
    value = dict[key]  # Act
```

**EAFP** (Easier to Ask Forgiveness than Permission): Try, catch errors
```python
try:
    value = dict[key]  # Act
except KeyError:  # Handle failure
    value = default
```

**Python prefers EAFP**, but `in` is cleaner for simple existence checks!

---

### The `in` Operator for Dictionaries

```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}

print('name' in student)    # True
print('email' in student)   # False
print('email' not in student)  # True
```

**Important:** `in` checks **keys**, not values.

```python
print('Alice' in student)  # False — 'Alice' is a value, not a key
print('name' in student)   # True — 'name' is a key
```

---

### Why Check for Keys?

Without checking, accessing a missing key crashes your program:

```python
data = {'x': 10}

# DANGEROUS
# print(data['y'])  # KeyError!

# SAFE — check first
if 'y' in data:
    print(data['y'])
else:
    print("Key 'y' not found")
```

---

### `in` vs `.get()` vs `try/except`

Three approaches to handle missing keys:

**Approach 1: `in` check**
```python
if 'email' in user:
    email = user['email']
else:
    email = 'N/A'
```

**Approach 2: `.get()` with default**
```python
email = user.get('email', 'N/A')
```

**Approach 3: `try/except`**
```python
try:
    email = user['email']
except KeyError:
    email = 'N/A'
```

**When to use which:**
- `in` — when you need different logic based on existence
- `.get()` — when you just need a value with a fallback
- `try/except` — when KeyError is rare (follows EAFP principle)

---

### Checking Keys in Nested Dicts

```python
data = {
    'user': {
        'name': 'Alice',
        'settings': {'theme': 'dark'}
    }
}

# Check at each level
if 'user' in data:
    if 'settings' in data['user']:
        if 'theme' in data['user']['settings']:
            print(data['user']['settings']['theme'])
```

**Cleaner with `.get()`:**
```python
theme = data.get('user', {}).get('settings', {}).get('theme', 'light')
print(theme)  # 'dark'
```

---

### Checking Values (Not Keys)

To check if a **value** exists:

```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}

# Check in values
print('Alice' in student.values())  # True
print(22 in student.values())       # True
print('B' in student.values())      # False
```

---

### Common Patterns

**1. Conditional Update:**
```python
config = {'port': 8080}

if 'host' not in config:
    config['host'] = 'localhost'
```

**2. Counting (check-and-increment):**
```python
text = "hello world hello"
counts = {}
for word in text.split():
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)  # {'hello': 2, 'world': 1}
```

**3. Grouping:**
```python
students = [('Alice', 'Math'), ('Bob', 'Science'), ('Alice', 'Science')]
groups = {}
for name, subject in students:
    if name not in groups:
        groups[name] = []
    groups[name].append(subject)
print(groups)  # {'Alice': ['Math', 'Science'], 'Bob': ['Science']}
```

**4. Avoid Duplicates:**
```python
seen = {}
items = [('a', 1), ('b', 2), ('a', 3)]
for key, val in items:
    if key not in seen:
        seen[key] = val  # Keep first occurrence only
print(seen)  # {'a': 1, 'b': 2}
```

**5. Required Fields Validation:**
```python
required = {'name', 'email', 'password'}
form_data = {'name': 'Alice', 'email': 'alice@mail.com'}

missing = [field for field in required if field not in form_data]
if missing:
    print(f"Missing fields: {missing}")
else:
    print("All fields present!")
# Missing fields: ['password']
```

---

### Performance

Key lookup with `in` is **O(1)** on average — just like sets. This is because dictionaries use hash tables internally.

```python
# Fast even for large dicts
big_dict = {i: i**2 for i in range(1_000_000)}
999_999 in big_dict  # Instant!
```

---

### Key Takeaways

1. `key in dict` checks if a **key** exists — O(1) operation
2. `in` does NOT check values — use `val in dict.values()` for that
3. Use `in` when you need conditional logic based on key existence
4. Use `.get()` when you just need a fallback value
5. Always check before `del` or `[]` access to avoid `KeyError`
