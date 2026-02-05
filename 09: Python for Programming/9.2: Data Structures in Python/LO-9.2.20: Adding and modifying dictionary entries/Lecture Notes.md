## Lecture Notes: Adding and Modifying Dictionary Entries

**Duration:** 10 minutes

---

### Adding New Key-Value Pairs

Simply assign a value to a new key:

```python
student = {'name': 'Alice', 'age': 22}

student['grade'] = 'A'
student['email'] = 'alice@mail.com'

print(student)
# {'name': 'Alice', 'age': 22, 'grade': 'A', 'email': 'alice@mail.com'}
```

---

### Modifying Existing Values

Same syntax — if the key exists, the value is overwritten:

```python
student = {'name': 'Alice', 'age': 22, 'grade': 'B'}

student['grade'] = 'A'  # Update grade
student['age'] = 23      # Update age

print(student)  # {'name': 'Alice', 'age': 23, 'grade': 'A'}
```

---

### The `update()` Method

Add or modify **multiple** entries at once:

```python
student = {'name': 'Alice', 'age': 22}

# Update with another dictionary
student.update({'age': 23, 'grade': 'A', 'city': 'Mumbai'})
print(student)
# {'name': 'Alice', 'age': 23, 'grade': 'A', 'city': 'Mumbai'}

# Update with keyword arguments
student.update(email='alice@mail.com', phone='9876543210')
print(student)
```

**Behavior:**
- Existing keys → values are **overwritten**
- New keys → entries are **added**

---

### The `setdefault()` Method

Sets a value **only if the key doesn't already exist**:

```python
config = {'theme': 'dark'}

# Key exists — no change
config.setdefault('theme', 'light')
print(config['theme'])  # 'dark' — unchanged!

# Key doesn't exist — sets it
config.setdefault('language', 'en')
print(config['language'])  # 'en' — newly added
```

**Useful for initialization:**
```python
word_groups = {}
words = ['apple', 'ant', 'banana', 'avocado', 'berry']

for word in words:
    first_letter = word[0]
    word_groups.setdefault(first_letter, []).append(word)

print(word_groups)
# {'a': ['apple', 'ant', 'avocado'], 'b': ['banana', 'berry']}
```

---

### The `|=` Operator (Python 3.9+)

Merge another dictionary into the current one:

```python
defaults = {'theme': 'light', 'lang': 'en', 'font': 14}
user_prefs = {'theme': 'dark', 'font': 16}

defaults |= user_prefs
print(defaults)  # {'theme': 'dark', 'lang': 'en', 'font': 16}
```

---

### Incrementing Values

A common pattern for counters:

```python
# Count character occurrences
text = "hello"
counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1
print(counts)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

---

### Practical Examples

**1. Building a Profile Step by Step:**
```python
profile = {}
profile['name'] = input("Name: ")
profile['age'] = int(input("Age: "))
profile['skills'] = []
profile['skills'].append('Python')
profile['skills'].append('SQL')
```

**2. Merging Configurations:**
```python
default_config = {'debug': False, 'port': 3000, 'host': 'localhost'}
env_config = {'debug': True, 'port': 8080}

final = {**default_config, **env_config}  # env overrides defaults
print(final)  # {'debug': True, 'port': 8080, 'host': 'localhost'}
```

**3. Accumulating Data:**
```python
sales = {}
transactions = [('Alice', 100), ('Bob', 200), ('Alice', 150), ('Bob', 50)]

for name, amount in transactions:
    sales[name] = sales.get(name, 0) + amount

print(sales)  # {'Alice': 250, 'Bob': 250}
```

---

### Summary Table

| Method | Adds New? | Overwrites? | Multiple? |
|--------|-----------|-------------|-----------|
| `d[key] = val` | Yes | Yes | No |
| `d.update(...)` | Yes | Yes | Yes |
| `d.setdefault(key, val)` | Yes | **No** | No |
| `d \|= other` | Yes | Yes | Yes |

---

### Key Takeaways

1. `dict[key] = value` — adds or overwrites a single entry
2. `dict.update()` — adds/overwrites multiple entries at once
3. `dict.setdefault()` — only sets if key is missing (safe initialization)
4. Use `.get()` with increment for counting patterns
5. Use `{**d1, **d2}` or `|=` for merging dictionaries
