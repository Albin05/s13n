# Lecture Script: LO-9.3.31 Create Generator Functions


### CS Theory Bite

> **Origin**: Generators (Python 2.2, PEP 255) implement **lazy evaluation** — computing values on-demand instead of all at once. Inspired by **CLU iterators** (1970s) and **Icon language** generators.
>
> **Analogy**: A generator is like **streaming video** — data arrives as needed instead of downloading the entire movie first.
>
> **Why it matters**: Generators process infinite sequences and huge files with constant memory — essential for data pipelines.


## [0:00-0:02] Hook (2 min)
**Say**: "Imagine you need to process a billion numbers. With a normal function, you'd create a list of a billion items in memory — instant crash! But with generators, you create numbers one at a time, as needed. Memory efficient, lightning fast, and incredibly powerful."

**Demo**:
```python
# Normal function - creates everything in memory
def get_numbers(n):
    return [i for i in range(n)]

# Generator - creates one at a time
def generate_numbers(n):
    for i in range(n):
        yield i

# This works perfectly with huge numbers!
for num in generate_numbers(10):
    print(num, end=" ")
# 0 1 2 3 4 5 6 7 8 9
```

**Say**: "That's the power of generators! Let's master them."

## [0:02-0:07] Understanding yield vs return (5 min)

**Say**: "The key difference: return gives you everything at once and exits. yield gives you one item, pauses, and remembers where it left off."

**Live Code**:
```python
# Regular function with return
def get_squares(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result  # Returns entire list

squares = get_squares(5)
print(squares)  # [0, 1, 4, 9, 16]
print(type(squares))  # <class 'list'>

# Generator function with yield
def generate_squares(n):
    for i in range(n):
        yield i ** 2  # Yields one at a time

squares_gen = generate_squares(5)
print(squares_gen)  # <generator object>
print(type(squares_gen))  # <class 'generator'>

# Use next() to get values one by one
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4

# Or use in a loop
for square in generate_squares(5):
    print(square, end=" ")  # 0 1 4 9 16
```

**Point out**: "The generator object doesn't hold all values — it generates them on demand! Memory efficient!"

**Emphasize**: "Once you iterate through a generator, it's exhausted. You can't iterate again without creating a new generator."

```python
gen = generate_squares(3)
print(list(gen))  # [0, 1, 4]
print(list(gen))  # [] - exhausted!
```

## [0:07-0:11] How Generators Work (4 min)

**Say**: "Let's see exactly how generators pause and resume execution."

**Live Code**:
```python
def countdown(n):
    print(f"Starting countdown from {n}")
    while n > 0:
        print(f"About to yield {n}")
        yield n
        print(f"Resumed after yielding {n}")
        n -= 1
    print("Countdown complete!")

# Create generator - nothing runs yet!
gen = countdown(3)
print("Generator created")

# First next() - runs until first yield
print("\nCalling next():")
print(next(gen))

# Second next() - resumes from where it left off
print("\nCalling next() again:")
print(next(gen))

# Third next()
print("\nCalling next() again:")
print(next(gen))
```

**Expected Output**:
```
Generator created

Calling next():
Starting countdown from 3
About to yield 3
3

Calling next() again:
Resumed after yielding 3
About to yield 2
2

Calling next() again:
Resumed after yielding 2
About to yield 1
1
```

**Point out**: "The generator PAUSES at each yield, maintains its state, and resumes when next() is called!"

## [0:11-0:15] Real-World Example: Reading Large Files (4 min)

**Say**: "Perfect use case — reading huge log files without loading everything into memory."

**Live Code**:
```python
def read_log_entries():
    """Simulate reading log entries from a large file"""
    logs = [
        "2024-01-01 10:00:00 INFO: Server started",
        "2024-01-01 10:05:00 WARNING: High memory usage",
        "2024-01-01 10:10:00 ERROR: Connection failed",
        "2024-01-01 10:15:00 INFO: Connection restored",
        "2024-01-01 10:20:00 ERROR: Disk space low",
        "2024-01-01 10:25:00 INFO: Request processed"
    ]
    for log in logs:
        yield log

# Process only ERROR logs - memory efficient!
print("Finding errors:")
for log in read_log_entries():
    if "ERROR" in log:
        print(f"  {log}")

# Chain generators for filtering
def filter_by_level(log_generator, level):
    """Generator that filters logs by level"""
    for log in log_generator:
        if level in log:
            yield log

# Get only warnings
print("\nWarnings:")
for log in filter_by_level(read_log_entries(), "WARNING"):
    print(f"  {log}")
```

**Say**: "Notice how we process millions of log lines without ever loading them all into memory!"

**Emphasize**: "In real code, replace the logs list with: with open('huge_file.log') as f: for line in f: yield line.strip()"

## [0:15-0:18] Generator Expressions and Infinite Sequences (3 min)

**Say**: "Generator expressions are like list comprehensions but with parentheses!"

**Live Code**:
```python
# List comprehension - creates entire list in memory
squares_list = [x ** 2 for x in range(10)]
print(f"List: {squares_list}")

# Generator expression - creates values on demand
squares_gen = (x ** 2 for x in range(10))
print(f"Generator: {squares_gen}")
print(f"Values: {list(squares_gen)}")

# Memory efficient filtering
even_squares = (x ** 2 for x in range(1000000) if x % 2 == 0)
first_five = [next(even_squares) for _ in range(5)]
print(f"First 5 even squares: {first_five}")

# Infinite generator - create sequences forever!
def fibonacci_generator():
    """Generate Fibonacci sequence indefinitely"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Get first 10 Fibonacci numbers
fib = fibonacci_generator()
fib_numbers = [next(fib) for _ in range(10)]
print(f"First 10 Fibonacci: {fib_numbers}")
```

**Point out**: "Infinite generators are perfect when you don't know how many values you'll need!"

## [0:18-0:21] Real-World Example: Data Processing Pipeline (3 min)

**Say**: "Generators shine when chaining operations — each step processes one item at a time."

**Live Code**:
```python
def load_students():
    """Simulate loading student records"""
    students = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 78},
        {"name": "Diana", "score": 95},
        {"name": "Eve", "score": 88}
    ]
    for student in students:
        yield student

def filter_passing(student_gen, passing_score=80):
    """Filter students who passed"""
    for student in student_gen:
        if student["score"] >= passing_score:
            yield student

def add_letter_grade(student_gen):
    """Add letter grade to each student"""
    for student in student_gen:
        score = student["score"]
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        else:
            grade = "F"
        student["grade"] = grade
        yield student

def format_output(student_gen):
    """Format students for display"""
    for student in student_gen:
        yield f"{student['name']}: {student['score']}% (Grade: {student['grade']})"

# Chain generators together - clean pipeline!
print("Students who passed:")
pipeline = load_students()
pipeline = filter_passing(pipeline)
pipeline = add_letter_grade(pipeline)
pipeline = format_output(pipeline)

for result in pipeline:
    print(f"  {result}")
```

**Say**: "Each generator processes one student at a time. With millions of students, this uses constant memory!"

## [0:21-0:23] Practice Challenge (2 min)

**Challenge**: "Create a generator that yields only even numbers from a list, and another that batches items."

**Give them this skeleton**:
```python
def even_numbers(numbers):
    # TODO: yield only even numbers
    pass

def batch_generator(items, batch_size):
    # TODO: yield items in batches
    pass

# Test
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers:", list(even_numbers(nums)))

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Batches of 3:")
for batch in batch_generator(data, 3):
    print(batch)
```

**Solution** (show after 1-2 minutes):
```python
def even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

def batch_generator(items, batch_size):
    batch = []
    for item in items:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:  # Don't forget remaining items!
        yield batch
```

## [0:23-0:25] Wrap-up (2 min)

**Key Points**:
1. **yield vs return**: yield pauses and remembers state, return exits completely
2. **Memory efficient**: Generate values on-demand, not all at once
3. **One-time use**: Generators are exhausted after iteration
4. **Generator expressions**: Use () instead of [] for memory efficiency
5. **Perfect for**: Large files, infinite sequences, data pipelines

**Common Mistakes**:
- Trying to iterate a generator twice without recreating it
- Using return in a generator (ends the generator immediately)
- Forgetting that generators are lazy — nothing happens until you iterate

**Real-World Use Cases**:
- Reading large files line by line
- Processing database queries with millions of rows
- Streaming data from APIs
- Creating infinite sequences (counters, Fibonacci, etc.)
- Building data processing pipelines

**Closing**: "Generators are one of Python's most powerful features! Use them whenever you're working with large datasets or don't need all values at once. Your programs will be faster and more memory-efficient!"
