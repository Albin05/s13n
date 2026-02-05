## Lecture Notes: Applying Set Membership Testing for Efficiency

**Duration:** 10 minutes

---

### The `in` Operator with Sets

Checking if an element exists in a set is extremely fast — **O(1) on average**.

```python
fruits = {'apple', 'banana', 'orange', 'mango'}

print('apple' in fruits)     # True
print('grape' in fruits)     # False
print('grape' not in fruits) # True
```

---

### Why Sets Are Faster Than Lists

**List membership: O(n)** — checks each element one by one:
```python
colors_list = ['red', 'green', 'blue', 'yellow', 'purple']
# 'purple' in colors_list → checks red, green, blue, yellow, purple → Found!
```

**Set membership: O(1)** — uses hash table for instant lookup:
```python
colors_set = {'red', 'green', 'blue', 'yellow', 'purple'}
# 'purple' in colors_set → hash lookup → Found instantly!
```

For small collections the difference is negligible. For large collections, it's dramatic.

---

### Performance Comparison

```python
# With a list of 1 million items
big_list = list(range(1_000_000))
big_set = set(range(1_000_000))

# Searching for the last element:
999_999 in big_list  # Checks all 1M elements — SLOW
999_999 in big_set   # Hash lookup — INSTANT
```

| Collection Size | List `in` | Set `in` |
|----------------|-----------|----------|
| 100 | ~50 checks avg | 1 lookup |
| 10,000 | ~5,000 checks avg | 1 lookup |
| 1,000,000 | ~500,000 checks avg | 1 lookup |

---

### When to Convert List to Set

If you need to check membership **multiple times**, convert to a set first:

```python
# BAD: Checking membership in a list repeatedly
valid_codes = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO']  # imagine thousands

user_inputs = ['ABC', 'XYZ', 'GHI', 'ABC', 'QRS']
for code in user_inputs:
    if code in valid_codes:  # O(n) each time!
        print(f"{code}: valid")

# GOOD: Convert to set first
valid_codes_set = set(valid_codes)  # one-time O(n) cost

for code in user_inputs:
    if code in valid_codes_set:  # O(1) each time!
        print(f"{code}: valid")
```

**Rule of thumb:** If checking membership more than a few times, use a set.

---

### Subset and Superset Checks

**Is A a subset of B?** (All elements of A are in B)
```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print(a.issubset(b))   # True
print(a <= b)           # True (operator form)
print(a < b)            # True (proper subset — not equal)
```

**Is A a superset of B?** (A contains all elements of B)
```python
print(b.issuperset(a))  # True
print(b >= a)            # True
print(b > a)             # True (proper superset)
```

**Are A and B disjoint?** (No common elements)
```python
x = {1, 2, 3}
y = {4, 5, 6}
z = {3, 4, 5}

print(x.isdisjoint(y))  # True — no overlap
print(x.isdisjoint(z))  # False — 3 is common
```

---

### Practical Applications

**1. Input Validation:**
```python
valid_commands = {'start', 'stop', 'pause', 'resume', 'quit'}

user_input = input("Enter command: ").lower()
if user_input in valid_commands:
    print(f"Executing: {user_input}")
else:
    print(f"Unknown command. Options: {valid_commands}")
```

**2. Filtering Data:**
```python
blocked_users = {'spam_bot', 'troll_123', 'fake_account'}

messages = [
    ('alice', 'Hello!'),
    ('spam_bot', 'Buy now!'),
    ('bob', 'Hi there'),
    ('troll_123', 'Bad content'),
]

clean_messages = [(user, msg) for user, msg in messages
                  if user not in blocked_users]
print(clean_messages)
# [('alice', 'Hello!'), ('bob', 'Hi there')]
```

**3. Permission Checking:**
```python
user_roles = {'read', 'write'}
required = {'read', 'write', 'admin'}

if required.issubset(user_roles):
    print("Access granted")
else:
    missing = required - user_roles
    print(f"Access denied. Missing: {missing}")
# Access denied. Missing: {'admin'}
```

**4. Deduplication Check:**
```python
def has_duplicates(data):
    return len(data) != len(set(data))

print(has_duplicates([1, 2, 3, 4]))     # False
print(has_duplicates([1, 2, 3, 2]))     # True
```

**5. Vowel Counting:**
```python
vowels = {'a', 'e', 'i', 'o', 'u'}
word = "programming"

vowel_count = sum(1 for char in word if char in vowels)
print(f"Vowels in '{word}': {vowel_count}")  # 3
```

---

### Common Pattern: Lookup Table

```python
# Convert a list to a set for fast lookups
stop_words = set(['the', 'a', 'an', 'is', 'in', 'it', 'of', 'and', 'to'])

text = "the quick fox is in the garden and it is happy"
words = text.split()

# Filter out stop words — each check is O(1)
meaningful = [w for w in words if w not in stop_words]
print(meaningful)  # ['quick', 'fox', 'garden', 'happy']
```

---

### Key Takeaways

1. **`in` with sets is O(1)** — constant time regardless of set size
2. **`in` with lists is O(n)** — gets slower as the list grows
3. Convert lists to sets when doing **repeated membership checks**
4. Use `issubset()` to check if all required items are present
5. Use `isdisjoint()` to verify no overlap between sets
6. Sets are ideal for **validation**, **filtering**, and **deduplication checks**
