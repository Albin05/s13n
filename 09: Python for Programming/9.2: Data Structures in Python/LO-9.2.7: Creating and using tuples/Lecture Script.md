## Lecture Script: Creating and Using Tuples

**Duration:** 18 minutes

---

### Hook (2 minutes)

"You're building a function that needs to return both a user's name and their age. Or maybe you want to store coordinates that should never change. Or perhaps you need to use data as dictionary keys. Lists can't do all of this - but tuples can!

Tuples are Python's immutable sequences. Think of them as 'locked' lists - once created, they can't be modified. This isn't a limitation, it's a feature! Immutability brings safety, performance, and enables use cases that lists simply can't handle.

Today, we'll master tuples - from basic creation to advanced patterns. You'll learn when to choose tuples over lists, how to use them for multiple return values, and why immutability is actually a powerful tool in your Python toolkit. Let's unlock the power of tuples!"

---

### Section 1: Creating Tuples (3 minutes)

**Basic Tuple Creation:**

```python
# Empty tuple
empty = ()
print(empty)  # ()
print(type(empty))  # <class 'tuple'>

# Tuple with values
coordinates = (3, 4)
print(coordinates)  # (3, 4)

# Mixed types
person = ('Alice', 25, 'Engineer')
print(person)  # ('Alice', 25, 'Engineer')

# Nested tuples
matrix = ((1, 2), (3, 4), (5, 6))
print(matrix)  # ((1, 2), (3, 4), (5, 6))
```

**Parentheses Are Optional (Usually):**

```python
# Without parentheses - still creates tuple
point = 3, 4
print(point)  # (3, 4)
print(type(point))  # <class 'tuple'>

# Multiple assignment
x, y, z = 1, 2, 3  # Actually tuple packing/unpacking
print(x, y, z)  # 1 2 3

# Function return - implicit tuple
def get_coords():
    return 10, 20  # Returns tuple

coords = get_coords()
print(coords)  # (10, 20)
```

**Single-Element Tuples (Tricky!):**

```python
# WRONG - This is NOT a tuple
not_a_tuple = (5)
print(type(not_a_tuple))  # <class 'int'>

# RIGHT - Need trailing comma
single = (5,)
print(type(single))  # <class 'tuple'>
print(single)  # (5,)

# Also works without parentheses
also_single = 5,
print(type(also_single))  # <class 'tuple'>
print(also_single)  # (5,)
```

**Using tuple() Constructor:**

```python
# From list
numbers = tuple([1, 2, 3, 4, 5])
print(numbers)  # (1, 2, 3, 4, 5)

# From string (each character becomes element)
letters = tuple('hello')
print(letters)  # ('h', 'e', 'l', 'l', 'o')

# From range
nums = tuple(range(5))
print(nums)  # (0, 1, 2, 3, 4)

# From another tuple (creates copy)
original = (1, 2, 3)
copy = tuple(original)
print(copy)  # (1, 2, 3)
```

---

### Section 2: Accessing Tuple Elements (3 minutes)

**Indexing - Same as Lists:**

```python
fruits = ('apple', 'banana', 'orange', 'mango')

# Positive indexing
print(fruits[0])   # apple
print(fruits[2])   # orange

# Negative indexing
print(fruits[-1])  # mango
print(fruits[-2])  # orange

# IndexError if out of range
try:
    print(fruits[10])
except IndexError as e:
    print(f"Error: {e}")  # tuple index out of range
```

**Slicing - Also Same as Lists:**

```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Basic slicing
print(numbers[2:5])    # (2, 3, 4)
print(numbers[:3])     # (0, 1, 2)
print(numbers[7:])     # (7, 8, 9)
print(numbers[:])      # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# With step
print(numbers[::2])    # (0, 2, 4, 6, 8)
print(numbers[1::2])   # (1, 3, 5, 7, 9)
print(numbers[::-1])   # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

# Negative indices in slices
print(numbers[-3:])    # (7, 8, 9)
print(numbers[:-3])    # (0, 1, 2, 3, 4, 5, 6)
```

**Nested Tuple Access:**

```python
# Matrix
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# Access row
print(matrix[0])     # (1, 2, 3)
print(matrix[1])     # (4, 5, 6)

# Access element
print(matrix[0][0])  # 1
print(matrix[1][2])  # 6
print(matrix[2][1])  # 8

# Slice of slice
print(matrix[0][1:])  # (2, 3)
```

---

### Section 3: Tuple Immutability (3 minutes)

**Cannot Modify Elements:**

```python
colors = ('red', 'green', 'blue')

# Cannot change
try:
    colors[0] = 'yellow'
except TypeError as e:
    print(f"Error: {e}")  
    # 'tuple' object does not support item assignment

# Cannot delete
try:
    del colors[1]
except TypeError as e:
    print(f"Error: {e}")  
    # 'tuple' object doesn't support item deletion
```

**Cannot Add or Remove:**

```python
numbers = (1, 2, 3)

# No append()
# numbers.append(4)  # AttributeError

# No extend()
# numbers.extend([4, 5])  # AttributeError

# No remove()
# numbers.remove(2)  # AttributeError

# No pop()
# numbers.pop()  # AttributeError
```

**But Can Create New Tuples:**

```python
# Concatenation creates new tuple
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(combined)  # (1, 2, 3, 4, 5, 6)
print(tuple1)    # (1, 2, 3) - unchanged

# Repetition creates new tuple
repeated = (1, 2) * 3
print(repeated)  # (1, 2, 1, 2, 1, 2)

# Slicing creates new tuple
numbers = (0, 1, 2, 3, 4)
subset = numbers[1:4]
print(subset)  # (1, 2, 3)
```

**Mutable Objects Inside Tuples:**

```python
# Tuple with mutable list inside
data = (1, 2, [3, 4])

# Cannot reassign tuple element
try:
    data[2] = [5, 6]  # TypeError
except TypeError as e:
    print(f"Error: {e}")

# BUT can modify the mutable object itself!
data[2].append(5)
print(data)  # (1, 2, [3, 4, 5])

# The tuple still references same list
# Only the list's contents changed
```

---

### Section 4: Tuple Methods and Operations (2 minutes)

**Only Two Methods:**

```python
numbers = (1, 2, 3, 2, 4, 2, 5)

# count() - count occurrences
count_2 = numbers.count(2)
print(count_2)  # 3

# index() - find first occurrence
pos = numbers.index(3)
print(pos)  # 2

# index() with start
pos = numbers.index(2, 2)  # Start searching from index 2
print(pos)  # 3 (finds second occurrence of 2)

# ValueError if not found
try:
    numbers.index(10)
except ValueError as e:
    print(f"Error: {e}")  # tuple.index(x): x not in tuple
```

**Common Operations:**

```python
numbers = (1, 2, 3, 4, 5)

# Length
print(len(numbers))  # 5

# Membership testing
print(3 in numbers)     # True
print(10 in numbers)    # False
print(6 not in numbers) # True

# Iteration
for num in numbers:
    print(num, end=' ')  # 1 2 3 4 5
print()

# Min, max, sum
print(min(numbers))  # 1
print(max(numbers))  # 5
print(sum(numbers))  # 15
```

---

### Section 5: Multiple Return Values (3 minutes)

**Functions Returning Tuples:**

```python
def get_user_info():
    name = "Alice"
    age = 25
    city = "NYC"
    return name, age, city  # Returns tuple

# Get as tuple
user = get_user_info()
print(user)  # ('Alice', 25, 'NYC')
print(type(user))  # <class 'tuple'>

# Unpack directly
name, age, city = get_user_info()
print(f"{name} is {age} years old and lives in {city}")
# Alice is 25 years old and lives in NYC
```

**Practical Examples:**

```python
def divide_with_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_with_remainder(17, 5)
print(f"17 ÷ 5 = {q} remainder {r}")  # 17 ÷ 5 = 3 remainder 2

# Statistics function
def calculate_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

minimum, maximum, average = calculate_stats([10, 20, 30, 40, 50])
print(f"Min: {minimum}, Max: {maximum}, Avg: {average}")
# Min: 10, Max: 50, Avg: 30.0

# Coordinate transformation
def translate_point(x, y, dx, dy):
    return x + dx, y + dy

new_x, new_y = translate_point(10, 20, 5, -3)
print(f"New coordinates: ({new_x}, {new_y})")  # (15, 17)
```

---

### Section 6: When to Use Tuples (2 minutes)

**Use Tuples When:**

```python
# 1. Data shouldn't change
DAYS_OF_WEEK = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
RGB_RED = (255, 0, 0)
ORIGIN = (0, 0)

# 2. As dictionary keys (must be hashable)
locations = {}
locations[(0, 0)] = "Origin"
locations[(10, 20)] = "Point A"
locations[(-5, 15)] = "Point B"

print(locations[(10, 20)])  # Point A

# Lists can't be dict keys!
# locations[[1, 2]] = "Test"  # TypeError: unhashable type: 'list'

# 3. Returning multiple values
def get_dimensions():
    return 1920, 1080

width, height = get_dimensions()

# 4. Fixed structure data
person = ('Alice', 25, 'Engineer')  # name, age, occupation
coordinate = (40.7128, -74.0060)    # latitude, longitude
rgb = (255, 128, 0)                 # red, green, blue
```

**Lists vs Tuples:**

```python
# Use LIST when:
# - Data will change
# - Adding/removing elements
# - Order might change
shopping_cart = ['milk', 'bread']  # Will add/remove items
shopping_cart.append('eggs')

# Use TUPLE when:
# - Data is fixed
# - Represents a record/structure
# - Using as dict key
# - Performance matters (tuples are faster)
coordinates = (lat, lon)  # Won't change
person_record = (name, age, city)  # Fixed structure
```

---

### Section 7: Tuple Unpacking Basics (2 minutes)

**Simple Unpacking:**

```python
# Basic unpacking
point = (3, 4)
x, y = point
print(f"x={x}, y={y}")  # x=3, y=4

# Direct unpacking
name, age = ('Alice', 25)
print(f"{name} is {age}")  # Alice is 25

# Multiple variables
r, g, b = (255, 128, 0)
print(f"RGB: ({r}, {g}, {b})")  # RGB: (255, 128, 0)
```

**Swapping Values:**

```python
# Traditional way (need temp variable)
a = 5
b = 10
temp = a
a = b
b = temp

# Python way (using tuple unpacking)
a = 5
b = 10
a, b = b, a  # Swap in one line!
print(a, b)  # 10 5

# Works with multiple values
x, y, z = 1, 2, 3
x, y, z = z, x, y  # Rotate
print(x, y, z)  # 3 1 2
```

**In Loops:**

```python
# List of tuples
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

for name, score in students:
    print(f"{name}: {score}")
# Alice: 85
# Bob: 92
# Charlie: 78

# Enumerate returns tuples
fruits = ['apple', 'banana', 'orange']
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: orange
```

---

### Summary (1 minute)

Tuples are immutable sequences in Python:

**Creation:**
- `()` - empty tuple
- `(1, 2, 3)` - with values
- `(5,)` - single element (needs comma!)
- `tuple([1, 2, 3])` - from iterable

**Key Characteristics:**
- **Immutable** - Cannot change after creation
- **Ordered** - Elements maintain position
- **Hashable** - Can be dict keys
- **Faster** than lists
- Only 2 methods: `count()` and `index()`

**Common Uses:**
- Fixed data (coordinates, RGB colors)
- Multiple return values from functions
- Dictionary keys
- Data that shouldn't change
- Better performance than lists

**Access:**
- Indexing: `tuple[0]`, `tuple[-1]`
- Slicing: `tuple[1:3]`, `tuple[::2]`
- Unpacking: `x, y = (3, 4)`

**Remember:**
- Immutable = safer and faster
- Perfect for fixed structures
- Use lists when data changes, tuples when it doesn't

Tuples bring structure and safety to your Python code!
