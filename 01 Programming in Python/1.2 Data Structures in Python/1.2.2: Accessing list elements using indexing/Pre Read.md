# Pre-Read: Accessing List Elements Using Indexing

## What You'll Learn
In this lesson, you'll learn how to access individual elements in a list using indexing - Python's way of pinpointing specific items by their position.

## Why This Matters
Accessing list elements is fundamental:
- Get the first student's name from a class roster
- Retrieve the highest score from test results
- Display the last item added to a shopping cart
- Access specific data from sensor readings
- Grab a particular user's information from a database result

Without indexing, lists would just be storage containers you couldn't actually use!

---

## Understanding List Indexing

Each item in a list has a position number called an **index**. Python uses **zero-based indexing**, meaning the first item is at index 0.

```python
fruits = ["apple", "banana", "cherry", "date"]
#         0        1         2         3
```

**Access using square brackets:**
```python
first = fruits[0]   # "apple"
second = fruits[1]  # "banana"
third = fruits[2]   # "cherry"
fourth = fruits[3]  # "date"
```

---

## Zero-Based Indexing

**Critical concept:** The first item is index 0, NOT 1!

```python
colors = ["red", "green", "blue"]

print(colors[0])  # "red" (first item)
print(colors[1])  # "green" (second item)
print(colors[2])  # "blue" (third item)
```

**Why zero-based?** It's a computer science convention that makes many operations more efficient.

---

## Negative Indexing

Access items from the end using negative numbers:

```python
fruits = ["apple", "banana", "cherry", "date"]
#         -4       -3        -2       -1

print(fruits[-1])  # "date" (last item)
print(fruits[-2])  # "cherry" (second to last)
print(fruits[-3])  # "banana"
print(fruits[-4])  # "apple" (first item, same as [0])
```

**Use cases:**
- `-1` for last item (very common!)
- `-2` for second to last
- Useful when you don't know the list length

---

## Real-World Examples

### Example 1: Student Grades

```python
grades = [85, 92, 78, 95, 88]

first_grade = grades[0]
last_grade = grades[-1]
third_grade = grades[2]

print(f"First student: {first_grade}")
print(f"Last student: {last_grade}")
print(f"Third student: {third_grade}")
```

### Example 2: Week Schedule

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

workweek_start = days[0]      # Monday
workweek_end = days[4]         # Friday
weekend_start = days[5]        # Saturday
last_day = days[-1]            # Sunday

print(f"Week starts: {workweek_start}")
print(f"Weekend begins: {weekend_start}")
```

### Example 3: Top Scores

```python
high_scores = [9500, 8700, 8200, 7900, 7500]

champion = high_scores[0]       # Highest score
runner_up = high_scores[1]      # Second highest
last_place = high_scores[-1]    # Lowest score

print(f"Champion: {champion}")
print(f"Runner-up: {runner_up}")
```

---

## Index Out of Range Error

Accessing an index that doesn't exist causes an error:

```python
colors = ["red", "green", "blue"]

print(colors[0])   # ✓ "red"
print(colors[2])   # ✓ "blue"
print(colors[3])   # ✗ IndexError: list index out of range
```

**Safe access:** Check list length first
```python
if len(colors) > 3:
    print(colors[3])
else:
    print("No fourth item")
```

---

## Using Indexing with Variables

```python
scores = [95, 87, 92, 88, 91]

index = 2
print(scores[index])  # 92

# Dynamic access
for i in range(len(scores)):
    print(f"Score {i+1}: {scores[i]}")
```

---

## Changing List Items with Indexing

Lists are mutable - you can change items:

```python
fruits = ["apple", "banana", "cherry"]

fruits[1] = "blueberry"  # Change second item
print(fruits)  # ["apple", "blueberry", "cherry"]

fruits[-1] = "date"      # Change last item
print(fruits)  # ["apple", "blueberry", "date"]
```

---

## Try It Yourself (Before Class)

Run this code:

```python
animals = ["dog", "cat", "rabbit", "hamster", "parrot"]

# Access different positions
print("First:", animals[0])
print("Third:", animals[2])
print("Last:", animals[-1])
print("Second to last:", animals[-2])

# Change an item
animals[1] = "kitten"
print("Modified:", animals)

# Try to predict before running
print(animals[len(animals) - 1])  # What does this give?
```

**Questions:**
1. What's the index of "rabbit"?
2. How do you access the first and last item?
3. What happens if you try `animals[10]`?
4. How do you change "dog" to "puppy"?

---

## Common Indexing Patterns

### Get First and Last

```python
items = [10, 20, 30, 40, 50]

first = items[0]
last = items[-1]
```

### Get Middle Item

```python
items = [1, 2, 3, 4, 5]
middle_index = len(items) // 2
middle = items[middle_index]  # 3
```

### Swap Two Items

```python
numbers = [1, 2, 3, 4, 5]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)  # [5, 2, 3, 4, 1]
```

---

## Key Takeaways

Before class, remember:
1. **Zero-based indexing** - first item is index 0
2. **Square brackets** - use `list[index]` to access
3. **Negative indices** - count from end (-1 is last)
4. **IndexError** - accessing non-existent index raises error
5. **Mutable** - can change items using indexing

## What's Next?

In the live session, we'll:
- Practice indexing in various scenarios
- Learn about slicing (getting multiple items at once)
- Combine indexing with loops
- Handle index errors gracefully
- Use indexing to build complex operations

See you in class!
