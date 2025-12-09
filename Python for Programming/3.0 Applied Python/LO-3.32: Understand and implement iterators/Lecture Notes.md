# Lecture Notes: Understand Iterators

## Iterators

An iterator is an object that can be iterated upon, returning data one element at a time. It implements the iterator protocol consisting of `__iter__()` and `__next__()` methods.


---

<div align="center">

![Variables concept - labeled storage containers](https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800&q=80)

*Think of variables as labeled containers storing different types of data*

</div>

---
### Iterable vs Iterator

```python
# Iterable: object that can return an iterator
numbers = [1, 2, 3, 4, 5]  # List is iterable

# Iterator: object with __next__() method
iterator = iter(numbers)  # Get iterator from iterable

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
```

## The Iterator Protocol

```python
class Counter:
    """A simple counter iterator"""

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        """Return the iterator object (self)"""
        return self

    def __next__(self):
        """Return the next value"""
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# Using the iterator
counter = Counter(1, 5)
for num in counter:
    print(num, end=" ")
# Output: 1 2 3 4 5

print()

# Using next() manually
counter2 = Counter(1, 3)
print(next(counter2))  # 1
print(next(counter2))  # 2
print(next(counter2))  # 3
# print(next(counter2))  # Would raise StopIteration
```

## Built-in Iterators

```python
# Strings are iterable
text = "Python"
text_iter = iter(text)

print(next(text_iter))  # P
print(next(text_iter))  # y
print(next(text_iter))  # t

# Lists are iterable
numbers = [10, 20, 30]
num_iter = iter(numbers)

print(next(num_iter))  # 10
print(next(num_iter))  # 20

# Dictionaries are iterable (iterate over keys)
person = {"name": "Alice", "age": 25}
dict_iter = iter(person)

print(next(dict_iter))  # name
print(next(dict_iter))  # age
```

## Real-World Examples

### Example 1: Custom Range Iterator

```python
class CustomRange:
    """Custom implementation of range() as an iterator"""

    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or \
           (self.step < 0 and self.current <= self.stop):
            raise StopIteration

        value = self.current
        self.current += self.step
        return value

# Test the custom range
print("Custom range 0 to 10, step 2:")
for num in CustomRange(0, 10, 2):
    print(num, end=" ")
# Output: 0 2 4 6 8
print()

print("\nCustom range 10 to 0, step -2:")
for num in CustomRange(10, 0, -2):
    print(num, end=" ")
# Output: 10 8 6 4 2
print()

# Using list() to convert iterator to list
print("\nAs a list:")
print(list(CustomRange(1, 6)))
# Output: [1, 2, 3, 4, 5]
```

### Example 2: File Line Iterator

```python
class FileLineIterator:
    """Iterator that reads file line by line"""

    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __iter__(self):
        self.file = open(self.filename, 'r')
        return self

    def __next__(self):
        if self.file is None:
            raise StopIteration

        line = self.file.readline()

        if line:
            return line.strip()
        else:
            self.file.close()
            raise StopIteration

# Simulate with a list of lines
class SimulatedFileIterator:
    """Simulates reading lines from a file"""

    def __init__(self):
        self.lines = [
            "First line of the file",
            "Second line of the file",
            "Third line of the file",
            "Last line of the file"
        ]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.lines):
            line = self.lines[self.index]
            self.index += 1
            return line
        else:
            raise StopIteration

print("Reading file lines:")
for line in SimulatedFileIterator():
    print(f"- {line}")
# Output:
# - First line of the file
# - Second line of the file
# - Third line of the file
# - Last line of the file
```

### Example 3: Reverse Iterator

```python
class ReverseIterator:
    """Iterator that returns items in reverse order"""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index -= 1
        return self.data[self.index]

# Test reverse iterator
numbers = [1, 2, 3, 4, 5]
print("Numbers in reverse:")
for num in ReverseIterator(numbers):
    print(num, end=" ")
# Output: 5 4 3 2 1
print()

# Reverse a string
text = "Python"
print("\nReversed text:")
for char in ReverseIterator(text):
    print(char, end="")
# Output: nohtyP
print()
```

### Example 4: Even Numbers Iterator

```python
class EvenNumbers:
    """Iterator that yields only even numbers from a list"""

    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.numbers):
            current = self.numbers[self.index]
            self.index += 1

            if current % 2 == 0:
                return current

        raise StopIteration

# Test even numbers iterator
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers:")
for num in EvenNumbers(numbers):
    print(num, end=" ")
# Output: 2 4 6 8 10
print()

# Another example
mixed_numbers = [15, 22, 33, 48, 51, 62]
print("\nEven numbers from mixed list:")
for num in EvenNumbers(mixed_numbers):
    print(num, end=" ")
# Output: 22 48 62
print()
```

### Example 5: Cycling Iterator

```python
class CycleIterator:
    """Iterator that cycles through items infinitely"""

    def __init__(self, data, max_cycles=None):
        self.data = data
        self.max_cycles = max_cycles
        self.index = 0
        self.cycle_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.max_cycles is not None and self.cycle_count >= self.max_cycles:
            raise StopIteration

        if not self.data:
            raise StopIteration

        value = self.data[self.index]
        self.index += 1

        if self.index >= len(self.data):
            self.index = 0
            self.cycle_count += 1

        return value

# Test cycling iterator
colors = ["red", "green", "blue"]
print("Cycling through colors (2 complete cycles):")
cycle = CycleIterator(colors, max_cycles=2)
for i, color in enumerate(cycle):
    print(f"{i+1}. {color}")
# Output:
# 1. red
# 2. green
# 3. blue
# 4. red
# 5. green
# 6. blue

print()

# Use in assignment rotation
tasks = ["Task A", "Task B", "Task C"]
people = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
task_cycle = CycleIterator(tasks, max_cycles=2)

print("Task assignments:")
for person in people:
    try:
        task = next(task_cycle)
        print(f"{person}: {task}")
    except StopIteration:
        print(f"{person}: No more tasks")
# Output:
# Alice: Task A
# Bob: Task B
# Charlie: Task C
# Diana: Task A
# Eve: Task B
```

## Iterator Tools from itertools

```python
import itertools

# count() - infinite counter
counter = itertools.count(start=10, step=2)
print("First 5 from count:")
for i, num in enumerate(counter):
    if i >= 5:
        break
    print(num, end=" ")
# Output: 10 12 14 16 18
print()

# cycle() - cycle through iterable infinitely
colors = ["red", "green", "blue"]
color_cycle = itertools.cycle(colors)
print("\nFirst 8 from cycle:")
for i, color in enumerate(color_cycle):
    if i >= 8:
        break
    print(color, end=" ")
# Output: red green blue red green blue red green
print()

# repeat() - repeat a value
repeater = itertools.repeat("Hello", 3)
print("\nRepeat:")
for item in repeater:
    print(item, end=" ")
# Output: Hello Hello Hello
print()

# chain() - chain multiple iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
chained = itertools.chain(list1, list2, list3)
print("\nChained:")
print(list(chained))
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# islice() - slice an iterator
numbers = itertools.count(0)
first_10 = itertools.islice(numbers, 10)
print("\nFirst 10 numbers:")
print(list(first_10))
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Iterator vs Iterable

```python
# Iterable: can be looped over multiple times
numbers_list = [1, 2, 3]
print("First loop:")
for num in numbers_list:
    print(num, end=" ")
print("\nSecond loop (works fine):")
for num in numbers_list:
    print(num, end=" ")
print()

# Iterator: can only be looped over once
numbers_iter = iter([1, 2, 3])
print("\nFirst loop with iterator:")
for num in numbers_iter:
    print(num, end=" ")
print("\nSecond loop with iterator (empty):")
for num in numbers_iter:
    print(num, end=" ")
print("(nothing printed)")
```

## Creating Iterable Classes

```python
class Countdown:
    """An iterable class (not an iterator itself)"""

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        """Return a new iterator each time"""
        return CountdownIterator(self.start)

class CountdownIterator:
    """The actual iterator"""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Can iterate multiple times
countdown = Countdown(3)

print("First countdown:")
for num in countdown:
    print(num, end=" ")
# Output: 3 2 1
print()

print("Second countdown (works because __iter__ returns new iterator):")
for num in countdown:
    print(num, end=" ")
# Output: 3 2 1
print()
```

## Key Takeaways

1. **Iterator protocol**: Requires `__iter__()` and `__next__()` methods
2. **__iter__()**: Returns the iterator object (usually self)
3. **__next__()**: Returns the next value or raises StopIteration
4. **StopIteration**: Signals the end of iteration
5. **Iterable vs Iterator**: Iterables can create iterators, iterators are consumed once
6. **Built-in support**: Lists, strings, dicts, etc. are iterables
7. **itertools module**: Provides powerful iterator tools
8. **Memory efficient**: Process one item at a time
