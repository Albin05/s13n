# Pre-Read: Using Function Parameters to Accept Inputs

## Why Parameters?

Imagine having a different calculator for every pair of numbers you want to add - one for "5+3", another for "10+20", etc. Ridiculous, right? **Parameters** solve this - one function, infinite uses!

### Simple Analogy

Think of parameters like **placeholders in a Mad Libs game**:
- **Template**: "Hello, [NAME]! You are [AGE] years old."
- **Parameters**: NAME and AGE are slots you fill in
- **Infinite variations**: Change the values, get different results
- **Same structure**, different data each time

Or like **a blender**:
- **Machine**: The function (same every time)
- **Ingredients**: Parameters (different each time)
- **Banana smoothie**: blend(banana, milk, ice)
- **Berry smoothie**: blend(berries, yogurt, ice)
- **One blender**, many recipes!

## What You'll Learn
In this lesson, you'll learn how to define functions that accept parameters (inputs), making your functions flexible and reusable for different data.

## Why This Matters
Functions without parameters can only do one specific thing. Parameters make functions powerful:
- A calculator function that works with any two numbers
- A greeting function that works with any name
- A discount function that works with any price
- A validation function that checks any password

Parameters turn functions from single-use tools into versatile, reusable building blocks.

---

## What are Function Parameters?

**Parameters** are variables listed in the function definition that accept values when the function is called.

```python
def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice")  # "Alice" is an argument
greet("Bob")    # "Bob" is an argument
```

**Key terms:**
- **Parameter**: Variable in function definition (`name`)
- **Argument**: Actual value passed when calling (`"Alice"`, `"Bob"`)

---

## Simple Example

```python
def add(a, b):  # a and b are parameters
    sum_result = a + b
    print(f"{a} + {b} = {sum_result}")

add(5, 3)   # 5 + 3 = 8
add(10, 20) # 10 + 20 = 30
add(7, 2)   # 7 + 2 = 9
```

**One function, many uses!** The same function works with different numbers.

---

## Multiple Parameters

You can have as many parameters as you need:

```python
def introduce(name, age, city):
    print(f"Hi, I'm {name}")
    print(f"I'm {age} years old")
    print(f"I live in {city}")

introduce("Alice", 25, "New York")
introduce("Bob", 30, "London")
```

**Order matters!** Arguments must match parameter order.

---

## Real-World Examples

### Example 1: Calculate Area

```python
def rectangle_area(length, width):
    area = length * width
    print(f"Area: {area} square units")

rectangle_area(5, 3)   # Area: 15 square units
rectangle_area(10, 8)  # Area: 80 square units
```

### Example 2: Check Password Strength

```python
def check_password(password, min_length):
    if len(password) >= min_length:
        print("Password is strong enough")
    else:
        print(f"Password too short. Need {min_length} characters")

check_password("abc", 8)        # Too short
check_password("secure123", 8)  # Strong enough
```

---

## Parameters Make Functions Flexible

### Without Parameters (Limited)

```python
def greet_alice():
    print("Hello, Alice!")

greet_alice()  # Only works for Alice!
```

### With Parameters (Flexible)

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")   # Hello, Alice!
greet("Bob")     # Hello, Bob!
greet("Charlie") # Hello, Charlie!
```

---

## Try It Yourself (Before Class)

Write and run this function:

```python
def multiply(x, y):
    result = x * y
    print(f"{x} × {y} = {result}")

multiply(4, 5)
multiply(10, 3)
multiply(7, 7)
```

**Questions:**
1. What does each call print?
2. Try adding a third parameter `z` - what changes?
3. What happens if you call `multiply(5)` (only one argument)?

---

## Key Takeaways

Before class, remember:
1. **Parameters = inputs** - make functions flexible
2. **Defined in ()** - after function name
3. **Order matters** - arguments match parameter positions
4. **Multiple parameters** - separate with commas
5. **Reusability** - one function, many uses

## What's Next?

In the live session, we'll:
- Write functions with various parameter counts
- Learn about return values (sending data back)
- Explore default parameters
- Understand parameter vs argument terminology

See you in class!
