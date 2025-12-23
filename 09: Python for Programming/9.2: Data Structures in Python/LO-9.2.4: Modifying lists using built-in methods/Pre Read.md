# Pre-Read: Modifying Lists Using Built-in Methods

## What You'll Learn
In this lesson, you'll learn how to modify lists using Python's built-in list methods - powerful tools for adding, removing, sorting, and manipulating list contents.

## Why This Matters
List methods let you:
- Add items to a shopping cart (append, insert)
- Remove completed tasks from a to-do list (remove, pop)
- Sort students by grade (sort)
- Find where an item is located (index)
- Count how many times an item appears (count)

These methods make lists dynamic and easy to work with in real applications.

---

## Lists Are Mutable

Unlike strings and tuples, lists can be changed after creation. List methods modify the list **in place** (change the original list).

```python
fruits = ["apple", "banana"]
fruits.append("cherry")  # Modifies fruits directly
print(fruits)  # ["apple", "banana", "cherry"]
```

---

## Adding Items to Lists

### append() - Add to End

Adds a single item to the end of the list:

```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # [1, 2, 3, 4]

numbers.append(5)
print(numbers)  # [1, 2, 3, 4, 5]
```

**Use case:** Building a list one item at a time

```python
tasks = []
tasks.append("Buy groceries")
tasks.append("Finish homework")
tasks.append("Call mom")
print(tasks)  # ["Buy groceries", "Finish homework", "Call mom"]
```

### insert() - Add at Specific Position

Inserts an item at a specific index:

```python
colors = ["red", "blue", "green"]
colors.insert(1, "yellow")  # Insert at index 1
print(colors)  # ["red", "yellow", "blue", "green"]
```

**Syntax:** `list.insert(index, item)`

```python
numbers = [1, 2, 4, 5]
numbers.insert(2, 3)  # Insert 3 at index 2
print(numbers)  # [1, 2, 3, 4, 5]
```

### extend() - Add Multiple Items

Adds all items from another list:

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
print(list1)  # [1, 2, 3, 4, 5, 6]
```

**append() vs extend():**

```python
# append adds the whole list as one item
list1 = [1, 2, 3]
list1.append([4, 5])
print(list1)  # [1, 2, 3, [4, 5]]

# extend adds each item individually
list2 = [1, 2, 3]
list2.extend([4, 5])
print(list2)  # [1, 2, 3, 4, 5]
```

---

## Removing Items from Lists

### remove() - Remove by Value

Removes the first occurrence of a value:

```python
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")  # Removes first "banana"
print(fruits)  # ["apple", "cherry", "banana"]
```

**Warning:** Raises error if item doesn't exist

```python
colors = ["red", "green", "blue"]
colors.remove("yellow")  # ValueError: 'yellow' is not in list
```

**Safe removal:**
```python
if "yellow" in colors:
    colors.remove("yellow")
```

### pop() - Remove by Index

Removes and **returns** item at given index:

```python
numbers = [10, 20, 30, 40, 50]
removed = numbers.pop(2)  # Remove index 2
print(removed)  # 30
print(numbers)  # [10, 20, 40, 50]
```

**No index = remove last item:**
```python
numbers = [10, 20, 30, 40, 50]
last = numbers.pop()  # Remove last
print(last)    # 50
print(numbers) # [10, 20, 30, 40]
```

**Use case:** Stack operations (LIFO)

```python
stack = []
stack.append(1)  # Push
stack.append(2)
stack.append(3)
print(stack.pop())  # 3 (Pop)
print(stack.pop())  # 2
```

### clear() - Remove All Items

Empties the entire list:

```python
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)  # []
```

---

## Sorting and Reversing

### sort() - Sort In Place

Sorts the list permanently:

```python
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)  # [1, 2, 5, 8, 9]
```

**Reverse order:**
```python
numbers = [5, 2, 8, 1, 9]
numbers.sort(reverse=True)
print(numbers)  # [9, 8, 5, 2, 1]
```

**Alphabetical sorting:**
```python
names = ["Charlie", "Alice", "Bob"]
names.sort()
print(names)  # ["Alice", "Bob", "Charlie"]
```

### reverse() - Reverse Order

Reverses the list in place:

```python
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]
```

---

## Finding and Counting

### index() - Find Position

Returns the index of first occurrence:

```python
fruits = ["apple", "banana", "cherry", "banana"]
position = fruits.index("banana")
print(position)  # 1
```

**With start/end range:**
```python
fruits = ["apple", "banana", "cherry", "banana"]
position = fruits.index("banana", 2)  # Search from index 2
print(position)  # 3
```

**Error if not found:**
```python
fruits = ["apple", "banana"]
fruits.index("orange")  # ValueError: 'orange' is not in list
```

### count() - Count Occurrences

Counts how many times a value appears:

```python
numbers = [1, 2, 2, 3, 2, 4, 2, 5]
count = numbers.count(2)
print(count)  # 4
```

```python
votes = ["Alice", "Bob", "Alice", "Charlie", "Alice", "Bob"]
alice_votes = votes.count("Alice")
print(f"Alice got {alice_votes} votes")  # Alice got 3 votes
```

---

## Real-World Examples

### Example 1: Shopping Cart

```python
cart = []

# Add items
cart.append("Laptop")
cart.append("Mouse")
cart.append("Keyboard")

# Insert priority item at start
cart.insert(0, "Charger")

# Remove item
cart.remove("Mouse")

print(cart)  # ["Charger", "Laptop", "Keyboard"]
```

### Example 2: Task Manager

```python
tasks = ["Buy groceries", "Walk dog", "Study Python", "Clean room"]

# Complete a task (remove)
tasks.remove("Walk dog")

# Add urgent task at beginning
tasks.insert(0, "Take medicine")

# Check remaining
print(f"{len(tasks)} tasks remaining")
```

### Example 3: Top Scores

```python
scores = [750, 920, 680, 890, 810]

# Sort to get rankings
scores.sort(reverse=True)
print("Rankings:", scores)  # [920, 890, 810, 750, 680]

# Find specific score position
player_score = 810
rank = scores.index(810) + 1  # +1 for human-friendly ranking
print(f"Your rank: {rank}")  # Your rank: 3
```

---

## Method Chaining

Some methods return None (modify in place), so can't chain:

```python
# This WON'T work
numbers = [3, 1, 2].sort()
print(numbers)  # None (sort returns None!)

# Do this instead
numbers = [3, 1, 2]
numbers.sort()
print(numbers)  # [1, 2, 3]
```

---

## Try It Yourself (Before Class)

Run this code:

```python
# Start with empty list
favorite_movies = []

# Add movies
favorite_movies.append("The Matrix")
favorite_movies.append("Inception")
favorite_movies.append("Interstellar")

# Insert at beginning
favorite_movies.insert(0, "The Shawshank Redemption")

print("Movies:", favorite_movies)

# Sort alphabetically
favorite_movies.sort()
print("Sorted:", favorite_movies)

# Remove one
favorite_movies.remove("Inception")
print("After removal:", favorite_movies)

# Count
print("Total movies:", len(favorite_movies))
```

**Try:**
1. Create a list of numbers and sort them
2. Add items using append and extend
3. Remove items using remove and pop
4. Find the index of a specific item

---

## Key Takeaways

Before class, remember:
1. **append()** - add item to end
2. **insert()** - add at specific position
3. **remove()** - remove by value (first occurrence)
4. **pop()** - remove by index, returns value
5. **sort()** - sort in place
6. **reverse()** - reverse order
7. **index()** - find position
8. **count()** - count occurrences

## What's Next?

In the live session, we'll:
- Practice all list methods with examples
- Learn when to use each method
- Combine methods for complex operations
- Handle errors gracefully
- Build real applications using list methods

See you in class!
