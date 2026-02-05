## Editorials: Set Difference and Symmetric Difference

---

### Q1 Solution: Basic Difference Operations

```python
fruits_i_like = {'apple', 'banana', 'mango', 'grape', 'orange'}
fruits_in_stock = {'banana', 'grape', 'kiwi', 'pear', 'orange'}

# 1. Want but unavailable
unavailable = fruits_i_like - fruits_in_stock
print(f"Want but unavailable: {unavailable}")

# 2. Available but don't like
dont_like = fruits_in_stock - fruits_i_like
print(f"Available but don't like: {dont_like}")

# 3. Non-overlapping
non_overlapping = fruits_i_like ^ fruits_in_stock
print(f"Non-overlapping: {non_overlapping}")
```

**Explanation:**
- `fruits_i_like - fruits_in_stock` → items I want that aren't available
- `fruits_in_stock - fruits_i_like` → items available that I don't want
- `fruits_i_like ^ fruits_in_stock` → combines both of the above (everything not shared)

---

### Q2 Solution: Employee Skill Gap

```python
required_skills = {'Python', 'SQL', 'Docker', 'AWS', 'Git'}
alice_skills = {'Python', 'Git', 'JavaScript', 'React'}
bob_skills = {'SQL', 'Docker', 'Python', 'AWS', 'Kubernetes'}

# Alice
alice_missing = required_skills - alice_skills
alice_extra = alice_skills - required_skills
alice_match = len(required_skills & alice_skills)
print(f"Alice missing: {alice_missing}")
print(f"Alice extra: {alice_extra}")

# Bob
bob_missing = required_skills - bob_skills
bob_extra = bob_skills - required_skills
bob_match = len(required_skills & bob_skills)
print(f"Bob missing: {bob_missing}")
print(f"Bob extra: {bob_extra}")

# Compare
if bob_match > alice_match:
    print(f"Bob meets more requirements ({bob_match} vs {alice_match})")
else:
    print(f"Alice meets more requirements ({alice_match} vs {bob_match})")
```

**Explanation:** We use difference to find gaps and extras, and intersection length to count matches.

---

### Q3 Solution: Student Attendance Tracker

```python
enrolled = {'Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace'}
day1 = {'Alice', 'Bob', 'Diana', 'Eve'}
day2 = {'Alice', 'Charlie', 'Eve', 'Frank'}
day3 = {'Bob', 'Charlie', 'Diana', 'Grace'}

# 1. Absent each day
print(f"Absent day 1: {enrolled - day1}")
print(f"Absent day 2: {enrolled - day2}")
print(f"Absent day 3: {enrolled - day3}")

# 2. All three days
all_three = day1 & day2 & day3
print(f"All 3 days: {all_three}")

# 3. None of the days
attended_any = day1 | day2 | day3
none = enrolled - attended_any
print(f"None of the days: {none}")

# 4. Exactly one day
attended_counts = {}
for student in enrolled:
    count = sum([student in day1, student in day2, student in day3])
    attended_counts[student] = count
exactly_one = {s for s, c in attended_counts.items() if c == 1}
print(f"Exactly one day: {exactly_one}")
```

---

### Q4 Solution: Database Sync

```python
local = {'user_1', 'user_2', 'user_3', 'user_4', 'user_5'}
remote = {'user_2', 'user_3', 'user_5', 'user_6', 'user_7'}

upload = local - remote
download = remote - local
synced = local & remote
need_action = local ^ remote

print(f"Upload (local only): {upload}")
print(f"Download (remote only): {download}")
print(f"Already synced: {synced}")
print(f"Need action: {need_action}")

# Perform sync
final = local | remote
print(f"Final synced database: {final}")
```

**Explanation:** Difference identifies what needs to go each direction. Symmetric difference shows everything needing action. Union gives the final merged state.

---

### Q5 Solution: Course Recommendation Engine

```python
courses = {
    'Alice': {'Math', 'Physics', 'Chemistry'},
    'Bob': {'Math', 'Biology', 'History'},
    'Charlie': {'Physics', 'Chemistry', 'Art'},
    'Diana': {'Math', 'Physics', 'Music'}
}

def unique_courses(s1, s2):
    return courses[s1] ^ courses[s2]

def recommend(student, friend):
    return courses[friend] - courses[student]

def exclusive_courses(student):
    others = set()
    for name, c in courses.items():
        if name != student:
            others |= c
    return courses[student] - others

print(f"Unique between Alice & Bob: {unique_courses('Alice', 'Bob')}")
print(f"Recommend for Alice from Diana: {recommend('Alice', 'Diana')}")

for student in courses:
    exc = exclusive_courses(student)
    if exc:
        print(f"{student} exclusive: {exc}")
    else:
        print(f"{student} exclusive: set()")
```

**Explanation:**
- `unique_courses` uses symmetric difference to find courses not shared.
- `recommend` uses difference to find what a friend has that the student doesn't.
- `exclusive_courses` takes the union of everyone else's courses, then differences to find what's unique to one student.
