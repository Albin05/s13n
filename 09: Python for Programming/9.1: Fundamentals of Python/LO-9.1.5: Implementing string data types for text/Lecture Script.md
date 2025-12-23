### LO-5 Implement String Data Types (21 minutes)

### Hook (3 minutes)

**Say**: "Every app you use has text - usernames, messages, posts. In Python, that's all strings!"

```python
username = "alice_2024"
message = "Hello World!"
email = "user@example.com"
```

### String Basics (6 minutes)

**Say**: "Strings are text in quotes. Use single or double quotes - both work the same!"

```python
name = "Alice"
city = 'New York'
message = "Hello World"

print(type(name))  # <class 'str'>
```

**Key Points**:
- Strings can use "" or ''
- Must match opening and closing quotes
- Use quotes inside strings: "She said 'Hi'"

**String Concatenation**:
```python
first = "John"
last = "Doe"
full_name = first + " " + last  # John Doe
```

### String Methods (6 minutes)

**Say**: "Strings have built-in methods to modify and check text. These are super useful for data cleaning!"

```python
name = "alice"
print(name.upper())      # ALICE
print(name.capitalize()) # Alice
print(name.title())      # Alice

text = "  hello  "
print(text.strip())      # hello (removes spaces)

email = "USER@EXAMPLE.COM"
print(email.lower())     # user@example.com
```

**Real-World**: Always lowercase emails before saving to database!

### Practice (6 minutes)

**Say**: "Let's build an email address from parts."

```python
first = "john"
last = "doe"
domain = "example.com"

# Solution
email = first + "." + last + "@" + domain
print(email)  # john.doe@example.com

# Better way with f-string
email = f"{first}.{last}@{domain}"
print(email)
```

