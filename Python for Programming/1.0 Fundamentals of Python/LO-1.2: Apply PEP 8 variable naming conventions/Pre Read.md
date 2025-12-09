# Pre-Read: Apply Variable Naming Conventions

## Why Naming Matters
Variable names should be clear and follow Python's rules. Good names make code readable; bad names cause errors or confusion.

## Naming Rules (MUST Follow)

### 1. Start with letter or underscore
✅ `age`, `_private`, `user1`
❌ `1age`, `@user`

### 2. Only letters, numbers, underscores
✅ `student_name`, `score_2024`
❌ `student-name`, `score$`

### 3. Case-sensitive
`age`, `Age`, `AGE` are THREE different variables

### 4. No reserved keywords
❌ `for`, `if`, `while`, `class`

## Naming Conventions (Best Practice)

### Use snake_case
```python
student_name = "Alice"  # Good
studentName = "Alice"   # Works but not Pythonic
```

### Be descriptive
```python
student_count = 30    # Clear
sc = 30               # Unclear
```

### Booleans sound like questions
```python
is_active = True
has_permission = False
```

## Try Before Class
Which names are valid?
- `my_name` ✅
- `2nd_place` ❌ (starts with number)
- `first-name` ❌ (has hyphen)
- `_value` ✅
