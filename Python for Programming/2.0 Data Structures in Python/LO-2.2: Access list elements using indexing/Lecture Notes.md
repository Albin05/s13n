# Lecture Notes: Access List Elements with Indexing

## List Indexing

Access individual list elements using their index (position).


---

<div align="center">

![Organized list representation](https://images.unsplash.com/photo-1586281380349-632531db7ed4?w=800&q=80)

*Lists are ordered collections that can store multiple items*

</div>

---
### Basic Indexing

```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])  # "apple" (first item)
print(fruits[1])  # "banana" (second item)
print(fruits[3])  # "date" (fourth item)
```

**Remember**: Python uses 0-based indexing!

### Negative Indexing

```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[-1])  # "date" (last item)
print(fruits[-2])  # "cherry" (second to last)
print(fruits[-4])  # "apple" (first item)
```

### Index Errors

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[10])  # IndexError: list index out of range
```

## Modifying Elements

```python
numbers = [10, 20, 30, 40]
numbers[0] = 15  # Change first item
print(numbers)  # [15, 20, 30, 40]
```

## Real-World Examples

### Access Student Data

```python
students = ["Alice", "Bob", "Charlie", "David"]
print(f"First student: {students[0]}")
print(f"Last student: {students[-1]}")
```

### Update Temperature

```python
temps = [72, 75, 78, 80]
temps[0] = 70  # Correct first reading
print(temps)
```

## Key Takeaways

1. **0-based**: First item is index 0
2. **Negative indexing**: -1 is last item
3. **Mutable**: Can change values
4. **Index errors**: Check bounds!
5. **Use len()**: Get list size
