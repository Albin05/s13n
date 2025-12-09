# Lecture Notes: Extract List Portions with Slicing

## List Slicing

Extract a portion (sub-list) from a list using slicing.


---

<div align="center">

![Organized list representation](https://images.unsplash.com/photo-1586281380349-632531db7ed4?w=800&q=80)

*Lists are ordered collections that can store multiple items*

</div>

---
### Basic Syntax

```python
list[start:stop]  # From start to stop-1
list[start:stop:step]  # With step
```

## Examples

### Basic Slicing

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])  # [2, 3, 4] (indices 2, 3, 4)
print(numbers[0:3])  # [0, 1, 2] (first 3)
print(numbers[5:])   # [5, 6, 7, 8, 9] (from index 5 to end)
print(numbers[:4])   # [0, 1, 2, 3] (first 4)
```

### With Step

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[::2])    # [0, 2, 4, 6, 8] (every 2nd)
print(numbers[1::2])   # [1, 3, 5, 7, 9] (odd indices)
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed)
```

### Practical Examples

```python
# Get first 3
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[:3])  # ['apple', 'banana', 'cherry']

# Get last 2
print(fruits[-2:])  # ['date', 'elderberry']

# Get middle items
print(fruits[1:4])  # ['banana', 'cherry', 'date']
```

## Slicing Creates New List

```python
original = [1, 2, 3, 4, 5]
subset = original[1:4]
subset[0] = 100

print(original)  # [1, 2, 3, 4, 5] (unchanged!)
print(subset)    # [100, 3, 4]
```

## Key Takeaways

1. **[start:stop]**: Extract from start to stop-1
2. **Omit start**: Defaults to 0
3. **Omit stop**: Goes to end
4. **Negative indices**: Count from end
5. **[::-1]**: Reverse a list
