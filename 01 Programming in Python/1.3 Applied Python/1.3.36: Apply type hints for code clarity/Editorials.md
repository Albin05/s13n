# Editorials: Apply Type Hints

## Problem 1: Add Type Hints to Basic Function

```python
def calculate_rectangle_area(length: float, width: float) -> float:
    return length * width
```

### Explanation
Both parameters are floats, and the return value is also a float.

---

## Problem 2: Type Hints for List Processing

```python
from typing import List

def sum_list(numbers: List[int]) -> int:
    return sum(numbers)

# Or with Python 3.9+:
def sum_list(numbers: list[int]) -> int:
    return sum(numbers)
```

### Explanation
Parameter is a list of integers, return value is an integer sum.

---

## Problem 3: Dictionary Type Hints

```python
from typing import List, Dict

def name_lengths(names: List[str]) -> Dict[str, int]:
    return {name: len(name) for name in names}

# Or with Python 3.9+:
def name_lengths(names: list[str]) -> dict[str, int]:
    return {name: len(name) for name in names}
```

### Explanation
Input is list of strings, output is dictionary mapping strings to integers.

---

## Problem 4: Optional Return Type

```python
from typing import List, Optional

def find_index(items: List[str], target: str) -> Optional[int]:
    try:
        return items.index(target)
    except ValueError:
        return None
```

### Explanation
Returns either an int (index) or None. Optional[int] is equivalent to Union[int, None].

---

## Problem 5: Complex Type Hints

```python
from typing import Dict, List, Optional

class StudentGradeBook:
    def __init__(self) -> None:
        self.grades: Dict[str, List[int]] = {}

    def add_student(self, name: str) -> None:
        self.grades[name] = []

    def add_grade(self, name: str, grade: int) -> None:
        if name in self.grades:
            self.grades[name].append(grade)

    def get_average(self, name: str) -> Optional[float]:
        if name in self.grades and self.grades[name]:
            return sum(self.grades[name]) / len(self.grades[name])
        return None

    def get_all_averages(self) -> Dict[str, Optional[float]]:
        return {name: self.get_average(name) for name in self.grades}
```

### Explanation
- `__init__` returns None
- grades is Dict[str, List[int]]
- get_average returns Optional[float] (None if no grades)
- get_all_averages returns Dict[str, Optional[float]]
