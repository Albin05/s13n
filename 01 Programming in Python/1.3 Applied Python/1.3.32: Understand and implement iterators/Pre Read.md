# Pre-Read: Understand Iterators

## Iterators

An iterator is an object that implements the iterator protocol with `__iter__()` and `__next__()` methods:

```python
# Lists, strings, tuples are iterables
numbers = [1, 2, 3, 4, 5]

# Get iterator from iterable
iterator = iter(numbers)

# Get values one at a time
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
```

## Iterator Protocol

```python
class Counter:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max_value:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# Use the iterator
counter = Counter(5)
for num in counter:
    print(num)
# Output: 1, 2, 3, 4, 5
```

## Built-in Iterators

```python
# Using iter() and next()
text = "Hello"
text_iter = iter(text)

print(next(text_iter))  # H
print(next(text_iter))  # e
print(next(text_iter))  # l
```
