# Lecture Script: LO-2.6 Building Lists Efficiently with Comprehensions

## [0:00-0:03] Hook (3 min)

"Remember last class when we wrote this code to square numbers?"

```python
squares = []
for num in range(1, 6):
    squares.append(num ** 2)
```

"What if I told you Python has a way to do this in ONE line, that's faster, more readable, and more Pythonic?"

```python
squares = [num ** 2 for num in range(1, 6)]
```

"Today we're learning list comprehensions - one of Python's most powerful and beloved features. By the end of class, you'll write code that makes other programmers say 'wow, that's elegant!'"

---

## [0:03-0:10] Main Concept 1: Basic List Comprehensions (7 min)

### The Syntax (2 min)

"Here's the basic structure:"

```python
new_list = [expression for item in iterable]
```

**Live coding:**
```python
# Traditional way
numbers = []
for x in range(1, 6):
    numbers.append(x)
print(numbers)  # [1, 2, 3, 4, 5]

# List comprehension way
numbers = [x for x in range(1, 6)]
print(numbers)  # [1, 2, 3, 4, 5]
```

"Read it like English: 'Create a list of x for each x in range 1-5'"

### Transformation (3 min)

"The power comes from the expression part - you can transform each item:"

```python
# Double each number
doubled = [x * 2 for x in range(1, 6)]
print(doubled)  # [2, 4, 6, 8, 10]

# Square each number
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Get first letter of names
names = ["Alice", "Bob", "Charlie"]
initials = [name[0] for name in names]
print(initials)  # ['A', 'B', 'C']
```

### Practice Together (2 min)

"Your turn! How would you create a list of cubes?"

```python
# Solution
cubes = [x ** 3 for x in range(1, 6)]
print(cubes)  # [1, 8, 27, 64, 125]
```

---

## [0:10-0:18] Main Concept 2: Filtering with Conditions (8 min)

### Adding if Conditions (3 min)

"What if you only want SOME items? Add an if condition at the end:"

```python
new_list = [expression for item in iterable if condition]
```

**Live coding:**
```python
# Get only even numbers
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Get only long words
words = ["apple", "pie", "banana", "cat"]
long_words = [word for word in words if len(word) > 3]
print(long_words)  # ['apple', 'banana']
```

### Transform AND Filter (3 min)

"The real magic: transform AND filter together!"

```python
# Square only the even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print(even_squares)  # [4, 16, 36]

# Uppercase names starting with 'A'
names = ["Alice", "Bob", "Andrew", "Charlie"]
a_names = [name.upper() for name in names if name.startswith('A')]
print(a_names)  # ['ALICE', 'ANDREW']
```

### Practice (2 min)

"Create a list of numbers from 1-20 that are divisible by 3:"

```python
# Solution
threes = [x for x in range(1, 21) if x % 3 == 0]
print(threes)  # [3, 6, 9, 12, 15, 18]
```

---

## [0:18-0:25] Main Concept 3: Conditional Expressions (if-else) (7 min)

### The if-else Syntax (3 min)

"What if you need BOTH branches? The syntax changes - if-else comes BEFORE for:"

```python
new_list = [expr_if_true if condition else expr_if_false for item in iterable]
```

**Important:** Show the difference on the board:
```
Filtering (no else):  [expr for x in list if condition]
If-else (both ways):  [expr_if if cond else expr_else for x in list]
```

**Live coding:**
```python
# Label numbers as even or odd
numbers = [1, 2, 3, 4, 5]
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']

# Pass or Fail
scores = [45, 78, 92, 65, 88]
results = ["Pass" if s >= 70 else "Fail" for s in scores]
print(results)  # ['Fail', 'Pass', 'Pass', 'Fail', 'Pass']
```

### Real-World Example (2 min)

```python
# Apply discount to expensive items
prices = [100, 50, 200, 75, 300]
final_prices = [p * 0.9 if p > 100 else p for p in prices]
print(final_prices)  # [100, 50, 180.0, 75, 270.0]
```

### Practice (2 min)

"Cap all values at 100:"

```python
values = [45, 120, 80, 150, 95]
# Solution
capped = [v if v <= 100 else 100 for v in values]
print(capped)  # [45, 100, 80, 100, 95]
```

---

## [0:25-0:28] When to Use Comprehensions vs Loops (3 min)

### The Golden Rule

"Use comprehensions when your code stays SIMPLE and READABLE."

**Good uses:**
```python
# Simple and clear
squares = [x ** 2 for x in range(10)]
evens = [x for x in numbers if x % 2 == 0]
```

**Bad uses - use loops instead:**
```python
# Too complex - hard to read!
result = [x**2 if x%2==0 else x**3 if x%3==0 else x for x in range(20) if x>5]

# Side effects - wrong tool!
[print(x) for x in numbers]  # Don't do this!

# Multiple operations - use loop
for item in items:
    processed = transform(item)
    validate(processed)
    results.append(processed)
```

---

## [0:28-0:30] Wrap-up & Practice (2 min)

### Quick Challenge

"Convert this loop to a comprehension:"

```python
# Traditional
result = []
for word in ["hello", "world", "python"]:
    if len(word) > 4:
        result.append(word.upper())

# Solution
result = [word.upper() for word in ["hello", "world", "python"] if len(word) > 4]
print(result)  # ['HELLO', 'WORLD', 'PYTHON']
```

### Key Takeaways

1. **Basic syntax**: `[expression for item in iterable]`
2. **With filtering**: `[expr for item in iterable if condition]`
3. **With if-else**: `[expr_if if cond else expr_else for item in iterable]`
4. **More concise and Pythonic** than loops
5. **Keep it simple** - if it's hard to read, use a loop!

---

## Key Points to Reinforce

- List comprehensions are ONE line
- Read like English: "list of X for each item in sequence"
- Filtering: if at the END
- If-else: BEFORE the for
- Faster than traditional loops
- Only use when it improves readability

## Student Questions to Anticipate

**Q: "When should I use comprehensions vs loops?"**
A: "If it fits on one readable line and is clear, use comprehensions. If it needs multiple statements or complex logic, use a loop."

**Q: "Why does if-else go before for but filtering if goes after?"**
A: "Filtering if at the end means 'only include if'. If-else before for means 'transform this way or that way for every item'."

**Q: "Are comprehensions always faster?"**
A: "Usually 20-30% faster for simple operations. But readability is more important than micro-optimization!"

## Transition to Next Topic

"Excellent! You now know one of Python's most powerful features. Next, we'll explore tuples - lists' immutable cousins. But first, practice these comprehensions - they'll make you a better Python programmer!"
