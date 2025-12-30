## Lecture Script: Removing Elements using remove() and discard()

**Duration:** 18 minutes

---

### Hook (2 minutes)

**Scenario:**

You're building a shopping cart system. Users can remove items from their cart:

```python
# Shopping cart (items as product IDs)
cart = {'BOOK-001', 'LAPTOP-042', 'MOUSE-015'}

# User removes an item (might not exist if already removed)
item_to_remove = 'MOUSE-015'

# Option 1: remove() - raises error if item doesn't exist
cart.remove(item_to_remove)  # Works

# Option 2: discard() - safe, no error if item doesn't exist
cart.discard('PHONE-099')  # Safe, even though item not in cart

print(cart)  # {'BOOK-001', 'LAPTOP-042'}
```

**The Problem:**
- What if user clicks "remove" twice on the same item?
- What if the item was already removed in another session?
- Should your program crash or handle it gracefully?

**Today's Focus:**

Learn the two methods for removing elements from sets:
- **remove()**: Removes element, raises KeyError if not found
- **discard()**: Removes element, silent if not found

Also explore **pop()** and **clear()** for other removal scenarios.

---

### Section 1: The remove() Method (4 minutes)

**What does remove() do?**

Removes a specified element from the set. Raises KeyError if element doesn't exist.

**Syntax:**
```python
set.remove(element)
```

**Basic Usage:**

```python
fruits = {'apple', 'banana', 'orange'}

# Remove existing element
fruits.remove('banana')
print(fruits)  # {'apple', 'orange'}

# Try to remove non-existent element
fruits.remove('grape')  # KeyError: 'grape'
```

**Key Points:**
- Removes specified element
- Raises KeyError if element not in set
- Modifies set in-place
- No return value (returns None)

**Examples:**

**1. Safe Remove with Try-Except:**

```python
tags = {'python', 'web', 'tutorial'}

# Safe removal
try:
    tags.remove('java')
    print("Removed java")
except KeyError:
    print("Tag 'java' not found")  # This runs

# Alternative: check first
if 'python' in tags:
    tags.remove('python')
    print("Removed python")
```

**2. Removing from User Input:**

```python
active_users = {'alice', 'bob', 'charlie'}

# User logs out
user_to_logout = 'bob'

try:
    active_users.remove(user_to_logout)
    print(f"{user_to_logout} logged out successfully")
    print(f"Active users: {active_users}")
except KeyError:
    print(f"User {user_to_logout} was not logged in")

# Output:
# bob logged out successfully
# Active users: {'alice', 'charlie'}
```

**3. Batch Removal:**

```python
# Remove multiple specific items
inventory = {'item1', 'item2', 'item3', 'item4', 'item5'}
to_remove = ['item2', 'item4', 'item6']  # item6 doesn't exist

for item in to_remove:
    try:
        inventory.remove(item)
        print(f"Removed {item}")
    except KeyError:
        print(f"{item} not in inventory")

print(f"Final inventory: {inventory}")

# Output:
# Removed item2
# Removed item4
# item6 not in inventory
# Final inventory: {'item1', 'item3', 'item5'}
```

**4. Transaction Processing:**

```python
pending_transactions = {'TX001', 'TX002', 'TX003'}

def process_transaction(tx_id):
    """Process and remove transaction"""
    try:
        pending_transactions.remove(tx_id)
        print(f"Transaction {tx_id} processed")
        return True
    except KeyError:
        print(f"Transaction {tx_id} already processed or invalid")
        return False

# Process transactions
process_transaction('TX001')  # Success
process_transaction('TX001')  # Already processed
process_transaction('TX002')  # Success

# Final state
print(f"Remaining: {pending_transactions}")  # {'TX003'}
```

---

### Section 2: The discard() Method (5 minutes)

**What does discard() do?**

Removes a specified element from the set. Does nothing if element doesn't exist (no error).

**Syntax:**
```python
set.discard(element)
```

**Basic Usage:**

```python
fruits = {'apple', 'banana', 'orange'}

# Discard existing element
fruits.discard('banana')
print(fruits)  # {'apple', 'orange'}

# Discard non-existent element - no error!
fruits.discard('grape')
print(fruits)  # {'apple', 'orange'} - unchanged, no error
```

**Key Points:**
- Removes specified element if present
- Silent operation if element not in set (no error)
- Safer than remove() for uncertain cases
- Modifies set in-place
- No return value (returns None)

**Examples:**

**1. Idempotent Operations:**

```python
# User preferences
enabled_features = {'dark_mode', 'notifications', 'auto_save'}

# Disable feature - safe to call multiple times
def disable_feature(feature):
    enabled_features.discard(feature)
    print(f"Feature '{feature}' disabled")

# Call multiple times - no error
disable_feature('notifications')  # Removes it
disable_feature('notifications')  # Safe, already removed
disable_feature('beta_access')    # Safe, never existed

print(enabled_features)  # {'dark_mode', 'auto_save'}
```

**2. Cleanup Operations:**

```python
# Active sessions
sessions = {'sess_001', 'sess_002', 'sess_003'}

# Cleanup expired sessions (might already be removed)
expired = ['sess_002', 'sess_004', 'sess_005']

for session in expired:
    sessions.discard(session)  # Safe even if already gone

print(f"Active sessions: {sessions}")  # {'sess_001', 'sess_003'}
```

**3. Tag Removal System:**

```python
class Article:
    def __init__(self, title):
        self.title = title
        self.tags = set()

    def add_tag(self, tag):
        self.tags.add(tag)

    def remove_tag(self, tag):
        """Safe tag removal"""
        self.tags.discard(tag)  # Won't error if tag doesn't exist

    def remove_tags(self, tags_to_remove):
        """Remove multiple tags safely"""
        for tag in tags_to_remove:
            self.tags.discard(tag)

# Usage
article = Article("Python Sets Guide")
article.tags = {'python', 'tutorial', 'beginner'}

# Remove tags (some may not exist)
article.remove_tag('advanced')      # Safe, doesn't exist
article.remove_tag('beginner')      # Removes it
article.remove_tags(['draft', 'python'])  # Removes python, ignores draft

print(article.tags)  # {'tutorial'}
```

**4. Filter Removal:**

```python
# Email blocklist
blocklist = {'spam@example.com', 'bad@test.com', 'fake@mail.com'}

# Remove emails matching pattern
def remove_by_domain(domain):
    """Remove all emails from specific domain"""
    to_remove = [email for email in blocklist if email.endswith(domain)]

    for email in to_remove:
        blocklist.discard(email)  # Safe removal

    print(f"Removed {len(to_remove)} emails from {domain}")

# Remove all @test.com emails
remove_by_domain('@test.com')

print(f"Blocklist: {blocklist}")
# {'spam@example.com', 'fake@mail.com'}
```

**5. State Management:**

```python
# Download manager
class DownloadManager:
    def __init__(self):
        self.active_downloads = set()
        self.completed = set()

    def start_download(self, file_id):
        self.active_downloads.add(file_id)
        print(f"Started: {file_id}")

    def complete_download(self, file_id):
        """Mark download complete - safe even if not active"""
        self.active_downloads.discard(file_id)  # Safe removal
        self.completed.add(file_id)
        print(f"Completed: {file_id}")

# Usage
dm = DownloadManager()
dm.start_download('file1')
dm.start_download('file2')

dm.complete_download('file1')
dm.complete_download('file1')  # Called twice - no error!
dm.complete_download('file3')  # Never started - no error!

print(f"Active: {dm.active_downloads}")      # {'file2'}
print(f"Completed: {dm.completed}")          # {'file1', 'file3'}
```

---

### Section 3: remove() vs discard() (3 minutes)

**When to Use Each:**

**Use remove() when:**
- You KNOW the element exists
- You WANT an error if it doesn't exist (debugging)
- Absence of element indicates a problem
- Strict validation is needed

**Use discard() when:**
- Element might not exist
- You want safe, silent removal
- Idempotent operations needed
- User-driven removal (clicks, requests)

**Comparison Table:**

| Feature                   | remove()          | discard()      |
| ------------------------- | ----------------- | -------------- |
| Element not found         | Raises KeyError   | Does nothing   |
| Safe for uncertain cases  | No                | Yes            |
| Returns value             | None              | None           |
| Modifies set              | Yes               | Yes            |
| Use for validation        | Yes               | No             |
| Use for user actions      | Risky             | Recommended    |

**Side-by-Side Examples:**

```python
colors = {'red', 'blue', 'green'}

# Scenario 1: remove()
try:
    colors.remove('yellow')  # KeyError!
except KeyError:
    print("Color not found - must handle error")

# Scenario 2: discard()
colors.discard('yellow')  # Safe, no error
print("Operation completed successfully")

# Scenario 3: When remove() is better
# You EXPECT the element to exist - error helps catch bugs
active_connections = {'conn1', 'conn2', 'conn3'}

def close_connection(conn_id):
    """Close connection - should always exist when called"""
    try:
        active_connections.remove(conn_id)
    except KeyError:
        # This indicates a bug in our logic!
        raise Exception(f"BUG: Trying to close non-existent connection {conn_id}")

# Scenario 4: When discard() is better
# User might remove same item multiple times
shopping_cart = {'item1', 'item2', 'item3'}

def remove_from_cart(item_id):
    """Remove from cart - user might click twice"""
    shopping_cart.discard(item_id)  # Safe for duplicate clicks
    return f"Cart updated"
```

**Performance:**
Both methods have O(1) average time complexity - performance is identical.

---

### Section 4: Additional Removal Methods (3 minutes)

**Method 1: pop()**

Removes and returns an arbitrary element. Raises KeyError if set is empty.

```python
numbers = {1, 2, 3, 4, 5}

# Remove arbitrary element
removed = numbers.pop()
print(f"Removed: {removed}")  # Could be any element
print(f"Remaining: {numbers}")

# Pop from empty set - error!
empty_set = set()
# removed = empty_set.pop()  # KeyError: 'pop from an empty set'

# Safe pop
if empty_set:
    removed = empty_set.pop()
else:
    print("Set is empty")
```

**Use Cases for pop():**

```python
# Process items one by one
tasks = {'task1', 'task2', 'task3', 'task4'}

while tasks:
    current_task = tasks.pop()
    print(f"Processing {current_task}")
    # Process the task...

print("All tasks completed")

# Random selection and removal
contestants = {'Alice', 'Bob', 'Charlie', 'Diana'}

winner = contestants.pop()
print(f"Winner: {winner}")
print(f"Runners-up: {contestants}")
```

**Method 2: clear()**

Removes all elements from the set.

```python
fruits = {'apple', 'banana', 'orange', 'grape'}

print(f"Before: {fruits}")
fruits.clear()
print(f"After: {fruits}")   # set()
print(f"Length: {len(fruits)}")  # 0
```

**Use Cases for clear():**

```python
# Reset system state
class GameSession:
    def __init__(self):
        self.active_players = set()
        self.power_ups = set()

    def start_round(self):
        # Clear previous round data
        self.power_ups.clear()
        print("Round started with clean state")

    def end_game(self):
        # Clear all data
        self.active_players.clear()
        self.power_ups.clear()
        print("Game ended, all data cleared")

# Temporary storage
temp_cache = {'item1', 'item2', 'item3'}

# Process items...
# Then clear cache
temp_cache.clear()
```

**Comparison of All Removal Methods:**

```python
s = {1, 2, 3, 4, 5}

# remove(x) - remove specific element, error if not exists
s.remove(3)  # Removes 3, error if 3 not in set

# discard(x) - remove specific element, silent if not exists
s.discard(10)  # Safe, no error

# pop() - remove arbitrary element, error if empty
x = s.pop()  # Removes and returns some element

# clear() - remove all elements
s.clear()  # Empties the set
```

---

### Common Pitfalls (1 minute)

**Pitfall 1: Using remove() with Uncertain Data**

```python
# Bad - might crash
user_tags = {'python', 'web'}
user_tags.remove('java')  # KeyError if not present!

# Good - use discard or check first
user_tags.discard('java')  # Safe

# Or
if 'java' in user_tags:
    user_tags.remove('java')
```

**Pitfall 2: Forgetting pop() is Random**

```python
# Bad - assuming order
numbers = {1, 2, 3, 4, 5}
first = numbers.pop()  # NOT guaranteed to be 1!

# Good - sets are unordered
numbers = {1, 2, 3, 4, 5}
any_number = numbers.pop()  # Acknowledge it's arbitrary
```

**Pitfall 3: Modifying Set During Iteration**

```python
# Bad - RuntimeError possible
tags = {'python', 'java', 'cpp', 'go'}
for tag in tags:
    if tag.startswith('j'):
        tags.remove(tag)  # Dangerous!

# Good - iterate over copy
tags = {'python', 'java', 'cpp', 'go'}
for tag in tags.copy():
    if tag.startswith('j'):
        tags.discard(tag)  # Safe

# Better - use set comprehension
tags = {tag for tag in tags if not tag.startswith('j')}
```

---

### Summary (1 minute)

**Four Methods for Removing Elements:**

**remove(element)**
- Removes specified element
- Raises KeyError if not found
- Use when: element must exist

**discard(element)**
- Removes specified element
- Silent if not found
- Use when: element might not exist

**pop()**
- Removes arbitrary element
- Returns the removed element
- Raises KeyError if set empty
- Use when: need any element

**clear()**
- Removes all elements
- Empties the set
- Use when: reset needed

**Key Decision Tree:**

```
Need to remove element?
├─ Remove ALL elements → clear()
├─ Remove ANY element → pop()
└─ Remove SPECIFIC element
   ├─ Must exist (validation) → remove()
   └─ Might not exist (safe) → discard()
```

**Common Patterns:**

```python
# Safe removal
my_set.discard(item)

# Removal with validation
try:
    my_set.remove(item)
except KeyError:
    handle_error()

# Remove all
my_set.clear()

# Process and remove
while my_set:
    item = my_set.pop()
    process(item)
```

**Remember:**
- discard() is almost always safer than remove()
- Use remove() only when you need strict validation
- Both have O(1) performance
- Sets are modified in-place
