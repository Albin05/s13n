## Question Bank: Creating and Initializing Dictionaries

---

### Q1: Basic Dictionary Creation (3 minutes, Low Difficulty)

Create dictionaries using three different methods:
1. Using curly braces: a `book` dict with keys `title`, `author`, `year`, `pages`
2. Using `dict()`: a `settings` dict with keys `theme`, `language`, `notifications`
3. Using `dict.fromkeys()`: a `scores` dict with keys `Math`, `Science`, `English` all set to 0

Print each dictionary.

**Expected Output:**
```
book: {'title': 'Python Crash Course', 'author': 'Eric Matthes', 'year': 2019, 'pages': 544}
settings: {'theme': 'dark', 'language': 'en', 'notifications': True}
scores: {'Math': 0, 'Science': 0, 'English': 0}
```

**Key Concepts:** Multiple dictionary creation methods

---

### Q2: Dictionary from Two Lists (3 minutes, Low Difficulty)

Given two lists:
```python
countries = ['India', 'Japan', 'Brazil', 'Germany', 'Australia']
capitals = ['New Delhi', 'Tokyo', 'Brasilia', 'Berlin', 'Canberra']
```

1. Create a dictionary mapping countries to capitals using `zip()`
2. Print the dictionary
3. Create the reverse mapping (capitals → countries) using a comprehension

**Expected Output:**
```
Countries to capitals: {'India': 'New Delhi', 'Japan': 'Tokyo', ...}
Capitals to countries: {'New Delhi': 'India', 'Tokyo': 'Japan', ...}
```

**Key Concepts:** `zip()` with `dict()`, dictionary comprehension

---

### Q3: Student Grade Book (5 minutes, Medium Difficulty)

Create a nested dictionary representing a grade book:

```python
# Structure: {student_name: {subject: grade}}
```

1. Create entries for 3 students with 3 subjects each
2. Print each student's grades
3. Calculate and print each student's average grade
4. Find the student with the highest average

**Expected Output:**
```
Alice: {'Math': 92, 'Science': 88, 'English': 95}
Bob: {'Math': 78, 'Science': 85, 'English': 80}
Charlie: {'Math': 95, 'Science': 92, 'English': 88}

Alice average: 91.67
Bob average: 81.00
Charlie average: 91.67
Top student: Alice (or Charlie, tied at 91.67)
```

**Key Concepts:** Nested dictionaries, iteration, calculations

---

### Q4: Word Frequency with Comprehension (5 minutes, Medium Difficulty)

Given a paragraph:
```python
text = "python is great and python is fun and learning python is the best way to learn programming and programming is fun"
```

1. Build a word frequency dictionary using a loop
2. Build a dictionary of words that appear more than once (using comprehension)
3. Build a dictionary of word lengths (word → length) for unique words
4. Find the most frequent word

**Expected Output:**
```
Frequencies: {'python': 3, 'is': 4, 'great': 1, 'and': 3, ...}
Repeated words: {'python': 3, 'is': 4, 'and': 3, 'fun': 2, 'programming': 2}
Word lengths: {'python': 6, 'is': 2, 'great': 5, ...}
Most frequent: 'is' (4 times)
```

**Key Concepts:** Building dicts from data, comprehension filtering, `max()`

---

### Q5: Inventory System (5 minutes, Medium Difficulty)

Create an inventory system using dictionaries:

```python
# Each product: {name: {'price': float, 'quantity': int, 'category': str}}
```

1. Create an inventory with at least 5 products across 2+ categories
2. Write a function `total_value(inventory)` — sum of price × quantity for all products
3. Write a function `by_category(inventory)` — returns `{category: [product_names]}`
4. Write a function `low_stock(inventory, threshold)` — returns products below threshold
5. Print results for all three functions

**Expected Output:**
```
Total inventory value: $X,XXX.XX
By category: {'electronics': ['laptop', 'phone'], 'food': ['rice', 'bread'], ...}
Low stock (< 5): {'bread': 3, 'phone': 2}
```

**Key Concepts:** Nested dicts, iteration, building new dicts from existing ones
