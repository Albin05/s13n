# Lecture Script: LO-13 Use Comparison Operators

## [0:00-0:02] Hook (2 min)
**Say**: "Raise your hand if you're 18 or older. How did your brain just make that decision? You compared your age to 18! That's exactly what comparison operators do in Python."

**Write on board**: `your_age >= 18` → True or False?

## [0:02-0:08] Introduction to Comparison Operators (6 min)

**Say**: "Comparison operators let Python ask questions and get True/False answers."

**Live Code**:
```python
age = 20
print(age >= 18)  # True
```

**Key Points to Emphasize**:
- Result is always True or False (boolean)
- We're asking: "Is age greater than or equal to 18?"

### The Six Operators

**Write on board**:
```
==  Equal to
!=  Not equal to
>   Greater than
<   Less than
>=  Greater than or equal to
<=  Less than or equal to
```

**Live Code**:
```python
x = 10
y = 20

print(x == y)   # False
print(x != y)   # True
print(x < y)    # True
print(x > y)    # False
print(x <= 10)  # True
print(y >= 20)  # True
```

**Ask students**: "What do you notice about the results?"
*Expected answer*: They're all True or False

## [0:08-0:12] Common Operators in Detail (4 min)

### Equal To (`==`)

**Say**: "Double equals checks if two values are the same. VERY different from single equals!"

**Live Code**:
```python
# Single = assigns
age = 18

# Double == compares
print(age == 18)  # True
print(age == 20)  # False
```

**Emphasize**: `=` assigns, `==` compares

### Not Equal To (`!=`)

**Live Code**:
```python
status = "pending"
print(status != "completed")  # True
```

**Say**: "Read as: 'status is NOT equal to completed'"

### Greater/Less Than

**Live Code**:
```python
score = 85
print(score > 75)   # True - passed threshold
print(score >= 90)  # False - not excellent yet
```

**Point out**: `>` doesn't include equal, `>=` does!

## [0:12-0:15] Real-World Application (3 min)

**Say**: "Let's build a simple age checker!"

**Live Code**:
```python
age = int(input("Enter your age: "))

can_vote = age >= 18
can_drive = age >= 16
is_child = age < 13

print(f"Can vote: {can_vote}")
print(f"Can drive: {can_drive}")
print(f"Is child: {is_child}")
```

**Run with different inputs**:
- Try age = 15
- Try age = 20
- Show how results change

## [0:15-0:18] Common Mistakes (3 min)

**Say**: "Let me show you the #1 mistake beginners make."

**Live Code (intentional error)**:
```python
x = 5
if x = 5:  # SyntaxError!
    print("Five")
```

**Show error**, then **fix**:
```python
if x == 5:  # Correct!
    print("Five")
```

**Second common mistake**:
```python
user_age = input("Age: ")  # This is a STRING!
# user_age = "18"

# Need to convert
age = int(user_age)
print(age >= 18)  # Now works!
```

## [0:18-0:20] Practice & Wrap-up (2 min)

**Challenge**: "Without running it, what's the output?"

**Write on board**:
```python
a = 10
b = 10
print(a == b)
print(a > b)
print(a >= b)
```

**Give students 30 seconds**

**Reveal**:
```python
True   # equal
False  # not greater
True   # greater or equal (equal counts!)
```

**Closing Tip**: "When in doubt, use `print()` to see what the comparison returns. True and False are your friends!"

## Key Points to Reinforce
1. Comparisons return True or False
2. `=` assigns, `==` compares
3. `>=` includes equal, `>` doesn't
4. Mind your data types!
