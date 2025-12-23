# Lecture Script: LO-3 Implement Integer Data Types

## Duration: 10-15 minutes

## [0:00-0:02] Hook
**Say**: "What's 10 divided by 3? In math, it's 3.333... But what if you're splitting 10 cookies among 3 people? You can't split a cookie! That's where integer division comes in."

## [0:02-0:07] What are Integers (5 min)

**Explain**: Whole numbers - no decimals

**Live Code**:
```python
age = 25
year = 2024
count = 0

print(type(age))  # <class 'int'>
```

**Emphasize**: Positive, negative, or zero - all integers!

## [0:07-0:12] Integer Operations (5 min)

**Demonstrate**:
```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333... (float!)
print(a // b)  # 3 (integer division)
print(a % b)   # 1 (remainder)
```

**Key Point**: `/` gives float, `//` gives integer

## [0:12-0:15] Practice & Wrap (3 min)

**Exercise**: "You have 25 candies and 4 friends. How many does each get? How many left over?"

```python
candies = 25
friends = 4

each_gets = candies // friends
leftover = candies % friends
```

**Answer**: 6 each, 1 leftover
