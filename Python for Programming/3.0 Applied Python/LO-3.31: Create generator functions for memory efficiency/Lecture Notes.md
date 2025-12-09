# Lecture Notes: Create Generator Functions

## Generator Functions

Generator functions use the `yield` keyword to return values lazily, one at a time, instead of creating and storing all values in memory at once.


---

<div align="center">

![Function machine concept - input to output](https://images.unsplash.com/photo-1581291518857-4e27b48ff24e?w=800&q=80)

*Functions are reusable blocks of code that take inputs and return outputs*

</div>

---
### Syntax

```python
def generator_name():
    # code
    yield value
    # more code
    yield another_value
```

## Basic Generator Function

```python
# Simple generator
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Using the generator
counter = count_up_to(5)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3

# Or use in a loop
for num in count_up_to(5):
    print(num)
# Output: 1, 2, 3, 4, 5
```

## Yield vs Return

```python
# Regular function with return
def get_squares(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result  # Returns entire list at once

squares_list = get_squares(5)
print(squares_list)  # [0, 1, 4, 9, 16]

# Generator function with yield
def generate_squares(n):
    for i in range(n):
        yield i ** 2  # Yields one value at a time

squares_gen = generate_squares(5)
print(squares_gen)  # <generator object>
print(list(squares_gen))  # [0, 1, 4, 9, 16]
```

## How Generators Work

```python
def simple_generator():
    print("First yield")
    yield 1
    print("Second yield")
    yield 2
    print("Third yield")
    yield 3
    print("Generator complete")

# Create generator object
gen = simple_generator()

print("Generator created")
print(next(gen))  # First yield, then returns 1
print(next(gen))  # Second yield, then returns 2
print(next(gen))  # Third yield, then returns 3
# print(next(gen))  # Would raise StopIteration

# Output:
# Generator created
# First yield
# 1
# Second yield
# 2
# Third yield
# 3
```

## Real-World Examples

### Example 1: Reading Large Files

```python
def read_large_file(file_path):
    """
    Read file line by line without loading entire file into memory
    """
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Simulate with a list for demonstration
def read_log_entries():
    """Simulate reading log entries"""
    logs = [
        "2024-01-01 10:00:00 INFO: Server started",
        "2024-01-01 10:05:00 WARNING: High memory usage",
        "2024-01-01 10:10:00 ERROR: Connection failed",
        "2024-01-01 10:15:00 INFO: Connection restored",
        "2024-01-01 10:20:00 INFO: Request processed"
    ]
    for log in logs:
        yield log

# Process logs one at a time
print("Processing logs:")
for log_entry in read_log_entries():
    if "ERROR" in log_entry:
        print(f"Found error: {log_entry}")
# Found error: 2024-01-01 10:10:00 ERROR: Connection failed

# Get only warning and error logs
def filter_logs(log_generator, level):
    """Filter logs by level"""
    for log in log_generator:
        if level in log:
            yield log

warnings_and_errors = filter_logs(read_log_entries(), "WARNING")
for log in warnings_and_errors:
    print(log)
# 2024-01-01 10:05:00 WARNING: High memory usage
```

### Example 2: Infinite Sequences

```python
def infinite_counter(start=0):
    """Generate infinite sequence of numbers"""
    count = start
    while True:
        yield count
        count += 1

# Use with a limit
counter = infinite_counter(1)
for i in range(10):
    print(next(counter), end=" ")
# Output: 1 2 3 4 5 6 7 8 9 10

print()

def fibonacci_generator():
    """Generate Fibonacci sequence indefinitely"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Get first 10 Fibonacci numbers
fib = fibonacci_generator()
fibonacci_numbers = [next(fib) for _ in range(10)]
print(f"First 10 Fibonacci numbers: {fibonacci_numbers}")
# First 10 Fibonacci numbers: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def prime_generator():
    """Generate prime numbers indefinitely"""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Get first 10 prime numbers
primes = prime_generator()
first_10_primes = [next(primes) for _ in range(10)]
print(f"First 10 primes: {first_10_primes}")
# First 10 primes: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

### Example 3: Data Processing Pipeline

```python
def load_data():
    """Simulate loading data from a database"""
    data = [
        {"id": 1, "name": "Alice", "score": 85},
        {"id": 2, "name": "Bob", "score": 92},
        {"id": 3, "name": "Charlie", "score": 78},
        {"id": 4, "name": "Diana", "score": 95},
        {"id": 5, "name": "Eve", "score": 88}
    ]
    for record in data:
        yield record

def filter_passing(data_generator, passing_score=80):
    """Filter records with score >= passing_score"""
    for record in data_generator:
        if record["score"] >= passing_score:
            yield record

def add_grade(data_generator):
    """Add letter grade to each record"""
    for record in data_generator:
        score = record["score"]
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        else:
            grade = "F"

        record["grade"] = grade
        yield record

def format_output(data_generator):
    """Format records for display"""
    for record in data_generator:
        yield f"{record['name']}: {record['score']}% (Grade: {record['grade']})"

# Chain generators together
print("Students who passed:")
pipeline = load_data()
pipeline = filter_passing(pipeline)
pipeline = add_grade(pipeline)
pipeline = format_output(pipeline)

for result in pipeline:
    print(result)
# Students who passed:
# Alice: 85% (Grade: B)
# Bob: 92% (Grade: A)
# Diana: 95% (Grade: A)
# Eve: 88% (Grade: B)
```

### Example 4: Batch Processing

```python
def batch_generator(items, batch_size):
    """
    Yield items in batches of specified size
    Useful for processing large datasets in chunks
    """
    batch = []
    for item in items:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []

    # Yield remaining items if any
    if batch:
        yield batch

# Process numbers in batches of 3
numbers = range(1, 11)
print("Processing in batches of 3:")
for batch in batch_generator(numbers, 3):
    print(f"Batch: {batch}, Sum: {sum(batch)}")
# Processing in batches of 3:
# Batch: [1, 2, 3], Sum: 6
# Batch: [4, 5, 6], Sum: 15
# Batch: [7, 8, 9], Sum: 24
# Batch: [10], Sum: 10

def sliding_window(items, window_size):
    """
    Generate sliding windows over a sequence
    """
    items_list = list(items)
    for i in range(len(items_list) - window_size + 1):
        yield items_list[i:i + window_size]

# Generate sliding windows
data = [1, 2, 3, 4, 5, 6]
print("\nSliding windows of size 3:")
for window in sliding_window(data, 3):
    print(window)
# Sliding windows of size 3:
# [1, 2, 3]
# [2, 3, 4]
# [3, 4, 5]
# [4, 5, 6]
```

### Example 5: Range Generators

```python
def custom_range(start, stop, step=1):
    """
    Custom implementation of range() using generator
    """
    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    elif step < 0:
        while current > stop:
            yield current
            current += step

print("Custom range 0 to 10, step 2:")
for num in custom_range(0, 10, 2):
    print(num, end=" ")
# Output: 0 2 4 6 8
print()

print("\nCustom range 10 to 0, step -2:")
for num in custom_range(10, 0, -2):
    print(num, end=" ")
# Output: 10 8 6 4 2
print()

def date_range(start_date, end_date):
    """
    Generate dates between start and end
    """
    from datetime import datetime, timedelta

    current = start_date
    while current <= end_date:
        yield current
        current += timedelta(days=1)

# Generate dates for a week
from datetime import datetime
start = datetime(2024, 1, 1)
end = datetime(2024, 1, 7)

print("\nDates in first week of 2024:")
for date in date_range(start, end):
    print(date.strftime("%Y-%m-%d"))
# 2024-01-01
# 2024-01-02
# ... through 2024-01-07

def countdown_timer(seconds):
    """
    Countdown from given seconds to 0
    """
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        yield f"{mins:02d}:{secs:02d}"
        seconds -= 1

print("\nCountdown from 5 seconds:")
for time_left in countdown_timer(5):
    print(time_left, end=" ")
# Output: 00:05 00:04 00:03 00:02 00:01 00:00
print()
```

## Generator Expressions

```python
# Generator expression (similar to list comprehension but with parentheses)
squares_gen = (x ** 2 for x in range(10))
print(squares_gen)  # <generator object>
print(list(squares_gen))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Memory efficient filtering
even_squares = (x ** 2 for x in range(1000000) if x % 2 == 0)
first_five = [next(even_squares) for _ in range(5)]
print(f"First 5 even squares: {first_five}")
# First 5 even squares: [0, 4, 16, 36, 64]
```

## Using send() with Generators

```python
def echo_generator():
    """Generator that can receive values"""
    while True:
        received = yield
        if received is not None:
            print(f"Received: {received}")

gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")   # Received: Hello
gen.send("World")   # Received: World
```

## Key Takeaways

1. **Generators**: Functions that use `yield` instead of `return`
2. **Lazy evaluation**: Values generated on-demand, not stored in memory
3. **Memory efficient**: Ideal for large datasets or infinite sequences
4. **State preservation**: Generator maintains its state between calls
5. **One-time use**: Generators are exhausted after iteration
6. **Generator expressions**: Like list comprehensions but with parentheses
7. **Chaining**: Generators can be chained for data pipelines
8. **Best practice**: Use for large data processing, file reading, infinite sequences
