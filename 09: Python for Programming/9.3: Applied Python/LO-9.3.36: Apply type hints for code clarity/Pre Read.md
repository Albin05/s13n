# Pre-Read: Apply Type Hints

## Type Hints

Type hints add type information to Python code without enforcing it:

```python
# Without type hints
def greet(name):
    return f"Hello, {name}!"

# With type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Type hints document expected types
def add(a: int, b: int) -> int:
    return a + b
```

## Variable Type Hints

```python
# Type hints for variables
name: str = "Alice"
age: int = 25
score: float = 95.5
is_active: bool = True

# Lists with type hints
numbers: list[int] = [1, 2, 3, 4, 5]
names: list[str] = ["Alice", "Bob", "Charlie"]
```

## Function Type Hints

```python
from typing import List, Dict

def process_names(names: List[str]) -> Dict[str, int]:
    """Count letters in each name"""
    return {name: len(name) for name in names}

result = process_names(["Alice", "Bob"])
print(result)  # {'Alice': 5, 'Bob': 3}
```
