## Question Bank: Adding Elements to Sets using add() and update()

**Total Duration:** 21 minutes

---

### Q1: Unique Visitor Tracker

**Duration:** 3 minutes
**Difficulty:** Low
**Category:** Implementation
**Type:** Coding

**Problem Statement:**

Create a program that tracks unique visitor IDs to a website. The program should:
- Start with an empty set of visitors
- Add visitor IDs one at a time using the add() method
- Print the total number of unique visitors after all IDs are added

**Input:**
```
5
101
102
101
103
102
```

The first line is the number of visitor IDs. The following lines are visitor IDs (which may contain duplicates).

**Output:**
```
Unique visitors: 3
```

**Constraints:**
- 1 ≤ n ≤ 100
- Visitor IDs are positive integers

---

### Q2: Tag Collection System

**Duration:** 3 minutes
**Difficulty:** Low
**Category:** Implementation
**Type:** Coding

**Problem Statement:**

Write a program that collects tags from multiple articles. Given a list of tag lists, combine all tags into a single set of unique tags using the update() method.

**Input:**
```
3
python tutorial beginner
python advanced tips
javascript tutorial web
```

The first line is the number of articles. Each following line contains space-separated tags for that article.

**Output:**
```
advanced beginner javascript python tips tutorial web
```

(Output should be sorted alphabetically)

**Constraints:**
- 1 ≤ number of articles ≤ 50
- 1 ≤ tags per article ≤ 10
- Tags are single words (lowercase letters)

---

### Q3: Email Deduplication

**Duration:** 5 minutes
**Difficulty:** Medium
**Category:** Implementation
**Type:** Coding

**Problem Statement:**

Create a program that manages email subscriptions. The program should:
1. Accept individual email subscriptions using add()
2. Accept bulk imports from CSV files using update()
3. Handle case-insensitive deduplication (treat "User@Example.com" and "user@example.com" as the same)
4. Track how many new subscribers were added in each operation

**Input:**
```
add alice@example.com
add bob@example.com
import charlie@example.com ALICE@example.com diana@example.com
add eve@example.com
import frank@example.com bob@example.com
done
```

**Output:**
```
Added: alice@example.com (Total: 1)
Added: bob@example.com (Total: 2)
Imported 2 new subscribers (Total: 4)
Added: eve@example.com (Total: 5)
Imported 1 new subscribers (Total: 6)
Final subscribers: 6
```

**Constraints:**
- Operations ≤ 100
- Email addresses are valid format
- Import can have 1-10 emails space-separated

---

### Q4: Permission Manager

**Duration:** 5 minutes
**Difficulty:** Medium
**Category:** Application
**Type:** Coding

**Problem Statement:**

Build a simple user permission management system. The system should:
1. Support granting individual permissions using add()
2. Support granting role-based permissions using update()
3. Check if a user has a specific permission
4. Display all current permissions

Define these roles:
- VIEWER: ['read']
- EDITOR: ['read', 'write', 'edit']
- ADMIN: ['read', 'write', 'edit', 'delete', 'manage_users']

**Input:**
```
grant read
grant write
grant_role ADMIN
check delete
check upload
show
done
```

**Output:**
```
Granted: read
Granted: write
Granted role ADMIN: 3 new permissions
Has permission 'delete': True
Has permission 'upload': False
Permissions: delete edit manage_users read write
```

**Constraints:**
- Operations ≤ 50
- Permission names are single words (lowercase letters + underscores)
- Role names: VIEWER, EDITOR, ADMIN

---

### Q5: Event Attendance Tracker

**Duration:** 5 minutes
**Difficulty:** Medium
**Category:** Application
**Type:** Coding

**Problem Statement:**

Create a system to track event attendance across multiple sessions. The program should:
1. Track attendees for each session
2. Find total unique attendees across all sessions
3. Find attendees who came to multiple sessions
4. Calculate attendance statistics

**Input:**
```
3
Session1: Alice Bob Charlie
Session2: Bob Diana Eve
Session3: Alice Bob Frank
```

The first line is the number of sessions. Each following line has session name and attendees.

**Output:**
```
Total unique attendees: 6
Attendees in multiple sessions: Alice Bob
Most frequent attendee: Bob (3 sessions)
Sessions held: 3
Average unique per session: 3.0
```

**Constraints:**
- 1 ≤ sessions ≤ 20
- 1 ≤ attendees per session ≤ 100
- Names are single words (alphabetic characters)

**Notes:**
- "Attendees in multiple sessions" should be sorted alphabetically
- If multiple people have same max attendance, show first alphabetically

---

## Metadata Summary

| Problem | Duration | Difficulty | Prerequisite LOs | Category       | Type   | Key Concepts       |
| ------- | -------- | ---------- | ---------------- | -------------- | ------ | ------------------ |
| Q1      | 3        | Low        | 9.2.10, 9.2.12   | Implementation | Coding | add(), uniqueness  |
| Q2      | 3        | Low        | 9.2.10, 9.2.12   | Implementation | Coding | update(), sorting  |
| Q3      | 5        | Medium     | 9.2.10, 9.2.12   | Implementation | Coding | add(), update(), tracking |
| Q4      | 5        | Medium     | 9.2.10, 9.2.12   | Application    | Coding | roles, permissions |
| Q5      | 5        | Medium     | 9.2.10, 9.2.12   | Application    | Coding | statistics, analysis |
