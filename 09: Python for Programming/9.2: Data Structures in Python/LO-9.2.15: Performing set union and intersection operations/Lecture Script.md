## Lecture Script: Performing Set Union and Intersection Operations

**Duration:** 18 minutes

---

### Hook (2 minutes)

**Scenario:**

You're building a music streaming app. You need to find:

```python
# User preferences
alice_likes = {'rock', 'jazz', 'blues'}
bob_likes = {'jazz', 'pop', 'blues'}

# Find songs BOTH like (common interests)
common = alice_likes & bob_likes
print(f"Both like: {common}")  # {'jazz', 'blues'}

# Find ALL songs either likes (combined interests)
all_genres = alice_likes | bob_likes
print(f"All genres: {all_genres}")
# {'rock', 'jazz', 'blues', 'pop'}
```

**The Power:**
- **Intersection (&)**: Find what's common between sets
- **Union (|)**: Combine sets into one

**Today's Focus:**

Master two fundamental set operations:
- **union()** and **|** operator: Combine sets
- **intersection()** and **&** operator: Find common elements

---

### Section 1: Union Operation (5 minutes)

**What is Union?**

Union combines all unique elements from two or more sets.

**Syntax:**
```python
# Method
set1.union(set2)
set1.union(set2, set3, ...)

# Operator
set1 | set2
set1 | set2 | set3
```

**Basic Examples:**

**1. Simple Union:**
```python
A = {1, 2, 3}
B = {3, 4, 5}

# Using method
result = A.union(B)
print(result)  # {1, 2, 3, 4, 5}

# Using operator
result = A | B
print(result)  # {1, 2, 3, 4, 5}

# Note: Original sets unchanged
print(A)  # {1, 2, 3}
print(B)  # {3, 4, 5}
```

**Key Points:**
- Returns NEW set (doesn't modify originals)
- Includes ALL unique elements from both sets
- Duplicates automatically removed
- Order is arbitrary (sets are unordered)

**2. Multiple Sets Union:**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

# Method - can take multiple arguments
result = set1.union(set2, set3)
print(result)  # {1, 2, 3, 4, 5, 6, 7}

# Operator - can chain
result = set1 | set2 | set3
print(result)  # {1, 2, 3, 4, 5, 6, 7}
```

**3. Empty Set Union:**
```python
A = {1, 2, 3}
B = set()  # Empty set

result = A | B
print(result)  # {1, 2, 3}

# Union with empty set returns copy of non-empty set
```

**Real-World Examples:**

**Example 1: Combining User Interests**
```python
# User profile tags
profile_tags = {'python', 'web', 'backend'}

# New interests to add
new_interests = {'api', 'database', 'python'}

# Combine all interests
all_interests = profile_tags | new_interests
print(all_interests)
# {'python', 'web', 'backend', 'api', 'database'}
```

**Example 2: Merging Subscriber Lists**
```python
# Email lists from different campaigns
campaign_a = {'alice@ex.com', 'bob@ex.com', 'charlie@ex.com'}
campaign_b = {'bob@ex.com', 'diana@ex.com', 'eve@ex.com'}

# Combine all unique subscribers
all_subscribers = campaign_a | campaign_b
print(f"Total unique subscribers: {len(all_subscribers)}")  # 5

# Note: bob@ex.com appears once (deduplicated)
```

**Example 3: Aggregating Search Results**
```python
# Search results from different sources
google_results = {'result1', 'result2', 'result3'}
bing_results = {'result2', 'result4', 'result5'}
ddg_results = {'result1', 'result5', 'result6'}

# Combine all unique results
all_results = google_results | bing_results | ddg_results
print(f"Total unique results: {len(all_results)}")  # 6
print(sorted(all_results))
# ['result1', 'result2', 'result3', 'result4', 'result5', 'result6']
```

**Example 4: Tag Aggregation**
```python
# Collect all tags from multiple articles
articles = [
    {'tags': {'python', 'tutorial', 'beginner'}},
    {'tags': {'python', 'advanced', 'tips'}},
    {'tags': {'javascript', 'tutorial', 'web'}}
]

# Start with empty set
all_tags = set()

# Union with each article's tags
for article in articles:
    all_tags = all_tags | article['tags']

print(sorted(all_tags))
# ['advanced', 'beginner', 'javascript', 'python', 'tips', 'tutorial', 'web']

# Alternative: use union() with multiple args
all_tags = set().union(*(article['tags'] for article in articles))
```

**Method vs Operator:**

```python
A = {1, 2, 3}
B = {3, 4, 5}

# Both produce same result
result1 = A.union(B)
result2 = A | B
print(result1 == result2)  # True

# Method advantage: accepts any iterable
A.union([4, 5, 6])  # Works!
# A | [4, 5, 6]  # Error! Operator needs sets

# Operator advantage: more concise
result = A | B | C | D  # Clean
# result = A.union(B).union(C).union(D)  # Verbose
```

---

### Section 2: Intersection Operation (5 minutes)

**What is Intersection?**

Intersection finds elements that exist in ALL sets.

**Syntax:**
```python
# Method
set1.intersection(set2)
set1.intersection(set2, set3, ...)

# Operator
set1 & set2
set1 & set2 & set3
```

**Basic Examples:**

**1. Simple Intersection:**
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Using method
result = A.intersection(B)
print(result)  # {3, 4}

# Using operator
result = A & B
print(result)  # {3, 4}

# Original sets unchanged
print(A)  # {1, 2, 3, 4}
print(B)  # {3, 4, 5, 6}
```

**Key Points:**
- Returns NEW set (doesn't modify originals)
- Includes ONLY elements present in ALL sets
- If no common elements, returns empty set
- Order is arbitrary

**2. Multiple Sets Intersection:**
```python
set1 = {1, 2, 3, 4}
set2 = {2, 3, 4, 5}
set3 = {3, 4, 5, 6}

# Find elements common to ALL three sets
result = set1 & set2 & set3
print(result)  # {3, 4}

# Using method
result = set1.intersection(set2, set3)
print(result)  # {3, 4}
```

**3. No Common Elements:**
```python
A = {1, 2, 3}
B = {4, 5, 6}

result = A & B
print(result)  # set() - empty set
print(len(result))  # 0
```

**Real-World Examples:**

**Example 1: Finding Common Interests**
```python
# Friend recommendations based on common interests
user_interests = {'python', 'web', 'ai', 'data'}
friend_interests = {'web', 'mobile', 'ai', 'design'}

common = user_interests & friend_interests
print(f"You both like: {common}")
# {'web', 'ai'}

# Calculate compatibility score
compatibility = len(common) / len(user_interests | friend_interests)
print(f"Compatibility: {compatibility:.0%}")  # 33%
```

**Example 2: Permission Validation**
```python
# User permissions
user_permissions = {'read', 'write', 'execute'}

# Required permissions for action
required = {'read', 'write'}

# Check if user has all required permissions
has_all = required & user_permissions == required

if has_all:
    print("Access granted")
else:
    missing = required - user_permissions
    print(f"Missing permissions: {missing}")

# Alternative check
if required.issubset(user_permissions):
    print("Access granted")
```

**Example 3: Finding Active Users in Both Systems**
```python
# Active users in different systems
web_users = {'alice', 'bob', 'charlie', 'diana'}
mobile_users = {'bob', 'diana', 'eve', 'frank'}

# Users active on both platforms
active_both = web_users & mobile_users
print(f"Active on both: {active_both}")
# {'bob', 'diana'}

# Users only on web
web_only = web_users - mobile_users
print(f"Web only: {web_only}")
# {'alice', 'charlie'}

# Users only on mobile
mobile_only = mobile_users - web_users
print(f"Mobile only: {mobile_only}")
# {'eve', 'frank'}
```

**Example 4: Product Feature Comparison**
```python
# Features of different products
product_a = {'wifi', 'bluetooth', 'nfc', 'camera'}
product_b = {'wifi', 'bluetooth', 'camera', 'gps'}
product_c = {'bluetooth', 'camera', 'gps', 'radio'}

# Common features across ALL products
common_features = product_a & product_b & product_c
print(f"All products have: {common_features}")
# {'bluetooth', 'camera'}

# Features in at least 2 products
at_least_two = (product_a & product_b) | (product_b & product_c) | (product_a & product_c)
print(f"In at least 2: {at_least_two}")
# {'wifi', 'bluetooth', 'camera', 'gps'}
```

**Example 5: Attendance Tracking**
```python
# Track attendance across multiple events
event1_attendees = {'alice', 'bob', 'charlie', 'diana'}
event2_attendees = {'bob', 'diana', 'eve'}
event3_attendees = {'bob', 'diana'}

# Who attended ALL events?
perfect_attendance = event1_attendees & event2_attendees & event3_attendees
print(f"Perfect attendance: {perfect_attendance}")
# {'bob', 'diana'}

# Who attended at least one event?
any_attendance = event1_attendees | event2_attendees | event3_attendees
print(f"Total unique attendees: {len(any_attendance)}")  # 5
```

---

### Section 3: Combining Union and Intersection (3 minutes)

**Venn Diagram Operations:**

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union: Everything in either set
union = A | B
print(f"Union: {union}")
# {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection: Only what's in both
intersection = A & B
print(f"Intersection: {intersection}")
# {4, 5}

# Difference: In A but not in B
diff_a = A - B
print(f"A - B: {diff_a}")
# {1, 2, 3}

# Symmetric Difference: In either but not both
sym_diff = A ^ B
print(f"A ^ B: {sym_diff}")
# {1, 2, 3, 6, 7, 8}
```

**Complex Example: Content Recommendation**
```python
# User viewing history
user_watched = {'movie1', 'movie2', 'movie3', 'movie4'}

# Friend recommendations
friend_watched = {'movie3', 'movie4', 'movie5', 'movie6'}

# Movies to recommend (friend watched but user hasn't)
recommend = friend_watched - user_watched
print(f"Recommend: {recommend}")
# {'movie5', 'movie6'}

# Movies both watched (common ground)
both_watched = user_watched & friend_watched
print(f"Both watched: {both_watched}")
# {'movie3', 'movie4'}

# All unique movies between both
all_movies = user_watched | friend_watched
print(f"Total unique movies: {len(all_movies)}")  # 6
```

**Set Operations Priority:**
```python
A = {1, 2, 3}
B = {2, 3, 4}
C = {3, 4, 5}

# Operations are left-to-right
result = A | B & C  # Same as A | (B & C)
print(result)  # {1, 2, 3, 4}

# Use parentheses for clarity
result = (A | B) & C
print(result)  # {3, 4}
```

---

### Section 4: Practical Applications (2 minutes)

**Application 1: Social Network Analysis**
```python
class SocialNetwork:
    def __init__(self):
        self.user_friends = {}

    def add_friendship(self, user, friend):
        if user not in self.user_friends:
            self.user_friends[user] = set()
        if friend not in self.user_friends:
            self.user_friends[friend] = set()

        self.user_friends[user].add(friend)
        self.user_friends[friend].add(user)

    def mutual_friends(self, user1, user2):
        """Find mutual friends"""
        return self.user_friends.get(user1, set()) & self.user_friends.get(user2, set())

    def friend_suggestions(self, user):
        """Suggest friends of friends"""
        friends = self.user_friends.get(user, set())
        suggestions = set()

        for friend in friends:
            # Friends of friends
            suggestions = suggestions | self.user_friends.get(friend, set())

        # Remove user and existing friends
        suggestions = suggestions - friends - {user}
        return suggestions

# Usage
network = SocialNetwork()
network.add_friendship('alice', 'bob')
network.add_friendship('alice', 'charlie')
network.add_friendship('bob', 'diana')

print(network.mutual_friends('alice', 'bob'))  # set()
print(network.friend_suggestions('alice'))  # {'diana'}
```

**Application 2: E-commerce Filtering**
```python
# Product filtering system
products_with_wifi = {1, 2, 3, 5, 8}
products_with_bluetooth = {2, 3, 4, 6, 8}
products_under_100 = {1, 2, 4, 7, 9}

# Find products with BOTH wifi and bluetooth
both_features = products_with_wifi & products_with_bluetooth
print(f"WiFi + Bluetooth: {both_features}")  # {2, 3, 8}

# Find affordable products with ANY wireless feature
wireless = products_with_wifi | products_with_bluetooth
affordable_wireless = wireless & products_under_100
print(f"Affordable wireless: {affordable_wireless}")  # {2, 4}
```

---

### Common Patterns (1 minute)

**Pattern 1: Deduplication Across Sources**
```python
# Merge unique items from multiple sources
all_items = source1 | source2 | source3
```

**Pattern 2: Finding Overlap**
```python
# Find common elements
common = set1 & set2 & set3
```

**Pattern 3: Compatibility Check**
```python
# Check if sets have common elements
has_overlap = bool(set1 & set2)
# or
has_overlap = len(set1 & set2) > 0
```

**Pattern 4: Progressive Filtering**
```python
# Start with all, filter progressively
candidates = all_users
candidates = candidates & active_users
candidates = candidates & premium_users
```

---

### Summary (1 minute)

**Two Core Operations:**

**Union (|)**
- Combines all unique elements
- `A | B` includes everything from both
- Use: Merging, aggregating, combining

**Intersection (&)**
- Finds common elements
- `A & B` includes only shared items
- Use: Finding overlap, validation, filtering

**Quick Reference:**
```python
A = {1, 2, 3}
B = {2, 3, 4}

A | B   # {1, 2, 3, 4} - union
A & B   # {2, 3} - intersection
A - B   # {1} - difference
A ^ B   # {1, 4} - symmetric difference
```

**Key Points:**
- Both return NEW sets (originals unchanged)
- Can chain operations: `A | B | C`
- Use & for filtering, | for combining
- Empty intersection = no common elements

**Remember:** Sets automatically handle uniqueness - perfect for combining and comparing data!
