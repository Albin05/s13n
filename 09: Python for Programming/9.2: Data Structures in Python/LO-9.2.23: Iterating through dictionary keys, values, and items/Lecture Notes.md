## Lecture Notes: Iterating Through Dictionary Keys, Values, and Items


---

## Introduction

Dictionary iteration offers **three views** - keys, values, or items (pairs) - representing different **perspectives on the same data**. This demonstrates **dictionary views**: efficient, dynamic representations that update with the dictionary. They're **not copies** - they're **live views** into the dictionary's current state!

### Why Three Iteration Methods?

**Keys only** (.keys() or default): When you just need identifiers
**Values only** (.values()): When you need to aggregate/analyze data
**Key-value pairs** (.items()): When you need context for each value

**All are O(n)** but with different overhead - choose based on what you actually need!

### Dictionary Views Are Live!

**Amazing property**: Views update automatically:
```python
d = {'a': 1}
view = d.items()
d['b'] = 2  # Add new item
# view now shows both items - it's LIVE!
```

**This is lazy evaluation** - no copying, just pointers!

---

### Three Ways to Iterate

```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}
```

**1. Iterate over keys (default):**
```python
for key in student:
    print(key)
# name
# age
# grade
```

**2. Iterate over values:**
```python
for value in student.values():
    print(value)
# Alice
# 22
# A
```

**3. Iterate over key-value pairs:**
```python
for key, value in student.items():
    print(f"{key}: {value}")
# name: Alice
# age: 22
# grade: A
```

---

### `.keys()` — All Keys

```python
student = {'name': 'Alice', 'age': 22, 'grade': 'A'}

keys = student.keys()
print(keys)       # dict_keys(['name', 'age', 'grade'])
print(list(keys)) # ['name', 'age', 'grade']

# Iterate
for key in student.keys():
    print(key, '->', student[key])
```

**Note:** `for key in dict` and `for key in dict.keys()` are identical.

---

### `.values()` — All Values

```python
prices = {'apple': 1.50, 'banana': 0.75, 'cherry': 3.00}

# Sum all values
total = sum(prices.values())
print(f"Total: ${total:.2f}")  # Total: $5.25

# Find max value
most_expensive = max(prices.values())
print(f"Max price: ${most_expensive}")  # $3.00
```

---

### `.items()` — Key-Value Pairs

```python
scores = {'Alice': 92, 'Bob': 78, 'Charlie': 85}

# Unpack into key and value
for name, score in scores.items():
    if score >= 80:
        print(f"{name}: Pass ({score})")
    else:
        print(f"{name}: Needs improvement ({score})")
```

---

### Iterating Over Nested Dictionaries

```python
grades = {
    'Alice': {'Math': 92, 'Science': 88},
    'Bob': {'Math': 78, 'Science': 85}
}

for student, subjects in grades.items():
    print(f"\n{student}:")
    for subject, score in subjects.items():
        print(f"  {subject}: {score}")
```

Output:
```
Alice:
  Math: 92
  Science: 88

Bob:
  Math: 78
  Science: 85
```

---

### Building New Dicts While Iterating

**Filtering:**
```python
scores = {'Alice': 92, 'Bob': 45, 'Charlie': 78, 'Diana': 38}

passing = {name: score for name, score in scores.items() if score >= 50}
print(passing)  # {'Alice': 92, 'Charlie': 78}
```

**Transforming:**
```python
prices = {'apple': 1.50, 'banana': 0.75, 'cherry': 3.00}

# Apply 10% discount
discounted = {item: round(price * 0.9, 2) for item, price in prices.items()}
print(discounted)  # {'apple': 1.35, 'banana': 0.68, 'cherry': 2.7}
```

**Inverting (swap keys and values):**
```python
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}
```

---

### Sorted Iteration

Dictionaries preserve insertion order, but you can iterate in sorted order:

```python
data = {'banana': 3, 'apple': 5, 'cherry': 1}

# Sort by key
for key in sorted(data):
    print(f"{key}: {data[key]}")

# Sort by value
for key in sorted(data, key=data.get):
    print(f"{key}: {data[key]}")

# Sort by value (descending)
for key in sorted(data, key=data.get, reverse=True):
    print(f"{key}: {data[key]}")
```

---

### Common Patterns

**1. Find Key with Max/Min Value:**
```python
scores = {'Alice': 92, 'Bob': 78, 'Charlie': 85}

top = max(scores, key=scores.get)
bottom = min(scores, key=scores.get)
print(f"Top: {top}, Bottom: {bottom}")
```

**2. Group Items by Value:**
```python
students = {'Alice': 'A', 'Bob': 'B', 'Charlie': 'A', 'Diana': 'B', 'Eve': 'A'}
groups = {}
for name, grade in students.items():
    groups.setdefault(grade, []).append(name)
print(groups)  # {'A': ['Alice', 'Charlie', 'Eve'], 'B': ['Bob', 'Diana']}
```

**3. Enumerate Dict Items:**
```python
colors = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}
for i, (name, code) in enumerate(colors.items(), 1):
    print(f"{i}. {name}: {code}")
```

---

### Key Takeaways

1. `for key in dict` — iterates over keys (most common)
2. `for val in dict.values()` — iterates over values only
3. `for key, val in dict.items()` — iterates over pairs (most flexible)
4. Use comprehensions to filter/transform while iterating
5. Use `sorted()` for ordered iteration
6. Never modify a dict while iterating over it — build a new one instead
