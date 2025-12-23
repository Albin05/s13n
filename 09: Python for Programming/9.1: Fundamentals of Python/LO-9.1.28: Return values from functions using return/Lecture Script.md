# Lecture Script: Returning Values from Functions Using Return

**Duration:** 20-25 minutes
**Learning Objective:** Students will be able to use return statements to send values back from functions and understand the difference between returning and printing values.

---

## Hook (2 minutes)

"You've learned how to create functions and pass data INTO them using parameters. But here's a critical question: how do we get data OUT of a function?

Imagine you build a calculator app. You write a function to add two numbers. The function does the math... and then what? Just prints the answer? What if you need to use that answer in another calculation? What if you need to save it? Display it differently?

This is where most beginners get stuck. They think printing IS returning. But here's the truth: **print() SHOWS you the answer, return GIVES you the answer.**

Today, we're learning about the `return` statement - one of the most important concepts in programming. It's the difference between a function that just displays information and a function that produces reusable data. By the end of this lesson, you'll understand how to build functions that don't just calculate - they deliver results you can actually use!

Let's dive in!"

---

## Section 1: The Problem - Functions That Only Print (3 minutes)

### The Limitation

"First, let's see what happens when we only use print():"

```python
def add(a, b):
    print(a + b)

add(5, 3)  # Displays: 8
```

**Ask class:** "This works, right? We see 8 on the screen. What's the problem?"

### The Issue Revealed

```python
def add(a, b):
    print(a + b)

# Try to use the result
x = add(5, 3)  # Displays: 8
print(x)  # Output: None

# Try to calculate with it
y = add(5, 3) + 10  # Displays 8, then Error!
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
```

**Point out:** "See the problem? The function DISPLAYS 8, but it doesn't GIVE us 8 to use! `x` is None because the function didn't return anything!"

### Real-World Scenario

```python
def calculate_discount(price, percent):
    discount = price * percent / 100
    print(discount)

# Business needs: Calculate discount, then subtract from price
discount_amount = calculate_discount(100, 20)  # Displays: 20.0
final_price = 100 - discount_amount  # Error! discount_amount is None
```

**Emphasize:** "In real programs, we need to USE function results, not just display them. That's why we need `return`!"

---

## Section 2: What Is Return? (4 minutes)

### Definition

"The `return` statement sends a value back from a function to wherever the function was called. Think of it as the function's OUTPUT."

### Syntax

```python
def function_name():
    # Do some work
    return value  # Send value back
```

### First Example

```python
def add(a, b):
    return a + b  # Send back the sum

result = add(5, 3)  # result receives 8
print(result)  # 8
```

**Break it down:**
1. `add(5, 3)` is called
2. Function calculates `5 + 3 = 8`
3. `return 8` sends the value back
4. `result` receives 8
5. Now we can use `result` anywhere!

### Return Exits the Function

```python
def calculate():
    print("Starting calculation...")
    return 10
    print("This never runs!")  # Unreachable code

result = calculate()
```

**Output:**
```
Starting calculation...
```

**Explain:** "The moment `return` executes, the function stops immediately and goes back to the caller. Any code after `return` is unreachable."

---

## Section 3: Return vs Print (4 minutes)

### Side-by-Side Comparison

```python
# Using print - can't reuse value
def add_print(a, b):
    print(a + b)

# Using return - value can be reused
def add_return(a, b):
    return a + b
```

### Demonstration

```python
# Print version
x = add_print(5, 3)  # Displays: 8
print(f"Result: {x}")  # Result: None
# Can't use in calculations!

# Return version
y = add_return(5, 3)  # Nothing displayed (yet)
print(f"Result: {y}")  # Result: 8
# Can use in calculations!
z = y + 10  # z = 18
```

### When to Use Each

**Use PRINT when:**
- Debugging
- Showing information to users
- Logging progress
- Creating reports

**Use RETURN when:**
- You need the value for calculations
- Storing data in variables
- Passing to other functions
- Building reusable functions

### You Can Use Both!

```python
def calculate_total(price, tax_rate):
    tax = price * tax_rate / 100
    total = price + tax
    print(f"Calculating: ${price} + ${tax} tax = ${total}")  # Display
    return total  # Also return for use

amount = calculate_total(100, 8)  # Shows calculation
discounted = amount * 0.9  # Use returned value
```

---

## Section 4: Multiple Return Statements (3 minutes)

### Conditional Returns

"A function can have multiple `return` statements, but only ONE will execute!"

```python
def classify_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(classify_number(5))    # Positive
print(classify_number(-3))   # Negative
print(classify_number(0))    # Zero
```

**Explain:** "Each return statement handles a different case. Once one executes, the function exits immediately."

### Live Coding - Grade Calculator

```python
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test it
grade = calculate_grade(85)
print(f"Grade: {grade}")  # Grade: B
```

### The Early Return Pattern

"Check for errors FIRST, then handle normal cases:"

```python
def calculate_discount(price, discount_percent):
    # Check errors first - exit early
    if price < 0:
        return "Error: Negative price"
    if discount_percent < 0 or discount_percent > 100:
        return "Error: Invalid discount"

    # Main logic only if inputs are valid
    discount = price * discount_percent / 100
    return discount

print(calculate_discount(100, 20))   # 20.0
print(calculate_discount(-50, 10))   # Error: Negative price
print(calculate_discount(100, 150))  # Error: Invalid discount
```

**Benefits:**
- Clearer error handling
- Less nested code
- Main logic isn't buried in conditions

---

## Section 5: Returning Multiple Values (3 minutes)

### The Tuple Return

"Python lets you return multiple values at once!"

```python
def get_name_parts(full_name):
    parts = full_name.split()
    first_name = parts[0]
    last_name = parts[-1]
    return first_name, last_name  # Returns tuple

# Unpack the returned tuple
first, last = get_name_parts("Alice Johnson")
print(f"First: {first}")  # First: Alice
print(f"Last: {last}")    # Last: Johnson
```

### What's Really Happening

```python
def get_coordinates():
    return 10, 20  # Returns tuple (10, 20)

# Can unpack
x, y = get_coordinates()

# Or keep as tuple
coords = get_coordinates()
print(coords)  # (10, 20)
print(type(coords))  # <class 'tuple'>
```

### Real-World Example - Circle Calculator

```python
def calculate_circle(radius):
    pi = 3.14159
    circumference = 2 * pi * radius
    area = pi * radius * radius
    return circumference, area  # Return both

# Use the returned values
circ, area = calculate_circle(5)
print(f"Circumference: {circ:.2f}")  # 31.42
print(f"Area: {area:.2f}")  # 78.54
```

### Statistics Function

```python
def get_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return total, average, minimum, maximum

# Get all stats at once
total, avg, min_val, max_val = get_stats([1, 2, 3, 4, 5])
print(f"Total: {total}, Average: {avg}, Min: {min_val}, Max: {max_val}")
# Total: 15, Average: 3.0, Min: 1, Max: 5
```

---

## Section 6: Return in Loops (2 minutes)

### Return Exits Immediately

```python
def find_first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num  # Exit function immediately!
    return None  # Only if no even found

nums = [1, 3, 5, 8, 9, 10]
result = find_first_even(nums)
print(result)  # 8 (stops at first even number)
```

**Explain:** "When return executes in a loop, the loop stops and the function exits. It doesn't check 9 or 10!"

### Find vs Find All

```python
# Find FIRST (return in loop)
def find_first(items, target):
    for item in items:
        if item == target:
            return item  # Exit immediately
    return None

# Find ALL (return after loop)
def find_all(items, target):
    matches = []
    for item in items:
        if item == target:
            matches.append(item)
    return matches  # Return after checking all

numbers = [1, 5, 3, 5, 7, 5]
print(find_first(numbers, 5))  # 5 (first occurrence)
print(find_all(numbers, 5))    # [5, 5, 5] (all occurrences)
```

---

## Section 7: Return None (2 minutes)

### Implicit None

```python
def greet(name):
    print(f"Hello, {name}")
    # No return statement

result = greet("Alice")  # Displays: Hello, Alice
print(result)  # None
```

**Explain:** "Functions without `return` automatically return `None`."

### Explicit None

```python
def check_positive(number):
    if number > 0:
        return number
    else:
        return None  # Explicit

print(check_positive(5))   # 5
print(check_positive(-3))  # None
```

### Return Without Value

```python
def validate_input(data):
    if not data:
        return  # Exit early, return None
    # Process data here
    print(f"Processing: {data}")

validate_input("")      # Returns None silently
validate_input("test")  # Processing: test
```

**Use case:** "Use bare `return` to exit early when there's no meaningful value to return."

---

## Section 8: Using Returned Values (2 minutes)

### Store and Use

```python
def square(x):
    return x * x

# Store in variable
result = square(5)
print(result)  # 25

# Use in calculation
total = square(3) + square(4)  # 9 + 16 = 25

# Pass to another function
print(square(10))  # 100

# Use in condition
if square(5) > 20:
    print("Large number")  # This runs
```

### Function Composition

"Returned values let you build complex operations from simple functions!"

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def square(x):
    return x * x

# Compose functions!
result = multiply(add(2, 3), square(2))  # (2+3) * 2² = 5 * 4 = 20
print(result)  # 20
```

### Real Application - Tax Calculator

```python
def calculate_tax(income):
    return income * 0.15

def calculate_net_income(income):
    tax = calculate_tax(income)  # Use returned value
    return income - tax

def format_currency(amount):
    return f"${amount:,.2f}"

# Chain functions together
salary = 50000
net = calculate_net_income(salary)
formatted = format_currency(net)
print(f"Net income: {formatted}")  # Net income: $42,500.00
```

---

## Section 9: Common Mistakes (2 minutes)

### Mistake 1: Forgetting to Return

```python
# WRONG - Calculates but doesn't return
def calculate_area(length, width):
    area = length * width
    # Forgot return!

result = calculate_area(5, 3)
print(result)  # None

# RIGHT - Return the calculated value
def calculate_area(length, width):
    area = length * width
    return area

result = calculate_area(5, 3)
print(result)  # 15
```

### Mistake 2: Code After Return

```python
# WRONG - Code after return never runs
def process():
    return 10
    print("Done")  # Unreachable!

# RIGHT - Put code before return
def process():
    print("Done")
    return 10
```

### Mistake 3: Confusing Print with Return

```python
# WRONG - Prints but can't use result
def add(a, b):
    print(a + b)

x = add(5, 3)  # Displays 8, but x is None
y = x + 10  # Error!

# RIGHT - Return for reuse
def add(a, b):
    return a + b

x = add(5, 3)  # x = 8
y = x + 10  # y = 18
```

### Mistake 4: Not Using Returned Value

```python
# WRONG - Value is wasted
calculate_total(100, 20)  # Returns value but we ignore it

# RIGHT - Capture and use
total = calculate_total(100, 20)
print(total)
```

---

## Section 10: Practice Exercise (2 minutes)

### Quick Challenge

"Let's write a function together!"

**Problem:** "Create a function `calculate_bmi` that takes weight (kg) and height (m), calculates BMI, and returns both the BMI value and a category string ('Underweight', 'Normal', 'Overweight', or 'Obese')."

**Give students 1-2 minutes to try, then show solution:**

```python
def calculate_bmi(weight, height):
    # Calculate BMI
    bmi = weight / (height ** 2)

    # Determine category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    # Return both values
    return bmi, category

# Test it
bmi_value, bmi_category = calculate_bmi(70, 1.75)
print(f"BMI: {bmi_value:.2f}")  # BMI: 22.86
print(f"Category: {bmi_category}")  # Category: Normal
```

**Ask:** "Why do we return values instead of just printing them?"
**Answer:** "So we can use them in other calculations, store them in databases, or display them in different formats!"

---

## Wrap-Up (1 minute)

### Key Takeaways

**What We Learned:**
1. **`return` sends values back** from functions to the caller
2. **`return` exits immediately** - code after return doesn't run
3. **`return` ≠ `print`** - return for reuse, print for display
4. **Multiple returns** - only one executes (first match)
5. **Return multiple values** using tuples
6. **Return None** explicitly or implicitly
7. **Functions without return** automatically return None

### The Power of Return

"Before today, your functions could display information. Now they can PRODUCE data that can be:
- Stored in variables
- Used in calculations
- Passed to other functions
- Built into complex operations

This transforms functions from simple display tools into powerful, reusable components!"

### Before vs After

**Before (Without Return):**
```python
def add(a, b):
    print(a + b)  # Just displays

add(5, 3)  # Shows 8, can't use it
```

**After (With Return):**
```python
def add(a, b):
    return a + b  # Sends value back

result = add(5, 3)  # Can store, use, reuse!
total = add(result, 10)  # Build on it!
```

### Quick Reference Card

```python
# Basic return
def function_name():
    result = calculate_something()
    return result

# Multiple returns
def classify(x):
    if x > 0:
        return "Positive"
    return "Negative"

# Return multiple values
def get_data():
    return value1, value2

# Early return
def validate(x):
    if error_condition:
        return None
    return processed_value

# Return in loop
def find_first(items, target):
    for item in items:
        if item == target:
            return item
    return None
```

---

## Next Lesson Preview

"Today we learned how to get data OUT of functions using return.

Next lesson, we'll learn about **default parameters** - how to make parameters optional by giving them default values! This makes functions even more flexible.

Think of it like this:
- Today: Functions that GIVE you results (return)
- Next time: Functions with FLEXIBLE inputs (defaults)

Example preview:
```python
def greet(name, greeting="Hello"):  # greeting has default value
    return f"{greeting}, {name}!"

print(greet("Alice"))  # Hello, Alice! (uses default)
print(greet("Bob", "Hi"))  # Hi, Bob! (custom greeting)
```

Get ready to make your functions even more powerful!"

---

## Homework Preview

"For homework, you'll:
1. Write functions that return calculated values
2. Create functions with multiple return statements
3. Build functions that return multiple values
4. Practice the early return pattern
5. Solve real-world problems using return values

Remember: Every time you write a function that computes something, ask yourself: 'Should I return this value so it can be reused?' If yes, use `return`!

See you next class!"

---

## Quick Check Questions (If Time Allows)

**Q1:** "What's the difference between return and print?"
**A:** Return sends a value back for reuse, print displays to screen.

**Q2:** "What happens to code after a return statement?"
**A:** It never executes - return exits the function immediately.

**Q3:** "What does a function return if there's no return statement?"
**A:** None (implicit return).

**Q4:** "Can a function have multiple return statements?"
**A:** Yes, but only ONE will execute (first match).

**Q5:** "How do you return multiple values?"
**A:** Separate with commas - Python returns them as a tuple.

**Q6:** "What happens when return executes inside a loop?"
**A:** Function exits immediately, loop stops.

**Q7:** "Can you use a returned value in calculations?"
**A:** Yes! That's the main benefit of return - values can be reused.

**Q8:** "What does `return` without a value do?"
**A:** Returns None and exits the function.

---

## Teaching Tips

### Engagement Strategies:

1. **Show Don't Tell:** Demonstrate the error when trying to use a printed value in calculations
2. **Interactive Examples:** Have students predict what will be returned
3. **Error Exploration:** Intentionally write code with mistakes to show error messages
4. **Real Scenarios:** Use relatable examples (calculator, shopping cart, grades)
5. **Visual Tracing:** Draw function call flow showing where return sends values

### Common Student Confusions:

1. **Return vs Print:** Keep reinforcing this throughout - use side-by-side comparisons
2. **Unreachable Code:** Show examples where code after return is ignored
3. **Multiple Returns:** Clarify that only ONE return executes, not all of them
4. **None Return:** Explain that functions return None if no return statement
5. **Tuple Returns:** Show that comma-separated returns create tuples automatically

### Demonstration Tips:

1. **Use print() to trace:** Add prints before and after return to show execution flow
2. **Store in variables:** Always demonstrate capturing returned values in variables
3. **Build incrementally:** Start with simple returns, add complexity gradually
4. **Show composition:** Demonstrate how returned values enable function composition
5. **Error examples:** Show what happens when you forget return

### Pacing Notes:

- If ahead: Add more practice problems, deeper dive into early return pattern
- If behind: Skip Practice Exercise, reduce real-world examples
- Critical sections: Sections 2 (What Is Return), 3 (Return vs Print), 5 (Multiple Values)
- Can combine: Sections 6 and 7 if time is tight

### Key Phrases to Repeat:

- "Print shows, return gives"
- "Return exits immediately"
- "Return for reuse, print for display"
- "Only one return executes"
- "Functions without return return None"

---

## Extended Examples (Optional/Bonus)

### Example 1: Bank Account

```python
def calculate_interest(balance, rate):
    interest = balance * rate / 100
    return interest

def calculate_new_balance(balance, rate):
    interest = calculate_interest(balance, rate)  # Use returned value
    new_balance = balance + interest
    return new_balance

# Use the functions
current = 1000
new = calculate_new_balance(current, 5)
print(f"Balance: ${current} → ${new}")  # Balance: $1000 → $1050.0
```

### Example 2: String Processing

```python
def clean_text(text):
    # Remove spaces, make lowercase
    cleaned = text.strip().lower()
    return cleaned

def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Chain functions
user_input = "  Hello World  "
cleaned = clean_text(user_input)
vowel_count = count_vowels(cleaned)
print(f"Text: '{cleaned}', Vowels: {vowel_count}")
# Text: 'hello world', Vowels: 3
```

### Example 3: List Processing

```python
def get_evens(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

def sum_list(numbers):
    return sum(numbers)

# Use returned values
nums = [1, 2, 3, 4, 5, 6]
even_nums = get_evens(nums)  # [2, 4, 6]
total = sum_list(even_nums)  # 12
print(f"Even numbers: {even_nums}, Sum: {total}")
```

---

**End of Lecture**

"Excellent work today! You've learned one of the most fundamental concepts in programming: the return statement. From now on, every function you write can produce data that can be stored, calculated with, and reused throughout your programs.

The key takeaway: **Functions that return values are building blocks you can combine to solve complex problems.**

Practice writing functions with return statements until it becomes second nature. Think about what data your function should PRODUCE, not just what it should DISPLAY.

Happy coding, and see you next time!"
