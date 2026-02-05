## Lecture Notes: Accessing Dictionary Values Using Keys and get() Method

**Duration:** 10 minutes

---

### Accessing with Square Brackets `[]`

```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}

print(student['name'])   # Alice
print(student['age'])    # 22
print(student['grade'])  # A
```

**If the key doesn't exist:**
```python
# print(student['email'])  # KeyError: 'email'
```

This crashes your program!

---

### Accessing with `.get()` — Safe Access

```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}

print(student.get('name'))    # Alice
print(student.get('email'))   # None — no crash!
print(student.get('email', 'not set'))  # 'not set' — custom default
```

**`.get(key, default)` returns:**
- The value if key exists
- `default` if key doesn't exist (defaults to `None`)

---

### When to Use `[]` vs `.get()`

| Situation | Use | Why |
|-----------|-----|-----|
| Key is guaranteed to exist | `dict[key]` | Clear, direct |
| Key might not exist | `dict.get(key)` | Avoids KeyError |
| Need a fallback value | `dict.get(key, default)` | Clean default handling |

```python
config = {'theme': 'dark', 'language': 'en'}

# Key exists — both work
print(config['theme'])         # 'dark'
print(config.get('theme'))     # 'dark'

# Key missing — different behavior
# print(config['font_size'])   # KeyError!
print(config.get('font_size', 14))  # 14
```

---

### Accessing All Keys, Values, and Items

```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}

# All keys
print(student.keys())    # dict_keys(['name', 'age', 'grade'])

# All values
print(student.values())  # dict_values(['Alice', 22, 'A'])

# All key-value pairs
print(student.items())   # dict_items([('name', 'Alice'), ('age', 22), ('grade', 'A')])
```

Convert to lists if needed:
```python
key_list = list(student.keys())
print(key_list)  # ['name', 'age', 'grade']
```

---

### Checking if a Key Exists

```python
student = {'name': 'Alice', 'age': 22}

# Using 'in'
if 'name' in student:
    print(student['name'])

# Check before access (pattern)
key = 'email'
if key in student:
    print(student[key])
else:
    print(f"'{key}' not found")
```

**Note:** `in` checks **keys**, not values:
```python
print('Alice' in student)  # False — checks keys, not values
print('name' in student)   # True
```

---

### Accessing Nested Dictionaries

```python
data = {
    'user': {
        'name': 'Alice',
        'address': {
            'city': 'Mumbai',
            'zip': '400001'
        }
    }
}

# Chain access
print(data['user']['name'])            # Alice
print(data['user']['address']['city']) # Mumbai
```

**Safe nested access:**
```python
# Using .get() chaining
city = data.get('user', {}).get('address', {}).get('city', 'Unknown')
print(city)  # Mumbai

# If path doesn't exist
phone = data.get('user', {}).get('phone', {}).get('number', 'N/A')
print(phone)  # N/A
```

---

### Practical Examples

**1. User Profile with Defaults:**
```python
profile = {'name': 'Alice', 'theme': 'dark'}

name = profile.get('name', 'Guest')
theme = profile.get('theme', 'light')
lang = profile.get('language', 'en')

print(f"Welcome {name}! Theme: {theme}, Language: {lang}")
# Welcome Alice! Theme: dark, Language: en
```

**2. Counting with `.get()`:**
```python
text = "hello world hello python hello"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)  # {'hello': 3, 'world': 1, 'python': 1}
```

**3. Configuration with Fallbacks:**
```python
config = {'port': 8080, 'debug': True}

host = config.get('host', 'localhost')
port = config.get('port', 3000)
debug = config.get('debug', False)
print(f"{host}:{port} (debug={debug})")
# localhost:8080 (debug=True)
```

---

### Key Takeaways

1. `dict[key]` — direct access, raises `KeyError` if key missing
2. `dict.get(key)` — safe access, returns `None` if key missing
3. `dict.get(key, default)` — safe access with custom fallback
4. Use `in` to check if a **key** exists before accessing
5. `.keys()`, `.values()`, `.items()` give views of dictionary contents
6. Chain `.get()` for safe nested dictionary access
