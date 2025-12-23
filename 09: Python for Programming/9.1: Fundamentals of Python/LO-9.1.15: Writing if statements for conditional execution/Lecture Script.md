### LO-15 Write If Statements (20 minutes)

### Hook (2 minutes)

**Say**: "Imagine a security guard at a concert. They check: 'IF you have a ticket, you can enter.' That's exactly what an if statement does in Python - it guards a block of code!"

### Basic If Statement (6 minutes)

**Say**: "An if statement executes code ONLY when a condition is True."

```python
age = 20

if age >= 18:
    print("You are an adult")
```

### Indentation (4 minutes)

**Say**: "In Python, indentation is REQUIRED. It's not just for looks!"

```python
if age >= 18:
    print("You can vote")
    print("You are an adult")
print("End")
```

### Using Conditions (4 minutes)

**Say**: "You can use any boolean expression as the condition."

```python
score = 85

if score >= 60:
    print("You passed!")

if score >= 90:
    print("Excellent!")
```

### Multiple If Statements (4 minutes)

**Say**: "You can have multiple if statements. Each one is checked independently!"

```python
temperature = 30

if temperature > 25:
    print("It's hot")

if temperature > 20:
    print("It's warm")

if temperature > 15:
    print("It's mild")
```

### Real-World Example (3 minutes)

**Say**: "Let's build a simple login checker!"

```python
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "secret":
    print("Login successful!")
    print("Welcome, admin!")

if username != "admin":
    print("Wrong username")

```

### Common Mistakes & Wrap-up (2 minutes)

**Say**: "Let me show you the most common mistakes!"

```python
# Mistake 1: Forgetting colon
if age >= 18  # SyntaxError!

# Mistake 2: Using = instead of ==
if age = 18:  # SyntaxError!

# Mistake 3: No indentation
if age >= 18:
print("Adult")  # IndentationError!
```

