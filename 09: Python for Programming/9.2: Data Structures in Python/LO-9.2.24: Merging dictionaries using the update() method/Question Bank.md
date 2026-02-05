## Question Bank: Merging Dictionaries

---

### Q1: Basic Merge Operations (3 minutes, Low Difficulty)

Given:
```python
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 30, 'd': 40}
```

1. Merge dict2 into dict1 using `update()` — print result
2. Start fresh with original values. Create a NEW merged dict using `{**d1, **d2}` — verify originals are unchanged
3. Merge with dict1 taking priority for shared keys

**Expected Output:**
```
After update: {'a': 1, 'b': 20, 'c': 30, 'd': 40}
Unpacking merge: {'a': 1, 'b': 20, 'c': 30, 'd': 40}
dict1 unchanged: {'a': 1, 'b': 2, 'c': 3}
dict1 priority: {'b': 2, 'c': 3, 'd': 40, 'a': 1}
```

**Key Concepts:** `update()`, `{**d1, **d2}`, merge priority

---

### Q2: Config System (3 minutes, Low Difficulty)

Build a 3-layer configuration system:
```python
defaults = {'theme': 'light', 'font_size': 14, 'language': 'en', 'sidebar': True, 'notifications': True}
user_config = {'theme': 'dark', 'font_size': 18}
session_config = {'sidebar': False}
```

1. Merge in priority order: defaults < user_config < session_config
2. Print the final config
3. Show which settings came from which layer

**Expected Output:**
```
Final config: {'theme': 'dark', 'font_size': 18, 'language': 'en', 'sidebar': False, 'notifications': True}
From defaults: ['language', 'notifications']
From user: ['theme', 'font_size']
From session: ['sidebar']
```

**Key Concepts:** Layered merging, tracking sources

---

### Q3: Merging Lists of Dicts (5 minutes, Medium Difficulty)

Given multiple data sources:
```python
source_a = {'item_1': 10, 'item_2': 20, 'item_3': 30}
source_b = {'item_2': 25, 'item_4': 40, 'item_5': 50}
source_c = {'item_1': 15, 'item_3': 35, 'item_5': 55}
```

Write functions:
1. `merge_sum(dicts)` — merge all, summing values for shared keys
2. `merge_max(dicts)` — merge all, keeping max value for shared keys
3. `merge_all_values(dicts)` — merge all, collecting all values as lists

**Expected Output:**
```
Sum: {'item_1': 25, 'item_2': 45, 'item_3': 65, 'item_4': 40, 'item_5': 105}
Max: {'item_1': 15, 'item_2': 25, 'item_3': 35, 'item_4': 40, 'item_5': 55}
All values: {'item_1': [10, 15], 'item_2': [20, 25], 'item_3': [30, 35], 'item_4': [40], 'item_5': [50, 55]}
```

**Key Concepts:** Custom merge strategies

---

### Q4: Profile Builder (5 minutes, Medium Difficulty)

Build a user profile from multiple API responses:

```python
basic_info = {'id': 42, 'name': 'Alice', 'email': 'alice@mail.com'}
social_info = {'twitter': '@alice', 'github': 'alicecodes'}
preferences = {'theme': 'dark', 'language': 'en', 'notifications': {'email': True, 'sms': False}}
activity = {'last_login': '2024-01-15', 'posts': 42}
```

1. Merge all into a single profile dict
2. Add a 'full_profile' key that is True
3. Print the profile in a formatted way

**Key Concepts:** Multi-source merging, nested data

---

### Q5: Inventory Reconciliation (5 minutes, Medium Difficulty)

Two warehouses report their stock:
```python
warehouse_a = {'laptop': 10, 'phone': 25, 'tablet': 8, 'charger': 100}
warehouse_b = {'phone': 15, 'tablet': 12, 'headset': 30, 'cable': 200}
```

Write functions:
1. `total_stock(w1, w2)` — combined stock (sum values for shared items)
2. `only_in_one(w1, w2)` — items available in only one warehouse
3. `rebalance(w1, w2)` — for shared items, calculate transfer needed to equalize stock

**Expected Output:**
```
Total stock: {'laptop': 10, 'phone': 40, 'tablet': 20, 'charger': 100, 'headset': 30, 'cable': 200}
Only in A: {'laptop': 10, 'charger': 100}
Only in B: {'headset': 30, 'cable': 200}
Rebalance: phone: transfer 5 from A to B, tablet: transfer 2 from B to A
```

**Key Concepts:** Custom merge with arithmetic, set operations on keys
