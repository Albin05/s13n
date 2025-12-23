# Lecture Script: LO-15 Write If Statements

## [0:00-0:02] Hook (2 min)
**Say**: "Imagine a security guard at a concert. They check: 'IF you have a ticket, you can enter.' That's exactly what an if statement does in Python - it guards a block of code!"

**Act it out**: Pretend to check a ticket and let someone through

## [0:02-0:08] Basic If Statement (6 min)

**Say**: "An if statement executes code ONLY when a condition is True."

**Write on board**:
```
if condition:
    code to run
```

**Live Code**:
```python
age = 20

if age >= 18:
    print("You are an adult")
```

**Run it** - Show output

**Key Points to Emphasize**:
1. `if` keyword
2. Condition (boolean expression)
3. Colon `:`
4. **Indentation** (4 spaces)

### Show When Condition is False

**Change code**:
```python
age = 15

if age >= 18:
    print("You are an adult")

print("Program continues")
```

**Run it** - Show that "You are an adult" doesn't print, but "Program continues" does

**Say**: "The if block only runs when the condition is True!"

## [0:08-0:12] Indentation (4 min)

**Say**: "In Python, indentation is REQUIRED. It's not just for looks!"

**Show correct indentation**:
```python
if age >= 18:
    print("You can vote")
    print("You are an adult")
print("End")
```

**Point out**: "First two lines are indented - they're INSIDE the if block. Last line is not - it ALWAYS runs."

### Show Indentation Error

**Intentionally remove indentation**:
```python
if age >= 18:
print("You can vote")  # Error!
```

**Run it** - Show the IndentationError

**Fix it** - Add indentation back

**Say**: "Always indent with 4 spaces after an if statement!"

## [0:12-0:16] Using Conditions (4 min)

**Say**: "You can use any boolean expression as the condition."

### With Comparison Operators

**Live Code**:
```python
score = 85

if score >= 60:
    print("You passed!")

if score >= 90:
    print("Excellent!")
```

**Run it** - Show only "You passed!" prints (85 < 90)

### With Logical Operators

**Live Code**:
```python
age = 20
has_license = True

if age >= 18 and has_license:
    print("You can drive")
```

**Run it** - Show output

**Change has_license to False and run again** - Show no output

## [0:16-0:20] Multiple If Statements (4 min)

**Say**: "You can have multiple if statements. Each one is checked independently!"

**Live Code**:
```python
temperature = 30

if temperature > 25:
    print("It's hot")

if temperature > 20:
    print("It's warm")

if temperature > 15:
    print("It's mild")
```

**Run it** - Show all three print!

**Ask**: "Why did all three print?"
*Expected answer*: Because all three conditions are true

## [0:20-0:23] Real-World Example (3 min)

**Say**: "Let's build a simple login checker!"

**Live Code**:
```python
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "secret":
    print("Login successful!")
    print("Welcome, admin!")

if username != "admin":
    print("Wrong username")

if password != "secret":
    print("Wrong password")
```

**Run with different inputs**:
1. Correct: admin, secret
2. Wrong username: user, secret
3. Wrong password: admin, wrong

## [0:23-0:25] Common Mistakes & Wrap-up (2 min)

**Say**: "Let me show you the most common mistakes!"

**Show on board**:
```python
# Mistake 1: Forgetting colon
if age >= 18  # SyntaxError!

# Mistake 2: Using = instead of ==
if age = 18:  # SyntaxError!

# Mistake 3: No indentation
if age >= 18:
print("Adult")  # IndentationError!
```

**Fix each one** and explain

**Challenge**: "Write an if statement that checks if a number is positive."

**Give students 30 seconds**

**Solution**:
```python
number = 5
if number > 0:
    print("Positive")
```

**Closing Tip**: "Remember: colon, then indent! And use `==` for comparison, not `=`!"

## Key Points to Reinforce
1. Syntax: `if condition:`
2. Indentation is REQUIRED (4 spaces)
3. Colon after condition
4. Use `==` not `=` for comparison
5. Multiple if statements are independent
