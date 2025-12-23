# Lecture Script: Writing For Loops to Iterate Over Sequences

**Duration:** 25-30 minutes
**Learning Objective:** Students will be able to use for loops to iterate through sequences like lists, strings, and tuples.

---

## [0:00-0:02] Hook (2 minutes)

**Open with a relatable scenario:**

> "Imagine you're a teacher with a class roster of 30 students. You need to call attendance. Do you say 'Student number 1, Student number 2, Student number 3...'? No! You call each student BY NAME: 'Alice? Present. Bob? Present.' That's exactly what a FOR loop does - it goes through each item in a list, using the ACTUAL values, not index numbers!"

**Interactive question:**
"How many of you have scrolled through your phone contacts or a playlist? You don't think '1, 2, 3...' - you see the actual names or songs!"

**The connection:**
> "For loops are Python's way of saying 'for each item in this collection, do something.' It's more natural than counting positions!"

**Live demo - the magic:**
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

**Run both:**
```
apple
banana
orange
```

**Point out:**
> "Both print the same thing, but look how much CLEANER the for loop is! No index i, no len(), no incrementing. Just 'for each fruit in fruits, print it.' Beautiful!"

---

## [0:02-0:10] Main Concept: For Loop Basics (8 minutes)

### Part 1: Basic Syntax (3 minutes)

**Explain:**
> "For loops iterate through sequences AUTOMATICALLY. Python handles all the indexing behind the scenes!"

**Syntax:**
```python
for item in sequence:
    # Do something with item
    # item is a variable holding current element
```

**Live code - Lists:**
```python
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(f"Number: {num}")
```

**Output:**
```
Number: 10
Number: 20
Number: 30
Number: 40
Number: 50
```

**Trace through:**
1. First iteration: num = 10
2. Second iteration: num = 20
3. Third iteration: num = 30
4. Fourth iteration: num = 40
5. Fifth iteration: num = 50
6. No more items → loop ends

**Live code - Strings:**
```python
word = "Python"

for letter in word:
    print(letter)
```

**Output:**
```
P
y
t
h
o
n
```

**Emphasize:**
> "Strings ARE sequences! Each character is an item. For loop iterates one character at a time!"

### Part 2: Accumulator Pattern (2 minutes)

**Show common pattern:**
```python
numbers = [1, 2, 3, 4, 5]
total = 0  # Initialize accumulator

for num in numbers:
    total += num  # Add each number

print(f"Sum: {total}")  # 15
```

**Explain:**
> "Accumulator pattern: start with initial value (0), update it each iteration. By the end, total holds the sum of all numbers!"

**Another example:**
```python
fruits = ["apple", "banana", "orange"]
all_fruits = []  # Empty list accumulator

for fruit in fruits:
    all_fruits.append(fruit.upper())

print(all_fruits)  # ['APPLE', 'BANANA', 'ORANGE']
```

### Part 3: For vs While (3 minutes)

**Create comparison on board:**

| For Loop | While Loop |
|----------|------------|
| `for item in list:` | `while i < len(list):` |
| No manual index | Need index variable |
| Automatic iteration | Manual increment |
| Best for sequences | Best for conditions |

**Side-by-side demo:**
```python
# Task: Print each item and double it

# WHILE loop way
fruits = ["apple", "banana", "orange"]
i = 0
while i < len(fruits):
    print(f"{fruits[i]}: {len(fruits[i]) * 2}")
    i += 1

# FOR loop way (cleaner!)
for fruit in fruits:
    print(f"{fruit}: {len(fruit) * 2}")
```

**Explain:**
> "Same result, but for loop is MUCH cleaner. No i, no len(), no i += 1. Just focus on WHAT you want to do with each item!"

---

## [0:10-0:18] Advanced: Enumerate and Zip (8 minutes)

### Part 1: Enumerate (when you need index) (4 minutes)

**The problem:**
> "Sometimes you DO need the index. Not often, but sometimes. Python has a solution: `enumerate()`!"

**Live code:**
```python
colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(f"Position {index}: {color}")
```

**Output:**
```
Position 0: red
Position 1: green
Position 2: blue
```

**Explain how it works:**
```python
# enumerate() returns pairs (tuples)
# (0, "red")
# (1, "green")
# (2, "blue")

# For loop UNPACKS each pair
for index, color in enumerate(colors):
    # index = 0, color = "red" (first iteration)
    # index = 1, color = "green" (second iteration)
    # etc.
```

**Custom start index:**
```python
for index, color in enumerate(colors, start=1):
    print(f"Color {index}: {color}")
```

**Output:**
```
Color 1: red
Color 2: green
Color 3: blue
```

### Part 2: Zip (parallel iteration) (4 minutes)

**The problem:**
> "What if you have TWO lists and want to iterate them together? Meet `zip()`!"

**Live code:**
```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

**Output:**
```
Alice is 25 years old
Bob is 30 years old
Charlie is 35 years old
```

**Explain how it works:**
```python
# zip() creates pairs from two lists
# ("Alice", 25)
# ("Bob", 30)
# ("Charlie", 35)

# For loop unpacks each pair
```

**Multiple lists:**
```python
names = ["Alice", "Bob"]
ages = [25, 30]
cities = ["NYC", "LA"]

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, from {city}")
```

**Output:**
```
Alice, 25, from NYC
Bob, 30, from LA
```

**Important note:**
> "Zip stops at the SHORTEST list! If lists have different lengths, extra items are ignored."

---

## [0:18-0:24] Dictionary Iteration (6 minutes)

### Part 1: Keys, Values, Items (3 minutes)

**Show dictionary:**
```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
```

**Iterate keys only:**
```python
for key in student.keys():  # or just: for key in student:
    print(key)
```

**Output:**
```
name
age
grade
```

**Iterate values only:**
```python
for value in student.values():
    print(value)
```

**Output:**
```
Alice
20
A
```

**Iterate key-value pairs (most common):**
```python
for key, value in student.items():
    print(f"{key}: {value}")
```

**Output:**
```
name: Alice
age: 20
grade: A
```

**Emphasize:**
> ".items() is the most useful! Gives you BOTH key and value. Perfect for displaying dictionaries!"

### Part 2: Nested Iteration (3 minutes)

**Nested lists:**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for num in row:
        print(num, end=" ")
    print()  # New line after each row
```

**Output:**
```
1 2 3
4 5 6
7 8 9
```

**Explain:**
> "Outer loop: each row. Inner loop: each number in that row. Nested for loops for 2D data!"

---

## [0:24-0:28] Practice Time (4 minutes)

**Exercise 1: Sum Numbers (1.5 minutes)**
> "Calculate the sum of all numbers in this list."

```python
# Given
numbers = [5, 10, 15, 20, 25]

# Solution
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")  # 75
```

**Exercise 2: Print with Position (2 minutes)**
> "Print each fruit with its position number (starting from 1)."

```python
# Given
fruits = ["apple", "banana", "orange"]

# Solution
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

**Output:**
```
1. apple
2. banana
3. orange
```

**Walk around and check:**
- Students trying to use index manually
- Forgetting colon after for statement
- Not understanding enumerate unpacking

---

## [0:28-0:30] Wrap-up and Key Takeaways (2 minutes)

**Summarize the main points:**

1. **For loops iterate sequences**: Lists, strings, tuples
2. **No manual indexing**: Python handles it automatically
3. **Syntax**: `for item in sequence:`
4. **Enumerate**: When you need index and value
5. **Zip**: Iterate multiple sequences together
6. **Dictionary methods**: `.items()`, `.keys()`, `.values()`
7. **Break and continue**: Work in for loops too
8. **Cleaner than while**: For known sequences

**Visual on board:**
```python
# Basic pattern
for item in collection:
    do_something(item)

# With index
for index, item in enumerate(collection):
    print(f"{index}: {item}")

# Multiple lists
for a, b in zip(list1, list2):
    combine(a, b)

# Dictionary
for key, value in dict.items():
    process(key, value)
```

**Common use cases:**
- ✅ Process every item in a list
- ✅ Iterate through characters in a string
- ✅ Calculate sums, products, averages
- ✅ Build new lists from existing ones
- ✅ Display dictionary contents
- ✅ Nested data structures

**Common mistakes:**
- ❌ Trying to use i as index when not using enumerate
- ❌ Modifying list while iterating (causes issues)
- ❌ Forgetting colon after for statement
- ❌ Wrong indentation for loop body
- ❌ Using while when for is cleaner

**Real-world reminder:**
> "For loops are EVERYWHERE in real code. Processing files, handling user input, analyzing data - all use for loops. Master this and you've mastered iteration!"

**Preview next lesson:**
> "Next: the `range()` function! Generate number sequences for for loops. Count, create lists of numbers, and more!"

**Final check question:**
"When should you use a for loop instead of a while loop?"

**Expected answer:** "When you have a sequence (list, string, etc.) and want to process each item. For is cleaner - no manual indexing or incrementing needed!"

---

## Teaching Tips

1. **Emphasize cleanliness** - For loops are more readable
2. **Contrast with while** - Show both to appreciate for
3. **Use real data** - Names, colors, real examples
4. **Demonstrate enumerate** - Students love this
5. **Practice unpacking** - Tuples, zip, enumerate
6. **Avoid index when possible** - More Pythonic

## Common Student Questions

**Q: "Can I modify the list while looping?"**
A: "Dangerous! Can cause skipped items or errors. Create a new list or use list comprehension instead."

**Q: "What if I need the index?"**
A: "Use enumerate()! Gives you both index and value cleanly."

**Q: "Does for work with dictionaries?"**
A: "Yes! Use .items() for key-value pairs, .keys() for keys, .values() for values."

**Q: "Can I use break and continue?"**
A: "Absolutely! They work exactly the same in for loops as in while loops."

**Q: "What's the difference between `for i in list` and `for i in range(len(list))`?"**
A: "First gives you actual items, second gives you indices. First is more Pythonic - use it unless you specifically need indices!"

---

## Additional Examples (if time permits)

### Count Vowels
```python
text = "hello world"
count = 0
for char in text:
    if char in "aeiou":
        count += 1
print(f"Vowels: {count}")  # 3
```

### Build Uppercase List
```python
words = ["hello", "world"]
uppercase = []
for word in words:
    uppercase.append(word.upper())
print(uppercase)  # ['HELLO', 'WORLD']
```

### Reversed Iteration
```python
numbers = [1, 2, 3, 4, 5]
for num in reversed(numbers):
    print(num)  # Prints 5, 4, 3, 2, 1
```
