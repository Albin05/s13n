# Editorials: Write If Statements

## Problem 1
```python
number = float(input("Enter a number: "))

if number > 0:
    print("Positive number")

if number < 0:
    print("Negative number")

if number == 0:
    print("Zero")
```

### Explanation
- Get number from user (use float to handle decimals)
- Three independent if statements check three different conditions
- Only the matching condition(s) will print

## Problem 2
```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")

if age >= 21:
    print("You can drink alcohol (in US)")

print("Thank you")
```

### Explanation
- Get age as integer
- First if checks 18+
- Second if checks 21+
- Last print always runs (not indented under any if)
- If age is 25, both if statements will execute

## Problem 3
```python
password = input("Enter password: ")
length = len(password)

if length >= 12:
    print("Strong length")

if length >= 8 and length < 12:
    print("Good length")

if length < 8:
    print("Too short")
```

### Explanation
- Get password and calculate length
- Three conditions check different length ranges
- Use `and` to specify range for "Good length"
- Only one condition will be true

### Alternative Solution
```python
password = input("Enter password: ")
length = len(password)

if length < 8:
    print("Too short")

if length >= 8:
    print("Good length")

if length >= 12:
    print("Strong length")
```

**Note**: This version prints both "Good length" and "Strong length" for passwords >= 12 characters.

## Problem 4
```python
attendance = float(input("Enter attendance %: "))
fee_status = input("Fee paid? (paid/unpaid): ").lower()

fee_paid = fee_status == "paid"

if attendance >= 75 and fee_paid:
    print("Eligible for exam")

if attendance < 75:
    print("Low attendance")

if not fee_paid:
    print("Fee not paid")
```

### Explanation
- Get attendance as float and fee status as string
- Convert fee status to boolean for easier checking
- First if requires BOTH conditions (using `and`)
- Second and third if statements check individual conditions
- All three if statements are independent

## Problem 5
```python
score = int(input("Enter your score: "))

# Grade assignments
if score >= 90 and score < 100:
    print("Grade: A")
    print("Excellent work!")

if score >= 80 and score < 90:
    print("Grade: B")
    print("Good job!")

if score >= 70 and score < 80:
    print("Grade: C")
    print("Satisfactory")

if score >= 60 and score < 70:
    print("Grade: D")
    print("Needs improvement")

if score < 60:
    print("Grade: F")
    print("Failed")

# Special cases
if score == 100:
    print("Perfect score!")

if score < 50:
    print("Please see instructor")
```

### Explanation
- Get score as integer
- Use multiple if statements with ranges for each grade
- Each range uses `and` to specify both lower and upper bounds
- Special cases at the end check for perfect score and very low scores
- Multiple statements can be indented under each if

### Sample Outputs

**Input: 95**
```
Grade: A
Excellent work!
```

**Input: 100**
```
Perfect score!
```

**Input: 45**
```
Grade: F
Failed
Please see instructor
```

**Input: 82**
```
Grade: B
Good job!
```

### Alternative with More Precise Ranges
```python
score = int(input("Enter your score: "))

# Grade A
if score >= 90:
    if score == 100:
        print("Perfect score!")
    print("Grade: A")
    print("Excellent work!")

# Grade B
if score >= 80 and score < 90:
    print("Grade: B")
    print("Good job!")

# Grade C
if score >= 70 and score < 80:
    print("Grade: C")
    print("Satisfactory")

# Grade D
if score >= 60 and score < 70:
    print("Grade: D")
    print("Needs improvement")

# Grade F
if score < 60:
    print("Grade: F")
    print("Failed")
    if score < 50:
        print("Please see instructor")
```

**Note**: This alternative uses nested if statements (an if inside another if). This will be covered in more detail in later lessons.
