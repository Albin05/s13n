## Modifying Lists Using Built-in Methods

### Adding Elements

```python
# append() - Add single element
fruits = ['apple']
fruits.append('banana')  # ['apple', 'banana']

# extend() - Add multiple elements
fruits.extend(['orange', 'mango'])
# ['apple', 'banana', 'orange', 'mango']

# insert() - Add at specific position
fruits.insert(1, 'grape')
# ['apple', 'grape', 'banana', 'orange', 'mango']
```

**Key Differences:**
```python
lst = [1, 2]
lst.append([3, 4])   # [1, 2, [3, 4]] - nested
lst.extend([3, 4])   # [1, 2, 3, 4] - flat
```

---

### Removing Elements

```python
numbers = [1, 2, 3, 2, 4]

# remove() - Remove by value (first occurrence)
numbers.remove(2)  # [1, 3, 2, 4]

# pop() - Remove and return by index
last = numbers.pop()     # Returns 4, list is [1, 3, 2]
second = numbers.pop(1)  # Returns 3, list is [1, 2]

# clear() - Remove all
numbers.clear()  # []
```

**Error Handling:**
```python
# remove raises ValueError if not found
if value in lst:
    lst.remove(value)

# pop raises IndexError if index invalid
if 0 <= index < len(lst):
    lst.pop(index)
```

---

### Sorting and Reversing

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() - Sort in-place
numbers.sort()              # [1, 1, 2, 3, 4, 5, 6, 9]
numbers.sort(reverse=True)  # [9, 6, 5, 4, 3, 2, 1, 1]

# reverse() - Reverse in-place
numbers.reverse()  # [1, 1, 2, 3, 4, 5, 6, 9]
```

**Custom Sorting:**
```python
# By length
words = ['apple', 'pie', 'banana']
words.sort(key=len)  # ['pie', 'apple', 'banana']

# Case-insensitive
words.sort(key=str.lower)

# By second element
pairs = [('a', 2), ('b', 1)]
pairs.sort(key=lambda x: x[1])  # [('b', 1), ('a', 2)]
```

---

### Searching and Counting

```python
items = ['a', 'b', 'c', 'b', 'd']

# index() - Find position
pos = items.index('b')  # 1 (first occurrence)
pos = items.index('b', 2)  # 3 (start search at index 2)

# count() - Count occurrences
count = items.count('b')  # 2
```

**Safe Finding:**
```python
# Avoid ValueError
if 'x' in items:
    pos = items.index('x')
else:
    pos = -1

# Or use try-except
try:
    pos = items.index('x')
except ValueError:
    pos = -1
```

---

### Copying Lists

```python
original = [1, 2, 3]

# Create independent copy
copy = original.copy()
copy.append(4)
# original: [1, 2, 3]
# copy: [1, 2, 3, 4]

# Alternative methods
copy1 = original[:]
copy2 = list(original)
```

**Shallow vs Deep:**
```python
# Shallow - nested objects shared
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0][0] = 999
# original: [[999, 2], [3, 4]] - affected!

# Deep - fully independent
import copy
deep = copy.deepcopy(original)
deep[0][0] = 999
# original: [[1, 2], [3, 4]] - unchanged
```

---

### Return Values

**Important: Most methods return None**

```python
# These modify in-place, return None
numbers = [3, 1, 2]
result = numbers.sort()
# result is None
# numbers is [1, 2, 3]

# DON'T DO THIS
numbers = numbers.sort()  # numbers becomes None!

# pop() is exception - returns removed value
numbers = [1, 2, 3]
last = numbers.pop()  # last is 3, numbers is [1, 2]
```

**Built-in Functions Return New Lists:**
```python
# sorted() - returns new sorted list
original = [3, 1, 2]
sorted_list = sorted(original)
# original: [3, 1, 2] - unchanged
# sorted_list: [1, 2, 3]

# reversed() - returns iterator
original = [1, 2, 3]
rev_iter = reversed(original)
rev_list = list(rev_iter)  # [3, 2, 1]
```

---

### Quick Reference

```python
lst = [1, 2, 3]

# Add
lst.append(4)        # Add to end
lst.extend([5, 6])   # Add multiple
lst.insert(0, 0)     # Insert at position

# Remove
lst.remove(2)        # Remove by value
val = lst.pop()      # Remove and return last
val = lst.pop(0)     # Remove and return at index
lst.clear()          # Remove all

# Organize
lst.sort()           # Sort ascending
lst.sort(reverse=True)  # Sort descending
lst.reverse()        # Reverse order

# Search
idx = lst.index(3)   # Find position
cnt = lst.count(2)   # Count occurrences

# Copy
cp = lst.copy()      # Shallow copy
```

**Remember:**
- Methods modify in-place
- Most return None (except pop)
- Check existence before remove/index
- Use copy() to preserve original
