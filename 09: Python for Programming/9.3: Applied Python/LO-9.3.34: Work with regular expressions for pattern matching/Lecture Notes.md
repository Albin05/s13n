# Lecture Notes: Work with Regular Expressions

## Regular Expressions (Regex)

Regular expressions are powerful patterns used for matching and manipulating text. Python's `re` module provides regex functionality.


---

<div align="center">

![Python Regex re.search Pattern Match](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/LO-9.3.34.jpg)

*Regular expressions process strings through pattern-matching operations to find and manipulate text*

</div>

---

## Introduction

Regular expressions implement **pattern matching** - describing text patterns with a mini-language! This is **formal language theory** in practice - regular expressions define **regular languages** (simplest class in Chomsky hierarchy). Regex is **text surgery** - find, extract, replace with surgical precision!

### Why Regular Expressions are Essential

**Problem without regex**: Manual string parsing is painful:
```python
# TEDIOUS - checking email manually!
def is_email(text):
    has_at = "@" in text
    has_dot = "." in text[text.index("@"):]
    no_spaces = " " not in text
    return has_at and has_dot and no_spaces
# Fragile, incomplete, verbose!
```

**Solution with regex**: Pattern describes format:
```python
# POWERFUL - pattern expresses format!
import re
def is_email(text):
    return bool(re.match(r'^[\w.+-]+@[\w-]+\.[\w.]+$', text))
# One line, comprehensive!
```

**This is pattern-based matching** - describe what to find, not how!

### Historical Context

**Regular expressions** invented by **Stephen Kleene** (1956) - mathematical notation for regular languages! **Ken Thompson** (1968) built regex into **ed** text editor (Unix) - first practical implementation!

**grep** (1973) = "**G**lobally search **R**egular **E**xpression and **P**rint" - Unix command that made regex mainstream. **Perl** (1987) extended regex enormously - "Perl-compatible regex" (PCRE) became industry standard!

**Python's `re` module** implements PCRE-style patterns. **Finite automata** theory underpins regex - patterns compile to **state machines** for efficient matching. `re.compile()` creates optimized state machine!

### Real-World Analogies

**Regex like metal detector**:
- **Pattern**: What to scan for (ring, coin, nail)
- **Text**: The beach (data to search)
- **Match**: Beep! Found something matching pattern
**Define what to find, sweep across data!**

**Or like search filters**:
```python
# Like advanced search in email:
# From: *@company.com  →  r'From:.*@company\.com'
# Subject: Invoice #*  →  r'Subject: Invoice #\d+'
# Structured searching!
```

**Or like DNA pattern matching**:
- **Gene sequence**: ATCGGATCG... (text)
- **Pattern**: ATCG{2,4}AT (regex)
- **Match**: Find all matching gene segments
**Biology uses regex-like pattern matching!**

### Regex Performance

**Compile for reuse** - avoid recompiling same pattern:
```python
# SLOW - recompiles every call!
for line in million_lines:
    re.search(r'\d{3}-\d{4}', line)

# FAST - compile once, reuse!
phone_pattern = re.compile(r'\d{3}-\d{4}')
for line in million_lines:
    phone_pattern.search(line)
# 10-50x faster for repeated use!
```

---
### Basic Syntax

```python
import re

# r"pattern" - raw string (recommended for regex)
pattern = r"hello"
text = "hello world"

# Check if pattern exists
if re.search(pattern, text):
    print("Pattern found!")
```

## Common Re Module Functions

```python
import re

text = "Contact: john@email.com, phone: 123-456-7890"

# search() - Find first occurrence
email_match = re.search(r"\w+@\w+\.\w+", text)
if email_match:
    print(f"Email: {email_match.group()}")
# Output: Email: john@email.com

# findall() - Find all occurrences
digits = re.findall(r"\d+", text)
print(f"All numbers: {digits}")
# Output: All numbers: ['123', '456', '7890']

# match() - Match from beginning
if re.match(r"Contact", text):
    print("Text starts with 'Contact'")
# Output: Text starts with 'Contact'

# split() - Split string by pattern
parts = re.split(r"[,:]", text)
print(f"Split parts: {parts}")
# Output: Split parts: ['Contact', ' john@email.com', ' phone', ' 123-456-7890']

# sub() - Replace pattern
cleaned = re.sub(r"\d", "X", "My PIN is 1234")
print(cleaned)
# Output: My PIN is XXXX
```

## Pattern Syntax

```python
import re

# Literal characters
re.search(r"hello", "hello world")  # Matches "hello"

# . (dot) - Any character except newline
re.search(r"h.llo", "hello")  # Matches
re.search(r"h.llo", "hallo")  # Matches

# \d - Any digit [0-9]
re.findall(r"\d", "Room 123")  # ['1', '2', '3']

# \w - Any word character [a-zA-Z0-9_]
re.findall(r"\w+", "Hello_World123")  # ['Hello_World123']

# \s - Any whitespace
re.split(r"\s+", "Hello   World")  # ['Hello', 'World']

# \D - Any non-digit
# \W - Any non-word character
# \S - Any non-whitespace

# ^ - Start of string
re.match(r"^Hello", "Hello World")  # Matches

# $ - End of string
re.search(r"World$", "Hello World")  # Matches

# [] - Character class
re.findall(r"[aeiou]", "hello")  # ['e', 'o']
re.findall(r"[0-9]", "abc123")  # ['1', '2', '3']
re.findall(r"[a-z]", "Hello")  # ['e', 'l', 'l', 'o']
```

## Quantifiers

```python
import re

# * - 0 or more
re.findall(r"ab*", "a ab abb abbb")  # ['a', 'ab', 'abb', 'abbb']

# + - 1 or more
re.findall(r"ab+", "a ab abb abbb")  # ['ab', 'abb', 'abbb']

# ? - 0 or 1
re.findall(r"colou?r", "color colour")  # ['color', 'colour']

# {n} - Exactly n times
re.findall(r"\d{3}", "123 4567 89")  # ['123', '456']

# {n,} - n or more times
re.findall(r"\d{2,}", "1 12 123 1234")  # ['12', '123', '1234']

# {n,m} - Between n and m times
re.findall(r"\d{2,4}", "1 12 123 1234 12345")  # ['12', '123', '1234', '1234']
```

## Real-World Examples

### Example 1: Email Validation

```python
import re

def validate_email(email):
    """Validate email address format"""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

# Test emails
emails = [
    "john@example.com",
    "alice.smith@company.co.uk",
    "invalid.email",
    "@example.com",
    "test@.com"
]

for email in emails:
    status = "Valid" if validate_email(email) else "Invalid"
    print(f"{email}: {status}")
# Output:
# john@example.com: Valid
# alice.smith@company.co.uk: Valid
# invalid.email: Invalid
# @example.com: Invalid
# test@.com: Invalid
```

### Example 2: Phone Number Extraction

```python
import re

def extract_phone_numbers(text):
    """Extract US phone numbers from text"""
    # Pattern: (123) 456-7890 or 123-456-7890 or 1234567890
    pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    return re.findall(pattern, text)

text = """
Contact us at (555) 123-4567 or 555-987-6543.
Office: 555.111.2222
Emergency: 5559999999
"""

phones = extract_phone_numbers(text)
print("Phone numbers found:")
for phone in phones:
    print(f"  {phone}")
# Output:
# Phone numbers found:
#   (555) 123-4567
#   555-987-6543
#   555.111.2222
#   5559999999
```

### Example 3: URL Parsing

```python
import re

def extract_urls(text):
    """Extract URLs from text"""
    pattern = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?"
    return re.findall(pattern, text)

text = """
Visit our website at https://www.example.com
Check out http://blog.example.com/article/python-regex
Download from https://files.example.org/downloads/file.pdf
"""

urls = extract_urls(text)
print("URLs found:")
for url in urls:
    print(f"  {url}")
# Output:
# URLs found:
#   https://www.example.com
#   http://blog.example.com/article/python-regex
#   https://files.example.org/downloads/file.pdf

def parse_url(url):
    """Parse URL into components"""
    pattern = r"(https?)://([a-zA-Z0-9.-]+)(.*)"
    match = re.match(pattern, url)

    if match:
        return {
            "protocol": match.group(1),
            "domain": match.group(2),
            "path": match.group(3)
        }
    return None

url = "https://www.example.com/path/to/page"
components = parse_url(url)
print(f"\nURL components: {components}")
# Output:
# URL components: {'protocol': 'https', 'domain': 'www.example.com', 'path': '/path/to/page'}
```

### Example 4: Data Cleaning

```python
import re

def clean_text(text):
    """Clean and normalize text"""
    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove special characters except basic punctuation
    text = re.sub(r"[^a-zA-Z0-9\s.,!?-]", "", text)

    # Normalize whitespace around punctuation
    text = re.sub(r"\s*([.,!?])\s*", r"\1 ", text)

    return text.strip()

messy_text = """
Hello!!!   This    is    a    test...
It  has   @#$%  weird   characters  and   spacing!!!
"""

cleaned = clean_text(messy_text)
print(f"Original: {repr(messy_text)}")
print(f"Cleaned: {cleaned}")
# Output:
# Cleaned: Hello! This is a test. It has weird characters and spacing!

def extract_hashtags(text):
    """Extract hashtags from social media text"""
    pattern = r"#\w+"
    return re.findall(pattern, text)

tweet = "Learning #Python is fun! #Programming #AI #MachineLearning"
tags = extract_hashtags(tweet)
print(f"\nHashtags: {tags}")
# Output:
# Hashtags: ['#Python', '#Programming', '#AI', '#MachineLearning']
```

### Example 5: Password Validation

```python
import re

def validate_password(password):
    """
    Validate password strength:
    - At least 8 characters
    - Contains uppercase letter
    - Contains lowercase letter
    - Contains digit
    - Contains special character
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters"

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain an uppercase letter"

    if not re.search(r"[a-z]", password):
        return False, "Password must contain a lowercase letter"

    if not re.search(r"\d", password):
        return False, "Password must contain a digit"

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain a special character"

    return True, "Password is valid"

# Test passwords
passwords = [
    "weak",
    "NoDigits!",
    "noupperlower123!",
    "NoSpecial123",
    "Valid123!"
]

for pwd in passwords:
    valid, message = validate_password(pwd)
    print(f"{pwd}: {message}")
# Output:
# weak: Password must be at least 8 characters
# NoDigits!: Password must contain a digit
# noupperlower123!: Password must contain an uppercase letter
# NoSpecial123: Password must contain a special character
# Valid123!: Password is valid
```

## Groups and Capturing

```python
import re

# Capturing groups with ()
text = "Date: 2024-12-25"
match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)

if match:
    print(f"Full match: {match.group(0)}")  # 2024-12-25
    print(f"Year: {match.group(1)}")         # 2024
    print(f"Month: {match.group(2)}")        # 12
    print(f"Day: {match.group(3)}")          # 25

# Named groups
match = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", text)
if match:
    print(f"Year: {match.group('year')}")    # 2024
    print(f"Month: {match.group('month')}")  # 12
    print(f"Day: {match.group('day')}")      # 25

# Non-capturing group (?:...)
pattern = r"(?:Mr|Mrs|Ms)\. \w+"
names = re.findall(pattern, "Mr. Smith and Mrs. Jones")
print(names)  # ['Mr. Smith', 'Mrs. Jones']
```

## Flags

```python
import re

# re.IGNORECASE or re.I - Case insensitive
text = "Hello WORLD hello"
matches = re.findall(r"hello", text, re.IGNORECASE)
print(matches)  # ['Hello', 'hello']

# re.MULTILINE or re.M - ^ and $ match line boundaries
text = "Line 1\nLine 2\nLine 3"
lines = re.findall(r"^Line.*", text, re.MULTILINE)
print(lines)  # ['Line 1', 'Line 2', 'Line 3']

# re.DOTALL or re.S - . matches newlines too
text = "First\nSecond"
match = re.search(r"First.Second", text, re.DOTALL)
print(match.group() if match else "No match")  # First\nSecond
```

## Compiling Patterns

```python
import re

# Compile for reuse (more efficient)
email_pattern = re.compile(r"\w+@\w+\.\w+")

text1 = "Contact: john@example.com"
text2 = "Email: alice@company.org"

print(email_pattern.search(text1).group())  # john@example.com
print(email_pattern.search(text2).group())  # alice@company.org
```

## Key Takeaways

1. **re module**: Python's regex library
2. **Common functions**: search(), findall(), match(), sub(), split()
3. **Patterns**: \d (digit), \w (word), \s (space), . (any), ^ (start), $ (end)
4. **Quantifiers**: * (0+), + (1+), ? (0-1), {n}, {n,m}
5. **Groups**: () for capturing, (?P<name>) for named groups
6. **Flags**: re.I (ignore case), re.M (multiline), re.S (dotall)
7. **Raw strings**: Use r"pattern" to avoid escape issues
8. **Applications**: Validation, extraction, cleaning, parsing
