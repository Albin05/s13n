# Editorials: Implement Integer Data Types

## Problem 1
```python
age = 25
year = 2024
siblings = 2

print(age, type(age))
print(year, type(year))
print(siblings, type(siblings))
```

## Problem 2
```python
a = 15
b = 4

print(a + b)  # 19
print(a - b)  # 11
print(a * b)  # 60
```

## Problem 3
```python
print(17 / 5)   # 3.4 (regular division, returns float)
print(17 // 5)  # 3 (integer division, drops decimal)
print(17 % 5)   # 2 (remainder: 17 = 5×3 + 2)
```

## Problem 4
```python
students = 50
group_size = 6

complete_groups = students // group_size
leftover = students % group_size

print(f"Groups: {complete_groups}")  # 8
print(f"Leftover: {leftover}")       # 2
```

## Problem 5
```python
total_minutes = 185

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"{hours} hours and {minutes} minutes")
# Output: 3 hours and 5 minutes
```

**Explanation**:
- `185 // 60 = 3` (how many complete hours)
- `185 % 60 = 5` (leftover minutes)
