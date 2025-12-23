# Lecture Script: Using Function Parameters to Accept Inputs

**Duration:** 20-25 minutes
**Learning Objective:** Students will be able to define and use function parameters to create flexible, reusable functions that work with different input values.

---

## Hook (2 minutes)

"Yesterday, we learned how to create functions - reusable blocks of code. But there was one limitation: every time we called our function, it did EXACTLY the same thing.

Imagine if your phone's calculator app worked like that. You open it, and it only calculates 5 + 3. Every single time. Want to add 10 + 20? Too bad! You'd need a different calculator for that.

Sounds ridiculous, right? That's because real calculators accept INPUTS - they work with whatever numbers YOU give them.

Today, we're going to make our functions work the same way! We'll learn about PARAMETERS - the mechanism that lets functions accept different inputs and produce different results. By the end of this lesson, you'll transform your functions from rigid, one-use tools into flexible, powerful building blocks that can handle ANY data you throw at them!"

---

## Section 1: The Problem - Functions Without Parameters (3 minutes)

### The Limitation

"Let's start by seeing WHY we need parameters. Here's a function from our last lesson:"

```python
def greet_alice():
    print("Hello, Alice!")

greet_alice()  # Hello, Alice!
```

**Ask class:** "What if I want to greet Bob? Charlie? Anyone else?"

**Students might suggest:** "Write another function!"

```python
def greet_alice():
    print("Hello, Alice!")

def greet_bob():
    print("Hello, Bob!")

def greet_charlie():
    print("Hello, Charlie!")
```

**Point out the problem:**
"Now we have THREE functions that do almost the same thing! This is:
- Repetitive code
- Hard to maintain (change the greeting format? Update 3 places!)
- Not scalable (what if you have 100 users?)

There MUST be a better way!"

### The Solution Preview

```python
def greet(name):  # ONE function with a parameter!
    print(f"Hello, {name}!")

greet("Alice")    # Hello, Alice!
greet("Bob")      # Hello, Bob!
greet("Charlie")  # Hello, Charlie!
```

"ONE function, unlimited names! That's the power of parameters!"

---

## Section 2: What Are Parameters? (4 minutes)

### Definition

"A **parameter** is a variable in the function definition that acts as a placeholder for data that will be provided later."

### Syntax

```python
def function_name(parameter):
    # Use parameter in function body
    print(parameter)
```

**Break it down:**
1. **Parameter goes inside parentheses** after function name
2. **It's just a variable name** - follows same naming rules
3. **It doesn't have a value yet** - it's waiting for one
4. **Used throughout the function body** like any variable

### Live Coding - Simple Parameter Example

```python
def greet(name):
    print(f"Hello, {name}!")
    print(f"Welcome to Python, {name}!")

# Call it with different values
greet("Sarah")
greet("Mike")
```

**Output:**
```
Hello, Sarah!
Welcome to Python, Sarah!
Hello, Mike!
Welcome to Python, Mike!
```

**Explain:**
- `name` is the parameter (placeholder)
- When we call `greet("Sarah")`, `name` becomes "Sarah"
- When we call `greet("Mike")`, `name` becomes "Mike"
- Same function, different data!

---

## Section 3: Parameters vs Arguments (3 minutes)

### Important Terminology

"You'll hear two terms that seem similar but mean different things:"

```python
def greet(name):  # 'name' is a PARAMETER
    print(f"Hello, {name}")

greet("Alice")  # "Alice" is an ARGUMENT
```

**PARAMETER:**
- Variable in the function **definition**
- **Placeholder** waiting for a value
- Defined once when writing the function
- Think: "P for Placeholder"

**ARGUMENT:**
- **Actual value** passed when **calling** the function
- The real data that goes into the parameter
- Can be different each time you call
- Think: "A for Actual value"

### Memory Aid

"**Parameters** WAIT at the function definition
**Arguments** ARRIVE when you call the function"

### Example to Reinforce

```python
def add(x, y):  # x and y are PARAMETERS
    sum_result = x + y
    print(f"{x} + {y} = {sum_result}")

add(5, 3)   # 5 and 3 are ARGUMENTS
add(10, 20) # 10 and 20 are ARGUMENTS
```

---

## Section 4: Multiple Parameters (4 minutes)

### Syntax for Multiple Parameters

"Functions can accept multiple parameters - just separate them with commas!"

```python
def function_name(param1, param2, param3):
    # Use all parameters
    pass
```

### Example 1: Two Parameters

```python
def calculate_area(length, width):
    area = length * width
    print(f"Area: {area} square units")

calculate_area(5, 3)   # Area: 15 square units
calculate_area(10, 8)  # Area: 80 square units
```

**Explain:**
- Two parameters: `length` and `width`
- First argument (5) → `length`
- Second argument (3) → `width`
- Both used in calculation

### Example 2: Three Parameters

```python
def introduce_person(name, age, city):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print("---")

introduce_person("Alice", 25, "New York")
introduce_person("Bob", 30, "London")
```

**Output:**
```
Name: Alice
Age: 25
City: New York
---
Name: Bob
Age: 30
City: London
---
```

### Critical Concept: Order Matters!

```python
def subtract(a, b):
    print(f"{a} - {b} = {a - b}")

subtract(10, 3)  # 10 - 3 = 7
subtract(3, 10)  # 3 - 10 = -7
```

**Point out:**
"See how swapping the order changes the result? Arguments are matched to parameters BY POSITION:
- 1st argument → 1st parameter
- 2nd argument → 2nd parameter
- Order MATTERS!"

---

## Section 5: Parameters with Different Data Types (3 minutes)

### String Parameters

```python
def shout(message):
    print(message.upper() + "!")

shout("hello")      # HELLO!
shout("good job")   # GOOD JOB!
```

### Numeric Parameters

```python
def square(number):
    result = number * number
    print(f"{number}² = {result}")

square(5)   # 5² = 25
square(10)  # 10² = 100
```

### Mixed Types

"Parameters can be DIFFERENT types in the same function!"

```python
def repeat_message(text, count):
    # text is string, count is integer
    repeated = text * count
    print(repeated)

repeat_message("Hello", 3)  # HelloHelloHello
repeat_message("*", 10)     # **********
```

### Parameters in Conditionals

```python
def check_age(age):
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a minor")

check_age(20)  # You are an adult
check_age(15)  # You are a minor
```

**Emphasize:** "Parameters work with EVERYTHING - conditionals, loops, calculations, string operations - anything!"

---

## Section 6: Common Mistakes (3 minutes)

### Mistake 1: Wrong Number of Arguments

```python
def add(a, b):
    print(a + b)

# WRONG - Too few arguments
add(5)  # TypeError: missing 1 required positional argument: 'b'

# WRONG - Too many arguments
add(5, 3, 2)  # TypeError: add() takes 2 positional arguments but 3 were given

# RIGHT
add(5, 3)  # 8
```

**Key Point:** "You MUST provide exactly as many arguments as parameters (unless using defaults - next lesson)."

### Mistake 2: Wrong Order

```python
def greet_with_age(name, age):
    print(f"{name} is {age} years old")

# WRONG - Swapped order
greet_with_age(25, "Alice")  # 25 is Alice years old (nonsense!)

# RIGHT - Correct order
greet_with_age("Alice", 25)  # Alice is 25 years old
```

### Mistake 3: Using Parameter Before Defining

```python
# WRONG - Using 'name' without it being a parameter
def greet():
    print(f"Hello, {name}")  # NameError: name 'name' is not defined

greet("Alice")

# RIGHT - Define as parameter
def greet(name):
    print(f"Hello, {name}")

greet("Alice")  # Works!
```

### Mistake 4: Confusing Parameter Names

```python
def calculate_discount(price, discount_percent):
    # WRONG - Using 'amount' which doesn't exist
    final = amount - (amount * discount_percent / 100)  # NameError!

    # RIGHT - Use the actual parameter name
    final = price - (price * discount_percent / 100)
    print(f"Final price: ${final}")
```

---

## Section 7: Real-World Applications (3 minutes)

### Use Case 1: Form Validation

```python
def validate_username(username):
    if len(username) < 3:
        print("Username too short!")
    elif len(username) > 20:
        print("Username too long!")
    else:
        print("Username is valid!")

validate_username("ab")        # Username too short!
validate_username("john_doe")  # Username is valid!
```

### Use Case 2: Price Calculator

```python
def calculate_total(price, tax_rate):
    tax = price * tax_rate / 100
    total = price + tax
    print(f"Price: ${price}")
    print(f"Tax ({tax_rate}%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")

calculate_total(100, 8)   # 8% tax
calculate_total(250, 10)  # 10% tax
```

### Use Case 3: Temperature Converter

```python
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

celsius_to_fahrenheit(0)    # 0°C = 32.0°F
celsius_to_fahrenheit(25)   # 25°C = 77.0°F
celsius_to_fahrenheit(100)  # 100°C = 212.0°F
```

### Use Case 4: Game Score

```python
def update_score(player_name, points):
    print(f"{player_name} scored {points} points!")
    print(f"Great job, {player_name}!")

update_score("Alice", 50)
update_score("Bob", 75)
```

**Point out:** "See how ONE function handles ANY player with ANY score? That's flexibility!"

---

## Section 8: Best Practices (2 minutes)

### 1. Use Descriptive Parameter Names

```python
# BAD - Unclear
def calc(x, y):
    print(x * y)

# GOOD - Clear purpose
def calculate_area(length, width):
    print(length * width)
```

### 2. Reasonable Number of Parameters

```python
# BAD - Too many parameters (confusing!)
def create_user(name, age, email, phone, address, city, state, zip, country):
    pass

# GOOD - Grouped logically
def create_user(name, age, email):
    pass

def add_address(street, city, state, zip):
    pass
```

**Rule of Thumb:** "Try to keep it under 4-5 parameters. More than that, consider breaking into multiple functions."

### 3. Logical Parameter Order

```python
# GOOD - Related parameters together
def send_email(recipient, subject, message):
    pass

# CONFUSING - Random order
def send_email(message, recipient, subject):
    pass
```

### 4. Consistent Naming Convention

```python
# GOOD - All use snake_case
def calculate_tax(income, tax_rate):
    pass

def format_name(first_name, last_name):
    pass
```

---

## Section 9: Practice Exercise (2 minutes)

### Quick Challenge

"Let's try writing a function together!"

**Problem:** "Write a function `calculate_bmi` that takes `weight` in kg and `height` in meters, and prints the BMI."

**Formula:** BMI = weight / (height²)

**Give students 1 minute to try, then show solution:**

```python
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    print(f"Weight: {weight} kg")
    print(f"Height: {height} m")
    print(f"BMI: {bmi:.2f}")

# Test it
calculate_bmi(70, 1.75)
calculate_bmi(80, 1.80)
```

**Expected Output:**
```
Weight: 70 kg
Height: 1.75 m
BMI: 22.86
Weight: 80 kg
Height: 1.80 m
BMI: 24.69
```

---

## Wrap-Up (1 minute)

### Key Takeaways

**What We Learned:**
1. **Parameters** = placeholders in function definition
2. **Arguments** = actual values passed when calling
3. **Multiple parameters** = separate with commas
4. **Order matters** = arguments match by position
5. **Any data type** = strings, numbers, booleans, etc.

### The Power of Parameters

"Without parameters, functions are like single-use tools.
WITH parameters, functions become Swiss Army knives - versatile, reusable, and powerful!"

### Before vs After

**Before (Without Parameters):**
```python
def greet_alice():
    print("Hello, Alice!")

def greet_bob():
    print("Hello, Bob!")
```

**After (With Parameters):**
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Anyone!")
```

### Quick Reference

```python
# Template
def function_name(parameter1, parameter2):
    # Use parameters in function body
    result = parameter1 + parameter2
    print(result)

# Call with arguments
function_name(arg1, arg2)
```

### Next Lesson Preview

"Today we learned how to PUT data INTO functions using parameters.

Next lesson, we'll learn how to GET data OUT of functions using RETURN statements! Instead of just printing results, we'll learn how to send data back so we can use it in other calculations.

Think of it like this:
- Today: Functions that ACCEPT gifts (parameters)
- Next time: Functions that GIVE gifts back (return values)

Get ready - it's going to level up your functions even more!"

---

## Homework Preview

"For homework, you'll:
1. Write functions with 1, 2, and 3 parameters
2. Create a mini calculator (add, subtract, multiply, divide functions)
3. Build a user greeting system with name and age parameters
4. Practice parameter order by writing functions where order matters

Remember: The best way to learn parameters is to WRITE functions that use them. Start simple, then gradually add more parameters. See you next class!"

---

## Quick Check Questions (If Time Allows)

**Q1:** "What's the difference between a parameter and an argument?"
**A:** Parameter is in the definition (placeholder), argument is the value when calling (actual data).

**Q2:** "If I call `subtract(10, 3)`, what is the first parameter equal to?"
**A:** 10 (first argument goes to first parameter).

**Q3:** "Can parameters be different data types?"
**A:** Yes! String, integer, float, boolean - any type.

**Q4:** "What error do you get if you pass too few arguments?"
**A:** TypeError: missing required positional argument.

**Q5:** "Why use parameters instead of hardcoding values?"
**A:** Flexibility! One function works with any data, making code reusable and maintainable.

---

## Teaching Tips

### Engagement Strategies:
1. **Use Real Names:** Use students' names in greeting examples
2. **Live Mistakes:** Intentionally make errors to show error messages
3. **Interactive Calling:** Have students call out different arguments to try
4. **Real Problems:** Use relatable examples (pizza price, game scores, etc.)

### Common Student Confusions:
1. **Parameter vs Argument:** Keep reinforcing the difference
2. **Order Sensitivity:** Show multiple examples of order mattering
3. **Scope:** Parameters only exist inside the function
4. **Naming:** Parameters can have same names as outside variables

### Pacing Notes:
- If ahead: Add more practice problems
- If behind: Skip Use Case 4, reduce practice time
- Critical sections: Sections 2, 3, 4 (core concepts)

---

**End of Lecture**

"Great work today! You've learned one of the most important concepts in programming: function parameters. From now on, every function you write will be more powerful and flexible. Practice writing functions with parameters until it becomes natural. Happy coding!"
