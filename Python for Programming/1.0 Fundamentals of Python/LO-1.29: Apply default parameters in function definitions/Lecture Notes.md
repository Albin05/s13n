# Lecture Notes: Apply Default Parameters

## Apply Default Parameters

Defining functions with default argument values


---

<div align="center">

![Function machine concept - input to output](https://images.unsplash.com/photo-1581291518857-4e27b48ff24e?w=800&q=80)

*Functions are reusable blocks of code that take inputs and return outputs*

</div>

---
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
