## Pre-Read: Modifying Lists Using Built-in Methods

## What Are List Methods?

List methods are **superpowers built into every list** - like apps pre-installed on your phone! Instead of writing loops and complex code, just call a method.

### Simple Analogy

Think of list methods like **voice commands to a smart home**:
- **Your list**: The smart home
- **Methods**: "Turn on lights" (append), "Rearrange furniture" (sort), "Remove item" (pop)
- **Self-operating**: Home knows how to do these things itself
- **Just say the word**: my_list.sort() - done!

Or like **a playlist's controls**:
- **Playlist**: Your list
- **Methods**: Add song, remove song, shuffle, sort by artist
- **Built-in**: All features ready to use
- **One button**: playlist.shuffle() - instant!

### Important: In-Place vs Return

**Biggest gotcha** - most methods change the list but return **None**:
```python
numbers = [3, 1, 2]
result = numbers.sort()  # numbers is [1, 2, 3], but...
print(result)  # None!

# DON'T DO THIS:
numbers = numbers.sort()  # Now numbers is None! Lost your data!
```

**Why?** Efficiency - don't wastefully create copies when you want to modify the original!

### What You'll Learn

Python lists have powerful built-in methods that let you add, remove, sort, and search elements efficiently.

### Why It Matters

Without list methods:
- Need complex loops for simple operations
- More code, more bugs
- Slower and harder to read

With list methods:
- One-line operations
- Fast and optimized
- Clean, readable code

### Adding Elements

**append() - Add to End:**
```python
cart = []
cart.append("apple")
cart.append("banana")
print(cart)  # ['apple', 'banana']
```

**extend() - Add Multiple:**
```python
cart = ['apple']
cart.extend(['banana', 'orange'])
print(cart)  # ['apple', 'banana', 'orange']
```

**insert() - Add at Position:**
```python
fruits = ['apple', 'orange']
fruits.insert(1, 'banana')
print(fruits)  # ['apple', 'banana', 'orange']
```

### Removing Elements

**remove() - Remove by Value:**
```python
items = [1, 2, 3, 2]
items.remove(2)  # Removes first 2
print(items)     # [1, 3, 2]
```

**pop() - Remove and Return:**
```python
numbers = [1, 2, 3, 4]
last = numbers.pop()     # Returns 4
print(numbers)           # [1, 2, 3]

first = numbers.pop(0)   # Returns 1
print(numbers)           # [2, 3]
```

### Organizing Lists

**sort() - Sort in Place:**
```python
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # [1, 2, 3, 4]

# Reverse order
numbers.sort(reverse=True)
print(numbers)  # [4, 3, 2, 1]
```

**reverse() - Reverse Order:**
```python
items = [1, 2, 3, 4]
items.reverse()
print(items)  # [4, 3, 2, 1]
```

### Finding Elements

**index() - Find Position:**
```python
fruits = ['apple', 'banana', 'orange']
pos = fruits.index('banana')
print(pos)  # 1
```

**count() - Count Occurrences:**
```python
numbers = [1, 2, 2, 3, 2]
count = numbers.count(2)
print(count)  # 3
```

### Important Note

Most list methods modify the list **in-place** and return **None**:

```python
numbers = [3, 1, 2]
result = numbers.sort()

print(result)   # None
print(numbers)  # [1, 2, 3] - list is sorted

# DON'T DO THIS:
numbers = numbers.sort()  # numbers becomes None!
```

### Try to Predict

```python
lst = []
lst.append(1)
lst.append(2)
lst.extend([3, 4])
lst.insert(0, 0)
lst.remove(2)
x = lst.pop()

# What is lst?
# What is x?
```

Answers:
- lst: `[0, 1, 3]`
- x: `4`

List methods are your toolkit for list manipulation!
