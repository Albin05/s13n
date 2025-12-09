# Post-Class Quiz: Apply Type Hints

## Q1: Do type hints enforce types at runtime in Python?
A) Yes, they raise errors for wrong types
B) No, they're only for documentation and tooling
C) Only in production mode

<details><summary>Answer</summary>
B) No, they're only for documentation and tooling

Explanation: Type hints in Python are optional and don't enforce types at runtime. They help with documentation, IDE support, and static analysis tools, but Python doesn't check them during execution.
</details>

## Q2: What does Optional[int] mean?
A) The parameter is optional
B) The value can be either int or None
C) The value must be an integer

<details><summary>Answer</summary>
B) The value can be either int or None

Explanation: Optional[int] is shorthand for Union[int, None]. It means the value can be either an integer or None.
</details>

## Q3: How do you specify a function returns nothing?
A) -> void
B) -> None
C) -> Empty

<details><summary>Answer</summary>
B) -> None

Explanation: Use `-> None` to indicate a function doesn't return a value (like functions that only print or modify state).
</details>

## Q4: What's the difference between List[int] and list[int]?
A) List is from typing module, list is built-in (Python 3.9+)
B) They're completely different
C) List is for classes, list is for functions

<details><summary>Answer</summary>
A) List is from typing module, list is built-in (Python 3.9+)

Explanation: Python 3.9+ allows using lowercase built-in types (list, dict, tuple) directly in type hints. Before that, you needed to import List, Dict, Tuple from the typing module.
</details>

## Q5: How do you specify a dictionary mapping strings to integers?
A) dict[str, int] or Dict[str, int]
B) dictionary<string, integer>
C) map[str: int]

<details><summary>Answer</summary>
A) dict[str, int] or Dict[str, int]

Explanation: Use dict[str, int] (Python 3.9+) or Dict[str, int] (from typing module) to specify a dictionary with string keys and integer values.
</details>
