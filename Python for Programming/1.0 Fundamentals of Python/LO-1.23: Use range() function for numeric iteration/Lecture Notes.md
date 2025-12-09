# Lecture Notes: Use Range Function

## The Range Function

`range()` generates a sequence of numbers, commonly used with for loops.


---

<div align="center">

![Circular pattern representing loops](https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=800&q=80)

*Loops allow you to repeat operations efficiently*

</div>

---
### Three Forms

```python
range(stop)              # 0 to stop-1
range(start, stop)       # start to stop-1
range(start, stop, step) # start to stop-1, by step
```

## Examples

### Form 1: range(stop)

```python
for i in range(5):
    print(i)

# Output: 0 1 2 3 4 (stops before 5!)
```

### Form 2: range(start, stop)

```python
for i in range(2, 7):
    print(i)

# Output: 2 3 4 5 6 (stops before 7!)
```

### Form 3: range(start, stop, step)

```python
for i in range(0, 10, 2):
    print(i)

# Output: 0 2 4 6 8 (even numbers)
```

### Counting Down

```python
for i in range(5, 0, -1):
    print(i)

# Output: 5 4 3 2 1 (countdown)
```

## Real-World Applications

### Multiplication Table

```python
num = 5

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

### Year Range

```python
for year in range(2020, 2025):
    print(f"Year: {year}")

# Output: 2020 2021 2022 2023 2024
```

### Skip Every Third

```python
for i in range(0, 20, 3):
    print(i)

# Output: 0 3 6 9 12 15 18
```

## Range with Lists

```python
fruits = ["apple", "banana", "cherry"]

# Access by index
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Output:
# 0: apple
# 1: banana
# 2: cherry
```

## Key Takeaways

1. **Generates numbers**: Not a list, but a range object
2. **Stops before end**: range(5) goes 0 to 4, not 5
3. **Default start**: 0 if not specified
4. **Default step**: 1 if not specified
5. **Can count down**: Use negative step
