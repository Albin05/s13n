## Lecture Notes: Accessing Dictionary Values Using Keys and get() Method


---

## Introduction

The `[]` vs `.get()` choice revisits **fail-fast vs. fail-safe** design - same philosophy as `remove()` vs `discard()` for sets! This represents different **error handling strategies**: crash loudly to catch bugs, or continue gracefully for robustness.

### Why Two Access Methods? Design Philosophy

**Why not just one?** Python provides both because **different contexts need different behaviors**:

**`dict[key]` = Fail-Fast:**
- "This key MUST exist!"
- Missing key → **crash with KeyError**
- **Use during development**: Catch bugs immediately
- **Database analogy**: Foreign key constraint - enforces data integrity

**`dict.get(key, default)` = Fail-Safe:**
- "This key might not exist, have a fallback"
- Missing key → **return default value**
- **Use in production**: Graceful degradation
- **Web server analogy**: Return 404 page instead of crashing

**Design wisdom**: One language, two philosophies - use the right tool for the context!

### Real-World Analogies

**`[]` like strict vending machine**:
- **Press A5**: "A5 exists? Dispense!"
- **Press Z9**: "Z9 doesn't exist? ERROR! Shut down!" 💥
- **Strict**: Forces you to know what buttons exist
- **Good for**: Catching configuration errors in development

**`.get()` like friendly assistant**:
- **Ask for A5**: "Here's your snack!"
- **Ask for Z9**: "Sorry, don't have that. Want the default instead?"
- **Graceful**: Provides fallback automatically
- **Good for**: User-facing features in production

**Or `[]` like password check**:
- **Correct password**: Access granted
- **Wrong password**: "Access denied!" (error)
- **No fallback**: Security requires exactness

**`.get()` like settings with defaults**:
- **Setting exists**: Use that value
- **Setting missing**: Use default value
- **Fallback**: System works either way

### The Graceful Degradation Pattern

**Problem without `.get()`** (fragile code):
```python
config = {'theme': 'dark'}

# Attempt 1: Crashes!
font_size = config['font_size']  # KeyError!

# Attempt 2: Verbose!
if 'font_size' in config:
    font_size = config['font_size']
else:
    font_size = 14  # default
# Too much code for simple fallback!
```

**Solution with `.get()`** (elegant code):
```python
config = {'theme': 'dark'}

font_size = config.get('font_size', 14)
# One line! Missing key? Use 14. Beautiful!
```

**This is "graceful degradation"** - system works even with missing data!

### The Word Counting Pattern

**Why `.get()` is perfect for counting**:

**Traditional approach** (complicated):
```python
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
# 5 lines just to count!
```

**With `.get()`** (elegant):
```python
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
# 2 lines! .get(word, 0) returns 0 if new word
```

**Even better** (Counter):
```python
from collections import Counter
word_count = Counter(words)
# But understanding .get() helps you understand Counter!
```

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
