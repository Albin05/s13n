## Lecture Notes: Performing Set Union and Intersection Operations


---

## Introduction

Union and intersection bring **200 years of mathematics** into programming - making **Venn diagrams executable**! This represents **declarative set theory**: describe relationships mathematically, let Python compute them.

### Why These Operations Are Revolutionary

**Before set operations** (traditional programming): Combining or comparing collections required nested loops:
```c
// C code - tedious comparison
for (int i = 0; i < size1; i++) {
    for (int j = 0; j < size2; j++) {
        if (array1[i] == array2[j]) {
            // Found common element - add to result
            // Check if already added (avoid duplicates)
            // ... 20+ lines of code
        }
    }
}
// O(n²) complexity! Slow for large data!
```

**With set operations** (modern Python): Mathematical elegance:
```python
common = set1 & set2  # One line! O(n) complexity!
```

**Real-world impact**: Code **95% shorter**, dramatically faster. **SQL databases** use these exact operations (UNION, INTERSECT). **Data science** built on set operations (pandas, numpy use them everywhere)!

### Historical Context

**Mathematical foundation**: **Georg Cantor** (1874) invented set theory. **Venn diagrams** (John Venn, 1880) visualized set relationships. **100+ years later**, programming languages made these diagrams executable!

**Symbol origins**:
- `∪` (union) looks like **U** for "union" - standardized 1890s
- `∩` (intersection) looks like **inverted U** - symbolizes overlap
- Python uses `|` and `&` from **logic gates** (hardware, 1940s) - programming tradition!

**Database influence**: **SQL** (1974) used `UNION` and `INTERSECT` keywords. Python adopted **symbolic operators** for conciseness - math notation beats English keywords!

### Real-World Analogies

**Union (|) like party guest list merge**:
- **Your list**: Alice, Bob, Charlie
- **Friend's list**: Bob, Diana, Eve
- **Combined**: Alice, Bob, Charlie, Diana, Eve
- **Automatic deduplication**: Bob appears once!
- **Python**: `your_list | friend_list` - instant merge!

**Intersection (&) like Venn diagram overlap**:
- **Circle A**: Your skills {Python, SQL, Git}
- **Circle B**: Job requirements {SQL, Git, Docker}
- **Overlap**: {SQL, Git} - where circles intersect!
- **Python**: `your_skills & job_requirements` - instant match!

**Or union like streaming services**:
- **Netflix**: Movies {A, B, C}
- **Hulu**: Movies {B, C, D}
- **Combined subscription**: {A, B, C, D} - all unique movies!
- **Union**: `netflix | hulu` - total content library!

**Intersection like mutual friends**:
- **Your friends**: 200 people
- **Their friends**: 300 people
- **Mutual**: Maybe 50 overlap
- **Intersection**: `your_friends & their_friends` - instant common ground!

### The Mathematical Beauty

**Set operations ARE math notation**:

**Mathematics (1880s)**:
```
A ∪ B  (union - all elements)
A ∩ B  (intersection - common elements)
```

**Python (2004)**:
```python
A | B  # union - all elements
A & B  # intersection - common elements
```

**This is programming at its purest**: Math textbooks from 140 years ago directly translate to Python code! **Georg Cantor would understand Python sets immediately** - that's beautiful API design!

### Performance and Algorithm Design

**Why these operations are fast**:

**Union (A | B)**:
- Hash table magic: O(len(A) + len(B))
- Add all from A → hash table
- Add all from B → automatically deduplicates
- Linear time, not quadratic!

**Intersection (A & B)**:
- Iterate smaller set: O(min(len(A), len(B)))
- Check each in larger set: O(1) per check
- Much faster than nested loops!

**Traditional nested loop**: O(n × m) - explodes with size!
**Set operations**: O(n + m) - scales beautifully!

**For 1000 vs 1000 elements**:
- Nested loops: 1,000,000 comparisons
- Set operations: ~2,000 operations
- **500x faster!**

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
