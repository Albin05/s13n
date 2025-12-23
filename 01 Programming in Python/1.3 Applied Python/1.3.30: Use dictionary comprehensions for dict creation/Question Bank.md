# Question Bank: Use Dictionary Comprehensions

## Problem 1 (Easy)

**Title:** Number Squares Dictionary

**Problem Statement:**
Create a dictionary where keys are numbers from 1 to 10 and values are their squares using dictionary comprehension.

**Input Format:**
No input required.

**Output Format:**
Print the dictionary.

**Sample Output:**
```
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
```

**Constraints:**
- Use dictionary comprehension
- Numbers from 1 to 10 inclusive

---

## Problem 2 (Easy)

**Title:** Name and Age Mapping

**Problem Statement:**
Given two lists - one with names and one with ages - create a dictionary that maps each name to its corresponding age using dictionary comprehension.

**Input Format:**
Two lists are provided in the code.

**Output Format:**
Print the dictionary.

**Sample Input:**
```python
names = ["Alice", "Bob", "Charlie", "Diana"]
ages = [25, 30, 35, 28]
```

**Sample Output:**
```
{'Alice': 25, 'Bob': 30, 'Charlie': 35, 'Diana': 28}
```

**Constraints:**
- Use dictionary comprehension with zip()
- Both lists have the same length

---

## Problem 3 (Medium)

**Title:** Filter Products by Price

**Problem Statement:**
Given a dictionary of products and prices, create a new dictionary containing only products that cost more than $50 using dictionary comprehension.

**Input Format:**
A dictionary of products and prices is provided.

**Output Format:**
Print the filtered dictionary.

**Sample Input:**
```python
products = {
    "laptop": 999,
    "mouse": 25,
    "keyboard": 75,
    "monitor": 299,
    "cable": 15,
    "headphones": 89
}
```

**Sample Output:**
```
{'laptop': 999, 'keyboard': 75, 'monitor': 299, 'headphones': 89}
```

**Constraints:**
- Use dictionary comprehension with condition
- Filter by price > 50

---

## Problem 4 (Medium)

**Title:** Grade Letter Converter

**Problem Statement:**
Given a dictionary of student names and their numeric scores, create a new dictionary with names and letter grades using dictionary comprehension. Use this grading scale: A (90+), B (80-89), C (70-79), D (60-69), F (below 60).

**Input Format:**
A dictionary of student scores is provided.

**Output Format:**
Print the dictionary with letter grades.

**Sample Input:**
```python
scores = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 78,
    "Diana": 95,
    "Eve": 67,
    "Frank": 55
}
```

**Sample Output:**
```
{'Alice': 'A', 'Bob': 'B', 'Charlie': 'C', 'Diana': 'A', 'Eve': 'D', 'Frank': 'F'}
```

**Constraints:**
- Use dictionary comprehension
- Apply correct grading scale
- Define a helper function for grade conversion

---

## Problem 5 (Hard)

**Title:** Nested Dictionary - Character Frequency

**Problem Statement:**
Given a list of words, create a nested dictionary where each word is a key, and its value is another dictionary containing the frequency of each character in that word. Use dictionary comprehension.

**Input Format:**
A list of words is provided.

**Output Format:**
Print the nested dictionary.

**Sample Input:**
```python
words = ["hello", "world", "python"]
```

**Sample Output:**
```
{
    'hello': {'h': 1, 'e': 1, 'l': 2, 'o': 1},
    'world': {'w': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1},
    'python': {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}
}
```

**Constraints:**
- Use nested dictionary comprehension
- Count character frequency for each word
- Maintain alphabetical order of characters (optional)

**Hint:**
You'll need a nested dictionary comprehension: the outer one for words, and the inner one for character frequencies in each word.
