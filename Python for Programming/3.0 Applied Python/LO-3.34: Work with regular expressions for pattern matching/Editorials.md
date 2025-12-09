# Editorials: Work with Regular Expressions

## Problem 1: Extract All Digits

```python
import re

def extract_digits(text):
    return re.findall(r"\d", text)

# Test
text = "Order 123 has 4 items, cost: $56.78"
print(extract_digits(text))
# Output: ['1', '2', '3', '4', '5', '6', '7', '8']
```

### Explanation
`\d` matches any single digit. `findall()` returns all matches as a list.

---

## Problem 2: Find All Words

```python
import re

def find_words(text):
    return re.findall(r"[a-zA-Z]+", text)

# Test
text = "Hello, World! How are you? 123"
print(find_words(text))
# Output: ['Hello', 'World', 'How', 'are', 'you']
```

### Explanation
`[a-zA-Z]+` matches one or more consecutive letters (uppercase or lowercase).

---

## Problem 3: Validate Email Address

```python
import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

# Test
print(is_valid_email("user@example.com"))  # True
print(is_valid_email("invalid.email"))     # False
print(is_valid_email("@example.com"))      # False
```

### Explanation
Pattern breakdown:
- `^` - Start of string
- `[a-zA-Z0-9._%+-]+` - Username (letters, digits, special chars)
- `@` - Literal @
- `[a-zA-Z0-9.-]+` - Domain
- `\.` - Literal dot
- `[a-zA-Z]{2,}` - Extension (2+ letters)
- `$` - End of string

---

## Problem 4: Extract and Format Dates

```python
import re

def extract_dates(text):
    pattern = r"(\d{4})-(\d{2})-(\d{2})"
    matches = re.findall(pattern, text)
    return matches

# Test
text = "Important dates: 2024-12-25 and 2024-01-01"
print(extract_dates(text))
# Output: [('2024', '12', '25'), ('2024', '01', '01')]
```

### Explanation
Capturing groups `()` extract year, month, day separately. `findall()` with groups returns list of tuples.

---

## Problem 5: Password Strength Checker

```python
import re

def check_password_strength(password):
    feedback = []
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Must be at least 8 characters")

    # Check uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Must contain an uppercase letter")

    # Check lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Must contain a lowercase letter")

    # Check digit
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Must contain a digit")

    # Check special character
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Must contain a special character")

    return {
        'valid': score == 5,
        'score': score,
        'feedback': feedback
    }

# Test
result = check_password_strength("Weak1")
print(result)
```

### Explanation
Each regex pattern checks for a specific criterion. Score increments for each met criterion, and feedback lists unmet criteria.
