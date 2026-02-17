## Pre-Read: Performing Set Union and Intersection Operations

**Duration:** 5 minutes

---

## What Are Union and Intersection?

These are Python's **"combine" and "compare"** operations - like merging guest lists or finding mutual friends! This is where **math class Venn diagrams become real code**.

### Simple Analogy

Think of sets like **two circles overlapping** (Venn diagram from math class):

**Union (|) is "everything in either circle"**:
- **Circle A**: {1, 2, 3}
- **Circle B**: {3, 4, 5}
- **Union**: {1, 2, 3, 4, 5} - grab everything!
- **Like**: Combining two playlists into one mega-playlist

**Intersection (&) is "only the overlap"**:
- **Circle A**: {1, 2, 3}
- **Circle B**: {3, 4, 5}
- **Intersection**: {3} - just the common part!
- **Like**: Finding songs that appear in BOTH playlists

### Why This is Mind-Blowing

**Remember Venn diagrams from school?** Those circles you drew with overlapping areas?

**Python made them executable!** 🤯

```python
# Math class: Draw two circles, shade overlap
# Python: Just type &
common = friends_A & friends_B  # Instant overlap!
```

**140 years of mathematics → One symbol in Python!**

### The "OR" vs "AND" Logic

**Union (|) = "OR" logic**:
- "Give me items from A **OR** B **OR** both"
- **Everything included**: If it's in either set, it's in!
- **Like**: "Show me users on web OR mobile"
- **Result**: Everyone! (Some on both, some on one)

**Intersection (&) = "AND" logic**:
- "Give me items in A **AND** B"
- **Only overlap**: Must be in BOTH sets!
- **Like**: "Show me users on web AND mobile"
- **Result**: Only multi-platform users!

### Real-World Magic

**Scenario**: Friend suggestions on social media

```python
your_friends = {'Alice', 'Bob', 'Charlie'}
suggested_person_friends = {'Bob', 'Charlie', 'Diana', 'Eve'}

# People you ALREADY know (intersection)
already_friends = your_friends & suggested_person_friends
# Result: {'Bob', 'Charlie'} - mutual friends!

# People you DON'T know yet (difference)
new_people = suggested_person_friends - your_friends
# Result: {'Diana', 'Eve'} - suggestions!

# Everyone involved (union)
all_people = your_friends | suggested_person_friends
# Result: {'Alice', 'Bob', 'Charlie', 'Diana', 'Eve'}
```

**One line each** - what would take 20 lines with loops!

---

## Introduction

Sets become truly powerful when you combine or compare them. Python provides mathematical set operations that make data analysis elegant and efficient:

- **Union (|)**: Combine sets - get everything from both
- **Intersection (&)**: Find overlap - get only what's common

These operations are fundamental to data analysis, filtering, and comparison tasks.

---

## Why It Matters

Set operations solve real-world problems:

- **Social networks**: Find mutual friends, suggest connections
- **E-commerce**: Filter products by multiple criteria
- **Analytics**: Combine data from different sources
- **User management**: Track multi-platform activity
- **Recommendations**: Find similar users or items

Understanding union and intersection makes complex data operations simple.

---

## Union Operation (|)

**Union combines all unique elements from sets:**

```python
A = {1, 2, 3}
B = {3, 4, 5}

# Everything from both sets
result = A | B
print(result)  # {1, 2, 3, 4, 5}

# Or use method
result = A.union(B)
print(result)  # {1, 2, 3, 4, 5}
```

**Key points:**
- `|` operator or `.union()` method
- Returns NEW set (originals unchanged)
- Duplicates automatically removed
- Perfect for merging data

**Real example:**
```python
# Merge subscriber lists
campaign_a = {'alice@ex.com', 'bob@ex.com'}
campaign_b = {'bob@ex.com', 'charlie@ex.com'}

all_subscribers = campaign_a | campaign_b
print(all_subscribers)
# {'alice@ex.com', 'bob@ex.com', 'charlie@ex.com'}
# bob@ex.com appears only once!
```

---

## Intersection Operation (&)

**Intersection finds elements common to ALL sets:**

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Only what's in both
result = A & B
print(result)  # {3, 4}

# Or use method
result = A.intersection(B)
print(result)  # {3, 4}
```

**Key points:**
- `&` operator or `.intersection()` method
- Returns NEW set (originals unchanged)
- Empty set if no common elements
- Perfect for finding overlap

**Real example:**
```python
# Find common interests
alice_likes = {'python', 'web', 'ai', 'data'}
bob_likes = {'web', 'mobile', 'ai', 'design'}

common_interests = alice_likes & bob_likes
print(common_interests)
# {'web', 'ai'}
```

---

## Quick Comparison

| Operation     | Symbol | What it does              | Example Result    |
| ------------- | ------ | ------------------------- | ----------------- |
| **Union**     | `\|`   | Everything from both sets | {1,2,3,4,5}       |
| **Intersection** | `&` | Only what's in both       | {3,4}             |

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A | B   # {1, 2, 3, 4, 5, 6} - union
A & B   # {3, 4} - intersection
```

---

## Practical Example: Multi-Platform Users

```python
# Users on different platforms
web_users = {'alice', 'bob', 'charlie', 'diana'}
mobile_users = {'bob', 'diana', 'eve', 'frank'}

# Users on BOTH platforms (intersection)
both_platforms = web_users & mobile_users
print(f"On both: {both_platforms}")
# {'bob', 'diana'}

# ALL unique users (union)
all_users = web_users | mobile_users
print(f"Total users: {len(all_users)}")
# 6 unique users

# Users ONLY on web (difference)
web_only = web_users - mobile_users
print(f"Web only: {web_only}")
# {'alice', 'charlie'}
```

---

## Multiple Sets

Both operations work with multiple sets:

```python
A = {1, 2, 3}
B = {2, 3, 4}
C = {3, 4, 5}

# Union of all three
all_numbers = A | B | C
print(all_numbers)  # {1, 2, 3, 4, 5}

# Common to all three
common = A & B & C
print(common)  # {3}
```

---

## Method vs Operator

```python
A = {1, 2, 3}
B = {3, 4, 5}

# Both work the same
result1 = A | B           # Operator
result2 = A.union(B)      # Method
print(result1 == result2)  # True

# Operator is more concise
combined = A | B | C | D

# Method can accept any iterable
A.union([4, 5, 6])  # Works!
# A | [4, 5, 6]     # Error! Needs set
```

**When to use which:**
- Operator (`|`, `&`): When working with sets, more concise
- Method: When working with lists/tuples, more flexible

---

## Before the Lecture

Try this exercise:

```python
# Friend recommendations
your_friends = {'alice', 'bob', 'charlie'}
suggested_friend_friends = {'bob', 'charlie', 'diana', 'eve'}

# Who should you add? (in suggestions but not your friends)
to_add = suggested_friend_friends - your_friends
print(to_add)  # ?

# Who do you already know? (in both)
already_friends = your_friends & suggested_friend_friends
print(already_friends)  # ?

# All people involved
all_people = your_friends | suggested_friend_friends
print(all_people)  # ?
```

**Think about:**
1. What will each operation return?
2. Why is intersection useful for finding overlap?
3. Why is union useful for combining data?

---

## Key Vocabulary

- **Union**: Combining sets to get all unique elements from both
- **Intersection**: Finding elements common to all sets
- **Operator**: Symbol like `|` or `&` for set operations
- **Method**: Function like `.union()` or `.intersection()`
- **Venn Diagram**: Visual representation of set relationships
- **Overlap**: Elements that appear in multiple sets

---

## What's Next

In the lecture, you'll learn:
- Detailed union and intersection syntax
- Chaining multiple operations
- Real-world applications (social networks, filtering, analytics)
- Performance considerations
- Combining operations for complex queries
- When to use each operation

Get ready to master powerful set operations!
