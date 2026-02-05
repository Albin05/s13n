## Question Bank: Creating and Initializing Sets for Unique Values

---

### Q1: Basic Set Creation (3 minutes, Low Difficulty)

Write a program that creates sets using three different methods:
1. Create a set `colors` using curly braces with values: `'red'`, `'green'`, `'blue'`, `'red'`
2. Create a set `numbers` using `set()` from the list `[10, 20, 30, 20, 10]`
3. Create an empty set called `empty`
4. Print each set, its type, and its length

**Expected Output:**
```
colors: {'red', 'green', 'blue'}
Type: <class 'set'>, Length: 3
numbers: {10, 20, 30}
Type: <class 'set'>, Length: 3
empty: set()
Type: <class 'set'>, Length: 0
```

**Key Concepts:** Set creation methods, duplicate removal, empty set syntax

---

### Q2: Duplicate Removal (3 minutes, Low Difficulty)

Given the following list of student IDs with duplicates:
```python
student_ids = [101, 203, 101, 305, 203, 407, 305, 509, 101, 407]
```

Write a program that:
1. Prints the original list and its length
2. Converts it to a set and prints the unique IDs
3. Converts back to a sorted list and prints it
4. Prints how many duplicates were removed

**Expected Output:**
```
Original: [101, 203, 101, 305, 203, 407, 305, 509, 101, 407]
Original count: 10
Unique IDs: {101, 203, 305, 407, 509}
Sorted unique: [101, 203, 305, 407, 509]
Duplicates removed: 5
```

**Key Concepts:** List to set conversion, duplicate counting, sorting

---

### Q3: Unique Word Counter (5 minutes, Medium Difficulty)

Write a program that analyzes text for unique words:

```python
text = "the quick brown fox jumps over the lazy dog the fox the dog"
```

1. Split the text into words
2. Find all unique words (case-insensitive)
3. Print the total word count and unique word count
4. Print the unique words in alphabetical order
5. Find words that appear more than once

**Expected Output:**
```
Total words: 12
Unique words: 8
Alphabetical: ['brown', 'dog', 'fox', 'jumps', 'lazy', 'over', 'quick', 'the']
Repeated words: {'the', 'fox', 'dog'}
```

**Key Concepts:** String splitting, case-insensitive comparison, set operations

---

### Q4: Visitor Tracking System (5 minutes, Medium Difficulty)

Write a program that tracks unique website visitors across three time periods:

```python
morning_visitors = ['user_1', 'user_2', 'user_3', 'user_1', 'user_4']
afternoon_visitors = ['user_2', 'user_5', 'user_3', 'user_6', 'user_2']
evening_visitors = ['user_1', 'user_7', 'user_5', 'user_8', 'user_1']
```

1. Convert each list to a set to get unique visitors per period
2. Print unique visitor count for each period
3. Find total unique visitors across all periods (use union)
4. Find visitors who came in ALL three periods (use intersection)
5. Find visitors who came only in the morning

**Expected Output:**
```
Morning unique: 4
Afternoon unique: 4
Evening unique: 4
Total unique visitors: 8
Visitors in all periods: {'user_1'} (or set() depending on data)
Morning only: {'user_4'}
```

**Key Concepts:** Set creation from lists, union, intersection, difference

---

### Q5: Email Deduplication (5 minutes, Medium Difficulty)

Write a program that processes a mailing list:

```python
emails = [
    'alice@mail.com', 'Bob@Mail.com', 'alice@mail.com',
    'charlie@mail.com', 'bob@mail.com', 'ALICE@MAIL.COM',
    'diana@mail.com', 'Charlie@Mail.com'
]
```

1. Normalize all emails to lowercase
2. Find unique emails using a set
3. Print original count vs unique count
4. Identify which emails had duplicates
5. Print the final clean mailing list (sorted)

**Expected Output:**
```
Original count: 8
Unique count: 4
Emails with duplicates: {'alice@mail.com', 'bob@mail.com', 'charlie@mail.com'}
Clean mailing list:
  alice@mail.com
  bob@mail.com
  charlie@mail.com
  diana@mail.com
```

**Key Concepts:** Case normalization, deduplication, finding duplicates
