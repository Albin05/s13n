# Lecture Notes: Use Dictionary Comprehensions

## Dictionary Comprehensions

Dictionary comprehensions provide a concise way to create dictionaries based on existing sequences or other dictionaries.


---

<div align="center">

![Dictionary with key-value pairs](https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&q=80)

*Dictionaries store data as key-value pairs for fast lookup*

</div>

---

## Introduction

Dictionary comprehensions implement **key-value transformation** - building dicts declaratively! This extends list comprehension syntax to **associative arrays** - the foundation of hash tables. Dict comprehensions are **mapping operations** made elegant!

### Why Dictionary Comprehensions Transform Code

**Problem with traditional approach**: Verbose dict building:
```python
# TEDIOUS - manual dict construction!
squares = {}
for i in range(6):
    squares[i] = i ** 2
# Loop machinery obscures intent!
```

**Solution with comprehensions**: Express mapping directly:
```python
# CLEAR - intent obvious!
squares = {i: i**2 for i in range(6)}
# "Map i to i² for each i" - declarative!
```

**This is mapping elegance** - key-value transformation visible!

### Historical Context

**Dictionary comprehensions** added **Python 2.7/3.0** (2010) with **PEP 274**. Later than list comprehensions (2000) - originally **dict()** with generator expressions: `dict((k, v) for...)` was workaround!

**Inspired by set theory**: Mathematical relations map domain to range - `{x → x² | x ∈ ℕ}` becomes `{x: x**2 for x in naturals}`. **Category theory** influenced functional programming - mappings are morphisms!

**Hash table optimization**: CPython's dict implementation uses **open addressing** (since 3.6) preserving insertion order. Comprehensions pre-allocate hash table size when possible - **amortized O(1)** insertions!

### Real-World Analogies

**Dict comprehensions like database indexing**:
- **Traditional**: Build index manually, entry by entry
- **Comprehension**: Declare index structure, auto-populate
- **Result**: Fast lookup table
**CREATE INDEX automatically builds mapping!**

**Or like phone book creation**:
```python
# Traditional: Add each person manually
phonebook = {}
for person in contacts:
    phonebook[person.name] = person.phone

# Comprehension: Declare mapping structure
phonebook = {p.name: p.phone for p in contacts}
# Automatic directory construction!
```

**Or like variable substitution**:
- **Template**: "Hello {name}, you are {age}"
- **Mapping**: `{name: "Alice", age: 25}`
- **Comprehension**: `{k: values[k] for k in template_vars}`
**Transform keys to values declaratively!**

### Dict vs List Comprehensions

**List comprehension**: Ordered sequence:
```python
[x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

**Dict comprehension**: Key-value mapping:
```python
{x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

**Choose based on access pattern** - dict for lookups, list for iteration!

---
### Syntax

```python
new_dict = {key_expression: value_expression for item in iterable}
new_dict = {key_expression: value_expression for item in iterable if condition}
```

## Basic Dictionary Comprehension

Traditional loop vs dictionary comprehension:

```python
# Traditional approach
squares = {}
for i in range(6):
    squares[i] = i ** 2
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dictionary comprehension
squares = {i: i ** 2 for i in range(6)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## Creating from Lists

```python
# Create dictionary from two lists using zip
names = ["Alice", "Bob", "Charlie", "Diana"]
ages = [25, 30, 35, 28]

people = {name: age for name, age in zip(names, ages)}
print(people)
# {'Alice': 25, 'Bob': 30, 'Charlie': 35, 'Diana': 28}

# Create dictionary with index as key
fruits = ["apple", "banana", "cherry", "date"]
fruit_dict = {i: fruit for i, fruit in enumerate(fruits)}
print(fruit_dict)
# {0: 'apple', 1: 'banana', 2: 'cherry', 3: 'date'}

# Swap key and value
fruit_indices = {fruit: i for i, fruit in enumerate(fruits)}
print(fruit_indices)
# {'apple': 0, 'banana': 1, 'cherry': 2, 'date': 3}
```

## Filtering Dictionary Comprehensions

```python
# Filter by value
prices = {
    "apple": 0.5,
    "banana": 0.3,
    "orange": 0.8,
    "grape": 1.2,
    "mango": 1.5
}

expensive_fruits = {fruit: price for fruit, price in prices.items() if price > 0.7}
print(expensive_fruits)
# {'orange': 0.8, 'grape': 1.2, 'mango': 1.5}

# Filter by key
long_names = {fruit: price for fruit, price in prices.items() if len(fruit) > 5}
print(long_names)
# {'banana': 0.3, 'orange': 0.8}

# Filter by both key and value
selected = {fruit: price for fruit, price in prices.items()
            if len(fruit) > 4 and price < 1.0}
print(selected)
# {'apple': 0.5, 'banana': 0.3, 'orange': 0.8}
```

## Real-World Examples

### Example 1: Grade Management

```python
# Convert grade percentages to letter grades
students_scores = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 78,
    "Diana": 95,
    "Eve": 88,
    "Frank": 72
}

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Convert scores to letter grades
letter_grades = {name: get_letter_grade(score)
                 for name, score in students_scores.items()}
print("Letter Grades:")
for name, grade in letter_grades.items():
    print(f"{name}: {grade}")
# Alice: A
# Bob: B
# Charlie: C
# Diana: A
# Eve: B
# Frank: C

# Get only students who got A or B
top_students = {name: score for name, score in students_scores.items()
                if score >= 80}
print(f"\nTop students: {top_students}")
# Top students: {'Alice': 92, 'Bob': 85, 'Diana': 95, 'Eve': 88}

# Calculate grade distribution
grade_count = {}
for grade in letter_grades.values():
    grade_count[grade] = grade_count.get(grade, 0) + 1
print(f"\nGrade distribution: {grade_count}")
# Grade distribution: {'A': 2, 'B': 2, 'C': 2}
```

### Example 2: Word Frequency Counter

```python
# Count word occurrences
text = "the quick brown fox jumps over the lazy dog the fox"
words = text.split()

# Create frequency dictionary
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
print("Word frequencies:")
print(word_freq)
# {'the': 3, 'quick': 1, 'brown': 1, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

# Get words that appear more than once
repeated_words = {word: count for word, count in word_freq.items() if count > 1}
print(f"\nRepeated words: {repeated_words}")
# Repeated words: {'the': 3, 'fox': 2}

# Create length dictionary
word_lengths = {word: len(word) for word in set(words)}
print(f"\nWord lengths: {word_lengths}")
# Word lengths: {'brown': 5, 'lazy': 4, 'fox': 3, 'quick': 5, 'over': 4, 'jumps': 5, 'dog': 3, 'the': 3}

# Group words by length
from collections import defaultdict
words_by_length = defaultdict(list)
for word in set(words):
    words_by_length[len(word)].append(word)
print(f"\nWords grouped by length: {dict(words_by_length)}")
# Words grouped by length: {5: ['brown', 'quick', 'jumps'], 4: ['lazy', 'over'], 3: ['fox', 'dog', 'the']}
```

### Example 3: Product Inventory Management

```python
# Product inventory with prices
inventory = {
    "laptop": {"price": 999, "stock": 5},
    "mouse": {"price": 25, "stock": 50},
    "keyboard": {"price": 75, "stock": 30},
    "monitor": {"price": 299, "stock": 15},
    "headphones": {"price": 150, "stock": 0}
}

# Extract only prices
prices = {product: details["price"] for product, details in inventory.items()}
print("Prices:")
print(prices)
# {'laptop': 999, 'mouse': 25, 'keyboard': 75, 'monitor': 299, 'headphones': 150}

# Get in-stock products
in_stock = {product: details for product, details in inventory.items()
            if details["stock"] > 0}
print("\nIn-stock products:")
for product, details in in_stock.items():
    print(f"{product}: {details['stock']} units at ${details['price']}")
# laptop: 5 units at $999
# mouse: 50 units at $25
# keyboard: 30 units at $75
# monitor: 15 units at $299

# Apply 10% discount to expensive items (price > 100)
discounted = {product: details["price"] * 0.9
              for product, details in inventory.items()
              if details["price"] > 100}
print("\nDiscounted prices (10% off for items > $100):")
for product, price in discounted.items():
    print(f"{product}: ${price:.2f}")
# laptop: $899.10
# monitor: $269.10
# headphones: $135.00

# Calculate total inventory value
total_value = sum(details["price"] * details["stock"]
                  for details in inventory.values())
print(f"\nTotal inventory value: ${total_value}")
# Total inventory value: $11220
```

### Example 4: Data Transformation

```python
# Temperature readings in Fahrenheit
temp_readings = {
    "Monday": 68,
    "Tuesday": 72,
    "Wednesday": 65,
    "Thursday": 70,
    "Friday": 75,
    "Saturday": 78,
    "Sunday": 73
}

# Convert to Celsius
celsius_temps = {day: round((temp - 32) * 5/9, 1)
                 for day, temp in temp_readings.items()}
print("Temperatures in Celsius:")
for day, temp in celsius_temps.items():
    print(f"{day}: {temp}°C")
# Monday: 20.0°C
# Tuesday: 22.2°C
# Wednesday: 18.3°C
# Thursday: 21.1°C
# Friday: 23.9°C
# Saturday: 25.6°C
# Sunday: 22.8°C

# Get warm days (Fahrenheit > 70)
warm_days = {day: temp for day, temp in temp_readings.items() if temp > 70}
print(f"\nWarm days (>70°F): {warm_days}")
# Warm days (>70°F): {'Tuesday': 72, 'Friday': 75, 'Saturday': 78, 'Sunday': 73}

# Create day abbreviations
abbrev_temps = {day[:3]: temp for day, temp in temp_readings.items()}
print(f"\nAbbreviated: {abbrev_temps}")
# Abbreviated: {'Mon': 68, 'Tue': 72, 'Wed': 65, 'Thu': 70, 'Fri': 75, 'Sat': 78, 'Sun': 73}
```

### Example 5: User Data Processing

```python
# User data from a form
users = [
    {"id": 1, "name": "Alice", "email": "alice@email.com", "age": 25, "active": True},
    {"id": 2, "name": "Bob", "email": "bob@email.com", "age": 30, "active": True},
    {"id": 3, "name": "Charlie", "email": "charlie@email.com", "age": 35, "active": False},
    {"id": 4, "name": "Diana", "email": "diana@email.com", "age": 28, "active": True},
    {"id": 5, "name": "Eve", "email": "eve@email.com", "age": 32, "active": False}
]

# Create lookup dictionary by ID
users_by_id = {user["id"]: user for user in users}
print("User lookup by ID:")
print(f"User 3: {users_by_id[3]['name']}")
# User 3: Charlie

# Create email to name mapping
email_to_name = {user["email"]: user["name"] for user in users}
print(f"\nEmail mapping: {email_to_name}")
# Email mapping: {'alice@email.com': 'Alice', 'bob@email.com': 'Bob', ...}

# Get active users only
active_users = {user["name"]: user["email"] for user in users if user["active"]}
print(f"\nActive users: {active_users}")
# Active users: {'Alice': 'alice@email.com', 'Bob': 'bob@email.com', 'Diana': 'diana@email.com'}

# Create age groups
age_groups = {user["name"]: "Young" if user["age"] < 30 else "Senior"
              for user in users}
print(f"\nAge groups: {age_groups}")
# Age groups: {'Alice': 'Young', 'Bob': 'Senior', 'Charlie': 'Senior', 'Diana': 'Young', 'Eve': 'Senior'}

# Extract only names and ages for active users
active_ages = {user["name"]: user["age"] for user in users if user["active"]}
print(f"\nActive users with ages: {active_ages}")
# Active users with ages: {'Alice': 25, 'Bob': 30, 'Diana': 28}
```

## Swapping Keys and Values

```python
# Original dictionary
capital_cities = {
    "USA": "Washington DC",
    "UK": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo"
}

# Swap keys and values
city_to_country = {city: country for country, city in capital_cities.items()}
print(city_to_country)
# {'Washington DC': 'USA', 'London': 'UK', 'Paris': 'France', 'Berlin': 'Germany', 'Tokyo': 'Japan'}
```

## Conditional Expressions

```python
# If-else in dictionary comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parity = {n: "even" if n % 2 == 0 else "odd" for n in numbers}
print(parity)
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even'}
```

## Nested Dictionary Comprehensions

```python
# Create a multiplication table as nested dictionary
multiplication_table = {
    i: {j: i*j for j in range(1, 6)}
    for i in range(1, 6)
}
print("Multiplication Table:")
for i, row in multiplication_table.items():
    print(f"{i}: {row}")
# 1: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# 2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
# 3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15}
# 4: {1: 4, 2: 8, 3: 12, 4: 16, 5: 20}
# 5: {1: 5, 2: 10, 3: 15, 4: 20, 5: 25}
```

## Key Takeaways

1. **Dictionary comprehensions**: Concise syntax for creating dictionaries
2. **Syntax**: `{key: value for item in iterable if condition}`
3. **Filtering**: Use `if` condition to filter items
4. **Transformation**: Transform both keys and values
5. **From lists**: Use `zip()` to combine two lists
6. **Swapping**: Reverse key-value pairs easily
7. **Readability**: More Pythonic than traditional loops
8. **Best practice**: Use for simple transformations, avoid complex logic
