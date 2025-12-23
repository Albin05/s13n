# Question Bank: Using Function Parameters to Accept Inputs

## Problem 1: Single Parameter Greeting (Easy)

Write a function `greet_person` that takes one parameter `name` and prints "Hello, {name}!".

**Expected Output:**
```python
greet_person("Alice")  # Hello, Alice!
greet_person("Bob")    # Hello, Bob!
```

**Hint:** Use f-string or string concatenation to include the parameter in the output.

---

## Problem 2: Two Number Addition (Easy)

Define a function `add_two` that takes two parameters `num1` and `num2`, and prints their sum.

**Expected Output:**
```python
add_two(5, 3)    # Sum: 8
add_two(10, 20)  # Sum: 30
```

**Hint:** Calculate sum = num1 + num2, then print the result.

---

## Problem 3: Rectangle Area Calculator (Easy)

Create a function `calculate_area` that accepts `length` and `width` parameters and prints the area.

**Expected Output:**
```python
calculate_area(5, 3)   # Area: 15
calculate_area(10, 4)  # Area: 40
```

**Hint:** Area = length × width

---

## Problem 4: Three Number Multiplier (Easy)

Write a function `multiply_three` that takes three parameters and prints their product.

**Expected Output:**
```python
multiply_three(2, 3, 4)  # Product: 24
multiply_three(5, 5, 2)  # Product: 50
```

**Hint:** Result = num1 × num2 × num3

---

## Problem 5: Person Introduction (Medium)

Define a function `introduce` that takes `name`, `age`, and `city` parameters and prints a full introduction.

**Expected Output:**
```python
introduce("Alice", 25, "New York")
# My name is Alice
# I am 25 years old
# I live in New York
```

**Hint:** Use multiple print statements with the parameters.

---

## Problem 6: Temperature Converter (Medium)

Create a function `celsius_to_fahrenheit` that takes a temperature in Celsius and prints the Fahrenheit equivalent.

**Expected Output:**
```python
celsius_to_fahrenheit(0)   # 0°C = 32.0°F
celsius_to_fahrenheit(100) # 100°C = 212.0°F
celsius_to_fahrenheit(25)  # 25°C = 77.0°F
```

**Hint:** Formula: F = (C × 9/5) + 32

---

## Problem 7: Circle Calculations (Medium)

Write a function `circle_info` that takes `radius` as a parameter and prints both circumference and area.

**Expected Output:**
```python
circle_info(5)
# Radius: 5
# Circumference: 31.4159
# Area: 78.53975
```

**Hint:** Circumference = 2πr, Area = πr², use π = 3.14159

---

## Problem 8: Power Calculator (Medium)

Define a function `power` that takes `base` and `exponent` parameters and prints the result.

**Expected Output:**
```python
power(2, 3)   # 2^3 = 8
power(5, 2)   # 5^2 = 25
power(10, 0)  # 10^0 = 1
```

**Hint:** Use the `**` operator or a loop.

---

## Problem 9: Age Validator (Medium)

Create a function `check_age` that takes `age` as a parameter and prints whether the person is a minor, adult, or senior.

**Expected Output:**
```python
check_age(15)  # Minor (under 18)
check_age(25)  # Adult (18-64)
check_age(70)  # Senior (65+)
```

**Hint:** Use if-elif-else conditions.

---

## Problem 10: Grade Calculator (Medium)

Write a function `calculate_grade` that takes a `score` parameter and prints the letter grade.

**Expected Output:**
```python
calculate_grade(95)  # Grade: A
calculate_grade(85)  # Grade: B
calculate_grade(75)  # Grade: C
calculate_grade(65)  # Grade: D
calculate_grade(55)  # Grade: F
```

**Hint:** A: 90+, B: 80-89, C: 70-79, D: 60-69, F: below 60

---

## Problem 11: String Repeater (Easy)

Define a function `repeat_string` that takes a `text` and `count` parameter, and prints the text repeated count times.

**Expected Output:**
```python
repeat_string("Hello", 3)  # HelloHelloHello
repeat_string("*", 5)      # *****
```

**Hint:** Use string multiplication: text * count

---

## Problem 12: Triangle Type Checker (Hard)

Create a function `triangle_type` that takes three side lengths and prints the triangle type (equilateral, isosceles, or scalene).

**Expected Output:**
```python
triangle_type(5, 5, 5)    # Equilateral triangle
triangle_type(5, 5, 3)    # Isosceles triangle
triangle_type(3, 4, 5)    # Scalene triangle
```

**Hint:** Equilateral: all equal, Isosceles: two equal, Scalene: all different

---

## Problem 13: Discount Calculator (Medium)

Write a function `apply_discount` that takes `price` and `discount_percent` and prints the final price.

**Expected Output:**
```python
apply_discount(100, 10)   # Final price: $90.0
apply_discount(250, 20)   # Final price: $200.0
apply_discount(80, 15)    # Final price: $68.0
```

**Hint:** Final = price - (price × discount_percent / 100)

---

## Problem 14: Even or Odd Checker (Easy)

Define a function `check_even_odd` that takes a `number` parameter and prints whether it's even or odd.

**Expected Output:**
```python
check_even_odd(4)   # 4 is even
check_even_odd(7)   # 7 is odd
check_even_odd(10)  # 10 is even
```

**Hint:** Use modulo operator: number % 2 == 0

---

## Problem 15: BMI Calculator (Medium)

Create a function `calculate_bmi` that takes `weight` (kg) and `height` (m) and prints the BMI with category.

**Expected Output:**
```python
calculate_bmi(70, 1.75)
# BMI: 22.86
# Category: Normal weight
```

**Hint:** BMI = weight / (height²). Categories: <18.5 Underweight, 18.5-24.9 Normal, 25-29.9 Overweight, 30+ Obese

---

## Problem 16: Count Down Timer (Medium)

Write a function `countdown` that takes a `start` parameter and counts down to 1.

**Expected Output:**
```python
countdown(5)
# 5 4 3 2 1 Go!
```

**Hint:** Use a for loop with range(start, 0, -1).

---

## Problem 17: Name Formatter (Easy)

Define a function `format_name` that takes `first_name` and `last_name` and prints the full name in different formats.

**Expected Output:**
```python
format_name("John", "Doe")
# Full name: John Doe
# Last, First: Doe, John
# Initials: J.D.
```

**Hint:** Use string slicing for initials: first_name[0] and last_name[0]

---

## Problem 18: Simple Interest Calculator (Medium)

Create a function `simple_interest` that takes `principal`, `rate`, and `time` parameters.

**Expected Output:**
```python
simple_interest(1000, 5, 2)
# Principal: $1000
# Interest: $100.0
# Total: $1100.0
```

**Hint:** Interest = (principal × rate × time) / 100

---

## Problem 19: Password Strength Checker (Hard)

Write a function `check_password_strength` that takes a `password` parameter and checks various criteria.

**Expected Output:**
```python
check_password_strength("Abc123")
# Length: 6 (Too short)
# Has uppercase: Yes
# Has lowercase: Yes
# Has numbers: Yes
# Strength: Weak
```

**Hint:** Check len(), str.isupper(), str.islower(), str.isdigit() methods.

---

## Problem 20: Fizz Buzz Function (Medium)

Define a function `fizz_buzz_single` that takes a `number` and prints Fizz, Buzz, FizzBuzz, or the number.

**Expected Output:**
```python
fizz_buzz_single(3)   # Fizz
fizz_buzz_single(5)   # Buzz
fizz_buzz_single(15)  # FizzBuzz
fizz_buzz_single(7)   # 7
```

**Hint:** Divisible by 3 and 5 = FizzBuzz, by 3 = Fizz, by 5 = Buzz

---

## Problem 21: Time Converter (Medium)

Create a function `convert_seconds` that takes total seconds and prints hours, minutes, and seconds.

**Expected Output:**
```python
convert_seconds(3665)
# 1 hour(s), 1 minute(s), 5 second(s)
```

**Hint:** hours = seconds // 3600, minutes = (seconds % 3600) // 60, remaining = seconds % 60

---

## Problem 22: Range Checker (Easy)

Write a function `in_range` that takes `number`, `min_val`, and `max_val` and checks if number is in range.

**Expected Output:**
```python
in_range(50, 1, 100)   # 50 is in range [1, 100]
in_range(150, 1, 100)  # 150 is out of range [1, 100]
```

**Hint:** Check if min_val <= number <= max_val

---

## Problem 23: String Length Categories (Easy)

Define a function `categorize_length` that takes a `text` parameter and categorizes its length.

**Expected Output:**
```python
categorize_length("Hi")          # Short (1-5 chars)
categorize_length("Hello World") # Medium (6-15 chars)
categorize_length("This is a very long sentence") # Long (16+ chars)
```

**Hint:** Use len(text) and if-elif-else

---

## Problem 24: Multiplication Table Row (Medium)

Create a function `times_table_row` that takes a `number` and prints one row of its multiplication table.

**Expected Output:**
```python
times_table_row(5)
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50
```

**Hint:** Use a for loop from 1 to 10

---

## Problem 25: Vowel Counter (Medium)

Write a function `count_vowels` that takes a `text` parameter and counts the vowels.

**Expected Output:**
```python
count_vowels("Hello World")  # Vowels: 3
count_vowels("Python")       # Vowels: 1
```

**Hint:** Loop through characters, check if char in "aeiouAEIOU"

---

## Problem 26: List Average (Medium)

Define a function `calculate_average` that takes three numbers and prints their average.

**Expected Output:**
```python
calculate_average(10, 20, 30)  # Average: 20.0
calculate_average(5, 10, 15)   # Average: 10.0
```

**Hint:** Average = (num1 + num2 + num3) / 3

---

## Problem 27: Maximum of Three (Easy)

Create a function `find_max` that takes three numbers and prints the largest.

**Expected Output:**
```python
find_max(10, 25, 15)  # Maximum: 25
find_max(50, 20, 40)  # Maximum: 50
```

**Hint:** Use max() function or if-elif-else

---

## Problem 28: Palindrome Checker (Hard)

Write a function `is_palindrome` that takes a `word` parameter and checks if it's a palindrome.

**Expected Output:**
```python
is_palindrome("radar")   # "radar" is a palindrome
is_palindrome("python")  # "python" is not a palindrome
```

**Hint:** Compare word with word[::-1]

---

## Problem 29: Leap Year Checker (Medium)

Define a function `check_leap_year` that takes a `year` parameter.

**Expected Output:**
```python
check_leap_year(2024)  # 2024 is a leap year
check_leap_year(2023)  # 2023 is not a leap year
```

**Hint:** Divisible by 4 AND (not divisible by 100 OR divisible by 400)

---

## Problem 30: Prime Number Checker (Hard)

Create a function `check_prime` that takes a `number` parameter and determines if it's prime.

**Expected Output:**
```python
check_prime(17)  # 17 is a prime number
check_prime(18)  # 18 is not a prime number
```

**Hint:** Check for divisors from 2 to sqrt(number)

---

## Key Concepts

### Parameter vs Argument

```python
def greet(name):  # 'name' is a PARAMETER
    print(f"Hello, {name}")

greet("Alice")  # "Alice" is an ARGUMENT
```

- **Parameter**: Variable in function definition (placeholder)
- **Argument**: Actual value passed when calling (real data)

### Multiple Parameters

```python
def function_name(param1, param2, param3):
    # Use parameters in function body
    pass

function_name(arg1, arg2, arg3)  # Arguments match parameters by position
```

### Parameter Order Matters

```python
def subtract(a, b):
    print(a - b)

subtract(10, 3)  # Output: 7
subtract(3, 10)  # Output: -7 (different result!)
```

**The order in which you pass arguments matters!**

### Why Use Parameters?

1. **Flexibility**: Same function works with different data
2. **Reusability**: Don't repeat code for different inputs
3. **Maintainability**: Update logic in one place
4. **Testability**: Test function with various inputs

### Without Parameters (Limited)

```python
def greet_alice():
    print("Hello, Alice!")

def greet_bob():
    print("Hello, Bob!")

def greet_charlie():
    print("Hello, Charlie!")

# Need separate function for each person!
```

### With Parameters (Flexible)

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Charlie")

# One function for everyone!
```

### Best Practices

1. **Descriptive Parameter Names**: Use `name` not `n`, `price` not `p`
2. **Logical Order**: Put related parameters together
3. **Reasonable Count**: Too many parameters (5+) can be confusing
4. **Consistent Types**: Document what type each parameter expects
5. **Clear Purpose**: Each parameter should have a clear role

### Common Mistakes

1. **Wrong Number of Arguments**:
   ```python
   def add(a, b):
       print(a + b)

   add(5)  # TypeError: missing 1 required positional argument
   ```

2. **Wrong Order**:
   ```python
   def divide(numerator, denominator):
       print(numerator / denominator)

   divide(5, 10)  # 0.5 (correct)
   divide(10, 5)  # 2.0 (swapped!)
   ```

3. **Undefined Parameters**:
   ```python
   def greet(name):
       print(f"Hello, {age}")  # Error! 'age' not defined
   ```

4. **Missing Arguments**:
   ```python
   def introduce(name, age):
       print(f"{name} is {age}")

   introduce("Alice")  # TypeError: missing 1 argument
   ```

### Real-World Applications

1. **Web Forms**: Functions process user input (name, email, password)
2. **Calculators**: Functions perform operations on any numbers
3. **Games**: Functions handle player actions with different parameters
4. **Data Processing**: Functions transform data of any type
5. **Validation**: Functions check various inputs against rules

### Practice Tips

1. **Start Simple**: Begin with one or two parameters
2. **Test Thoroughly**: Call function with different arguments
3. **Use Print Debugging**: Print parameters inside function to see values
4. **Experiment**: Try different data types as arguments
5. **Read Errors**: Error messages tell you what's wrong
6. **Document**: Add comments explaining what each parameter is for
