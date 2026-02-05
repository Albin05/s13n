## Lecture Script: Accessing Dictionary Values

**Duration:** 15 minutes

---

### Hook (2 minutes)

Your app receives user data from an API:

```python
user_data = {'name': 'Alice', 'age': 25}
```

You try to access the email:
```python
email = user_data['email']  # CRASH! KeyError: 'email'
```

Your entire program stops because one field is missing. This happens in real applications all the time — APIs return partial data, configs are incomplete, user input varies.

The solution? `.get()` — your safety net for dictionary access.

```python
email = user_data.get('email', 'no-email@default.com')
# No crash, has a sensible default
```

---

### Section 1: Square Bracket Access (2 minutes)

```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}

# Direct access
print(student['name'])   # Alice
print(student['grade'])  # A

# KeyError if missing
# print(student['email'])  # KeyError: 'email'
```

Use `[]` when you're **certain** the key exists.

---

### Section 2: The .get() Method (3 minutes)

```python
student = {'name': 'Alice', 'age': 22}

# Returns None for missing keys
print(student.get('name'))    # Alice
print(student.get('email'))   # None

# Custom default value
print(student.get('email', 'N/A'))     # N/A
print(student.get('grade', 'Pending')) # Pending
```

**Common pattern — counting:**
```python
counts = {}
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)  # {'apple': 3, 'banana': 2, 'cherry': 1}
```

---

### Section 3: Checking Key Existence (2 minutes)

```python
data = {'x': 10, 'y': 20}

# 'in' checks keys
print('x' in data)   # True
print(10 in data)     # False — checks keys, not values!

# Pattern: check then access
if 'z' in data:
    print(data['z'])
else:
    print("z not found")
```

---

### Section 4: keys(), values(), items() (3 minutes)

```python
person = {'name': 'Alice', 'age': 25, 'city': 'Mumbai'}

# Keys
for key in person.keys():
    print(key)  # name, age, city

# Values
for val in person.values():
    print(val)  # Alice, 25, Mumbai

# Key-value pairs
for key, val in person.items():
    print(f"{key}: {val}")
```

---

### Section 5: Nested Access (2 minutes)

```python
data = {
    'user': {
        'name': 'Alice',
        'settings': {'theme': 'dark'}
    }
}

# Direct (risky)
print(data['user']['settings']['theme'])  # dark

# Safe (with .get() chain)
theme = data.get('user', {}).get('settings', {}).get('theme', 'light')
print(theme)  # dark
```

---

### Summary (1 minute)

1. `dict[key]` — fast but crashes on missing keys
2. `dict.get(key, default)` — safe, returns default for missing keys
3. `key in dict` — checks key existence
4. `.keys()`, `.values()`, `.items()` — iterate over contents
5. Chain `.get()` for safe nested access
