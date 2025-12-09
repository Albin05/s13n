# Pre-Read: Use Dictionary Comprehensions

## Dictionary Comprehensions

Dictionary comprehensions provide a concise way to create dictionaries:

```python
# Traditional way
squares_dict = {}
for i in range(5):
    squares_dict[i] = i ** 2

# Dictionary comprehension
squares_dict = {i: i ** 2 for i in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## Creating from Lists

```python
# Create dictionary from two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

people = {name: age for name, age in zip(names, ages)}
print(people)  # {'Alice': 25, 'Bob': 30, 'Charlie': 35}
```

## Filtering Dictionaries

```python
# Filter dictionary by value
prices = {"apple": 0.5, "banana": 0.3, "orange": 0.8, "grape": 1.2}
expensive = {fruit: price for fruit, price in prices.items() if price > 0.5}
print(expensive)  # {'orange': 0.8, 'grape': 1.2}
```

## Transforming Values

```python
# Convert values to uppercase
names = {"first": "john", "last": "doe"}
upper_names = {key: value.upper() for key, value in names.items()}
print(upper_names)  # {'first': 'JOHN', 'last': 'DOE'}
```
