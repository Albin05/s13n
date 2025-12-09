# Lecture Notes: Write Elif Statements

## Elif Statements

The `elif` (else if) statement allows you to check multiple conditions where **only one block of code will execute**.


---

<div align="center">

![Flowchart showing decision making](https://images.unsplash.com/photo-1559027615-cd4628902d4a?w=800&q=80)

*Control flow determines the execution path of your program*

</div>

---
### Basic Syntax

```python
if condition1:
    # Runs if condition1 is True
elif condition2:
    # Runs if condition1 is False and condition2 is True
elif condition3:
    # Runs if condition1 and condition2 are False and condition3 is True
```

**Key Characteristics**:
1. `elif` must come after an `if` statement
2. You can have multiple `elif` statements
3. Only the **first True condition** executes
4. Once a match is found, remaining conditions are skipped

## Why Use Elif?

### Problem with Multiple If Statements

```python
score = 85

if score >= 90:
    grade = "A"

if score >= 80:
    grade = "B"  # This runs!

if score >= 70:
    grade = "C"  # This also runs!

print(grade)  # C (last assignment wins!)
```

**Issues**:
- All conditions are checked (inefficient)
- Multiple blocks might execute
- Results can be unexpected

### Solution with Elif

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"  # This runs and STOPS
elif score >= 70:
    grade = "C"  # Never checked

print(grade)  # B (correct!)
```

**Benefits**:
- Only one block executes
- More efficient (stops after first match)
- Clearer intent

## Examples

### Example 1: Grade Calculator

```python
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")

# Output: Grade: C
```

### Example 2: Age Categories

```python
age = 15

if age >= 65:
    print("Senior citizen")
elif age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")  # This runs
elif age >= 3:
    print("Child")

# Output: Teenager
```

## Order Matters!

The order of conditions is crucial because Python checks from top to bottom:

### Incorrect Order

```python
score = 95

if score >= 60:  # This is checked first
    print("Pass")  # This runs for 95!
elif score >= 90:  # Never reached!
    print("Excellent")
```

### Correct Order

```python
score = 95

if score >= 90:  # Check specific conditions first
    print("Excellent")  # This runs
elif score >= 60:  # More general conditions later
    print("Pass")
```

**Rule**: Put more **specific** conditions before more **general** ones.

## Real-World Applications

### BMI Calculator

```python
bmi = 27.5

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"  # This runs
else:
    category = "Obese"

print(f"BMI Category: {category}")
```

## Key Takeaways

1. **Mutually exclusive**: Only one block executes in an if-elif chain
2. **Order matters**: Check specific conditions before general ones
3. **First match wins**: Stops at first True condition
4. **Must follow if**: `elif` can't be used alone
5. **More efficient**: Stops checking once a match is found
