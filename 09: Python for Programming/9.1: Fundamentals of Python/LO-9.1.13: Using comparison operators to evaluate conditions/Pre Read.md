# Pre-Read: Use Comparison Operators

## What You'll Learn
In this lesson, you'll learn how to compare values in Python using comparison operators.

## What are Comparison Operators?
Comparison operators let you **compare two values** and get a True or False answer.

Think of it like asking questions:
- "Is 5 greater than 3?" → True
- "Is my age equal to 18?" → Could be True or False

## The Six Comparison Operators

```python
# Equal to
5 == 5    # True
5 == 3    # False

# Not equal to
5 != 3    # True
5 != 5    # False

# Greater than
5 > 3     # True
3 > 5     # False

# Less than
3 < 5     # True
5 < 3     # False

# Greater than or equal to
5 >= 5    # True
5 >= 3    # True
3 >= 5    # False

# Less than or equal to
5 <= 5    # True
3 <= 5    # True
5 <= 3    # False
```

## Important Note
**Single `=` vs Double `==`**
- `=` assigns a value: `age = 18`
- `==` checks equality: `age == 18`

Don't confuse them!

## Real-World Example
```python
age = 17
can_vote = age >= 18
print(can_vote)  # False
```

## What's Next?
In the main lesson, you'll learn:
- How to use each comparison operator
- What True and False mean in Python
- Comparing different data types
- Practical applications
