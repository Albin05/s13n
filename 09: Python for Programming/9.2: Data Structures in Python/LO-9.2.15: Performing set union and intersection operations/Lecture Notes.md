## Lecture Notes: Performing Set Union and Intersection Operations

**Duration:** 12 minutes

---

## Overview

Two fundamental set operations:
- **Union (|)**: Combine all unique elements
- **Intersection (&)**: Find common elements

Both return new sets without modifying originals.

---

## Union Operation (4 minutes)

### Syntax
```python
# Operator
result = set1 | set2 | set3

# Method
result = set1.union(set2, set3)
```

### Examples

```python
A = {1, 2, 3}
B = {3, 4, 5}

result = A | B
# {1, 2, 3, 4, 5}
```

**Multiple sets:**
```python
all_data = source1 | source2 | source3
```

**Real-world:**
```python
# Merge subscriber lists
campaign_a = {'alice@ex.com', 'bob@ex.com'}
campaign_b = {'bob@ex.com', 'charlie@ex.com'}

all_subscribers = campaign_a | campaign_b
# {'alice@ex.com', 'bob@ex.com', 'charlie@ex.com'}
```

---

## Intersection Operation (4 minutes)

### Syntax
```python
# Operator
result = set1 & set2 & set3

# Method
result = set1.intersection(set2, set3)
```

### Examples

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A & B
# {3, 4}
```

**Multiple sets:**
```python
common = set1 & set2 & set3
# Only elements in ALL sets
```

**Real-world:**
```python
# Find common interests
alice_interests = {'python', 'web', 'ai'}
bob_interests = {'web', 'mobile', 'ai'}

common = alice_interests & bob_interests
# {'web', 'ai'}
```

---

## Practical Patterns (2 minutes)

**Pattern 1: Deduplication**
```python
all_unique = list1_set | list2_set | list3_set
```

**Pattern 2: Finding Overlap**
```python
has_common = bool(set1 & set2)
```

**Pattern 3: Multi-Platform Users**
```python
web_users = {'alice', 'bob', 'charlie'}
mobile_users = {'bob', 'charlie', 'diana'}

# Both platforms
both = web_users & mobile_users  # {'bob', 'charlie'}

# All users
all = web_users | mobile_users  # 4 users

# Web only
web_only = web_users - mobile_users  # {'alice'}
```

---

## Applications (2 minutes)

**E-commerce Filtering:**
```python
products_wifi = {1, 2, 3, 5}
products_bt = {2, 3, 4, 6}
under_100 = {1, 2, 4, 7}

# Both features
both_features = products_wifi & products_bt  # {2, 3}

# Any wireless + affordable
wireless = products_wifi | products_bt
affordable_wireless = wireless & under_100  # {2, 4}
```

**Permission Validation:**
```python
user_perms = {'read', 'write', 'execute'}
required_perms = {'read', 'write'}

has_all = required_perms.issubset(user_perms)
# or
has_all = (required_perms & user_perms) == required_perms
```

---

## Quick Reference

```python
A = {1, 2, 3}
B = {2, 3, 4}

# Union
A | B           # {1, 2, 3, 4}
A.union(B)      # {1, 2, 3, 4}

# Intersection
A & B           # {2, 3}
A.intersection(B)  # {2, 3}

# Chaining
A | B | C       # Union of all three
A & B & C       # Common to all three
```

**Key Points:**
- Both return NEW sets
- Originals unchanged
- Use `|` for combining
- Use `&` for filtering
- O(n) average time complexity

**Remember:** Sets automatically handle uniqueness!
