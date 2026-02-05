## Pre-Read: Accessing Dictionary Values

**Duration:** 5 minutes

---

### Two Ways to Access Values

```python
student = {'name': 'Alice', 'age': 22}

# Way 1: Square brackets — errors if key missing
print(student['name'])  # Alice

# Way 2: .get() — returns None if key missing
print(student.get('name'))    # Alice
print(student.get('email'))   # None (no error!)
print(student.get('email', 'N/A'))  # N/A (custom default)
```

---

### The Problem with `[]`

```python
data = {'x': 10}
# print(data['y'])  # KeyError: 'y' — CRASH!
```

---

### The Solution: `.get()`

```python
data = {'x': 10}
print(data.get('y', 0))  # 0 — safe!
```

---

### Quick Exercise

```python
config = {'port': 8080}

# What does each print?
print(config.get('port', 3000))     # ?
print(config.get('host', 'localhost'))  # ?
```

**Answers:** `8080` (key exists, uses actual value), `localhost` (key missing, uses default)
