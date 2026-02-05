## Editorials: Applying Set Membership Testing for Efficiency

---

### Q1 Solution: Command Validator

```python
valid_commands = {'start', 'stop', 'pause', 'resume', 'help', 'quit'}

inputs = ['start', 'STOP', 'fly', 'Pause', 'quit', 'dance', 'help']

for inp in inputs:
    if inp.lower() in valid_commands:
        print(f"{inp} -> Valid")
    else:
        print(f"{inp} -> Invalid")
```

**Explanation:** We convert user input to lowercase with `.lower()` before checking against the set. Since the set contains lowercase strings, this makes the comparison case-insensitive. The `in` check is O(1).

---

### Q2 Solution: Duplicate Detector

```python
def find_duplicates(data):
    seen = set()
    duplicates = set()
    for item in data:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return duplicates

print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))  # {2, 3}
print(find_duplicates(['a', 'b', 'c', 'a']))     # {'a'}
print(find_duplicates([1, 2, 3]))                 # set()
```

**Explanation:** We maintain a `seen` set. For each element, we check if it's already been seen (O(1) check). If yes, it's a duplicate. If no, we add it to `seen`. This runs in O(n) total — much better than O(n²) with nested loops.

---

### Q3 Solution: Permission System

```python
roles = {
    'viewer': {'read'},
    'editor': {'read', 'write'},
    'admin': {'read', 'write', 'delete', 'manage_users'},
    'superadmin': {'read', 'write', 'delete', 'manage_users', 'system_config'}
}

users = {
    'Alice': 'admin',
    'Bob': 'editor',
    'Charlie': 'viewer'
}

def check_access(username, required_permissions):
    role = users.get(username)
    if role is None:
        print(f"{username}: User not found")
        return

    user_perms = roles[role]
    required_set = set(required_permissions)

    if required_set.issubset(user_perms):
        print(f"{username}: Access GRANTED")
    else:
        missing = required_set - user_perms
        print(f"{username}: Access DENIED, missing: {missing}")

check_access('Alice', {'read', 'delete'})
check_access('Bob', {'read', 'write', 'delete'})
check_access('Charlie', {'write'})
```

**Explanation:** `issubset()` checks if the user has ALL required permissions. If not, `required - user_perms` tells us exactly what's missing. Both operations are efficient set operations.

---

### Q4 Solution: Efficient Word Filter

```python
stop_words = {'the', 'a', 'an', 'is', 'in', 'it', 'of', 'and', 'to', 'for',
              'on', 'with', 'at', 'by', 'from', 'or', 'but', 'not', 'this', 'that'}

text = "the quick brown fox is in the garden and it is a beautiful day for a walk in the park"

words = text.split()
total = len(words)

# Filter using set membership — O(1) per word
meaningful = [w for w in words if w not in stop_words]
stop_count = total - len(meaningful)

print(f"Total words: {total}")
print(f"Stop words found: {stop_count}")
print(f"Meaningful words: {len(meaningful)}")
print(f"Filtered: {meaningful}")
```

**Explanation:** Each `w not in stop_words` check is O(1) because `stop_words` is a set. If it were a list, each check would be O(n) where n is the number of stop words. For large texts, this difference is significant.

---

### Q5 Solution: Anagram Checker

```python
def are_anagrams(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

def share_all_letters(word1, word2):
    return set(word1.lower()) == set(word2.lower())

# Anagram tests
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False

# Same unique letters tests
print(share_all_letters("aabb", "ab"))     # True
print(share_all_letters("abc", "abcd"))    # False
```

**Explanation:**
- `are_anagrams` sorts both words and compares — if they have the same characters in the same quantities, the sorted versions are identical.
- `share_all_letters` converts both to sets and compares — sets ignore frequency, so "aabb" and "ab" have the same set `{'a', 'b'}`.
- Set equality check (`==`) verifies both sets contain exactly the same elements.
