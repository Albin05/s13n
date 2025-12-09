# Lecture Script: LO-16 Write Elif Statements

## [0:00-0:02] Hook (2 min)
**Say**: "You walk into a coffee shop. Small is $3, Medium is $4, Large is $5. How does the cashier know which price? They check: IF small, ELIF medium, ELIF large. That's elif in action!"

## [0:02-0:08] Problem with Multiple If (6 min)

**Say**: "First, let's see what happens with only if statements."

**Live Code**:
```python
score = 85

if score >= 90:
    print("Grade: A")

if score >= 80:
    print("Grade: B")

if score >= 70:
    print("Grade: C")
```

**Run it** - Show that only "B" prints, but all conditions were checked

**Say**: "This works, but Python checked ALL three conditions. Wasteful! Plus, if we're assigning grades, we need elif."

## [0:08-0:14] Introducing Elif (6 min)

**Say**: "elif means 'else if'. It checks a condition ONLY if previous ones were False."

**Write syntax on board**:
```
if condition1:
    code
elif condition2:
    code
elif condition3:
    code
```

**Live Code**:
```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  # Runs and STOPS!
elif score >= 70:
    print("Grade: C")  # Never checked

# Output: Grade: B
```

**Emphasize**: "Once Python finds a True condition, it STOPS checking!"

## [0:14-0:18] Order Matters (4 min)

**Say**: "The order of conditions is CRITICAL!"

**Show wrong order**:
```python
score = 95

if score >= 70:
    print("Pass")  # This catches 95!
elif score >= 90:
    print("Excellent")  # Never reached
```

**Run it** - Show "Pass" instead of "Excellent"

**Fix it**:
```python
if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Pass")
```

**Run it** - Show "Excellent"

**Say**: "Always put specific conditions BEFORE general ones!"

## [0:18-0:22] Real-World Example (4 min)

**Say**: "Let's build a ticket pricing system!"

**Live Code**:
```python
age = int(input("Enter age: "))

if age >= 65:
    price = 8
    print("Senior ticket: $8")
elif age >= 18:
    price = 12
    print("Adult ticket: $12")
elif age >= 13:
    price = 10
    print("Teen ticket: $10")
elif age >= 5:
    price = 6
    print("Child ticket: $6")
else:
    price = 0
    print("Free for under 5")
```

**Test with different ages**: 70, 25, 15, 7, 3

## [0:22-0:25] Practice & Wrap-up (3 min)

**Challenge**: "What prints?"

**Write on board**:
```python
x = 15

if x > 20:
    print("A")
elif x > 10:
    print("B")
elif x > 5:
    print("C")
```

**Give students 30 seconds**

**Reveal**: `B` (first True condition)

**Closing Tip**: "Remember: elif = efficiency + clarity. Use it when only one option should run!"

## Key Points to Reinforce
1. elif comes after if
2. Only first True condition executes
3. Order matters - specific before general
4. More efficient than multiple if
