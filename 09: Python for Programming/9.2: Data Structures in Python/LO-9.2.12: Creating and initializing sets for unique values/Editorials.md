## Editorials: Creating and Initializing Sets for Unique Values

---

### Q1 Solution: Basic Set Creation

```python
# 1. Curly braces — duplicates removed
colors = {'red', 'green', 'blue', 'red'}
print(f"colors: {colors}")
print(f"Type: {type(colors)}, Length: {len(colors)}")

# 2. set() constructor — from list
numbers = set([10, 20, 30, 20, 10])
print(f"numbers: {numbers}")
print(f"Type: {type(numbers)}, Length: {len(numbers)}")

# 3. Empty set
empty = set()
print(f"empty: {empty}")
print(f"Type: {type(empty)}, Length: {len(empty)}")
```

**Explanation:**
- Curly braces with values creates a set. The duplicate `'red'` is removed automatically.
- `set()` with a list creates a set from the list elements, removing duplicates.
- `set()` with no arguments creates an empty set. Using `{}` would create a dict.

---

### Q2 Solution: Duplicate Removal

```python
student_ids = [101, 203, 101, 305, 203, 407, 305, 509, 101, 407]

# 1. Original
print(f"Original: {student_ids}")
print(f"Original count: {len(student_ids)}")

# 2. Convert to set
unique_ids = set(student_ids)
print(f"Unique IDs: {unique_ids}")

# 3. Sorted list
sorted_ids = sorted(unique_ids)
print(f"Sorted unique: {sorted_ids}")

# 4. Count duplicates
duplicates_removed = len(student_ids) - len(unique_ids)
print(f"Duplicates removed: {duplicates_removed}")
```

**Explanation:**
- `set(student_ids)` removes all duplicates, keeping 5 unique IDs from 10 total.
- `sorted()` converts the set to a sorted list since sets are unordered.
- The difference between the original length and unique length tells us how many duplicates existed.

---

### Q3 Solution: Unique Word Counter

```python
text = "the quick brown fox jumps over the lazy dog the fox the dog"

# 1. Split into words
words = text.lower().split()
print(f"Total words: {len(words)}")

# 2. Unique words
unique_words = set(words)
print(f"Unique words: {len(unique_words)}")

# 3. Alphabetical
print(f"Alphabetical: {sorted(unique_words)}")

# 4. Repeated words
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

repeated = {word for word, count in word_counts.items() if count > 1}
print(f"Repeated words: {repeated}")
```

**Explanation:**
- `.lower().split()` normalizes case and splits by whitespace.
- `set(words)` gives unique words. `sorted()` puts them in alphabetical order.
- To find repeated words, we count occurrences with a dictionary, then use a set comprehension to filter words appearing more than once.

---

### Q4 Solution: Visitor Tracking System

```python
morning_visitors = ['user_1', 'user_2', 'user_3', 'user_1', 'user_4']
afternoon_visitors = ['user_2', 'user_5', 'user_3', 'user_6', 'user_2']
evening_visitors = ['user_1', 'user_7', 'user_5', 'user_8', 'user_1']

# 1. Convert to sets
morning = set(morning_visitors)
afternoon = set(afternoon_visitors)
evening = set(evening_visitors)

# 2. Unique per period
print(f"Morning unique: {len(morning)}")
print(f"Afternoon unique: {len(afternoon)}")
print(f"Evening unique: {len(evening)}")

# 3. Total unique (union)
total = morning | afternoon | evening
print(f"Total unique visitors: {len(total)}")

# 4. All periods (intersection)
all_periods = morning & afternoon & evening
print(f"Visitors in all periods: {all_periods}")

# 5. Morning only (difference)
morning_only = morning - afternoon - evening
print(f"Morning only: {morning_only}")
```

**Explanation:**
- Converting lists to sets removes per-period duplicates (e.g., `user_1` visited twice in morning but counts once).
- **Union** (`|`) combines all visitors across periods — each person counted once.
- **Intersection** (`&`) finds visitors present in all three periods.
- **Difference** (`-`) finds visitors who came only in the morning and not in other periods.

---

### Q5 Solution: Email Deduplication

```python
emails = [
    'alice@mail.com', 'Bob@Mail.com', 'alice@mail.com',
    'charlie@mail.com', 'bob@mail.com', 'ALICE@MAIL.COM',
    'diana@mail.com', 'Charlie@Mail.com'
]

# 1. Normalize to lowercase
normalized = [email.lower() for email in emails]

# 2. Unique emails
unique_emails = set(normalized)

# 3. Counts
print(f"Original count: {len(emails)}")
print(f"Unique count: {len(unique_emails)}")

# 4. Find duplicates
seen = set()
duplicates = set()
for email in normalized:
    if email in seen:
        duplicates.add(email)
    seen.add(email)
print(f"Emails with duplicates: {duplicates}")

# 5. Clean sorted list
print("Clean mailing list:")
for email in sorted(unique_emails):
    print(f"  {email}")
```

**Explanation:**
- Emails are case-insensitive, so `'Alice@Mail.com'` and `'alice@mail.com'` are the same. We normalize with `.lower()`.
- Converting to a set removes duplicates. The difference in counts reveals how many were duplicated.
- To identify *which* emails had duplicates, we track seen emails and flag any that appear again.
- `sorted()` gives us a clean, alphabetically ordered mailing list.
