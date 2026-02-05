# Lecture Script: LO-9.3.32 Understand and Implement Iterators

## [0:00-0:02] Hook (2 min)
**Say**: "Every for loop you've ever written uses iterators under the hood. When you write 'for item in my_list', Python calls iter() to get an iterator, then repeatedly calls next(). Today we'll pull back the curtain and build our own iterators from scratch!"

**Demo**:
```python
# What Python does behind the scenes
numbers = [1, 2, 3]
iterator = iter(numbers)  # Get iterator
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3

# Create our own!
class Counter:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.max_num:
            raise StopIteration
        self.current += 1
        return self.current

for num in Counter(5):
    print(num, end=" ")  # 1 2 3 4 5
```

**Say**: "That's the iterator protocol! Let's master it."

## [0:02-0:07] The Iterator Protocol (5 min)

**Say**: "Two magic methods define an iterator: __iter__() returns the iterator object, and __next__() returns the next value."

**Live Code**:
```python
class SimpleCounter:
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
            raise StopIteration  # Signal end of iteration
        else:
            value = self.current
            self.current += 1
            return value

# Using the iterator
counter = SimpleCounter(1, 5)
for num in counter:
    print(num, end=" ")  # 1 2 3 4 5

print()

# Using next() manually
counter2 = SimpleCounter(1, 3)
print(next(counter2))  # 1
print(next(counter2))  # 2
print(next(counter2))  # 3
try:
    print(next(counter2))  # Raises StopIteration
except StopIteration:
    print("Iterator exhausted!")
```

**Point out**: "__iter__() returns self, making the object iterable. __next__() provides values one at a time."

**Emphasize**: "Raising StopIteration tells Python the iteration is complete. Never return None instead!"

## [0:07-0:11] Iterable vs Iterator (4 min)

**Say**: "Important distinction: an iterable CAN create an iterator. An iterator IS the thing that yields values."

**Live Code**:
```python
# Built-in iterables
numbers = [1, 2, 3, 4, 5]  # List is iterable, not an iterator
print(f"Type: {type(numbers)}")

# Get iterator from iterable
iterator = iter(numbers)
print(f"Iterator type: {type(iterator)}")

# Iterator can only be used once
print(next(iterator))  # 1
print(next(iterator))  # 2

# Loop uses remaining values
for num in iterator:
    print(num, end=" ")  # 3 4 5
print()

# Now exhausted
for num in iterator:
    print(num)  # Nothing prints!

print("Iterator is exhausted")

# But the original list can be iterated again
for num in numbers:
    print(num, end=" ")  # 1 2 3 4 5
print()
```

**Point out**: "Lists are reusable because iter() creates a NEW iterator each time. Iterator objects are consumed once."

**Live Code - Make a Reusable Iterable**:
```python
class Countdown:
    """An iterable class (not an iterator itself)"""

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        """Return a NEW iterator each time"""
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

# Can iterate multiple times!
countdown = Countdown(3)

print("First countdown:")
for num in countdown:
    print(num, end=" ")  # 3 2 1
print()

print("Second countdown:")
for num in countdown:
    print(num, end=" ")  # 3 2 1
print()
```

**Emphasize**: "Separate iterable and iterator classes when you need multiple iterations!"

## [0:11-0:14] Real-World Example: Custom Range (3 min)

**Say**: "Let's build our own version of Python's range() function."

**Live Code**:
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
        # Forward iteration
        if self.step > 0 and self.current >= self.stop:
            raise StopIteration
        # Backward iteration
        if self.step < 0 and self.current <= self.stop:
            raise StopIteration

        value = self.current
        self.current += self.step
        return value

# Test forward iteration
print("Forward range 0 to 10, step 2:")
for num in CustomRange(0, 10, 2):
    print(num, end=" ")  # 0 2 4 6 8
print()

# Test backward iteration
print("Backward range 10 to 0, step -2:")
for num in CustomRange(10, 0, -2):
    print(num, end=" ")  # 10 8 6 4 2
print()

# Convert to list
print("As a list:", list(CustomRange(1, 6)))
# [1, 2, 3, 4, 5]
```

**Say**: "This is exactly how Python's range() works internally — it's an iterator!"

## [0:14-0:17] Real-World Example: Reverse Iterator (3 min)

**Say**: "Let's create an iterator that traverses any sequence in reverse."

**Live Code**:
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

# Reverse a list
numbers = [1, 2, 3, 4, 5]
print("Numbers in reverse:")
for num in ReverseIterator(numbers):
    print(num, end=" ")  # 5 4 3 2 1
print()

# Reverse a string
text = "Python"
print("Reversed text:")
for char in ReverseIterator(text):
    print(char, end="")  # nohtyP
print()

# Works with any sequence!
tuple_data = ('a', 'b', 'c', 'd')
print("Reversed tuple:", list(ReverseIterator(tuple_data)))
```

**Point out**: "Our iterator works with any sequence — lists, strings, tuples. That's the power of the iterator protocol!"

## [0:17-0:20] Real-World Example: Filtering Iterator (3 min)

**Say**: "Iterators can filter data on-the-fly, yielding only items that match a condition."

**Live Code**:
```python
class EvenNumbers:
    """Iterator that yields only even numbers"""

    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Keep searching for next even number
        while self.index < len(self.numbers):
            current = self.numbers[self.index]
            self.index += 1

            if current % 2 == 0:
                return current

        # No more even numbers
        raise StopIteration

# Test
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers:")
for num in EvenNumbers(numbers):
    print(num, end=" ")  # 2 4 6 8 10
print()

# Another example
mixed = [15, 22, 33, 48, 51, 62, 77, 88]
print("Even numbers from mixed:", list(EvenNumbers(mixed)))
# [22, 48, 62, 88]
```

**Say**: "The iterator skips odd numbers automatically. Memory efficient — no intermediate lists!"

## [0:20-0:22] The itertools Module (2 min)

**Say**: "Python's itertools module provides powerful built-in iterators. Let's see a few!"

**Live Code**:
```python
import itertools

# count() - infinite counter
print("First 5 from count:")
counter = itertools.count(start=10, step=2)
for i, num in enumerate(counter):
    if i >= 5:
        break
    print(num, end=" ")  # 10 12 14 16 18
print()

# cycle() - repeat sequence infinitely
colors = ["red", "green", "blue"]
color_cycle = itertools.cycle(colors)
print("First 8 from cycle:")
for i, color in enumerate(color_cycle):
    if i >= 8:
        break
    print(color, end=" ")  # red green blue red green blue red green
print()

# chain() - combine multiple iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
chained = itertools.chain(list1, list2, list3)
print("Chained:", list(chained))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# islice() - slice an iterator
numbers = itertools.count(0)
first_10 = itertools.islice(numbers, 10)
print("First 10:", list(first_10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Point out**: "itertools provides production-ready iterators for common patterns!"

## [0:22-0:23] Practice Challenge (1 min)

**Challenge**: "Create a CycleIterator that repeats a sequence a specific number of times."

**Skeleton**:
```python
class CycleIterator:
    def __init__(self, data, max_cycles):
        self.data = data
        self.max_cycles = max_cycles
        # TODO: Add tracking variables

    def __iter__(self):
        # TODO
        pass

    def __next__(self):
        # TODO: Return items, cycling through data
        pass

# Test
colors = ["red", "green", "blue"]
cycle = CycleIterator(colors, 2)
for color in cycle:
    print(color, end=" ")
# Should print: red green blue red green blue
```

**Solution** (show after 1 minute):
```python
class CycleIterator:
    def __init__(self, data, max_cycles):
        self.data = data
        self.max_cycles = max_cycles
        self.index = 0
        self.cycle_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cycle_count >= self.max_cycles:
            raise StopIteration

        value = self.data[self.index]
        self.index += 1

        if self.index >= len(self.data):
            self.index = 0
            self.cycle_count += 1

        return value
```

## [0:23-0:25] Wrap-up (2 min)

**Key Points**:
1. **Iterator protocol**: Implement __iter__() and __next__()
2. **__iter__()**: Returns self (the iterator object)
3. **__next__()**: Returns next value or raises StopIteration
4. **Iterable vs Iterator**: Iterables create iterators, iterators are consumed once
5. **StopIteration**: Signals end of iteration — never return None

**Common Mistakes**:
- Forgetting to raise StopIteration (infinite loop!)
- Returning None instead of raising StopIteration
- Making iterator and iterable the same when you need multiple passes
- Not resetting state when __iter__() is called

**Real-World Use Cases**:
- Custom data structure traversal
- Lazy data loading from databases or files
- Filtering and transforming sequences
- Implementing custom range-like functions
- Building data pipelines

**When to Use**:
- Need fine control over iteration
- Want to iterate complex data structures
- Building a library or framework
- Working with infinite sequences

**When NOT to Use**:
- Simple one-time iterations (use generator instead)
- Built-in types already work (don't reinvent the wheel)

**Closing**: "Iterators are fundamental to Python! Now you understand what happens when you write a for loop, and you can create custom iteration patterns for any data structure!"
