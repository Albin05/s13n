## Pre-Read: Checking for Key Existence

**Duration:** 5 minutes

---

### The `in` Keyword

```python
data = {'name': 'Alice', 'age': 25}

print('name' in data)   # True — key exists
print('email' in data)  # False — key doesn't exist
```

---

### Keys vs Values

```python
# 'in' checks KEYS, not values
print('Alice' in data)          # False — Alice is a value
print('Alice' in data.values()) # True — check values explicitly
```

---

### Why It Matters

```python
data = {'x': 10}

# Without checking:
# print(data['y'])  # KeyError — crash!

# With checking:
if 'y' in data:
    print(data['y'])
else:
    print("Not found")
```

---

### Try This

```python
config = {'debug': True, 'port': 8080}
print('debug' in config)    # ?
print(True in config)       # ?
print('host' not in config) # ?
```

**Answers:** `True`, `False`, `True`
