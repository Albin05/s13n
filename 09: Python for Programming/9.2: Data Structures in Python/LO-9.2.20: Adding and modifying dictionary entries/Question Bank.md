## Question Bank: Adding and Modifying Dictionary Entries

---

### Q1: Building a Contact (3 minutes, Low Difficulty)

Start with an empty dictionary. Build a contact entry by:
1. Adding `name` = `'Alice'`
2. Adding `phone` = `'555-0101'`
3. Adding `email` = `'alice@old.com'`
4. Updating `email` to `'alice@new.com'`
5. Adding `city` = `'Mumbai'` using `setdefault()`
6. Try to change `city` to `'Delhi'` using `setdefault()` — observe what happens

Print the contact after each step.

**Expected Output:**
```
Step 1: {'name': 'Alice'}
Step 2: {'name': 'Alice', 'phone': '555-0101'}
Step 3: {'name': 'Alice', 'phone': '555-0101', 'email': 'alice@old.com'}
Step 4: {'name': 'Alice', 'phone': '555-0101', 'email': 'alice@new.com'}
Step 5: {'name': 'Alice', 'phone': '555-0101', 'email': 'alice@new.com', 'city': 'Mumbai'}
Step 6: {'name': 'Alice', 'phone': '555-0101', 'email': 'alice@new.com', 'city': 'Mumbai'}
```

**Key Concepts:** Assignment, `setdefault()` behavior

---

### Q2: Config Merger (3 minutes, Low Difficulty)

Given:
```python
defaults = {'theme': 'light', 'font_size': 14, 'language': 'en', 'notifications': True}
user_settings = {'theme': 'dark', 'font_size': 18}
```

1. Create a final config by merging defaults with user settings (user overrides defaults)
2. Print which settings were overridden

**Expected Output:**
```
Final config: {'theme': 'dark', 'font_size': 18, 'language': 'en', 'notifications': True}
Overridden: theme (light -> dark), font_size (14 -> 18)
```

**Key Concepts:** `update()`, detecting changes

---

### Q3: Word Frequency Counter (5 minutes, Medium Difficulty)

```python
text = "to be or not to be that is the question to be is to exist"
```

1. Build a frequency dictionary using `.get()` pattern
2. Find the most common word
3. Find words that appear exactly once
4. Find words that appear more than twice

**Expected Output:**
```
Frequencies: {'to': 4, 'be': 3, 'or': 1, 'not': 1, ...}
Most common: 'to' (4 times)
Appear once: ['or', 'not', 'that', 'the', 'question', 'exist']
Appear 3+ times: ['to', 'be']
```

**Key Concepts:** Counter pattern with `.get()`, dict comprehension

---

### Q4: Shopping Cart Manager (5 minutes, Medium Difficulty)

Build a shopping cart system using a dictionary:

```python
# cart: {product_name: {'price': float, 'quantity': int}}
```

Implement:
1. `add_item(cart, name, price, qty)` — add new item or increase quantity
2. `update_quantity(cart, name, new_qty)` — set new quantity
3. `get_total(cart)` — total cost
4. `apply_discount(cart, product, percent)` — reduce price by percent

Test:
- Add "Apple" ($1.50, qty 3)
- Add "Banana" ($0.75, qty 5)
- Add "Apple" again ($1.50, qty 2) — should increase to qty 5
- Apply 10% discount on Apple
- Print cart and total

**Key Concepts:** `setdefault()`, modifying nested values

---

### Q5: Grade Tracker (5 minutes, Medium Difficulty)

Build a grade tracking system:

```python
# grades: {student: [list of scores]}
```

1. Initialize with empty dict
2. Add scores one by one: Alice:85, Bob:90, Alice:92, Charlie:78, Bob:88, Alice:95
3. Calculate each student's average
4. Assign letter grades (A: 90+, B: 80+, C: 70+, D: below 70)
5. Print a summary

**Expected Output:**
```
Alice: [85, 92, 95] -> Avg: 90.67 -> Grade: A
Bob: [90, 88] -> Avg: 89.00 -> Grade: B
Charlie: [78] -> Avg: 78.00 -> Grade: C
```

**Key Concepts:** `setdefault()` with lists, accumulating data
