## Question Bank: Modifying Lists Using Built-in Methods

### Q1: Basic List Method Operations (3 minutes, Low Difficulty)

**Problem:**
Start with an empty list and perform these operations in sequence:
1. Append the values 10, 20, 30
2. Insert 15 at index 1
3. Extend with [40, 50]
4. Remove the value 20
5. Print the final list

**Expected Output:**
```
After append 10, 20, 30: [10, 20, 30]
After insert 15 at index 1: [10, 15, 20, 30]
After extend [40, 50]: [10, 15, 20, 30, 40, 50]
After remove 20: [10, 15, 30, 40, 50]
Final list: [10, 15, 30, 40, 50]
```

**Category:** Implementation
**Prerequisite LOs:** 9.2.1, 9.2.2, 9.2.3

---

### Q2: Pop and Sort Operations (3 minutes, Low Difficulty)

**Problem:**
Given `numbers = [45, 23, 67, 12, 89, 34, 56]`:
1. Pop the last element and print it
2. Pop the element at index 2 and print it
3. Sort the remaining list in ascending order
4. Sort the list in descending order
5. Reverse the list

Print the list after each operation.

**Expected Output:**
```
After pop last: [45, 23, 67, 12, 89, 34]
Popped: 56
After pop index 2: [45, 23, 12, 89, 34]
Popped: 67
After sort ascending: [12, 23, 34, 45, 89]
After sort descending: [89, 45, 34, 23, 12]
After reverse: [12, 23, 34, 45, 89]
```

**Category:** Implementation
**Prerequisite LOs:** 9.2.1, 9.2.2, 9.2.3

---

### Q3: Shopping Cart Manager (5 minutes, Medium Difficulty)

**Problem:**
Create a shopping cart system using lists:

1. Start with empty cart
2. Add these items (as strings): "Laptop", "Mouse", "Keyboard"
3. Insert "Monitor" at position 1
4. Add "USB Cable" to the end
5. Customer changes mind - remove "Mouse"
6. Sort items alphabetically
7. Count how many items start with 'M'
8. Find the index of "Laptop"

Print the cart and results after each significant operation.

**Expected Output:**
```
Initial cart: []
After adding items: ['Laptop', 'Mouse', 'Keyboard']
After insert Monitor: ['Laptop', 'Monitor', 'Mouse', 'Keyboard']
After adding USB Cable: ['Laptop', 'Monitor', 'Mouse', 'Keyboard', 'USB Cable']
After removing Mouse: ['Laptop', 'Monitor', 'Keyboard', 'USB Cable']
After sorting: ['Keyboard', 'Laptop', 'Monitor', 'USB Cable']
Items starting with M: 1
Index of Laptop: 1
Final cart: ['Keyboard', 'Laptop', 'Monitor', 'USB Cable']
```

**Category:** Application
**Prerequisite LOs:** 9.2.1, 9.2.2, 9.2.3

---

### Q4: Student Grade Management (5 minutes, Medium Difficulty)

**Problem:**
You have a list of student scores:
```python
scores = [78, 92, 85, 78, 90, 88, 78, 95, 82, 78]
```

Perform these operations:
1. Count how many students scored 78
2. Find the index of the first score of 90
3. Remove the first occurrence of 78
4. Add a new score of 88 to the end
5. Sort scores in descending order
6. Pop the highest score (first element after sorting)
7. Calculate and print:
   - Total number of students
   - Average score (rounded to 1 decimal)
   - Highest remaining score
   - Lowest remaining score

**Expected Output:**
```
Count of 78: 4
Index of first 90: 4
After removing first 78: [92, 85, 78, 90, 88, 78, 95, 82, 78]
After adding 88: [92, 85, 78, 90, 88, 78, 95, 82, 78, 88]
After sorting descending: [95, 92, 90, 88, 88, 85, 82, 78, 78, 78]
Popped highest: 95
Final scores: [92, 90, 88, 88, 85, 82, 78, 78, 78]

Statistics:
Total students: 9
Average score: 84.3
Highest score: 92
Lowest score: 78
```

**Category:** Application
**Prerequisite LOs:** 9.2.1, 9.2.2, 9.2.3

---

### Q5: Playlist Manager (5 minutes, Medium Difficulty)

**Problem:**
Create a music playlist manager with these features:

```python
playlist = []
```

Implement these operations:
1. Add songs: "Song A", "Song B", "Song C", "Song D", "Song E"
2. Insert "Song X" at position 2
3. User dislikes "Song B" - remove it
4. Add "Song F" and "Song G" using extend
5. Shuffle by reversing the playlist
6. Create a backup copy of the playlist
7. In the backup, remove last 2 songs using pop
8. Sort original playlist alphabetically
9. Show both playlists

Then answer:
- How many songs in original playlist?
- How many times does "Song X" appear?
- What's the index of "Song D" in original playlist?

**Expected Output:**
```
After adding initial songs: ['Song A', 'Song B', 'Song C', 'Song D', 'Song E']
After insert Song X: ['Song A', 'Song B', 'Song X', 'Song C', 'Song D', 'Song E']
After removing Song B: ['Song A', 'Song X', 'Song C', 'Song D', 'Song E']
After extending: ['Song A', 'Song X', 'Song C', 'Song D', 'Song E', 'Song F', 'Song G']
After reversing: ['Song G', 'Song F', 'Song E', 'Song D', 'Song C', 'Song X', 'Song A']
Backup created

Backup after removing last 2:
['Song G', 'Song F', 'Song E', 'Song D', 'Song C']

Original after sorting:
['Song A', 'Song C', 'Song D', 'Song E', 'Song F', 'Song G', 'Song X']

Backup playlist:
['Song G', 'Song F', 'Song E', 'Song D', 'Song C']

Original playlist:
['Song A', 'Song C', 'Song D', 'Song E', 'Song F', 'Song G', 'Song X']

Analysis:
Total songs in original: 7
Occurrences of 'Song X': 1
Index of 'Song D': 2
```

**Category:** Application
**Prerequisite LOs:** 9.2.1, 9.2.2, 9.2.3
