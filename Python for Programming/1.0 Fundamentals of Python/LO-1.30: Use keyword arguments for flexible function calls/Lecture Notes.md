# Lecture Notes: Use Keyword Arguments

## Use Keyword Arguments

Calling functions with named arguments


---

<div align="center">

![Variables concept - labeled storage containers](https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800&q=80)

*Think of variables as labeled containers storing different types of data*

</div>

---
### Key Concepts

**Core principle**: func(arg_name=value)

### Syntax and Usage

```python
# Basic example will be shown in practical examples below
```

### Practical Examples

#### Example 1: Basic Keyword Arguments

```python
def create_profile(name, age, city, country):
    return f"{name}, {age}, from {city}, {country}"

# Positional
print(create_profile("Alice", 25, "Boston", "USA"))

# Keyword arguments
print(create_profile(name="Bob", age=30, city="London", country="UK"))

# Mixed (positional first, then keyword)
print(create_profile("Charlie", 35, city="Paris", country="France"))
```

#### Example 2: Using **kwargs

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Boston")
# name: Alice
# age: 25
# city: Boston
```

#### Example 3: Combining *args and **kwargs

```python
def flexible_function(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"Keyword: {kwargs}")

flexible_function(1, 2, 3, name="Alice", age=25)
# Positional: (1, 2, 3)
# Keyword: {'name': 'Alice', 'age': 25}
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
