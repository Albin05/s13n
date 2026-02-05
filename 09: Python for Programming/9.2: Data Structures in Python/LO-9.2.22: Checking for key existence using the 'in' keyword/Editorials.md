## Editorials: Checking for Key Existence

---

### Q1 Solution: Key vs Value Check

```python
phonebook = {'Alice': '555-0101', 'Bob': '555-0202', 'Charlie': '555-0303'}

print(f"'Alice' is a key: {'Alice' in phonebook}")
print(f"'Alice' is a value: {'Alice' in phonebook.values()}")
print(f"'555-0202' is a key: {'555-0202' in phonebook}")
print(f"'555-0202' is a value: {'555-0202' in phonebook.values()}")
print(f"'Diana' in phonebook: {'Diana' in phonebook}")
```

**Explanation:** `in phonebook` checks keys. `in phonebook.values()` checks values. 'Alice' is a key but not a value. '555-0202' is a value but not a key.

---

### Q2 Solution: Form Validator

```python
def validate_form(data, required_fields):
    missing = [f for f in required_fields if f not in data]
    if missing:
        return False, missing
    return True, []

required = ['name', 'email', 'password', 'age']
forms = [
    {'name': 'Alice', 'email': 'a@b.com', 'password': '123', 'age': 25},
    {'name': 'Bob', 'email': 'b@c.com'},
    {'name': 'Charlie', 'age': 30, 'phone': '555-0000'}
]

for i, form in enumerate(forms, 1):
    valid, missing = validate_form(form, required)
    if valid:
        print(f"Form {i}: VALID")
    else:
        print(f"Form {i}: INVALID - Missing: {missing}")
```

---

### Q3 Solution: Safe Data Merger

```python
def safe_merge(base, updates, overwrite=False):
    added, skipped, overwritten = [], [], []
    result = base.copy()

    for key, val in updates.items():
        if key in result:
            if overwrite:
                overwritten.append((key, result[key], val))
                result[key] = val
            else:
                skipped.append(key)
        else:
            added.append(key)
            result[key] = val

    return result, added, skipped, overwritten

base = {'name': 'Alice', 'age': 25, 'city': 'Mumbai'}
updates = {'age': 26, 'email': 'alice@mail.com', 'phone': '9876543210'}

r, a, s, o = safe_merge(base, updates, overwrite=False)
print("Without overwrite:")
print(f"  Added: {a}")
print(f"  Skipped: {s}")
print(f"  Result: {r}")

r, a, s, o = safe_merge(base, updates, overwrite=True)
print("\nWith overwrite:")
print(f"  Added: {a}")
print(f"  Overwritten: {[(k, f'{old} -> {new}') for k, old, new in o]}")
print(f"  Result: {r}")
```

---

### Q4 Solution: Inventory Alert System

```python
inventory = {
    'laptop': {'stock': 5, 'min_stock': 10, 'price': 999},
    'mouse': {'stock': 50, 'min_stock': 20, 'price': 29},
    'keyboard': {'stock': 8, 'min_stock': 15, 'price': 79},
    'monitor': {'stock': 30, 'min_stock': 10, 'price': 399}
}

# 1. Add discount if missing
for product, details in inventory.items():
    if 'discount' not in details:
        details['discount'] = 0

# 2. Low stock alerts
for product, details in inventory.items():
    if details['stock'] < details['min_stock']:
        print(f"LOW STOCK: {product} ({details['stock']}/{details['min_stock']})")

# 3. Search
search = 'webcam'
if search in inventory:
    print(f"{search}: {inventory[search]}")
else:
    print(f"{search}: Not found")

# 4. Add new product only if not exists
new_product = 'laptop'
if new_product not in inventory:
    inventory[new_product] = {'stock': 20, 'min_stock': 5, 'price': 1299}
    print(f"Added {new_product}")
else:
    print(f"{new_product} already exists")
```

---

### Q5 Solution: Student Records Manager

```python
records = {
    'S001': {'name': 'Alice', 'marks': {'Math': 85, 'Science': 92}},
    'S002': {'name': 'Bob', 'marks': {'Math': 78}},
    'S003': {'name': 'Charlie', 'marks': {'Science': 88, 'English': 76}}
}

def has_subject(sid, subject):
    if sid not in records:
        return False
    return subject in records[sid]['marks']

def add_mark(sid, subject, score):
    if sid not in records:
        print(f"Student {sid} not found")
        return
    if subject in records[sid]['marks']:
        print(f"{records[sid]['name']} already has {subject} grade")
        return
    records[sid]['marks'][subject] = score
    print(f"Added {subject}={score} for {records[sid]['name']}")

def get_mark(sid, subject):
    if sid not in records:
        return "Student not found"
    return records[sid]['marks'].get(subject, "Not graded")

def common_subjects(id1, id2):
    s1 = set(records[id1]['marks'].keys())
    s2 = set(records[id2]['marks'].keys())
    return s1 & s2

print(has_subject('S001', 'Math'))     # True
print(has_subject('S002', 'English'))  # False
add_mark('S002', 'Science', 82)
print(get_mark('S001', 'Math'))        # 85
print(get_mark('S002', 'English'))     # Not graded
print(common_subjects('S001', 'S003')) # {'Science'}
```
