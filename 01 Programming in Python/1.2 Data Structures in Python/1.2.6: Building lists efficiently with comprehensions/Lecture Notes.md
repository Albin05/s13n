# Lecture Notes: Building Lists Efficiently with Comprehensions

## Building Lists Efficiently with Comprehensions

Transform your Python code with elegant, concise list comprehensions - the Pythonic way to build lists.

---

<div align="center">

![Abstract flowing patterns](https://images.unsplash.com/photo-1557672172-298e090bd0f1?w=800&q=80)

*List comprehensions: elegant, efficient, and expressive*

</div>

---

### Key Concepts

1. **List Comprehension Syntax**: Concise list creation in one line
2. **Filtering**: Adding conditions to select items
3. **Transformation**: Applying expressions to modify items
4. **Conditional Expressions**: Using if-else within comprehensions
5. **Nested Comprehensions**: Working with 2D data
6. **Best Practices**: When to use comprehensions vs loops

## Basic Syntax

```python
# Basic comprehension
new_list = [expression for item in iterable]

# With filtering
new_list = [expression for item in iterable if condition]

# With if-else
new_list = [expr_if if condition else expr_else for item in iterable]

# Nested
new_list = [expression for item1 in iterable1 for item2 in iterable2]
```

---

## Examples

### Example 1: Basic List Comprehension

**Traditional loop:**
```python
squares = []
for num in range(1, 6):
    squares.append(num ** 2)
print(squares)  # [1, 4, 9, 16, 25]
```

**List comprehension:**
```python
squares = [num ** 2 for num in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

**Benefits:**
- More concise (1 line vs 3 lines)
- More readable once you understand the syntax
- Faster execution
- More Pythonic

### Example 2: Filtering with Conditions

```python
# Get even numbers from 1-20
evens = [num for num in range(1, 21) if num % 2 == 0]
print(evens)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Filter words longer than 5 characters
words = ["apple", "pie", "banana", "cat", "strawberry", "dog"]
long_words = [word for word in words if len(word) > 5]
print(long_words)
# ['banana', 'strawberry']

# Get positive numbers only
numbers = [-5, 3, -2, 8, -1, 10, -7, 4]
positives = [num for num in numbers if num > 0]
print(positives)
# [3, 8, 10, 4]
```

### Example 3: Transform and Filter Together

```python
# Square only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [num ** 2 for num in numbers if num % 2 == 0]
print(even_squares)
# [4, 16, 36, 64, 100]

# Uppercase names starting with 'A'
names = ["Alice", "Bob", "Andrew", "Charlie", "Anna", "David"]
a_names_upper = [name.upper() for name in names if name.startswith('A')]
print(a_names_upper)
# ['ALICE', 'ANDREW', 'ANNA']
```

### Example 4: Using if-else (Conditional Expression)

```python
# Label numbers as even or odd
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
labels = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(labels)
# ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']

# Classify scores as Pass or Fail
scores = [45, 78, 92, 65, 88, 53, 71]
results = ["Pass" if score >= 70 else "Fail" for score in scores]
print(results)
# ['Fail', 'Pass', 'Pass', 'Fail', 'Pass', 'Fail', 'Pass']
```

---

## Common Patterns

### Pattern 1: Map (Transform Each Element)

```python
# Convert to uppercase
words = ["hello", "world", "python"]
upper = [word.upper() for word in words]

# Calculate lengths
lengths = [len(word) for word in words]
```

### Pattern 2: Filter (Select Elements)

```python
# Get even numbers
evens = [n for n in range(20) if n % 2 == 0]

# Get strings longer than 5 chars
long = [s for s in strings if len(s) > 5]
```

### Pattern 3: Map and Filter Combined

```python
# Square even numbers
even_squares = [n**2 for n in range(10) if n % 2 == 0]

# Uppercase long words
long_upper = [w.upper() for w in words if len(w) > 5]
```

---

## Best Practices

1. **Keep It Simple**
   ```python
   # Good - clear and readable
   squares = [x ** 2 for x in range(10)]

   # Bad - too complex
   result = [x**2 if x%2==0 else x**3 if x%3==0 else x for x in range(20) if x>5]
   ```

2. **Use Meaningful Variable Names**
   ```python
   # Good
   adult_names = [person.name for person in people if person.age >= 18]

   # Avoid
   result = [p.n for p in people if p.a >= 18]
   ```

3. **Don't Nest Too Deeply**
   ```python
   # Good - flat comprehension
   flat = [num for row in matrix for num in row]

   # Avoid - too complex
   result = [[x*y for x in row1] for row1 in [[a+b for a in r] for r in matrix]]
   ```

---

## Common Mistakes

1. **Forgetting Brackets**
   ```python
   # Wrong - generator, not list
   squares = (x ** 2 for x in range(10))

   # Correct - list comprehension
   squares = [x ** 2 for x in range(10)]
   ```

2. **Wrong if-else Placement**
   ```python
   # Wrong - syntax error
   result = [x for x in range(10) if x % 2 == 0 else x * 2]

   # Correct - if-else before for
   result = [x if x % 2 == 0 else x * 2 for x in range(10)]
   ```

3. **Using When Loop Is Better**
   ```python
   # Don't use comprehension for side effects
   # Bad:
   [print(x) for x in numbers]  # Creates unnecessary list

   # Good:
   for x in numbers:
       print(x)
   ```

---

## Key Takeaways

1. **List comprehensions** create lists concisely in one line
2. **Syntax**: `[expression for item in iterable]`
3. **Add filtering** with `if` at the end
4. **Use if-else** before `for` for conditional expressions
5. **More Pythonic** and often faster than loops
6. **Keep simple** - use loops for complex logic
7. **Creates new list** - doesn't modify original
8. **Readability first** - if it's hard to read, use a loop
