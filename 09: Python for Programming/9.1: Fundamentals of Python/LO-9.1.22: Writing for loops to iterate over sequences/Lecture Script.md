### LO-22 Write For Loops (20 minutes)


### CS Theory Bite

> **Origin**: For loops implement the **iterator pattern** (Gang of Four, 1994) — Python's `for` is actually a **for-each** loop, iterating over any iterable object, not just counting numbers.
>
> **Analogy**: A `for` loop is like a **conveyor belt** — items come one at a time, you process each, and it automatically stops at the end.
>
> **Why it matters**: For loops are the most common loop — 90% of iteration tasks are "do something for each item."


### Hook (2 minutes)

**Say**: "Want to print every student's name? You could copy-paste print() 30 times... or use a for loop and do it in 2 lines!"

```python
# Without for loop (while loop way)
fruits = ["apple", "banana", "orange"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# With for loop (clean!)
for fruit in fruits:
    print(fruit)
```

### For Loop Basics (6 minutes)

**Say**: "for loops automatically iterate through each item in a sequence."

```python
for item in sequence:
    # Do something with item
    # item is a variable holding current element
```

**Examples**:
```python
# List
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# String (each character!)
for letter in "Python":
    print(letter)  # P y t h o n

# Tuple
coords = (10, 20, 30)
for coord in coords:
    print(coord)
```

**Key Points**:
- No manual indexing needed
- Works with lists, strings, tuples, sets, dictionaries
- Loop variable gets each item automatically
- Can't modify the original list during iteration

### Dictionary Iteration (5 minutes)

**Say**: "Dictionaries are different - you can iterate keys, values, or both!"

```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Keys only (default)
for key in student:
    print(key)  # name, age, grade

# Values only
for value in student.values():
    print(value)  # Alice, 20, A

# Both keys and values
for key, value in student.items():
    print(f"{key}: {value}")
```

### Using Enumerate (4 minutes)

**Say**: "Need the index too? Use enumerate()!"

```python
colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(f"Position {index}: {color}")

# Output:
# Position 0: red
# Position 1: green
# Position 2: blue
```

**Real-World**: Numbered list
```python
tasks = ["Buy milk", "Call mom", "Finish homework"]

for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")
# 1. Buy milk
# 2. Call mom
# 3. Finish homework
```

### Practice (3 minutes)

Sum all numbers in a list:
```python
numbers = [5, 10, 15, 20, 25]

total = 0
for num in numbers:
    total += num

print(f"Sum: {total}")  # 75
```
