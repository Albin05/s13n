## Question Bank: Understanding Tuple Immutability

### Q1: Testing Immutability (3 minutes, Low Difficulty)

**Problem:**
Given `data = (10, 20, 30, 40, 50)`, attempt these operations and explain what happens:
1. Try to change element at index 2 to 999
2. Try to append 60 to the tuple
3. Try to remove 30 from the tuple
4. Create a new tuple by concatenating with (60, 70)
5. Create a new tuple with element at index 2 changed to 999 (using slicing)

**Expected Output:**
```
Attempting data[2] = 999:
  TypeError: 'tuple' object does not support item assignment

Attempting data.append(60):
  AttributeError: 'tuple' object has no attribute 'append'

Attempting data.remove(30):
  AttributeError: 'tuple' object has no attribute 'remove'

Concatenation: (10, 20, 30, 40, 50, 60, 70)
Original unchanged: (10, 20, 30, 40, 50)

Modified copy: (10, 20, 999, 40, 50)
Original still: (10, 20, 30, 40, 50)
```

**Category:** Implementation
**Prerequisite LOs:** 9.2.7

---

### Q2: Shallow Immutability (3 minutes, Low Difficulty)

**Problem:**
Given `container = (1, 2, [3, 4, 5], 6)`:
1. Try to change container[0] to 100
2. Try to replace container[2] with [7, 8, 9]
3. Modify the list at container[2] by appending 6
4. Modify the list at container[2] by changing first element to 999
5. Print the final state and explain what happened

**Expected Output:**
```
Attempting container[0] = 100:
  TypeError: 'tuple' object does not support item assignment

Attempting container[2] = [7, 8, 9]:
  TypeError: 'tuple' object does not support item assignment

Appending to container[2]:
  Success! container[2].append(6) works
  Container is now: (1, 2, [3, 4, 5, 6], 6)

Modifying container[2][0]:
  Success! container[2][0] = 999 works
  Container is now: (1, 2, [999, 4, 5, 6], 6)

Explanation: The tuple structure is immutable (cannot reassign elements),
but the mutable objects INSIDE can still be modified.
```

**Category:** Implementation
**Prerequisite LOs:** 9.2.7

---

### Q3: Hashability and Dictionary Keys (5 minutes, Medium Difficulty)

**Problem:**
Create a coordinate-based game system using tuples as dictionary keys:

1. Create a `game_map` dictionary with these locations:
   - (0, 0): 'Start'
   - (5, 3): 'Enemy'
   - (10, 7): 'Treasure'
   - (3, 9): 'Trap'

2. Write a function `move_player(position, direction)` that:
   - Takes current position tuple and direction ('up', 'down', 'left', 'right')
   - Returns new position tuple
   - up: y+1, down: y-1, left: x-1, right: x+1

3. Start at (0, 0) and move: right, right, up, up, up, right, right, right
4. Print what's at each position along the way
5. Try to use a list [0, 0] as a dictionary key and show the error

**Expected Output:**
```
Game Map created with 4 locations

Starting at (0, 0): Start

Move right to (1, 0): Empty
Move right to (2, 0): Empty
Move up to (2, 1): Empty
Move up to (2, 2): Empty
Move up to (2, 3): Empty
Move right to (3, 3): Empty
Move right to (4, 3): Empty
Move right to (5, 3): Enemy

Path complete! Found: Enemy at (5, 3)

Attempting to use list as key:
TypeError: unhashable type: 'list'
Lists cannot be dictionary keys because they are mutable.
Tuples work because they are immutable and hashable.
```

**Category:** Application
**Prerequisite LOs:** 9.2.7

---

### Q4: Configuration Management (5 minutes, Medium Difficulty)

**Problem:**
Create an immutable configuration system:

```python
# Database configuration tuple
DB_CONFIG = (
    'postgresql',  # db_type
    'localhost',   # host
    5432,          # port
    'production_db',  # database
    True           # ssl_enabled
)
```

Write functions:
1. `get_connection_string(config)` - returns formatted connection string
2. `update_config(config, **kwargs)` - returns NEW tuple with updated values
   - Takes keyword args: db_type, host, port, database, ssl_enabled
   - Only updates provided values
3. Demonstrate that original config never changes
4. Show the benefit: try to accidentally modify the original config
5. Compare with a mutable list version and show the danger

**Expected Output:**
```
Original config: ('postgresql', 'localhost', 5432, 'production_db', True)
Connection string: postgresql://localhost:5432/production_db?ssl=true

Updated config (new host): ('postgresql', 'db.example.com', 5432, 'production_db', True)
Original unchanged: ('postgresql', 'localhost', 5432, 'production_db', True)

Updated config (port and db): ('postgresql', 'localhost', 3306, 'test_db', True)
Original still unchanged: ('postgresql', 'localhost', 5432, 'production_db', True)

Attempting to modify original:
TypeError: 'tuple' object does not support item assignment
✓ Original config is protected!

Danger with mutable list:
List config: ['postgresql', 'localhost', 5432, 'production_db', True]
Accidental modification: ['WRONG', 'localhost', 5432, 'production_db', True]
✗ Original config was corrupted!

Conclusion: Immutable tuples prevent accidental config corruption.
```

**Category:** Application
**Prerequisite LOs:** 9.2.7

---

### Q5: Caching with Tuples (5 minutes, Medium Difficulty)

**Problem:**
Implement a memoization system using tuples as cache keys:

```python
# Function to compute expensive operation
def expensive_calculation(a, b, c):
    """Simulates expensive computation"""
    result = (a ** 2) + (b ** 3) + (c ** 4)
    return result
```

Create a caching system:
1. Create a `cache` dictionary
2. Write `cached_calculation(a, b, c)` that:
   - Uses (a, b, c) tuple as cache key
   - Returns cached result if exists
   - Otherwise computes, caches, and returns
3. Write `cache_stats()` to show hits and misses
4. Test with these calls and show cache working:
   - (2, 3, 4) - miss
   - (1, 2, 3) - miss
   - (2, 3, 4) - hit!
   - (1, 2, 3) - hit!
   - (5, 6, 7) - miss
5. Try to use [2, 3, 4] as key and explain why it fails

**Expected Output:**
```
Cache initialized

Call cached_calculation(2, 3, 4):
  Cache MISS - computing...
  Result: 287
  Cache now has 1 entry

Call cached_calculation(1, 2, 3):
  Cache MISS - computing...
  Result: 90
  Cache now has 2 entries

Call cached_calculation(2, 3, 4):
  Cache HIT! Returning cached value
  Result: 287
  Cache still has 2 entries

Call cached_calculation(1, 2, 3):
  Cache HIT! Returning cached value
  Result: 90
  Cache still has 2 entries

Call cached_calculation(5, 6, 7):
  Cache MISS - computing...
  Result: 2642
  Cache now has 3 entries

Cache Statistics:
  Total calls: 5
  Cache hits: 2
  Cache misses: 3
  Hit rate: 40.0%

Attempting to use list [2, 3, 4] as cache key:
TypeError: unhashable type: 'list'

Explanation: Lists cannot be dictionary keys because:
  1. Lists are mutable (can change)
  2. Mutable objects cannot be hashed
  3. Dictionary keys must be hashable
  4. Tuples are immutable and hashable - perfect for caching!
```

**Category:** Application
**Prerequisite LOs:** 9.2.7
