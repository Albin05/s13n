# Lecture Script: LO-2.5 Iterating Through Lists Using Loops

## [0:00-0:03] Hook (3 min)

"Imagine you're a teacher with 100 students, and you need to calculate the class average. Would you manually add each score one by one? Of course not! You'd use a loop to process all the scores automatically."

**Live Demo - The Problem:**
```python
# Without loops - tedious and doesn't scale!
score1 = 85
score2 = 92
score3 = 78
total = score1 + score2 + score3
# Now imagine doing this for 100 students...
```

**With loops - elegant solution:**
```python
scores = [85, 92, 78, 95, 88, 76, 90, 84]
total = 0
for score in scores:
    total += score
average = total / len(scores)
print(f"Class average: {average:.2f}")
```

"Today, we're learning list iteration - one of the most essential skills in programming. You'll use this every single day as a developer."

---

## [0:03-0:12] Main Concept 1: Basic for Loop (9 min)

### The for Loop Syntax (2 min)

"The for loop is Python's primary way to process lists. Here's the syntax:"

```python
for item in list_name:
    # Do something with item
```

**Live Coding:**
```python
fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    print(f"I like {fruit}")
# Output:
# I like apple
# I like banana
# I like cherry
# I like date
```

"Notice: Python automatically goes through each item, one by one. The variable `fruit` takes on each value in the list."

### How It Works (2 min)

**Draw on board/screen:**
```
fruits = ["apple", "banana", "cherry", "date"]
         ↑
for fruit in fruits:
    print(fruit)

Step 1: fruit = "apple"  → print "apple"
Step 2: fruit = "banana" → print "banana"
Step 3: fruit = "cherry" → print "cherry"
Step 4: fruit = "date"   → print "date"
Step 5: No more items → loop ends
```

### Practical Example: Calculate Sum (3 min)

```python
numbers = [10, 20, 30, 40, 50]

# Pattern: Start with accumulator at 0
total = 0

for num in numbers:
    total += num  # Add each number to total
    print(f"Current total: {total}")

print(f"Final sum: {total}")
```

**Key point:** "Always initialize your accumulator BEFORE the loop!"

### Practice Together (2 min)

"Let's find the maximum score:"
```python
scores = [78, 92, 85, 95, 88]
highest = scores[0]  # Start with first score

for score in scores:
    if score > highest:
        highest = score

print(f"Highest score: {highest}")  # 95
```

---

## [0:12-0:20] Main Concept 2: enumerate(), range(), and zip() (8 min)

### Using enumerate() (3 min)

"Sometimes you need both the index AND the value. That's where enumerate() comes in:"

```python
tasks = ["Buy groceries", "Finish homework", "Call dentist"]

# With enumerate - get index and value
for i, task in enumerate(tasks):
    print(f"{i}: {task}")
# Output:
# 0: Buy groceries
# 1: Finish homework
# 2: Call dentist
```

"Want to start counting from 1 instead of 0?"
```python
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")
# Output:
# 1. Buy groceries
# 2. Finish homework
# 3. Call dentist
```

### Using range() for Indices (2 min)

"When you need to modify list items, use range():"

```python
prices = [10.00, 20.00, 15.00, 30.00]
print("Original:", prices)

# Apply 10% discount
for i in range(len(prices)):
    prices[i] = prices[i] * 0.9

print("After discount:", prices)
```

**Important:** "We use range(len(list)) when we need to change the actual list items."

### Using zip() for Multiple Lists (3 min)

"What if you have related data in separate lists? Use zip():"

```python
students = ["Alice", "Bob", "Charlie"]
math_scores = [85, 92, 78]
english_scores = [88, 84, 90]

print("Student Report Cards:")
for student, math, english in zip(students, math_scores, english_scores):
    average = (math + english) / 2
    print(f"{student}: Math={math}, English={english}, Avg={average:.1f}")
```

**Output:**
```
Student Report Cards:
Alice: Math=85, English=88, Avg=86.5
Bob: Math=92, English=84, Avg=88.0
Charlie: Math=78, English=90, Avg=84.0
```

---

## [0:20-0:25] Main Concept 3: Common Patterns & Loop Control (5 min)

### Pattern 1: Filtering (2 min)

"Build a new list with only items that match a condition:"

```python
ages = [15, 22, 17, 30, 19, 14, 25, 18]
adults = []

for age in ages:
    if age >= 18:
        adults.append(age)

print(f"Adults: {adults}")  # [22, 30, 19, 25, 18]
```

### Pattern 2: Transformation (1 min)

"Convert each item to a new form:"

```python
names = ["alice", "bob", "charlie"]
capitalized = []

for name in names:
    capitalized.append(name.capitalize())

print(capitalized)  # ['Alice', 'Bob', 'Charlie']
```

### break and continue (2 min)

**break - Exit early:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Find first number > 5
for num in numbers:
    if num > 5:
        print(f"Found: {num}")
        break  # Stop searching!
# Output: Found: 6
```

**continue - Skip to next:**
```python
# Print only odd numbers
for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)
# Output: 1, 3, 5, 7, 9
```

---

## [0:25-0:28] Common Mistakes (3 min)

### Mistake 1: Modifying List While Iterating

"This is dangerous and can cause bugs:"
```python
# WRONG - Don't do this!
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    numbers.remove(num)  # Bad!
```

"Instead, create a new list:"
```python
# CORRECT
numbers = [1, 2, 3, 4, 5]
filtered = []
for num in numbers:
    if num % 2 != 0:  # Keep odd numbers
        filtered.append(num)
```

### Mistake 2: Forgetting to Initialize

```python
# WRONG
for num in numbers:
    total += num  # Error! total doesn't exist

# CORRECT
total = 0  # Initialize first!
for num in numbers:
    total += num
```

---

## [0:28-0:30] Practice Exercise & Wrap-up (2 min)

### Quick Exercise

"Here's a challenge: Calculate the average temperature and find the hottest day:"

```python
temperatures = [72, 75, 68, 70, 73, 69, 71]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Your turn! Calculate:
# 1. Average temperature
# 2. Find hottest day

# Solution (reveal after students try):
total = sum(temperatures)
average = total / len(temperatures)

hottest_temp = temperatures[0]
hottest_day = days[0]

for i in range(len(temperatures)):
    if temperatures[i] > hottest_temp:
        hottest_temp = temperatures[i]
        hottest_day = days[i]

print(f"Average: {average:.1f}°F")
print(f"Hottest: {hottest_day} ({hottest_temp}°F)")
```

---

## Key Points to Reinforce

1. **for loop is the primary iteration tool** - `for item in list:`
2. **enumerate()** when you need index + value
3. **range(len(list))** when modifying elements
4. **zip()** for parallel lists
5. **Always initialize accumulators** before loops
6. **Never modify list structure** while iterating
7. **break** exits early, **continue** skips iteration
8. **Common patterns**: accumulation, filtering, transformation, search

## Student Questions to Anticipate

**Q: "When should I use enumerate vs range?"**
A: "Use enumerate when you need both index and value. Use range when you only need indices or are modifying the list."

**Q: "Why can't I modify the list while iterating?"**
A: "Because Python is iterating through the list by position. If you remove items, the positions change, causing unpredictable behavior."

**Q: "Is there a faster way than loops?"**
A: "Yes! List comprehensions, which we'll learn next. But understanding loops is essential first."

## Transition to Next Topic

"Excellent work! You now know how to process lists with loops. Next, we'll learn list comprehensions - a more elegant way to create lists in a single line. But everything you learned today is the foundation!"
