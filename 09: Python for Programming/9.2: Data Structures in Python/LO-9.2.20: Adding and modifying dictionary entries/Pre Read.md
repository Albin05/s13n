## Pre-Read: Adding and Modifying Dictionary Entries

**Duration:** 5 minutes

---

## What Does Add/Modify Mean?

Dictionaries have a **"save button"** that's smart - use `dict[key] = value` and it automatically adds if new or updates if existing! This is **one syntax for two operations**.

### Simple Analogy

**Like editing a document**:
- **Type new heading**: Creates new section
- **Type existing heading**: Replaces old content
- **Same action**: Just type - document figures out add vs update!
- **Dict**: Same with `student['grade'] = 'A'` - adds or updates!

**Or like phone contacts**:
- **Save "Mom"**: First time → creates new contact
- **Save "Mom" again**: Updates existing contact
- **No mode switch**: Phone automatically handles both
- **Dict**: Works identically!

### The "No Error" Magic

**Beautiful thing**: You never get errors!
```python
person = {}  # Empty dict

# Add (first time) - works!
person['name'] = 'Alice'

# Modify (exists) - works!
person['name'] = 'Alice B.'

# Never crashes! Just works!
```

**Compare to lists** (need to check index exists):
```python
items = []
# items[0] = 'x'  # IndexError! List crashes!
items.append('x')  # Must use append for new items
```

**Dicts are more forgiving!**

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
