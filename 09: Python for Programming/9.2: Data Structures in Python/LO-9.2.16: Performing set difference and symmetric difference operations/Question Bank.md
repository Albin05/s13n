## Question Bank: Set Difference and Symmetric Difference Operations

---

### Q1: Basic Difference Operations (3 minutes, Low Difficulty)

Given two sets:
```python
fruits_i_like = {'apple', 'banana', 'mango', 'grape', 'orange'}
fruits_in_stock = {'banana', 'grape', 'kiwi', 'pear', 'orange'}
```

Write a program that prints:
1. Fruits I like that are NOT in stock
2. Fruits in stock that I DON'T like
3. Fruits that are either liked or in stock, but not both

**Expected Output:**
```
Want but unavailable: {'apple', 'mango'}
Available but don't like: {'kiwi', 'pear'}
Non-overlapping: {'apple', 'mango', 'kiwi', 'pear'}
```

**Key Concepts:** Set difference, symmetric difference

---

### Q2: Employee Skill Gap Analysis (3 minutes, Low Difficulty)

```python
required_skills = {'Python', 'SQL', 'Docker', 'AWS', 'Git'}
alice_skills = {'Python', 'Git', 'JavaScript', 'React'}
bob_skills = {'SQL', 'Docker', 'Python', 'AWS', 'Kubernetes'}
```

For each employee, print:
1. Skills they're missing (required but don't have)
2. Extra skills they have (have but not required)
3. Who meets more requirements?

**Expected Output:**
```
Alice missing: {'SQL', 'Docker', 'AWS'}
Alice extra: {'JavaScript', 'React'}
Bob missing: {'Git'}
Bob extra: {'Kubernetes'}
Bob meets more requirements (4 vs 2)
```

**Key Concepts:** Difference for gap analysis, counting matches

---

### Q3: Student Attendance Tracker (5 minutes, Medium Difficulty)

```python
enrolled = {'Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace'}
day1_present = {'Alice', 'Bob', 'Diana', 'Eve'}
day2_present = {'Alice', 'Charlie', 'Eve', 'Frank'}
day3_present = {'Bob', 'Charlie', 'Diana', 'Grace'}
```

Write a program that finds:
1. Students absent on each day
2. Students who attended ALL three days
3. Students who attended NONE of the days
4. Students who attended exactly one day (use symmetric difference and other operations)

**Expected Output:**
```
Absent day 1: {'Charlie', 'Frank', 'Grace'}
Absent day 2: {'Bob', 'Diana', 'Grace'}
Absent day 3: {'Alice', 'Eve', 'Frank'}
All 3 days: set() (no one attended all 3)
None of the days: set()
Exactly one day: {'Frank', 'Grace'}
```

**Key Concepts:** Difference for absences, intersection, complex set logic

---

### Q4: Database Sync (5 minutes, Medium Difficulty)

You have a local database and a remote database with user records:
```python
local_users = {'user_1', 'user_2', 'user_3', 'user_4', 'user_5'}
remote_users = {'user_2', 'user_3', 'user_5', 'user_6', 'user_7'}
```

Write a program that:
1. Finds users to **upload** (in local but not remote)
2. Finds users to **download** (in remote but not local)
3. Finds users already **synced** (in both)
4. Finds all users that need **action** (in one but not both)
5. Performs the sync: start with local, add remote-only, and print final state

**Expected Output:**
```
Upload (local only): {'user_1', 'user_4'}
Download (remote only): {'user_6', 'user_7'}
Already synced: {'user_2', 'user_3', 'user_5'}
Need action: {'user_1', 'user_4', 'user_6', 'user_7'}
Final synced database: {'user_1', 'user_2', 'user_3', 'user_4', 'user_5', 'user_6', 'user_7'}
```

**Key Concepts:** Difference, symmetric difference, union, practical sync logic

---

### Q5: Course Recommendation Engine (5 minutes, Medium Difficulty)

```python
courses = {
    'Alice': {'Math', 'Physics', 'Chemistry'},
    'Bob': {'Math', 'Biology', 'History'},
    'Charlie': {'Physics', 'Chemistry', 'Art'},
    'Diana': {'Math', 'Physics', 'Music'}
}
```

Write functions:
1. `unique_courses(student1, student2)` — courses one has that the other doesn't (symmetric difference)
2. `recommend(student, friend)` — courses the friend takes that the student doesn't (difference)
3. `exclusive_courses(student)` — courses only this student takes (no one else does)

Test with:
- Unique courses between Alice and Bob
- Recommendations for Alice based on Diana
- Exclusive courses for each student

**Expected Output:**
```
Unique between Alice & Bob: {'Physics', 'Chemistry', 'Biology', 'History'}
Recommend for Alice from Diana: {'Music'}
Charlie exclusive: {'Art'}
Bob exclusive: {'Biology', 'History'}
Diana exclusive: {'Music'}
Alice exclusive: set()
```

**Key Concepts:** Symmetric difference, difference, iterating with sets
