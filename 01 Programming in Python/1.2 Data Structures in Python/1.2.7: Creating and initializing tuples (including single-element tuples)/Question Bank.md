# Question Bank: Creating and Initializing Tuples (Including Single-Element Tuples)

## Problem 1: Create Student Record (Easy)
Create a tuple called `student` that stores a student's name ("Alice"), age (20), and major ("Computer Science"). Print the tuple and verify its type.

**Expected Output:**
```
('Alice', 20, 'Computer Science')
<class 'tuple'>
```

**Hint:** Use parentheses and commas to create the tuple.

---

## Problem 2: Single Lucky Number (Easy)
Create a single-element tuple containing your lucky number (7). Verify it's actually a tuple by printing its type.

**Expected Output:**
```
(7,)
<class 'tuple'>
```

**Hint:** Don't forget the trailing comma!

---

## Problem 3: RGB Color Creator (Easy)
Create three tuples representing RGB colors:
- red: (255, 0, 0)
- green: (0, 255, 0)
- blue: (0, 0, 255)

Print all three colors.

**Expected Output:**
```
Red: (255, 0, 0)
Green: (0, 255, 0)
Blue: (0, 0, 255)
```

**Hint:** Each tuple should have three integer values.

---

## Problem 4: Convert List to Tuple (Easy)
Given the list `numbers = [1, 2, 3, 4, 5]`, convert it to a tuple and print the result.

**Expected Output:**
```
(1, 2, 3, 4, 5)
```

**Hint:** Use the `tuple()` constructor.

---

## Problem 5: Tuple Unpacking Basics (Easy)
Create a tuple `coordinates = (10, 20)` and unpack it into variables `x` and `y`. Print both variables.

**Expected Output:**
```
X: 10
Y: 20
```

**Hint:** Use multiple assignment: `x, y = coordinates`

---

## Problem 6: Swap Two Variables (Medium)
Write code that swaps the values of two variables `a = 5` and `b = 10` using tuple unpacking. Print the values before and after swapping.

**Expected Output:**
```
Before: a = 5, b = 10
After: a = 10, b = 5
```

**Hint:** Use the pattern `a, b = b, a`

---

## Problem 7: Create Tuple from String (Medium)
Create a tuple from the string "Python" where each character becomes a tuple element. Print the resulting tuple and its length.

**Expected Output:**
```
('P', 'y', 't', 'h', 'o', 'n')
Length: 6
```

**Hint:** Use `tuple()` constructor with a string.

---

## Problem 8: Function Returns Multiple Values (Medium)
Write a function `get_min_max(numbers)` that takes a list of numbers and returns both the minimum and maximum values as a tuple. Test it with `[3, 7, 1, 9, 4]`.

**Expected Output:**
```
Minimum: 1, Maximum: 9
```

**Hint:** Return multiple values separated by comma: `return min(numbers), max(numbers)`

---

## Problem 9: Combine Two Tuples (Medium)
Given `tuple1 = (1, 2, 3)` and `tuple2 = (4, 5, 6)`, create a new tuple that combines both. Verify that the original tuples are unchanged.

**Expected Output:**
```
Combined: (1, 2, 3, 4, 5, 6)
Original tuple1: (1, 2, 3)
Original tuple2: (4, 5, 6)
```

**Hint:** Use the `+` operator to concatenate tuples.

---

## Problem 10: Tuple Packing Without Parentheses (Medium)
Create a tuple containing three favorite fruits without using parentheses. Verify it's a tuple by checking its type.

**Expected Output:**
```
('apple', 'banana', 'cherry')
<class 'tuple'>
```

**Hint:** Separate values with commas: `fruits = "apple", "banana", "cherry"`

---

## Problem 11: Nested Tuples (Medium)
Create a tuple called `students` that contains three tuples, each with a student's name and score:
- ("Alice", 85)
- ("Bob", 92)
- ("Charlie", 78)

Print each student's information using a loop.

**Expected Output:**
```
Alice: 85
Bob: 92
Charlie: 78
```

**Hint:** Use a for loop with tuple unpacking: `for name, score in students:`

---

## Problem 12: Demonstrate Immutability (Hard)
Create a tuple `original = (1, 2, 3)`. Try to "modify" it by creating a new tuple with the first element changed to 10. Show that the original tuple remains unchanged.

**Expected Output:**
```
Original: (1, 2, 3)
Modified: (10, 2, 3)
Original after 'modification': (1, 2, 3)
```

**Hint:** Create a new tuple: `modified = (10,) + original[1:]` or `modified = (10, 2, 3)`

---

## Problem 13: Create Tuple from Range (Hard)
Create a tuple containing the first 10 even numbers (2, 4, 6, ..., 20) using the `range()` function and tuple constructor.

**Expected Output:**
```
(2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
```

**Hint:** Use `range(2, 21, 2)` and convert to tuple.

---

## Problem 14: Coordinate Distance Calculator (Hard)
Write a function `calculate_distance(point1, point2)` that takes two tuples representing 2D coordinates and returns the distance between them using the formula: `√((x₂-x₁)² + (y₂-y₁)²)`

Test with `point1 = (0, 0)` and `point2 = (3, 4)`.

**Expected Output:**
```
Distance: 5.0
```

**Hint:** Use `math.sqrt()` and unpack the tuples to get x and y values.

---

## Problem 15: Tuple Repetition and Analysis (Hard)
Create a tuple by repeating `(1, 2)` three times. Then:
1. Count how many times the number 1 appears
2. Find the index of the first occurrence of 2
3. Print the length of the tuple

**Expected Output:**
```
Tuple: (1, 2, 1, 2, 1, 2)
Count of 1: 3
First index of 2: 1
Length: 6
```

**Hint:** Use the `*` operator for repetition, `.count()` and `.index()` methods.

---

## Problem 16: Function with Tuple Parameter (Hard)
Write a function `display_person_info(person)` that takes a tuple containing (name, age, city) and prints a formatted message. Handle the case where the tuple might not have exactly 3 elements.

**Test Cases:**
```python
display_person_info(("Alice", 25, "New York"))
display_person_info(("Bob", 30))
```

**Expected Output:**
```
Alice is 25 years old and lives in New York.
Invalid person data: expected 3 elements.
```

**Hint:** Check `len(person) == 3` before unpacking.

---

## Problem 17: Convert Multiple Lists to Tuples (Hard)
Given three lists:
```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]
```

Use `zip()` to combine them and create a list of tuples where each tuple contains (name, age, city).

**Expected Output:**
```
[('Alice', 25, 'NYC'), ('Bob', 30, 'LA'), ('Charlie', 35, 'Chicago')]
```

**Hint:** Use `list(zip(names, ages, cities))`

---

## Problem 18: Tuple with Mixed Nesting (Very Hard)
Create a tuple that represents a simple family tree:
```
family = ("John", "Mary", (("Alice", "Engineer"), ("Bob", "Doctor")))
```

Access and print:
1. The parents' names (first two elements)
2. The first child's name
3. The second child's profession

**Expected Output:**
```
Parents: John and Mary
First child: Alice
Second child's profession: Doctor
```

**Hint:** Use nested indexing: `family[2][0][0]` for first child's name.

---

## Problem 19: Immutable Tuple with Mutable Content (Very Hard)
Create a tuple containing a list: `data = ([1, 2, 3], "fixed")`. Show that:
1. You cannot reassign elements of the tuple
2. But you CAN modify the list inside the tuple
3. Explain why this happens

**Expected Output:**
```
Original: ([1, 2, 3], 'fixed')
After modifying list: ([1, 2, 3, 4], 'fixed')
Trying to reassign tuple element: TypeError
```

**Hint:** The tuple is immutable, but the list it contains is mutable.

---

## Problem 20: Advanced Tuple Unpacking (Very Hard)
Use extended tuple unpacking to separate the first element, last element, and middle elements from a tuple:
```python
numbers = (1, 2, 3, 4, 5, 6)
```

Assign:
- `first` = first element
- `last` = last element
- `middle` = all middle elements as a list

**Expected Output:**
```
First: 1
Middle: [2, 3, 4, 5]
Last: 6
```

**Hint:** Use `first, *middle, last = numbers`
