# Pre-Read: Define Variables

## What You'll Learn
In this lesson, you'll learn what variables are and how to create them in Python. Variables are the foundation of all programming!

## Why This Matters
Imagine you're building a calculator app. You need to remember:
- The first number the user enters
- The second number
- The operation they want to perform
- The result

Without variables, the computer has no way to remember these values. Variables are like labeled containers that store information your program needs.

---

## What is a Variable?

Think of a variable as a **labeled box** in the computer's memory. You give it a name (the label) and put data inside it (the contents).

```python
score = 100
```

This creates a box labeled `score` and puts the number `100` inside it.

### A Brief History: Why Variables Matter

In the early days of computing (1940s), programmers had to write numbers directly into machine code. If you wanted to change a value, you'd have to rewrite the entire program!

Variables revolutionized programming by introducing **symbolic names** for data. Now we can write `total = price * quantity` and the computer figures out the actual numbers. This was a game-changer - it made programs:
- **Reusable** - same code works with different data
- **Readable** - `age` is clearer than remembering "memory location 1047"
- **Flexible** - values can change while the program runs

### Another Way to Think About Variables

Consider a spreadsheet cell:
- Cell **A1** is like a variable name
- The **value in A1** is like the variable's value
- You can reference **A1** in formulas, and if A1 changes, all formulas update automatically

Variables work the same way in Python!

## Creating Variables in Python

Creating a variable in Python is simple - just use the equals sign `=`:

```python
age = 25
name = "Alice"
price = 19.99
is_active = True
```

**Important**: The `=` sign means "assign," not "equals" like in math!

### How to Read This Code

```python
age = 25
```

Read this as: **"age is assigned 25"** or **"assign 25 to age"**

Don't read it as "age equals 25" - that's mathematical equality, not assignment.

---

## Variables Can Change

Unlike in mathematics, variables in programming can be reassigned to different values:

```python
score = 100
print(score)  # Shows: 100

score = 150   # Change the value
print(score)  # Shows: 150
```

The variable `score` now contains `150` instead of `100`. The old value is gone.

---

## Real-World Example

```python
# Storing game information
player_name = "DragonMaster"
health = 100
level = 5

print(player_name)  # DragonMaster
print(health)       # 100
print(level)        # 5

# Player takes damage
health = 75
print(health)       # 75
```

---

## Try It Yourself (Before Class)

Run this code and see what happens:

```python
# Create variables
my_name = "YourNameHere"
my_age = 20
my_score = 95

# Print them
print(my_name)
print(my_age)
print(my_score)

# Change a variable
my_score = 100
print(my_score)  # What will this show?
```

**Expected Output:**
```
YourNameHere
20
95
100
```

---

## Key Takeaways

Before class, remember:
1. **Variables store data** - like labeled containers
2. **Use `=` to create variables** - `name = value`
3. **Variables can be reassigned** - they can change value
4. **The `=` means "assign"** - not mathematical equality

## Questions to Think About

Come to class ready to discuss:
- Why would we want to change a variable's value?
- What happens to the old value when we reassign a variable?
- Can you think of examples from apps you use that would need variables?

## What's Next?

In the live session, we'll:
- Practice creating many different variables
- Learn the rules for naming variables
- Understand how variables work in memory
- Build programs that use variables effectively

See you in class!
