## Editorials: Removing Elements using remove() and discard()

**Duration:** 10 minutes

---

### Q1: Shopping Cart Removal

**Solution:**

```python
# Read initial cart
line = input()
cart = set(line.split(': ')[1].split())

# Process commands
while True:
    command = input().split()

    if command[0] == 'show':
        print(f"Final cart: {' '.join(sorted(cart))}")
        break

    mode = command[0]
    item = command[1]

    if mode == 'strict':
        try:
            cart.remove(item)
            print(f"Removed {item} (strict)")
        except KeyError:
            print(f"Error: {item} not in cart")

    elif mode == 'safe':
        cart.discard(item)
        print(f"Item {item} safely removed (safe)")
```

**Explanation:**

1. Parse initial cart from "cart: ITEM1 ITEM2" format
2. For each command, split into mode and item
3. **strict mode**: Use remove(), catch KeyError if item not found
4. **safe mode**: Use discard(), no error handling needed
5. discard() is idempotent - safe to call multiple times

**Key Learning:** discard() is safer for user-driven operations where duplicate requests are possible.

---

### Q2: Session Manager

**Solution:**

```python
# Read initial sessions
n = int(input())
sessions = set(input().split())

print(f"Initial sessions: {n}")

# Read sessions to remove
m = int(input())
to_remove = input().split()

# Remove each session
for session_id in to_remove:
    if session_id in sessions:
        sessions.discard(session_id)
        print(f"Removing {session_id}... found and removed")
    else:
        print(f"Removing {session_id}... not found")

# Report final state
print(f"Active sessions: {len(sessions)}")
print(f"Remaining: {' '.join(sorted(sessions))}")
```

**Explanation:**

1. Read initial sessions into a set
2. For each session to remove, check if it exists first
3. Use discard() for safe removal (even though we checked, it's good practice)
4. Report whether session was found or not
5. Display final active sessions

**Alternative (simpler but less informative):**

```python
n = int(input())
sessions = set(input().split())
print(f"Initial sessions: {n}")

m = int(input())
to_remove = input().split()

for session_id in to_remove:
    was_present = session_id in sessions
    sessions.discard(session_id)
    status = "found and removed" if was_present else "not found"
    print(f"Removing {session_id}... {status}")

print(f"Active sessions: {len(sessions)}")
print(f"Remaining: {' '.join(sorted(sessions))}")
```

**Key Learning:** Check membership before removal if you need to provide feedback.

---

### Q3: Feature Flag Manager

**Solution:**

```python
# Critical features that cannot be disabled
CRITICAL = {'authentication', 'security'}

# Read initial features
n = int(input())
features = set(input().split())

# Process commands
while True:
    command = input().split()

    if command[0] == 'status':
        print(f"Active features: {' '.join(sorted(features))}")
        critical_intact = CRITICAL.issubset(features)
        if critical_intact:
            print(f"Critical features intact: {' '.join(sorted(CRITICAL))}")
        else:
            print(f"WARNING: Missing critical features!")
        break

    action = command[0]
    feature = command[1]

    if action == 'enable':
        before = len(features)
        features.add(feature)
        after = len(features)
        print(f"Enabled {feature} ({before} → {after} features)")

    elif action == 'disable':
        # Check if critical
        if feature in CRITICAL:
            print(f"Cannot disable critical feature: {feature}")
        else:
            before = len(features)
            features.discard(feature)
            after = len(features)
            print(f"Disabled {feature} ({before} → {after} features)")
```

**Explanation:**

1. Define CRITICAL features as a constant set
2. Check before disabling if feature is critical
3. Use discard() for safe removal (feature might not be enabled)
4. Track feature count before and after to show changes
5. Use issubset() to verify all critical features are present

**Key Learning:** Combine validation logic with safe removal methods.

---

### Q4: Email Subscription Cleanup

**Solution:**

```python
# Read subscribers (case-insensitive storage)
n = int(input())
subscribers = set(email.lower() for email in input().split())

# Process commands
while True:
    command = input().split()

    if command[0] == 'report':
        print("--- Subscription Report ---")
        print(f"Total subscribers: {len(subscribers)}")
        print(f"Subscribers: {' '.join(sorted(subscribers))}")
        break

    elif command[0] == 'unsubscribe':
        email = command[1].lower()
        before = len(subscribers)
        subscribers.discard(email)
        after = len(subscribers)

        if before > after:
            print(f"Unsubscribed: {email} ({before} → {after})")
        else:
            print(f"Already unsubscribed: {email}")

    elif command[0] == 'bulk_cleanup':
        domain = command[1]

        # Find emails from this domain
        to_remove = [email for email in subscribers if email.endswith(domain)]

        before = len(subscribers)
        for email in to_remove:
            subscribers.discard(email)
        after = len(subscribers)

        print(f"Bulk cleanup for {domain}: removed {len(to_remove)} emails ({before} → {after})")
```

**Explanation:**

1. **Case-insensitive**: Convert all emails to lowercase on input
2. **unsubscribe**: Use discard(), check if count changed to detect if email existed
3. **bulk_cleanup**:
   - Find all emails matching domain with list comprehension
   - Remove each safely with discard()
   - Report count of removed emails
4. Compare len() before and after to track changes

**Key Learning:** Use discard() with before/after comparison to provide feedback without checking membership first.

---

### Q5: Task Queue Processor

**Solution:**

```python
# Parse initial pending tasks
line = input()
pending = set(line.split(': ')[1].split())
processing = set()
completed = set()

# Process commands
while True:
    command = input().split()

    if command[0] == 'stats':
        print("--- Queue Statistics ---")
        print(f"Pending: {len(pending)} tasks ({' '.join(sorted(pending))})")
        print(f"Processing: {len(processing)} tasks ({' '.join(sorted(processing))})")
        print(f"Completed: {len(completed)} tasks ({' '.join(sorted(completed))})")
        break

    action = command[0]
    task_id = command[1]

    if action == 'start':
        # Must be in pending to start
        if task_id in pending:
            pending.remove(task_id)
            processing.add(task_id)
            print(f"Started {task_id} (pending → processing)")
        else:
            print(f"Cannot start {task_id}: not in pending queue")

    elif action == 'complete':
        # Must be in processing to complete
        if task_id in processing:
            processing.remove(task_id)
            completed.add(task_id)
            print(f"Completed {task_id} (processing → completed)")
        else:
            print(f"Cannot complete {task_id}: not in processing")

    elif action == 'fail':
        # Must be in processing to fail (move back to pending)
        if task_id in processing:
            processing.remove(task_id)
            pending.add(task_id)
            print(f"Failed {task_id} (processing → pending)")
        else:
            print(f"Cannot fail {task_id}: not in processing")
```

**Explanation:**

1. **Three sets**: pending, processing, completed for task lifecycle
2. **start**: Check membership first, use remove() for validation, add to processing
3. **complete**: Check membership, use remove(), add to completed
4. **fail**: Check membership, use remove(), add back to pending
5. **Validation**: Check membership before remove() to provide meaningful error messages

**Why remove() here instead of discard()?**
- We want to enforce state rules
- If task isn't in expected state, that's an error condition
- Better to validate explicitly with membership check

**Alternative using try-except:**

```python
elif action == 'start':
    try:
        pending.remove(task_id)
        processing.add(task_id)
        print(f"Started {task_id} (pending → processing)")
    except KeyError:
        print(f"Cannot start {task_id}: not in pending queue")
```

**Key Learning:**
- Use remove() when state transitions have strict rules
- Check membership first for better error messages
- OR use try-except to catch KeyError

---

## Common Patterns Summary

1. **Safe User Actions**: Use discard()
   ```python
   cart.discard(item_id)  # User removes item
   ```

2. **State Validation**: Use remove() with try-except or membership check
   ```python
   if task_id in pending:
       pending.remove(task_id)
   ```

3. **Tracking Changes**: Compare len() before and after
   ```python
   before = len(my_set)
   my_set.discard(item)
   after = len(my_set)
   changed = (before != after)
   ```

4. **Bulk Removal**: Use discard() in loop
   ```python
   for item in items_to_remove:
       my_set.discard(item)
   ```

5. **Critical Item Protection**: Check before removing
   ```python
   if item not in PROTECTED:
       my_set.discard(item)
   ```

## Performance Notes

- Both remove() and discard() are O(1) average case
- Membership check `item in set` is also O(1) average case
- Combined check + remove is still O(1)
