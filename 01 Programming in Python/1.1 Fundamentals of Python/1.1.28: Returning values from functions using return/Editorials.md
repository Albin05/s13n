# Editorials: Returning Values from Functions Using Return

## Problem 1: Simple Return

**Problem:** Write a function `double` that takes a number and returns double its value.

**Solution:**
```python
def double(number):
    return number * 2

# Test cases
result = double(5)
print(result)  # 10

result = double(12)
print(result)  # 24
```

**Output:**
```
10
24
```

**Explanation:**
- The function takes one parameter `number`
- It calculates `number * 2` and returns the result
- The `return` statement sends the value back to the caller
- First call: `double(5)` returns 10, which is stored in `result` and printed
- Second call: `double(12)` returns 24
- The returned value can be stored in a variable for later use

**Key Concept:** `return` sends data back from the function to wherever it was called.

---

## Problem 2: Add Two Numbers with Return

**Problem:** Create a function `add_numbers` that takes two parameters and returns their sum.

**Solution:**
```python
def add_numbers(a, b):
    return a + b

# Test cases
sum1 = add_numbers(5, 3)
print(sum1)  # 8

sum2 = add_numbers(10, 20)
print(sum2)  # 30
```

**Output:**
```
8
30
```

**Explanation:**
- Function takes two parameters: `a` and `b`
- Returns the sum of both parameters
- First call: `add_numbers(5, 3)` returns 8
- Second call: `add_numbers(10, 20)` returns 30
- Unlike `print()`, `return` lets us capture and use the result
- We can store the returned value in variables (`sum1`, `sum2`)

**Key Concept:** Functions with `return` are more flexible than those that just print - you can use the results in other calculations.

---

## Problem 3: Return String

**Problem:** Define a function `make_greeting` that takes a `name` parameter and returns a greeting string.

**Solution:**
```python
def make_greeting(name):
    return f"Hello, {name}!"

# Test cases
msg = make_greeting("Alice")
print(msg)  # "Hello, Alice!"

msg = make_greeting("Bob")
print(msg)  # "Hello, Bob!"
```

**Output:**
```
Hello, Alice!
Hello, Bob!
```

**Explanation:**
- Function takes `name` parameter
- Creates a formatted greeting string using f-string
- Returns the string (not printing it)
- Returned string is stored in `msg` variable
- We can then print it, modify it, or use it elsewhere
- Return value is type `str` (string)

**Key Concept:** Functions can return any data type - numbers, strings, booleans, lists, etc.

---

## Problem 4: Return Boolean

**Problem:** Write a function `is_even` that takes a number and returns True if even, False if odd.

**Solution:**
```python
def is_even(number):
    return number % 2 == 0

# Test cases
print(is_even(4))   # True
print(is_even(7))   # False
print(is_even(10))  # True
```

**Output:**
```
True
False
True
```

**Explanation:**
- Function checks if number is divisible by 2
- `number % 2 == 0` evaluates to True or False
- This boolean value is returned directly
- 4 % 2 == 0 → True (even)
- 7 % 2 == 1 (remainder) → 7 % 2 == 0 → False (odd)
- 10 % 2 == 0 → True (even)
- Returned booleans can be used in if statements or stored

**Key Concept:** Returning booleans is common for validation and checking functions.

---

## Problem 5: Calculate Area with Return

**Problem:** Create a function `calculate_rectangle_area` that takes length and width, and returns the area.

**Solution:**
```python
def calculate_rectangle_area(length, width):
    return length * width

# Test cases
area1 = calculate_rectangle_area(5, 3)
print(f"Area: {area1}")  # Area: 15

area2 = calculate_rectangle_area(10, 8)
print(f"Area: {area2}")  # Area: 80
```

**Output:**
```
Area: 15
Area: 80
```

**Explanation:**
- Function multiplies length by width
- Returns the calculated area
- First call: 5 × 3 = 15
- Second call: 10 × 8 = 80
- Returned values can be used in further calculations:
  ```python
  total_area = area1 + area2  # 15 + 80 = 95
  ```
- This is more flexible than just printing the result

**Key Concept:** Calculation functions should return results for maximum reusability.

---

## Problem 6: Return Maximum of Two

**Problem:** Write a function `get_max` that takes two numbers and returns the larger one.

**Solution:**
```python
def get_max(a, b):
    if a > b:
        return a
    else:
        return b

# Alternative using built-in function
def get_max_alt(a, b):
    return max(a, b)

# Test cases
print(get_max(10, 25))  # 25
print(get_max(50, 30))  # 50
print(get_max(15, 15))  # 15
```

**Output:**
```
25
50
15
```

**Explanation:**
- Function compares two numbers
- Returns whichever is larger
- If `a > b`, return `a`, otherwise return `b`
- When equal (15, 15), the else branch runs, returning `b`
- Can also use Python's built-in `max()` function
- Multiple return statements: only ONE executes per call

**Key Concept:** Functions can have multiple `return` statements - the first one reached exits the function.

---

## Problem 7: Return Grade

**Problem:** Define a function `calculate_grade` that takes a score and returns the letter grade.

**Solution:**
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

# Test cases
print(calculate_grade(95))  # "A"
print(calculate_grade(85))  # "B"
print(calculate_grade(75))  # "C"
print(calculate_grade(65))  # "D"
print(calculate_grade(55))  # "F"
```

**Output:**
```
A
B
C
D
F
```

**Explanation:**
- Function evaluates score against multiple thresholds
- Returns appropriate grade letter
- Once a condition is met, that `return` executes and function exits
- Subsequent conditions are not checked
- Score 95: first condition (>= 90) is True → returns "A"
- Score 85: second condition (>= 80) is True → returns "B"
- Each call returns a string that can be stored or printed

**Key Concept:** Multiple return statements with conditions create branching logic.

---

## Problem 8: Multiple Return Paths

**Problem:** Create a function `classify_number` that takes a number and returns "Positive", "Negative", or "Zero".

**Solution:**
```python
def classify_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Test cases
print(classify_number(5))    # "Positive"
print(classify_number(-3))   # "Negative"
print(classify_number(0))    # "Zero"
```

**Output:**
```
Positive
Negative
Zero
```

**Explanation:**
- Three possible return paths
- num = 5: first condition true → returns "Positive"
- num = -3: second condition true → returns "Negative"
- num = 0: both false, else executes → returns "Zero"
- Exactly ONE return executes per function call
- Clear categorization of input into three cases

**Key Concept:** Different execution paths can return different values based on conditions.

---

## Problem 9: Return Multiple Values

**Problem:** Write a function `get_circle_info` that takes radius and returns both circumference and area.

**Solution:**
```python
def get_circle_info(radius):
    pi = 3.14159
    circumference = 2 * pi * radius
    area = pi * radius * radius
    return circumference, area

# Test case
circ, area = get_circle_info(5)
print(f"Circumference: {circ}, Area: {area}")
```

**Output:**
```
Circumference: 31.4159, Area: 78.53975
```

**Explanation:**
- Function calculates two values
- Returns them as a tuple: `return circumference, area`
- Tuple packing: multiple values separated by comma
- Tuple unpacking: `circ, area = get_circle_info(5)`
- Both values are received and stored simultaneously
- Circumference: 2 × π × 5 = 31.4159
- Area: π × 5² = 78.53975

**Key Concept:** Python can return multiple values using tuples.

---

## Problem 10: Temperature Converter with Return

**Problem:** Define a function `celsius_to_fahrenheit` that converts Celsius to Fahrenheit and returns the result.

**Solution:**
```python
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Test cases
f1 = celsius_to_fahrenheit(0)
print(f"{f1}°F")  # 32.0°F

f2 = celsius_to_fahrenheit(100)
print(f"{f2}°F")  # 212.0°F
```

**Output:**
```
32.0°F
212.0°F
```

**Explanation:**
- Function applies conversion formula
- Formula: F = (C × 9/5) + 32
- 0°C: (0 × 1.8) + 32 = 32°F (freezing point)
- 100°C: (100 × 1.8) + 32 = 212°F (boiling point)
- Returned value can be used in comparisons, stored, or displayed
- Could simplify to: `return (celsius * 9/5) + 32` (no intermediate variable)

**Key Concept:** Return calculated values to make functions pure and testable.

---

## Problem 11: Return from Loop

**Problem:** Create a function `find_first_even` that takes a list and returns the first even number found.

**Solution:**
```python
def find_first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num  # Exit immediately when found
    return None  # If no even number found

# Test case
nums = [1, 3, 5, 8, 9, 10]
result = find_first_even(nums)
print(result)  # 8
```

**Output:**
```
8
```

**Explanation:**
- Function loops through list
- When first even number is found, immediately returns it
- `return` inside loop exits the entire function
- Sequence: checks 1 (odd), 3 (odd), 5 (odd), 8 (even) → returns 8
- 9 and 10 are never checked (function already exited)
- If no even number found, loop completes and returns None
- This is called "early return" - exits as soon as answer is found

**Key Concept:** `return` inside a loop exits the function immediately, stopping iteration.

---

## Problem 12: Return None Explicitly

**Problem:** Write a function `check_positive` that returns the number if positive, otherwise returns None.

**Solution:**
```python
def check_positive(number):
    if number > 0:
        return number
    else:
        return None

# Test cases
print(check_positive(5))   # 5
print(check_positive(-3))  # None
print(check_positive(0))   # None
```

**Output:**
```
5
None
None
```

**Explanation:**
- Function validates if number is positive
- If positive (> 0), returns the number itself
- If not positive, explicitly returns None
- check_positive(5): 5 > 0 → returns 5
- check_positive(-3): -3 not > 0 → returns None
- check_positive(0): 0 not > 0 → returns None
- None is Python's way of representing "no value" or "null"
- Can simplify: `return None` can be omitted (implicit)

**Key Concept:** Returning None indicates failure, absence, or invalid result.

---

## Problem 13: Calculate Discount with Return

**Problem:** Define a function `apply_discount` that takes price and discount percentage, returns final price.

**Solution:**
```python
def apply_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price

# Test cases
final = apply_discount(100, 20)
print(f"${final}")  # $80.0

final = apply_discount(250, 10)
print(f"${final}")  # $225.0
```

**Output:**
```
$80.0
$225.0
```

**Explanation:**
- Calculates discount amount from percentage
- Subtracts discount from original price
- Returns final price
- First: $100 with 20% off → $100 - $20 = $80
- Second: $250 with 10% off → $250 - $25 = $225
- Could be simplified to one line:
  ```python
  return price * (1 - discount_percent / 100)
  ```
- Returned value can be used in more calculations (e.g., adding tax)

**Key Concept:** Return intermediate results for use in multi-step calculations.

---

## Problem 14: Return Early

**Problem:** Create a function `validate_age` that returns "Valid" for ages 18-100, otherwise returns an error message.

**Solution:**
```python
def validate_age(age):
    if age < 18:
        return "Too young"
    if age > 100:
        return "Invalid age"
    return "Valid"

# Test cases
print(validate_age(25))   # "Valid"
print(validate_age(15))   # "Too young"
print(validate_age(120))  # "Invalid age"
```

**Output:**
```
Valid
Too young
Invalid age
```

**Explanation:**
- Early return pattern: check error cases first
- If age < 18, immediately return "Too young" and exit
- If age > 100, immediately return "Invalid age" and exit
- If neither condition met, age is valid → return "Valid"
- Benefits: avoids nested if-else, clearer logic
- Age 25: passes both checks → returns "Valid"
- Age 15: fails first check → returns "Too young"
- Age 120: passes first, fails second → returns "Invalid age"

**Key Concept:** Early returns for error cases make code cleaner and easier to read.

---

## Problem 15: Power Function with Return

**Problem:** Write a function `power` that takes base and exponent, returns the result.

**Solution:**
```python
def power(base, exponent):
    return base ** exponent

# Test cases
print(power(2, 3))   # 8
print(power(5, 2))   # 25
print(power(10, 0))  # 1
```

**Output:**
```
8
25
1
```

**Explanation:**
- Simple one-line function
- Uses Python's exponentiation operator `**`
- 2³ = 2 × 2 × 2 = 8
- 5² = 5 × 5 = 25
- 10⁰ = 1 (any number to power 0 is 1)
- Returns calculated power
- Could also implement with loop for integer exponents

**Key Concept:** Simple functions can return expressions directly without intermediate variables.

---

## Problem 16: Return String Length

**Problem:** Define a function `get_length` that takes a string and returns its length.

**Solution:**
```python
def get_length(text):
    return len(text)

# Test cases
print(get_length("hello"))  # 5
print(get_length("Python"))  # 6
```

**Output:**
```
5
6
```

**Explanation:**
- Uses built-in `len()` function
- Returns the length as an integer
- "hello" has 5 characters
- "Python" has 6 characters
- Returned integer can be used in comparisons:
  ```python
  if get_length(password) < 8:
      print("Password too short")
  ```

**Key Concept:** Wrapper functions can return values from built-in functions.

---

## Problem 17: Return List Element

**Problem:** Create a function `get_first_element` that takes a list and returns the first element, or None if empty.

**Solution:**
```python
def get_first_element(lst):
    if len(lst) == 0:
        return None
    return lst[0]

# Alternative using truthiness
def get_first_element_alt(lst):
    if not lst:  # Empty lists are falsy
        return None
    return lst[0]

# Test cases
print(get_first_element([1, 2, 3]))  # 1
print(get_first_element([]))         # None
```

**Output:**
```
1
None
```

**Explanation:**
- Checks if list is empty first (defensive programming)
- If empty, returns None (avoiding IndexError)
- If not empty, returns first element lst[0]
- [1, 2, 3]: not empty → returns 1
- []: empty → returns None
- Alternative uses list truthiness: empty lists evaluate to False
- Prevents crashes when accessing non-existent elements

**Key Concept:** Return None for edge cases where normal return isn't possible.

---

## Problem 18: Calculate BMI with Return

**Problem:** Write a function `calculate_bmi` that takes weight (kg) and height (m), returns BMI and category.

**Solution:**
```python
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category

# Test case
bmi, category = calculate_bmi(70, 1.75)
print(f"BMI: {bmi:.2f}, Category: {category}")
```

**Output:**
```
BMI: 22.86, Category: Normal
```

**Explanation:**
- Calculates BMI using formula: weight / height²
- Determines category based on BMI value
- Returns both values as tuple
- 70 / (1.75²) = 70 / 3.0625 = 22.86
- BMI 22.86 falls in "Normal" range (18.5-24.9)
- Both values can be unpacked and used separately
- Returning multiple related values together is common pattern

**Key Concept:** Return tuples when function naturally produces multiple related values.

---

## Problem 19: Return Vowel Count

**Problem:** Define a function `count_vowels` that takes a string and returns the number of vowels.

**Solution:**
```python
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Test cases
count = count_vowels("Hello World")
print(f"Vowels: {count}")  # Vowels: 3

count = count_vowels("Python")
print(f"Vowels: {count}")  # Vowels: 1
```

**Output:**
```
Vowels: 3
Vowels: 1
```

**Explanation:**
- Loops through each character in string
- Checks if character is a vowel
- Increments counter for each vowel found
- "Hello World": e, o, o = 3 vowels
- "Python": o = 1 vowel
- Returns final count
- Alternative using list comprehension:
  ```python
  return sum(1 for char in text if char in "aeiouAEIOU")
  ```

**Key Concept:** Return accumulated results from loops.

---

## Problem 20: Return Factorial

**Problem:** Create a function `factorial` that takes a number and returns its factorial.

**Solution:**
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Test cases
print(factorial(5))  # 120
print(factorial(3))  # 6
print(factorial(0))  # 1
```

**Output:**
```
120
6
1
```

**Explanation:**
- Factorial: n! = n × (n-1) × (n-2) × ... × 1
- Special case: 0! = 1 and 1! = 1
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 3! = 3 × 2 × 1 = 6
- Uses loop to multiply numbers from 2 to n
- Returns accumulated product
- Could also use recursion

**Key Concept:** Mathematical operations often need to return calculated values.

---

## Problem 21: Return List of Squares

**Problem:** Write a function `get_squares` that takes a number n and returns a list of squares from 1 to n.

**Solution:**
```python
def get_squares(n):
    result = []
    for i in range(1, n + 1):
        result.append(i ** 2)
    return result

# Alternative using list comprehension
def get_squares_alt(n):
    return [i ** 2 for i in range(1, n + 1)]

# Test case
result = get_squares(5)
print(result)  # [1, 4, 9, 16, 25]
```

**Output:**
```
[1, 4, 9, 16, 25]
```

**Explanation:**
- Creates empty list to accumulate results
- Loops from 1 to n (inclusive)
- Calculates square of each number and adds to list
- 1² = 1, 2² = 4, 3² = 9, 4² = 16, 5² = 25
- Returns completed list
- List comprehension is more concise
- Returned list can be iterated, indexed, or modified

**Key Concept:** Return collections (lists, tuples, sets) built up in loops.

---

## Problem 22: Return Middle Element

**Problem:** Define a function `get_middle` that takes a list and returns the middle element.

**Solution:**
```python
def get_middle(lst):
    middle_index = len(lst) // 2
    return lst[middle_index]

# Test cases
print(get_middle([1, 2, 3, 4, 5]))  # 3
print(get_middle([10, 20, 30]))     # 20
```

**Output:**
```
3
20
```

**Explanation:**
- Finds middle index using integer division
- [1, 2, 3, 4, 5]: length 5, middle index 5 // 2 = 2, element at index 2 is 3
- [10, 20, 30]: length 3, middle index 3 // 2 = 1, element at index 1 is 20
- For even-length lists, returns the first of the two middle elements
- Note: Doesn't handle empty lists (would raise IndexError)
- Could add validation: `if not lst: return None`

**Key Concept:** Return specific elements from collections based on calculated indices.

---

## Problem 23: Return Absolute Value

**Problem:** Create a function `absolute_value` that takes a number and returns its absolute value.

**Solution:**
```python
def absolute_value(number):
    if number < 0:
        return -number
    else:
        return number

# Alternative
def absolute_value_alt(number):
    return abs(number)  # Using built-in

# Test cases
print(absolute_value(-5))   # 5
print(absolute_value(10))   # 10
print(absolute_value(-15))  # 15
```

**Output:**
```
5
10
15
```

**Explanation:**
- If number is negative, return its negation (makes it positive)
- If number is positive or zero, return as is
- -(-5) = 5 (negating negative gives positive)
- 10 is already positive → returns 10
- -(-15) = 15
- Python has built-in `abs()` function for this
- Demonstrates conditional return based on value

**Key Concept:** Simple transformations can return modified versions of input.

---

## Problem 24: Return Prime Check

**Problem:** Write a function `is_prime` that takes a number and returns True if prime, False otherwise.

**Solution:**
```python
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

# Test cases
print(is_prime(17))  # True
print(is_prime(18))  # False
print(is_prime(2))   # True
```

**Output:**
```
True
False
True
```

**Explanation:**
- Prime: number divisible only by 1 and itself
- Numbers < 2 are not prime → return False
- Check divisibility from 2 to √number (optimization)
- If any divisor found → return False immediately
- If loop completes without finding divisor → return True
- 17: no divisors from 2 to 4 → prime (True)
- 18: divisible by 2 → not prime (False)
- 2: no divisors to check → prime (True)

**Key Concept:** Boolean functions return True/False based on validation logic.

---

## Problem 25: Return Min and Max

**Problem:** Define a function `get_min_max` that takes three numbers and returns the smallest and largest.

**Solution:**
```python
def get_min_max(a, b, c):
    minimum = min(a, b, c)
    maximum = max(a, b, c)
    return minimum, maximum

# Test case
minimum, maximum = get_min_max(5, 10, 3)
print(f"Min: {minimum}, Max: {maximum}")  # Min: 3, Max: 10
```

**Output:**
```
Min: 3, Max: 10
```

**Explanation:**
- Uses built-in `min()` and `max()` functions
- min(5, 10, 3) = 3
- max(5, 10, 3) = 10
- Returns both as tuple
- Both values unpacked into separate variables
- Alternative manual approach:
  ```python
  minimum = a
  if b < minimum: minimum = b
  if c < minimum: minimum = c
  # Similar for maximum
  ```

**Key Concept:** Returning multiple related statistics together is convenient.

---

## Problem 26: Return Reversed String

**Problem:** Create a function `reverse_string` that takes a string and returns it reversed.

**Solution:**
```python
def reverse_string(text):
    return text[::-1]

# Test cases
print(reverse_string("hello"))   # "olleh"
print(reverse_string("Python"))  # "nohtyP"
```

**Output:**
```
olleh
nohtyP
```

**Explanation:**
- Uses Python's slice notation with step -1
- `[::-1]` reverses the string
- "hello" → "olleh"
- "Python" → "nohtyP"
- Alternative using loop:
  ```python
  result = ""
  for char in text:
      result = char + result
  return result
  ```
- Returns new reversed string, original unchanged

**Key Concept:** Return transformed versions of input data.

---

## Problem 27: Return Sum of List

**Problem:** Write a function `sum_list` that takes a list of numbers and returns their sum.

**Solution:**
```python
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Alternative
def sum_list_alt(numbers):
    return sum(numbers)  # Using built-in

# Test cases
total = sum_list([1, 2, 3, 4, 5])
print(total)  # 15

total = sum_list([10, 20, 30])
print(total)  # 60
```

**Output:**
```
15
60
```

**Explanation:**
- Accumulates sum in `total` variable
- Loops through all numbers, adding each to total
- [1, 2, 3, 4, 5]: 1 + 2 + 3 + 4 + 5 = 15
- [10, 20, 30]: 10 + 20 + 30 = 60
- Returns final sum
- Python's built-in `sum()` does this directly
- Returned value can be used in further calculations

**Key Concept:** Return aggregated results from processing collections.

---

## Problem 28: Return Leap Year Check

**Problem:** Define a function `is_leap_year` that takes a year and returns True if leap year, False otherwise.

**Solution:**
```python
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

# Alternative (one-line)
def is_leap_year_alt(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Test cases
print(is_leap_year(2024))  # True
print(is_leap_year(2023))  # False
print(is_leap_year(2000))  # True
```

**Output:**
```
True
False
True
```

**Explanation:**
- Leap year rules:
  1. Divisible by 400 → leap year (2000)
  2. Divisible by 100 (but not 400) → not leap year (1900)
  3. Divisible by 4 (but not 100) → leap year (2024)
  4. Otherwise → not leap year (2023)
- 2024: divisible by 4, not by 100 → True
- 2023: not divisible by 4 → False
- 2000: divisible by 400 → True
- Multiple return paths, early exits when rule matched

**Key Concept:** Complex logic can have multiple return points for different conditions.

---

## Problem 29: Return Fibonacci Number

**Problem:** Create a function `fibonacci` that takes n and returns the nth Fibonacci number.

**Solution:**
```python
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test cases
print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(5))  # 5
print(fibonacci(10)) # 55
```

**Output:**
```
0
1
5
55
```

**Explanation:**
- Fibonacci: each number is sum of previous two
- Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
- Base cases: fib(0) = 0, fib(1) = 1
- For n > 1, iterate calculating next Fibonacci number
- fib(5): 0, 1, 1, 2, 3, 5
- fib(10): continues to 55
- Uses two variables to track previous two numbers
- Returns final calculated value

**Key Concept:** Iterative algorithms build up result and return final value.

---

## Problem 30: Return Filtered List

**Problem:** Write a function `get_evens` that takes a list and returns a new list with only even numbers.

**Solution:**
```python
def get_evens(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

# Alternative using list comprehension
def get_evens_alt(numbers):
    return [num for num in numbers if num % 2 == 0]

# Test cases
result = get_evens([1, 2, 3, 4, 5, 6])
print(result)  # [2, 4, 6]

result = get_evens([1, 3, 5])
print(result)  # []
```

**Output:**
```
[2, 4, 6]
[]
```

**Explanation:**
- Creates new list to store even numbers
- Loops through input list
- Checks each number with modulo operator
- If even (num % 2 == 0), adds to result list
- [1, 2, 3, 4, 5, 6]: evens are 2, 4, 6
- [1, 3, 5]: no evens, returns empty list
- Returns filtered list
- List comprehension provides more concise syntax
- Original list is unchanged

**Key Concept:** Return new filtered/transformed collections rather than modifying originals.

---

## Summary of Key Concepts

### 1. Basic Return
```python
def function():
    return value  # Send value back
```

### 2. Return Exits Function
```python
def example():
    return "First"
    print("Never runs")  # Unreachable
```

### 3. Multiple Returns (One Executes)
```python
def check(x):
    if x > 0:
        return "Positive"
    return "Non-positive"
```

### 4. Return Multiple Values
```python
def stats():
    return 10, 20  # Returns tuple
a, b = stats()  # Unpack
```

### 5. Return None
```python
def no_return():
    print("Hello")
    # Implicitly returns None
```

### 6. Return in Loops
```python
def find(items, target):
    for item in items:
        if item == target:
            return item  # Exit immediately
    return None  # Not found
```

### 7. Early Return Pattern
```python
def validate(x):
    if x < 0:
        return "Error"
    # Main logic here
    return "Valid"
```
