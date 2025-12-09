# Editorials: Use Dictionary Comprehensions

## Problem 1: Number Squares Dictionary

```python
# Create dictionary with numbers 1-10 and their squares
squares = {i: i ** 2 for i in range(1, 11)}
print(squares)
```

### Explanation
The dictionary comprehension iterates through numbers 1 to 10 (inclusive) using `range(1, 11)`. For each number `i`, it creates a key-value pair where the key is `i` and the value is `i ** 2` (the square).

**Time Complexity:** O(n) where n is 10
**Space Complexity:** O(n) for the output dictionary

---

## Problem 2: Name and Age Mapping

```python
names = ["Alice", "Bob", "Charlie", "Diana"]
ages = [25, 30, 35, 28]

# Create dictionary mapping names to ages
people = {name: age for name, age in zip(names, ages)}
print(people)
```

### Explanation
The `zip(names, ages)` function pairs each name with its corresponding age. The dictionary comprehension then creates key-value pairs from these tuples. The unpacking `name, age` extracts elements from each tuple.

**Time Complexity:** O(n) where n is the length of the lists
**Space Complexity:** O(n) for the output dictionary

---

## Problem 3: Filter Products by Price

```python
products = {
    "laptop": 999,
    "mouse": 25,
    "keyboard": 75,
    "monitor": 299,
    "cable": 15,
    "headphones": 89
}

# Filter products with price > 50
expensive = {product: price for product, price in products.items() if price > 50}
print(expensive)
```

### Explanation
The dictionary comprehension iterates through `products.items()` which returns tuples of (key, value). The condition `if price > 50` filters only products with price greater than 50. The result is a new dictionary with only those products.

**Time Complexity:** O(n) where n is the number of products
**Space Complexity:** O(k) where k is the number of products matching the condition

---

## Problem 4: Grade Letter Converter

```python
scores = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 78,
    "Diana": 95,
    "Eve": 67,
    "Frank": 55
}

# Helper function to convert score to letter grade
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Convert scores to letter grades
letter_grades = {name: get_letter_grade(score) for name, score in scores.items()}
print(letter_grades)
```

### Explanation
1. Define a helper function `get_letter_grade()` that takes a numeric score and returns the corresponding letter grade
2. Use dictionary comprehension to iterate through `scores.items()`
3. For each name-score pair, apply the helper function to convert the score to a letter
4. Create a new dictionary with names as keys and letter grades as values

**Alternative solution without helper function:**
```python
letter_grades = {
    name: "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
    for name, score in scores.items()
}
print(letter_grades)
```

**Time Complexity:** O(n) where n is the number of students
**Space Complexity:** O(n) for the output dictionary

---

## Problem 5: Nested Dictionary - Character Frequency

```python
words = ["hello", "world", "python"]

# Create nested dictionary with character frequencies
char_freq = {
    word: {char: word.count(char) for char in set(word)}
    for word in words
}
print(char_freq)

# Alternative with sorted characters
char_freq_sorted = {
    word: {char: word.count(char) for char in sorted(set(word))}
    for word in words
}
print("\nWith sorted characters:")
print(char_freq_sorted)
```

### Explanation
This uses a nested dictionary comprehension:

1. **Outer comprehension:** `for word in words`
   - Iterates through each word in the list
   - Creates a key for each word

2. **Inner comprehension:** `{char: word.count(char) for char in set(word)}`
   - `set(word)` gets unique characters in the word
   - For each unique character, counts its occurrences using `word.count(char)`
   - Creates a dictionary of character frequencies

For example, for "hello":
- `set("hello")` gives `{'h', 'e', 'l', 'o'}`
- Count each: h=1, e=1, l=2, o=1
- Result: `{'h': 1, 'e': 1, 'l': 2, 'o': 1}`

**More efficient solution using Counter:**
```python
from collections import Counter

words = ["hello", "world", "python"]
char_freq = {word: dict(Counter(word)) for word in words}
print(char_freq)
```

**Time Complexity:** O(n * m * k) where n is number of words, m is average word length, and k is unique characters per word (due to count operations)
**Space Complexity:** O(n * k) for the nested dictionary

**Note:** The `count()` method scans the entire string for each character, which is inefficient. Using `Counter` is more efficient as it scans the string only once.
