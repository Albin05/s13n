## Lecture Script: Adding Elements to Sets using add() and update()

**Duration:** 18 minutes

---

### Hook (2 minutes)

**Scenario:**

You're building a tag system for a blog. Users can add tags to articles:

```python
# Article tags
article_tags = {'python', 'programming'}

# User adds one tag
article_tags.add('tutorial')
print(article_tags)  # {'python', 'programming', 'tutorial'}

# User adds multiple tags from another article
related_tags = ['web', 'django', 'python']  # python is duplicate
article_tags.update(related_tags)
print(article_tags)  
# {'python', 'programming', 'tutorial', 'web', 'django'}
# Duplicates automatically handled!
```

**Today's Focus:**

Master the two methods for adding elements to sets: `add()` for single elements and `update()` for multiple elements.

---

### Section 1: The add() Method (4 minutes)

**What does add() do?**

Adds a single element to the set. If element already exists, nothing happens.

**Syntax:**
```python
set.add(element)
```

**Basic Usage:**
```python
fruits = {'apple', 'banana'}

# Add single element
fruits.add('orange')
print(fruits)  # {'apple', 'banana', 'orange'}

# Add duplicate - no effect
fruits.add('apple')
print(fruits)  # {'apple', 'banana', 'orange'} - unchanged
```

**Key Points:**
- Adds one element at a time
- Silently ignores duplicates
- Modifies set in-place
- No return value (returns None)

**Examples:**

**1. Building a Set Incrementally:**
```python
# Start empty
visited_pages = set()

# Add pages as user visits
visited_pages.add('/home')
visited_pages.add('/about')
visited_pages.add('/contact')
visited_pages.add('/home')  # Duplicate - ignored

print(visited_pages)
# {'/home', '/about', '/contact'}
print(f"Unique pages visited: {len(visited_pages)}")  # 3
```

**2. Conditional Adding:**
```python
valid_codes = {'A100', 'B200', 'C300'}

# Add only if validation passes
new_code = 'D400'
if new_code.startswith(('A', 'B', 'C', 'D')):
    valid_codes.add(new_code)

print(valid_codes)  # {'A100', 'B200', 'C300', 'D400'}
```

**3. User Input Collection:**
```python
interests = set()

# Simulate user adding interests
user_inputs = ['coding', 'music', 'coding', 'sports']

for interest in user_inputs:
    interests.add(interest)
    print(f"Added: {interest}, Total: {len(interests)}")

# Output shows duplicate 'coding' doesn't increase count
print(f"Final interests: {interests}")
# {'coding', 'music', 'sports'}
```

**Common Pattern - Deduplication:**
```python
# Process items, keep unique
seen = set()
unique_items = []

for item in [1, 2, 2, 3, 1, 4]:
    if item not in seen:
        seen.add(item)
        unique_items.append(item)

print(unique_items)  # [1, 2, 3, 4] - order preserved
```

---

### Section 2: The update() Method (5 minutes)

**What does update() do?**

Adds multiple elements from any iterable (list, tuple, set, string, etc.).

**Syntax:**
```python
set.update(iterable)
set.update(iterable1, iterable2, ...)
```

**Basic Usage:**
```python
numbers = {1, 2, 3}

# Update with list
numbers.update([4, 5, 6])
print(numbers)  # {1, 2, 3, 4, 5, 6}

# Update with tuple
numbers.update((7, 8))
print(numbers)  # {1, 2, 3, 4, 5, 6, 7, 8}
```

**Multiple Iterables:**
```python
base_set = {1, 2, 3}

# Update with multiple iterables at once
base_set.update([4, 5], (6, 7), {8, 9})
print(base_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
```

**Automatic Deduplication:**
```python
tags = {'python', 'web'}

# Update with list containing duplicates
new_tags = ['python', 'django', 'flask', 'web', 'api']
tags.update(new_tags)

print(tags)
# {'python', 'web', 'django', 'flask', 'api'}
# Duplicates (python, web) ignored
```

**Update from String:**
```python
# Be careful - strings are iterable!
letters = set()

letters.update('hello')
print(letters)  # {'h', 'e', 'l', 'o'} - individual characters!

# To add whole string, wrap in list
words = set()
words.update(['hello'])
print(words)  # {'hello'}
```

**Examples:**

**1. Combining Data Sources:**
```python
# User preferences from different sources
database_prefs = {'dark_mode', 'notifications'}
cache_prefs = {'auto_save', 'dark_mode'}
default_prefs = {'notifications', 'tips'}

# Combine all
all_prefs = set()
all_prefs.update(database_prefs, cache_prefs, default_prefs)

print(all_prefs)
# {'dark_mode', 'notifications', 'auto_save', 'tips'}
```

**2. Batch Processing:**
```python
# Process multiple log files
all_errors = set()

log1_errors = ['404', '500', '404']
log2_errors = ['403', '500', '502']
log3_errors = ['404', '503']

all_errors.update(log1_errors)
all_errors.update(log2_errors)
all_errors.update(log3_errors)

print(f"Unique error codes: {sorted(all_errors)}")
# ['403', '404', '500', '502', '503']
```

**3. Tag Aggregation:**
```python
# Aggregate tags from multiple articles
all_tags = set()

articles = [
    {'tags': ['python', 'tutorial', 'beginner']},
    {'tags': ['python', 'advanced', 'tips']},
    {'tags': ['javascript', 'tutorial', 'web']}
]

for article in articles:
    all_tags.update(article['tags'])

print(f"All unique tags: {sorted(all_tags)}")
# ['advanced', 'beginner', 'javascript', 'python', 'tips', 'tutorial', 'web']
```

---

### Section 3: add() vs update() (3 minutes)

**When to Use Each:**

**Use add() when:**
- Adding one element at a time
- Building set incrementally in a loop
- Conditional additions

**Use update() when:**
- Adding multiple elements at once
- Combining sets or lists
- Bulk operations

**Comparison:**
```python
# Scenario: Add elements [4, 5, 6] to set

# Method 1: add() - requires loop
numbers = {1, 2, 3}
for num in [4, 5, 6]:
    numbers.add(num)

# Method 2: update() - one line
numbers = {1, 2, 3}
numbers.update([4, 5, 6])

# Both result in: {1, 2, 3, 4, 5, 6}
# update() is cleaner for multiple elements
```

**Performance:**
```python
# update() is faster for multiple elements
import time

# Setup
large_list = list(range(10000))

# Using add() in loop
s1 = set()
start = time.time()
for item in large_list:
    s1.add(item)
time_add = time.time() - start

# Using update()
s2 = set()
start = time.time()
s2.update(large_list)
time_update = time.time() - start

# update() is typically faster
print(f"add() in loop: {time_add:.4f}s")
print(f"update(): {time_update:.4f}s")
```

---

### Section 4: Practical Applications (3 minutes)

**Application 1: Email Subscription List**

```python
class EmailList:
    def __init__(self):
        self.subscribers = set()
    
    def add_subscriber(self, email):
        """Add single subscriber"""
        self.subscribers.add(email.lower())
        print(f"Added: {email}")
    
    def import_subscribers(self, email_list):
        """Import multiple subscribers"""
        before = len(self.subscribers)
        self.subscribers.update(e.lower() for e in email_list)
        after = len(self.subscribers)
        print(f"Imported {after - before} new subscribers")
    
    def get_count(self):
        return len(self.subscribers)

# Usage
newsletter = EmailList()
newsletter.add_subscriber('alice@example.com')
newsletter.add_subscriber('bob@example.com')

# Import from CSV
csv_emails = ['charlie@example.com', 'ALICE@example.com', 'diana@example.com']
newsletter.import_subscribers(csv_emails)

print(f"Total subscribers: {newsletter.get_count()}")  # 4 (alice counted once)
```

**Application 2: Feature Flags**

```python
# Track enabled features
enabled_features = {'login', 'search'}

# Enable single feature
def enable_feature(feature):
    enabled_features.add(feature)
    print(f"Enabled: {feature}")

# Enable multiple features (beta rollout)
def enable_beta_features():
    beta_features = ['advanced_search', 'dark_mode', 'notifications']
    enabled_features.update(beta_features)
    print(f"Beta features enabled: {beta_features}")

# Check feature
def is_enabled(feature):
    return feature in enabled_features

# Usage
enable_feature('profile')
enable_beta_features()

print(f"Dark mode enabled: {is_enabled('dark_mode')}")  # True
print(f"All features: {sorted(enabled_features)}")
```

**Application 3: Permission System**

```python
# User permissions
class User:
    def __init__(self, username):
        self.username = username
        self.permissions = set()
    
    def grant_permission(self, permission):
        """Grant single permission"""
        self.permissions.add(permission)
    
    def grant_role(self, role_permissions):
        """Grant all permissions from a role"""
        self.permissions.update(role_permissions)
    
    def has_permission(self, permission):
        return permission in self.permissions

# Define roles
ADMIN_ROLE = {'read', 'write', 'delete', 'manage_users'}
EDITOR_ROLE = {'read', 'write', 'edit'}
VIEWER_ROLE = {'read'}

# Create user
alice = User('alice')
alice.grant_role(EDITOR_ROLE)  # Grant editor role
alice.grant_permission('delete')  # Add one more permission

print(f"Alice's permissions: {sorted(alice.permissions)}")
# ['delete', 'edit', 'read', 'write']
```

---

### Common Pitfalls (1 minute)

**Pitfall 1: add() with Iterable**
```python
# Wrong - adds whole list as single element
# my_set.add([1, 2, 3])  # TypeError: unhashable type: 'list'

# Right - use update for multiple elements
my_set = set()
my_set.update([1, 2, 3])
```

**Pitfall 2: update() with String**
```python
tags = set()

# Be careful!
tags.update('python')  # Adds: {'p', 'y', 't', 'h', 'o', 'n'}

# To add whole string
tags.update(['python'])  # Adds: {'python'}
```

**Pitfall 3: Expecting Return Value**
```python
# Wrong
result = my_set.add(5)  # result is None!

# Right
my_set.add(5)  # Modifies set in-place
# Then use my_set
```

---

### Summary (1 minute)

**Two Methods for Adding:**

**add(element)**
- Adds one element
- `fruits.add('apple')`
- Use for: single additions, loops, conditions

**update(iterable, ...)**
- Adds multiple elements
- `numbers.update([1, 2, 3])`
- Use for: bulk additions, combining sets

**Key Points:**
- Both modify set in-place
- Both ignore duplicates automatically
- Neither returns a value
- update() is faster for multiple elements
- Elements must be immutable

**Common Patterns:**
```python
# Single addition
tags.add('python')

# Multiple additions
tags.update(['web', 'tutorial', 'code'])

# From multiple sources
all_data.update(source1, source2, source3)

# Conditional
if valid:
    allowed.add(item)
```

**Remember:** Sets automatically handle uniqueness—you can't add duplicates!
