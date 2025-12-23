# Lecture Notes: Create Lists

## Lists

A list is an ordered, mutable collection of items.


---

<div align="center">

![Organized list representation](https://images.unsplash.com/photo-1586281380349-632531db7ed4?w=800&q=80)

*Lists are ordered collections that can store multiple items*

</div>

---
### Creating Lists

```python
# Empty list
my_list = []

# List with items
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "hello", 3.14, True]
```

### List Characteristics

1. **Ordered**: Items maintain their position
2. **Mutable**: Can be changed after creation
3. **Allow duplicates**: Same value can appear multiple times
4. **Mixed types**: Can contain different data types

## Examples

### Shopping List

```python
shopping = ["milk", "eggs", "bread", "butter"]
print(shopping)  # ['milk', 'eggs', 'bread', 'butter']
```

### Number List

```python
scores = [85, 92, 78, 95, 88]
print(f"First score: {scores[0]}")  # 85
print(f"Number of scores: {len(scores)}")  # 5
```

### Creating from Range

```python
numbers = list(range(5))
print(numbers)  # [0, 1, 2, 3, 4]
```

## Key Takeaways

1. **Square brackets**: [] to create lists
2. **Comma-separated**: Items separated by commas
3. **Any type**: Can store any Python objects
4. **Ordered**: Position matters
5. **Mutable**: Can be modified
