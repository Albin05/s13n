# Lecture Script: LO-71 Use List Comprehensions

## [0:00-0:02] Hook (2 min)
**Say**: "Want to create a list of squares from 0 to 9? Traditional way: 4 lines of code. Python way: 1 line! That's the power of list comprehensions — concise, readable, and Pythonic. Let me show you the magic!"

**Demo**:
```python
# Traditional way - boring!
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List comprehension - elegant!
squares = [i ** 2 for i in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**Say**: "Same result, way less code. Let's master list comprehensions!"

## [0:02-0:06] Basic Syntax (4 min)

**Say**: "List comprehension syntax: [expression for item in iterable]. It's like a for loop turned inside out!"

**Live Code**:
```python
# Pattern: [what_to_do for item in sequence]

# Example 1: Double each number
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print(doubled)  # [2, 4, 6, 8, 10]

# Example 2: Convert to uppercase
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
print(upper_names)  # ['ALICE', 'BOB', 'CHARLIE']

# Example 3: Get string lengths
words = ["hello", "world", "python"]
lengths = [len(word) for word in words]
print(lengths)  # [5, 5, 6]

# Example 4: Create ranges
multiples_of_5 = [i * 5 for i in range(1, 11)]
print(multiples_of_5)  # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
```

**Point out**: "Read it like English: 'Create a list of [n * 2] FOR each [n] IN [numbers]'."

**Emphasize**: "The result is ALWAYS a list, no matter what the input is!"

## [0:06-0:10] List Comprehensions with Conditions (4 min)

**Say**: "Add an 'if' to filter items. Pattern: [expression for item in iterable if condition]"

**Live Code**:
```python
# Get only even numbers
numbers = range(20)
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Get only positive numbers
numbers = [-5, -2, 0, 3, 7, -1, 8]
positives = [n for n in numbers if n > 0]
print(positives)  # [3, 7, 8]

# Get long words (more than 5 letters)
words = ["hi", "python", "is", "awesome", "yes"]
long_words = [word for word in words if len(word) > 5]
print(long_words)  # ['python', 'awesome']

# Square only odd numbers
numbers = range(10)
odd_squares = [n ** 2 for n in numbers if n % 2 != 0]
print(odd_squares)  # [1, 9, 25, 49, 81]
```

**Say**: "The 'if' at the end FILTERS. Only items passing the condition are included!"

**Point out**: "This replaces filter() and map() in one clean line!"

## [0:10-0:14] if-else in List Comprehensions (4 min)

**Say**: "Want to transform differently based on a condition? Use if-else BEFORE the for!"

**Live Code**:
```python
# Pattern: [value_if_true if condition else value_if_false for item in iterable]

# Label numbers as even or odd
numbers = [1, 2, 3, 4, 5, 6]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd', 'even']

# Replace negative numbers with 0
numbers = [-3, 5, -1, 8, -7, 2]
non_negative = [n if n >= 0 else 0 for n in numbers]
print(non_negative)  # [0, 5, 0, 8, 0, 2]

# Double evens, triple odds
numbers = [1, 2, 3, 4, 5]
transformed = [n * 2 if n % 2 == 0 else n * 3 for n in numbers]
print(transformed)  # [3, 4, 9, 8, 15]

# Grade to letter
scores = [85, 92, 78, 95, 88]
grades = ["A" if s >= 90 else "B" if s >= 80 else "C" for s in scores]
print(grades)  # ['B', 'A', 'C', 'A', 'B']
```

**Emphasize**: "if-else BEFORE for: transform. if AFTER for: filter. Big difference!"

**Show the difference**:
```python
# FILTER - if after for
evens = [n for n in range(10) if n % 2 == 0]
# [0, 2, 4, 6, 8] - only evens

# TRANSFORM - if-else before for
labels = ["even" if n % 2 == 0 else "odd" for n in range(5)]
# ['even', 'odd', 'even', 'odd', 'even'] - all numbers, labeled
```

## [0:14-0:18] Real-World Examples (4 min)

**Say**: "Let's see list comprehensions solving real problems!"

**Live Code**:
```python
# Example 1: Process student data
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 95}
]

# Extract all grades
grades = [student["grade"] for student in students]
print(grades)  # [85, 92, 78, 95]

# Get names of passing students (grade >= 80)
passed = [student["name"] for student in students if student["grade"] >= 80]
print(passed)  # ['Alice', 'Bob', 'Diana']

# Create formatted reports
reports = [f"{s['name']}: {s['grade']}%" for s in students]
print(reports)
# ['Alice: 85%', 'Bob: 92%', 'Charlie: 78%', 'Diana: 95%']

# Example 2: File processing
files = ["doc.txt", "image.png", "script.py", "data.csv", "photo.jpg"]

# Get only Python files
python_files = [f for f in files if f.endswith(".py")]
print(python_files)  # ['script.py']

# Get filenames without extensions
names = [f.split(".")[0] for f in files]
print(names)  # ['doc', 'image', 'script', 'data', 'photo']

# Example 3: Temperature conversion
fahrenheit_temps = [32, 68, 86, 104, 122]
celsius_temps = [(f - 32) * 5/9 for f in fahrenheit_temps]
print([f"{c:.1f}°C" for c in celsius_temps])
# ['0.0°C', '20.0°C', '30.0°C', '40.0°C', '50.0°C']
```

**Say**: "Notice how readable these are! Each one is clear and concise."

## [0:18-0:21] Nested List Comprehensions (3 min)

**Say**: "List comprehensions can be nested for working with 2D data. But don't overdo it!"

**Live Code**:
```python
# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get even numbers from 2D list
evens = [num for row in matrix for num in row if num % 2 == 0]
print(evens)  # [2, 4, 6, 8]

# Create coordinate pairs
coordinates = [(x, y) for x in range(3) for y in range(3)]
print(coordinates)
# [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]

# Create multiplication table
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for row in table:
    print(row)
# [1, 2, 3, 4, 5]
# [2, 4, 6, 8, 10]
# [3, 6, 9, 12, 15]
# [4, 8, 12, 16, 20]
# [5, 10, 15, 20, 25]
```

**Point out**: "Read nested comprehensions from left to right: 'for row in matrix, for num in row'."

**Emphasize**: "If it gets too complex, use regular for loops instead! Readability matters more than brevity."

## [0:21-0:23] Practice Challenge (2 min)

**Challenge**: "Given a list of words, create a list of lengths for words starting with vowels."

**Skeleton**:
```python
words = ["apple", "banana", "orange", "grape", "kiwi", "elderberry"]

# TODO: Get lengths of words starting with a, e, i, o, or u
vowel_word_lengths = []  # Use list comprehension!

print(vowel_word_lengths)  # Should be [5, 6, 10]
```

**Give them 1-2 minutes**

**Solution**:
```python
vowels = "aeiouAEIOU"
vowel_word_lengths = [len(word) for word in words if word[0] in vowels]
print(vowel_word_lengths)  # [5, 6, 10]
```

**Bonus challenge**:
```python
# Convert to uppercase, but only vowel words
result = [word.upper() for word in words if word[0] in vowels]
print(result)  # ['APPLE', 'ORANGE', 'ELDERBERRY']
```

## [0:23-0:25] Wrap-up (2 min)

**Key Points**:
1. **Basic syntax**: `[expression for item in iterable]`
2. **With filter**: `[expression for item in iterable if condition]`
3. **With transform**: `[value_if_true if condition else value_if_false for item in iterable]`
4. **Nested**: `[item for sublist in list for item in sublist]`
5. **Always returns a list** — even if input is tuple, set, etc.

**Common Mistakes**:
- Confusing filter (if after for) vs transform (if-else before for)
- Making comprehensions too complex — use regular loops if unclear
- Forgetting square brackets — that's what makes it a LIST comprehension
- Not considering readability — sometimes a for loop is clearer!

**When to Use List Comprehensions**:
- Simple transformations and filters
- When it improves readability
- When you want a Pythonic, concise solution
- Processing collections in one line

**When NOT to Use**:
- Complex logic that's hard to read
- Multiple conditions and transformations
- When side effects are needed (use regular for loops)
- When debugging would be difficult

**Performance Note**: "List comprehensions are usually faster than regular for loops with append()!"

**Closing**: "List comprehensions are the Pythonic way to create lists! They're concise, readable, and fast. Master them, and your code will look professional and clean. Remember: keep them simple and readable — if it's getting confusing, use a regular for loop instead!"
