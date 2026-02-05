# Lecture Script: LO-9.3.34 Work with Regular Expressions for Pattern Matching

## [0:00-0:02] Hook (2 min)
**Say**: "You need to extract all email addresses from 10,000 log files. Manual searching? Hours. Regular expression? One line: re.findall(r'\w+@\w+\.\w+', text). Regex is pattern matching on steroids — find, validate, extract, and replace text with surgical precision!"

**Demo**:
```python
import re

text = "Contact us at support@example.com or sales@company.org"

# Extract all emails
emails = re.findall(r'\w+@\w+\.\w+', text)
print(emails)
# ['support@example.com', 'sales@company.org']

# Validate an email
email = "user@domain.com"
if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
    print("Valid email!")
```

**Say**: "That's regex power! Let's master it."

## [0:02-0:06] Basic Pattern Matching (4 min)

**Say**: "Start simple: re.search() finds a pattern, re.findall() finds all matches."

**Live Code**:
```python
import re

text = "The quick brown fox jumps over the lazy dog"

# search() - find first occurrence
match = re.search(r"fox", text)
if match:
    print(f"Found: {match.group()}")  # Found: fox
    print(f"Position: {match.start()}-{match.end()}")  # Position: 16-19

# findall() - find all occurrences
text2 = "I have 3 cats, 2 dogs, and 5 birds"
numbers = re.findall(r"\d", text2)
print(f"Numbers: {numbers}")  # ['3', '2', '5']

# match() - match from beginning
if re.match(r"The", text):
    print("Starts with 'The'")  # Starts with 'The'

if not re.match(r"quick", text):
    print("Doesn't start with 'quick'")

# sub() - replace pattern
cleaned = re.sub(r"\d", "X", "My PIN is 1234")
print(cleaned)  # My PIN is XXXX
```

**Point out**: "search() finds anywhere, match() requires start of string, findall() gets all matches!"

**Emphasize**: "Always use raw strings r\"pattern\" for regex to avoid escape character issues!"

## [0:06-0:10] Pattern Syntax Basics (4 min)

**Say**: "Regex has special characters that match patterns, not just literal text."

**Live Code**:
```python
import re

# . (dot) - any character except newline
print(re.findall(r"c.t", "cat cot cut c9t"))
# ['cat', 'cot', 'cut', 'c9t']

# \d - any digit [0-9]
print(re.findall(r"\d+", "Room 123, Floor 4"))
# ['123', '4']

# \w - word character [a-zA-Z0-9_]
print(re.findall(r"\w+", "Hello_World123!"))
# ['Hello_World123']

# \s - whitespace
print(re.split(r"\s+", "Split   by    spaces"))
# ['Split', 'by', 'spaces']

# ^ - start of string, $ - end of string
print(bool(re.match(r"^Hello", "Hello World")))  # True
print(bool(re.search(r"World$", "Hello World")))  # True

# [] - character class
print(re.findall(r"[aeiou]", "hello"))  # ['e', 'o']
print(re.findall(r"[0-9]", "abc123"))   # ['1', '2', '3']
print(re.findall(r"[a-z]", "Hello"))    # ['e', 'l', 'l', 'o']
```

**Point out**: "These are building blocks! Combine them for powerful patterns."

## [0:10-0:13] Quantifiers (3 min)

**Say**: "Quantifiers specify how many times a pattern should match."

**Live Code**:
```python
import re

# * - 0 or more
print(re.findall(r"ab*", "a ab abb abbb"))
# ['a', 'ab', 'abb', 'abbb']

# + - 1 or more
print(re.findall(r"ab+", "a ab abb abbb"))
# ['ab', 'abb', 'abbb']

# ? - 0 or 1 (optional)
print(re.findall(r"colou?r", "color colour"))
# ['color', 'colour']

# {n} - exactly n times
print(re.findall(r"\d{3}", "123 4567 89"))
# ['123', '456']

# {n,} - n or more times
print(re.findall(r"\d{2,}", "1 12 123 1234"))
# ['12', '123', '1234']

# {n,m} - between n and m times
print(re.findall(r"\d{2,4}", "1 12 123 1234 12345"))
# ['12', '123', '1234', '1234']

# Combining patterns
print(re.findall(r"\w+@\w+", "Contact: user@domain"))
# ['user@domain']
```

**Emphasize**: "+ means 'one or more', * means 'zero or more'. Choose wisely!"

## [0:13-0:16] Real-World Example: Email Validation (3 min)

**Say**: "Let's build a proper email validator step by step."

**Live Code**:
```python
import re

def validate_email(email):
    """
    Validate email format:
    - username: letters, numbers, dots, underscores, hyphens
    - @ symbol
    - domain: letters, numbers, dots, hyphens
    - extension: 2+ letters
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

# Test valid emails
valid_emails = [
    "user@example.com",
    "john.doe@company.co.uk",
    "alice_123@test-domain.com"
]

for email in valid_emails:
    print(f"{email}: {validate_email(email)}")
# user@example.com: True
# john.doe@company.co.uk: True
# alice_123@test-domain.com: True

# Test invalid emails
invalid_emails = [
    "invalid.email",
    "@example.com",
    "user@",
    "user@domain"
]

for email in invalid_emails:
    print(f"{email}: {validate_email(email)}")
# invalid.email: False
# @example.com: False
# user@: False
# user@domain: False
```

**Say**: "Break down the pattern: ^starts, [char class]+, @symbol, domain pattern, .ext$ends"

## [0:16-0:19] Real-World Example: Phone Number Extraction (3 min)

**Say**: "Extract phone numbers in various formats from text."

**Live Code**:
```python
import re

def extract_phone_numbers(text):
    """
    Extract US phone numbers:
    - (123) 456-7890
    - 123-456-7890
    - 1234567890
    """
    pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    return re.findall(pattern, text)

text = """
Contact information:
Office: (555) 123-4567
Mobile: 555-987-6543
Fax: 555.111.2222
Emergency: 5559999999
"""

phones = extract_phone_numbers(text)
print("Phone numbers found:")
for phone in phones:
    print(f"  {phone}")
# (555) 123-4567
# 555-987-6543
# 555.111.2222
# 5559999999

# Clean phone numbers to standard format
def clean_phone(phone):
    """Extract only digits"""
    return re.sub(r"\D", "", phone)

for phone in phones:
    cleaned = clean_phone(phone)
    formatted = f"({cleaned[:3]}) {cleaned[3:6]}-{cleaned[6:]}"
    print(f"{phone:20} -> {formatted}")
```

**Point out**: "\(? makes parentheses optional, [-.\s]? makes separators optional!"

## [0:19-0:21] Groups and Capturing (2 min)

**Say**: "Parentheses create groups — extract specific parts of a match."

**Live Code**:
```python
import re

# Capturing groups
text = "Date: 2024-12-25"
match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)

if match:
    print(f"Full match: {match.group(0)}")  # 2024-12-25
    print(f"Year: {match.group(1)}")        # 2024
    print(f"Month: {match.group(2)}")       # 12
    print(f"Day: {match.group(3)}")         # 25

# Named groups - even better!
match = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", text)
if match:
    print(f"Year: {match.group('year')}")    # 2024
    print(f"Month: {match.group('month')}")  # 12
    print(f"Day: {match.group('day')}")      # 25

# Extract all matches with groups
text = "Alice: 25, Bob: 30, Charlie: 35"
matches = re.findall(r"(\w+): (\d+)", text)
for name, age in matches:
    print(f"{name} is {age} years old")
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old
```

**Emphasize**: "Named groups (?P<name>) make code more readable than numbered groups!"

## [0:21-0:23] Real-World Example: Data Cleaning (2 min)

**Say**: "Regex is perfect for cleaning messy text data."

**Live Code**:
```python
import re

def clean_text(text):
    """Clean and normalize text"""
    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove special characters (keep letters, numbers, basic punctuation)
    text = re.sub(r"[^a-zA-Z0-9\s.,!?-]", "", text)

    # Normalize whitespace around punctuation
    text = re.sub(r"\s*([.,!?])\s*", r"\1 ", text)

    return text.strip()

messy = """Hello!!!   This    is    @#$%  messy   text...
With  weird   spacing  and   characters!!!"""

cleaned = clean_text(messy)
print(f"Original:\n{messy}\n")
print(f"Cleaned:\n{cleaned}")
# Original:
# Hello!!!   This    is    @#$%  messy   text...
# With  weird   spacing  and   characters!!!
#
# Cleaned:
# Hello! This is messy text. With weird spacing and characters!

# Extract hashtags from social media
tweet = "Learning #Python is fun! #Programming #AI #MachineLearning"
hashtags = re.findall(r"#\w+", tweet)
print(f"\nHashtags: {hashtags}")
# ['#Python', '#Programming', '#AI', '#MachineLearning']
```

**Say**: "Notice how we chain multiple re.sub() calls to progressively clean the text!"

## [0:23-0:24] Practice Challenge (1 min)

**Challenge**: "Write a regex to validate passwords: 8+ chars, 1 uppercase, 1 lowercase, 1 digit, 1 special char."

**Skeleton**:
```python
import re

def validate_password(password):
    # TODO: Check password requirements
    # At least 8 characters
    # Contains uppercase
    # Contains lowercase
    # Contains digit
    # Contains special character
    pass

# Test
passwords = ["weak", "NoDigits!", "noupperlower123!", "Valid123!"]
for pwd in passwords:
    print(f"{pwd}: {validate_password(pwd)}")
```

**Solution** (show after 1 minute):
```python
def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True
```

## [0:24-0:25] Wrap-up (1 min)

**Key Points**:
1. **Core functions**: search(), findall(), match(), sub(), split()
2. **Pattern basics**: . (any), \d (digit), \w (word), \s (space)
3. **Anchors**: ^ (start), $ (end)
4. **Quantifiers**: * (0+), + (1+), ? (0-1), {n}, {n,m}
5. **Groups**: () capture, (?P<name>) named groups

**Common Patterns**:
- Email: r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
- Phone: r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
- URL: r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
- Date: r"\d{4}-\d{2}-\d{2}"

**Common Mistakes**:
- Not using raw strings r"pattern"
- Forgetting to escape special characters (\. not .)
- Greedy vs non-greedy matching (.*? vs .*)
- Not testing edge cases

**Real-World Use Cases**:
- Validating user input (emails, phones, passwords)
- Extracting structured data from text
- Cleaning and normalizing text data
- Log file parsing
- Web scraping

**Closing**: "Regex is powerful but can get complex fast. Start simple, test thoroughly, and remember: use raw strings, test edge cases, and don't try to parse HTML with regex (use a parser)!"
