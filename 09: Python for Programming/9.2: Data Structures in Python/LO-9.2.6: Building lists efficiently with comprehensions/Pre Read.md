# Pre-Read: Building Lists Efficiently with Comprehensions

## What You'll Learn
In this lesson, you'll learn about list comprehensions - Python's elegant and powerful way to create lists in a single, readable line of code.

## Why This Matters
List comprehensions are essential for:
- Writing more concise and readable code
- Creating lists faster and more efficiently
- Following Pythonic coding conventions
- Transforming data in one elegant expression
- Filtering and mapping data simultaneously
- Impressing future employers with clean code

List comprehensions are used everywhere in professional Python code. They're one of Python's most beloved features!

---

## What is a List Comprehension?

A **list comprehension** is a concise way to create lists based on existing sequences or ranges. It combines the for loop and list building into a single line.

**Traditional approach:**
```python
squares = []
for num in range(1, 6):
    squares.append(num ** 2)
print(squares)  # [1, 4, 9, 16, 25]
```

**List comprehension approach:**
```python
squares = [num ** 2 for num in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

Much cleaner and more Pythonic!

---

## Basic Syntax

```python
new_list = [expression for item in iterable]
```

**Components:**
- `expression`: What to do with each item
- `item`: Variable name for each element
- `iterable`: The sequence to process (list, range, string, etc.)

### Simple Examples

```python
# Create list of numbers 1-10
numbers = [x for x in range(1, 11)]
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Double each number
doubles = [x * 2 for x in range(1, 6)]
print(doubles)  # [2, 4, 6, 8, 10]

# Get first letter of each name
names = ["Alice", "Bob", "Charlie"]
initials = [name[0] for name in names]
print(initials)  # ['A', 'B', 'C']
```

---

## Comprehensions vs Traditional Loops

### Example 1: Squaring Numbers

**Traditional loop:**
```python
squares = []
for num in [1, 2, 3, 4, 5]:
    squares.append(num ** 2)
# Result: [1, 4, 9, 16, 25]
```

**List comprehension:**
```python
squares = [num ** 2 for num in [1, 2, 3, 4, 5]]
# Result: [1, 4, 9, 16, 25]
```

### Example 2: Uppercase Conversion

**Traditional loop:**
```python
words = ["hello", "world", "python"]
upper_words = []
for word in words:
    upper_words.append(word.upper())
# Result: ['HELLO', 'WORLD', 'PYTHON']
```

**List comprehension:**
```python
upper_words = [word.upper() for word in ["hello", "world", "python"]]
# Result: ['HELLO', 'WORLD', 'PYTHON']
```

---

## List Comprehensions with Conditions (Filtering)

Add an `if` condition to filter items:

```python
new_list = [expression for item in iterable if condition]
```

### Example: Even Numbers Only

**Traditional loop:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(evens)  # [2, 4, 6, 8, 10]
```

**List comprehension:**
```python
evens = [num for num in range(1, 11) if num % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]
```

### Example: Filter Long Words

```python
words = ["apple", "pie", "banana", "cat", "strawberry"]
long_words = [word for word in words if len(word) > 5]
print(long_words)  # ['banana', 'strawberry']
```

### Example: Positive Numbers Only

```python
numbers = [-5, 3, -2, 8, -1, 10, -7]
positives = [num for num in numbers if num > 0]
print(positives)  # [3, 8, 10]
```

---

## Transform and Filter Together

You can transform items while filtering:

```python
# Square only even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_squares = [num ** 2 for num in numbers if num % 2 == 0]
print(even_squares)  # [4, 16, 36]

# Capitalize names starting with 'A'
names = ["Alice", "Bob", "Andrew", "Charlie", "Anna"]
a_names = [name.upper() for name in names if name.startswith('A')]
print(a_names)  # ['ALICE', 'ANDREW', 'ANNA']
```

---

## Comprehensions with if-else (Conditional Expression)

When you need both branches (if-else), the syntax changes:

```python
new_list = [expression_if_true if condition else expression_if_false for item in iterable]
```

**Note:** The if-else comes BEFORE the for!

### Example: Even or Odd Labels

```python
numbers = [1, 2, 3, 4, 5]
labels = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']
```

### Example: Pass or Fail

```python
scores = [45, 78, 92, 65, 88, 53]
results = ["Pass" if score >= 70 else "Fail" for score in scores]
print(results)  # ['Fail', 'Pass', 'Pass', 'Fail', 'Pass', 'Fail']
```

**Syntax reminder:**
- **Filtering only (no else):** `[expr for x in list if condition]`
- **If-else (both branches):** `[expr_if if condition else expr_else for x in list]`

---

## Real-World Examples

### Example 1: Temperature Conversion

```python
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]
```

### Example 2: Extract Vowels from String

```python
word = "comprehension"
vowels = [char for char in word if char in "aeiou"]
print(vowels)  # ['o', 'e', 'e', 'i', 'o']
```

### Example 3: Price with Tax

```python
prices = [10.00, 25.50, 15.75, 30.00]
tax_rate = 0.08
prices_with_tax = [price * (1 + tax_rate) for price in prices]
print(prices_with_tax)  # [10.8, 27.54, 17.01, 32.4]
```

### Example 4: Clean Data

```python
# Remove whitespace from strings
data = ["  hello  ", "world  ", "  python"]
cleaned = [item.strip() for item in data]
print(cleaned)  # ['hello', 'world', 'python']
```

### Example 5: Create Tuples

```python
numbers = [1, 2, 3, 4, 5]
pairs = [(num, num ** 2) for num in numbers]
print(pairs)  # [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
```

---

## Nested List Comprehensions

You can nest comprehensions for 2D data (advanced!):

```python
# Create a 3x3 matrix
matrix = [[i * 3 + j for j in range(1, 4)] for i in range(3)]
print(matrix)
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]

# Flatten a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## Working with Strings

Strings are iterable, so you can use comprehensions:

```python
# Convert each character to uppercase
word = "python"
upper_chars = [char.upper() for char in word]
print(upper_chars)  # ['P', 'Y', 'T', 'H', 'O', 'N']

# Get ASCII codes
word = "ABC"
ascii_codes = [ord(char) for char in word]
print(ascii_codes)  # [65, 66, 67]

# Remove vowels from a word
word = "beautiful"
no_vowels = ''.join([char for char in word if char not in "aeiou"])
print(no_vowels)  # "btfl"
```

---

## Working with range()

```python
# First 10 squares
squares = [x ** 2 for x in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# First 10 cubes
cubes = [x ** 3 for x in range(1, 11)]
print(cubes)  # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# Multiples of 5 up to 50
multiples = [x * 5 for x in range(1, 11)]
print(multiples)  # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
```

---

## Common Patterns

### Pattern 1: Apply Function to Each Item

```python
# Round all numbers
numbers = [3.14159, 2.71828, 1.41421]
rounded = [round(num, 2) for num in numbers]
print(rounded)  # [3.14, 2.72, 1.41]

# Get lengths of words
words = ["apple", "banana", "cherry"]
lengths = [len(word) for word in words]
print(lengths)  # [5, 6, 6]
```

### Pattern 2: Filter by Condition

```python
# Get numbers greater than 5
numbers = [2, 7, 1, 9, 4, 6, 3, 8]
large = [num for num in numbers if num > 5]
print(large)  # [7, 9, 6, 8]

# Get words starting with 'p'
words = ["python", "java", "perl", "ruby", "php"]
p_words = [word for word in words if word.startswith('p')]
print(p_words)  # ['python', 'perl', 'php']
```

### Pattern 3: Transform with Condition

```python
# Double evens, keep odds as-is
numbers = [1, 2, 3, 4, 5, 6]
result = [num * 2 if num % 2 == 0 else num for num in numbers]
print(result)  # [1, 4, 3, 8, 5, 12]
```

---

## When to Use List Comprehensions

**Use comprehensions when:**
- Creating a simple list based on another sequence
- Transforming or filtering data in one operation
- Code is readable and fits on one line (or two at most)
- Operation is straightforward

**Use traditional loops when:**
- Logic is complex with multiple conditions
- Need multiple operations per item
- Debugging is needed (loops are easier to debug)
- Code becomes hard to read as a comprehension

```python
# Good use - simple and readable
squares = [x ** 2 for x in range(10)]

# Bad use - too complex, hard to read
result = [x ** 2 if x % 2 == 0 else x ** 3 if x % 3 == 0 else x for x in range(20) if x > 5]

# Better as traditional loop
result = []
for x in range(20):
    if x > 5:
        if x % 2 == 0:
            result.append(x ** 2)
        elif x % 3 == 0:
            result.append(x ** 3)
        else:
            result.append(x)
```

---

## Try It Yourself (Before Class)

Run this code:

```python
# Example 1: Basic transformation
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print("Squares:", squares)

# Example 2: Filtering
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print("Evens:", evens)

# Example 3: Transform and filter
numbers = [1, 2, 3, 4, 5, 6]
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print("Even squares:", even_squares)

# Example 4: With if-else
numbers = [1, 2, 3, 4, 5]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print("Labels:", labels)

# Example 5: From string
word = "Python"
chars = [c.lower() for c in word]
print("Characters:", chars)
```

**Questions:**
1. What gets printed in each example?
2. How would you create a list of numbers from 1-20 that are divisible by 3?
3. Can you convert ["apple", "banana", "cherry"] to their lengths [5, 6, 6]?
4. How would you filter out numbers less than 5 and square the rest?

---

## Key Takeaways

Before class, remember:
1. **Basic syntax**: `[expression for item in iterable]`
2. **With filtering**: `[expression for item in iterable if condition]`
3. **With if-else**: `[expr_if if condition else expr_else for item in iterable]`
4. **More concise** than traditional loops
5. **More Pythonic** and preferred for simple operations
6. **Not always better** - use loops for complex logic
7. **Works with any iterable** - lists, strings, range, tuples, etc.

## What's Next?

In the live session, we'll:
- Practice writing list comprehensions
- Convert loops to comprehensions
- Combine multiple conditions
- Work with nested comprehensions
- Learn when (and when not) to use them
- Apply them to solve real problems

See you in class!
