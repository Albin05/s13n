# Editorials: Apply Logical Operators

## Problem 1
```python
age = int(input("Enter your age: "))
has_license = input("Do you have a license? (yes/no): ").lower() == "yes"

can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")
```

### Explanation
- Get age as integer
- Get license status and convert to boolean by comparing with "yes"
- Use `and` to check both conditions must be true
- Print result

## Problem 2
```python
is_weekend = input("Is it weekend? (yes/no): ").lower() == "yes"
is_sunny = input("Is it sunny? (yes/no): ").lower() == "yes"

good_day = is_weekend or is_sunny
print(f"Good day to go outside: {good_day}")
```

### Explanation
- Get both inputs and convert to booleans
- Use `or` because only one condition needs to be true
- If it's weekend OR sunny, it's a good day

## Problem 3
```python
score = int(input("Enter exam score: "))
submitted = input("Was assignment submitted? (yes/no): ").lower() == "yes"

passed = score >= 60 and submitted
excellent = score >= 90 and submitted

print(f"Passed: {passed}")
print(f"Excellent: {excellent}")
```

### Explanation
- Get score and submission status
- For passing: need score >= 60 AND assignment submitted
- For excellent: need score >= 90 AND assignment submitted
- Both require assignment to be submitted (using `and`)

## Problem 4
```python
username = input("Enter username: ")
password = input("Enter password: ")

valid_username = len(username) > 0
valid_password = len(password) >= 8

login_valid = valid_username and valid_password
print(f"Login valid: {login_valid}")
```

### Explanation
- Check username is not empty (length > 0)
- Check password meets minimum length (>= 8)
- Both must be true for valid login (using `and`)
- Store intermediate results in variables for clarity

### Alternative (More Concise)
```python
username = input("Enter username: ")
password = input("Enter password: ")

login_valid = len(username) > 0 and len(password) >= 8
print(f"Login valid: {login_valid}")
```

## Problem 5
```python
age = int(input("Enter your age: "))
has_parent = input("Is parent with you? (yes/no): ").lower() == "yes"
rating = input("Movie rating (G/PG/PG13/R): ").upper()

# Determine if can watch based on rating
if rating == "G" or rating == "PG":
    can_watch = True
elif rating == "PG13":
    can_watch = age >= 13 or has_parent
elif rating == "R":
    can_watch = age >= 17 or (age >= 13 and has_parent)
else:
    can_watch = False

print(f"Can watch movie: {can_watch}")
```

### Explanation
- Get age, parent presence, and movie rating
- For G and PG: anyone can watch
- For PG13: must be 13+ OR have parent (using `or`)
- For R: must be 17+ OR (13+ AND have parent)
  - The second condition uses `and` inside `or`
- Print final result

**Note**: This solution uses `if/elif/else` which will be covered in the next LO. 

### Alternative Without If Statements
```python
age = int(input("Enter your age: "))
has_parent = input("Is parent with you? (yes/no): ").lower() == "yes"
rating = input("Movie rating (G/PG/PG13/R): ").upper()

# Calculate for each rating
can_watch_g = rating == "G"
can_watch_pg = rating == "PG"
can_watch_pg13 = rating == "PG13" and (age >= 13 or has_parent)
can_watch_r = rating == "R" and (age >= 17 or (age >= 13 and has_parent))

# Combine all conditions with OR
can_watch = can_watch_g or can_watch_pg or can_watch_pg13 or can_watch_r

print(f"Can watch movie: {can_watch}")
```

### Explanation for Alternative
- Create a boolean variable for each rating type
- For PG13 and R, combine rating check with age/parent conditions
- Use `or` to combine all possibilities
- Only one needs to be True for can_watch to be True
