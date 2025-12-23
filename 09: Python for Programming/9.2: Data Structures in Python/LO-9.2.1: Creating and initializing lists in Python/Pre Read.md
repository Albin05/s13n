# Pre-Read: Creating and Initializing Lists in Python

## What You'll Learn
In this lesson, you'll learn how to create and initialize lists - Python's most versatile data structure for storing collections of items.

## Why This Matters
Lists are everywhere in programming:
- Shopping cart items in an e-commerce site
- Student names in a classroom management system
- Temperature readings from a weather station
- Tasks in a to-do list application
- User posts in a social media feed

Lists let you store multiple related values in a single, organized structure instead of creating hundreds of individual variables.

---

## What is a List?

A **list** is an ordered, mutable (changeable) collection that can store multiple items of any type.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
```

**Key characteristics:**
- **Ordered**: Items have a specific position (index)
- **Mutable**: Can be changed after creation
- **Allow duplicates**: Can have repeated values
- **Any type**: Can store integers, strings, floats, booleans, even other lists

---

## Creating Lists

### Method 1: Square Brackets (Most Common)

```python
# Empty list
empty_list = []

# List with items
colors = ["red", "green", "blue"]
scores = [95, 87, 92, 88]
```

### Method 2: Using the list() Constructor

```python
# From a string (each character becomes an item)
letters = list("Python")
print(letters)  # ['P', 'y', 't', 'h', 'o', 'n']

# From a range
numbers = list(range(1, 6))
print(numbers)  # [1, 2, 3, 4, 5]

# Empty list
empty = list()
```

---

## Lists Can Store Any Type

### Same Type (Homogeneous)

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]
prices = [19.99, 5.50, 12.00]
```

### Mixed Types (Heterogeneous)

```python
student = ["Alice", 25, 3.8, True]
# [name, age, GPA, is_enrolled]
```

### Lists Within Lists (Nested)

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

students = [
    ["Alice", 85],
    ["Bob", 92],
    ["Charlie", 78]
]
```

---

## Real-World Examples

### Example 1: Shopping Cart

```python
cart_items = ["Laptop", "Mouse", "Keyboard", "Monitor"]
quantities = [1, 2, 1, 1]
prices = [999.99, 25.50, 79.99, 299.99]
```

### Example 2: Temperature Readings

```python
# Hourly temperatures for a day
temperatures = [72, 74, 76, 78, 80, 82, 84, 85,
                83, 81, 79, 76, 74, 72, 70, 68,
                67, 66, 65, 64, 63, 63, 62, 62]
```

### Example 3: To-Do List

```python
tasks = [
    "Buy groceries",
    "Finish homework",
    "Call dentist",
    "Practice Python",
    "Go for a run"
]
```

---

## Empty Lists

Start with an empty list and add items later:

```python
shopping_list = []
# We'll add items as we think of them

exam_scores = []
# We'll add scores as students finish the exam
```

---

## Lists vs Other Data Types

### Single Variable (Before Lists)

```python
student1 = "Alice"
student2 = "Bob"
student3 = "Charlie"
# Tedious and doesn't scale!
```

### List (Better)

```python
students = ["Alice", "Bob", "Charlie"]
# Easy to manage, can loop through, can grow/shrink
```

---

## Common List Patterns

### Pattern 1: Sequential Numbers

```python
# Manual
numbers = [1, 2, 3, 4, 5]

# Using range (more flexible)
numbers = list(range(1, 6))

# Even numbers
evens = list(range(0, 11, 2))  # [0, 2, 4, 6, 8, 10]
```

### Pattern 2: Repeating Elements

```python
# Five zeros
zeros = [0] * 5  # [0, 0, 0, 0, 0]

# Ten "hello"s
greetings = ["hello"] * 10
```

### Pattern 3: Combining Lists

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # [1, 2, 3, 4, 5, 6]
```

---

## Try It Yourself (Before Class)

Run this code:

```python
# Create different lists
favorite_foods = ["pizza", "sushi", "tacos"]
lucky_numbers = [7, 13, 21, 42]
mixed_data = ["Python", 3.11, True, 2024]

print("Foods:", favorite_foods)
print("Numbers:", lucky_numbers)
print("Mixed:", mixed_data)

# Check list length
print("Number of foods:", len(favorite_foods))

# Create an empty list
my_goals = []
print("My goals:", my_goals)
```

**Try:**
1. Create a list of your favorite movies
2. Create a list with numbers 1 through 10
3. Create a list with your name, age, and city
4. What happens if you multiply a list by 3?

---

## Key Takeaways

Before class, remember:
1. **Lists store multiple items** - use square brackets `[]`
2. **Ordered and indexed** - items have positions starting at 0
3. **Mutable** - can be changed after creation
4. **Any type allowed** - mix strings, numbers, booleans, etc.
5. **Use list()** - to convert other types to lists

## What's Next?

In the live session, we'll:
- Access individual items using indexing
- Modify lists by adding, removing, and changing items
- Slice lists to get portions
- Loop through lists
- Use powerful list methods
- Build lists with comprehensions

See you in class!
