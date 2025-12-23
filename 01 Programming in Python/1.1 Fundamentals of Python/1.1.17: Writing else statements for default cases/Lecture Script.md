# Lecture Script: LO-17 Write Else Statements

## [0:00-0:02] Hook (2 min)
**Say**: "At a restaurant: IF you want pasta, we make pasta. ELIF you want pizza, we make pizza. ELSE we make our house special! That's else - the default option!"

## [0:02-0:08] Basic Else (6 min)

**Say**: "else handles everything that didn't match previous conditions."

**Live Code**:
```python
age = 16

if age >= 18:
    print("Can vote")
else:
    print("Cannot vote yet")

# Output: Cannot vote yet
```

**Emphasize**: "No condition after else. It just says 'otherwise, do this!'"

## [0:08-0:14] Complete If-Elif-Else (6 min)

**Live Code**:
```python
score = 55

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# Output: F
```

**Say**: "else catches EVERYTHING below 60. We don't need to write 'else score < 60'!"

## [0:14-0:18] When to Use Else (4 min)

**Show two versions**:
```python
# With else
if temperature > 30:
    print("Hot")
else:
    print("Not hot")

# Without else
if temperature > 30:
    print("Hot")
# Nothing prints otherwise
```

**Say**: "Use else when you NEED a default action. Skip it when you don't!"

## [0:18-0:20] Practice & Wrap-up (2 min)

**Challenge**: "What prints?"
```python
x = 5
if x > 10:
    print("Big")
elif x > 20:
    print("Huge")
else:
    print("Small")
```

**Answer**: "Small" (neither condition True, so else runs)

**Closing Tip**: "else = your safety net. It catches everything else!"

## Key Points to Reinforce
1. No condition in else
2. Always goes last
3. Optional but useful
4. Catches all unmatched cases
