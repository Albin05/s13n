# Pre-Read: Implement String Data Types

## What are Strings?

**Strings** are text data - any characters in quotes.

```python
name = "Alice"
message = 'Hello, World!'
email = "user@example.com"
```

Single `'` or double `"` quotes both work!

## String Operations

### Concatenation (Combining)
```python
first = "Hello"
second = "World"
combined = first + " " + second
print(combined)  # "Hello World"
```

### Repetition
```python
laugh = "ha" * 3
print(laugh)  # "hahaha"
```

### Length
```python
name = "Alice"
print(len(name))  # 5
```

## Special Characters
```python
# Use opposite quotes inside
message = "He said, 'Hello!'"
message = 'She said, "Hi!"'

# Or escape quotes
message = "He said, \"Hello!\""
```

## When to Use Strings
✅ Names, messages, text, emails, URLs, addresses

## Try It
```python
first_name = "Alice"
last_name = "Johnson"
full_name = first_name + " " + last_name
print(full_name)
```
