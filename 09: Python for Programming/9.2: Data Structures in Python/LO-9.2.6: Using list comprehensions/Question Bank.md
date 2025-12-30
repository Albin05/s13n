## Question Bank: Using List Comprehensions

### Q1: Basic List Comprehension Transformations (3 minutes, Low Difficulty)

**Problem:**
Use list comprehensions to create:
1. A list of numbers from 1 to 10
2. A list of squares of numbers from 1 to 10
3. A list of even numbers from 0 to 20
4. A list converting ['hello', 'world', 'python'] to uppercase
5. A list of lengths of words in ['apple', 'banana', 'cherry']

**Expected Output:**
```
Numbers 1-10: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Evens 0-20: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Uppercase: ['HELLO', 'WORLD', 'PYTHON']
Lengths: [5, 6, 6]
```

**Category:** Implementation
**Prerequisite LOs:** 9.2.1, 9.2.2, 9.2.3, 9.2.4, 9.2.5

---

### Q2: Filtering with Comprehensions (3 minutes, Low Difficulty)

**Problem:**
Given `numbers = [12, 7, 23, 8, 45, 16, 34, 9, 50, 3]`, use list comprehensions to create:
1. List of numbers greater than 20
2. List of numbers divisible by 4
3. List of single-digit numbers
4. List of numbers between 10 and 30 (inclusive)
5. List of odd numbers

**Expected Output:**
```
Greater than 20: [23, 45, 34, 50]
Divisible by 4: [12, 8, 16, 50]
Single digit: [7, 8, 9, 3]
Between 10-30: [12, 23, 16]
Odd numbers: [7, 23, 45, 9, 3]
```

**Category:** Implementation
**Prerequisite LOs:** 9.2.1, 9.2.2, 9.2.3, 9.2.4, 9.2.5

---

### Q3: Temperature Conversion System (5 minutes, Medium Difficulty)

**Problem:**
You have temperature readings in Celsius:
```python
celsius_temps = [0, 10, 15, 20, 25, 30, 35, 40]
```

Using list comprehensions:
1. Convert all temperatures to Fahrenheit (F = C × 9/5 + 32)
2. Create a list of temperatures in Fahrenheit that are above 77°F
3. Create a list of tuples (Celsius, Fahrenheit) for each temperature
4. Create a "comfort level" list: "Cold" if F < 60, "Comfortable" if 60 ≤ F ≤ 80, "Hot" if F > 80
5. Calculate which Celsius temperatures convert to Fahrenheit values divisible by 10

**Expected Output:**
```
Fahrenheit: [32.0, 50.0, 59.0, 68.0, 77.0, 86.0, 95.0, 104.0]
Above 77°F: [86.0, 95.0, 104.0]
C-F Pairs: [(0, 32.0), (10, 50.0), (15, 59.0), (20, 68.0), (25, 77.0), (30, 86.0), (35, 95.0), (40, 104.0)]
Comfort levels: ['Cold', 'Cold', 'Cold', 'Comfortable', 'Comfortable', 'Hot', 'Hot', 'Hot']
Divisible by 10 in F: [0°C, 20°C, 30°C]
```

**Category:** Application
**Prerequisite LOs:** 9.2.1, 9.2.2, 9.2.3, 9.2.4, 9.2.5

---

### Q4: Student Grade Processor (5 minutes, Medium Difficulty)

**Problem:**
You have student data:
```python
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank']
scores = [85, 72, 90, 65, 78, 95]
```

Use list comprehensions to create:
1. List of students who passed (score ≥ 70)
2. List of tuples (student, score) for all students
3. List of tuples (student, score) only for passing students
4. List of letter grades: A (≥90), B (≥80), C (≥70), D (≥60), F (<60)
5. List of formatted strings: "Student: Grade (Letter)"

**Expected Output:**
```
Passing students: ['Alice', 'Bob', 'Charlie', 'Eve', 'Frank']
All student-score pairs: [('Alice', 85), ('Bob', 72), ('Charlie', 90), ('Diana', 65), ('Eve', 78), ('Frank', 95)]
Passing pairs: [('Alice', 85), ('Bob', 72), ('Charlie', 90), ('Eve', 78), ('Frank', 95)]
Letter grades: ['B', 'C', 'A', 'D', 'C', 'A']
Formatted results:
  Alice: 85 (B)
  Bob: 72 (C)
  Charlie: 90 (A)
  Diana: 65 (D)
  Eve: 78 (C)
  Frank: 95 (A)
```

**Category:** Application
**Prerequisite LOs:** 9.2.1, 9.2.2, 9.2.3, 9.2.4, 9.2.5

---

### Q5: E-commerce Product Filter (5 minutes, Medium Difficulty)

**Problem:**
You have product data:
```python
products = [
    {'name': 'Laptop', 'price': 999, 'category': 'Electronics', 'stock': 5},
    {'name': 'Mouse', 'price': 29, 'category': 'Electronics', 'stock': 50},
    {'name': 'Desk', 'price': 299, 'category': 'Furniture', 'stock': 10},
    {'name': 'Chair', 'price': 199, 'category': 'Furniture', 'stock': 15},
    {'name': 'Monitor', 'price': 349, 'category': 'Electronics', 'stock': 8},
    {'name': 'Keyboard', 'price': 79, 'category': 'Electronics', 'stock': 30}
]
```

Use list comprehensions to:
1. Extract all product names
2. Get products in 'Electronics' category
3. Find products priced under $100
4. Calculate 10% discount prices for products over $200
5. Create "low stock" alert list (stock < 10) with format: "Product: X units left"

**Expected Output:**
```
Product names: ['Laptop', 'Mouse', 'Desk', 'Chair', 'Monitor', 'Keyboard']

Electronics: ['Laptop', 'Mouse', 'Monitor', 'Keyboard']

Under $100: ['Mouse', 'Keyboard']

Discounted prices (>$200):
  Laptop: $899.10
  Desk: $269.10
  Monitor: $314.10

Low stock alerts:
  Laptop: 5 units left
  Monitor: 8 units left
```

**Category:** Application
**Prerequisite LOs:** 9.2.1, 9.2.2, 9.2.3, 9.2.4, 9.2.5
