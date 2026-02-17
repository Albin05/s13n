### LO-16 Write Elif Statements (20 minutes)


### CS Theory Bite

> **Origin**: `elif` is Python's elegant alternative to **switch/case** statements found in C/Java. It implements **decision trees** — sequential condition checking until a match is found.
>
> **Analogy**: `elif` is like a **multiple-choice exam** — check option A, if not then B, if not then C, until one matches.
>
> **Why it matters**: Real decisions rarely have just two options — `elif` handles multi-branch logic cleanly.


### Hook (2 minutes)

**Say**: "You walk into a coffee shop. Small is $3, Medium is $4, Large is $5. How does the cashier know which price? They check: IF small, ELIF medium, ELIF large. That's elif in action!"

### Problem with Multiple If (6 minutes)

**Say**: "First, let's see what happens with only if statements."

```python
score = 85

if score >= 90:
    print("Grade: A")

if score >= 80:
    print("Grade: B")

if score >= 70:
    print("Grade: C")
```

### Introducing Elif (6 minutes)

**Say**: "elif means 'else if'. It checks a condition ONLY if previous ones were False."

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

### Order Matters (4 minutes)

**Say**: "The order of conditions is CRITICAL!"

```python
score = 95

if score >= 70:
    print("Pass")  # This catches 95!
elif score >= 90:
    print("Excellent")  # Never reached
```

### Real-World Example (4 minutes)

**Say**: "Let's build a ticket pricing system!"

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
```

### Practice & Wrap-up (3 minutes)

```python
x = 15

if x > 20:
    print("A")
elif x > 10:
    print("B")
elif x > 5:
    print("C")
```

