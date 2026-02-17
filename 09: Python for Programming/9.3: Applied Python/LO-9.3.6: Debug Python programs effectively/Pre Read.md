## Pre-Read: Debug Python Programs Effectively


---

## Introduction

**Debugging** is the systematic process of finding and fixing errors (bugs) in code. Named after Grace Hopper's 1947 discovery of a literal moth causing computer errors! Modern debugging uses **scientific method**: observe symptoms, form hypotheses, test, fix. No random changes - systematic investigation!

### Why Systematic Debugging Matters

**Problem with random debugging**: Trial and error wastes time:
```python
# Desperate - random changes!
# result = calculate(x, y)  # Comment this?
result = calculate(y, x)  # Swap?
# Hope something works!
```

**Solution with systematic debugging**: Scientific method:
```python
# Systematic - test hypothesis!
print(f"Input: x={x}, y={y}")
result = calculate(x, y)
print(f"Output: {result}")
# Observe, hypothesize, test!
```

**This is the scientific method** - observe, experiment, conclude!

### Real-World Analogy

**Debugging like medical diagnosis**:
- **Symptoms**: Program misbehaves (patient feels sick)
- **Tests**: Print statements, debugger (blood tests, scans)
- **Diagnosis**: Find bug (identify disease)
- **Treatment**: Fix code (prescribe medicine)
**Doctors diagnose systematically - so should programmers!**

### The Origin of "Bug"

**First computer bug**: Literal moth found in Harvard Mark II computer (1947) by Grace Hopper! Coined term "debugging" - removing bugs from hardware. Now means fixing software errors!

---

### Three Types of Errors

1. **Syntax** — code won't run at all (`SyntaxError`)
2. **Runtime** — code crashes mid-execution (`TypeError`, `ValueError`)
3. **Logic** — code runs but gives wrong answers (hardest!)

---

### Your Best Friend: The Traceback

```
Traceback (most recent call last):
  File "app.py", line 5, in calculate
    return x / y
ZeroDivisionError: division by zero
```

Read **bottom to top**: error first, then trace how you got there.

---

### Simplest Debug Tool: print()

```python
x = get_data()
print(f"DEBUG: x = {x}, type = {type(x)}")
```

---

### Try This

Find the bug:
```python
def count_evens(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
        return count  # Bug! Where should this line be?
```
