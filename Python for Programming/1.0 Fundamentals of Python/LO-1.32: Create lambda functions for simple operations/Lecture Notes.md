# Lecture Notes: Create Lambda Functions

## Create Lambda Functions

Writing anonymous single-expression functions


---

<div align="center">

![Function machine concept - input to output](https://images.unsplash.com/photo-1581291518857-4e27b48ff24e?w=800&q=80)

*Functions are reusable blocks of code that take inputs and return outputs*

</div>

---
### Key Concepts

**Core principle**: lambda args: expression

### Syntax and Usage

```python
# Basic example will be shown in practical examples below
```

### Practical Examples

#### Example 1: Basic Lambda

```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square_lambda = lambda x: x ** 2

print(square(5))         # 25
print(square_lambda(5))  # 25
```

#### Example 2: Lambda with Sorting

```python
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort by grade
sorted_students = sorted(students, key=lambda s: s["grade"])
print([s["name"] for s in sorted_students])
# ['Charlie', 'Alice', 'Bob']
```

#### Example 3: Lambda with map and filter

```python
numbers = [1, 2, 3, 4, 5]

# map - apply function to each element
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# filter - keep elements where function returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]
```

### Best Practices

1. Write clear, readable code
2. Handle errors appropriately
3. Follow Python conventions
4. Document your code
5. Test thoroughly

### Common Mistakes

1. Not handling edge cases
2. Overcomplicating simple tasks
3. Not following naming conventions

### Key Takeaways

1. Understanding the core concept is essential
2. Practice with real examples
3. Apply best practices
4. Avoid common pitfalls
5. Write clean, maintainable code
