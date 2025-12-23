# Question Bank: Returning Values from Functions Using Return

## Problem 1: Simple Return (Easy)

Write a function `double` that takes a number and returns double its value.

**Expected Output:**
```python
result = double(5)
print(result)  # 10

result = double(12)
print(result)  # 24
```

**Hint:** Use `return number * 2`

---

## Problem 2: Add Two Numbers with Return (Easy)

Create a function `add_numbers` that takes two parameters and returns their sum.

**Expected Output:**
```python
sum1 = add_numbers(5, 3)
print(sum1)  # 8

sum2 = add_numbers(10, 20)
print(sum2)  # 30
```

**Hint:** Return the sum of both parameters.

---

## Problem 3: Return String (Easy)

Define a function `make_greeting` that takes a `name` parameter and returns a greeting string.

**Expected Output:**
```python
msg = make_greeting("Alice")
print(msg)  # "Hello, Alice!"

msg = make_greeting("Bob")
print(msg)  # "Hello, Bob!"
```

**Hint:** Use f-string and return the formatted message.

---

## Problem 4: Return Boolean (Easy)

Write a function `is_even` that takes a number and returns True if even, False if odd.

**Expected Output:**
```python
print(is_even(4))   # True
print(is_even(7))   # False
print(is_even(10))  # True
```

**Hint:** Check if `number % 2 == 0` and return the result.

---

## Problem 5: Calculate Area with Return (Medium)

Create a function `calculate_rectangle_area` that takes length and width, and returns the area.

**Expected Output:**
```python
area1 = calculate_rectangle_area(5, 3)
print(f"Area: {area1}")  # Area: 15

area2 = calculate_rectangle_area(10, 8)
print(f"Area: {area2}")  # Area: 80
```

**Hint:** Return `length * width`

---

## Problem 6: Return Maximum of Two (Medium)

Write a function `get_max` that takes two numbers and returns the larger one.

**Expected Output:**
```python
print(get_max(10, 25))  # 25
print(get_max(50, 30))  # 50
print(get_max(15, 15))  # 15
```

**Hint:** Use if-else or the built-in `max()` function.

---

## Problem 7: Return Grade (Medium)

Define a function `calculate_grade` that takes a score and returns the letter grade.

**Expected Output:**
```python
print(calculate_grade(95))  # "A"
print(calculate_grade(85))  # "B"
print(calculate_grade(75))  # "C"
print(calculate_grade(65))  # "D"
print(calculate_grade(55))  # "F"
```

**Hint:** Use if-elif-else to determine grade, return the letter.

---

## Problem 8: Multiple Return Paths (Medium)

Create a function `classify_number` that takes a number and returns "Positive", "Negative", or "Zero".

**Expected Output:**
```python
print(classify_number(5))    # "Positive"
print(classify_number(-3))   # "Negative"
print(classify_number(0))    # "Zero"
```

**Hint:** Use multiple if-elif-else with return in each branch.

---

## Problem 9: Return Multiple Values (Medium)

Write a function `get_circle_info` that takes radius and returns both circumference and area.

**Expected Output:**
```python
circ, area = get_circle_info(5)
print(f"Circumference: {circ}, Area: {area}")
# Circumference: 31.4159, Area: 78.53975
```

**Hint:** Return as tuple: `return circumference, area`

---

## Problem 10: Temperature Converter with Return (Medium)

Define a function `celsius_to_fahrenheit` that converts Celsius to Fahrenheit and returns the result.

**Expected Output:**
```python
f1 = celsius_to_fahrenheit(0)
print(f"{f1}°F")  # 32.0°F

f2 = celsius_to_fahrenheit(100)
print(f"{f2}°F")  # 212.0°F
```

**Hint:** Formula: `(celsius * 9/5) + 32`

---

## Problem 11: Return from Loop (Medium)

Create a function `find_first_even` that takes a list and returns the first even number found.

**Expected Output:**
```python
nums = [1, 3, 5, 8, 9, 10]
result = find_first_even(nums)
print(result)  # 8
```

**Hint:** Loop through list, return immediately when even number found.

---

## Problem 12: Return None Explicitly (Easy)

Write a function `check_positive` that returns the number if positive, otherwise returns None.

**Expected Output:**
```python
print(check_positive(5))   # 5
print(check_positive(-3))  # None
print(check_positive(0))   # None
```

**Hint:** Return number if `number > 0`, else `return None`

---

## Problem 13: Calculate Discount with Return (Medium)

Define a function `apply_discount` that takes price and discount percentage, returns final price.

**Expected Output:**
```python
final = apply_discount(100, 20)
print(f"${final}")  # $80.0

final = apply_discount(250, 10)
print(f"${final}")  # $225.0
```

**Hint:** Calculate discount amount, return `price - discount_amount`

---

## Problem 14: Return Early (Medium)

Create a function `validate_age` that returns "Valid" for ages 18-100, otherwise returns an error message.

**Expected Output:**
```python
print(validate_age(25))   # "Valid"
print(validate_age(15))   # "Too young"
print(validate_age(120))  # "Invalid age"
```

**Hint:** Use early returns for error cases, final return for valid case.

---

## Problem 15: Power Function with Return (Medium)

Write a function `power` that takes base and exponent, returns the result.

**Expected Output:**
```python
print(power(2, 3))   # 8
print(power(5, 2))   # 25
print(power(10, 0))  # 1
```

**Hint:** Return `base ** exponent`

---

## Problem 16: Return String Length (Easy)

Define a function `get_length` that takes a string and returns its length.

**Expected Output:**
```python
print(get_length("hello"))  # 5
print(get_length("Python"))  # 6
```

**Hint:** Return `len(text)`

---

## Problem 17: Return List Element (Medium)

Create a function `get_first_element` that takes a list and returns the first element, or None if empty.

**Expected Output:**
```python
print(get_first_element([1, 2, 3]))  # 1
print(get_first_element([]))         # None
```

**Hint:** Check if list is empty first, then return first element.

---

## Problem 18: Calculate BMI with Return (Hard)

Write a function `calculate_bmi` that takes weight (kg) and height (m), returns BMI and category.

**Expected Output:**
```python
bmi, category = calculate_bmi(70, 1.75)
print(f"BMI: {bmi:.2f}, Category: {category}")
# BMI: 22.86, Category: Normal
```

**Hint:** Calculate BMI, determine category, return both as tuple.

---

## Problem 19: Return Vowel Count (Medium)

Define a function `count_vowels` that takes a string and returns the number of vowels.

**Expected Output:**
```python
count = count_vowels("Hello World")
print(f"Vowels: {count}")  # Vowels: 3

count = count_vowels("Python")
print(f"Vowels: {count}")  # Vowels: 1
```

**Hint:** Loop through string, count vowels, return count.

---

## Problem 20: Return Factorial (Hard)

Create a function `factorial` that takes a number and returns its factorial.

**Expected Output:**
```python
print(factorial(5))  # 120
print(factorial(3))  # 6
print(factorial(0))  # 1
```

**Hint:** Use loop to multiply, return result. Factorial of 0 is 1.

---

## Problem 21: Return List of Squares (Medium)

Write a function `get_squares` that takes a number n and returns a list of squares from 1 to n.

**Expected Output:**
```python
result = get_squares(5)
print(result)  # [1, 4, 9, 16, 25]
```

**Hint:** Use list comprehension or loop to build list, return it.

---

## Problem 22: Return Middle Element (Medium)

Define a function `get_middle` that takes a list and returns the middle element.

**Expected Output:**
```python
print(get_middle([1, 2, 3, 4, 5]))  # 3
print(get_middle([10, 20, 30]))     # 20
```

**Hint:** Find middle index using `len(lst) // 2`, return that element.

---

## Problem 23: Return Absolute Value (Easy)

Create a function `absolute_value` that takes a number and returns its absolute value.

**Expected Output:**
```python
print(absolute_value(-5))   # 5
print(absolute_value(10))   # 10
print(absolute_value(-15))  # 15
```

**Hint:** If negative, return `-number`, else return `number`.

---

## Problem 24: Return Prime Check (Hard)

Write a function `is_prime` that takes a number and returns True if prime, False otherwise.

**Expected Output:**
```python
print(is_prime(17))  # True
print(is_prime(18))  # False
print(is_prime(2))   # True
```

**Hint:** Check divisibility from 2 to sqrt(number), return False if divisible.

---

## Problem 25: Return Min and Max (Medium)

Define a function `get_min_max` that takes three numbers and returns the smallest and largest.

**Expected Output:**
```python
minimum, maximum = get_min_max(5, 10, 3)
print(f"Min: {minimum}, Max: {maximum}")  # Min: 3, Max: 10
```

**Hint:** Use `min()` and `max()` functions, return as tuple.

---

## Problem 26: Return Reversed String (Easy)

Create a function `reverse_string` that takes a string and returns it reversed.

**Expected Output:**
```python
print(reverse_string("hello"))   # "olleh"
print(reverse_string("Python"))  # "nohtyP"
```

**Hint:** Return `text[::-1]`

---

## Problem 27: Return Sum of List (Medium)

Write a function `sum_list` that takes a list of numbers and returns their sum.

**Expected Output:**
```python
total = sum_list([1, 2, 3, 4, 5])
print(total)  # 15

total = sum_list([10, 20, 30])
print(total)  # 60
```

**Hint:** Use loop or built-in `sum()` function.

---

## Problem 28: Return Leap Year Check (Medium)

Define a function `is_leap_year` that takes a year and returns True if leap year, False otherwise.

**Expected Output:**
```python
print(is_leap_year(2024))  # True
print(is_leap_year(2023))  # False
print(is_leap_year(2000))  # True
```

**Hint:** Divisible by 4 AND (not by 100 OR by 400).

---

## Problem 29: Return Fibonacci Number (Hard)

Create a function `fibonacci` that takes n and returns the nth Fibonacci number.

**Expected Output:**
```python
print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(5))  # 5
print(fibonacci(10)) # 55
```

**Hint:** Use loop to calculate, return result.

---

## Problem 30: Return Filtered List (Hard)

Write a function `get_evens` that takes a list and returns a new list with only even numbers.

**Expected Output:**
```python
result = get_evens([1, 2, 3, 4, 5, 6])
print(result)  # [2, 4, 6]

result = get_evens([1, 3, 5])
print(result)  # []
```

**Hint:** Use list comprehension or loop to build new list with evens.

---

## Key Concepts

### What is Return?

```python
def function_name():
    # Do some work
    return value  # Send value back
```

The `return` statement:
- Sends a value back to the caller
- Exits the function immediately
- Can return any data type
- Returns `None` if no value specified

### Return vs Print

```python
# Print - displays but doesn't return value
def add_print(a, b):
    print(a + b)  # Shows on screen

result = add_print(5, 3)  # Displays: 8
print(result)  # None (function returned nothing)

# Return - sends value back
def add_return(a, b):
    return a + b  # Send back the sum

result = add_return(5, 3)  # result gets 8
print(result)  # 8
```

**Key Difference:**
- `print()` → For displaying output to users
- `return` → For sending data back to use in code

### Using Returned Values

```python
def square(n):
    return n * n

# Store in variable
x = square(5)  # x = 25

# Use in calculation
y = square(3) + square(4)  # y = 9 + 16 = 25

# Pass to another function
print(square(10))  # Prints 100

# Use in conditions
if square(2) == 4:
    print("Correct!")
```

### Multiple Return Statements

```python
def check_sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Only ONE return executes (first match)
print(check_sign(5))   # "Positive"
print(check_sign(-3))  # "Negative"
```

### Early Return Pattern

```python
def validate_input(value):
    # Check error cases first
    if value < 0:
        return "Error: Negative value"
    if value > 100:
        return "Error: Too large"

    # Main logic only runs if valid
    return "Valid"
```

**Benefits:**
- Clearer error handling
- Avoids deep nesting
- Exits early on errors

### Returning Multiple Values

```python
def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average  # Returns tuple

# Unpack returned values
sum_val, avg_val = calculate_stats([1, 2, 3, 4, 5])
print(f"Sum: {sum_val}, Average: {avg_val}")
```

### Return None

```python
# Explicit return None
def do_something():
    print("Working...")
    return None

# Implicit return None (no return statement)
def do_something_else():
    print("Working...")
    # Automatically returns None

x = do_something()  # x is None
y = do_something_else()  # y is None
```

### Common Patterns

**Pattern 1: Calculation and Return**
```python
def calculate_total(price, quantity):
    total = price * quantity
    return total
```

**Pattern 2: Validation and Return Boolean**
```python
def is_valid_email(email):
    if '@' not in email:
        return False
    if '.' not in email:
        return False
    return True
```

**Pattern 3: Find and Return**
```python
def find_item(items, target):
    for item in items:
        if item == target:
            return item
    return None  # Not found
```

**Pattern 4: Process and Return List**
```python
def double_all(numbers):
    result = []
    for num in numbers:
        result.append(num * 2)
    return result
```

### Best Practices

1. **Return Consistent Types**: Don't return string sometimes, number other times
2. **Document Return Values**: Comment what function returns
3. **Use Descriptive Names**: Function name should hint at return value
4. **Return Early for Errors**: Check errors first, return early
5. **Avoid Side Effects**: Function should return value, not modify globals

### Common Mistakes

1. **Forgetting to Return**
   ```python
   # WRONG
   def add(a, b):
       a + b  # Calculated but not returned!

   # RIGHT
   def add(a, b):
       return a + b
   ```

2. **Code After Return**
   ```python
   # WRONG - Second line never runs
   def get_value():
       return 10
       print("This never prints!")  # Unreachable

   # RIGHT
   def get_value():
       print("Calculating...")
       return 10
   ```

3. **Return in Wrong Scope**
   ```python
   # WRONG - Return inside loop exits function
   def sum_list(numbers):
       for num in numbers:
           return num  # Only returns first element!

   # RIGHT
   def sum_list(numbers):
       total = 0
       for num in numbers:
           total += num
       return total  # Returns after all processing
   ```

4. **Not Using Returned Value**
   ```python
   # Wasteful - result not used
   add(5, 3)  # Returns 8, but value is lost

   # Better - store and use
   result = add(5, 3)
   print(result)
   ```

### When to Use Return vs Print

**Use Return When:**
- You need the value for further calculations
- Result will be stored in a variable
- Function result will be passed to another function
- Building reusable, composable functions

**Use Print When:**
- Debugging
- Displaying information to user
- Logging progress
- Creating output for reports

**Often Use Both:**
```python
def calculate_and_display(a, b):
    result = a + b
    print(f"Calculating: {a} + {b} = {result}")  # Display
    return result  # Also return for use
```

### Real-World Applications

1. **Calculations**: Return computed values
2. **Validation**: Return True/False for checks
3. **Data Processing**: Return transformed data
4. **API Functions**: Return results from operations
5. **Helper Functions**: Return intermediate values
6. **Utilities**: Return formatted/processed data
