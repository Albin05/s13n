# Lecture Notes: Implement String Data Types

## Introduction
Strings represent text data in Python. They're one of the most commonly used data types.

---

<div align="center">

![Python String Character Indexing](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.5.png)

*Strings are immutable sequences of characters — Python provides rich methods for slicing, searching, and transforming text*

</div>

---

## Understanding Strings

### Why "String"?

The term "string" comes from "string of characters" - imagine beads on a string, where each bead is a character. A string is a **sequence** of characters strung together:

```
"Hello" = ['H', 'e', 'l', 'l', 'o']
```

### From Numbers to Text

Remember: computers only understand numbers (binary). So how do they store text?

Each character is assigned a number:
- 'A' = 65
- 'B' = 66
- 'a' = 97
- '!' = 33

This mapping is called **character encoding**:
- **ASCII** (1960s): 128 characters - English letters, digits, symbols
- **Unicode** (1991): 1 million+ characters - emoji, Chinese, Arabic, math symbols 😊

Python 3 uses Unicode by default - that's why you can write: `message = "Hello 世界 🌍"`

### Strings Are Immutable

**Important concept**: Once created, strings cannot be changed. Every "modification" creates a **new** string:

```python
name = "Alice"
name = name.upper()  # Creates new string "ALICE"
# The original "Alice" is discarded
```

Think of strings like **printed words on paper** - you can't erase and change them, you must print a new paper.

**Why immutable?**
- **Safety**: No accidental changes
- **Efficiency**: Same string can be reused in memory
- **Hashable**: Can be used as dictionary keys (you'll learn later)

### Real-World Analogy

A string is like a **text message**:
- Made up of individual characters (letters, numbers, spaces, emojis)
- Has a specific order (sequence matters!)
- Once sent, you can't edit it - only send a new message

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
