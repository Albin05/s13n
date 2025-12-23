# Question Bank: Work with Regular Expressions

## Problem 1 (Easy)

**Title:** Extract All Digits

**Problem Statement:**
Write a function `extract_digits(text)` that extracts all individual digits from a string using regex.

**Input Format:**
A string containing text and digits.

**Output Format:**
A list of all individual digits as strings.

**Sample Input:**
```python
text = "Order 123 has 4 items, cost: $56.78"
print(extract_digits(text))
```

**Sample Output:**
```
['1', '2', '3', '4', '5', '6', '7', '8']
```

**Constraints:**
- Use re.findall()
- Extract individual digits only

---

## Problem 2 (Easy)

**Title:** Find All Words

**Problem Statement:**
Write a function `find_words(text)` that extracts all words (sequences of letters) from a string, ignoring punctuation and numbers.

**Input Format:**
A string with words, punctuation, and numbers.

**Output Format:**
A list of all words.

**Sample Input:**
```python
text = "Hello, World! How are you? 123"
print(find_words(text))
```

**Sample Output:**
```
['Hello', 'World', 'How', 'are', 'you']
```

**Constraints:**
- Use re.findall()
- Match only letter sequences

---

## Problem 3 (Medium)

**Title:** Validate Email Address

**Problem Statement:**
Write a function `is_valid_email(email)` that validates if a string is a properly formatted email address using regex. Valid format: username@domain.extension

**Input Format:**
A string potentially containing an email.

**Output Format:**
Boolean (True if valid, False otherwise).

**Sample Input:**
```python
print(is_valid_email("user@example.com"))
print(is_valid_email("invalid.email"))
print(is_valid_email("@example.com"))
```

**Sample Output:**
```
True
False
False
```

**Constraints:**
- Use re.match() or re.search()
- Pattern: letters/numbers/dots before @, letters/dots for domain, 2+ letters for extension

---

## Problem 4 (Medium)

**Title:** Extract and Format Dates

**Problem Statement:**
Write a function `extract_dates(text)` that finds all dates in YYYY-MM-DD format and returns them as a list of tuples (year, month, day).

**Input Format:**
A string containing dates in YYYY-MM-DD format.

**Output Format:**
List of tuples with (year, month, day).

**Sample Input:**
```python
text = "Important dates: 2024-12-25 and 2024-01-01"
print(extract_dates(text))
```

**Sample Output:**
```
[('2024', '12', '25'), ('2024', '01', '01')]
```

**Constraints:**
- Use capturing groups
- Pattern: YYYY-MM-DD format
- Return as tuples

---

## Problem 5 (Hard)

**Title:** Password Strength Checker

**Problem Statement:**
Write a function `check_password_strength(password)` that returns a dictionary with:
- 'valid': Boolean indicating if password meets all criteria
- 'score': Integer from 0-5 based on criteria met
- 'feedback': List of criteria not met

Criteria:
1. At least 8 characters long
2. Contains at least one uppercase letter
3. Contains at least one lowercase letter
4. Contains at least one digit
5. Contains at least one special character (!@#$%^&*)

**Input Format:**
A password string.

**Output Format:**
Dictionary with 'valid', 'score', and 'feedback' keys.

**Sample Input:**
```python
result = check_password_strength("Weak1")
print(result)
```

**Sample Output:**
```
{
    'valid': False,
    'score': 3,
    'feedback': ['Must be at least 8 characters', 'Must contain a special character']
}
```

**Constraints:**
- Use multiple regex patterns
- Check all 5 criteria
- Return detailed feedback
