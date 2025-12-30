## Lecture Script: Performing Set Difference and Symmetric Difference Operations

**Duration:** 18 minutes

---

### Hook (2 minutes)

**Scenario:**

Finding exclusive content between platforms:

```python
netflix_shows = {'Stranger Things', 'The Crown', 'Bridgerton', 'Wednesday'}
hulu_shows = {'The Handmaid\'s Tale', 'The Crown', 'Only Murders', 'Wednesday'}

# Shows ONLY on Netflix (difference)
netflix_exclusive = netflix_shows - hulu_shows
print(f"Netflix only: {netflix_exclusive}")
# {'Stranger Things', 'Bridgerton'}

# Shows on EITHER but not BOTH (symmetric difference)
exclusive_to_one = netflix_shows ^ hulu_shows
print(f"Exclusive to one platform: {exclusive_to_one}")
# {'Stranger Things', 'Bridgerton', "The Handmaid's Tale", 'Only Murders'}
```

**Today's Focus:** Master `-` (difference) and `^` (symmetric difference) for finding exclusive elements.

---

### Section 1: Difference Operation (5 minutes)

**What is Difference?**
Elements in first set but NOT in second.

**Syntax:**
```python
result = set1 - set2
result = set1.difference(set2)
```

**Examples:**

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# A - B: in A but not in B
diff = A - B
print(diff)  # {1, 2, 3}

# B - A: in B but not in A (different!)
diff = B - A
print(diff)  # {6, 7, 8}
```

**Key Point:** Order matters! `A - B ≠ B - A`

**Real-World Examples:**

**1. Feature Comparison:**
```python
product_v1 = {'feature_a', 'feature_b', 'feature_c'}
product_v2 = {'feature_b', 'feature_c', 'feature_d', 'feature_e'}

# Removed features
removed = product_v1 - product_v2
print(f"Removed: {removed}")  # {'feature_a'}

# New features
added = product_v2 - product_v1
print(f"Added: {added}")  # {'feature_d', 'feature_e'}
```

**2. User Churn Analysis:**
```python
last_month_users = {'alice', 'bob', 'charlie', 'diana'}
this_month_users = {'bob', 'charlie', 'eve', 'frank'}

# Users who left
churned = last_month_users - this_month_users
print(f"Churned: {churned}")  # {'alice', 'diana'}

# New users
new = this_month_users - last_month_users
print(f"New: {new}")  # {'eve', 'frank'}
```

**3. Todo List Management:**
```python
all_tasks = {'task1', 'task2', 'task3', 'task4', 'task5'}
completed_tasks = {'task2', 'task4'}

# Remaining tasks
remaining = all_tasks - completed_tasks
print(f"TODO: {remaining}")  # {'task1', 'task3', 'task5'}
```

---

### Section 2: Symmetric Difference (5 minutes)

**What is Symmetric Difference?**
Elements in EITHER set but NOT in BOTH.

**Syntax:**
```python
result = set1 ^ set2
result = set1.symmetric_difference(set2)
```

**Examples:**

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Elements in either but not both
sym_diff = A ^ B
print(sym_diff)  # {1, 2, 3, 6, 7, 8}
# Excludes 4 and 5 (in both)
```

**Key Point:** Symmetric! `A ^ B = B ^ A`

**Visualize:**
```python
# Equivalent to:
sym_diff = (A - B) | (B - A)
# (in A only) OR (in B only)
```

**Real-World Examples:**

**1. Find Disagreements:**
```python
alice_votes = {'proposal_a', 'proposal_b', 'proposal_c'}
bob_votes = {'proposal_b', 'proposal_c', 'proposal_d'}

# They disagree on
disagreements = alice_votes ^ bob_votes
print(f"Disagree on: {disagreements}")
# {'proposal_a', 'proposal_d'}
```

**2. Unique Purchases:**
```python
store_a_customers = {'cust1', 'cust2', 'cust3', 'cust4'}
store_b_customers = {'cust3', 'cust4', 'cust5', 'cust6'}

# Customers exclusive to one store
exclusive = store_a_customers ^ store_b_customers
print(f"Shop at only one: {exclusive}")
# {'cust1', 'cust2', 'cust5', 'cust6'}
```

**3. Data Sync Detection:**
```python
server_a_files = {'file1.txt', 'file2.txt', 'file3.txt'}
server_b_files = {'file2.txt', 'file3.txt', 'file4.txt'}

# Files that need syncing
needs_sync = server_a_files ^ server_b_files
print(f"Need sync: {needs_sync}")
# {'file1.txt', 'file4.txt'}
```

---

### Section 3: Combining Operations (3 minutes)

**All Four Operations:**

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"Union (|):     {A | B}")        # {1,2,3,4,5,6}
print(f"Intersection (&): {A & B}")     # {3,4}
print(f"Difference (-):   {A - B}")     # {1,2}
print(f"Sym Diff (^):     {A ^ B}")     # {1,2,5,6}
```

**Complex Analysis:**
```python
current_users = {'alice', 'bob', 'charlie', 'diana'}
premium_users = {'bob', 'diana'}
trial_users = {'eve', 'frank'}

# Current non-premium
free_users = current_users - premium_users
# {'alice', 'charlie'}

# All users (current + trial)
all_users = current_users | trial_users
# {'alice', 'bob', 'charlie', 'diana', 'eve', 'frank'}

# Users not on trial
non_trial = all_users - trial_users
# {'alice', 'bob', 'charlie', 'diana'}
```

---

### Section 4: Practical Applications (2 minutes)

**Access Control:**
```python
def check_access(user_permissions, required_permissions):
    # Missing permissions
    missing = required_permissions - user_permissions

    if missing:
        return False, f"Missing: {missing}"
    return True, "Access granted"

user_perms = {'read', 'write'}
required = {'read', 'write', 'delete'}

allowed, msg = check_access(user_perms, required)
print(msg)  # Missing: {'delete'}
```

**Inventory Management:**
```python
def find_discrepancies(expected_items, actual_items):
    missing = expected_items - actual_items
    extra = actual_items - expected_items

    return {
        'missing': missing,
        'extra': extra,
        'discrepancy_count': len(missing) + len(extra)
    }

expected = {'item1', 'item2', 'item3', 'item4'}
actual = {'item2', 'item3', 'item5'}

report = find_discrepancies(expected, actual)
print(f"Missing: {report['missing']}")  # {'item1', 'item4'}
print(f"Extra: {report['extra']}")      # {'item5'}
```

---

### Summary (1 minute)

**Two Operations:**

**Difference (-):**
- `A - B`: Elements in A but NOT in B
- Order matters: `A - B ≠ B - A`
- Use: Finding what's missing, exclusive elements

**Symmetric Difference (^):**
- `A ^ B`: Elements in EITHER but NOT BOTH
- Symmetric: `A ^ B = B ^ A`
- Equivalent to: `(A - B) | (B - A)`
- Use: Finding disagreements, unique elements

**Quick Reference:**
```python
A = {1, 2, 3}
B = {2, 3, 4}

A | B   # {1,2,3,4} - union
A & B   # {2,3} - intersection
A - B   # {1} - difference
A ^ B   # {1,4} - symmetric difference
```
