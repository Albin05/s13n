## Question Bank: Creating and Initializing Lists in Python

### Q1: Create Different Types of Lists (3 minutes, Low Difficulty)

**Problem:**
Create the following lists and print each one:
1. Empty list
2. List of integers from 1 to 5
3. List of three strings: "red", "green", "blue"
4. List of three floats: 1.5, 2.5, 3.5
5. Mixed list with a string, integer, float, and boolean

**Expected Output:**
```
Empty list: []
Integers: [1, 2, 3, 4, 5]
Colors: ['red', 'green', 'blue']
Floats: [1.5, 2.5, 3.5]
Mixed: ['Python', 42, 3.14, True]
```

**Category:** Implementation  
**Prerequisite LOs:** 9.1.1, 9.1.2

---

### Q2: Create Lists from Range and String (3 minutes, Low Difficulty)

**Problem:**
1. Create a list of numbers from 0 to 9 using range()
2. Create a list of even numbers from 2 to 20 using range()
3. Convert the string "PYTHON" to a list of characters
4. Split the sentence "I love programming" into a list of words

**Expected Output:**
```
Numbers 0-9: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Even numbers 2-20: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Characters: ['P', 'Y', 'T', 'H', 'O', 'N']
Words: ['I', 'love', 'programming']
```

**Category:** Implementation  
**Prerequisite LOs:** 9.1.1, 9.1.2

---

### Q3: Create and Work with Nested Lists (5 minutes, Medium Difficulty)

**Problem:**
Create a 3x3 matrix (nested list) representing a tic-tac-toe board with the following layout:
```
X | O | X
---------
O | X | O
---------
X | O | X
```
Then:
1. Print the entire board
2. Print the center element
3. Print the top row
4. Print the bottom-right element

**Expected Output:**
```
Board: [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]
Center: X
Top row: ['X', 'O', 'X']
Bottom-right: X
```

**Category:** Implementation  
**Prerequisite LOs:** 9.1.1, 9.1.2

---

### Q4: Student Grade Management (5 minutes, Medium Difficulty)

**Problem:**
Create a list to store information for 4 students. Each student should be a nested list containing: [name, math_grade, science_grade, english_grade].

Students:
- Alice: 85, 90, 88
- Bob: 78, 82, 86  
- Charlie: 92, 89, 94
- Diana: 88, 91, 87

Then:
1. Print all students
2. Calculate and print the average for each student
3. Find the student with the highest math grade

**Expected Output:**
```
All students:
[['Alice', 85, 90, 88], ['Bob', 78, 82, 86], ['Charlie', 92, 89, 94], ['Diana', 88, 91, 87]]

Student Averages:
Alice: 87.67
Bob: 82.00
Charlie: 91.67
Diana: 88.67

Highest math grade: Charlie with 92
```

**Category:** Application  
**Prerequisite LOs:** 9.1.1, 9.1.2

---

### Q5: Shopping Cart System (5 minutes, Medium Difficulty)

**Problem:**
Create a shopping cart system where each item is represented as a list: [product_name, price, quantity].

Add these items to the cart:
- Laptop: $999.99, quantity 1
- Mouse: $29.99, quantity 2
- Keyboard: $79.99, quantity 1
- USB Cable: $9.99, quantity 3

Calculate and display:
1. Total number of unique items
2. Total number of individual products (sum of quantities)
3. Subtotal for each item (price × quantity)
4. Grand total

**Expected Output:**
```
Shopping Cart:
Item 1: Laptop - $999.99 x 1 = $999.99
Item 2: Mouse - $29.99 x 2 = $59.98
Item 3: Keyboard - $79.99 x 1 = $79.99
Item 4: USB Cable - $9.99 x 3 = $29.97

Unique items: 4
Total products: 7
Grand Total: $1169.93
```

**Category:** Application  
**Prerequisite LOs:** 9.1.1, 9.1.2
