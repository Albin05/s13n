## Editorials: Modifying Lists Using Built-in Methods

### Q1 Solution: Basic List Method Operations

```python
# Start with empty list
lst = []
print(f"Initial: {lst}")

# 1. Append 10, 20, 30
lst.append(10)
lst.append(20)
lst.append(30)
print(f"After append 10, 20, 30: {lst}")

# 2. Insert 15 at index 1
lst.insert(1, 15)
print(f"After insert 15 at index 1: {lst}")

# 3. Extend with [40, 50]
lst.extend([40, 50])
print(f"After extend [40, 50]: {lst}")

# 4. Remove 20
lst.remove(20)
print(f"After remove 20: {lst}")

# 5. Final list
print(f"Final list: {lst}")
```

**Explanation:**
- `append(x)` adds single element to end
- `insert(i, x)` inserts element at specific index
- `extend(iterable)` adds all elements from iterable
- `remove(x)` removes first occurrence of value

**Key Points:**
- append vs extend: append adds whole object, extend adds each element
- insert shifts elements to the right
- remove raises ValueError if value not found

---

### Q2 Solution: Pop and Sort Operations

```python
numbers = [45, 23, 67, 12, 89, 34, 56]

# 1. Pop last
popped_last = numbers.pop()
print(f"After pop last: {numbers}")
print(f"Popped: {popped_last}")

# 2. Pop at index 2
popped_index = numbers.pop(2)
print(f"After pop index 2: {numbers}")
print(f"Popped: {popped_index}")

# 3. Sort ascending
numbers.sort()
print(f"After sort ascending: {numbers}")

# 4. Sort descending
numbers.sort(reverse=True)
print(f"After sort descending: {numbers}")

# 5. Reverse
numbers.reverse()
print(f"After reverse: {numbers}")
```

**Explanation:**
- `pop()` without argument removes and returns last element
- `pop(i)` removes and returns element at index i
- `sort()` sorts in-place in ascending order
- `sort(reverse=True)` sorts in descending order
- `reverse()` reverses the list in-place

**Key Points:**
- pop() returns the removed element
- sort() modifies the list and returns None
- reverse() just reverses order, doesn't sort

---

### Q3 Solution: Shopping Cart Manager

```python
# 1. Start with empty cart
cart = []
print(f"Initial cart: {cart}")

# 2. Add items
cart.append("Laptop")
cart.append("Mouse")
cart.append("Keyboard")
print(f"After adding items: {cart}")

# 3. Insert Monitor at position 1
cart.insert(1, "Monitor")
print(f"After insert Monitor: {cart}")

# 4. Add USB Cable
cart.append("USB Cable")
print(f"After adding USB Cable: {cart}")

# 5. Remove Mouse
cart.remove("Mouse")
print(f"After removing Mouse: {cart}")

# 6. Sort alphabetically
cart.sort()
print(f"After sorting: {cart}")

# 7. Count items starting with 'M'
m_count = sum(1 for item in cart if item.startswith('M'))
print(f"Items starting with M: {m_count}")

# 8. Find index of Laptop
laptop_index = cart.index("Laptop")
print(f"Index of Laptop: {laptop_index}")

print(f"Final cart: {cart}")
```

**Explanation:**
- Build cart incrementally with append()
- insert() places item at specific position
- remove() deletes by value
- sort() arranges alphabetically
- List comprehension counts items matching condition
- index() finds position of value

**Application Pattern:**
This demonstrates a typical CRUD pattern:
- Create: append, insert
- Read: index, iteration
- Update: sort, modify
- Delete: remove

---

### Q4 Solution: Student Grade Management

```python
scores = [78, 92, 85, 78, 90, 88, 78, 95, 82, 78]

# 1. Count 78s
count_78 = scores.count(78)
print(f"Count of 78: {count_78}")

# 2. Find first 90
index_90 = scores.index(90)
print(f"Index of first 90: {index_90}")

# 3. Remove first 78
scores.remove(78)
print(f"After removing first 78: {scores}")

# 4. Add 88
scores.append(88)
print(f"After adding 88: {scores}")

# 5. Sort descending
scores.sort(reverse=True)
print(f"After sorting descending: {scores}")

# 6. Pop highest
highest = scores.pop(0)
print(f"Popped highest: {highest}")
print(f"Final scores: {scores}")

# 7. Statistics
total_students = len(scores)
average = sum(scores) / len(scores)
highest_remaining = max(scores)
lowest_remaining = min(scores)

print("\nStatistics:")
print(f"Total students: {total_students}")
print(f"Average score: {average:.1f}")
print(f"Highest score: {highest_remaining}")
print(f"Lowest score: {lowest_remaining}")
```

**Explanation:**
- `count(x)` returns number of occurrences
- `index(x)` finds first position of value
- `remove(x)` deletes first occurrence
- `append(x)` adds to end
- `sort(reverse=True)` sorts high to low
- `pop(0)` removes and returns first element
- `len()`, `sum()`, `max()`, `min()` for statistics

**Data Analysis Pattern:**
- Use count() for frequency
- Use sort() for ranking
- Use built-in functions for aggregation
- Combine methods for complex operations

---

### Q5 Solution: Playlist Manager

```python
# 1. Add initial songs
playlist = []
playlist.append("Song A")
playlist.append("Song B")
playlist.append("Song C")
playlist.append("Song D")
playlist.append("Song E")
print(f"After adding initial songs: {playlist}")

# 2. Insert Song X at position 2
playlist.insert(2, "Song X")
print(f"After insert Song X: {playlist}")

# 3. Remove Song B
playlist.remove("Song B")
print(f"After removing Song B: {playlist}")

# 4. Extend with Song F and G
playlist.extend(["Song F", "Song G"])
print(f"After extending: {playlist}")

# 5. Reverse playlist
playlist.reverse()
print(f"After reversing: {playlist}")

# 6. Create backup copy
backup = playlist.copy()
print("Backup created")

# 7. Remove last 2 from backup
backup.pop()
backup.pop()
print(f"\nBackup after removing last 2:")
print(backup)

# 8. Sort original
playlist.sort()
print(f"\nOriginal after sorting:")
print(playlist)

# 9. Show both playlists
print(f"\nBackup playlist:")
print(backup)
print(f"\nOriginal playlist:")
print(playlist)

# Analysis
total_songs = len(playlist)
song_x_count = playlist.count("Song X")
song_d_index = playlist.index("Song D")

print(f"\nAnalysis:")
print(f"Total songs in original: {total_songs}")
print(f"Occurrences of 'Song X': {song_x_count}")
print(f"Index of 'Song D': {song_d_index}")
```

**Explanation:**
- `append(x)` adds one song at a time
- `insert(i, x)` places song at specific position
- `remove(x)` deletes by name
- `extend(list)` adds multiple songs efficiently
- `reverse()` reverses order in-place
- `copy()` creates independent copy
- `pop()` removes from end
- `sort()` arranges alphabetically
- `len()`, `count()`, `index()` for analysis

**Copy Pattern:**
- Use `copy()` when you need independent version
- Modifications to copy don't affect original
- Shallow copy sufficient for simple lists
- For nested structures, use `copy.deepcopy()`

**Key Concepts:**
- List methods modify in-place (except pop which also returns value)
- copy() creates independent list for backup
- Combine methods to build complex operations
- Always check if value exists before remove/index
