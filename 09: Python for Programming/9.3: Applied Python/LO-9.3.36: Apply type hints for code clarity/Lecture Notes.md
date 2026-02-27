# Lecture Notes: Apply Type Hints

## Type Hints

Type hints (type annotations) document the expected types of variables, function parameters, and return values. They improve code readability and enable better IDE support, but don't enforce types at runtime.


---

<div align="center">

![Python Type Hints Annotation Function Code](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/LO-9.3.36.png)

*Type hints reference Python's type hierarchy to annotate expected types for code clarity*

</div>

---

## Introduction

Type hints implement **gradual typing** - adding type information to dynamically-typed Python! This is **documentation that tools can verify** - IDEs catch bugs before runtime. Type hints bridge **dynamic flexibility** and **static safety**!

### Why Type Hints Transform Development

**Problem without types**: Bugs found at runtime:
```python
# MYSTERY - what types does this accept?
def process(data, config):
    return data.transform(config["key"])
# What is data? What shape is config?
# Bugs discovered only when code runs!
```

**Solution with type hints**: Self-documenting, tool-verified:
```python
# CLEAR - types documented and checked!
def process(data: DataFrame, config: dict[str, Any]) -> DataFrame:
    return data.transform(config["key"])
# IDE warns about type mismatches immediately!
```

**This is shift-left testing** - catch errors earlier in development!

### Historical Context

**Type hints** added **Python 3.5** (2015) with **PEP 484** (Guido van Rossum & Jukka Lehtosalo). Inspired by **mypy** project (2012) - optional static type checker for Python!

**Gradual typing** theory by **Jeremy Siek** (2006) - add types incrementally, mix typed and untyped code. Python's approach: **types are optional** - don't break existing code, adopt gradually!

**typing module** provides advanced types: `List[int]`, `Dict[str, Any]`, `Optional[str]`, `Union[int, str]`. **Python 3.9+** simplified: `list[int]` instead of `List[int]` - built-in generics! **Python 3.10** added `X | Y` union syntax replacing `Union[X, Y]`!

### Real-World Analogies

**Type hints like ingredient labels**:
- **Without labels**: Mystery can - could be beans or paint!
- **With labels**: "Black Beans, 15oz, No Salt Added"
- **Type hints**: `def cook(ingredient: str, temp: int) -> Dish`
**Labels prevent mistakes before you open the can!**

**Or like electrical outlets**:
```python
# Like outlet standards:
# US outlet accepts US plug (type compatibility)
# European plug won't fit US outlet (type mismatch!)

def charge_device(plug: USPlug) -> None:
    # Only US plugs accepted!
    pass
# Type system prevents wrong connections!
```

**Or like postal addressing**:
- **No types**: Send package to "somewhere" (might arrive?)
- **With types**: Send to `address: Address` (verified format!)
- **Type checker**: Post office verifies address format before shipping
**Verify before sending, not after delivery fails!**

### Type Hints Don't Enforce at Runtime!

**Critical understanding** - Python ignores type hints at runtime:
```python
def add(a: int, b: int) -> int:
    return a + b

add("hello", "world")  # Works! Python doesn't check!
# Type hints are for TOOLS (mypy, IDE), not Python itself!
```

**Use mypy** for static checking: `mypy your_file.py` catches errors!

---
### Basic Syntax

```python
# Variable type hints
name: str = "Alice"
age: int = 25
height: float = 5.8
is_student: bool = True

# Function type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Multiple parameters
def add(a: int, b: int) -> int:
    return a + b
```

## Function Type Hints

```python
# Basic function with type hints
def calculate_area(length: float, width: float) -> float:
    """Calculate rectangle area"""
    return length * width

# Function with no return value
def print_message(message: str) -> None:
    print(message)

# Function with optional parameter
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

# Multiple return values (tuple)
def divide_with_remainder(dividend: int, divisor: int) -> tuple[int, int]:
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

result = divide_with_remainder(17, 5)
print(result)  # (3, 2)
```

## Collection Type Hints

```python
from typing import List, Dict, Set, Tuple

# List of integers
def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)

# Dictionary mapping strings to integers
def count_letters(words: List[str]) -> Dict[str, int]:
    return {word: len(word) for word in words}

# Set of strings
def get_unique_words(text: str) -> Set[str]:
    return set(text.lower().split())

# Tuple with specific types
def get_person_info() -> Tuple[str, int, float]:
    return ("Alice", 25, 5.8)

# List of lists
def create_matrix() -> List[List[int]]:
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

## Python 3.9+ Syntax (Simplified)

```python
# Python 3.9+ allows lowercase type names
def process_items(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}

# Tuple
def get_coordinates() -> tuple[float, float]:
    return (10.5, 20.3)

# Set
def get_tags() -> set[str]:
    return {"python", "programming", "tutorial"}
```

## Real-World Examples

### Example 1: User Management

```python
from typing import Dict, List, Optional

class User:
    def __init__(self, name: str, email: str, age: int) -> None:
        self.name: str = name
        self.email: str = email
        self.age: int = age

def create_user(name: str, email: str, age: int) -> User:
    """Create a new user"""
    return User(name, email, age)

def find_user_by_email(users: List[User], email: str) -> Optional[User]:
    """Find user by email, return None if not found"""
    for user in users:
        if user.email == email:
            return user
    return None

def get_users_by_age_range(users: List[User], min_age: int, max_age: int) -> List[User]:
    """Filter users by age range"""
    return [user for user in users if min_age <= user.age <= max_age]

# Usage
users: List[User] = [
    create_user("Alice", "alice@email.com", 25),
    create_user("Bob", "bob@email.com", 30),
    create_user("Charlie", "charlie@email.com", 35)
]

found_user: Optional[User] = find_user_by_email(users, "bob@email.com")
if found_user:
    print(f"Found: {found_user.name}")
```

### Example 2: Data Processing

```python
from typing import List, Dict, Callable

def process_data(data: List[int], operation: Callable[[int], int]) -> List[int]:
    """Apply operation to each element"""
    return [operation(x) for x in data]

def double(x: int) -> int:
    return x * 2

def square(x: int) -> int:
    return x ** 2

numbers: List[int] = [1, 2, 3, 4, 5]
doubled: List[int] = process_data(numbers, double)
squared: List[int] = process_data(numbers, square)

print(f"Doubled: {doubled}")  # [2, 4, 6, 8, 10]
print(f"Squared: {squared}")  # [1, 4, 9, 16, 25]

def aggregate_data(data: List[Dict[str, int]]) -> Dict[str, int]:
    """Aggregate data from list of dictionaries"""
    result: Dict[str, int] = {}
    for item in data:
        for key, value in item.items():
            result[key] = result.get(key, 0) + value
    return result

sales_data: List[Dict[str, int]] = [
    {"apples": 10, "oranges": 5},
    {"apples": 15, "bananas": 8},
    {"oranges": 3, "bananas": 12}
]

totals: Dict[str, int] = aggregate_data(sales_data)
print(f"Totals: {totals}")  # {'apples': 25, 'oranges': 8, 'bananas': 20}
```

### Example 3: Configuration Management

```python
from typing import Dict, Any, Union

ConfigValue = Union[str, int, bool, float]

def load_config() -> Dict[str, ConfigValue]:
    """Load configuration settings"""
    return {
        "host": "localhost",
        "port": 8080,
        "debug": True,
        "timeout": 30.5
    }

def get_config_value(config: Dict[str, ConfigValue], key: str, default: ConfigValue = None) -> ConfigValue:
    """Get configuration value with optional default"""
    return config.get(key, default)

config: Dict[str, ConfigValue] = load_config()
host: ConfigValue = get_config_value(config, "host")
port: ConfigValue = get_config_value(config, "port")
debug: ConfigValue = get_config_value(config, "debug")

print(f"Server: {host}:{port}, Debug: {debug}")
```

### Example 4: API Response Handling

```python
from typing import List, Dict, Optional, TypedDict

class UserResponse(TypedDict):
    id: int
    name: str
    email: str
    active: bool

def fetch_users() -> List[UserResponse]:
    """Fetch users from API"""
    return [
        {"id": 1, "name": "Alice", "email": "alice@example.com", "active": True},
        {"id": 2, "name": "Bob", "email": "bob@example.com", "active": False}
    ]

def get_active_users(users: List[UserResponse]) -> List[UserResponse]:
    """Filter for active users only"""
    return [user for user in users if user["active"]]

def find_user_by_id(users: List[UserResponse], user_id: int) -> Optional[UserResponse]:
    """Find user by ID"""
    for user in users:
        if user["id"] == user_id:
            return user
    return None

# Usage
all_users: List[UserResponse] = fetch_users()
active_users: List[UserResponse] = get_active_users(all_users)
user: Optional[UserResponse] = find_user_by_id(all_users, 1)
```

### Example 5: Type Aliases

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

grades: StudentGrades = {
    "Alice": [85, 90, 92],
    "Bob": [78, 82, 80]
}
averages: Dict[str, float] = calculate_average_grade(grades)
```

## Optional and Union Types

```python
from typing import Optional, Union

# Optional[Type] is shorthand for Union[Type, None]
def find_item(items: List[str], target: str) -> Optional[int]:
    """Return index of item or None if not found"""
    try:
        return items.index(target)
    except ValueError:
        return None

# Union allows multiple possible types
def process_id(id_value: Union[int, str]) -> str:
    """Convert ID to string"""
    return str(id_value)

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
```

## Generic Types

```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    """Generic stack implementation"""

    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def peek(self) -> T:
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

# Usage with specific types
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)

str_stack: Stack[str] = Stack()
str_stack.push("hello")
str_stack.push("world")
```

## Checking Types at Runtime

```python
# Type hints don't enforce types at runtime
def add(a: int, b: int) -> int:
    return a + b

# This still works (no error!)
result = add("hello", "world")  # Returns "helloworld"
print(result)

# To enforce types, use isinstance()
def add_strict(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")
    return a + b

# Now this raises an error
# add_strict("hello", "world")  # TypeError
```

## Key Takeaways

1. **Type hints**: Document expected types, don't enforce them
2. **Function signatures**: `def func(param: type) -> return_type:`
3. **Collections**: Use List, Dict, Set, Tuple from typing
4. **Optional**: Use Optional[Type] for values that can be None
5. **Union**: Use Union[Type1, Type2] for multiple possible types
6. **Type aliases**: Create readable names for complex types
7. **Modern syntax**: Python 3.9+ allows list, dict, tuple instead of List, Dict, Tuple
8. **Benefits**: Better IDE support, documentation, error detection
