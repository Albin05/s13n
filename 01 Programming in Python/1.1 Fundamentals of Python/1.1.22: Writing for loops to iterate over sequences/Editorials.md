# Editorials: Writing For Loops to Iterate Over Sequences

## Problem 1: Print List Items (Easy)

### Solution
```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
```

**Output:**
```
apple
banana
orange
```

### Explanation
- `for fruit in fruits:` iterates through the list
- Variable `fruit` takes each value from the list in order
- No indexing or counter needed
- Clean, Pythonic way to iterate
- Works with any sequence (list, tuple, string)

---

## Problem 2: Sum List Numbers (Easy)

### Solution
```python
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print(f"Total: {total}")
```

**Output:**
```
Total: 150
```

### Explanation
- Initialize total before loop
- Each iteration adds current number to total
- 10 + 20 + 30 + 40 + 50 = 150
- Accumulator pattern with for loop
- Simpler than while loop (no manual indexing)

---

## Problem 3: Iterate String Characters (Easy)

### Solution
```python
word = "python"

for char in word:
    print(char)
```

**Output:**
```
p
y
t
h
o
n
```

### Explanation
- Strings are sequences - can iterate directly
- Each character accessed in order
- Variable `char` holds each character
- No need for `word[i]` indexing
- More readable than while loop

---

## Problem 4: Count Vowels (Easy)

### Solution
```python
text = "hello world"
vowel_count = 0

for char in text:
    if char in "aeiou":
        vowel_count += 1

print(f"Vowels: {vowel_count}")
```

**Output:**
```
Vowels: 3
```

### Explanation
- Iterate through each character
- Check if character is vowel
- Increment counter when found
- Vowels in "hello world": e, o, o = 3
- Simple filtering with for loop

---

## Problem 5: Print with Index (Medium)

### Solution
```python
colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(f"{index}: {color}")
```

**Output:**
```
0: red
1: green
2: blue
```

### Explanation
- `enumerate()` provides both index and value
- Returns tuples: (0, "red"), (1, "green"), (2, "blue")
- Unpacking: `index, color` from each tuple
- Start index is 0 by default
- Can specify start: `enumerate(colors, 1)` for 1-based

---

## Problem 6: Iterate Multiple Lists (Medium)

### Solution
```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

**Output:**
```
Alice is 25 years old
Bob is 30 years old
Charlie is 35 years old
```

### Explanation
- `zip()` combines multiple lists
- Creates pairs: ("Alice", 25), ("Bob", 30), ("Charlie", 35)
- Loop unpacks each pair
- Stops at shortest list length
- Elegant parallel iteration

---

## Problem 7: Build New List (Medium)

### Solution
```python
numbers = [1, 2, 3, 4, 5]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print(f"Doubled: {doubled}")
```

**Output:**
```
Doubled: [2, 4, 6, 8, 10]
```

### Explanation
- Create empty result list
- Iterate through original
- Transform each element (multiply by 2)
- Append to new list
- Original list unchanged
- Map/transform pattern

---

## Problem 8: Dictionary Iteration (Medium)

### Solution
```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

for key, value in student.items():
    print(f"{key}: {value}")
```

**Output:**
```
name: Alice
age: 20
grade: A
```

### Explanation
- `.items()` returns key-value pairs
- Each iteration unpacks one pair
- Can also use `.keys()` for keys only
- Or `.values()` for values only
- Dictionary iteration is powerful

---

## Problem 9: Nested Lists (Hard)

### Solution
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for num in row:
        print(num, end=" ")
    print()  # Newline after each row
```

**Output:**
```
1 2 3
4 5 6
7 8 9
```

### Explanation
- Outer loop iterates rows
- Inner loop iterates elements in each row
- `end=" "` prints on same line
- `print()` after inner loop creates newline
- Nested for loops for 2D structures

---

## Problem 10: Find Maximum (Hard)

### Solution
```python
numbers = [45, 12, 78, 34, 90, 23]
max_num = numbers[0]  # Initialize with first element

for num in numbers:
    if num > max_num:
        max_num = num

print(f"Maximum: {max_num}")
```

**Output:**
```
Maximum: 90
```

### Explanation
- Initialize max with first element
- Compare each number to current max
- Update max when larger found
- Final max is 90
- Alternative: use built-in `max(numbers)`
- Understanding algorithm is important

---

## Problem 11: List Comprehension Alternative (Hard)

### Solution
```python
# Traditional for loop
numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
    squares.append(num ** 2)

print(f"Squares: {squares}")

# List comprehension (more Pythonic)
squares_comp = [num ** 2 for num in numbers]
print(f"Squares (comprehension): {squares_comp}")
```

**Output:**
```
Squares: [1, 4, 9, 16, 25]
Squares (comprehension): [1, 4, 9, 16, 25]
```

### Explanation
- Both produce same result
- List comprehension is more concise
- Syntax: `[expression for item in sequence]`
- For loop more readable for beginners
- Comprehension faster for large lists

---

## Problem 12: Tuple Unpacking (Hard)

### Solution
```python
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
]

for name, score in students:
    print(f"{name} scored {score}")
```

**Output:**
```
Alice scored 85
Bob scored 92
Charlie scored 78
```

### Explanation
- List contains tuples
- For loop unpacks each tuple
- `name, score` gets values from tuple
- Works with any iterable of tuples
- Clean way to handle structured data

---

## Problem 13: Reverse Iteration (Hard)

### Solution
```python
numbers = [1, 2, 3, 4, 5]

for num in reversed(numbers):
    print(num)
```

**Output:**
```
5
4
3
2
1
```

### Explanation
- `reversed()` iterates in reverse order
- Original list unchanged
- Returns reverse iterator
- More efficient than `numbers[::-1]` for large lists
- Works with any sequence

---

## Problem 14: Filter with For Loop (Very Hard)

### Solution
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(f"Even numbers: {evens}")

# Alternative with list comprehension
evens_comp = [num for num in numbers if num % 2 == 0]
print(f"Even (comprehension): {evens_comp}")
```

**Output:**
```
Even numbers: [2, 4, 6, 8, 10]
Even (comprehension): [2, 4, 6, 8, 10]
```

### Explanation
- Filter pattern: collect items matching condition
- Traditional loop: check condition, append if True
- Comprehension: `[expr for item in seq if condition]`
- Both create new list with only evens
- Comprehension more Pythonic

---

## Problem 15: Nested Dictionary (Very Hard)

### Solution
```python
school = {
    "math": {"Alice": 90, "Bob": 85},
    "science": {"Alice": 88, "Bob": 92}
}

for subject, students in school.items():
    print(f"\n{subject.upper()}:")
    for student, grade in students.items():
        print(f"  {student}: {grade}")
```

**Output:**
```
MATH:
  Alice: 90
  Bob: 85

SCIENCE:
  Alice: 88
  Bob: 92
```

### Explanation
- Nested dictionary structure
- Outer loop: subjects
- Inner loop: students in each subject
- Two-level unpacking
- Demonstrates complex data iteration

---

## Problem 16: Calculate Average per Student (Very Hard)

### Solution
```python
grades = {
    "Alice": [85, 90, 88],
    "Bob": [92, 87, 95],
    "Charlie": [78, 82, 80]
}

for student, scores in grades.items():
    average = sum(scores) / len(scores)
    print(f"{student}: {average:.1f}")
```

**Output:**
```
Alice: 87.7
Bob: 91.3
Charlie: 80.0
```

### Explanation
- Dictionary with list values
- Iterate key-value pairs
- Calculate average for each student's scores
- Use `sum()` and `len()` functions
- Format average to 1 decimal place

---

## Problem 17: Flatten Nested List (Very Hard)

### Solution
```python
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = []

for sublist in nested:
    for num in sublist:
        flat.append(num)

print(f"Flattened: {flat}")
```

**Output:**
```
Flattened: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Explanation
- Convert 2D list to 1D
- Outer loop: each sublist
- Inner loop: elements in sublist
- Append all to single flat list
- Result contains all 9 numbers in order

---

## Problem 18: Count Word Frequencies (Very Hard)

### Solution
```python
text = "the quick brown fox jumps over the lazy dog the fox"
words = text.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

for word, count in frequency.items():
    print(f"{word}: {count}")
```

**Output:**
```
the: 3
quick: 1
brown: 1
fox: 2
jumps: 1
over: 1
lazy: 1
dog: 1
```

### Explanation
- Count occurrences of each word
- First loop: build frequency dictionary
- Check if word exists, increment or initialize
- Second loop: display results
- Classic frequency counting pattern

---

## Problem 19: Process CSV-like Data (Very Hard)

### Solution
```python
data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "NYC"],
    ["Bob", "30", "LA"],
    ["Charlie", "35", "Chicago"]
]

headers = data[0]
rows = data[1:]

for row in rows:
    for i, value in enumerate(row):
        print(f"{headers[i]}: {value}")
    print("-" * 20)
```

**Output:**
```
Name: Alice
Age: 25
City: NYC
--------------------
Name: Bob
Age: 30
City: LA
--------------------
Name: Charlie
Age: 35
City: Chicago
--------------------
```

### Explanation
- First row is headers
- Remaining rows are data
- Iterate each data row
- Use enumerate to match with headers
- Display structured data

---

## Problem 20: Multiplication Table (Very Hard)

### Solution
```python
size = 5

for i in range(1, size + 1):
    for j in range(1, size + 1):
        product = i * j
        print(f"{product:4}", end="")
    print()  # Newline after each row
```

**Output:**
```
   1   2   3   4   5
   2   4   6   8  10
   3   6   9  12  15
   4   8  12  16  20
   5  10  15  20  25
```

### Explanation
- Nested loops for rows and columns
- Outer loop: i from 1 to 5
- Inner loop: j from 1 to 5
- Calculate and print product
- `:4` formats with 4-character width
- Creates aligned multiplication table

---

## Key Concepts Demonstrated

1. **Direct Iteration**: `for item in sequence` - no indexing needed
2. **Enumerate**: Get index and value together
3. **Zip**: Iterate multiple sequences in parallel
4. **Dictionary Methods**: `.items()`, `.keys()`, `.values()`
5. **Nested Loops**: Iterate 2D structures
6. **Accumulator Pattern**: Build sum, max, new lists
7. **Tuple Unpacking**: Extract multiple values per iteration
8. **Reversed**: Iterate backwards
9. **List Comprehension**: Concise alternative to for loops
10. **Filter Pattern**: Collect items matching condition

## For Loop vs While Loop

| Feature | For Loop | While Loop |
|---------|----------|------------|
| **Use case** | Known sequence | Unknown iterations |
| **Syntax** | `for item in seq:` | `while condition:` |
| **Iteration** | Automatic | Manual |
| **Indexing** | Optional (enumerate) | Manual counter |
| **Best for** | Lists, strings, ranges | Conditions, user input |

## Common Patterns

```python
# Pattern 1: Iterate sequence
for item in sequence:
    process(item)

# Pattern 2: Accumulate
total = 0
for num in numbers:
    total += num

# Pattern 3: Build new list
result = []
for item in sequence:
    result.append(transform(item))

# Pattern 4: Enumerate
for index, item in enumerate(sequence):
    print(f"{index}: {item}")

# Pattern 5: Zip multiple
for a, b in zip(list1, list2):
    combine(a, b)

# Pattern 6: Dictionary iteration
for key, value in dictionary.items():
    process(key, value)

# Pattern 7: Nested
for row in matrix:
    for item in row:
        process(item)

# Pattern 8: Filter
result = []
for item in sequence:
    if condition(item):
        result.append(item)
```

## Best Practices

1. **Use for over while**: When iterating sequences
2. **Meaningful names**: `for student in students` not `for s in s`
3. **Enumerate when needed**: Don't manually track index
4. **Zip for parallel**: Better than indexing multiple lists
5. **Dictionary methods**: Use `.items()` for key-value pairs
6. **List comprehension**: For simple transformations
7. **Break and continue**: Work same as in while loops
8. **Keep simple**: Avoid deeply nested loops when possible

## Python-Specific Features

- **No semicolons**: Clean syntax
- **Indentation matters**: Defines loop body
- **Works on any iterable**: Lists, tuples, strings, ranges, files
- **Unpacking**: Extract multiple values per iteration
- **Built-in functions**: `enumerate()`, `zip()`, `reversed()`
- **Comprehensions**: List, dict, set comprehensions
- **Else clause**: Runs if loop completes without break

## Common Mistakes

1. **Modifying list during iteration**: Creates issues
2. **Not understanding enumerate**: Manually tracking index
3. **Forgetting colon**: Syntax error
4. **Wrong indentation**: Not part of loop
5. **Using index when not needed**: Less Pythonic
6. **Not using zip**: Parallel iteration with indexing
7. **Deep nesting**: Hard to read and maintain
