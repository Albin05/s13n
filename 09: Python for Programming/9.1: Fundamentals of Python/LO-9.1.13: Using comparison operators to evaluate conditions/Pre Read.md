# Pre-Read: Use Comparison Operators

## What You'll Learn
In this lesson, you'll learn how to compare values in Python using comparison operators.

## What are Comparison Operators?
Comparison operators let you **compare two values** and get a True or False answer.

Think of it like asking questions:
- "Is 5 greater than 3?" → True
- "Is my age equal to 18?" → Could be True or False

### Why Programs Need to Compare

Every smart app you use makes comparisons constantly:
- **Netflix**: Is movie rating >= 4 stars? Show it in "Recommended"
- **Amazon**: Is price < $50? Show "Under $50" badge
- **Spotify**: Is play_count > 1000? Add to "Popular" playlist
- **Phone**: Is battery_level <= 20%? Show low battery warning

Without comparisons, apps couldn't filter, sort, or make decisions!

### Simple Analogy

Comparison operators are like **yes/no questions**:
- "Is the door locked?" → Yes/No (True/False)
- "Is the water hot?" → Yes/No (True/False)
- "Is today Monday?" → Yes/No (True/False)

Computers use these True/False answers to decide what to do next.

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
