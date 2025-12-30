## Question Bank: Creating and Using Sets

---

### Q1: Basic Set Operations (3 minutes, Low Difficulty)

Write a program that:
1. Creates a set `numbers` with values: `{1, 2, 3, 4, 5}`
2. Adds the number `6` to the set
3. Tries to add the number `3` again (observe what happens)
4. Removes the number `2` using `remove()`
5. Removes the number `10` using `discard()` (note the difference)
6. Prints the final set and its length

**Expected Output:**
```
After adding 6: {1, 2, 3, 4, 5, 6}
After trying to add 3 again: {1, 2, 3, 4, 5, 6}
After removing 2: {1, 3, 4, 5, 6}
After discarding 10: {1, 3, 4, 5, 6}
Final set: {1, 3, 4, 5, 6}
Length: 5
```

**Key Concepts:**
- Creating sets
- Adding elements
- Duplicate handling
- Removing elements (remove vs discard)

---

### Q2: Removing Duplicates (3 minutes, Low Difficulty)

Write a program that:
1. Creates a list with duplicate values:
   ```python
   scores = [85, 92, 78, 92, 85, 88, 95, 78, 92]
   ```
2. Converts the list to a set to remove duplicates
3. Converts back to a sorted list
4. Prints:
   - Original list length
   - Number of unique scores
   - Sorted unique scores

**Expected Output:**
```
Original list length: 9
Number of unique scores: 5
Unique scores (sorted): [78, 85, 88, 92, 95]
```

**Key Concepts:**
- Converting between lists and sets
- Automatic duplicate removal
- Sorting sets

---

### Q3: Social Network Analysis (5 minutes, Medium Difficulty)

Write a program that analyzes social connections:

1. Create three sets representing friend lists:
   ```python
   alice_friends = {'Bob', 'Charlie', 'Diana', 'Eve'}
   bob_friends = {'Alice', 'Charlie', 'Frank', 'Diana'}
   charlie_friends = {'Alice', 'Bob', 'Eve', 'George'}
   ```

2. Find and print:
   - Mutual friends between Alice and Bob
   - Friends only Alice has (not Bob)
   - Friends only Bob has (not Alice)
   - All unique people in the network (union of all three)
   - Friends that all three have in common

3. Write a function `suggest_friends(person_friends, other_friends)` that:
   - Takes two friend sets
   - Returns friends of friends (people in other_friends but not in person_friends)
   - These are friend suggestions!

4. Get friend suggestions for Alice based on Bob's friends

**Expected Output:**
```
Mutual friends (Alice & Bob): {'Charlie', 'Diana'}
Only Alice has: {'Eve'}
Only Bob has: {'Frank'}
All people in network: {'Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'George'}
Friends all three have: {'Alice', 'Bob'} or set() (depends on interpretation)

Friend suggestions for Alice (from Bob's friends): {'Frank'}
```

**Key Concepts:**
- Set intersection (mutual friends)
- Set difference (unique friends)
- Set union (all people)
- Practical set applications
- Friend recommendation algorithm

---

### Q4: Tag-Based Content Filter (5 minutes, Medium Difficulty)

Write a program that filters content based on tags:

1. Create a list of articles with tags:
   ```python
   articles = [
       {'title': 'Python Basics', 'tags': {'python', 'programming', 'tutorial', 'beginner'}},
       {'title': 'Web Development', 'tags': {'python', 'web', 'django', 'tutorial'}},
       {'title': 'JavaScript Guide', 'tags': {'javascript', 'programming', 'web', 'beginner'}},
       {'title': 'Data Science', 'tags': {'python', 'data', 'pandas', 'advanced'}},
       {'title': 'React Tutorial', 'tags': {'javascript', 'react', 'web', 'tutorial'}}
   ]
   ```

2. Write a function `find_articles_with_all_tags(articles, required_tags)` that:
   - Returns articles that have ALL the required tags
   - Use set operations to check

3. Write a function `find_articles_with_any_tag(articles, tags)` that:
   - Returns articles that have ANY of the given tags

4. Write a function `get_all_tags(articles)` that:
   - Returns a set of all unique tags across all articles

5. Find and print:
   - Articles with tags `{'python', 'tutorial'}`
   - Articles with any of `{'web', 'data'}`
   - All unique tags in the system
   - Most common tags (tags that appear in most articles)

**Expected Output:**
```
Articles with python AND tutorial:
  - Python Basics
  - Web Development

Articles with web OR data:
  - Web Development
  - JavaScript Guide
  - Data Science
  - React Tutorial

All unique tags: {'python', 'programming', 'tutorial', 'beginner', 'web', 'django', 'javascript', 'data', 'pandas', 'advanced', 'react'}

Most common tags: {'python', 'tutorial', 'web'}
```

**Key Concepts:**
- Set subset operations
- Set intersection with multiple sets
- Set union across collections
- Practical tag filtering
- Content recommendation systems

---

### Q5: Student Course Enrollment System (5 minutes, Medium Difficulty)

Write a program that manages student course enrollments:

1. Create enrollment data:
   ```python
   enrollments = {
       'Alice': {'Math', 'Physics', 'Chemistry', 'English'},
       'Bob': {'Math', 'Chemistry', 'Biology', 'History'},
       'Charlie': {'Math', 'English', 'Art', 'Music'},
       'Diana': {'Physics', 'Chemistry', 'Biology', 'Math'}
   }
   ```

2. Write a function `find_common_courses(*students)` that:
   - Takes variable number of student names
   - Returns courses ALL specified students are taking
   - Use set intersection

3. Write a function `find_any_courses(*students)` that:
   - Returns all courses ANY of the students are taking
   - Use set union

4. Write a function `can_form_study_group(students, min_common)` that:
   - Checks if students have at least `min_common` courses together
   - Returns True/False

5. Write a function `course_statistics(enrollments)` that returns:
   - Total number of unique courses
   - Most popular course (appears in most student schedules)
   - Students taking the most courses

6. Perform analysis:
   - Find courses Alice and Bob share
   - Find courses only Diana is taking (that no one else is)
   - Can Alice, Bob, and Charlie form a study group? (need 2+ common courses)
   - Get course statistics

**Expected Output:**
```
Common courses (Alice & Bob): {'Math', 'Chemistry'}

Courses only Diana takes: set() or {'Biology'} (depending on interpretation)

All courses any of them take: {'Math', 'Physics', 'Chemistry', 'English', 'Biology', 'History', 'Art', 'Music'}

Can Alice, Bob, Charlie form study group (min 2 common)? True
Common: {'Math'}

Course Statistics:
  Total unique courses: 10
  Most popular course: Math (4 students)
  Students with most courses: Alice, Bob, Charlie, Diana (tied at 4 courses each)
```

**Key Concepts:**
- Multiple set operations
- Variable arguments with sets
- Set intersection across multiple sets
- Data analysis with sets
- Practical enrollment management

**Bonus Challenge:**
Write a function that suggests courses for a student based on:
- What courses their friends are taking
- That they're not already enrolled in
- That appear in at least 2 of their friends' schedules

---

### Additional Practice Problems

**Practice 1: Unique Character Counter**
Write a program that finds all unique characters in a string and counts how many unique characters two strings share.

**Practice 2: Permission System**
Create a role-based permission system using sets. Check if a user has required permissions, find missing permissions, etc.

**Practice 3: Inventory Management**
Use sets to track inventory across multiple warehouses. Find items available in all warehouses, items only in specific warehouses, etc.

**Practice 4: Email List Manager**
Manage email lists using sets. Find subscribers to multiple lists, unique subscribers, unsubscribe from all lists, etc.

**Practice 5: Spell Checker**
Create a simple spell checker using a set of valid words. Find misspelled words, suggest corrections based on similar valid words.
