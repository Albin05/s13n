# Pre-Read: Apply Variable Naming Conventions

## Why Naming Matters

Imagine reading a book where every character was named "Person1", "Person2", "Person3". Confusing, right?

Variable names are the same - they tell the story of your code. Good names make code **self-explanatory**. Bad names require constant mental translation and lead to bugs.

### The Cost of Bad Naming

Consider this real example:
```python
# Unclear
d = 86400
t = d * 7
```

vs.

```python
# Clear
seconds_per_day = 86400
seconds_per_week = seconds_per_day * 7
```

The second version needs no comments - the names explain everything. The first version forces you to guess what `d` and `t` mean.

**In professional development:**
- Poor naming wastes hours of debugging time
- Good naming prevents bugs before they happen
- Clear names reduce onboarding time for new team members

### Python's Philosophy: Community Standards

Python has an official style guide called **PEP 8**. It's not just suggestions - it's how the entire Python community writes code.

Following PEP 8 means:
- Your code looks professional
- Other Python developers can read it instantly
- You can read their code easily too
- Tools can automatically check your style

Think of it like **driving on the right side of the road** - it's a convention that makes everyone safer.

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
