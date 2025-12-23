# Lecture Script: Writing Nested Conditionals for Complex Logic

**Duration:** 20-25 minutes
**Learning Objective:** Students will be able to write nested if statements to handle complex decision-making with multiple conditions.

---

## [0:00-0:02] Hook (2 minutes)

**Open with a relatable scenario:**

> "Imagine you're applying for a credit card. The bank doesn't just check ONE thing - they check your age, your income, your credit score, AND your employment status. How do we write code that makes decisions based on MULTIPLE criteria? That's where nested conditionals come in!"

**Interactive question:**
"Who has played a video game where you needed to unlock certain levels? Like you need to be level 10 AND have a special item AND complete a quest?"

**The connection:**
> "That's exactly how nested conditionals work! We check one condition, and INSIDE that check, we check another condition. It's like security checkpoints at an airport - you go through multiple layers of verification."

**Live demo - show the power:**
```python
age = 25
has_license = True
has_car = True

if age >= 18:
    if has_license:
        if has_car:
            print("You can drive!")
        else:
            print("You need a car")
    else:
        print("You need a license first")
else:
    print("You're too young to drive")
```

---

## [0:02-0:08] Main Concept: Basic Nested Conditionals (6 minutes)

### Part 1: What is Nesting? (2 minutes)

**Explain the concept:**
> "Nesting means putting one if statement INSIDE another. The outer condition must be true before Python even looks at the inner condition."

**Live code - Simple example:**
```python
temperature = 85
is_sunny = True

if temperature > 80:
    print("It's hot!")
    if is_sunny:
        print("And it's sunny - perfect beach weather!")
    else:
        print("But it's cloudy")
else:
    print("It's not hot today")
```

**Run this and show output:**
```
It's hot!
And it's sunny - perfect beach weather!
```

**Explain the flow:**
> "Python first checks: Is temperature > 80? YES. So it prints 'It's hot!' and enters the outer if block. Then inside, it checks: Is it sunny? YES. So it prints the beach message."

**Change temperature to 70 and run again:**
```python
temperature = 70
is_sunny = True

if temperature > 80:
    print("It's hot!")
    if is_sunny:
        print("And it's sunny - perfect beach weather!")
    else:
        print("But it's cloudy")
else:
    print("It's not hot today")
```

**Output:**
```
It's not hot today
```

**Emphasize:**
> "Notice the inner if statement NEVER ran! Python saw the outer condition was False and skipped the entire block. The inner condition is only checked if the outer condition is True."

### Part 2: Indentation is CRITICAL (2 minutes)

**Draw on board:**
```
if outer_condition:
    # Outer block
    statement_A
    if inner_condition:
        # Inner block
        statement_B
    else:
        # Inner else
        statement_C
else:
    # Outer else
    statement_D
```

**Demonstrate the importance:**
```python
# CORRECT nesting
score = 85
passed = True

if score >= 60:
    print("Score is passing")
    if passed:
        print("Status: PASS")
    else:
        print("Status: INCOMPLETE")
else:
    print("Score is failing")
```

**Show WRONG indentation:**
```python
# WRONG - indentation error
score = 85
passed = True

if score >= 60:
    print("Score is passing")
if passed:  # NOT nested! This is a separate if
    print("Status: PASS")
else:
    print("Status: INCOMPLETE")
```

**Explain the difference:**
> "In the first version, `if passed:` is nested INSIDE the outer if - it only runs when score >= 60. In the second version, it's a SEPARATE if statement that always runs. Indentation determines structure!"

### Part 3: Multiple Levels (2 minutes)

**Show deeper nesting:**
```python
username = "admin"
password = "secret"
has_2fa = True

if username == "admin":
    print("Username correct")
    if password == "secret":
        print("Password correct")
        if has_2fa:
            print("Login successful!")
        else:
            print("2FA required")
    else:
        print("Wrong password")
else:
    print("Unknown user")
```

**Test with correct credentials:**
```
Username correct
Password correct
Login successful!
```

**Test with wrong password:**
```python
password = "wrong"
```
```
Username correct
Wrong password
```

**Explain:**
> "Three levels of security! Each level is only checked if the previous level passed. This is like airport security - first your ticket, then your ID, then your boarding pass."

---

## [0:08-0:14] Pattern: Decision Trees (6 minutes)

### Part 1: Age Classification (2 minutes)

**Real-world example:**
```python
age = 25

if age >= 0:
    if age < 13:
        category = "Child"
    elif age < 20:
        category = "Teenager"
    elif age < 60:
        category = "Adult"
    else:
        category = "Senior"
    print(f"Category: {category}")
else:
    print("Invalid age!")
```

**Walk through the logic:**
- First: Is age valid (>= 0)?
- If yes, classify into categories
- If no, reject as invalid

**Emphasize validation:**
> "Always validate input first! The outer if checks if age makes sense before trying to classify it."

### Part 2: Ticket Pricing (2 minutes)

**Complex pricing logic:**
```python
age = 15
is_student = True

if age < 18:
    # Child pricing
    if is_student:
        price = 5
    else:
        price = 7
else:
    # Adult pricing
    if is_student:
        price = 8
    else:
        price = 10

print(f"Ticket price: ${price}")
```

**Draw a decision tree on board:**
```
Age < 18?
├─ YES: Child
│   ├─ Student? → $5
│   └─ Not student? → $7
└─ NO: Adult
    ├─ Student? → $8
    └─ Not student? → $10
```

**Show all 4 outcomes:**
```python
# Test case 1: Child student
age, is_student = 15, True  # Output: $5

# Test case 2: Child non-student
age, is_student = 15, False  # Output: $7

# Test case 3: Adult student
age, is_student = 25, True  # Output: $8

# Test case 4: Adult non-student
age, is_student = 25, False  # Output: $10
```

### Part 3: Grade Calculator (2 minutes)

**Nested elif chains:**
```python
score = 85
bonus_applied = True

if score >= 0 and score <= 100:
    # Apply bonus if eligible
    if bonus_applied:
        score = min(score + 5, 100)
        print(f"Bonus applied! New score: {score}")

    # Assign grade
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Grade: {grade}")
else:
    print("Invalid score!")
```

**Explain the structure:**
> "First, validate the score. Then apply bonus if eligible. Finally, assign the grade. Each step builds on the previous one."

---

## [0:14-0:18] Common Patterns and Best Practices (4 minutes)

### Part 1: Avoid Deep Nesting (2 minutes)

**Show a BAD example:**
```python
# TOO DEEP - hard to read!
if condition1:
    if condition2:
        if condition3:
            if condition4:
                if condition5:
                    print("All conditions met")
```

**Show the BETTER approach:**
```python
# BETTER - use 'and' operator
if condition1 and condition2 and condition3 and condition4 and condition5:
    print("All conditions met")
```

**Another alternative:**
```python
# BETTER - early exit
if not condition1:
    print("Failed check 1")
elif not condition2:
    print("Failed check 2")
elif not condition3:
    print("Failed check 3")
else:
    print("All conditions met")
```

**Rule of thumb:**
> "If you have more than 3-4 levels of nesting, consider refactoring. Use `and`/`or` operators or early exits to keep code readable."

### Part 2: Clear Error Messages (1 minute)

**Good practice:**
```python
username = "john"
password = "pass123"

if username:
    if password:
        if len(password) >= 8:
            print("Login successful")
        else:
            print("Password too short (minimum 8 characters)")
    else:
        print("Password cannot be empty")
else:
    print("Username cannot be empty")
```

**Explain:**
> "Each else provides a SPECIFIC error message. This helps users understand exactly what went wrong!"

### Part 3: Test All Paths (1 minute)

**Emphasize testing:**
```python
# Make sure to test EVERY path!
age = 15
has_permission = True

if age >= 18:
    print("Access granted")
else:
    if has_permission:
        print("Access granted with parental permission")
    else:
        print("Access denied")
```

**Show the paths:**
> "This has THREE possible outcomes:
> 1. age >= 18 → Access granted
> 2. age < 18 AND has_permission → Access granted with permission
> 3. age < 18 AND NOT has_permission → Access denied
>
> Test ALL three scenarios!"

---

## [0:18-0:22] Practice Time (4 minutes)

**Exercise 1: Restaurant Bill (1.5 minutes)**
> "Write code that calculates a tip based on bill amount and service quality. If bill > $50 AND service is 'excellent', tip is 20%. If bill > $50 AND service is 'good', tip is 15%. Otherwise, tip is 10%."

```python
# Solution
bill = 75
service = "excellent"

if bill > 50:
    if service == "excellent":
        tip_percent = 0.20
    else:
        tip_percent = 0.15
else:
    tip_percent = 0.10

tip = bill * tip_percent
print(f"Tip: ${tip:.2f}")
```

**Exercise 2: Access Control (1.5 minutes)**
> "Write code for a building security system. If person has_keycard AND pin_correct AND is_business_hours, grant access. If they have keycard and PIN but it's after hours, check if is_authorized_personnel."

```python
# Solution
has_keycard = True
pin_correct = True
is_business_hours = False
is_authorized_personnel = True

if has_keycard:
    if pin_correct:
        if is_business_hours:
            print("Access granted")
        else:
            if is_authorized_personnel:
                print("Access granted (after hours)")
            else:
                print("Access denied: Not authorized for after-hours")
    else:
        print("Access denied: Incorrect PIN")
else:
    print("Access denied: No keycard")
```

**Walk around and help students with common issues:**
- Forgetting colons after if statements
- Wrong indentation levels
- Missing else blocks

---

## [0:22-0:25] Wrap-up and Key Takeaways (3 minutes)

**Summarize the main points:**

1. **Nesting means if inside if**: Outer must be True before inner is checked
2. **Indentation defines structure**: Each nested level is indented 4 spaces
3. **Validate first**: Check inputs before processing
4. **Specific error messages**: Help users understand failures
5. **Avoid deep nesting**: Use `and`/`or` or early exits for readability
6. **Test all paths**: Every combination should be verified

**Visual summary on board:**
```
if outer_condition:
    # This runs if outer is True
    if inner_condition:
        # This runs if BOTH are True
    else:
        # This runs if outer is True but inner is False
else:
    # This runs if outer is False
```

**Real-world reminder:**
> "Nested conditionals are everywhere: login systems, shopping carts, game logic, form validation. Master this and you can handle any complex decision-making!"

**Common mistakes to avoid:**
- Missing colons
- Wrong indentation
- Not testing all paths
- Too many nesting levels

**Preview next lesson:**
> "Next time, we'll learn about while loops - how to repeat code until a condition becomes false. This is perfect for things like 'keep asking for password until correct'!"

**Final check question:**
"Quick quiz: If the outer condition is False, does Python check the inner condition?"

**Expected answer:** "No! Python skips the entire outer block if the condition is False."

---

## Teaching Tips

1. **Use real-world examples** - Security systems, pricing, permissions
2. **Draw decision trees** - Visual helps students understand flow
3. **Live code everything** - Show results immediately
4. **Test both paths** - Always show True AND False cases
5. **Emphasize indentation** - Use a linter or show errors live
6. **Start simple** - Two levels first, then add complexity

## Common Student Questions

**Q: "How many levels of nesting can I have?"**
A: "Technically unlimited, but practically keep it to 3-4 levels max. Beyond that, use and/or operators or refactor into functions."

**Q: "What's the difference between nested if and using 'and'?"**
A: "Nested ifs can have different actions at each level (like error messages). Using 'and' only gives you one action if all conditions are True."

**Q: "Do I always need an else?"**
A: "No! else is optional. Use it when you need to do something when the condition is False."

**Q: "Can I nest if inside else?"**
A: "Absolutely! You can nest if statements inside any block - if, else, or elif."

---

## Additional Examples (if time permits)

### Scholarship Eligibility
```python
gpa = 3.8
income = 45000
extracurricular = True

if gpa >= 3.0:
    if income < 50000:
        if extracurricular:
            print("Full scholarship")
        else:
            print("Partial scholarship")
    else:
        print("No financial aid")
else:
    print("GPA too low")
```

### Parking Fee Calculator
```python
hours = 5
vehicle_type = "car"
is_weekend = True

if vehicle_type == "car":
    base_rate = 5
else:
    base_rate = 10  # truck

if hours <= 2:
    fee = base_rate * hours
else:
    if is_weekend:
        fee = (base_rate * 2) + (base_rate * 0.5 * (hours - 2))
    else:
        fee = base_rate * hours

print(f"Fee: ${fee}")
```
