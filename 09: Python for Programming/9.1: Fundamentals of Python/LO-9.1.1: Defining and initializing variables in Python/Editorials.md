# Editorials: Define Variables

## Problem 1: Create and Print Variables (Easy)

### Solution
```python
student_name = "Alice"
student_age = 20
student_grade = "A"

print(student_name)
print(student_age)
print(student_grade)
```

### Explanation
- Three separate variables created with different types
- Strings use quotes, numbers don't
- `print()` displays each value

---

## Problem 2: Variable Reassignment (Easy)

### Solution
```python
temperature = 72
print(temperature)

temperature = 68
print(temperature)

temperature = 75
print(temperature)
```

### Explanation
- Same variable name `temperature` used three times
- Each assignment replaces the previous value
- Old values are discarded when reassigned

---

## Problem 3: Score Tracker (Medium)

### Solution
```python
game_score = 0
print(game_score)

game_score = game_score + 100
print(game_score)

game_score = game_score + 150
print(game_score)

game_score = game_score - 50
print(game_score)
```

### Explanation
- Start with 0
- `game_score = game_score + 100` means: take current value (0), add 100, store result (100)
- Continue updating based on current value
- Final: 0 ’ 100 ’ 250 ’ 200

---

## Problem 4: Shopping Calculator (Medium)

### Solution
```python
item_price = 25
quantity = 3
total = item_price * quantity
print(total)

quantity = 5
total = item_price * quantity
print(total)
```

### Explanation
- `total` is calculated, not hard-coded
- When `quantity` changes, must recalculate `total`
- First: 25 × 3 = 75
- Second: 25 × 5 = 125

---

## Problem 5: Variable Swap Challenge (Hard)

### Solution
```python
a = 10
b = 20

# Use temporary variable
temp = a    # temp now has 10
a = b       # a now has 20
b = temp    # b now has 10

print("a =", a)
print("b =", b)
```

### Explanation
**Why we need a temporary variable:**
```python
# This doesn't work:
a = b  # a becomes 20, but we lost the original value of a (10)!
b = a  # b becomes 20 (not the original 10)
# Both are now 20!
```

**Correct approach:**
1. Save `a`'s value in `temp` (temp = 10)
2. Copy `b` into `a` (a = 20)
3. Copy `temp` into `b` (b = 10)

**Python shortcut** (advanced):
```python
a, b = b, a  # Swaps in one line!
```
