## Pre-Read: Adding and Modifying Dictionary Entries

**Duration:** 5 minutes

---

### Adding to a Dictionary

```python
person = {'name': 'Alice'}
person['age'] = 25        # Add new key
person['name'] = 'Alice B.'  # Modify existing key
```

---

### Multiple Updates

```python
person.update({'city': 'Mumbai', 'email': 'alice@mail.com'})
```

---

### Safe Setting

```python
# setdefault — only sets if key doesn't exist
config = {'port': 8080}
config.setdefault('port', 3000)  # No change — key exists
config.setdefault('host', 'localhost')  # Added — key was new
```

---

### Common Pattern: Counting

```python
counts = {}
for item in ['a', 'b', 'a', 'c', 'a']:
    counts[item] = counts.get(item, 0) + 1
# {'a': 3, 'b': 1, 'c': 1}
```

---

### Try This

```python
cart = {}
cart['apple'] = 3
cart['banana'] = 5
cart['apple'] = 10  # What happens?
print(cart)
```

**Answer:** `{'apple': 10, 'banana': 5}` — the value is overwritten.
