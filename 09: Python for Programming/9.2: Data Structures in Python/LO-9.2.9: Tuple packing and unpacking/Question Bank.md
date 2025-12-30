## Question Bank: Tuple Packing and Unpacking

---

### Q1: Basic Tuple Unpacking (3 minutes, Low Difficulty)

Write a program that:
1. Creates a tuple `student` with values: `('Alice', 20, 'Computer Science', 3.8)`
2. Unpacks it into variables: `name`, `age`, `major`, `gpa`
3. Prints the information in a formatted string
4. Uses unpacking to swap `age` and `gpa` values
5. Prints the swapped values

**Expected Output:**
```
Name: Alice
Age: 20
Major: Computer Science
GPA: 3.8

After swap:
Age: 3.8
GPA: 20
```

**Key Concepts:**
- Basic tuple unpacking
- Variable assignment from tuples
- Variable swapping using tuple unpacking

---

### Q2: Extended Unpacking with * Operator (3 minutes, Low Difficulty)

Write a program that:
1. Creates a tuple `scores` with test scores: `(95, 88, 92, 78, 85, 90, 87)`
2. Uses extended unpacking to extract:
   - First score into variable `first`
   - Last score into variable `last`
   - All middle scores into list `middle`
3. Calculates and prints:
   - The first and last scores
   - The average of middle scores
   - How many middle scores there are

**Expected Output:**
```
First score: 95
Last score: 87
Middle scores: [88, 92, 78, 85, 90]
Number of middle scores: 5
Average of middle scores: 86.6
```

**Key Concepts:**
- Extended unpacking with *
- Collecting remaining elements
- Processing unpacked data

---

### Q3: Data Transformation System (5 minutes, Medium Difficulty)

Write a program that processes coordinate transformations:

1. Create a list of 2D points: `[(0, 0), (3, 4), (6, 8), (1, 2)]`

2. Write a function `translate_point(point, dx, dy)` that:
   - Unpacks the point coordinates
   - Returns new coordinates translated by dx, dy

3. Write a function `scale_point(point, factor)` that:
   - Unpacks the point coordinates
   - Returns new coordinates scaled by factor

4. Write a function `reflect_point(point)` that:
   - Unpacks the point coordinates
   - Returns point reflected over y-axis (x becomes -x)

5. For each original point:
   - Translate by (5, 5)
   - Scale by 2
   - Reflect
   - Print original and final coordinates

**Expected Output:**
```
Original: (0, 0) → Translated: (5, 5) → Scaled: (10, 10) → Reflected: (-10, 10)
Original: (3, 4) → Translated: (8, 9) → Scaled: (16, 18) → Reflected: (-16, 18)
Original: (6, 8) → Translated: (11, 13) → Scaled: (22, 26) → Reflected: (-22, 26)
Original: (1, 2) → Translated: (6, 7) → Scaled: (12, 14) → Reflected: (-12, 14)
```

**Key Concepts:**
- Unpacking in function parameters
- Packing return values
- Chaining transformations
- Loop unpacking

---

### Q4: Student Grade Analyzer (5 minutes, Medium Difficulty)

Write a program that analyzes student grades:

1. Create a list of student records (tuples):
   ```python
   students = [
       ('Alice', 85, 90, 88, 92),
       ('Bob', 78, 82, 75, 80),
       ('Charlie', 92, 95, 93, 90),
       ('Diana', 88, 85, 90, 87)
   ]
   ```

2. Write a function `analyze_student(student)` that:
   - Unpacks name and all test scores
   - Calculates average, highest, and lowest scores
   - Returns tuple: `(name, average, highest, lowest, passed)`
     - `passed` is True if average >= 85, False otherwise

3. Process all students and print:
   - Each student's analysis
   - Names of students who passed
   - Class average

**Expected Output:**
```
Alice: Avg=88.75, High=92, Low=85, Status=PASS
Bob: Avg=78.75, High=82, Low=75, Status=FAIL
Charlie: Avg=92.50, High=95, Low=90, Status=PASS
Diana: Avg=87.50, High=90, Low=85, Status=PASS

Students who passed: Alice, Charlie, Diana
Class average: 86.88
```

**Key Concepts:**
- Unpacking variable-length tuples
- Extended unpacking with *
- Packing function returns
- Loop unpacking
- Data aggregation

---

### Q5: CSV Data Processor (5 minutes, Medium Difficulty)

Write a program that processes CSV-like data:

1. Create a list of CSV strings representing employees:
   ```python
   csv_data = [
       "101,Alice,Engineering,95000,5",
       "102,Bob,Marketing,75000,3",
       "103,Charlie,Engineering,105000,7",
       "104,Diana,HR,65000,2",
       "105,Eve,Engineering,98000,4"
   ]
   ```

2. Write a function `parse_employee(csv_string)` that:
   - Splits the CSV string
   - Unpacks into: id, name, department, salary, years
   - Converts numeric values to appropriate types
   - Returns a tuple: `(id, name, department, salary, years)`

3. Write a function `calculate_bonus(employee)` that:
   - Unpacks employee tuple
   - Calculates bonus:
     - Base: 5% of salary
     - Add 1% per year of service
     - Engineers get additional 2%
   - Returns tuple: `(name, bonus)`

4. Process all employees and print:
   - Each employee's bonus
   - Total bonus budget
   - Department with highest total bonuses

**Expected Output:**
```
Alice (Engineering, 5 years): Bonus = $11400.00
Bob (Marketing, 3 years): Bonus = $6000.00
Charlie (Engineering, 7 years): Bonus = $14700.00
Diana (HR, 2 years): Bonus = $4550.00
Eve (Engineering, 4 years): Bonus = $10780.00

Total bonus budget: $47430.00
Department with highest bonuses: Engineering ($36880.00)
```

**Key Concepts:**
- String parsing and unpacking
- Type conversion after unpacking
- Packing and unpacking in functions
- Complex data processing
- Aggregation by category
- Extended unpacking for flexible data handling

**Bonus Challenge:**
Modify the program to handle employees with optional fields (some may have fewer than 5 fields) using extended unpacking.

---

### Additional Practice Problems

**Practice 1: Fibonacci with Unpacking**
Write a function that generates the first n Fibonacci numbers using tuple unpacking for state updates.

**Practice 2: Matrix Operations**
Create functions for matrix addition and multiplication that use unpacking to process row and column data.

**Practice 3: Dictionary Unpacking**
Write a function that accepts `**kwargs` and uses unpacking to process configuration options with defaults.

**Practice 4: Nested Unpacking**
Process a list of nested tuples representing hierarchical data (e.g., `('Department', [('Team', [('Employee', )]))]`)

**Practice 5: Zip and Unpack**
Combine multiple lists using zip and unpack in a loop to process parallel data streams.
