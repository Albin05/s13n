### LO-2 Apply Variable Naming Conventions (15 minutes)

### Hook (2 minutes)

**Say**: "You can name variables almost anything... but should you? Let's learn the rules and best practices!"

```python
x = 10      # Valid but unclear
age = 10    # Valid and clear!
```

### Naming Rules (5 minutes)

**Key Rules**:
- Must start with letter or underscore
- Can contain letters, numbers, underscores
- Cannot use Python keywords (if, for, while, etc.)
- Case-sensitive (Age ≠ age)

```python
# Valid
student_name = "Alice"
_private = 42
age2 = 25

# Invalid
2students = 10      # Error!
student-name = "Bob" # Error!
for = 5              # Error! (keyword)
```

### PEP 8 Conventions (6 minutes)

**Say**: "Python has style guidelines called PEP 8. Follow them to write professional code!"

**Best Practices**:
- Use `snake_case` for variables (all lowercase, underscores)
- Make names descriptive
- Avoid single letters except in loops

```python
# Good - follows PEP 8
student_name = "Alice"
total_score = 95
is_active = True

# Bad - works but not Pythonic
studentName = "Bob"   # camelCase (not Python style)
TotalScore = 85       # PascalCase (for classes)
x = True              # too vague
```

**Real-World**: Professional Python projects follow PEP 8. Learn it now!

### Practice (2 minutes)

Fix these names to follow PEP 8:
```python
StudentName = "Alice"  # Change to: student_name
totalPrice = 99.99     # Change to: total_price
2ndPlace = "Bob"       # Change to: second_place
```
