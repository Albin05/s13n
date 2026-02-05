## Question Bank: Checking for Key Existence

---

### Q1: Key vs Value Check (3 minutes, Low Difficulty)

Given:
```python
phonebook = {'Alice': '555-0101', 'Bob': '555-0202', 'Charlie': '555-0303'}
```

Write code to check:
1. Is 'Alice' a key? Is 'Alice' a value?
2. Is '555-0202' a key? Is '555-0202' a value?
3. Is 'Diana' in the phonebook?

**Expected Output:**
```
'Alice' is a key: True
'Alice' is a value: False
'555-0202' is a key: False
'555-0202' is a value: True
'Diana' in phonebook: False
```

**Key Concepts:** `in` checks keys, `.values()` for value checks

---

### Q2: Form Validator (3 minutes, Low Difficulty)

Write a function `validate_form(data, required_fields)` that checks if all required fields are present in a form dictionary.

```python
required = ['name', 'email', 'password', 'age']

form1 = {'name': 'Alice', 'email': 'a@b.com', 'password': '123', 'age': 25}
form2 = {'name': 'Bob', 'email': 'b@c.com'}
form3 = {'name': 'Charlie', 'age': 30, 'phone': '555-0000'}
```

For each form, print whether it's valid and list any missing fields.

**Expected Output:**
```
Form 1: VALID
Form 2: INVALID - Missing: ['password', 'age']
Form 3: INVALID - Missing: ['email', 'password']
```

**Key Concepts:** `in` with loops, collecting missing keys

---

### Q3: Safe Data Merger (5 minutes, Medium Difficulty)

Write a function `safe_merge(base, updates, overwrite=False)` that:
- Adds new keys from `updates` to `base`
- If `overwrite=False`: skips keys that already exist in `base`
- If `overwrite=True`: overwrites existing keys
- Returns which keys were added, skipped, or overwritten

```python
base = {'name': 'Alice', 'age': 25, 'city': 'Mumbai'}
updates = {'age': 26, 'email': 'alice@mail.com', 'phone': '9876543210'}
```

Test with both `overwrite=False` and `overwrite=True`.

**Expected Output:**
```
Without overwrite:
  Added: ['email', 'phone']
  Skipped: ['age']
  Result: {'name': 'Alice', 'age': 25, 'city': 'Mumbai', 'email': 'alice@mail.com', 'phone': '9876543210'}

With overwrite:
  Added: ['email', 'phone']
  Overwritten: ['age'] (25 -> 26)
  Result: {'name': 'Alice', 'age': 26, 'city': 'Mumbai', 'email': 'alice@mail.com', 'phone': '9876543210'}
```

**Key Concepts:** `in` for conditional updates

---

### Q4: Inventory Alert System (5 minutes, Medium Difficulty)

```python
inventory = {
    'laptop': {'stock': 5, 'min_stock': 10, 'price': 999},
    'mouse': {'stock': 50, 'min_stock': 20, 'price': 29},
    'keyboard': {'stock': 8, 'min_stock': 15, 'price': 79},
    'monitor': {'stock': 30, 'min_stock': 10, 'price': 399}
}
```

Write a program that:
1. Checks if each product has a 'discount' key — if not, set discount to 0
2. Finds products where stock is below min_stock
3. Checks if a searched product exists, prints info or "Not found"
4. Adds a new product only if it doesn't already exist

**Key Concepts:** `in` with nested dicts, conditional adding

---

### Q5: Student Records Manager (5 minutes, Medium Difficulty)

```python
records = {
    'S001': {'name': 'Alice', 'marks': {'Math': 85, 'Science': 92}},
    'S002': {'name': 'Bob', 'marks': {'Math': 78}},
    'S003': {'name': 'Charlie', 'marks': {'Science': 88, 'English': 76}}
}
```

Write functions:
1. `has_subject(student_id, subject)` — check if student has a grade for that subject
2. `add_mark(student_id, subject, score)` — add only if subject not already graded
3. `get_mark(student_id, subject)` — return mark or "Not graded"
4. `common_subjects(id1, id2)` — subjects both students have grades for

**Key Concepts:** Nested key checking, `in` with dict keys
