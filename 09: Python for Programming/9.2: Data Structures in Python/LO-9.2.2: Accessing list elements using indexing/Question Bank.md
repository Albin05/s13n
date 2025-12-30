## Question Bank: Accessing List Elements Using Indexing

### Q1: Basic Positive and Negative Indexing (3 minutes, Low Difficulty)

**Problem:**
Given the list `colors = ['red', 'green', 'blue', 'yellow', 'purple']`, access and print:
1. First element
2. Third element
3. Last element using positive index
4. Last element using negative index
5. Second to last element

**Expected Output:**
```
First: red
Third: blue
Last (positive): purple
Last (negative): purple
Second to last: yellow
```

**Category:** Implementation  
**Prerequisite LOs:** 9.2.1

---

### Q2: Accessing Nested List Elements (3 minutes, Low Difficulty)

**Problem:**
Given this matrix:
```python
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
```
Access and print:
1. The entire first row
2. The element at row 1, column 2
3. The center element (row 1, column 1)
4. The last element of the last row
5. The first element of the last row

**Expected Output:**
```
First row: [10, 20, 30]
Row 1, Col 2: 60
Center: 50
Last element: 90
Last row, first element: 70
```

**Category:** Implementation  
**Prerequisite LOs:** 9.2.1

---

### Q3: Safe Element Access with Error Handling (5 minutes, Medium Difficulty)

**Problem:**
Create a function `safe_access(lst, index)` that:
1. Returns the element if index is valid
2. Returns "Index out of range" if invalid
3. Test with a list `[10, 20, 30, 40, 50]` using indices: 0, 3, -1, 10, -10

**Expected Output:**
```
Index 0: 10
Index 3: 40
Index -1: 50
Index 10: Index out of range
Index -10: Index out of range
```

**Category:** Implementation  
**Prerequisite LOs:** 9.2.1

---

### Q4: Student Grade Lookup System (5 minutes, Medium Difficulty)

**Problem:**
You have two parallel lists:
```python
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
grades = [85, 92, 78, 88, 95]
```

Create a program that:
1. Takes a student name as input
2. Finds their grade
3. Displays their rank (1st, 2nd, 3rd, etc. based on position)
4. Shows if they scored above 85

Test with: 'Charlie' and 'Frank'

**Expected Output:**
```
Student: Charlie
Grade: 78
Rank: 3rd
Above 85: No

Student: Frank
Student not found
```

**Category:** Application  
**Prerequisite LOs:** 9.2.1

---

### Q5: Product Inventory Access (5 minutes, Medium Difficulty)

**Problem:**
Given this inventory (each item: [name, quantity, price]):
```python
inventory = [
    ['Laptop', 5, 999.99],
    ['Mouse', 50, 29.99],
    ['Keyboard', 30, 79.99],
    ['Monitor', 10, 299.99],
    ['USB Cable', 100, 9.99]
]
```

Write code to:
1. Display first product's details
2. Display last product's details
3. Find and display the product at position 3 (1-based)
4. Calculate total value of first product (qty × price)
5. Display all product names only

**Expected Output:**
```
First product:
  Name: Laptop
  Quantity: 5
  Price: $999.99

Last product:
  Name: USB Cable
  Quantity: 100
  Price: $9.99

Position 3: Keyboard

First product total value: $4999.95

All products: Laptop, Mouse, Keyboard, Monitor, USB Cable
```

**Category:** Application  
**Prerequisite LOs:** 9.2.1
