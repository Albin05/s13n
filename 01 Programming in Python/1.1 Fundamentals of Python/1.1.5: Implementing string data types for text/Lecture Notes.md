# Lecture Notes: Implement String Data Types

## Introduction
Strings represent text data in Python. They're one of the most commonly used data types.

---


## Creating Strings

### Using Quotes
```python
# Single quotes
name = 'Alice'

# Double quotes
message = "Hello, World!"

# Both work the same!
```

### Quotes Inside Strings
```python
# Use opposite quote type
text1 = "He said, 'Hello!'"
text2 = 'She said, "Hi!"'

# Or escape with backslash
text3 = "He said, \"Hello!\""
```

### Multi-line Strings
```python
long_text = """This is a
multi-line string that
spans several lines."""
```

---

## String Operations

### Concatenation (+)
```python
first = "Hello"
second = "World"
result = first + " " + second
print(result)  # "Hello World"
```

**Can't mix strings and numbers**:
```python
age = 25
# message = "Age: " + age  # ❌ Error!
message = "Age: " + str(age)  # ✅ Works!
```

### Repetition (*)
```python
laugh = "ha" * 3
print(laugh)  # "hahaha"

line = "=" * 20
print(line)  # "===================="
```

### Length
```python
name = "Alice"
length = len(name)
print(length)  # 5
```

---

## String Methods

### Upper and Lower Case
```python
name = "Alice"
print(name.upper())  # "ALICE"
print(name.lower())  # "alice"
```

### Strip Whitespace
```python
text = "  hello  "
print(text.strip())  # "hello"
```

### Replace
```python
text = "Hello World"
new_text = text.replace("World", "Python")
print(new_text)  # "Hello Python"
```

### Check Contents
```python
email = "user@example.com"
print(email.startswith("user"))  # True
print(email.endswith(".com"))    # True
print("@" in email)              # True
```

---

## Practical Examples

### Example 1: Full Name
```python
first_name = "Alice"
last_name = "Johnson"
full_name = first_name + " " + last_name
print(full_name)  # "Alice Johnson"
```

### Example 2: Email Creation
```python
username = "alice"
domain = "example.com"
email = username + "@" + domain
print(email)  # "alice@example.com"
```

### Example 3: Formatting Output
```python
name = "Bob"
age = 25
message = "Name: " + name + ", Age: " + str(age)
print(message)  # "Name: Bob, Age: 25"
```

---

## Key Takeaways
1. Strings are text in quotes
2. Use `+` to concatenate
3. Use `*` to repeat
4. Can't directly mix strings and numbers
5. Many useful string methods available
6. Use `len()` to get length
