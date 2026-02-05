## Lecture Notes: Creating and Initializing Dictionaries for Key-Value Pairs

**Duration:** 12 minutes

---

### What Is a Dictionary?

A **dictionary** stores data as **key-value pairs**. Think of it like a real dictionary: you look up a word (key) to find its definition (value).

```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}
print(student)
# {'name': 'Alice', 'age': 22, 'grade': 'A'}
```

**Key Properties:**
1. **Key-value pairs** — every entry has a key and a value
2. **Keys must be unique** — no duplicate keys
3. **Keys must be immutable** — strings, numbers, tuples
4. **Values can be anything** — strings, lists, other dicts, etc.
5. **Ordered** (Python 3.7+) — insertion order is preserved

---

### Creating Dictionaries

**Method 1: Curly Braces (Most Common)**
```python
person = {'name': 'Alice', 'age': 25, 'city': 'Mumbai'}

# Numbers as keys
scores = {1: 'Gold', 2: 'Silver', 3: 'Bronze'}

# Mixed key types
data = {'name': 'Bob', 1: 'first', (0, 0): 'origin'}
```

**Method 2: `dict()` Constructor**
```python
# From keyword arguments
person = dict(name='Alice', age=25, city='Mumbai')

# From list of tuples
pairs = [('name', 'Alice'), ('age', 25), ('city', 'Mumbai')]
person = dict(pairs)

# From zip
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'Mumbai']
person = dict(zip(keys, values))
```

**Method 3: Empty Dictionary**
```python
empty = {}          # curly braces
empty = dict()      # constructor
print(type(empty))  # <class 'dict'>
```

---

### Dictionary Comprehension

Create dictionaries using a compact expression:

```python
# Squares of numbers
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# From two lists
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 22]
people = {name: age for name, age in zip(names, ages)}
print(people)  # {'Alice': 25, 'Bob': 30, 'Charlie': 22}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

---

### `dict.fromkeys()` — Same Value for Multiple Keys

```python
# Initialize with default value
subjects = dict.fromkeys(['Math', 'Science', 'English'], 0)
print(subjects)  # {'Math': 0, 'Science': 0, 'English': 0}

# Default is None if not specified
fields = dict.fromkeys(['name', 'age', 'email'])
print(fields)  # {'name': None, 'age': None, 'email': None}
```

---

### Keys Must Be Unique

If you use the same key twice, the last value wins:

```python
data = {'a': 1, 'b': 2, 'a': 3}
print(data)  # {'a': 3, 'b': 2}
# The first 'a': 1 is overwritten
```

---

### What Can Be Keys?

**Valid keys (immutable):**
```python
d = {
    'name': 'Alice',      # string
    42: 'answer',          # int
    3.14: 'pi',            # float
    (1, 2): 'coordinates', # tuple
    True: 'yes',           # bool
}
```

**Invalid keys (mutable):**
```python
# d = {[1, 2]: 'list'}    # TypeError — lists are mutable
# d = {{1}: 'set'}        # TypeError — sets are mutable
```

---

### Nested Dictionaries

Dictionaries can contain other dictionaries:

```python
students = {
    'Alice': {'age': 22, 'grade': 'A', 'courses': ['Math', 'Physics']},
    'Bob': {'age': 24, 'grade': 'B', 'courses': ['Chemistry', 'Biology']}
}

print(students['Alice']['grade'])      # 'A'
print(students['Bob']['courses'][0])   # 'Chemistry'
```

---

### Practical Examples

**1. Configuration Settings:**
```python
config = {
    'debug': False,
    'database': 'postgresql',
    'port': 5432,
    'max_connections': 100
}
```

**2. Word Frequency Counter:**
```python
text = "the cat sat on the mat the cat"
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)  # {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}
```

**3. Student Records:**
```python
student = dict.fromkeys(['name', 'age', 'email', 'grade'], '')
student['name'] = 'Alice'
student['age'] = 22
print(student)
```

---

### Quick Reference

| Method | Example | Result |
|--------|---------|--------|
| Literal | `{'a': 1, 'b': 2}` | Dict with 2 pairs |
| `dict()` | `dict(a=1, b=2)` | Same as above |
| From tuples | `dict([('a',1), ('b',2)])` | Same as above |
| From zip | `dict(zip(keys, vals))` | Zipped pairs |
| Comprehension | `{x: x**2 for x in range(3)}` | `{0:0, 1:1, 2:4}` |
| `fromkeys()` | `dict.fromkeys(['a','b'], 0)` | `{'a':0, 'b':0}` |
| Empty | `{}` or `dict()` | Empty dict |

---

### Key Takeaways

1. Dictionaries store **key-value pairs** for structured data
2. Multiple creation methods: `{}`, `dict()`, comprehensions, `fromkeys()`
3. Keys must be **unique** and **immutable**
4. Values can be **any type** including lists and other dicts
5. Order is **preserved** (Python 3.7+)
6. Perfect for **structured data**, **lookups**, and **configurations**
