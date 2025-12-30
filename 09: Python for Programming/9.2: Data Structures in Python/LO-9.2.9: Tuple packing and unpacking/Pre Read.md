## Pre-Read: Tuple Packing and Unpacking

**Duration:** 5 minutes

---

### What You'll Learn

Tuple packing and unpacking is Python's elegant way to work with multiple values simultaneously. It's one of Python's most powerful features that makes code cleaner and more readable.

---

### The Magic of Multiple Assignment

**Normal way:**
```python
x = 10
y = 20
```

**Python's way:**
```python
x, y = 10, 20  # Assign both at once!
```

This simple feature powers many elegant patterns in Python.

---

### Packing: Creating Tuples

**Packing** means Python automatically creates a tuple from comma-separated values.

```python
# These are the same:
coords = (10, 20, 30)  # Explicit tuple
coords = 10, 20, 30    # Implicit packing

# Both create: (10, 20, 30)
```

**Key insight:** The **comma** creates the tuple, not the parentheses!

**Why it matters:**
```python
# Return multiple values from function
def get_dimensions():
    return 100, 50  # Automatically packed into tuple

width, height = get_dimensions()  # Unpacked!
```

---

### Unpacking: Extracting Values

**Unpacking** extracts tuple elements into separate variables.

```python
point = (10, 20)

# Extract into variables
x, y = point

print(x)  # 10
print(y)  # 20
```

**Real-world example:**
```python
def get_user_info():
    return 'Alice', 25, 'NYC'

# Unpack all at once
name, age, city = get_user_info()
print(f"{name} is {age} years old")
```

---

### Variable Swapping

**Traditional approach (most languages):**
```python
temp = a
a = b
b = temp
```

**Python's elegant way:**
```python
a, b = b, a  # One line!
```

**How?** The right side `(b, a)` is packed into a tuple first, then unpacked to `a, b`.

---

### Extended Unpacking with *

What if you don't know how many elements there are?

```python
scores = (95, 88, 92, 78, 85)

# Get first, collect the rest
first, *rest = scores

print(first)  # 95
print(rest)   # [88, 92, 78, 85]
```

The `*` operator collects remaining elements into a list!

**Different positions:**
```python
# First and rest
first, *rest = (1, 2, 3, 4)
# first=1, rest=[2,3,4]

# First, middle, last
first, *middle, last = (1, 2, 3, 4)
# first=1, middle=[2,3], last=4

# Beginning and last
*beginning, last = (1, 2, 3, 4)
# beginning=[1,2,3], last=4
```

---

### Unpacking in Loops

Makes iteration over complex data super clean:

```python
# List of coordinate pairs
points = [(0, 0), (3, 4), (6, 8)]

# Unpack each pair directly
for x, y in points:
    print(f"Point at ({x}, {y})")
```

**Without unpacking (tedious):**
```python
for point in points:
    x = point[0]
    y = point[1]
    print(f"Point at ({x}, {y})")
```

---

### Common Patterns

**Pattern 1: Ignoring values**
```python
# Use _ for values you don't need
name, _, city = ('Alice', 25, 'NYC')
print(f"{name} from {city}")
# Age is ignored
```

**Pattern 2: Function arguments**
```python
def calculate(x, y):
    return x + y, x - y, x * y

# Unpack all results
sum_val, diff_val, prod_val = calculate(10, 5)
```

**Pattern 3: Parsing data**
```python
# CSV data
csv_row = "Alice,25,NYC"
name, age, city = csv_row.split(',')
```

---

### Try to Predict

```python
# Question 1
a, b = 10, 20
a, b = b, a
# What are a and b now?

# Question 2
data = (1, 2, 3, 4, 5)
first, *middle, last = data
# What is middle?

# Question 3
def mystery():
    return 5, 10, 15

result = mystery()
# What type is result?
```

**Answers:**
1. `a = 20, b = 10` (swapped!)
2. `middle = [2, 3, 4]` (a list!)
3. `tuple` (multiple returns are packed)

---

### Why This Matters

**Cleaner Code:**
```python
# Before
def get_stats(numbers):
    stats = {}
    stats['min'] = min(numbers)
    stats['max'] = max(numbers)
    stats['avg'] = sum(numbers)/len(numbers)
    return stats

result = get_stats([10, 20, 30])
minimum = result['min']
maximum = result['max']

# After
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

minimum, maximum, average = get_stats([10, 20, 30])
```

**More Pythonic:**
- Less code
- More readable
- Easier to understand
- Industry standard

---

### What to Remember

1. **Packing:** Comma creates tuple
   - `coords = 10, 20` → `(10, 20)`

2. **Unpacking:** Extract to variables
   - `x, y = coords` → `x=10, y=20`

3. **Extended unpacking:** Use `*` to collect
   - `first, *rest = data`

4. **Swapping:** One line elegance
   - `a, b = b, a`

5. **Loop unpacking:** Clean iteration
   - `for x, y in points:`

---

### Quick Exercise

Before the lesson, try this:

```python
# Create a tuple with your name, age, and city
info = "YourName", YourAge, "YourCity"

# Unpack it
name, age, city = info

# Print each
print(name)
print(age)
print(city)

# Try swapping age and city
age, city = city, age
print(f"After swap: age={age}, city={city}")
```

Notice how natural and Pythonic it feels!

---

### Get Ready!

In the lesson, you'll learn:
- Deep dive into packing and unpacking mechanics
- Extended unpacking with `*` operator in detail
- Unpacking in function parameters and returns
- Nested unpacking
- Real-world applications
- Common patterns and best practices

**Packing and unpacking is everywhere in Python code. Master it, and your code becomes more elegant and Pythonic!**
