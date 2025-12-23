# Pre-Read: Read JSON Files

## What is JSON?

JSON (JavaScript Object Notation) stores structured data:

```json
{
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "JavaScript"]
}
```

## Reading JSON Files

```python
import json

with open("data.json", "r") as file:
    data = json.load(file)
    print(data["name"])  # Alice
    print(data["skills"])  # ['Python', 'JavaScript']
```

## JSON to Python

| JSON | Python |
|------|--------|
| object {} | dict |
| array [] | list |
| string | str |
| number | int/float |
| true/false | True/False |
| null | None |

## Why Use JSON?

1. **Structured**: Nested data
2. **Popular**: Used in APIs
3. **Readable**: Easy to understand
