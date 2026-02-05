## Lecture Script: Iterating Through Dictionaries

**Duration:** 15 minutes

---

### Hook (2 minutes)

You have student grades and need to:
- Print a report card
- Calculate averages
- Find the top student

All of this requires **iterating** through the dictionary:

```python
grades = {'Alice': 92, 'Bob': 78, 'Charlie': 85}

for name, score in grades.items():
    status = 'Pass' if score >= 80 else 'Needs work'
    print(f"{name}: {score} - {status}")
```

Three lines, full report. Let's learn every way to loop through dictionaries.

---

### Section 1: Iterating Keys (2 minutes)

```python
data = {'a': 1, 'b': 2, 'c': 3}

# Default — iterates keys
for key in data:
    print(key, data[key])

# Explicit — same result
for key in data.keys():
    print(key, data[key])
```

---

### Section 2: Iterating Values (2 minutes)

```python
prices = {'apple': 1.50, 'banana': 0.75, 'cherry': 3.00}

# Sum all prices
total = sum(prices.values())
print(f"Total: ${total}")

# Find average
avg = sum(prices.values()) / len(prices)
```

---

### Section 3: Iterating Items (3 minutes)

```python
user = {'name': 'Alice', 'age': 25, 'city': 'Mumbai'}

for key, val in user.items():
    print(f"{key}: {val}")
```

**Nested dicts:**
```python
grades = {
    'Alice': {'Math': 92, 'Science': 88},
    'Bob': {'Math': 78, 'Science': 85}
}

for student, subjects in grades.items():
    avg = sum(subjects.values()) / len(subjects)
    print(f"{student}: avg = {avg}")
```

---

### Section 4: Sorting and Filtering (3 minutes)

**Sorted by key:**
```python
for k in sorted(data):
    print(k, data[k])
```

**Sorted by value:**
```python
scores = {'Alice': 92, 'Bob': 78, 'Charlie': 85}
for name in sorted(scores, key=scores.get, reverse=True):
    print(f"{name}: {scores[name]}")
```

**Filtering with comprehension:**
```python
passing = {n: s for n, s in scores.items() if s >= 80}
```

---

### Section 5: Common Patterns (2 minutes)

**Find max/min:**
```python
top = max(scores, key=scores.get)
```

**Group by value:**
```python
groups = {}
for name, grade in students.items():
    groups.setdefault(grade, []).append(name)
```

**Invert dict:**
```python
inverted = {v: k for k, v in original.items()}
```

---

### Summary (1 minute)

1. `for key in dict` — keys
2. `for val in dict.values()` — values
3. `for k, v in dict.items()` — pairs (most useful)
4. Use `sorted()` for ordered iteration
5. Comprehensions for filtering and transforming
