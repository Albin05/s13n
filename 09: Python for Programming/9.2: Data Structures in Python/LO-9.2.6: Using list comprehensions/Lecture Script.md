## Lecture Script: Using List Comprehensions


---

### CS Theory Bite

> **Origin**: List comprehensions came from **Haskell** (1990) and **mathematical set notation**: `{x² | x ∈ ℕ, x < 10}` → `[x**2 for x in range(10)]`. Added in **Python 2.0** (PEP 202, 2000).
>
> **Analogy**: A comprehension is like an **assembly line blueprint** — describe the transformation once, and it produces the entire output automatically.
>
> **Why it matters**: Comprehensions are faster than loops (C-level optimization) and more readable for simple transformations.



### Hook (2 minutes)

"You need to create a list of squares from 1 to 100. With a traditional loop, you'd write 4 lines of code - initialize empty list, loop through range, calculate square, append to list. But what if I told you Python has a way to do this in just one elegant line?

List comprehensions are Python's superpower for creating lists. They're faster, more readable, and more Pythonic than traditional loops. Think of them as a recipe: 'Give me this expression, for each item, from this source, where this condition is true.' One line, crystal clear intent.

Master list comprehensions and you'll write code that's not just shorter, but actually easier to understand. Whether you're filtering data, transforming values, or building complex structures, comprehensions make your code shine. Today, we'll go from basics to advanced techniques that will transform how you work with lists."

---

### Section 1: Basic List Comprehension Syntax (3 minutes)

**From Loop to Comprehension:**

```python
# Traditional loop approach
squares = []
for num in range(1, 6):
    squares.append(num ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# List comprehension - one line!
squares = [num ** 2 for num in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

**Syntax Breakdown:**

```python
# Pattern: [expression for item in iterable]
#           ^^^^^^^^^^     ^^^^    ^^^^^^^^
#           what to       loop    where from
#           create        variable

# Simple examples
numbers = [x for x in range(5)]
print(numbers)  # [0, 1, 2, 3, 4]

doubles = [x * 2 for x in range(5)]
print(doubles)  # [0, 2, 4, 6, 8]

strings = [str(x) for x in range(5)]
print(strings)  # ['0', '1', '2', '3', '4']
```

**Working with Existing Lists:**

```python
# Transform each element
words = ['hello', 'world', 'python']
upper_words = [word.upper() for word in words]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']

# Calculate from elements
prices = [10.99, 25.50, 5.75, 100.00]
with_tax = [price * 1.08 for price in prices]
print(with_tax)  # [11.8692, 27.54, 6.21, 108.0]

# String operations
names = ['alice', 'bob', 'charlie']
capitalized = [name.capitalize() for name in names]
print(capitalized)  # ['Alice', 'Bob', 'Charlie']
```

**Mathematical Operations:**

```python
# Squares
squares = [n ** 2 for n in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Cubes
cubes = [n ** 3 for n in range(1, 6)]
print(cubes)  # [1, 8, 27, 64, 125]

# Formula application
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]
```

---

### Section 2: Comprehensions with Conditionals (3 minutes)

**Filtering with if:**

```python
# Pattern: [expression for item in iterable if condition]

# Get only even numbers
numbers = range(1, 11)
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Get only odd numbers
odds = [n for n in numbers if n % 2 != 0]
print(odds)  # [1, 3, 5, 7, 9]

# Filter by value threshold
scores = [45, 78, 92, 67, 85, 54, 90]
passing = [score for score in scores if score >= 70]
print(passing)  # [78, 92, 85, 90]
```

**String Filtering:**

```python
# Filter by length
words = ['a', 'bat', 'cat', 'elephant', 'dog']
long_words = [word for word in words if len(word) > 3]
print(long_words)  # ['elephant']

# Filter by starting letter
fruits = ['apple', 'banana', 'apricot', 'orange', 'avocado']
a_fruits = [fruit for fruit in fruits if fruit.startswith('a')]
print(a_fruits)  # ['apple', 'apricot', 'avocado']

# Filter by content
emails = ['user@gmail.com', 'test@yahoo.com', 'admin@gmail.com']
gmail = [email for email in emails if 'gmail' in email]
print(gmail)  # ['user@gmail.com', 'admin@gmail.com']
```

**Transform AND Filter:**

```python
# Square only even numbers
numbers = range(1, 11)
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]

# Uppercase only long words
words = ['hi', 'hello', 'hey', 'goodbye']
long_upper = [word.upper() for word in words if len(word) > 3]
print(long_upper)  # ['HELLO', 'GOODBYE']

# Price with discount for expensive items
prices = [15, 50, 120, 30, 200]
discounted = [price * 0.9 for price in prices if price > 100]
print(discounted)  # [108.0, 180.0]
```

---

### Section 3: if-else in Comprehensions (3 minutes)

**Conditional Expression (Ternary):**

```python
# Pattern: [true_expr if condition else false_expr for item in iterable]

# Categorize as even/odd
numbers = range(1, 6)
types = ['even' if n % 2 == 0 else 'odd' for n in numbers]
print(types)  # ['odd', 'even', 'odd', 'even', 'odd']

# Replace negatives with zero
values = [5, -2, 8, -7, 3]
positive_only = [x if x > 0 else 0 for x in values]
print(positive_only)  # [5, 0, 8, 0, 3]

# Cap values at maximum
scores = [85, 105, 92, 110, 78]
capped = [score if score <= 100 else 100 for score in scores]
print(capped)  # [85, 100, 92, 100, 78]
```

**Pass/Fail Grading:**

```python
grades = [85, 72, 90, 65, 78, 95]
results = ['Pass' if grade >= 70 else 'Fail' for grade in grades]
print(results)  # ['Pass', 'Pass', 'Pass', 'Fail', 'Pass', 'Pass']

# With letter grades
letter_grades = [
    'A' if score >= 90 else 
    'B' if score >= 80 else 
    'C' if score >= 70 else 
    'D' if score >= 60 else 'F'
    for score in grades
]
print(letter_grades)  # ['B', 'C', 'A', 'D', 'C', 'A']
```

**Data Cleaning:**

```python
# Replace None with default
data = [10, None, 30, None, 50]
cleaned = [x if x is not None else 0 for x in data]
print(cleaned)  # [10, 0, 30, 0, 50]

# Sanitize strings
inputs = ['hello', '', 'world', '  ', 'python']
valid = [s if s.strip() else 'N/A' for s in inputs]
print(valid)  # ['hello', 'N/A', 'world', 'N/A', 'python']
```

---

### Section 4: Nested Comprehensions (3 minutes)

**2D Lists (Matrices):**

```python
# Create 3x3 matrix
matrix = [[i * 3 + j for j in range(3)] for i in range(3)]
print(matrix)
# [[0, 1, 2],
#  [3, 4, 5],
#  [6, 7, 8]]

# Identity matrix
identity = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
print(identity)
# [[1, 0, 0],
#  [0, 1, 0],
#  [0, 0, 1]]

# Multiplication table
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for row in table:
    print(row)
# [1, 2, 3, 4, 5]
# [2, 4, 6, 8, 10]
# [3, 6, 9, 12, 15]
# ...
```

**Flattening Lists:**

```python
# Nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flatten to 1D
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# With filtering
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_flat = [num for row in matrix for num in row if num % 2 == 0]
print(even_flat)  # [2, 4, 6, 8]
```

**Cartesian Product:**

```python
# All combinations
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
products = [(color, size) for color in colors for size in sizes]
print(products)
# [('red', 'S'), ('red', 'M'), ('red', 'L'),
#  ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]

# Coordinate grid
coords = [(x, y) for x in range(3) for y in range(3)]
print(coords)
# [(0, 0), (0, 1), (0, 2),
#  (1, 0), (1, 1), (1, 2),
#  (2, 0), (2, 1), (2, 2)]
```

---

### Section 5: Working with Multiple Lists (2 minutes)

**Using zip() in Comprehensions:**

```python
# Combine two lists
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]

# Create tuples
pairs = [(name, score) for name, score in zip(names, scores)]
print(pairs)  # [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# Calculate from multiple sources
prices = [100, 200, 300]
quantities = [2, 1, 3]
totals = [p * q for p, q in zip(prices, quantities)]
print(totals)  # [200, 200, 900]

# String formatting
students = ['Alice', 'Bob']
grades = [92, 85]
reports = [f"{name}: {grade}" for name, grade in zip(students, grades)]
print(reports)  # ['Alice: 92', 'Bob: 85']
```

**enumerate() in Comprehensions:**

```python
# Add index to values
fruits = ['apple', 'banana', 'orange']
indexed = [(i, fruit) for i, fruit in enumerate(fruits)]
print(indexed)  # [(0, 'apple'), (1, 'banana'), (2, 'orange')]

# Numbered list
numbered = [f"{i+1}. {fruit}" for i, fruit in enumerate(fruits)]
print(numbered)  # ['1. apple', '2. banana', '3. orange']
```

---

### Section 6: Practical Applications (3 minutes)

**Data Transformation:**

```python
# Parse CSV-like data
data = "10,20,30,40,50"
numbers = [int(x) for x in data.split(',')]
print(numbers)  # [10, 20, 30, 40, 50]

# Extract from dictionaries
users = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 22}
]
names = [user['name'] for user in users]
print(names)  # ['Alice', 'Bob', 'Charlie']

adults = [user for user in users if user['age'] >= 25]
print(adults)  # [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
```

**Text Processing:**

```python
# Extract words
sentence = "The quick brown fox jumps"
words = [word for word in sentence.split()]
print(words)  # ['The', 'quick', 'brown', 'fox', 'jumps']

# Filter and clean
text = "Hello123 World456 Python789"
letters_only = [''.join(c for c in word if c.isalpha()) for word in text.split()]
print(letters_only)  # ['Hello', 'World', 'Python']

# First letters
words = ['apple', 'banana', 'cherry']
initials = [word[0].upper() for word in words]
print(initials)  # ['A', 'B', 'C']
```

**Mathematical Sequences:**

```python
# Fibonacci-like with comprehension + recursion
fibs = [0, 1]
fibs.extend([fibs[i-1] + fibs[i-2] for i in range(2, 10)])
print(fibs)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Prime numbers (simple check)
def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

primes = [n for n in range(2, 50) if is_prime(n)]
print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

---

### Section 7: Performance and Best Practices (1 minute)

**When to Use Comprehensions:**

```python
# GOOD - Simple transformation
squares = [x ** 2 for x in range(10)]

# GOOD - Simple filtering
evens = [x for x in range(10) if x % 2 == 0]

# AVOID - Too complex, use regular loop
# BAD - Hard to read
result = [
    x * y + z if x > y else y * z + x 
    for x in range(10) 
    for y in range(10) 
    for z in range(10)
    if x + y + z > 15
]

# BETTER - Use regular loop for complex logic
result = []
for x in range(10):
    for y in range(10):
        for z in range(10):
            if x + y + z > 15:
                if x > y:
                    result.append(x * y + z)
                else:
                    result.append(y * z + x)
```

**Performance Tips:**

```python
# Comprehensions are faster than loops
import time

# Traditional loop
start = time.time()
squares = []
for i in range(1000000):
    squares.append(i ** 2)
loop_time = time.time() - start

# Comprehension
start = time.time()
squares = [i ** 2 for i in range(1000000)]
comp_time = time.time() - start

print(f"Loop: {loop_time:.4f}s")
print(f"Comprehension: {comp_time:.4f}s")
# Comprehension is typically 20-30% faster
```

---

### Summary (1 minute)

List comprehensions are a powerful Python feature for creating lists:

**Basic Syntax:**
- `[expression for item in iterable]`
- `[expr for item in iterable if condition]`
- `[expr if cond else other for item in iterable]`

**Key Benefits:**
- More concise than loops
- Faster performance
- More readable (when simple)
- Pythonic style

**Common Patterns:**
- Transform: `[x * 2 for x in numbers]`
- Filter: `[x for x in numbers if x > 0]`
- Both: `[x * 2 for x in numbers if x > 0]`
- Nested: `[x for row in matrix for x in row]`

**Best Practices:**
- Use for simple to moderate transformations
- Keep them readable (< 2 lines)
- Use regular loops for complex logic
- Combine with zip(), enumerate(), range()

**Remember:**
- Comprehensions create new lists
- Original data unchanged
- Can nest but keep it simple
- Performance boost over loops

Master comprehensions and your Python code becomes elegant and efficient!
