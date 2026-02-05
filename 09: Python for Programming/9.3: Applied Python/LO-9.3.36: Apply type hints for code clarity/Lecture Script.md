# Lecture Script: LO-9.3.36 Apply Type Hints for Code Clarity

## [0:00-0:02] Hook (2 min)
**Say**: "What does this function return? A string? A number? A list? Without looking at the code, you can't tell. Type hints solve this: def greet(name: str) -> str. Crystal clear documentation, better IDE support, catch errors before runtime. No enforcement, just clarity!"

**Demo**:
```python
# Without type hints - unclear
def calculate(x, y):
    return x * y

# With type hints - crystal clear!
def calculate(x: int, y: int) -> int:
    return x * y

# IDE knows types, gives autocomplete!
result: int = calculate(5, 3)

# Document complex types
from typing import List

def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)

# Type checkers catch mistakes
# sum_numbers("hello")  # Type checker warns!
```

**Say**: "That's type hints! Let's master them."

## [0:02-0:06] Basic Type Hints (4 min)

**Say**: "Type hints document expected types for variables, parameters, and return values."

**Live Code**:
```python
# Variable type hints
name: str = "Alice"
age: int = 25
height: float = 5.8
is_student: bool = True

print(f"{name} is {age} years old")

# Function type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

# Function with no return value
def print_message(message: str) -> None:
    print(message)

# Optional parameters still work
def greet_with_title(name: str, title: str = "Mr.") -> str:
    return f"Hello, {title} {name}!"

# Test
result: str = greet("Bob")
print(result)  # Hello, Bob!

sum_result: int = add(10, 20)
print(sum_result)  # 30

print_message("Testing")  # Testing
```

**Point out**: "Type hints are DOCUMENTATION, not enforcement. Python doesn't check them at runtime!"

**Emphasize**: "Use type hints for clarity, IDE support, and static analysis tools like mypy!"

## [0:06-0:10] Collection Type Hints (4 min)

**Say**: "For collections, specify what they contain using typing module."

**Live Code**:
```python
from typing import List, Dict, Set, Tuple

# List of integers
def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)

# Dictionary mapping strings to integers
def count_word_lengths(words: List[str]) -> Dict[str, int]:
    return {word: len(word) for word in words}

# Set of strings
def get_unique_words(text: str) -> Set[str]:
    return set(text.lower().split())

# Tuple with specific types
def get_person_info() -> Tuple[str, int, float]:
    return ("Alice", 25, 5.8)

# Test
nums: List[int] = [1, 2, 3, 4, 5]
total: int = sum_numbers(nums)
print(f"Sum: {total}")

words: List[str] = ["hello", "world", "python"]
lengths: Dict[str, int] = count_word_lengths(words)
print(f"Lengths: {lengths}")

name, age, height = get_person_info()
print(f"{name}, {age}, {height}")
```

**Say**: "Python 3.9+ allows lowercase: list[int], dict[str, int]. Older versions need List, Dict from typing."

**Live Code - Modern Syntax**:
```python
# Python 3.9+ syntax (simpler!)
def process_items(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}

def get_coordinates() -> tuple[float, float]:
    return (10.5, 20.3)

def get_tags() -> set[str]:
    return {"python", "programming", "tutorial"}
```

## [0:10-0:13] Optional and Union Types (3 min)

**Say**: "Sometimes values can be None or multiple types. Optional and Union handle this."

**Live Code**:
```python
from typing import Optional, Union

# Optional[Type] means "Type or None"
def find_user(user_id: int) -> Optional[str]:
    """Return username or None if not found"""
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}
    return users.get(user_id)

result: Optional[str] = find_user(1)
print(result)  # Alice

result2: Optional[str] = find_user(999)
print(result2)  # None

# Union allows multiple possible types
def process_id(id_value: Union[int, str]) -> str:
    """Convert ID to string"""
    return str(id_value)

print(process_id(123))      # "123"
print(process_id("ABC"))    # "ABC"

# Multiple types in Union
def parse_value(value: str) -> Union[int, float, str]:
    """Try to parse as int, then float, or return as string"""
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value

print(parse_value("42"))      # 42 (int)
print(parse_value("3.14"))    # 3.14 (float)
print(parse_value("hello"))   # hello (str)
```

**Point out**: "Optional[str] is shorthand for Union[str, None]!"

## [0:13-0:16] Real-World Example: User Management (3 min)

**Say**: "Type hints make large codebases maintainable. Let's see a practical example."

**Live Code**:
```python
from typing import List, Dict, Optional

class User:
    def __init__(self, name: str, email: str, age: int) -> None:
        self.name: str = name
        self.email: str = email
        self.age: int = age

    def __repr__(self) -> str:
        return f"User({self.name}, {self.email}, {self.age})"

def create_user(name: str, email: str, age: int) -> User:
    """Create a new user"""
    return User(name, email, age)

def find_user_by_email(users: List[User], email: str) -> Optional[User]:
    """Find user by email, return None if not found"""
    for user in users:
        if user.email == email:
            return user
    return None

def get_users_by_age_range(
    users: List[User],
    min_age: int,
    max_age: int
) -> List[User]:
    """Filter users by age range"""
    return [user for user in users if min_age <= user.age <= max_age]

def get_user_summary(users: List[User]) -> Dict[str, int]:
    """Get summary statistics"""
    return {
        "total": len(users),
        "avg_age": sum(u.age for u in users) // len(users) if users else 0
    }

# Usage - IDE provides autocomplete and type checking!
users: List[User] = [
    create_user("Alice", "alice@email.com", 25),
    create_user("Bob", "bob@email.com", 30),
    create_user("Charlie", "charlie@email.com", 35)
]

found: Optional[User] = find_user_by_email(users, "bob@email.com")
if found:
    print(f"Found: {found.name}")

young_users: List[User] = get_users_by_age_range(users, 20, 30)
print(f"Young users: {[u.name for u in young_users]}")

summary: Dict[str, int] = get_user_summary(users)
print(f"Summary: {summary}")
```

**Say**: "Notice how clear everything is! We know exactly what each function expects and returns."

## [0:16-0:19] Type Aliases and Complex Types (3 min)

**Say**: "For complex types, create aliases for readability."

**Live Code**:
```python
from typing import List, Dict, Tuple

# Define type aliases for complex types
Coordinate = Tuple[float, float]
Path = List[Coordinate]
StudentGrades = Dict[str, List[int]]

def calculate_distance(start: Coordinate, end: Coordinate) -> float:
    """Calculate distance between two points"""
    x1, y1 = start
    x2, y2 = end
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def calculate_path_length(path: Path) -> float:
    """Calculate total path length"""
    total: float = 0.0
    for i in range(len(path) - 1):
        total += calculate_distance(path[i], path[i + 1])
    return total

def calculate_average_grade(grades: StudentGrades) -> Dict[str, float]:
    """Calculate average grade for each student"""
    return {
        student: sum(student_grades) / len(student_grades)
        for student, student_grades in grades.items()
    }

# Usage
path: Path = [(0.0, 0.0), (3.0, 4.0), (6.0, 8.0)]
length: float = calculate_path_length(path)
print(f"Path length: {length:.2f}")

grades: StudentGrades = {
    "Alice": [85, 90, 92],
    "Bob": [78, 82, 80]
}
averages: Dict[str, float] = calculate_average_grade(grades)
print(f"Averages: {averages}")
```

**Point out**: "Type aliases make complex signatures readable and maintainable!"

## [0:19-0:21] Callable and Generic Types (2 min)

**Say**: "Type hint functions themselves using Callable, and create generic types with TypeVar."

**Live Code**:
```python
from typing import List, Callable, TypeVar

# Callable[[arg_types], return_type]
def apply_operation(
    numbers: List[int],
    operation: Callable[[int], int]
) -> List[int]:
    """Apply operation to each number"""
    return [operation(x) for x in numbers]

def double(x: int) -> int:
    return x * 2

def square(x: int) -> int:
    return x ** 2

nums: List[int] = [1, 2, 3, 4, 5]
doubled: List[int] = apply_operation(nums, double)
squared: List[int] = apply_operation(nums, square)

print(f"Doubled: {doubled}")  # [2, 4, 6, 8, 10]
print(f"Squared: {squared}")  # [1, 4, 9, 16, 25]

# Generic types
T = TypeVar('T')

def get_first(items: List[T]) -> T:
    """Get first item from list"""
    return items[0]

# Works with any type!
numbers: List[int] = [1, 2, 3]
first_num: int = get_first(numbers)  # Type checker knows it's int

words: List[str] = ["hello", "world"]
first_word: str = get_first(words)  # Type checker knows it's str
```

**Say**: "Generics let you write type-safe functions that work with any type!"

## [0:21-0:23] Type Hints Don't Enforce (2 min)

**Say**: "CRITICAL: Type hints are documentation, NOT runtime checks!"

**Live Code**:
```python
def add(a: int, b: int) -> int:
    return a + b

# This WORKS at runtime - no type checking!
result = add("hello", "world")
print(result)  # helloworld

# Python doesn't care about type hints at runtime
print(type(result))  # <class 'str'>

# To enforce types, use isinstance()
def add_strict(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")
    return a + b

# This raises an error
try:
    add_strict("hello", "world")
except TypeError as e:
    print(f"Error: {e}")
# Error: Both arguments must be integers

# Use mypy or other type checkers for static analysis
# Run: mypy your_script.py
```

**Emphasize**: "Use mypy, pyright, or your IDE's type checker to catch type errors before runtime!"

## [0:23-0:24] Practice Challenge (1 min)

**Challenge**: "Add type hints to this student grade calculator."

**Skeleton**:
```python
def add_grade(student_grades, student, grade):
    if student not in student_grades:
        student_grades[student] = []
    student_grades[student].append(grade)

def get_average(student_grades, student):
    if student in student_grades and student_grades[student]:
        return sum(student_grades[student]) / len(student_grades[student])
    return 0.0

# TODO: Add type hints
```

**Solution** (show after 1 minute):
```python
from typing import Dict, List

def add_grade(
    student_grades: Dict[str, List[int]],
    student: str,
    grade: int
) -> None:
    if student not in student_grades:
        student_grades[student] = []
    student_grades[student].append(grade)

def get_average(
    student_grades: Dict[str, List[int]],
    student: str
) -> float:
    if student in student_grades and student_grades[student]:
        return sum(student_grades[student]) / len(student_grades[student])
    return 0.0
```

## [0:24-0:25] Wrap-up (1 min)

**Key Points**:
1. **Type hints**: Document expected types, don't enforce them
2. **Basic syntax**: param: type, -> return_type
3. **Collections**: List[int], Dict[str, int], Set[str], Tuple[int, str]
4. **Optional**: Optional[Type] for values that can be None
5. **Union**: Union[Type1, Type2] for multiple possible types

**Common Mistakes**:
- Expecting type hints to prevent bugs at runtime (they don't!)
- Forgetting to import from typing module (older Python)
- Using complex types without type aliases
- Not using a type checker (mypy, pyright)

**Benefits**:
- Better IDE autocomplete and suggestions
- Catch bugs with static type checkers
- Self-documenting code
- Easier refactoring
- Team communication

**Tools**:
- mypy: Static type checker
- pyright: Microsoft's type checker
- IDEs: VS Code, PyCharm have built-in type checking

**Python Version Notes**:
- Python 3.5+: Basic type hints
- Python 3.9+: Simplified syntax (list vs List)
- Python 3.10+: Union types with | (str | int)

**Closing**: "Type hints are optional but invaluable! They make code clearer, catch bugs early, and improve the development experience. Use them in all new code and gradually add them to existing projects!"
