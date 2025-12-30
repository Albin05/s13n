## Editorials: Adding Elements to Sets using add() and update()

**Duration:** 10 minutes

---

### Q1: Unique Visitor Tracker

**Solution:**

```python
# Read number of visitor IDs
n = int(input())

# Create empty set for visitors
visitors = set()

# Add each visitor ID
for _ in range(n):
    visitor_id = int(input())
    visitors.add(visitor_id)

# Print result
print(f"Unique visitors: {len(visitors)}")
```

**Explanation:**

1. **Initialize empty set:** `visitors = set()` creates a new empty set
2. **Loop through inputs:** Read n visitor IDs one at a time
3. **Add using add():** `visitors.add(visitor_id)` adds each ID to the set
4. **Automatic deduplication:** Sets automatically ignore duplicate values
5. **Count unique:** `len(visitors)` gives the number of unique visitors

**Key Concept:** The add() method automatically handles duplicates - adding the same value multiple times has no effect.

**Time Complexity:** O(n) where n is the number of IDs
**Space Complexity:** O(k) where k is the number of unique IDs

---

### Q2: Tag Collection System

**Solution:**

```python
# Read number of articles
n = int(input())

# Create empty set for all tags
all_tags = set()

# Process each article
for _ in range(n):
    # Read tags for this article and split into list
    tags = input().split()

    # Add all tags using update()
    all_tags.update(tags)

# Print sorted tags
print(' '.join(sorted(all_tags)))
```

**Explanation:**

1. **Initialize empty set:** `all_tags = set()` for storing unique tags
2. **Read and split:** `input().split()` converts "python tutorial beginner" to ['python', 'tutorial', 'beginner']
3. **Update with list:** `all_tags.update(tags)` adds all tags from the list at once
4. **Automatic deduplication:** Duplicate tags across articles are automatically handled
5. **Sort and display:** `sorted(all_tags)` returns alphabetically sorted list

**Why update() instead of add():**
- update() accepts an iterable (list of tags)
- add() would add the entire list as one element (and fail because lists are unhashable)
- update() is more efficient than looping with add()

**Time Complexity:** O(n*m) where n is articles and m is average tags per article
**Space Complexity:** O(t) where t is total unique tags

---

### Q3: Email Deduplication

**Solution:**

```python
# Initialize subscribers set
subscribers = set()

# Process commands
while True:
    command = input().split()

    if command[0] == 'done':
        break

    elif command[0] == 'add':
        email = command[1].lower()
        subscribers.add(email)
        print(f"Added: {email} (Total: {len(subscribers)})")

    elif command[0] == 'import':
        # Get all emails after 'import' keyword
        emails = command[1:]

        # Track count before import
        before = len(subscribers)

        # Add all emails (case-insensitive)
        subscribers.update(e.lower() for e in emails)

        # Calculate new subscribers
        after = len(subscribers)
        new_count = after - before

        print(f"Imported {new_count} new subscribers (Total: {after})")

# Final count
print(f"Final subscribers: {len(subscribers)}")
```

**Explanation:**

1. **Command parsing:** Split input to separate command from arguments
2. **Case normalization:** `.lower()` ensures case-insensitive deduplication
3. **add() for single:** Use add() when adding one email at a time
4. **update() for bulk:** Use update() with generator expression for multiple emails
5. **Track changes:** Compare set size before and after to count new additions
6. **Generator expression:** `(e.lower() for e in emails)` normalizes emails during update

**Key Insight:**
- Generator expression `(e.lower() for e in emails)` is memory-efficient
- Could also use list comprehension `[e.lower() for e in emails]`
- Set automatically prevents duplicates even within the import list

**Time Complexity:** O(n) where n is total emails processed
**Space Complexity:** O(u) where u is unique emails

---

### Q4: Permission Manager

**Solution:**

```python
# Define role permissions
ROLES = {
    'VIEWER': ['read'],
    'EDITOR': ['read', 'write', 'edit'],
    'ADMIN': ['read', 'write', 'edit', 'delete', 'manage_users']
}

# Initialize permissions set
permissions = set()

# Process commands
while True:
    command = input().split()

    if command[0] == 'done':
        break

    elif command[0] == 'grant':
        permission = command[1]
        permissions.add(permission)
        print(f"Granted: {permission}")

    elif command[0] == 'grant_role':
        role_name = command[1]
        role_perms = ROLES[role_name]

        # Track new permissions
        before = len(permissions)
        permissions.update(role_perms)
        after = len(permissions)
        new_count = after - before

        print(f"Granted role {role_name}: {new_count} new permissions")

    elif command[0] == 'check':
        permission = command[1]
        has_perm = permission in permissions
        print(f"Has permission '{permission}': {has_perm}")

    elif command[0] == 'show':
        print(f"Permissions: {' '.join(sorted(permissions))}")
```

**Explanation:**

1. **Role definition:** Dictionary maps role names to permission lists
2. **add() for individual:** Single permission granted with add()
3. **update() for roles:** All role permissions added at once with update()
4. **Membership testing:** `permission in permissions` is O(1) average case
5. **Count new permissions:** Some role permissions may already exist
6. **Display sorted:** Shows permissions in alphabetical order

**Design Choice:**
- Using set for permissions enables fast lookup (O(1) vs O(n) for list)
- update() prevents duplicate permissions automatically
- Role-based access control (RBAC) is common security pattern

**Time Complexity:** O(1) for grant/check, O(r) for grant_role where r is role size
**Space Complexity:** O(p) where p is unique permissions

---

### Q5: Event Attendance Tracker

**Solution:**

```python
# Read number of sessions
n = int(input())

# Track all unique attendees and attendance count per person
all_attendees = set()
attendance_count = {}
session_names = []

# Process each session
for _ in range(n):
    line = input()

    # Parse session: "Session1: Alice Bob Charlie"
    parts = line.split(': ')
    session_name = parts[0]
    attendees = parts[1].split()

    session_names.append(session_name)

    # Add to overall set
    all_attendees.update(attendees)

    # Count attendance for each person
    for person in attendees:
        attendance_count[person] = attendance_count.get(person, 0) + 1

# Find attendees in multiple sessions
multiple_sessions = sorted([
    person for person, count in attendance_count.items() if count > 1
])

# Find most frequent attendee
max_attendance = max(attendance_count.values())
most_frequent = sorted([
    person for person, count in attendance_count.items()
    if count == max_attendance
])[0]

# Calculate average
total_session_attendees = sum(len(s.split(': ')[1].split())
                               for s in session_names)
avg_per_session = sum(len(set(s.split(': ')[1].split()))
                       for s in session_names) / n

# Output results
print(f"Total unique attendees: {len(all_attendees)}")
print(f"Attendees in multiple sessions: {' '.join(multiple_sessions)}")
print(f"Most frequent attendee: {most_frequent} ({max_attendance} sessions)")
print(f"Sessions held: {n}")
print(f"Average unique per session: {avg_per_session:.1f}")
```

**Alternative Cleaner Solution:**

```python
n = int(input())

all_attendees = set()
attendance_count = {}
session_data = []

# Collect data
for _ in range(n):
    line = input()
    session_name, attendees_str = line.split(': ')
    attendees = set(attendees_str.split())

    session_data.append(attendees)
    all_attendees.update(attendees)

    for person in attendees:
        attendance_count[person] = attendance_count.get(person, 0) + 1

# Analysis
multiple_sessions = sorted([p for p, c in attendance_count.items() if c > 1])
max_count = max(attendance_count.values())
most_frequent = sorted([p for p, c in attendance_count.items() if c == max_count])[0]
avg_unique = sum(len(s) for s in session_data) / n

# Output
print(f"Total unique attendees: {len(all_attendees)}")
print(f"Attendees in multiple sessions: {' '.join(multiple_sessions)}")
print(f"Most frequent attendee: {most_frequent} ({max_count} sessions)")
print(f"Sessions held: {n}")
print(f"Average unique per session: {avg_unique:.1f}")
```

**Explanation:**

1. **Data structures:**
   - `all_attendees`: set for unique attendees across all sessions
   - `attendance_count`: dict to track how many sessions each person attended
   - `session_data`: list of sets, one per session

2. **update() usage:** `all_attendees.update(attendees)` adds all attendees from current session

3. **Frequency counting:** Dictionary tracks attendance count per person

4. **Multiple sessions:** List comprehension filters people with count > 1

5. **Most frequent:**
   - Find max count
   - Filter people with max count
   - Sort alphabetically and take first (tie-breaking)

6. **Statistics:** Calculate average unique attendees per session

**Key Concepts:**
- Combining sets with update() for union operation
- Using dictionary for counting/aggregation
- List comprehensions for filtering
- Set provides O(1) membership testing

**Time Complexity:** O(n*m) where n is sessions and m is average attendees
**Space Complexity:** O(a) where a is total unique attendees

---

## Common Patterns Used

1. **Deduplication:** Using set's automatic uniqueness
2. **Bulk Addition:** update() for adding multiple elements
3. **Tracking Changes:** Comparing len() before and after
4. **Case Normalization:** Converting to lowercase for case-insensitive comparison
5. **Generator Expressions:** Memory-efficient transformation during update()
6. **Membership Testing:** Fast O(1) lookups with `in` operator

## Performance Tips

1. Use update() instead of looping with add() for multiple elements
2. Generator expressions with update() are memory-efficient
3. Set membership testing is O(1) average case
4. Combining sets is faster than manual iteration
