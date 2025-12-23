# Post-class Quiz: Writing Nested Conditionals for Complex Logic

Test your understanding of nested if statements and complex decision-making logic.

---

## Q1: What is the output of this code?
```python
x = 10
y = 5

if x > 5:
    if y > 3:
        print("A")
    else:
        print("B")
else:
    print("C")
```

A) A
B) B
C) C
D) No output

<details><summary>Answer</summary>
**A) A**

**Explanation:** x > 5 is True (10 > 5), so we enter the outer if block. Then y > 3 is also True (5 > 3), so we print "A".
</details>

---

## Q2: What is the key purpose of indentation in nested conditionals?

A) To make code look pretty
B) To define which code belongs to which condition
C) To improve code performance
D) To satisfy Python syntax requirements only

<details><summary>Answer</summary>
**B) To define which code belongs to which condition**

**Explanation:** Indentation in Python determines code structure. It shows which statements are inside which blocks. While it is a syntax requirement (D), the PURPOSE is to define structure (B).
</details>

---

## Q3: What is the output?
```python
age = 15
has_permission = False

if age >= 18:
    print("Adult")
else:
    if has_permission:
        print("Allowed with permission")
    else:
        print("Not allowed")
```

A) Adult
B) Allowed with permission
C) Not allowed
D) Error

<details><summary>Answer</summary>
**C) Not allowed**

**Explanation:** age >= 18 is False (15 < 18), so we go to the outer else block. Inside, has_permission is False, so we go to the inner else and print "Not allowed".
</details>

---

## Q4: Which code structure is generally MORE readable?
```python
# Option A
if a:
    if b:
        if c:
            print("Success")

# Option B
if a and b and c:
    print("Success")
```

A) Option A is more readable
B) Option B is more readable
C) Both are equally readable
D) Neither is readable

<details><summary>Answer</summary>
**B) Option B is more readable**

**Explanation:** When you simply need all conditions to be True with a single action, using `and` is clearer and more concise than deep nesting. Nested ifs are better when you need different actions at each level.
</details>

---

## Q5: What happens if the outer condition is False in a nested if?

A) Python checks the inner condition anyway
B) Python skips the entire outer block including inner conditions
C) Python raises an error
D) Python executes the outer else, then checks inner condition

<details><summary>Answer</summary>
**B) Python skips the entire outer block including inner conditions**

**Explanation:** If the outer condition is False, Python NEVER evaluates the inner conditions. It skips the entire outer if block and goes to the outer else (if present).
</details>

---

## Q6: What is the output?
```python
score = 75

if score >= 0 and score <= 100:
    if score >= 60:
        print("Pass")
    else:
        print("Fail")
else:
    print("Invalid")
```

A) Pass
B) Fail
C) Invalid
D) No output

<details><summary>Answer</summary>
**A) Pass**

**Explanation:** score is 75, which is between 0 and 100 (outer condition True). Then score >= 60 is True (75 >= 60), so we print "Pass".
</details>

---

## Q7: How many possible execution paths are there in this code?
```python
if condition_A:
    if condition_B:
        print("Path 1")
    else:
        print("Path 2")
else:
    print("Path 3")
```

A) 2
B) 3
C) 4
D) 5

<details><summary>Answer</summary>
**B) 3**

**Explanation:**
- Path 1: condition_A True AND condition_B True → "Path 1"
- Path 2: condition_A True AND condition_B False → "Path 2"
- Path 3: condition_A False → "Path 3"

Total: 3 paths
</details>

---

## Q8: What is the output?
```python
temperature = 95
humidity = 70

if temperature > 90:
    if humidity > 60:
        print("Dangerous")
    else:
        print("Hot")
else:
    print("Normal")
```

A) Dangerous
B) Hot
C) Normal
D) Error

<details><summary>Answer</summary>
**A) Dangerous**

**Explanation:** temperature > 90 is True (95 > 90), and humidity > 60 is also True (70 > 60), so we print "Dangerous".
</details>

---

## Q9: Which is TRUE about nested conditionals?

A) The inner condition is always checked first
B) You can only nest 2 levels deep
C) The outer condition must be True for inner condition to be checked
D) else is required for every if in nested structures

<details><summary>Answer</summary>
**C) The outer condition must be True for inner condition to be checked**

**Explanation:** The outer condition guards the inner condition. If outer is False, inner is never evaluated. Options A, B, and D are false.
</details>

---

## Q10: What is the output?
```python
username = "admin"
password = "wrong"

if username == "admin":
    if password == "secret":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Unknown user")
```

A) Login successful
B) Wrong password
C) Unknown user
D) No output

<details><summary>Answer</summary>
**B) Wrong password**

**Explanation:** username == "admin" is True, so we enter outer if. Then password == "secret" is False ("wrong" != "secret"), so we go to the inner else and print "Wrong password".
</details>

---

## Q11: What does this code validate?
```python
if age >= 0:
    if age < 18:
        category = "Minor"
    else:
        category = "Adult"
else:
    category = "Invalid"
```

A) Age is a positive number
B) Age is between 0 and 18
C) Age is a valid non-negative number before classification
D) Age is exactly 18

<details><summary>Answer</summary>
**C) Age is a valid non-negative number before classification**

**Explanation:** The outer if checks age >= 0 (validation). Only if valid does it proceed to classify as Minor or Adult. This is a validation-first pattern.
</details>

---

## Q12: What is the maximum recommended nesting depth?

A) 1 level
B) 2 levels
C) 3-4 levels
D) Unlimited

<details><summary>Answer</summary>
**C) 3-4 levels**

**Explanation:** While technically you can nest infinitely, best practice is to keep it to 3-4 levels maximum for readability. Beyond that, consider refactoring using `and`/`or` operators or functions.
</details>

---

## Q13: What is the output?
```python
x = 5
y = 10

if x > 0:
    if y > 0:
        result = x + y
    else:
        result = x - y
else:
    result = 0

print(result)
```

A) 0
B) 5
C) 10
D) 15

<details><summary>Answer</summary>
**D) 15**

**Explanation:** x > 0 is True (5 > 0), and y > 0 is also True (10 > 0), so result = x + y = 5 + 10 = 15.
</details>

---

## Q14: When should you use nested if instead of `and` operator?

A) Never - always use `and`
B) When you need different actions at each condition level
C) When you want slower code
D) Only when you have more than 5 conditions

<details><summary>Answer</summary>
**B) When you need different actions at each condition level**

**Explanation:** Nested ifs are useful when you need to provide specific feedback or take different actions based on which condition failed. For example, different error messages for missing username vs wrong password.
</details>

---

## Q15: What is the output?
```python
score = 50
bonus = True

if score >= 60:
    print("Pass")
else:
    if bonus:
        print("Pass with bonus")
    else:
        print("Fail")
```

A) Pass
B) Pass with bonus
C) Fail
D) No output

<details><summary>Answer</summary>
**B) Pass with bonus**

**Explanation:** score >= 60 is False (50 < 60), so we go to outer else. Inside, bonus is True, so we print "Pass with bonus".
</details>

---

## Score Interpretation

- **13-15 correct**: Excellent! You've mastered nested conditionals.
- **10-12 correct**: Good work! Review execution flow and when to use nesting vs `and`.
- **7-9 correct**: Fair. Practice more with nested structures and decision trees.
- **Below 7**: Review the lesson materials on nested if statements and indentation.

## Key Concepts to Remember

1. **Outer first**: Outer condition is checked before inner
2. **Indentation matters**: Defines which code belongs to which block
3. **Short-circuit**: If outer is False, inner never runs
4. **Validation pattern**: Check inputs first, then process
5. **Specific errors**: Use nesting for detailed error messages
6. **Readability limit**: Keep to 3-4 levels maximum
7. **Test all paths**: Every combination should be verified
8. **And vs nesting**: Use `and` for simple all-true checks, nesting for different actions
9. **else is optional**: Only use when needed
10. **Structure defines logic**: Proper indentation creates correct flow
