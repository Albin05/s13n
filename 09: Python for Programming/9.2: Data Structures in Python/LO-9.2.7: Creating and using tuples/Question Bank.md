## Question Bank: Creating and Using Tuples

### Q1: Basic Tuple Creation and Access (3 minutes, Low Difficulty)

**Problem:**
Create and manipulate tuples:
1. Create a tuple with numbers 10, 20, 30, 40, 50
2. Access the first and last elements
3. Get a slice from index 1 to 3
4. Create a single-element tuple with value 100
5. Convert the list [1, 2, 3] to a tuple

**Expected Output:**
```
Tuple: (10, 20, 30, 40, 50)
First: 10
Last: 50
Slice [1:3]: (20, 30)
Single element: (100,)
From list: (1, 2, 3)
```

**Category:** Implementation
**Prerequisite LOs:** 9.2.1, 9.2.2, 9.2.3

---

### Q2: Tuple Methods and Operations (3 minutes, Low Difficulty)

**Problem:**
Given `numbers = (5, 10, 15, 10, 20, 10, 25)`:
1. Count how many times 10 appears
2. Find the index of the first occurrence of 15
3. Find the index of the second occurrence of 10 (hint: use start parameter)
4. Check if 20 is in the tuple
5. Calculate the sum and length of the tuple

**Expected Output:**
```
Count of 10: 3
Index of 15: 2
Second occurrence of 10 at index: 3
20 in tuple: True
Sum: 105
Length: 7
```

**Category:** Implementation
**Prerequisite LOs:** 9.2.1, 9.2.2, 9.2.3

---

### Q3: Coordinate System (5 minutes, Medium Difficulty)

**Problem:**
Create a coordinate system using tuples:

1. Define points as tuples: origin (0, 0), point_a (3, 4), point_b (-2, 5)
2. Write a function `distance_from_origin(point)` that calculates distance using: √(x² + y²)
3. Write a function `translate_point(point, dx, dy)` that returns new point (x+dx, y+dy)
4. Create a list of 5 random points (as tuples)
5. Find which point is farthest from origin

Print all results with clear labels.

**Expected Output:**
```
Origin: (0, 0)
Point A: (3, 4)
Point B: (-2, 5)

Distance from origin:
  Point A: 5.0
  Point B: 5.39

Translate Point A by (2, -1): (5, 3)

Random points: [(1, 2), (4, 1), (-3, 2), (2, -4), (5, 5)]
Farthest point: (5, 5) at distance 7.07
```

**Category:** Application
**Prerequisite LOs:** 9.2.1, 9.2.2, 9.2.3

---

### Q4: RGB Color Manager (5 minutes, Medium Difficulty)

**Problem:**
Create a color management system using tuples for RGB values:

```python
colors = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'yellow': (255, 255, 0),
    'cyan': (0, 255, 255),
    'magenta': (255, 0, 255)
}
```

Implement:
1. Function `brightness(rgb)` that returns average of R, G, B values
2. Function `invert_color(rgb)` that returns (255-R, 255-G, 255-B)
3. Find the brightest and darkest colors
4. Create a list of all colors with brightness > 150
5. Invert all primary colors (red, green, blue)

**Expected Output:**
```
Color brightness:
  red: 85.0
  green: 85.0
  blue: 85.0
  white: 255.0
  black: 0.0
  yellow: 170.0
  cyan: 170.0
  magenta: 170.0

Brightest: white (255.0)
Darkest: black (0.0)

Bright colors (>150): ['white', 'yellow', 'cyan', 'magenta']

Inverted colors:
  red (255, 0, 0) → (0, 255, 255)
  green (0, 255, 0) → (255, 0, 255)
  blue (0, 0, 255) → (255, 255, 0)
```

**Category:** Application
**Prerequisite LOs:** 9.2.1, 9.2.2, 9.2.3

---

### Q5: Student Records System (5 minutes, Medium Difficulty)

**Problem:**
Create a student management system using tuples for immutable student records:

```python
# Each record: (id, name, age, grade, gpa)
students = [
    (101, 'Alice', 20, 'A', 3.8),
    (102, 'Bob', 21, 'B', 3.2),
    (103, 'Charlie', 19, 'A', 3.9),
    (104, 'Diana', 20, 'C', 2.8),
    (105, 'Eve', 22, 'B', 3.5)
]
```

Implement:
1. Function `find_by_id(students, student_id)` that returns student tuple
2. Function `get_honors_students(students)` for GPA ≥ 3.5
3. Calculate average GPA of all students
4. Create a dictionary mapping student IDs to names
5. Find the youngest and oldest students

**Expected Output:**
```
Student 103: (103, 'Charlie', 19, 'A', 3.9)

Honors students (GPA ≥ 3.5):
  Alice: 3.8
  Charlie: 3.9
  Eve: 3.5

Average GPA: 3.44

ID to Name mapping:
  {101: 'Alice', 102: 'Bob', 103: 'Charlie', 104: 'Diana', 105: 'Eve'}

Youngest: Charlie (19 years)
Oldest: Eve (22 years)
```

**Category:** Application
**Prerequisite LOs:** 9.2.1, 9.2.2, 9.2.3
