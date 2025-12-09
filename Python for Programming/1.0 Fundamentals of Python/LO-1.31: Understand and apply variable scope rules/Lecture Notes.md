# Lecture Notes: Understand Variable Scope

## Understand Variable Scope

Understanding local, global, and nonlocal scopes


---

<div align="center">

![Variables concept - labeled storage containers](https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800&q=80)

*Think of variables as labeled containers storing different types of data*

</div>

---
### Key Concepts

**Core principle**: global, nonlocal, LEGB rule

### Syntax and Usage

```python
# Basic example will be shown in practical examples below
```

### Practical Examples

#### Example 1: Local vs Global

```python
x = 10  # Global variable

def my_function():
    x = 20  # Local variable
    print(f"Local x: {x}")

my_function()  # Local x: 20
print(f"Global x: {x}")  # Global x: 10
```

#### Example 2: Using global Keyword

```python
count = 0

def increment():
    global count
    count += 1
    print(f"Count: {count}")

increment()  # Count: 1
increment()  # Count: 2
print(count)  # 2
```

#### Example 3: Nested Functions and nonlocal

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20
        print(f"Inner x: {x}")

    inner()  # Inner x: 20
    print(f"Outer x: {x}")  # Outer x: 20

outer()
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
