## Editorials: Creating and Using Sets

---

### Q1 Solution: Basic Set Operations

```python
# 1. Create set
numbers = {1, 2, 3, 4, 5}
print(f"Initial set: {numbers}")

# 2. Add 6
numbers.add(6)
print(f"After adding 6: {numbers}")

# 3. Try to add 3 again
numbers.add(3)
print(f"After trying to add 3 again: {numbers}")
# No change - sets only store unique elements

# 4. Remove 2
numbers.remove(2)
print(f"After removing 2: {numbers}")

# 5. Discard 10
numbers.discard(10)
print(f"After discarding 10: {numbers}")
# No error even though 10 doesn't exist

# 6. Print final result
print(f"Final set: {numbers}")
print(f"Length: {len(numbers)}")
```

**Explanation:**

**add() Method:**
- Adds element to set
- If element already exists, nothing happens
- Sets automatically maintain uniqueness

**remove() vs discard():**
```python
# remove() - raises KeyError if element not found
numbers.remove(2)  # ✓ Works
# numbers.remove(100)  # ✗ KeyError

# discard() - safe, no error if element not found
numbers.discard(10)  # ✓ Works, does nothing
numbers.discard(100)  # ✓ Also works, does nothing
```

**Key Takeaway:** Use `discard()` when you're not sure if element exists, use `remove()` when you expect it to exist.

---

### Q2 Solution: Removing Duplicates

```python
# 1. Create list with duplicates
scores = [85, 92, 78, 92, 85, 88, 95, 78, 92]

# 2. Convert to set (removes duplicates)
unique_scores = set(scores)

# 3. Convert back to sorted list
sorted_scores = sorted(unique_scores)

# 4. Print results
print(f"Original list length: {len(scores)}")
print(f"Number of unique scores: {len(unique_scores)}")
print(f"Unique scores (sorted): {sorted_scores}")
```

**Explanation:**

**Duplicate Removal Process:**
```python
scores = [85, 92, 78, 92, 85, 88, 95, 78, 92]
          ↓ Convert to set
unique_scores = {85, 92, 78, 88, 95}  # Duplicates removed
          ↓ Sort
sorted_scores = [78, 85, 88, 92, 95]  # Sorted list
```

**Why This Works:**
- Sets automatically remove duplicates
- Only unique elements are stored
- Fast and efficient

**Note:** Sets are unordered, so we use `sorted()` to get a sorted list.

**Alternative with Order Preservation:**
```python
def remove_duplicates_preserve_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

scores = [85, 92, 78, 92, 85, 88, 95, 78, 92]
unique = remove_duplicates_preserve_order(scores)
# [85, 92, 78, 88, 95] - order preserved
```

---

### Q3 Solution: Social Network Analysis

```python
# 1. Create friend sets
alice_friends = {'Bob', 'Charlie', 'Diana', 'Eve'}
bob_friends = {'Alice', 'Charlie', 'Frank', 'Diana'}
charlie_friends = {'Alice', 'Bob', 'Eve', 'George'}

# 2. Analysis
# Mutual friends (intersection)
mutual_alice_bob = alice_friends & bob_friends
print(f"Mutual friends (Alice & Bob): {mutual_alice_bob}")

# Only Alice has
only_alice = alice_friends - bob_friends
print(f"Only Alice has: {only_alice}")

# Only Bob has
only_bob = bob_friends - alice_friends
print(f"Only Bob has: {only_bob}")

# All unique people (union)
all_people = alice_friends | bob_friends | charlie_friends
print(f"All people in network: {all_people}")

# Friends all three have in common
# Note: Need to remove themselves from their own friend lists for accurate result
common_all = alice_friends & bob_friends & charlie_friends
print(f"Friends all three have: {common_all}")

# 3. Friend suggestion function
def suggest_friends(person_friends, other_friends):
    """Return friends of friends (not already friends)"""
    return other_friends - person_friends

# 4. Get suggestions for Alice
suggestions = suggest_friends(alice_friends, bob_friends)
print(f"\nFriend suggestions for Alice (from Bob's friends): {suggestions}")
```

**Explanation:**

**Set Operations Used:**

**1. Intersection (&)** - Mutual friends
```python
alice_friends & bob_friends
# Returns: {'Charlie', 'Diana'}
# People both Alice and Bob are friends with
```

**2. Difference (-)** - Unique friends
```python
alice_friends - bob_friends
# Returns: {'Eve'}
# Friends Alice has that Bob doesn't
```

**3. Union (|)** - All people
```python
alice_friends | bob_friends | charlie_friends
# Returns all unique people across all sets
```

**Friend Suggestion Algorithm:**
```python
def suggest_friends(person_friends, other_friends):
    return other_friends - person_friends
```

This returns people in `other_friends` who are NOT in `person_friends`. These are potential new friends!

**Real-World Application:**
- Social networks (Facebook, LinkedIn friend suggestions)
- "People you may know" features
- Network analysis

---

### Q4 Solution: Tag-Based Content Filter

```python
# 1. Articles with tags
articles = [
    {'title': 'Python Basics', 'tags': {'python', 'programming', 'tutorial', 'beginner'}},
    {'title': 'Web Development', 'tags': {'python', 'web', 'django', 'tutorial'}},
    {'title': 'JavaScript Guide', 'tags': {'javascript', 'programming', 'web', 'beginner'}},
    {'title': 'Data Science', 'tags': {'python', 'data', 'pandas', 'advanced'}},
    {'title': 'React Tutorial', 'tags': {'javascript', 'react', 'web', 'tutorial'}}
]

# 2. Find articles with ALL required tags
def find_articles_with_all_tags(articles, required_tags):
    """Return articles that have ALL required tags"""
    result = []
    required_set = set(required_tags)
    
    for article in articles:
        # Check if required tags is subset of article tags
        if required_set.issubset(article['tags']):
            result.append(article['title'])
    
    return result

# 3. Find articles with ANY tag
def find_articles_with_any_tag(articles, tags):
    """Return articles that have ANY of the given tags"""
    result = []
    tag_set = set(tags)
    
    for article in articles:
        # Check if there's any intersection
        if article['tags'] & tag_set:
            result.append(article['title'])
    
    return result

# 4. Get all unique tags
def get_all_tags(articles):
    """Return set of all unique tags"""
    all_tags = set()
    for article in articles:
        all_tags = all_tags | article['tags']  # Union
    return all_tags

# 5. Analysis
print("Articles with python AND tutorial:")
result = find_articles_with_all_tags(articles, {'python', 'tutorial'})
for title in result:
    print(f"  - {title}")

print("\nArticles with web OR data:")
result = find_articles_with_any_tag(articles, {'web', 'data'})
for title in result:
    print(f"  - {title}")

print(f"\nAll unique tags: {get_all_tags(articles)}")

# Find most common tags
def find_common_tags(articles, min_count):
    """Find tags that appear in at least min_count articles"""
    tag_counts = {}
    
    # Count tag occurrences
    for article in articles:
        for tag in article['tags']:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
    
    # Filter by min_count
    common = {tag for tag, count in tag_counts.items() if count >= min_count}
    return common

common_tags = find_common_tags(articles, 3)
print(f"\nMost common tags (3+ articles): {common_tags}")
```

**Explanation:**

**Subset Check (ALL tags):**
```python
required_set.issubset(article['tags'])
# True if ALL required tags are in article tags
```

Example:
```python
required = {'python', 'tutorial'}
article_tags = {'python', 'programming', 'tutorial', 'beginner'}

required.issubset(article_tags)  # True
# All required tags are present
```

**Intersection Check (ANY tag):**
```python
article['tags'] & tag_set
# Returns common tags
# If result is not empty, there's at least one match
```

Example:
```python
search_tags = {'web', 'data'}
article_tags = {'python', 'web', 'django'}

article_tags & search_tags  # {'web'}
# At least one tag matches
```

**Union for All Tags:**
```python
all_tags = set()
for article in articles:
    all_tags = all_tags | article['tags']
```

Combines all tags across all articles.

**Key Patterns:**
- `issubset()` for "AND" logic (all must match)
- Intersection `&` for "OR" logic (any can match)
- Union `|` to combine sets
- Real-world application: Content filtering, search, recommendations

---

### Q5 Solution: Student Course Enrollment System

```python
# 1. Enrollment data
enrollments = {
    'Alice': {'Math', 'Physics', 'Chemistry', 'English'},
    'Bob': {'Math', 'Chemistry', 'Biology', 'History'},
    'Charlie': {'Math', 'English', 'Art', 'Music'},
    'Diana': {'Physics', 'Chemistry', 'Biology', 'Math'}
}

# 2. Find common courses
def find_common_courses(*students):
    """Find courses ALL students are taking"""
    if not students:
        return set()
    
    # Start with first student's courses
    common = enrollments[students[0]].copy()
    
    # Intersect with each subsequent student
    for student in students[1:]:
        common = common & enrollments[student]
    
    return common

# 3. Find any courses
def find_any_courses(*students):
    """Find all courses ANY student is taking"""
    all_courses = set()
    
    for student in students:
        all_courses = all_courses | enrollments[student]
    
    return all_courses

# 4. Study group check
def can_form_study_group(students, min_common):
    """Check if students have enough common courses"""
    common = find_common_courses(*students)
    return len(common) >= min_common

# 5. Course statistics
def course_statistics(enrollments):
    """Calculate enrollment statistics"""
    # Count course enrollments
    course_counts = {}
    for student, courses in enrollments.items():
        for course in courses:
            course_counts[course] = course_counts.get(course, 0) + 1
    
    # Total unique courses
    total_courses = len(course_counts)
    
    # Most popular course
    most_popular = max(course_counts.items(), key=lambda x: x[1])
    
    # Students taking most courses
    max_courses = max(len(courses) for courses in enrollments.values())
    top_students = [
        student for student, courses in enrollments.items()
        if len(courses) == max_courses
    ]
    
    return {
        'total_courses': total_courses,
        'most_popular': most_popular,
        'top_students': top_students,
        'max_courses': max_courses
    }

# 6. Analysis
print("Common courses (Alice & Bob):", find_common_courses('Alice', 'Bob'))

# Courses only Diana takes
diana_courses = enrollments['Diana']
other_courses = set()
for student, courses in enrollments.items():
    if student != 'Diana':
        other_courses = other_courses | courses

only_diana = diana_courses - other_courses
print(f"\nCourses only Diana takes: {only_diana}")

# All courses
all_courses = find_any_courses('Alice', 'Bob', 'Charlie', 'Diana')
print(f"\nAll courses: {all_courses}")

# Study group check
can_study = can_form_study_group(['Alice', 'Bob', 'Charlie'], 2)
common = find_common_courses('Alice', 'Bob', 'Charlie')
print(f"\nCan Alice, Bob, Charlie form study group (min 2 common)? {can_study}")
print(f"Common: {common}")

# Statistics
stats = course_statistics(enrollments)
print(f"\nCourse Statistics:")
print(f"  Total unique courses: {stats['total_courses']}")
print(f"  Most popular course: {stats['most_popular'][0]} ({stats['most_popular'][1]} students)")
print(f"  Students with most courses: {', '.join(stats['top_students'])} ({stats['max_courses']} courses each)")
```

**Explanation:**

**Multiple Set Intersection:**
```python
def find_common_courses(*students):
    common = enrollments[students[0]].copy()
    for student in students[1:]:
        common = common & enrollments[student]
    return common
```

This progressively narrows down to courses ALL students share:
```
Alice: {Math, Physics, Chemistry, English}
  & Bob: {Math, Chemistry, Biology, History}
  = {Math, Chemistry}
    & Charlie: {Math, English, Art, Music}
    = {Math}
```

**Multiple Set Union:**
```python
def find_any_courses(*students):
    all_courses = set()
    for student in students:
        all_courses = all_courses | enrollments[student]
    return all_courses
```

Combines all courses from all students.

**Finding Unique to One Person:**
```python
diana_courses - other_courses
```

Courses Diana has that nobody else has.

**Bonus Challenge Solution:**
```python
def suggest_courses(student, enrollments):
    """Suggest courses based on friends' enrollments"""
    student_courses = enrollments[student]
    
    # Collect courses from all other students
    friend_courses = {}
    for other, courses in enrollments.items():
        if other != student:
            for course in courses:
                if course not in student_courses:
                    friend_courses[course] = friend_courses.get(course, 0) + 1
    
    # Return courses taken by 2+ friends
    suggestions = {
        course for course, count in friend_courses.items()
        if count >= 2
    }
    
    return suggestions

suggestions = suggest_courses('Alice', enrollments)
print(f"\nCourse suggestions for Alice: {suggestions}")
# Courses taken by 2+ other students that Alice isn't taking
```

**Real-World Applications:**
- University enrollment systems
- Study group formation
- Course recommendation
- Resource allocation
- Scheduling optimization

---

### Key Takeaways

**Set Operation Summary:**

| Operation | Operator | Method | Description |
|-----------|----------|--------|-------------|
| Union | `\|` | `.union()` | All elements from both |
| Intersection | `&` | `.intersection()` | Common elements |
| Difference | `-` | `.difference()` | In first, not second |
| Symmetric Difference | `^` | `.symmetric_difference()` | In either, not both |

**Common Patterns:**

1. **Remove duplicates:**
```python
unique = list(set(items))
```

2. **Fast membership:**
```python
valid_items = set(valid_list)
if item in valid_items:  # O(1)
```

3. **Find common elements:**
```python
common = set1 & set2
```

4. **Find differences:**
```python
only_in_first = set1 - set2
```

5. **Combine collections:**
```python
all_items = set1 | set2 | set3
```

**Best Practices:**
- Use sets for uniqueness and fast lookups
- Convert to list when order matters
- Use appropriate operation (union, intersection, difference)
- Remember elements must be immutable
- Sets are unordered - don't rely on order
