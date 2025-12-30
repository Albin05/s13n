## Question Bank: Removing Elements using remove() and discard()

**Total Duration:** 21 minutes

---

### Q1: Shopping Cart Removal

**Duration:** 3 minutes
**Difficulty:** Low
**Category:** Implementation
**Type:** Coding

**Problem Statement:**

Create a program that manages a shopping cart. The program should:
- Accept commands to remove items from the cart
- Use remove() when the item must exist (strict mode)
- Use discard() when the item might not exist (safe mode)
- Handle errors appropriately

**Input:**
```
cart: BOOK001 LAPTOP042 MOUSE015
strict MOUSE015
safe PHONE099
strict BOOK001
safe BOOK001
show
```

First line: initial cart items (space-separated)
Following lines: commands in format "mode item" where mode is "strict" or "safe"
Last command: "show" to display final cart

**Output:**
```
Removed MOUSE015 (strict)
Item PHONE099 safely removed (safe)
Removed BOOK001 (strict)
Item BOOK001 safely removed (safe)
Final cart: LAPTOP042
```

**Constraints:**
- 1 ≤ items in cart ≤ 20
- Item IDs are alphanumeric strings
- 1 ≤ commands ≤ 30

---

### Q2: Session Manager

**Duration:** 3 minutes
**Difficulty:** Low
**Category:** Implementation
**Type:** Coding

**Problem Statement:**

Write a program that manages active user sessions. The program should:
- Track active sessions
- Remove sessions using discard() for safe cleanup
- Report the number of sessions before and after cleanup

**Input:**
```
5
sess_001 sess_002 sess_003 sess_004 sess_005
3
sess_002 sess_006 sess_004
```

First line: number of initial sessions
Second line: space-separated session IDs
Third line: number of sessions to remove
Fourth line: space-separated session IDs to remove (some may not exist)

**Output:**
```
Initial sessions: 5
Removing sess_002... found and removed
Removing sess_006... not found
Removing sess_004... found and removed
Active sessions: 3
Remaining: sess_001 sess_003 sess_005
```

**Constraints:**
- 1 ≤ initial sessions ≤ 50
- 1 ≤ sessions to remove ≤ 50
- Session IDs format: sess_NNN

---

### Q3: Feature Flag Manager

**Duration:** 5 minutes
**Difficulty:** Medium
**Category:** Implementation
**Type:** Coding

**Problem Statement:**

Create a feature flag management system that:
1. Starts with a set of enabled features
2. Processes enable/disable commands
3. Uses discard() for safe disable operations
4. Reports feature status after each command
5. Validates that critical features cannot be disabled

Critical features: ['authentication', 'security']

**Input:**
```
5
authentication security logging analytics dashboard
disable logging
disable authentication
enable notifications
disable analytics
status
```

First line: number of initial features
Second line: space-separated feature names
Following lines: commands (enable/disable feature_name or status)

**Output:**
```
Disabled logging (5 → 4 features)
Cannot disable critical feature: authentication
Enabled notifications (4 → 5 features)
Disabled analytics (5 → 4 features)
Active features: authentication dashboard notifications security
Critical features intact: authentication security
```

**Constraints:**
- 1 ≤ features ≤ 30
- Feature names are lowercase words
- Critical features cannot be disabled
- 1 ≤ commands ≤ 50

---

### Q4: Email Subscription Cleanup

**Duration:** 5 minutes
**Difficulty:** Medium
**Category:** Application
**Type:** Coding

**Problem Statement:**

Build an email subscription cleanup system that:
1. Maintains a set of subscriber emails
2. Processes unsubscribe requests (safe removal with discard)
3. Processes bulk cleanup (remove bounced emails)
4. Handles case-insensitive email matching
5. Reports cleanup statistics

**Input:**
```
6
alice@example.com bob@test.com charlie@example.com diana@test.com eve@mail.com frank@example.com
unsubscribe alice@example.com
unsubscribe ALICE@EXAMPLE.COM
bulk_cleanup test.com
unsubscribe george@nowhere.com
report
```

First line: number of subscribers
Second line: space-separated email addresses
Following lines: commands (unsubscribe email, bulk_cleanup domain, or report)

**Output:**
```
Unsubscribed: alice@example.com (6 → 5)
Already unsubscribed: alice@example.com
Bulk cleanup for test.com: removed 2 emails (5 → 3)
Not subscribed: george@nowhere.com
--- Subscription Report ---
Total subscribers: 3
Subscribers: charlie@example.com eve@mail.com frank@example.com
```

**Constraints:**
- 1 ≤ subscribers ≤ 100
- Valid email format
- Case-insensitive matching
- 1 ≤ commands ≤ 50

---

### Q5: Task Queue Processor

**Duration:** 5 minutes
**Difficulty:** Medium
**Category:** Application
**Type:** Coding

**Problem Statement:**

Create a task queue processing system that:
1. Maintains pending, processing, and completed task sets
2. Moves tasks between states using remove() and discard()
3. Handles task state transitions safely
4. Detects and reports invalid transitions
5. Provides queue statistics

Task lifecycle: pending → processing → completed

**Input:**
```
pending: task1 task2 task3 task4 task5
start task1
start task6
complete task1
complete task1
start task2
fail task2
start task3
complete task3
stats
```

First line: initial pending tasks
Following lines: commands (start/complete/fail task_id, or stats)

**Output:**
```
Started task1 (pending → processing)
Cannot start task6: not in pending queue
Completed task1 (processing → completed)
Cannot complete task1: not in processing
Started task2 (pending → processing)
Failed task2 (processing → pending)
Started task3 (pending → processing)
Completed task3 (processing → completed)
--- Queue Statistics ---
Pending: 3 tasks (task2 task4 task5)
Processing: 0 tasks ()
Completed: 2 tasks (task1 task3)
```

**Constraints:**
- 1 ≤ initial tasks ≤ 50
- Task IDs are alphanumeric
- 1 ≤ commands ≤ 100
- Valid transitions: pending→processing, processing→completed, processing→pending (fail)

**Notes:**
- Use remove() when you expect the task to be in a specific state
- Use discard() when state is uncertain
- Catch KeyError and provide meaningful messages

---

## Metadata Summary

| Problem | Duration | Difficulty | Prerequisite LOs | Category       | Type   | Key Concepts                |
| ------- | -------- | ---------- | ---------------- | -------------- | ------ | --------------------------- |
| Q1      | 3        | Low        | 9.2.10, 9.2.12   | Implementation | Coding | remove(), discard(), errors |
| Q2      | 3        | Low        | 9.2.10, 9.2.12   | Implementation | Coding | discard(), safe removal     |
| Q3      | 5        | Medium     | 9.2.10, 9.2.12   | Implementation | Coding | validation, critical items  |
| Q4      | 5        | Medium     | 9.2.10, 9.2.12   | Application    | Coding | bulk operations, matching   |
| Q5      | 5        | Medium     | 9.2.10, 9.2.12   | Application    | Coding | state management, workflows |
