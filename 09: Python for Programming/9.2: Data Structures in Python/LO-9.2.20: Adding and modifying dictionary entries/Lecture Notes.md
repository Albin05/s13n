## Lecture Notes: Adding and Modifying Dictionary Entries


---

## Introduction

Dictionary modification demonstrates **mutable mapping** design - the same operation (`dict[key] = value`) can both add AND modify, making it **context-sensitive**. This represents **upsert semantics**: update if exists, insert if new - a fundamental database concept!

---

<div align="center">

![Python Dictionary Add Update Key Value Pair](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.2/LO-9.2.20.png)

*dict[key] = value performs an upsert: if the key exists, its value is updated; if not, a new entry is inserted*

</div>

---

### Why Unified Add/Modify Syntax is Elegant

**Traditional approach** (separate operations): Different syntax for add vs modify:
```c
// C/Java - verbose!
if (map.containsKey("age")) {
    map.put("age", 23);  // Modify existing
} else {
    map.put("age", 23);  // Add new
}
// Same code repeated! Needless complexity.
```

**Python's approach** (unified): One syntax for both:
```python
student['age'] = 23  # Add OR modify - don't care!
# Simple, clean, no if-check needed!
```

**This is "upsert"** (UPDATE or INSERT) - databases use this pattern! MongoDB's `upsert`, SQL's `INSERT ON DUPLICATE KEY UPDATE` - Python dictionaries had it from day 1 (1991)!

### Real-World Analogies

**Dict modification like updating contacts**:
- **Add new contact**: Save "Bob" → 555-1234
- **Update existing**: "Bob" already exists? Replace with new number
- **Same button**: Phone doesn't ask "add or update?" - just saves!
- **Python dict**: Same syntax for both operations

**Or like whiteboard**:
- **Write "Score: 10"**: First time - creates entry
- **Write "Score: 20"**: Erase old, write new - updates
- **Same action**: Writing on whiteboard - adds or overwrites naturally

**Or like variable assignment**:
```python
x = 10  # First time - creates variable
x = 20  # Next time - updates variable
# Dict operations work the SAME way!
```

### The `setdefault()` Design Genius

**Problem**: Want to initialize if missing, keep if exists:
```python
# Verbose approach:
if 'count' not in data:
    data['count'] = 0
# Now use data['count']
```

**Elegant solution**:
```python
data.setdefault('count', 0)  # Initialize only if new!
# One line, returns the value, perfect!
```

**Why brilliant**: Combines **check + set + get** in one atomic operation. Used constantly for grouping/accumulation patterns!

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
