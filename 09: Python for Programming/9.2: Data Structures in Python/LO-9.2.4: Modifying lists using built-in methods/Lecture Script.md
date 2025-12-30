## Lecture Script: Modifying Lists Using Built-in Methods

**Duration:** 18 minutes

---

### Hook (2 minutes)

"You've built a shopping cart list, but now the customer changes their mind - they want to add more items, remove some, rearrange the order, and maybe even sort by price. Do you create a new list from scratch? No! Python lists come with powerful built-in methods that let you modify them in-place.

Think of list methods as your toolkit for list manipulation. Want to add an item? Use append(). Need to remove something specific? Use remove(). Want to sort? Use sort(). These methods transform your lists dynamically, making your code flexible and efficient.

Today, we'll master the essential list methods that every Python programmer needs. By the end, you'll be modifying lists with confidence, whether you're building shopping carts, managing to-do lists, or processing data streams."

---

### Section 1: Adding Elements (3 minutes)

**append() - Add Single Element to End:**

```python
# Add one item to the end
fruits = ['apple', 'banana']
fruits.append('orange')
print(fruits)  # ['apple', 'banana', 'orange']

# Works with any type
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # [1, 2, 3, 4]

# Can append complex objects
cart = []
cart.append({'item': 'laptop', 'price': 999})
cart.append({'item': 'mouse', 'price': 29})
print(cart)  
# [{'item': 'laptop', 'price': 999}, {'item': 'mouse', 'price': 29}]
```

**extend() - Add Multiple Elements:**

```python
# Add all elements from another iterable
fruits = ['apple', 'banana']
fruits.extend(['orange', 'mango'])
print(fruits)  # ['apple', 'banana', 'orange', 'mango']

# Extend with any iterable
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)  # [1, 2, 3, 4, 5, 6]

# Even strings (iterates over characters)
letters = ['a', 'b']
letters.extend('cd')
print(letters)  # ['a', 'b', 'c', 'd']
```

**append() vs extend():**

```python
# append adds the entire object as one element
list1 = [1, 2, 3]
list1.append([4, 5])
print(list1)  # [1, 2, 3, [4, 5]] - nested list

# extend adds each element individually
list2 = [1, 2, 3]
list2.extend([4, 5])
print(list2)  # [1, 2, 3, 4, 5] - flat list
```

**insert() - Add at Specific Position:**

```python
# Insert at index
fruits = ['apple', 'orange', 'mango']
fruits.insert(1, 'banana')
print(fruits)  # ['apple', 'banana', 'orange', 'mango']

# Insert at beginning
numbers = [2, 3, 4]
numbers.insert(0, 1)
print(numbers)  # [1, 2, 3, 4]

# Insert at end (like append)
items = [1, 2, 3]
items.insert(len(items), 4)
print(items)  # [1, 2, 3, 4]

# Index beyond length inserts at end
data = [1, 2, 3]
data.insert(100, 4)
print(data)  # [1, 2, 3, 4]
```

---

### Section 2: Removing Elements (4 minutes)

**remove() - Remove by Value:**

```python
# Remove first occurrence
fruits = ['apple', 'banana', 'orange', 'banana']
fruits.remove('banana')
print(fruits)  # ['apple', 'orange', 'banana']

# ValueError if not found
numbers = [1, 2, 3]
try:
    numbers.remove(5)
except ValueError:
    print("Value not in list")

# Safe removal
items = [1, 2, 3, 4, 5]
if 3 in items:
    items.remove(3)
print(items)  # [1, 2, 4, 5]
```

**pop() - Remove and Return by Index:**

```python
# Pop last element (default)
numbers = [1, 2, 3, 4, 5]
last = numbers.pop()
print(last)     # 5
print(numbers)  # [1, 2, 3, 4]

# Pop at specific index
fruits = ['apple', 'banana', 'orange']
second = fruits.pop(1)
print(second)   # 'banana'
print(fruits)   # ['apple', 'orange']

# Pop first element
items = [10, 20, 30]
first = items.pop(0)
print(first)    # 10
print(items)    # [20, 30]

# IndexError if index out of range
try:
    items.pop(100)
except IndexError:
    print("Index out of range")
```

**Using pop() for Stack Operations:**

```python
# LIFO - Last In, First Out
stack = []

# Push items
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # [1, 2, 3]

# Pop items
print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack)        # [1]
```

**clear() - Remove All Elements:**

```python
# Empty the list
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)  # []

# Equivalent to
numbers = [1, 2, 3, 4, 5]
numbers[:] = []
print(numbers)  # []
```

**del Statement:**

```python
# Delete by index
fruits = ['apple', 'banana', 'orange', 'mango']
del fruits[1]
print(fruits)  # ['apple', 'orange', 'mango']

# Delete slice
numbers = [1, 2, 3, 4, 5, 6, 7]
del numbers[2:5]
print(numbers)  # [1, 2, 6, 7]

# Delete entire list
items = [1, 2, 3]
del items
# items no longer exists
```

---

### Section 3: Sorting and Reversing (3 minutes)

**sort() - Sort In-Place:**

```python
# Sort ascending (default)
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Sort descending
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort(reverse=True)
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# Sort strings alphabetically
fruits = ['orange', 'apple', 'mango', 'banana']
fruits.sort()
print(fruits)  # ['apple', 'banana', 'mango', 'orange']

# Case-sensitive sorting
words = ['Zebra', 'apple', 'Mango', 'banana']
words.sort()
print(words)  # ['Mango', 'Zebra', 'apple', 'banana']

# Case-insensitive sorting
words = ['Zebra', 'apple', 'Mango', 'banana']
words.sort(key=str.lower)
print(words)  # ['apple', 'banana', 'Mango', 'Zebra']
```

**Custom Sorting with key:**

```python
# Sort by length
words = ['apple', 'pie', 'banana', 'cherry']
words.sort(key=len)
print(words)  # ['pie', 'apple', 'banana', 'cherry']

# Sort tuples by second element
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
students.sort(key=lambda x: x[1])
print(students)  
# [('Charlie', 78), ('Alice', 85), ('Bob', 92)]

# Sort dictionaries
products = [
    {'name': 'laptop', 'price': 999},
    {'name': 'mouse', 'price': 29},
    {'name': 'keyboard', 'price': 79}
]
products.sort(key=lambda x: x['price'])
print(products)
# [{'name': 'mouse', 'price': 29}, 
#  {'name': 'keyboard', 'price': 79}, 
#  {'name': 'laptop', 'price': 999}]
```

**reverse() - Reverse In-Place:**

```python
# Reverse order
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]

# Reverse strings
fruits = ['apple', 'banana', 'orange']
fruits.reverse()
print(fruits)  # ['orange', 'banana', 'apple']

# reverse() vs [::-1]
# reverse() modifies in-place
lst = [1, 2, 3]
lst.reverse()       # lst is now [3, 2, 1]

# [::-1] creates new list
lst = [1, 2, 3]
rev = lst[::-1]     # lst unchanged, rev is [3, 2, 1]
```

---

### Section 4: Searching and Counting (3 minutes)

**index() - Find Position:**

```python
# Find first occurrence
fruits = ['apple', 'banana', 'orange', 'banana']
pos = fruits.index('banana')
print(pos)  # 1

# ValueError if not found
try:
    pos = fruits.index('mango')
except ValueError:
    print("Not found")

# Search in range
fruits = ['apple', 'banana', 'orange', 'banana']
pos = fruits.index('banana', 2)  # Start from index 2
print(pos)  # 3

# Safe index finding
def safe_index(lst, value):
    try:
        return lst.index(value)
    except ValueError:
        return -1

fruits = ['apple', 'banana', 'orange']
print(safe_index(fruits, 'banana'))  # 1
print(safe_index(fruits, 'mango'))   # -1
```

**count() - Count Occurrences:**

```python
# Count how many times value appears
numbers = [1, 2, 2, 3, 2, 4, 2, 5]
count = numbers.count(2)
print(count)  # 4

# Count in strings
letters = ['a', 'b', 'c', 'a', 'b', 'a']
print(letters.count('a'))  # 3
print(letters.count('d'))  # 0

# Find most common element
votes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Alice', 'Bob']
candidates = list(set(votes))
counts = [(c, votes.count(c)) for c in candidates]
winner = max(counts, key=lambda x: x[1])
print(f"Winner: {winner[0]} with {winner[1]} votes")
# Winner: Alice with 3 votes
```

---

### Section 5: Copying Lists (2 minutes)

**copy() - Shallow Copy:**

```python
# Create independent copy
original = [1, 2, 3, 4, 5]
copy = original.copy()

copy.append(6)
print(original)  # [1, 2, 3, 4, 5] - unchanged
print(copy)      # [1, 2, 3, 4, 5, 6]

# Equivalent methods
original = [1, 2, 3]
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)
# All create independent copies
```

**Shallow vs Deep Copy:**

```python
# Shallow copy - nested objects still referenced
original = [[1, 2], [3, 4]]
shallow = original.copy()

shallow[0][0] = 999
print(original)  # [[999, 2], [3, 4]] - affected!
print(shallow)   # [[999, 2], [3, 4]]

# Deep copy - fully independent
import copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0][0] = 999
print(original)  # [[1, 2], [3, 4]] - unchanged
print(deep)      # [[999, 2], [3, 4]]
```

---

### Section 6: Method Chaining and Return Values (2 minutes)

**Important: Most Methods Return None:**

```python
# These modify in-place and return None
numbers = [3, 1, 2]
result = numbers.sort()
print(result)   # None
print(numbers)  # [1, 2, 3] - list is sorted

# Common mistake
numbers = [3, 1, 2]
numbers = numbers.sort()  # DON'T DO THIS!
print(numbers)  # None - you've lost your list!

# Methods that return values
numbers = [1, 2, 3]
popped = numbers.pop()     # Returns removed element
print(popped)              # 3
```

**Correct Patterns:**

```python
# Modify then use
numbers = [3, 1, 2]
numbers.sort()
print(numbers)  # [1, 2, 3]

# If you need original
original = [3, 1, 2]
sorted_copy = sorted(original)  # Built-in function, returns new list
print(original)     # [3, 1, 2] - unchanged
print(sorted_copy)  # [1, 2, 3]

# Reverse comparison
original = [1, 2, 3]
reversed_copy = list(reversed(original))  # Built-in, returns iterator
print(original)       # [1, 2, 3]
print(reversed_copy)  # [3, 2, 1]
```

---

### Section 7: Practical Applications (1 minute)

**To-Do List Manager:**

```python
todos = []

# Add tasks
todos.append("Buy groceries")
todos.append("Call mom")
todos.insert(0, "Urgent: Pay bills")

# Complete task
if "Call mom" in todos:
    todos.remove("Call mom")

# View tasks
todos.sort()
print("To-Do List:")
for i, task in enumerate(todos, 1):
    print(f"{i}. {task}")
```

**Shopping Cart:**

```python
cart = []

# Add items
cart.append({'item': 'laptop', 'price': 999, 'qty': 1})
cart.append({'item': 'mouse', 'price': 29, 'qty': 2})

# Sort by price
cart.sort(key=lambda x: x['price'], reverse=True)

# Calculate total
total = sum(item['price'] * item['qty'] for item in cart)
print(f"Total: ${total}")  # Total: $1057
```

---

### Summary (1 minute)

Today we mastered list methods for modifying lists:

**Adding Elements:**
- `append(x)` - Add single element to end
- `extend(iterable)` - Add multiple elements
- `insert(i, x)` - Insert at specific position

**Removing Elements:**
- `remove(x)` - Remove first occurrence of value
- `pop([i])` - Remove and return element at index
- `clear()` - Remove all elements

**Organizing:**
- `sort()` - Sort in-place
- `reverse()` - Reverse in-place

**Searching:**
- `index(x)` - Find position of value
- `count(x)` - Count occurrences

**Copying:**
- `copy()` - Create shallow copy

**Remember:**
- Most methods modify in-place and return None
- Use `sorted()` and `reversed()` built-ins for new lists
- Check existence before removing to avoid errors
- Methods are powerful but destructive - copy first if needed

Master these methods and you'll handle lists like a pro!
