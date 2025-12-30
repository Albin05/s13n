## Question Bank: Using Tuple Methods count() and index()

---

### Q1: Basic count() and index() Usage (3 minutes, Low Difficulty)

Write a program that:
1. Creates a tuple: `numbers = (5, 10, 5, 15, 20, 5, 25)`
2. Counts how many times `5` appears
3. Finds the index of the first occurrence of `10`
4. Finds the index of the second occurrence of `5`
5. Tries to find the index of `30` with error handling

**Expected Output:**
```
Count of 5: 3
First occurrence of 10 at index: 1
Second occurrence of 5 at index: 2
30 not found in tuple
```

**Key Concepts:**
- Using count() method
- Using index() method
- Finding nth occurrence
- Error handling with try-except

---

### Q2: Safe Index Finding (3 minutes, Low Difficulty)

Write a function `safe_index(tup, value)` that:
- Returns the index of value if it exists in the tuple
- Returns -1 if the value doesn't exist
- Use count() to check existence before calling index()

Test with:
```python
colors = ('red', 'blue', 'green', 'yellow')
print(safe_index(colors, 'blue'))    # 1
print(safe_index(colors, 'purple'))  # -1
```

**Expected Output:**
```
1
-1
```

**Key Concepts:**
- Combining count() and index()
- Safe searching without exceptions
- Function implementation

---

### Q3: Find All Occurrences (5 minutes, Medium Difficulty)

Write a function `find_all_indices(tup, value)` that:
- Returns a list of ALL indices where value appears
- Uses index() with start parameter in a loop
- Handles ValueError when no more occurrences exist

Test with:
```python
data = (10, 20, 10, 30, 10, 40, 10)
print(find_all_indices(data, 10))  # [0, 2, 4, 6]
print(find_all_indices(data, 20))  # [1]
print(find_all_indices(data, 50))  # []
```

**Expected Output:**
```
[0, 2, 4, 6]
[1]
[]
```

**Key Concepts:**
- Using index() with start parameter
- Loop until ValueError
- Building result list
- Handling edge cases

---

### Q4: Voting System (5 minutes, Medium Difficulty)

Write a program that implements a voting system:

1. Given votes: `votes = ('Alice', 'Bob', 'Alice', 'Charlie', 'Alice', 'Bob', 'Alice')`

2. Write `count_votes(votes)` that returns a dictionary:
   ```python
   {'Alice': 4, 'Bob': 2, 'Charlie': 1}
   ```

3. Write `find_winner(votes)` that:
   - Returns the candidate with most votes
   - Uses count() to tally votes
   
4. Write `get_vote_positions(votes, candidate)` that:
   - Returns list of indices where candidate received votes
   - Uses index() with start parameter

**Expected Output:**
```
Vote counts: {'Alice': 4, 'Bob': 2, 'Charlie': 1}
Winner: Alice with 4 votes
Alice received votes at positions: [0, 2, 4, 6]
Bob received votes at positions: [1, 5]
Charlie received votes at positions: [3]
```

**Key Concepts:**
- Frequency counting with count()
- Finding maximum using counts
- Position tracking with index()
- Dictionary for results

---

### Q5: Data Validation System (5 minutes, Medium Difficulty)

Write a data validation system for a tuple of field names:

1. Write `check_duplicates(fields)` that:
   - Finds and returns any duplicate fields
   - Uses count() to detect duplicates
   - Returns list of duplicates (unique)

2. Write `check_required(provided, required)` that:
   - Checks if all required fields are in provided fields
   - Returns list of missing fields
   - Uses count() to verify presence

3. Write `get_duplicate_positions(fields)` that:
   - Returns dictionary mapping each duplicate to its positions
   - Uses find_all_indices approach

Test with:
```python
provided = ('name', 'email', 'name', 'age', 'email')
required = ('name', 'email', 'age', 'city')
```

**Expected Output:**
```
Duplicates found: ['name', 'email']
name appears at positions: [0, 2]
email appears at positions: [1, 4]

Missing required fields: ['city']
```

**Key Concepts:**
- Data validation
- Duplicate detection
- Required field checking
- Position mapping

---

### Additional Practice Problems

**Practice 1:** Write a function that finds the spacing (distance) between consecutive occurrences of a value in a tuple.

**Practice 2:** Implement a function that checks if a tuple has a specific pattern (e.g., value appears exactly 3 times with specific spacing).

**Practice 3:** Create a tuple analyzer that generates statistics: most common element, least common element, elements appearing once.

**Practice 4:** Write a function that replaces nth occurrence of a value by creating a new tuple (remember: tuples are immutable).

**Practice 5:** Implement a function that checks if two tuples have the same frequency distribution of elements using count().
