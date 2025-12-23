# Editorials: Using Function Parameters to Accept Inputs

## Problem 1: Single Parameter Greeting

**Problem:** Write a function `greet_person` that takes one parameter `name` and prints "Hello, {name}!".

**Solution:**
```python
def greet_person(name):
    print(f"Hello, {name}!")

# Test cases
greet_person("Alice")
greet_person("Bob")
```

**Output:**
```
Hello, Alice!
Hello, Bob!
```

**Explanation:**
- The function is defined with one parameter `name`
- Inside the function, we use an f-string to insert the name into the greeting
- When called with "Alice", the parameter `name` holds the value "Alice"
- The function prints "Hello, Alice!"
- Same function works with different names by just changing the argument

**Key Concept:** Parameters make functions reusable with different inputs. One function definition works for any name.

---

## Problem 2: Two Number Addition

**Problem:** Define a function `add_two` that takes two parameters `num1` and `num2`, and prints their sum.

**Solution:**
```python
def add_two(num1, num2):
    sum_result = num1 + num2
    print(f"Sum: {sum_result}")

# Test cases
add_two(5, 3)
add_two(10, 20)
```

**Output:**
```
Sum: 8
Sum: 30
```

**Explanation:**
- Function takes two parameters: `num1` and `num2`
- First call: `num1` = 5, `num2` = 3, sum = 8
- Second call: `num1` = 10, `num2` = 20, sum = 30
- Same function performs addition on any two numbers
- Parameters are separated by commas in the definition

**Key Concept:** Multiple parameters allow functions to work with multiple inputs. Arguments are matched to parameters by position.

---

## Problem 3: Rectangle Area Calculator

**Problem:** Create a function `calculate_area` that accepts `length` and `width` parameters and prints the area.

**Solution:**
```python
def calculate_area(length, width):
    area = length * width
    print(f"Area: {area}")

# Test cases
calculate_area(5, 3)
calculate_area(10, 4)
```

**Output:**
```
Area: 15
Area: 40
```

**Explanation:**
- Parameters `length` and `width` represent rectangle dimensions
- Area is calculated by multiplying length × width
- First call: 5 × 3 = 15
- Second call: 10 × 4 = 40
- Descriptive parameter names make code self-documenting

**Key Concept:** Use meaningful parameter names that describe what data they hold.

---

## Problem 4: Three Number Multiplier

**Problem:** Write a function `multiply_three` that takes three parameters and prints their product.

**Solution:**
```python
def multiply_three(num1, num2, num3):
    product = num1 * num2 * num3
    print(f"Product: {product}")

# Test cases
multiply_three(2, 3, 4)
multiply_three(5, 5, 2)
```

**Output:**
```
Product: 24
Product: 50
```

**Explanation:**
- Function accepts three parameters
- First call: 2 × 3 × 4 = 24
- Second call: 5 × 5 × 2 = 50
- All three parameters are multiplied together
- You can have as many parameters as needed (though too many makes it complex)

**Key Concept:** Functions can accept multiple parameters. Each parameter is separated by a comma.

---

## Problem 5: Person Introduction

**Problem:** Define a function `introduce` that takes `name`, `age`, and `city` parameters and prints a full introduction.

**Solution:**
```python
def introduce(name, age, city):
    print(f"My name is {name}")
    print(f"I am {age} years old")
    print(f"I live in {city}")

# Test case
introduce("Alice", 25, "New York")
```

**Output:**
```
My name is Alice
I am 25 years old
I live in New York
```

**Explanation:**
- Three parameters hold different types of information
- `name` is a string, `age` is an integer, `city` is a string
- Multiple print statements can use the same parameters
- Parameters are accessible throughout the entire function body
- Order matters: first argument goes to `name`, second to `age`, third to `city`

**Key Concept:** Parameters can hold different types of data. Order of arguments must match order of parameters.

---

## Problem 6: Temperature Converter

**Problem:** Create a function `celsius_to_fahrenheit` that takes a temperature in Celsius and prints the Fahrenheit equivalent.

**Solution:**
```python
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

# Test cases
celsius_to_fahrenheit(0)
celsius_to_fahrenheit(100)
celsius_to_fahrenheit(25)
```

**Output:**
```
0°C = 32.0°F
100°C = 212.0°F
25°C = 77.0°F
```

**Explanation:**
- Parameter `celsius` holds the temperature to convert
- Formula: F = (C × 9/5) + 32
- 0°C = 32°F (freezing point of water)
- 100°C = 212°F (boiling point of water)
- 25°C = 77°F (room temperature)
- Parameters can be used in mathematical calculations

**Key Concept:** Parameters can be used in formulas and calculations inside the function.

---

## Problem 7: Circle Calculations

**Problem:** Write a function `circle_info` that takes `radius` as a parameter and prints both circumference and area.

**Solution:**
```python
def circle_info(radius):
    pi = 3.14159
    circumference = 2 * pi * radius
    area = pi * radius * radius
    print(f"Radius: {radius}")
    print(f"Circumference: {circumference}")
    print(f"Area: {area}")

# Test case
circle_info(5)
```

**Output:**
```
Radius: 5
Circumference: 31.4159
Area: 78.53975
```

**Explanation:**
- Single parameter `radius` is used in multiple calculations
- Circumference = 2πr = 2 × 3.14159 × 5 = 31.4159
- Area = πr² = 3.14159 × 5² = 78.53975
- One parameter can be reused multiple times in different formulas
- Local variable `pi` is combined with parameter `radius`

**Key Concept:** A single parameter can be used multiple times within the function.

---

## Problem 8: Power Calculator

**Problem:** Define a function `power` that takes `base` and `exponent` parameters and prints the result.

**Solution:**
```python
def power(base, exponent):
    result = base ** exponent
    print(f"{base}^{exponent} = {result}")

# Test cases
power(2, 3)
power(5, 2)
power(10, 0)
```

**Output:**
```
2^3 = 8
2^5 = 25
10^0 = 1
```

**Explanation:**
- `base` is the number to be multiplied
- `exponent` is how many times to multiply it
- Python's `**` operator calculates powers
- 2³ = 2 × 2 × 2 = 8
- 5² = 5 × 5 = 25
- 10⁰ = 1 (any number to power 0 is 1)

**Key Concept:** Parameters represent different roles in calculations (base vs exponent).

---

## Problem 9: Age Validator

**Problem:** Create a function `check_age` that takes `age` as a parameter and prints whether the person is a minor, adult, or senior.

**Solution:**
```python
def check_age(age):
    if age < 18:
        print("Minor (under 18)")
    elif age < 65:
        print("Adult (18-64)")
    else:
        print("Senior (65+)")

# Test cases
check_age(15)
check_age(25)
check_age(70)
```

**Output:**
```
Minor (under 18)
Adult (18-64)
Senior (65+)
```

**Explanation:**
- Parameter `age` is used in conditional statements
- If age < 18: Minor
- Else if age < 65: Adult
- Else: Senior
- Parameters work seamlessly with control flow (if/elif/else)
- Same function categorizes any age value

**Key Concept:** Parameters can be used in conditional logic to make decisions.

---

## Problem 10: Grade Calculator

**Problem:** Write a function `calculate_grade` that takes a `score` parameter and prints the letter grade.

**Solution:**
```python
def calculate_grade(score):
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

# Test cases
calculate_grade(95)
calculate_grade(85)
calculate_grade(75)
calculate_grade(65)
calculate_grade(55)
```

**Output:**
```
Grade: A
Grade: B
Grade: C
Grade: D
Grade: F
```

**Explanation:**
- Parameter `score` is compared against grade thresholds
- 90+ = A, 80-89 = B, 70-79 = C, 60-69 = D, below 60 = F
- Conditions are checked in order from highest to lowest
- First matching condition executes, others are skipped
- One function handles all possible scores

**Key Concept:** Parameters combined with if-elif-else create flexible decision-making functions.

---

## Problem 11: String Repeater

**Problem:** Define a function `repeat_string` that takes a `text` and `count` parameter, and prints the text repeated count times.

**Solution:**
```python
def repeat_string(text, count):
    repeated = text * count
    print(repeated)

# Test cases
repeat_string("Hello", 3)
repeat_string("*", 5)
```

**Output:**
```
HelloHelloHello
*****
```

**Explanation:**
- Two parameters: `text` (what to repeat) and `count` (how many times)
- String multiplication: "Hello" * 3 = "HelloHelloHello"
- "*" * 5 = "*****"
- Parameters can be different data types (string and integer)
- Both parameters work together to produce the result

**Key Concept:** Parameters of different types can work together in operations.

---

## Problem 12: Triangle Type Checker

**Problem:** Create a function `triangle_type` that takes three side lengths and prints the triangle type.

**Solution:**
```python
def triangle_type(side1, side2, side3):
    if side1 == side2 == side3:
        print("Equilateral triangle")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

# Test cases
triangle_type(5, 5, 5)
triangle_type(5, 5, 3)
triangle_type(3, 4, 5)
```

**Output:**
```
Equilateral triangle
Isosceles triangle
Scalene triangle
```

**Explanation:**
- Three parameters represent triangle sides
- Equilateral: all three sides equal (5, 5, 5)
- Isosceles: exactly two sides equal (5, 5, 3)
- Scalene: all sides different (3, 4, 5)
- Multiple comparisons using `==` and `or` operators
- Parameters are compared against each other

**Key Concept:** Parameters can be compared with each other to determine relationships.

---

## Problem 13: Discount Calculator

**Problem:** Write a function `apply_discount` that takes `price` and `discount_percent` and prints the final price.

**Solution:**
```python
def apply_discount(price, discount_percent):
    discount_amount = price * discount_percent / 100
    final_price = price - discount_amount
    print(f"Final price: ${final_price}")

# Test cases
apply_discount(100, 10)
apply_discount(250, 20)
apply_discount(80, 15)
```

**Output:**
```
Final price: $90.0
Final price: $200.0
Final price: $68.0
```

**Explanation:**
- `price` = original price, `discount_percent` = percentage off
- First: $100 with 10% off = $100 - $10 = $90
- Second: $250 with 20% off = $250 - $50 = $200
- Third: $80 with 15% off = $80 - $12 = $68
- Parameters used in multi-step calculation
- Both parameters contribute to the final result

**Key Concept:** Parameters can represent different aspects of a problem (amount and percentage).

---

## Problem 14: Even or Odd Checker

**Problem:** Define a function `check_even_odd` that takes a `number` parameter and prints whether it's even or odd.

**Solution:**
```python
def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

# Test cases
check_even_odd(4)
check_even_odd(7)
check_even_odd(10)
```

**Output:**
```
4 is even
7 is odd
10 is even
```

**Explanation:**
- Parameter `number` is tested using modulo operator
- Even numbers: remainder of division by 2 is 0
- Odd numbers: remainder of division by 2 is 1
- 4 % 2 = 0 (even)
- 7 % 2 = 1 (odd)
- 10 % 2 = 0 (even)

**Key Concept:** Parameters can be used with mathematical operators like modulo (%).

---

## Problem 15: BMI Calculator

**Problem:** Create a function `calculate_bmi` that takes `weight` (kg) and `height` (m) and prints the BMI with category.

**Solution:**
```python
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    print(f"BMI: {bmi:.2f}")

    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")

# Test case
calculate_bmi(70, 1.75)
```

**Output:**
```
BMI: 22.86
Category: Normal weight
```

**Explanation:**
- Two parameters: `weight` in kg, `height` in meters
- BMI = weight / height²
- 70 / (1.75²) = 70 / 3.0625 = 22.86
- BMI 22.86 falls in Normal weight category (18.5-24.9)
- Calculated value is then used in subsequent conditionals
- `.2f` formats BMI to 2 decimal places

**Key Concept:** Results calculated from parameters can be used in further logic.

---

## Problem 16: Count Down Timer

**Problem:** Write a function `countdown` that takes a `start` parameter and counts down to 1.

**Solution:**
```python
def countdown(start):
    for i in range(start, 0, -1):
        print(i, end=" ")
    print("Go!")

# Test case
countdown(5)
```

**Output:**
```
5 4 3 2 1 Go!
```

**Explanation:**
- Parameter `start` determines where countdown begins
- `range(start, 0, -1)` creates sequence: start, start-1, ..., 2, 1
- With start=5: range produces 5, 4, 3, 2, 1
- `end=" "` prints numbers on same line with spaces
- Final `print("Go!")` moves to new line and prints "Go!"
- Parameters can control loop ranges

**Key Concept:** Parameters can define loop boundaries and control iteration.

---

## Problem 17: Name Formatter

**Problem:** Define a function `format_name` that takes `first_name` and `last_name` and prints the full name in different formats.

**Solution:**
```python
def format_name(first_name, last_name):
    print(f"Full name: {first_name} {last_name}")
    print(f"Last, First: {last_name}, {first_name}")
    print(f"Initials: {first_name[0]}.{last_name[0]}.")

# Test case
format_name("John", "Doe")
```

**Output:**
```
Full name: John Doe
Last, First: Doe, John
Initials: J.D.
```

**Explanation:**
- Two string parameters: `first_name` and `last_name`
- Format 1: Simple concatenation with space
- Format 2: Reversed order with comma separator
- Format 3: String indexing [0] gets first character of each name
- Same data displayed in multiple ways
- Parameters can be sliced and combined differently

**Key Concept:** String parameters can be manipulated with indexing, slicing, and concatenation.

---

## Problem 18: Simple Interest Calculator

**Problem:** Create a function `simple_interest` that takes `principal`, `rate`, and `time` parameters.

**Solution:**
```python
def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    total = principal + interest
    print(f"Principal: ${principal}")
    print(f"Interest: ${interest}")
    print(f"Total: ${total}")

# Test case
simple_interest(1000, 5, 2)
```

**Output:**
```
Principal: $1000
Interest: $100.0
Total: $1100.0
```

**Explanation:**
- Three parameters for the interest formula
- Interest = (P × R × T) / 100
- P = $1000, R = 5%, T = 2 years
- Interest = (1000 × 5 × 2) / 100 = $100
- Total = Principal + Interest = $1100
- All three parameters used together in one formula

**Key Concept:** Multiple parameters can be combined in mathematical formulas.

---

## Problem 19: Password Strength Checker

**Problem:** Write a function `check_password_strength` that takes a `password` parameter and checks various criteria.

**Solution:**
```python
def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)

    print(f"Length: {length} ({'OK' if length >= 8 else 'Too short'})")
    print(f"Has uppercase: {'Yes' if has_upper else 'No'}")
    print(f"Has lowercase: {'Yes' if has_lower else 'No'}")
    print(f"Has numbers: {'Yes' if has_digit else 'No'}")

    if length >= 8 and has_upper and has_lower and has_digit:
        print("Strength: Strong")
    elif length >= 6:
        print("Strength: Weak")
    else:
        print("Strength: Very Weak")

# Test case
check_password_strength("Abc123")
```

**Output:**
```
Length: 6 (Too short)
Has uppercase: Yes
Has lowercase: Yes
Has numbers: Yes
Strength: Weak
```

**Explanation:**
- Parameter `password` is analyzed for multiple criteria
- Length: 6 characters (minimum should be 8)
- Has uppercase: Yes (A)
- Has lowercase: Yes (b, c)
- Has numbers: Yes (1, 2, 3)
- Overall: Weak (has variety but too short)
- String methods: `.isupper()`, `.islower()`, `.isdigit()`
- `any()` function checks if at least one character meets criteria

**Key Concept:** String parameters can be analyzed using built-in string methods.

---

## Problem 20: Fizz Buzz Function

**Problem:** Define a function `fizz_buzz_single` that takes a `number` and prints Fizz, Buzz, FizzBuzz, or the number.

**Solution:**
```python
def fizz_buzz_single(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Test cases
fizz_buzz_single(3)
fizz_buzz_single(5)
fizz_buzz_single(15)
fizz_buzz_single(7)
```

**Output:**
```
Fizz
Buzz
FizzBuzz
7
```

**Explanation:**
- Parameter `number` is tested against multiple conditions
- 3: divisible by 3 → Fizz
- 5: divisible by 5 → Buzz
- 15: divisible by both 3 and 5 → FizzBuzz
- 7: not divisible by 3 or 5 → print the number itself
- Order matters: check both conditions first
- Classic programming problem using conditionals

**Key Concept:** Multiple conditions can be checked in priority order using if-elif-else.

---

## Problem 21: Time Converter

**Problem:** Create a function `convert_seconds` that takes total seconds and prints hours, minutes, and seconds.

**Solution:**
```python
def convert_seconds(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    print(f"{hours} hour(s), {minutes} minute(s), {seconds} second(s)")

# Test case
convert_seconds(3665)
```

**Output:**
```
1 hour(s), 1 minute(s), 5 second(s)
```

**Explanation:**
- Parameter: 3665 total seconds
- Hours: 3665 // 3600 = 1 hour
- Remaining: 3665 % 3600 = 65 seconds
- Minutes: 65 // 60 = 1 minute
- Seconds: 65 % 60 = 5 seconds
- Integer division (//) and modulo (%) extract time components
- One parameter broken down into multiple components

**Key Concept:** Parameters can be decomposed into multiple values using mathematical operations.

---

## Problem 22: Range Checker

**Problem:** Write a function `in_range` that takes `number`, `min_val`, and `max_val` and checks if number is in range.

**Solution:**
```python
def in_range(number, min_val, max_val):
    if min_val <= number <= max_val:
        print(f"{number} is in range [{min_val}, {max_val}]")
    else:
        print(f"{number} is out of range [{min_val}, {max_val}]")

# Test cases
in_range(50, 1, 100)
in_range(150, 1, 100)
```

**Output:**
```
50 is in range [1, 100]
150 is out of range [1, 100]
```

**Explanation:**
- Three parameters: value to check and range boundaries
- Python's chained comparison: `min_val <= number <= max_val`
- 50 is between 1 and 100 → in range
- 150 is greater than 100 → out of range
- All three parameters used in one comparison
- Descriptive parameter names make logic clear

**Key Concept:** Multiple parameters can define boundaries for validation.

---

## Problem 23: String Length Categories

**Problem:** Define a function `categorize_length` that takes a `text` parameter and categorizes its length.

**Solution:**
```python
def categorize_length(text):
    length = len(text)
    if length <= 5:
        print("Short (1-5 chars)")
    elif length <= 15:
        print("Medium (6-15 chars)")
    else:
        print("Long (16+ chars)")

# Test cases
categorize_length("Hi")
categorize_length("Hello World")
categorize_length("This is a very long sentence")
```

**Output:**
```
Short (1-5 chars)
Medium (6-15 chars)
Long (16+ chars)
```

**Explanation:**
- Parameter `text` is a string
- `len(text)` calculates string length
- "Hi": 2 characters → Short
- "Hello World": 11 characters → Medium
- "This is a very long sentence": 28 characters → Long
- Length determines category through conditionals
- String parameter used with `len()` function

**Key Concept:** String parameters can be measured and categorized using `len()`.

---

## Problem 24: Multiplication Table Row

**Problem:** Create a function `times_table_row` that takes a `number` and prints one row of its multiplication table.

**Solution:**
```python
def times_table_row(number):
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

# Test case
times_table_row(5)
```

**Output:**
```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

**Explanation:**
- Parameter `number` is the base for multiplication table
- Loop from 1 to 10
- Each iteration: `number` × i
- Parameter used repeatedly in loop
- 5 × 1 = 5, 5 × 2 = 10, ..., 5 × 10 = 50
- One parameter generates 10 lines of output

**Key Concept:** Parameters can be used repeatedly inside loops.

---

## Problem 25: Vowel Counter

**Problem:** Write a function `count_vowels` that takes a `text` parameter and counts the vowels.

**Solution:**
```python
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    print(f"Vowels: {count}")

# Test cases
count_vowels("Hello World")
count_vowels("Python")
```

**Output:**
```
Vowels: 3
Vowels: 1
```

**Explanation:**
- Parameter `text` is iterated character by character
- "Hello World": e, o, o = 3 vowels
- "Python": o = 1 vowel
- Loop through each character with `for char in text`
- Check if character is in vowel string
- Counter incremented for each vowel found
- String parameter used in iteration

**Key Concept:** String parameters can be iterated character by character using for loops.

---

## Problem 26: List Average

**Problem:** Define a function `calculate_average` that takes three numbers and prints their average.

**Solution:**
```python
def calculate_average(num1, num2, num3):
    total = num1 + num2 + num3
    average = total / 3
    print(f"Average: {average}")

# Test cases
calculate_average(10, 20, 30)
calculate_average(5, 10, 15)
```

**Output:**
```
Average: 20.0
Average: 10.0
```

**Explanation:**
- Three numeric parameters
- First: (10 + 20 + 30) / 3 = 60 / 3 = 20.0
- Second: (5 + 10 + 15) / 3 = 30 / 3 = 10.0
- All parameters added, then divided by count
- Result is a float (division always produces float in Python 3)

**Key Concept:** All parameters can be combined in a single calculation.

---

## Problem 27: Maximum of Three

**Problem:** Create a function `find_max` that takes three numbers and prints the largest.

**Solution:**
```python
def find_max(num1, num2, num3):
    maximum = max(num1, num2, num3)
    print(f"Maximum: {maximum}")

# Test cases
find_max(10, 25, 15)
find_max(50, 20, 40)
```

**Output:**
```
Maximum: 25
Maximum: 50
```

**Explanation:**
- Three parameters to compare
- Built-in `max()` function finds largest value
- Alternative manual approach:
  ```python
  if num1 >= num2 and num1 >= num3:
      maximum = num1
  elif num2 >= num3:
      maximum = num2
  else:
      maximum = num3
  ```
- `max()` is simpler and clearer
- All three parameters passed to one function

**Key Concept:** Multiple parameters can be passed to built-in functions like `max()`.

---

## Problem 28: Palindrome Checker

**Problem:** Write a function `is_palindrome` that takes a `word` parameter and checks if it's a palindrome.

**Solution:**
```python
def is_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        print(f'"{word}" is a palindrome')
    else:
        print(f'"{word}" is not a palindrome')

# Test cases
is_palindrome("radar")
is_palindrome("python")
```

**Output:**
```
"radar" is a palindrome
"python" is not a palindrome
```

**Explanation:**
- Parameter `word` is reversed using slicing [::-1]
- "radar" reversed = "radar" (same → palindrome)
- "python" reversed = "nohtyp" (different → not palindrome)
- String slicing creates reversed copy
- Original and reversed compared for equality
- String parameter manipulated with advanced slicing

**Key Concept:** String parameters can be reversed and manipulated using Python slicing.

---

## Problem 29: Leap Year Checker

**Problem:** Define a function `check_leap_year` that takes a `year` parameter.

**Solution:**
```python
def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

# Test cases
check_leap_year(2024)
check_leap_year(2023)
```

**Output:**
```
2024 is a leap year
2023 is not a leap year
```

**Explanation:**
- Parameter `year` tested against leap year rules
- Rule: divisible by 4 AND (not divisible by 100 OR divisible by 400)
- 2024: divisible by 4, not by 100 → leap year
- 2023: not divisible by 4 → not leap year
- Complex logical condition with `and`, `or`, `not`
- Parentheses group conditions correctly

**Key Concept:** Parameters can be used in complex boolean expressions with multiple operators.

---

## Problem 30: Prime Number Checker

**Problem:** Create a function `check_prime` that takes a `number` parameter and determines if it's prime.

**Solution:**
```python
def check_prime(number):
    if number < 2:
        print(f"{number} is not a prime number")
        return

    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

# Test cases
check_prime(17)
check_prime(18)
```

**Output:**
```
17 is a prime number
18 is not a prime number
```

**Explanation:**
- Parameter `number` checked for prime property
- Prime: only divisible by 1 and itself
- Numbers < 2 are not prime
- Check divisors from 2 to √number (optimization)
- 17: no divisors found → prime
- 18: divisible by 2, 3, 6, 9 → not prime
- Loop breaks early if divisor found (efficiency)
- `number ** 0.5` calculates square root

**Key Concept:** Parameters can be used in algorithmic logic with loops and early exits.

---

## Summary of Key Concepts

### 1. Parameter Definition
```python
def function_name(parameter1, parameter2):
    # Use parameters here
    pass
```

### 2. Parameter vs Argument
- **Parameter**: Variable in function definition
- **Argument**: Actual value passed when calling

### 3. Multiple Parameters
- Separated by commas
- Order matters when calling
- Can be different data types

### 4. Parameter Usage
- In calculations
- In conditionals
- In loops
- In string operations
- With built-in functions

### 5. Best Practices
- Use descriptive names
- Keep count reasonable (< 5 ideal)
- Document expected types
- Validate inputs when needed

### 6. Common Patterns
```python
# Single parameter
def greet(name):
    print(f"Hello, {name}")

# Multiple parameters
def add(a, b):
    return a + b

# Parameters in loops
def repeat(text, count):
    for i in range(count):
        print(text)

# Parameters in conditionals
def categorize(age):
    if age < 18:
        return "Minor"
    else:
        return "Adult"
```
