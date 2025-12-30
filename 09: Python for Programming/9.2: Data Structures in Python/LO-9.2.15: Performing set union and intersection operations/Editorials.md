## Editorials: Performing Set Union and Intersection Operations

**Duration:** 10 minutes

---

### Q1: Common Interests Finder

**Solution:**

```python
n = int(input())
users = {}

# Read user interests
for _ in range(n):
    line = input().split(': ')
    name = line[0]
    interests = set(line[1].split())
    users[name] = interests

# Find pairwise intersections
names = list(users.keys())
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        common = users[names[i]] & users[names[j]]
        print(f"{names[i].title()} & {names[j].title()}: {' '.join(sorted(common))}")

# Find common to all
all_common = set.intersection(*users.values())
print(f"All three: {' '.join(sorted(all_common))}")
```

**Key Learning:** Use `&` operator to find intersection (common elements). `set.intersection(*list)` unpacks multiple sets.

---

### Q2: Subscriber List Merger

**Solution:**

```python
n = int(input())
all_subscribers = set()

for _ in range(n):
    line = input().split(': ')
    emails = set(line[1].split())
    all_subscribers = all_subscribers | emails

print(f"Total unique subscribers: {len(all_subscribers)}")
print(f"Subscribers: {' '.join(sorted(all_subscribers))}")
```

**Key Learning:** Use `|` operator for union to merge sets. Union automatically removes duplicates.

---

### Q3: Multi-Platform User Analysis

**Solution:**

```python
platforms = {}
for _ in range(3):
    line = input().split(': ')
    platform = line[0]
    users = set(line[1].split())
    platforms[platform] = users

web = platforms['web']
mobile = platforms['mobile']
desktop = platforms['desktop']

# All platforms
all_platforms = web & mobile & desktop
print(f"Active on all platforms: {' '.join(sorted(all_platforms))}")

# At least 2 platforms
at_least_two = (web & mobile) | (mobile & desktop) | (web & desktop)
print(f"Active on at least 2 platforms: {' '.join(sorted(at_least_two))}")

# Platform-exclusive users
web_only = web - mobile - desktop
mobile_only = mobile - web - desktop
desktop_only = desktop - web - mobile

print(f"Web only: {' '.join(sorted(web_only))}")
print(f"Mobile only: {' '.join(sorted(mobile_only))}")
print(f"Desktop only: {' '.join(sorted(desktop_only))}")

# Total unique
all_users = web | mobile | desktop
print(f"Total unique users: {len(all_users)}")
```

**Key Learning:** Combine `&`, `|`, and `-` operators for complex set analysis.

---

### Q4: Product Feature Comparison

**Solution:**

```python
n = int(input())
products = {}

for _ in range(n):
    line = input().split(': ')
    name = line[0]
    features = set(line[1].split())
    products[name] = features

# Categories
budget_line = input().split(': ')
budget_products = budget_line[1].split()
premium_line = input().split(': ')
premium_products = premium_line[1].split()

# Common to all products
common_all = set.intersection(*products.values())
print(f"Common to all products: {' '.join(sorted(common_all))}")

# Budget features
budget_features = set.union(*[products[p] for p in budget_products])
print(f"Budget models offer: {' '.join(sorted(budget_features))}")

# Premium features
premium_features = set.union(*[products[p] for p in premium_products])
print(f"Premium models offer: {' '.join(sorted(premium_features))}")

# Exclusives
exclusive_budget = budget_features - premium_features
exclusive_premium = premium_features - budget_features
print(f"Exclusive to budget: {' '.join(sorted(exclusive_budget))}")
print(f"Exclusive to premium: {' '.join(sorted(exclusive_premium))}")

# Best value
max_features = max(len(f) for f in products.values())
best_value = [name for name, features in products.items() if len(features) == max_features]
print(f"Best value (most features): {' '.join(best_value)} ({max_features} features each)")
```

**Key Learning:** Use `set.union(*list)` and `set.intersection(*list)` to operate on multiple sets at once.

---

### Q5: Course Enrollment System

**Solution:**

```python
n = int(input())
courses = {}

for _ in range(n):
    line = input().split(': ')
    course = line[0]
    students = set(line[1].split())
    courses[course] = students

while True:
    command = input().strip()

    if command == 'find_taking_multiple':
        # Find students in multiple courses
        student_courses = {}
        for course, students in courses.items():
            for student in students:
                if student not in student_courses:
                    student_courses[student] = []
                student_courses[student].append(course)

        print("Students taking multiple courses:")
        for student in sorted(student_courses.keys()):
            if len(student_courses[student]) > 1:
                course_list = ' '.join(sorted(student_courses[student]))
                print(f"- {student}: {len(student_courses[student])} courses ({course_list})")

    elif command == 'find_course_pairs':
        print("\nCourse pairs with shared students:")
        course_names = list(courses.keys())
        for i in range(len(course_names)):
            for j in range(i + 1, len(course_names)):
                shared = courses[course_names[i]] & courses[course_names[j]]
                if shared:
                    print(f"- {course_names[i]} & {course_names[j]}: {len(shared)} student{'s' if len(shared) > 1 else ''} ({' '.join(sorted(shared))})")

    elif command.startswith('recommend'):
        student = command.split()[1]

        # Find courses the student is taking
        student_courses = [c for c, students in courses.items() if student in students]

        # Find classmates
        classmates = set()
        for course in student_courses:
            classmates |= courses[course]
        classmates.discard(student)

        # Find courses classmates are taking
        recommendations = {}
        for classmate in classmates:
            for course, students in courses.items():
                if classmate in students and course not in student_courses:
                    recommendations[course] = recommendations.get(course, 0) + 1

        print(f"\nRecommendations for {student} (based on classmates):")
        for course in sorted(recommendations.keys(), key=lambda x: -recommendations[x]):
            print(f"- {course}: {recommendations[course]} classmates also take this")
        break
```

**Key Learning:** Complex analysis using union (`|`) for aggregation, intersection (`&`) for finding overlap, and set operations in loops for recommendations.

---

## Common Patterns

1. **Merge multiple sets:** `result = set1 | set2 | set3`
2. **Find common:** `common = set1 & set2 & set3`
3. **Exclusive to one:** `exclusive = set1 - set2 - set3`
4. **Union of list of sets:** `set.union(*list_of_sets)`
5. **Intersection of list of sets:** `set.intersection(*list_of_sets)`
