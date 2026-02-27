# Lecture Notes: Apply Default Parameters

## Introduction

Default parameters introduce **optional arguments** - the ability to call functions with fewer arguments by providing sensible defaults. This represents a balance between **flexibility** and **convenience** in API design.

### Why Default Parameters Exist

**The convenience problem**: Some functions have common use cases. Requiring all parameters every time is tedious and error-prone.
**Default parameters solution**: Provide sensible defaults for common cases. Users can override when needed, but don't have to specify everything every time.

**Real-world API design**: Python's own `print()` function uses defaults: `print(value, sep=' ', end='\n')`. You rarely need to change `sep` or `end`, so they have defaults!

### Real-World Analogy

Default parameters are like **ordering at a restaurant**:
- **Required**: "I want a burger" (must specify main item)
- **Optional/defaults**: Comes with lettuce, tomato, pickles (default toppings)
- **Override**: "No pickles, extra cheese" (customize when needed)
- **Same kitchen**, flexible ordering!

Or like **a thermostat with preset modes**:
- **Cool to 72°F**: Default setting most people want
- **Override**: Can adjust to 68°F or 75°F if needed
- **Convenience**: One button for common case, detailed control when wanted

### The Power of Sensible Defaults

Default parameters embody **convention over configuration**:
```python
def send_email(to, subject, body, cc=None, bcc=None, priority='normal'):
    # Most emails don't need cc/bcc/priority changes
    # But they're available when needed!
```

This makes **common cases simple**, while keeping **complex cases possible**.

### Design Principle

Good defaults follow the **Principle of Least Surprise**:
- Defaults should be what users expect 90% of the time
- Reduces cognitive load
- Makes functions easier to use
- Professional libraries use this extensively

---

<div align="center">

![Python Default Parameter Types Diagram](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.29.png)

*Default parameters provide preset values that are used automatically unless the caller explicitly overrides them*

</div>

---

## Apply Default Parameters

Defining functions with default argument values


### Key Concepts

**Core principle**: def func(arg1, arg2=default_value):

### Syntax and Usage

```python
# Basic example will be shown in practical examples below
```

### Practical Examples

#### Example 1: Basic Default Parameters

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))              # Hello, Alice!
print(greet("Bob", "Hi"))          # Hi, Bob!
print(greet("Charlie", greeting="Hey"))  # Hey, Charlie!
```

#### Example 2: Multiple Defaults

```python
def create_user(username, email, role="user", active=True):
    return {
        "username": username,
        "email": email,
        "role": role,
        "active": active
    }

user1 = create_user("alice", "alice@example.com")
user2 = create_user("bob", "bob@example.com", role="admin")
user3 = create_user("charlie", "charlie@example.com", active=False)
```

#### Example 3: Mutable Default Gotcha

```python
# Bad - mutable default
def add_item_bad(item, items=[]):
    items.append(item)
    return items

print(add_item_bad(1))  # [1]
print(add_item_bad(2))  # [1, 2] - Unexpected!

# Good - use None
def add_item_good(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item_good(1))  # [1]
print(add_item_good(2))  # [2] - Expected!
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
