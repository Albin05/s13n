## Question Bank: Applying Set Membership Testing for Efficiency

---

### Q1: Command Validator (3 minutes, Low Difficulty)

Write a program with a set of valid commands: `'start'`, `'stop'`, `'pause'`, `'resume'`, `'help'`, `'quit'`.

Given a list of user inputs:
```python
inputs = ['start', 'STOP', 'fly', 'Pause', 'quit', 'dance', 'help']
```

For each input (case-insensitive), print whether it's valid or invalid.

**Expected Output:**
```
start -> Valid
STOP -> Valid
fly -> Invalid
Pause -> Valid
quit -> Valid
dance -> Invalid
help -> Valid
```

**Key Concepts:** Set membership, case-insensitive checking

---

### Q2: Duplicate Detector (3 minutes, Low Difficulty)

Write a function `find_duplicates(data)` that takes a list and returns a set of elements that appear more than once.

Test with:
```python
print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))  # {2, 3}
print(find_duplicates(['a', 'b', 'c', 'a']))     # {'a'}
print(find_duplicates([1, 2, 3]))                 # set()
```

**Key Concepts:** Set membership for tracking seen elements

---

### Q3: Permission System (5 minutes, Medium Difficulty)

Create a permission checking system:

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
```

Write a function `check_access(username, required_permissions)` that:
1. Gets the user's role and permissions
2. Checks if they have ALL required permissions (subset check)
3. If not, reports which permissions are missing

Test with:
- Alice trying to `{'read', 'delete'}` → Granted
- Bob trying to `{'read', 'write', 'delete'}` → Denied, missing: `{'delete'}`
- Charlie trying to `{'write'}` → Denied, missing: `{'write'}`

**Key Concepts:** Subset checking, difference for missing items

---

### Q4: Efficient Word Filter (5 minutes, Medium Difficulty)

Given a large text and a set of stop words, write an efficient word filter:

```python
stop_words = {'the', 'a', 'an', 'is', 'in', 'it', 'of', 'and', 'to', 'for',
              'on', 'with', 'at', 'by', 'from', 'or', 'but', 'not', 'this', 'that'}

text = "the quick brown fox is in the garden and it is a beautiful day for a walk in the park"
```

1. Split text into words
2. Filter out stop words using set membership (O(1) per check)
3. Count total words, stop words found, and meaningful words
4. Print the meaningful words

**Expected Output:**
```
Total words: 19
Stop words found: 10
Meaningful words: 9
Filtered: ['quick', 'brown', 'fox', 'garden', 'beautiful', 'day', 'walk', 'park']
```

**Key Concepts:** O(1) membership testing, filtering with sets

---

### Q5: Anagram Checker (5 minutes, Medium Difficulty)

Write a function `are_anagrams(word1, word2)` that checks if two words are anagrams (contain exactly the same characters with the same frequencies).

Then write `share_all_letters(word1, word2)` that checks if both words use exactly the same set of unique characters (ignoring frequency).

Test with:
```python
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False

print(share_all_letters("aabb", "ab"))     # True (same unique chars)
print(share_all_letters("abc", "abcd"))    # False
```

**Key Concepts:** Set equality for character comparison, sorted comparison for anagrams
