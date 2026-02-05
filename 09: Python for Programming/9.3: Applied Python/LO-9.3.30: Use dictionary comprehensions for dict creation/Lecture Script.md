# Lecture Script: LO-72 Use Dictionary Comprehensions

## [0:00-0:02] Hook (2 min)
**Say**: "You love list comprehensions? Wait till you see dictionary comprehensions! Create dictionaries in one line with the same elegant syntax. Traditional way: 5 lines. Python way: 1 line! Let me blow your mind!"

**Demo**:
```python
# Traditional way - tedious!
squares = {}
for i in range(6):
    squares[i] = i ** 2
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dictionary comprehension - beautiful!
squares = {i: i ** 2 for i in range(6)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

**Say**: "Same result, one line! Let's master dictionary comprehensions!"

## [0:02-0:06] Basic Syntax (4 min)

**Say**: "Dict comprehension syntax: {key: value for item in iterable}. Just like list comprehension but with curly braces and key-value pairs!"

**Live Code**:
```python
# Pattern: {key_expression: value_expression for item in sequence}

# Example 1: Number to square mapping
squares = {n: n ** 2 for n in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Example 2: Name to length mapping
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {'Alice': 5, 'Bob': 3, 'Charlie': 7}

# Example 3: Create from two lists using zip
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined = {k: v for k, v in zip(keys, values)}
print(combined)  # {'a': 1, 'b': 2, 'c': 3}

# Example 4: Index mapping
fruits = ["apple", "banana", "cherry"]
fruit_index = {fruit: i for i, fruit in enumerate(fruits)}
print(fruit_index)  # {'apple': 0, 'banana': 1, 'cherry': 2}
```

**Point out**: "Read it like: 'Create a dict with {key: value} FOR each item IN sequence'."

**Emphasize**: "Use curly braces {}, not square brackets [], and separate key from value with a colon!"

## [0:06-0:10] Dictionary Comprehensions with Filters (4 min)

**Say**: "Add 'if' to filter which items get included. Pattern: {key: value for item in iterable if condition}"

**Live Code**:
```python
# Filter by value
prices = {"apple": 0.5, "banana": 0.3, "orange": 0.8, "grape": 1.2}
expensive = {fruit: price for fruit, price in prices.items() if price > 0.5}
print(expensive)  # {'orange': 0.8, 'grape': 1.2}

# Filter by key
long_names = {fruit: price for fruit, price in prices.items() if len(fruit) > 5}
print(long_names)  # {'banana': 0.3, 'orange': 0.8}

# Filter even numbers only
evens = {n: n ** 2 for n in range(10) if n % 2 == 0}
print(evens)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Filter and transform
students = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
passed = {name: grade for name, grade in students.items() if grade >= 80}
print(passed)  # {'Alice': 85, 'Bob': 92, 'Diana': 95}
```

**Say**: "The 'if' at the end FILTERS which items get into the dictionary!"

**Point out**: "Use .items() to iterate through both keys and values of an existing dict!"

## [0:10-0:14] Transforming Keys and Values (4 min)

**Say**: "You can transform both keys and values during comprehension!"

**Live Code**:
```python
# Transform values only
prices = {"apple": 0.5, "banana": 0.3, "orange": 0.8}
double_prices = {fruit: price * 2 for fruit, price in prices.items()}
print(double_prices)  # {'apple': 1.0, 'banana': 0.6, 'orange': 1.6}

# Transform keys only
upper_keys = {fruit.upper(): price for fruit, price in prices.items()}
print(upper_keys)  # {'APPLE': 0.5, 'BANANA': 0.3, 'ORANGE': 0.8}

# Transform both
formatted = {fruit.upper(): f"${price:.2f}" for fruit, price in prices.items()}
print(formatted)  # {'APPLE': '$0.50', 'BANANA': '$0.30', 'ORANGE': '$0.80'}

# Swap keys and values
grades = {"Alice": "A", "Bob": "B", "Charlie": "A"}
grade_to_students = {grade: name for name, grade in grades.items()}
print(grade_to_students)  # {'A': 'Charlie', 'B': 'Bob'}
# Warning: Last value wins if duplicate keys!

# Better: Group by value (we'll learn this later)
from collections import defaultdict
grouped = defaultdict(list)
for name, grade in grades.items():
    grouped[grade].append(name)
print(dict(grouped))  # {'A': ['Alice', 'Charlie'], 'B': ['Bob']}
```

**Point out**: "When swapping, be careful of duplicate keys — last one wins!"

## [0:14-0:18] Real-World Examples (4 min)

**Say**: "Let's see dictionary comprehensions solving real problems!"

**Live Code**:
```python
# Example 1: Student grade processing
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "Diana", "score": 95}
]

# Create name to score mapping
scores = {s["name"]: s["score"] for s in students}
print(scores)  # {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95}

# Convert scores to letter grades
def get_letter(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    return "F"

letter_grades = {name: get_letter(score) for name, score in scores.items()}
print(letter_grades)  # {'Alice': 'B', 'Bob': 'A', 'Charlie': 'C', 'Diana': 'A'}

# Example 2: Temperature conversion
temps_f = {"Monday": 68, "Tuesday": 72, "Wednesday": 65, "Thursday": 70}
temps_c = {day: round((temp - 32) * 5/9, 1) for day, temp in temps_f.items()}
print(temps_c)  # {'Monday': 20.0, 'Tuesday': 22.2, 'Wednesday': 18.3, 'Thursday': 21.1}

# Example 3: Word frequency
text = "the quick brown fox jumps over the lazy dog the fox"
words = text.split()
word_freq = {word: words.count(word) for word in set(words)}
print(word_freq)  # {'the': 3, 'quick': 1, 'brown': 1, 'fox': 2, ...}

# Example 4: Product inventory
products = [
    {"id": "P001", "name": "Laptop", "price": 999},
    {"id": "P002", "name": "Mouse", "price": 25},
    {"id": "P003", "name": "Keyboard", "price": 75}
]

# ID to product mapping
inventory = {p["id"]: {"name": p["name"], "price": p["price"]} for p in products}
print(inventory)
# {'P001': {'name': 'Laptop', 'price': 999}, ...}
```

**Say**: "Notice how clean and readable these are compared to traditional for loops!"

## [0:18-0:21] Conditional Expressions (3 min)

**Say**: "Just like list comprehensions, you can use if-else to transform values conditionally!"

**Live Code**:
```python
# Pattern: {key: value_if_true if condition else value_if_false for item in iterable}

# Label numbers as even or odd
numbers = range(10)
parity = {n: "even" if n % 2 == 0 else "odd" for n in numbers}
print(parity)
# {0: 'even', 1: 'odd', 2: 'even', 3: 'odd', ...}

# Apply discount to expensive items
prices = {"laptop": 999, "mouse": 25, "monitor": 299, "keyboard": 75}
discounted = {
    item: price * 0.9 if price > 100 else price
    for item, price in prices.items()
}
print(discounted)
# {'laptop': 899.1, 'mouse': 25, 'monitor': 269.1, 'keyboard': 75}

# Classify students by performance
students = {"Alice": 92, "Bob": 85, "Charlie": 78, "Diana": 95}
performance = {
    name: "Excellent" if score >= 90 else "Good" if score >= 80 else "Average"
    for name, score in students.items()
}
print(performance)
# {'Alice': 'Excellent', 'Bob': 'Good', 'Charlie': 'Average', 'Diana': 'Excellent'}

# Create color codes
colors = ["red", "green", "blue"]
color_codes = {
    color: "#FF0000" if color == "red"
    else "#00FF00" if color == "green"
    else "#0000FF"
    for color in colors
}
print(color_codes)
# {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}
```

**Emphasize**: "if-else BEFORE for transforms values. if AFTER for filters items!"

## [0:21-0:23] Practice Challenge (2 min)

**Challenge**: "Given a list of words, create a dict mapping each word to its length, but only for words longer than 4 characters."

**Skeleton**:
```python
words = ["hi", "python", "is", "awesome", "and", "powerful"]

# TODO: Create dict with word: length, only if len(word) > 4
word_lengths = {}  # Use dict comprehension!

print(word_lengths)  # Should be {'python': 6, 'awesome': 7, 'powerful': 8}
```

**Give them 1-2 minutes**

**Solution**:
```python
word_lengths = {word: len(word) for word in words if len(word) > 4}
print(word_lengths)  # {'python': 6, 'awesome': 7, 'powerful': 8}
```

**Bonus challenge**:
```python
# Uppercase the words as keys
word_lengths = {word.upper(): len(word) for word in words if len(word) > 4}
print(word_lengths)  # {'PYTHON': 6, 'AWESOME': 7, 'POWERFUL': 8}
```

## [0:23-0:25] Wrap-up (2 min)

**Key Points**:
1. **Basic syntax**: `{key: value for item in iterable}`
2. **With filter**: `{key: value for item in iterable if condition}`
3. **With transform**: `{key: value_if_true if condition else value_if_false for item in iterable}`
4. **From two lists**: Use `zip()` to combine keys and values
5. **Always returns a dict** — use curly braces {}

**Common Mistakes**:
- Using square brackets [] instead of curly braces {}
- Forgetting the colon between key and value
- Duplicate keys — last one wins, earlier values are lost
- Making comprehensions too complex — readability matters
- Confusing filter (if after for) vs transform (if-else before for)

**When to Use Dictionary Comprehensions**:
- Creating mappings from sequences
- Transforming existing dictionaries
- Filtering dictionaries
- Inverting key-value pairs
- When it improves readability

**When NOT to Use**:
- Complex logic that's hard to read
- When you need to handle duplicate keys carefully
- When side effects are needed
- When a regular for loop would be clearer

**Performance Note**: "Dict comprehensions are faster than traditional dict creation with loops!"

**Dict Comprehensions vs List Comprehensions**:
- **List**: `[expression for item in iterable]` → returns list
- **Dict**: `{key: value for item in iterable}` → returns dict
- **Set**: `{expression for item in iterable}` → returns set (no duplicate values)

**Closing**: "Dictionary comprehensions are incredibly powerful for data transformation! They make your code concise, readable, and Pythonic. Master them along with list comprehensions, and you'll write professional Python code. Remember: keep them simple — if it's getting hard to read, break it into multiple steps!"
