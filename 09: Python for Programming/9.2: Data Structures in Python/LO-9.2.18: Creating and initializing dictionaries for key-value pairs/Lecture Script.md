## Lecture Script: Creating and Initializing Dictionaries


---

### CS Theory Bite

> **Origin**: Dictionaries implement **hash maps** — the most important data structure in computing. Invented for **LISP** (1958) as association lists, evolved into O(1) hash tables. **Python 3.7+** guarantees insertion order.
>
> **Analogy**: A dictionary is like a **real dictionary** — look up a word (key) and instantly find its definition (value). No scanning page by page.
>
> **Why it matters**: Dicts are Python's Swiss Army knife — used for JSON, caching, counting, configuration, and database records.



### Hook (2 minutes)

**Scenario:**

You need to store information about a student — name, age, grade, email, courses. With lists:

```python
student = ['Alice', 22, 'A', 'alice@mail.com', ['Math', 'Physics']]
# What is student[2]? Hard to remember!
```

With a dictionary:
```python
student = {
    'name': 'Alice',
    'age': 22,
    'grade': 'A',
    'email': 'alice@mail.com',
    'courses': ['Math', 'Physics']
}
print(student['grade'])  # 'A' — clear and readable!
```

Dictionaries give your data **meaning** by labeling each value with a key.

---

### Section 1: Creating Dictionaries (3 minutes)

**Curly Braces:**
```python
person = {'name': 'Alice', 'age': 25}

# Numbers as keys
medals = {1: 'Gold', 2: 'Silver', 3: 'Bronze'}

# Empty dictionary
empty = {}
```

**`dict()` Constructor:**
```python
# Keyword arguments (keys must be valid variable names)
person = dict(name='Alice', age=25)

# From list of tuples
person = dict([('name', 'Alice'), ('age', 25)])

# From zip
keys = ['name', 'age', 'city']
vals = ['Alice', 25, 'Mumbai']
person = dict(zip(keys, vals))
```

---

### Section 2: Comprehensions and fromkeys (3 minutes)

**Dictionary Comprehension:**
```python
# Create a mapping of numbers to their squares
squares = {n: n**2 for n in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With filtering
even_sq = {n: n**2 for n in range(10) if n % 2 == 0}
```

**`fromkeys()`** — when all keys share the same initial value:
```python
subjects = dict.fromkeys(['Math', 'Science', 'English'], 0)
# {'Math': 0, 'Science': 0, 'English': 0}
```

---

### Section 3: Keys and Values Rules (3 minutes)

**Keys must be unique:**
```python
d = {'x': 1, 'y': 2, 'x': 3}
print(d)  # {'x': 3, 'y': 2} — last value wins
```

**Keys must be immutable:**
```python
ok = {'name': 1, 42: 2, (1,2): 3}  # strings, ints, tuples — fine
# bad = {[1,2]: 3}  # TypeError — lists can't be keys
```

**Values can be anything:**
```python
data = {
    'name': 'Alice',          # string
    'scores': [85, 92, 78],   # list
    'address': {'city': 'Mumbai', 'zip': '400001'},  # dict
    'active': True             # bool
}
```

---

### Section 4: Nested Dictionaries (2 minutes)

```python
company = {
    'engineering': {
        'Alice': {'role': 'Lead', 'salary': 120000},
        'Bob': {'role': 'Developer', 'salary': 95000}
    },
    'marketing': {
        'Charlie': {'role': 'Manager', 'salary': 100000}
    }
}

# Access nested values
print(company['engineering']['Alice']['role'])  # 'Lead'
```

---

### Section 5: Practical Uses (2 minutes)

**Config files:**
```python
config = dict(debug=False, port=8080, host='localhost')
```

**Counting things:**
```python
text = "apple banana apple cherry banana apple"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)  # {'apple': 3, 'banana': 2, 'cherry': 1}
```

**Mapping data:**
```python
status_codes = {200: 'OK', 404: 'Not Found', 500: 'Server Error'}
print(status_codes[404])  # 'Not Found'
```

---

### Summary (1 minute)

1. Dictionaries store **key-value pairs** — labeled, structured data
2. Create with `{}`, `dict()`, comprehensions, or `fromkeys()`
3. Keys: **unique** and **immutable** (strings, numbers, tuples)
4. Values: **any type** — including lists and nested dicts
5. Dictionaries are the backbone of structured data in Python
