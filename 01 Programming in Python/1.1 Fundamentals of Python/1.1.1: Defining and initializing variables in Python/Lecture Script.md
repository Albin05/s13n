# Lecture Script: LO-1 Define Variables

## Instructor Guide
**Duration**: 15-20 minutes
**Format**: Interactive lecture with live coding

---

## Timeline

| Time | Activity | Duration |
|------|----------|----------|
| 0:00-0:02 | Hook & Learning Objective | 2 min |
| 0:02-0:08 | What are Variables + Demo | 6 min |
| 0:08-0:14 | Variable Assignment & Reassignment | 6 min |
| 0:14-0:18 | Student Exercise | 4 min |
| 0:18-0:20 | Q&A & Transition | 2 min |

---

## [0:00-0:02] Hook (2 min)

**Say**: "Imagine playing a video game. The game needs to remember your score, your character's name, your health - all while you're playing. How does it do that? With variables! Today you'll learn how to make Python remember information."

**Show**: Quick demo of a variable in action
```python
score = 0
score = score + 100
print(score)  # 100
```

**Learning Objective**: "By the end of this lesson, you'll be able to create variables and change their values in Python."

---

## [0:02-0:08] What are Variables (6 min)

### Part 1: The Concept (2 min)

**Say**: "A variable is like a labeled box. The label is the variable name, and you put data inside the box."

**Draw or Show**:
```
Box labeled "age" containing "25"
Box labeled "name" containing "Alice"
```

### Part 2: Creating Variables (4 min)

**Live Code**:
```python
# Create a variable
age = 25
print(age)  # 25

name = "Alice"
print(name)  # Alice

score = 100
print(score)  # 100
```

**Key Points to Emphasize**:
- Variable name on LEFT, value on RIGHT
- Use `=` to assign (not "equals" like math)
- Read as "age is assigned 25"

**Ask**: "Can someone tell me what this does?"
```python
city = "Boston"
```
(Answer: Creates a variable called city with the value "Boston")

---

## [0:08-0:14] Variable Reassignment (6 min)

### Part 1: Variables Can Change (3 min)

**Say**: "Unlike math where x = 5 is permanent, in programming variables can change. They're called VARIables because they VARY!"

**Live Code**:
```python
health = 100
print(health)  # 100

health = 75   # Player took damage!
print(health)  # 75

health = 100  # Player healed!
print(health)  # 100
```

**Emphasize**: The old value disappears when you reassign.

### Part 2: Using Current Value (3 min)

**Live Code**:
```python
score = 0
print("Start:", score)  # 0

score = score + 50  # Add 50 to current score
print("After bonus:", score)  # 50

score = score + 100
print("After level:", score)  # 150
```

**Explain**: "score = score + 50" means:
1. Get the current value of score (0)
2. Add 50 to it (0 + 50 = 50)
3. Store the result back in score

---

## [0:14-0:18] Student Exercise (4 min)

**Say**: "Your turn! Create a variable called `money` with value 100. Then add 50 to it. Then subtract 30. Print it after each step."

**Share Starter Code**:
```python
# Your code here
money = 100
print(money)

# Add 50

# Subtract 30
```

**Give 2 minutes**, then show solution:

```python
money = 100
print(money)  # 100

money = money + 50
print(money)  # 150

money = money - 30
print(money)  # 120
```

**Debrief**: Ask 1-2 students what they learned or what was tricky.

---

## [0:18-0:20] Wrap-up (2 min)

**Summary**: "Great work! You now know how to:
- Create variables with `=`
- Change variable values
- Use variables in calculations"

**Quick Check**: "True or False: Can I use a variable before creating it?" (Answer: False - must create first)

**Preview**: "Next in LO-2, we'll learn the RULES for naming variables - what names are allowed and what aren't."

---

## Teaching Tips

**Common Student Questions**:
- **Q**: "Why does `=` mean assign and not equals?"
  **A**: "In Python, `=` is assignment. We use `==` for equality checking (you'll learn that later)."

- **Q**: "Where does the old value go?"
  **A**: "It's discarded - Python's garbage collector cleans it up automatically."

**If Students Struggle**:
- Use more physical analogies (boxes, labels)
- Show errors live to normalize debugging
- Pair program: have them guide you through code

**Extension for Advanced Students**:
"Can you create 3 variables in one line? Try: `x, y, z = 1, 2, 3`"
