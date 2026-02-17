## Lecture Script: Tuple Packing and Unpacking


---

### CS Theory Bite

> **Origin**: Tuple packing/unpacking implements **destructuring** — extracting multiple values in one statement. Python 3 added **starred unpacking** (`a, *rest = tuple`) for flexible extraction.
>
> **Analogy**: Unpacking is like **opening a gift box with multiple items** — one action, multiple things extracted and assigned to variables.
>
> **Why it matters**: Tuple unpacking enables elegant patterns: multiple return values, variable swapping (`a, b = b, a`), and loop destructuring.



### Hook (2 minutes)

**Scenario:**

Imagine you're writing a function that needs to return a user's name, age, and city. In many languages, you'd need to create a class or structure. In Python, you can simply do this:

```python
def get_user():
    return 'Alice', 25, 'NYC'

name, age, city = get_user()
print(f"{name} is {age} years old and lives in {city}")
```

**The Magic:**

Without thinking about it, you just used two powerful Python features:
- **Packing:** The function automatically packed three values into a tuple
- **Unpacking:** You extracted those values into separate variables in one line

**What seems simple is actually one of Python's most elegant features!**

Want to swap two variables? In most languages, you need a temporary variable:
```python
# Traditional way
temp = a
a = b
b = temp
```

In Python:
```python
# Pythonic way
a, b = b, a
```

**Today's Journey:**

Learn how tuple packing and unpacking make your code cleaner, more readable, and more Pythonic. This feature powers everything from multiple return values to elegant variable swapping.

---

### Section 1: Understanding Tuple Packing (3 minutes)

**What is Packing?**

Packing is when Python automatically creates a tuple from multiple values separated by commas.

```python
# Explicit tuple creation
coords = (10, 20)

# Implicit packing (no parentheses needed)
coords = 10, 20

# Both create the same tuple
print(coords)  # (10, 20)
print(type(coords))  # <class 'tuple'>
```

**The comma creates the tuple, not the parentheses!**

**Multiple Values:**

```python
# Pack multiple values
person = 'Alice', 25, 'Engineer', 'NYC'
print(person)  # ('Alice', 25, 'Engineer', 'NYC')

# Even works with expressions
data = 5 * 2, 3 + 4, len('hello')
print(data)  # (10, 7, 5)
```

**Return Multiple Values:**

```python
def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return total, count, average  # Packed into tuple

# Function returns a tuple
result = calculate_stats([10, 20, 30])
print(result)  # (60, 3, 20.0)
```

**Why Packing Matters:**

1. **Clean Function Returns:** Return multiple values without creating classes
2. **Natural Syntax:** Comma-separated values automatically become tuples
3. **Immutable Groups:** Create fixed collections effortlessly

---

### Section 2: Basic Tuple Unpacking (3 minutes)

**What is Unpacking?**

Unpacking extracts tuple elements into separate variables in a single assignment.

```python
# Create a tuple
point = (10, 20)

# Unpack into variables
x, y = point

print(f"x = {x}")  # x = 10
print(f"y = {y}")  # y = 20
```

**The Number Must Match:**

```python
coords = (10, 20, 30)

# Correct: 3 variables for 3 values
x, y, z = coords  # Works!

# Wrong: Too few variables
# x, y = coords  # ValueError: too many values to unpack

# Wrong: Too many variables
# x, y, z, w = coords  # ValueError: not enough values to unpack
```

**Unpacking Function Returns:**

```python
def get_user_info():
    return 'Alice', 25, 'NYC'

# Unpack directly
name, age, city = get_user_info()

print(f"{name}, {age}, {city}")  # Alice, 25, NYC
```

**Unpacking from Lists:**

```python
# Works with any sequence, not just tuples
colors = ['red', 'green', 'blue']
primary1, primary2, primary3 = colors

print(primary1)  # red
```

**Ignoring Values:**

```python
# Use _ for values you don't need
name, _, city = ('Alice', 25, 'NYC')
print(f"{name} from {city}")  # Alice from NYC
# age is ignored
```

**Nested Unpacking:**

```python
# Unpack nested structures
person = ('Alice', (25, 'Engineer'))

name, (age, job) = person
print(f"{name}, {age}, {job}")  # Alice, 25, Engineer
```

---

### Section 3: Extended Unpacking with * Operator (4 minutes)

**The Problem:**

What if you want the first few elements and collect the rest?

```python
scores = (95, 88, 92, 78, 85, 90)

# Without extended unpacking - tedious
first = scores[0]
second = scores[1]
rest = scores[2:]
```

**The Solution: * Operator:**

The `*` operator collects remaining elements into a list.

```python
scores = (95, 88, 92, 78, 85, 90)

# Collect rest
first, second, *rest = scores

print(first)   # 95
print(second)  # 88
print(rest)    # [92, 78, 85, 90] - note: list, not tuple!
```

**Different Positions:**

```python
numbers = (1, 2, 3, 4, 5)

# * at the end
first, *rest = numbers
print(first)  # 1
print(rest)   # [2, 3, 4, 5]

# * in the middle
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

# * at the beginning
*beginning, last = numbers
print(beginning)  # [1, 2, 3, 4]
print(last)       # 5
```

**Practical Examples:**

```python
# Process first item, collect rest
def process_items(items):
    if not items:
        return
    
    first, *rest = items
    print(f"Processing: {first}")
    print(f"Remaining: {rest}")

process_items([10, 20, 30, 40])
# Processing: 10
# Remaining: [20, 30, 40]
```

**Split head and tail:**

```python
# Get first and last, ignore middle
data = (100, 200, 300, 400, 500)
first, *_, last = data

print(f"First: {first}, Last: {last}")
# First: 100, Last: 500
# Middle values ignored with *_
```

**Important Notes:**

1. **Only one * per unpacking:**
```python
# Invalid
# *a, *b = (1, 2, 3)  # SyntaxError
```

2. **Result is always a list:**
```python
a, *b = (1,)
print(b)  # [] - empty list, not tuple
```

3. **Can be empty:**
```python
first, *rest = (1,)
print(rest)  # []
```

---

### Section 4: Variable Swapping (2 minutes)

**Traditional Approach:**

```python
# Without unpacking - need temporary variable
a = 10
b = 20

temp = a
a = b
b = temp

print(f"a = {a}, b = {b}")  # a = 20, b = 10
```

**Python's Elegant Way:**

```python
a = 10
b = 20

# Swap in one line!
a, b = b, a

print(f"a = {a}, b = {b}")  # a = 20, b = 10
```

**How It Works:**

1. Right side evaluated first: `(b, a)` → `(20, 10)` tuple
2. Then unpacked to left side: `a, b = (20, 10)`

**Multiple Variable Rotation:**

```python
# Rotate three variables
x, y, z = 1, 2, 3
x, y, z = y, z, x

print(x, y, z)  # 2 3 1
```

**Practical Example - Bubble Sort:**

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Pythonic swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

numbers = [64, 34, 25, 12, 22]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)  # [12, 22, 25, 34, 64]
```

**Conditional Swap:**

```python
a, b = 5, 10

# Ensure a is always smaller
if a > b:
    a, b = b, a

print(f"a = {a}, b = {b}")  # a = 5, b = 10
```

---

### Section 5: Unpacking in Function Parameters (2 minutes)

**Unpacking Arguments:**

```python
def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

# Have coordinates as tuples
point1 = (0, 0)
point2 = (3, 4)

# Unpack using *
distance = calculate_distance(*point1, *point2)
print(distance)  # 5.0
```

**Dictionary Unpacking:**

```python
def create_user(name, age, city):
    return f"{name}, {age}, from {city}"

# Unpack dictionary with **
user_data = {'name': 'Alice', 'age': 25, 'city': 'NYC'}
result = create_user(**user_data)
print(result)  # Alice, 25, from NYC
```

**Combining Both:**

```python
def send_email(to, subject, body, cc=None):
    print(f"To: {to}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    if cc:
        print(f"CC: {cc}")

# Positional arguments
args = ('user@example.com', 'Hello', 'Welcome!')

# Keyword arguments
kwargs = {'cc': 'admin@example.com'}

send_email(*args, **kwargs)
```

---

### Section 6: Unpacking in Loops (2 minutes)

**Iterating Over Tuples:**

```python
# List of coordinate tuples
points = [(0, 0), (3, 4), (6, 8)]

# Unpack in loop
for x, y in points:
    print(f"Point: ({x}, {y})")

# Output:
# Point: (0, 0)
# Point: (3, 4)
# Point: (6, 8)
```

**With enumerate():**

```python
names = ['Alice', 'Bob', 'Charlie']

# Unpack index and value
for index, name in enumerate(names):
    print(f"{index}: {name}")

# Output:
# 0: Alice
# 1: Bob
# 2: Charlie
```

**With zip():**

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['NYC', 'LA', 'Chicago']

# Unpack multiple iterables
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, {city}")

# Output:
# Alice, 25, NYC
# Bob, 30, LA
# Charlie, 35, Chicago
```

**Dictionary Items:**

```python
user_scores = {'Alice': 95, 'Bob': 88, 'Charlie': 92}

# Unpack key-value pairs
for name, score in user_scores.items():
    print(f"{name}: {score}")

# Output:
# Alice: 95
# Bob: 88
# Charlie: 92
```

**Extended Unpacking in Loops:**

```python
# Process first element differently
data = [
    (1, 2, 3, 4, 5),
    (10, 20, 30),
    (100, 200, 300, 400)
]

for first, *rest in data:
    print(f"First: {first}, Rest: {rest}")

# Output:
# First: 1, Rest: [2, 3, 4, 5]
# First: 10, Rest: [20, 30]
# First: 100, Rest: [200, 300, 400]
```

---

### Section 7: Practical Applications (3 minutes)

**Application 1: Parsing CSV Data**

```python
# CSV row as string
csv_row = "Alice,25,Engineer,NYC,95000"

# Unpack and convert
name, age, job, city, salary = csv_row.split(',')
age = int(age)
salary = int(salary)

print(f"{name} - {job} in {city}, ${salary}")
# Alice - Engineer in NYC, $95000
```

**Application 2: Statistics Functions**

```python
def get_statistics(numbers):
    """Return min, max, mean, median"""
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    
    minimum = sorted_nums[0]
    maximum = sorted_nums[-1]
    mean = sum(sorted_nums) / n
    
    if n % 2 == 0:
        median = (sorted_nums[n//2-1] + sorted_nums[n//2]) / 2
    else:
        median = sorted_nums[n//2]
    
    return minimum, maximum, mean, median

# Unpack all statistics
data = [23, 45, 12, 67, 34, 89, 21]
min_val, max_val, mean_val, median_val = get_statistics(data)

print(f"Min: {min_val}")
print(f"Max: {max_val}")
print(f"Mean: {mean_val:.2f}")
print(f"Median: {median_val}")
```

**Application 3: Coordinate Transformations**

```python
def translate_point(point, dx, dy):
    """Move point by dx, dy"""
    x, y = point
    return x + dx, y + dy

def scale_point(point, factor):
    """Scale point by factor"""
    x, y = point
    return x * factor, y * factor

# Chain transformations
original = (10, 20)
moved = translate_point(original, 5, -10)
scaled = scale_point(moved, 2)

print(f"Original: {original}")
print(f"Moved: {moved}")
print(f"Scaled: {scaled}")
```

**Application 4: Partitioning Data**

```python
def partition_by_threshold(numbers, threshold):
    """Split into below and above threshold"""
    below = []
    above = []
    
    for num in numbers:
        if num < threshold:
            below.append(num)
        else:
            above.append(num)
    
    return below, above

# Unpack results
scores = [45, 67, 89, 34, 92, 56, 78, 23, 95]
failing, passing = partition_by_threshold(scores, 60)

print(f"Failing: {failing}")
print(f"Passing: {passing}")
```

**Application 5: Processing Records**

```python
# Employee records: (id, name, department, salary)
employees = [
    (101, 'Alice', 'Engineering', 95000),
    (102, 'Bob', 'Marketing', 75000),
    (103, 'Charlie', 'Engineering', 105000),
    (104, 'Diana', 'HR', 65000)
]

# Filter engineers and extract names
engineer_names = []
for emp_id, name, dept, salary in employees:
    if dept == 'Engineering':
        engineer_names.append(name)

print(f"Engineers: {engineer_names}")
# Engineers: ['Alice', 'Charlie']

# Get highest paid with extended unpacking
sorted_emps = sorted(employees, key=lambda e: e[3], reverse=True)
top_earner_id, top_earner_name, *_ = sorted_emps[0]

print(f"Top earner: {top_earner_name} (ID: {top_earner_id})")
# Top earner: Charlie (ID: 103)
```

**Application 6: State Management**

```python
def fibonacci_generator():
    """Generate Fibonacci sequence"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b  # Elegant update using unpacking

# Generate first 10 Fibonacci numbers
fib = fibonacci_generator()
first_10 = [next(fib) for _ in range(10)]
print(first_10)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

### Common Pitfalls and Best Practices (1 minute)

**Pitfall 1: Forgetting Number Must Match**

```python
# Wrong
data = (1, 2, 3)
# a, b = data  # ValueError!

# Right - use extended unpacking
a, b, *rest = data  # a=1, b=2, rest=[3]
```

**Pitfall 2: Single-Element Tuple**

```python
# Wrong
single = (5)      # This is int 5
a, = single       # TypeError

# Right
single = (5,)     # Tuple with one element
a, = single       # a = 5
```

**Pitfall 3: Unpacking Strings**

```python
# Be careful - strings are iterable!
a, b, c = "Hi!"
print(a, b, c)  # H i !

# If you want the whole string
text, = ("Hello",)
print(text)  # Hello
```

**Best Practice 1: Use _ for Ignored Values**

```python
# Clear intent
name, _, _, city = ('Alice', 25, 'Engineer', 'NYC')
print(f"{name} from {city}")
```

**Best Practice 2: Extended Unpacking for Flexibility**

```python
# Handles variable-length data
first, *middle, last = range(10)
# Works for any length >= 2
```

**Best Practice 3: Unpacking in Comprehensions**

```python
points = [(1, 2), (3, 4), (5, 6)]
x_coords = [x for x, y in points]
print(x_coords)  # [1, 3, 5]
```

---

### Summary (1 minute)

**What We Learned:**

1. **Packing:** Multiple values automatically create tuples
   - `coords = 10, 20` (parentheses optional)
   - Functions can return multiple values

2. **Basic Unpacking:** Extract tuple elements
   - `x, y = point`
   - Number of variables must match

3. **Extended Unpacking:** Use `*` to collect remaining items
   - `first, *rest = numbers`
   - `first, *middle, last = data`

4. **Variable Swapping:** Elegant one-liner
   - `a, b = b, a`

5. **Function Integration:**
   - Return multiple values: `return min, max, avg`
   - Unpack arguments: `func(*args, **kwargs)`

6. **Loop Unpacking:**
   - `for x, y in points`
   - `for index, value in enumerate(items)`
   - `for key, value in dict.items()`

**Key Takeaways:**

- **Packing and unpacking make Python code more readable and concise**
- **Use extended unpacking (*) when dealing with variable-length data**
- **Always ensure the number of variables matches (or use *)**
- **Leverage unpacking in loops for cleaner iteration**
- **Use _ for values you want to ignore**

**Real-World Impact:**

Tuple packing and unpacking are everywhere in Python:
- Function returns (multiple values)
- Data processing (CSV, JSON parsing)
- Algorithm implementations (swapping, transformations)
- Iterating over structured data

**Master this feature and your Python code becomes more elegant, readable, and Pythonic!**

**Practice these patterns and they'll become second nature.**
