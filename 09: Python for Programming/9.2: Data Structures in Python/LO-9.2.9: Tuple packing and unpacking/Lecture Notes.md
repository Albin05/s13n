## Lecture Notes: Tuple Packing and Unpacking

**Duration:** 12 minutes

---

### Tuple Packing

**Definition:** Automatically creating a tuple from comma-separated values.

```python
# Explicit (with parentheses)
point = (10, 20)

# Implicit (comma creates tuple)
point = 10, 20

# Both create the same tuple
print(point)  # (10, 20)
```

**Key Point:** The comma creates the tuple, not the parentheses!

**Function Returns:**
```python
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

result = get_stats([10, 20, 30])  # Returns tuple
print(result)  # (10, 30, 20.0)
```

---

### Basic Unpacking

**Definition:** Extracting tuple elements into separate variables.

```python
# Unpack into variables
point = (10, 20)
x, y = point

print(x)  # 10
print(y)  # 20
```

**Rule:** Number of variables must match number of elements!

```python
coords = (10, 20, 30)

# Correct
x, y, z = coords  # ✓

# Wrong
# x, y = coords  # ✗ ValueError: too many values to unpack
```

**Unpacking Returns:**
```python
def get_user():
    return 'Alice', 25, 'NYC'

name, age, city = get_user()
```

**Ignoring Values:**
```python
# Use _ for ignored values
name, _, city = ('Alice', 25, 'NYC')
print(f"{name} from {city}")  # Alice from NYC
```

---

### Extended Unpacking with *

**Collect Remaining Elements:**

```python
numbers = (1, 2, 3, 4, 5)

# * at end
first, *rest = numbers
# first = 1, rest = [2, 3, 4, 5]

# * in middle
first, *middle, last = numbers
# first = 1, middle = [2, 3, 4], last = 5

# * at beginning
*beginning, last = numbers
# beginning = [1, 2, 3, 4], last = 5
```

**Important:** The `*` creates a **list**, not a tuple!

**Selective Extraction:**
```python
data = (10, 20, 30, 40, 50)

# Get first and last, ignore middle
first, *_, last = data
# first = 10, last = 50
```

**Rules:**
- Only ONE `*` per unpacking
- Result is always a list
- Can be empty: `first, *rest = (1,)` → `rest = []`

---

### Variable Swapping

**Traditional Way:**
```python
# Need temporary variable
temp = a
a = b
b = temp
```

**Python Way:**
```python
# One line!
a, b = b, a
```

**How It Works:**
1. Right side evaluated first: `(b, a)` creates tuple
2. Then unpacked to left: `a, b = tuple`

**Rotation:**
```python
x, y, z = 1, 2, 3
x, y, z = y, z, x
# x=2, y=3, z=1
```

---

### Unpacking in Functions

**Unpacking Arguments:**
```python
def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

point1 = (0, 0)
point2 = (3, 4)

# Unpack with *
result = distance(*point1, *point2)
# Same as: distance(0, 0, 3, 4)
```

**Dictionary Unpacking:**
```python
def create_user(name, age, city):
    return f"{name}, {age}, {city}"

data = {'name': 'Alice', 'age': 25, 'city': 'NYC'}
result = create_user(**data)
```

---

### Unpacking in Loops

**Tuples in Loops:**
```python
points = [(0, 0), (3, 4), (6, 8)]

for x, y in points:
    print(f"({x}, {y})")
```

**With enumerate:**
```python
names = ['Alice', 'Bob', 'Charlie']

for index, name in enumerate(names):
    print(f"{index}: {name}")
```

**With zip:**
```python
names = ['Alice', 'Bob']
ages = [25, 30]

for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

**Dictionary Items:**
```python
scores = {'Alice': 95, 'Bob': 88}

for name, score in scores.items():
    print(f"{name}: {score}")
```

**Extended Unpacking in Loops:**
```python
data = [(1, 2, 3, 4), (10, 20, 30), (100, 200)]

for first, *rest in data:
    print(f"First: {first}, Rest: {rest}")
# First: 1, Rest: [2, 3, 4]
# First: 10, Rest: [20, 30]
# First: 100, Rest: [200]
```

---

### Practical Patterns

**Pattern 1: Multiple Returns**
```python
def analyze(data):
    return min(data), max(data), sum(data)/len(data)

minimum, maximum, average = analyze([10, 20, 30])
```

**Pattern 2: Coordinate Operations**
```python
def translate(point, dx, dy):
    x, y = point
    return x + dx, y + dy

new_point = translate((10, 20), 5, -5)
```

**Pattern 3: Parsing Strings**
```python
csv = "Alice,25,NYC"
name, age, city = csv.split(',')
```

**Pattern 4: Data Processing**
```python
students = [
    ('Alice', 85, 90, 88),
    ('Bob', 78, 82, 75)
]

for name, *scores in students:
    avg = sum(scores) / len(scores)
    print(f"{name}: {avg:.2f}")
```

**Pattern 5: State Updates**
```python
# Fibonacci generator
a, b = 0, 1
while a < 100:
    print(a)
    a, b = b, a + b  # Elegant update
```

---

### Common Pitfalls

**Pitfall 1: Mismatched Count**
```python
# Wrong
data = (1, 2, 3)
# a, b = data  # ValueError

# Right
a, b, c = data
# or
a, *rest = data
```

**Pitfall 2: Single-Element Tuple**
```python
# Wrong
single = (5)     # This is int 5!

# Right
single = (5,)    # Need trailing comma
```

**Pitfall 3: Forgetting * Creates List**
```python
first, *rest = (1, 2, 3)
print(type(rest))  # <class 'list'> not tuple!
```

**Pitfall 4: Multiple * Operators**
```python
# Invalid
# *a, *b = (1, 2, 3)  # SyntaxError
```

---

### Quick Reference

**Packing:**
```python
coords = 10, 20              # Implicit
return x, y, z               # Function return
```

**Basic Unpacking:**
```python
x, y = point                 # Must match count
name, _, city = data         # Ignore with _
```

**Extended Unpacking:**
```python
first, *rest = data          # Collect rest
first, *middle, last = data  # Collect middle
*beginning, last = data      # Collect beginning
```

**Swapping:**
```python
a, b = b, a                  # Swap
x, y, z = y, z, x            # Rotate
```

**Loop Unpacking:**
```python
for x, y in points:          # Tuples
for i, v in enumerate(lst):  # enumerate
for k, v in dict.items():    # Dictionary
```

---

### Key Takeaways

**Packing:**
- Comma creates tuple, not parentheses
- Multiple return values automatically packed
- Natural and Pythonic syntax

**Unpacking:**
- Extract tuple elements to variables
- Number must match (without *)
- Use _ to ignore values

**Extended Unpacking:**
- Use * to collect remaining items
- Creates a list, not tuple
- Only one * per statement
- Very flexible

**Swapping:**
- One-line variable swap
- No temporary variable needed
- Works with rotation too

**Benefits:**
- ✓ Cleaner code
- ✓ More readable
- ✓ Pythonic patterns
- ✓ Multiple return values
- ✓ Elegant transformations

**Use Cases:**
- Function returns
- Data parsing
- Coordinate operations
- State updates
- Loop iterations
- Algorithm implementations

**Master packing and unpacking for more elegant Python code!**
