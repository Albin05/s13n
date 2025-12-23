# Pre-Read: Writing For Loops to Iterate Over Sequences

## What You'll Learn
In this lesson, you'll learn how to use for loops to iterate over sequences like lists, strings, and other collections. For loops make it easy to process each item in a collection automatically.

## Why This Matters
For loops are one of the most commonly used features in Python:
- Process every student in a class list
- Check every character in a password
- Calculate the total of all prices in a shopping cart
- Display every item in a menu

For loops eliminate the need to manually access each element by index.

---

## What is a For Loop?

A **for loop** automatically iterates over each item in a sequence (list, string, range, etc.) and runs code for each item.

```python
for item in sequence:
    # Do something with item
```

**Key differences from while loops:**
- **While loop**: "Keep going while condition is True" (you control when it stops)
- **For loop**: "Go through each item in this sequence" (automatic iteration)

---

## Simple Examples

### Example 1: Iterate Over a List

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

**Output:**
```
apple
banana
cherry
```

**What happens:**
1. Take first item ("apple") and run the code
2. Take second item ("banana") and run the code
3. Take third item ("cherry") and run the code
4. No more items → stop

### Example 2: Iterate Over a String

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

---

## For Loops vs While Loops

### Using While (More Code)

```python
fruits = ["apple", "banana", "cherry"]
index = 0

while index < len(fruits):
    print(fruits[index])
    index += 1
```

### Using For (Cleaner)

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

**For loops are better when:**
- You need to process every item in a sequence
- You don't need the index
- You want cleaner, more readable code

---

## Real-World Examples

### Example 1: Calculate Total Price

```python
prices = [19.99, 5.50, 12.00, 8.75]
total = 0

for price in prices:
    total += price

print(f"Total: ${total}")  # Total: $46.24
```

### Example 2: Count Vowels in a String

```python
text = "Hello World"
vowel_count = 0

for char in text:
    if char.lower() in "aeiou":
        vowel_count += 1

print(f"Vowels: {vowel_count}")  # Vowels: 3
```

### Example 3: Print Numbered List

```python
students = ["Alice", "Bob", "Charlie"]

for student in students:
    print(f"Student: {student}")
```

---

## Try It Yourself (Before Class)

Run this code:

```python
numbers = [10, 20, 30, 40, 50]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print(doubled)
```

**Questions:**
1. What does this code do?
2. What will be in the `doubled` list?
3. Try changing `num * 2` to `num + 5` - what happens?

---

## Key Takeaways

Before class, remember:
1. **For loops iterate sequences** - automatically go through each item
2. **Cleaner than while** - for sequences you know the length of
3. **Works with many types** - lists, strings, ranges, tuples, etc.
4. **Loop variable** - gets each item automatically
5. **No index needed** - unless you specifically want it

## What's Next?

In the live session, we'll:
- Practice iterating over different data types
- Learn to use the range() function with for loops
- Understand when to use for vs while loops
- Combine for loops with break and continue

See you in class!
