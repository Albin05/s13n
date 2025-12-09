# Question Bank: Apply Type Hints

## Problem 1 (Easy)

**Title:** Add Type Hints to Basic Function

**Problem Statement:**
Add appropriate type hints to this function:

```python
def calculate_rectangle_area(length, width):
    return length * width
```

**Constraints:**
- Parameters are floats
- Return value is a float

---

## Problem 2 (Easy)

**Title:** Type Hints for List Processing

**Problem Statement:**
Add type hints to this function that takes a list of integers and returns their sum:

```python
def sum_list(numbers):
    return sum(numbers)
```

**Constraints:**
- Use typing.List or list (Python 3.9+)
- Parameter is list of integers
- Returns integer

---

## Problem 3 (Medium)

**Title:** Dictionary Type Hints

**Problem Statement:**
Add type hints to this function that takes a list of names and returns a dictionary mapping each name to its length:

```python
def name_lengths(names):
    return {name: len(name) for name in names}
```

**Constraints:**
- Input is list of strings
- Output is dictionary mapping string to int

---

## Problem 4 (Medium)

**Title:** Optional Return Type

**Problem Statement:**
Add type hints to this function that searches for a value in a list and returns its index, or None if not found:

```python
def find_index(items, target):
    try:
        return items.index(target)
    except ValueError:
        return None
```

**Constraints:**
- Use Optional for return type
- Items is list of strings
- Target is a string

---

## Problem 5 (Hard)

**Title:** Complex Type Hints

**Problem Statement:**
Add complete type hints to this class and all its methods:

```python
class StudentGradeBook:
    def __init__(self):
        self.grades = {}

    def add_student(self, name):
        self.grades[name] = []

    def add_grade(self, name, grade):
        if name in self.grades:
            self.grades[name].append(grade)

    def get_average(self, name):
        if name in self.grades and self.grades[name]:
            return sum(self.grades[name]) / len(self.grades[name])
        return None

    def get_all_averages(self):
        return {name: self.get_average(name) for name in self.grades}
```

**Constraints:**
- Use appropriate types for all parameters and return values
- grades should be Dict[str, List[int]]
- Use Optional where appropriate
