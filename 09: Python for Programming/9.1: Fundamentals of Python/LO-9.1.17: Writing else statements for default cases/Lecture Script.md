### LO-17 Write Else Statements (20 minutes)

### Hook (2 minutes)

**Say**: "At a restaurant: IF you want pasta, we make pasta. ELIF you want pizza, we make pizza. ELSE we make our house special! That's else - the default option!"

```python
choice = "burger"

if choice == "pasta":
    print("Making pasta")
elif choice == "pizza":
    print("Making pizza")
else:
    print("House special!")  # Default!
```

### Basic Else (6 minutes)

**Say**: "else handles everything that didn't match previous conditions."

```python
age = 16

if age >= 18:
    print("Can vote")
else:
    print("Cannot vote yet")

# Output: Cannot vote yet
```

**Key Points**:
- `else` doesn't need a condition
- Catches EVERYTHING not caught by if/elif
- Must come after if (and optional elif)
- Only executes if all previous conditions were False

```python
score = 45

if score >= 60:
    print("Pass")
else:
    print("Fail")  # Runs for ANY score < 60
```

### Complete If-Elif-Else (6 minutes)

**Say**: "else catches EVERYTHING below 60. We don't need to write 'else score < 60'!"

```python
score = 55

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"  # Anything below 60

print(f"Grade: {grade}")  # F
```

**Real-World**: Login validation
```python
password = input("Enter password: ")

if len(password) >= 8:
    print("Password accepted")
else:
    print("Too short! Must be 8+ characters")
```

### When to Use Else (4 minutes)

**Say**: "Use else when you NEED a default action. Skip it when you don't!"

```python
# With else - always get output
if temperature > 30:
    print("Hot")
else:
    print("Not hot")

# Without else - may print nothing
if temperature > 30:
    print("Hot")
# Nothing prints if temperature <= 30
```

**Best Practice**: Use else for complete coverage
```python
status = "pending"

if status == "active":
    print("Process")
elif status == "inactive":
    print("Skip")
else:
    print(f"Unknown status: {status}")  # Catch unexpected values!
```

### Practice (2 minutes)

```python
x = 5

if x > 10:
    print("Big")
elif x > 5:
    print("Medium")
else:
    print("Small")  # Runs!

# Output: Small
```
