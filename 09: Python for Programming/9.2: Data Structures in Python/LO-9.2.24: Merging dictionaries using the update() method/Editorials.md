## Editorials: Merging Dictionaries

---

### Q1 Solution: Basic Merge Operations

```python
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 30, 'd': 40}

# 1. update() — modifies dict1
d1_copy = dict1.copy()
d1_copy.update(dict2)
print(f"After update: {d1_copy}")

# 2. Unpacking — creates new dict
merged = {**dict1, **dict2}
print(f"Unpacking merge: {merged}")
print(f"dict1 unchanged: {dict1}")

# 3. dict1 priority
priority = {**dict2, **dict1}
print(f"dict1 priority: {priority}")
```

**Explanation:** In `{**d1, **d2}`, d2 values override d1 for shared keys. To give d1 priority, reverse the order: `{**d2, **d1}`.

---

### Q2 Solution: Config System

```python
defaults = {'theme': 'light', 'font_size': 14, 'language': 'en', 'sidebar': True, 'notifications': True}
user_config = {'theme': 'dark', 'font_size': 18}
session_config = {'sidebar': False}

final = {**defaults, **user_config, **session_config}
print(f"Final config: {final}")

# Track sources
for key in final:
    if key in session_config:
        source = 'session'
    elif key in user_config:
        source = 'user'
    else:
        source = 'defaults'
    print(f"  {key}: {final[key]} (from {source})")
```

---

### Q3 Solution: Custom Merge Strategies

```python
source_a = {'item_1': 10, 'item_2': 20, 'item_3': 30}
source_b = {'item_2': 25, 'item_4': 40, 'item_5': 50}
source_c = {'item_1': 15, 'item_3': 35, 'item_5': 55}

def merge_sum(dicts):
    result = {}
    for d in dicts:
        for k, v in d.items():
            result[k] = result.get(k, 0) + v
    return result

def merge_max(dicts):
    result = {}
    for d in dicts:
        for k, v in d.items():
            if k in result:
                result[k] = max(result[k], v)
            else:
                result[k] = v
    return result

def merge_all_values(dicts):
    result = {}
    for d in dicts:
        for k, v in d.items():
            result.setdefault(k, []).append(v)
    return result

sources = [source_a, source_b, source_c]
print(f"Sum: {merge_sum(sources)}")
print(f"Max: {merge_max(sources)}")
print(f"All values: {merge_all_values(sources)}")
```

**Explanation:**
- `merge_sum` uses `.get(k, 0) + v` to accumulate sums.
- `merge_max` uses `max()` to keep the highest value.
- `merge_all_values` uses `setdefault(k, [])` to build lists of all values.

---

### Q4 Solution: Profile Builder

```python
basic_info = {'id': 42, 'name': 'Alice', 'email': 'alice@mail.com'}
social_info = {'twitter': '@alice', 'github': 'alicecodes'}
preferences = {'theme': 'dark', 'language': 'en', 'notifications': {'email': True, 'sms': False}}
activity = {'last_login': '2024-01-15', 'posts': 42}

profile = {**basic_info, **social_info, **preferences, **activity, 'full_profile': True}

print("User Profile:")
for key, value in profile.items():
    print(f"  {key}: {value}")
```

---

### Q5 Solution: Inventory Reconciliation

```python
warehouse_a = {'laptop': 10, 'phone': 25, 'tablet': 8, 'charger': 100}
warehouse_b = {'phone': 15, 'tablet': 12, 'headset': 30, 'cable': 200}

def total_stock(w1, w2):
    result = w1.copy()
    for item, qty in w2.items():
        result[item] = result.get(item, 0) + qty
    return result

def only_in_one(w1, w2):
    only_w1 = {k: v for k, v in w1.items() if k not in w2}
    only_w2 = {k: v for k, v in w2.items() if k not in w1}
    return only_w1, only_w2

def rebalance(w1, w2):
    shared = set(w1.keys()) & set(w2.keys())
    transfers = []
    for item in shared:
        diff = w1[item] - w2[item]
        if diff > 0:
            transfer = diff // 2
            transfers.append(f"{item}: transfer {transfer} from A to B")
        elif diff < 0:
            transfer = abs(diff) // 2
            transfers.append(f"{item}: transfer {transfer} from B to A")
    return transfers

print(f"Total stock: {total_stock(warehouse_a, warehouse_b)}")
only_a, only_b = only_in_one(warehouse_a, warehouse_b)
print(f"Only in A: {only_a}")
print(f"Only in B: {only_b}")
print("Rebalance:")
for t in rebalance(warehouse_a, warehouse_b):
    print(f"  {t}")
```

**Explanation:** `total_stock` sums quantities using `.get()`. `only_in_one` uses `not in` to find exclusive items. `rebalance` calculates transfer amounts by finding the difference and dividing by 2 for each shared item.
