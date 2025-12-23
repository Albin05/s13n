# Editorials: Building Lists Efficiently with Comprehensions

## Problem 1: Square Numbers (Easy)

### Solution
```python
squares = [x ** 2 for x in range(1, 11)]
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### Explanation
- Use range(1, 11) to generate numbers 1 through 10
- Apply the expression `x ** 2` to square each number
- This is a basic transformation comprehension

---

## Problem 2: Filter Positive Numbers (Easy)

### Solution
```python
numbers = [-5, 3, -2, 8, -1, 10, -7, 4, 0]
positives = [num for num in numbers if num > 0]
print(positives)
# [3, 8, 10, 4]
```

### Explanation
- Use filtering: `if num > 0` at the end
- Only numbers that satisfy the condition are included
- Zero is excluded because 0 is not > 0

---

## Problem 3: Uppercase Words (Easy)

### Solution
```python
words = ["hello", "world", "python", "programming"]
uppercase = [word.upper() for word in words]
print(uppercase)
# ['HELLO', 'WORLD', 'PYTHON', 'PROGRAMMING']
```

### Explanation
- Apply .upper() method to each word
- Simple transformation comprehension
- No filtering needed - all words are transformed

---

## Problem 4: Even or Odd Labels (Medium)

### Solution
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
labels = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(labels)
# ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']
```

### Explanation
- Use conditional expression (if-else BEFORE for)
- For each number, check if even (num % 2 == 0)
- Return "even" if true, "odd" if false
- Every number gets a label (no filtering)

---

## Problem 5: Filter and Transform (Medium)

### Solution
```python
even_squares = [x ** 2 for x in range(1, 21) if x % 2 == 0]
print(even_squares)
# [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
```

### Explanation
- Filter: `if x % 2 == 0` selects only even numbers
- Transform: `x ** 2` squares each selected number
- Combines both operations in one comprehension
- Even numbers from 1-20: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20

---

## Problem 6: String Lengths (Medium)

### Solution
```python
words = ["apple", "pie", "banana", "cat", "strawberry", "dog", "kiwi"]
long_word_lengths = [len(word) for word in words if len(word) > 4]
print(long_word_lengths)
# [5, 6, 10]
```

### Explanation
- Filter words with `if len(word) > 4`
- Apply len() to get length of each filtered word
- Words selected: "apple" (5), "banana" (6), "strawberry" (10)
- Note: "kiwi" has 4 characters, not > 4, so excluded

---

## Problem 7: Temperature Conversion (Medium)

### Solution
```python
celsius = [-5, 0, 10, 20, -3, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius if temp > 0]
print(fahrenheit)
# [50.0, 68.0, 86.0, 104.0]
```

### Explanation
- Filter: `if temp > 0` excludes negative and zero temperatures
- Transform: Apply formula (C × 9/5) + 32
- Selected temps: 10, 20, 30, 40
- Results: 50°F, 68°F, 86°F, 104°F

---

## Problem 8: Extract Initials (Medium)

### Solution
```python
names = ["Alice", "Bob", "Charlie", "David"]
initials = ''.join([name[0] for name in names])
print(initials)
# "ABCD"
```

### Explanation
- List comprehension: `[name[0] for name in names]` extracts first letter
- Creates ['A', 'B', 'C', 'D']
- `''.join()` concatenates the letters into a single string
- Empty string '' means no separator between letters

**Alternative for uppercase:**
```python
initials = ''.join([name[0].upper() for name in names])
```

---

## Problem 9: Nested List Flattening (Hard)

### Solution
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Explanation
- Read like nested loops: for each row, then for each num in that row
- Equivalent to:
  ```python
  flat = []
  for row in matrix:
      for num in row:
          flat.append(num)
  ```
- First loop iterates rows: [1,2,3], [4,5,6], [7,8,9]
- Second loop iterates numbers within each row
- Collects all numbers in order

---

## Problem 10: Cartesian Product (Hard)

### Solution
```python
colors = ["red", "blue", "green"]
sizes = ["S", "M", "L"]
combinations = [(color, size) for color in colors for size in sizes]
print(combinations)
# [('red', 'S'), ('red', 'M'), ('red', 'L'),
#  ('blue', 'S'), ('blue', 'M'), ('blue', 'L'),
#  ('green', 'S'), ('green', 'M'), ('green', 'L')]
```

### Explanation
- Nested comprehension creates all possible pairs
- For each color, pair it with every size
- Equivalent to:
  ```python
  combinations = []
  for color in colors:
      for size in sizes:
          combinations.append((color, size))
  ```
- Total combinations: 3 colors × 3 sizes = 9 pairs

---

## Problem 11: Conditional Replacement (Hard)

### Solution
```python
values = [45, 120, 80, 150, 95, 200, 110]
capped = [value if value <= 100 else 100 for value in values]
print(capped)
# [45, 100, 80, 100, 95, 100, 100]
```

### Explanation
- If-else before for (conditional expression)
- If value <= 100, keep it
- If value > 100, replace with 100
- This "caps" all values at maximum of 100
- Values changed: 120→100, 150→100, 200→100, 110→100

---

## Problem 12: Remove Vowels (Hard)

### Solution
```python
text = "Hello World"
no_vowels = ''.join([char for char in text if char not in "aeiouAEIOU"])
print(no_vowels)
# "Hll Wrld"
```

### Explanation
- Filter characters: `if char not in "aeiouAEIOU"`
- Checks both lowercase and uppercase vowels
- Spaces and consonants are kept
- List created: ['H', 'l', 'l', ' ', 'W', 'r', 'l', 'd']
- Join to create string: "Hll Wrld"

---

## Problem 13: Prime Number Filter (Hard)

### Solution
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [num for num in range(2, 51) if is_prime(num)]
print(primes)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

### Explanation
- Helper function checks if number is prime
- Check divisibility from 2 to sqrt(n)
- List comprehension filters numbers using is_prime()
- Alternative without helper (less readable):
  ```python
  primes = [n for n in range(2, 51)
            if all(n % i != 0 for i in range(2, int(n**0.5)+1))]
  ```

---

## Problem 14: Dictionary Value Extraction (Hard)

### Solution
```python
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 28}
]

ages = [person["age"] for person in people if person["age"] > 25]
print(ages)
# [30, 35, 28]
```

### Explanation
- Filter: `if person["age"] > 25` selects people over 25
- Extract: `person["age"]` gets the age value
- Selected people: Alice (30), Charlie (35), David (28)
- Bob (22) excluded because 22 ≤ 25

**Alternative to get names too:**
```python
older_people = [(p["name"], p["age"]) for p in people if p["age"] > 25]
# [('Alice', 30), ('Charlie', 35), ('David', 28)]
```

---

## Problem 15: Create Multiplication Table Row (Hard)

### Solution
```python
number = 7
row = [number * i for i in range(1, 11)]
print(row)
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
```

### Explanation
- Multiply the number by each value 1-10
- Range(1, 11) gives [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
- Each multiplied by 7: 7×1, 7×2, 7×3, ... 7×10
- This is the 7 times table

**Full multiplication table (2D):**
```python
table = [[i * j for j in range(1, 11)] for i in range(1, 11)]
# Creates 10×10 multiplication table
```
