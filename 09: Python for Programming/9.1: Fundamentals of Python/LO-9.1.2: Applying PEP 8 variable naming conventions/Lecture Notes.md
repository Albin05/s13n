# Lecture Notes: Apply Variable Naming Conventions

## Naming Rules (Must Follow)

### 1. Start with letter or underscore
✅ `name`, `_value`
❌ `1name`, `@user`


### 2. Only letters, numbers, underscores
✅ `student_name`, `score_2024`
❌ `student-name`, `total$`

### 3. Case sensitive
`age` ≠ `Age` ≠ `AGE`

### 4. No reserved keywords
❌ `for`, `if`, `while`, `class`

## Naming Conventions (Best Practice)

### snake_case
```python
student_name = "Alice"  # Pythonic
studentName = "Alice"   # Not Pythonic
```

### Be descriptive
```python
student_count = 30  # Good
sc = 30             # Bad
```

### Constants in UPPER_CASE
```python
MAX_SIZE = 100
PI = 3.14159
```

## Key Takeaways
1. Follow rules to avoid errors
2. Use snake_case for variables
3. Be descriptive and clear
4. Avoid reserved keywords
