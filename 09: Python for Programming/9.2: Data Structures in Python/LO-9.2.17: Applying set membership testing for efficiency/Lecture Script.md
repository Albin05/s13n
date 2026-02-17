## Lecture Script: Applying Set Membership Testing for Efficiency


---

### CS Theory Bite

> **Origin**: Set membership (`in`) is **O(1)** via hash lookup — vs list membership which is **O(n)** linear scan. For 1 million items, set lookup is ~1000x faster.
>
> **Analogy**: Checking set membership is like **scanning a barcode** (instant) vs **reading every label on a shelf** (slow).
>
> **Why it matters**: Converting a list to a set before repeated `in` checks is one of the easiest Python optimizations.



### Hook (2 minutes)

**The Speed Test:**

You have a list of 10 million usernames. You need to check if a username is taken.

```python
# Approach 1: List
usernames_list = list(range(10_000_000))
# 9_999_999 in usernames_list → checks millions of elements!

# Approach 2: Set
usernames_set = set(range(10_000_000))
# 9_999_999 in usernames_set → instant!
```

The list approach could take seconds. The set approach takes microseconds. Same data, vastly different performance.

**Today:** We'll learn why sets are so fast for lookups and how to use this in real code.

---

### Section 1: How `in` Works (3 minutes)

**With a list:**
```python
colors = ['red', 'green', 'blue', 'yellow']
'blue' in colors
# Python checks: red? no. green? no. blue? YES!
# → 3 comparisons (linear search)
```

**With a set:**
```python
colors = {'red', 'green', 'blue', 'yellow'}
'blue' in colors
# Python computes hash('blue'), looks up directly
# → 1 operation (hash lookup)
```

The key insight: sets use **hash tables** internally. Each element has a computed "address" that Python can jump to directly.

---

### Section 2: When to Use Sets for Lookup (3 minutes)

**Convert list to set when doing repeated checks:**

```python
# Scenario: validate 1000 user inputs against 5000 valid codes
valid_codes_list = ['CODE_' + str(i) for i in range(5000)]
user_inputs = ['CODE_42', 'CODE_999', 'INVALID', 'CODE_1']

# SLOW: O(n) per check × m inputs = O(n*m)
for inp in user_inputs:
    if inp in valid_codes_list:  # scans up to 5000 items each time
        print(f"{inp}: valid")

# FAST: Convert once, then O(1) per check
valid_codes_set = set(valid_codes_list)  # one-time cost
for inp in user_inputs:
    if inp in valid_codes_set:  # instant each time
        print(f"{inp}: valid")
```

---

### Section 3: Subset and Superset (3 minutes)

**Subset check** — "Does this user have all required permissions?"

```python
required = {'read', 'write', 'delete'}
user_perms = {'read', 'write', 'delete', 'admin'}

# Is required a subset of user_perms?
print(required.issubset(user_perms))  # True
print(required <= user_perms)         # True

# Missing permissions?
missing = required - user_perms
print(missing)  # set() — nothing missing!
```

**Disjoint check** — "Do these groups share any members?"

```python
team_a = {'Alice', 'Bob', 'Charlie'}
team_b = {'Diana', 'Eve', 'Frank'}
team_c = {'Frank', 'Grace', 'Alice'}

print(team_a.isdisjoint(team_b))  # True — no overlap
print(team_a.isdisjoint(team_c))  # False — Alice is in both
```

---

### Section 4: Practical Patterns (3 minutes)

**Pattern 1: Fast Filtering**
```python
blocked = {'spam', 'troll', 'bot'}
messages = [('spam', 'Buy!'), ('alice', 'Hi'), ('bot', 'Click')]
clean = [(u, m) for u, m in messages if u not in blocked]
```

**Pattern 2: Duplicate Detection**
```python
def has_duplicates(items):
    return len(items) != len(set(items))

print(has_duplicates([1, 2, 3]))     # False
print(has_duplicates([1, 2, 2, 3]))  # True
```

**Pattern 3: Counting Matches**
```python
vowels = set('aeiou')
word = 'programming'
count = sum(1 for ch in word if ch in vowels)
print(f"Vowels: {count}")  # 3
```

---

### Summary (1 minute)

1. **Set `in`** is **O(1)** — lists are **O(n)**
2. Convert lists to sets for **repeated** membership checks
3. Use `issubset()` for "has all required" checks
4. Use `isdisjoint()` for "no overlap" checks
5. Sets are the go-to for **validation**, **filtering**, and **dedup checks**
