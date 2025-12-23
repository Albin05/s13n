# Pre-Read: Work with Regular Expressions

## Regular Expressions

Regular expressions (regex) are patterns used to match text:

```python
import re

# Find a pattern in a string
text = "My email is john@example.com"
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)

if match:
    print(f"Found: {match.group()}")
# Output: Found: john@example.com
```

## Basic Patterns

```python
import re

# Match exact text
if re.search(r"hello", "hello world"):
    print("Found 'hello'")

# Match digits
text = "Order number: 12345"
numbers = re.findall(r"\d+", text)
print(numbers)  # ['12345']

# Match words
words = re.findall(r"\w+", "Hello, World!")
print(words)  # ['Hello', 'World']
```

## Common Functions

```python
import re

# search() - find first match
result = re.search(r"\d+", "Age: 25")
print(result.group())  # 25

# findall() - find all matches
numbers = re.findall(r"\d+", "1 apple, 2 oranges, 3 bananas")
print(numbers)  # ['1', '2', '3']

# match() - match from start
if re.match(r"Hello", "Hello World"):
    print("Starts with Hello")
```
