# Editorials: Defining Reusable Functions in Python

## Problem 1: Simple Greeting Function

**Problem:** Define a function named `greet` that prints "Hello, World!" when called.

**Solution:**
```python
def greet():
    print("Hello, World!")

# Call the function
greet()
```

**Output:**
```
Hello, World!
```

**Explanation:**
- `def greet():` - Defines a function named `greet` with no parameters
- The colon `:` marks the start of the function body
- `print("Hello, World!")` - Function body, indented 4 spaces
- `greet()` - Calls the function, executing the code inside
- Parentheses `()` are required even with no parameters

**Key Concept:** Basic function definition and calling syntax.

---

## Problem 2: Print Separator

**Problem:** Create a function `print_separator` that prints a line of 30 dashes.

**Solution:**
```python
def print_separator():
    print('-' * 30)

print_separator()
```

**Output:**
```
------------------------------
```

**Explanation:**
- String multiplication: `'-' * 30` creates a string with 30 dashes
- Function encapsulates this reusable separator
- Can be called multiple times without repeating code

**Key Concept:** Functions make reusable components for common tasks.

---

## Problem 3: Welcome Message

**Problem:** Write a function `welcome` that prints a welcome message.

**Solution:**
```python
def welcome():
    print("Welcome to Python Programming!")
    print("Let's learn functions together!")

welcome()
```

**Output:**
```
Welcome to Python Programming!
Let's learn functions together!
```

**Explanation:**
- Functions can contain multiple statements
- Each statement executes in order when function is called
- All statements must be indented at the same level

**Key Concept:** Functions can execute multiple lines of code.

---

## Problem 4: Display Menu

**Problem:** Create a function `show_menu` that displays a simple menu.

**Solution:**
```python
def show_menu():
    print("=== MENU ===")
    print("1. Start")
    print("2. Settings")
    print("3. Exit")

show_menu()
```

**Output:**
```
=== MENU ===
1. Start
2. Settings
3. Exit
```

**Explanation:**
- Organizes related print statements into a single function
- Makes code more readable and maintainable
- Menu can be displayed anywhere by calling `show_menu()`

**Key Concept:** Functions group related operations together.

---

## Problem 5: Calculate Circle Area

**Problem:** Define a function that calculates and prints the area of a circle with radius 5.

**Solution:**
```python
def circle_area():
    radius = 5
    pi = 3.14159
    area = pi * radius * radius
    print(f"Area: {area}")

circle_area()
```

**Output:**
```
Area: 78.53975
```

**Explanation:**
- Variables defined inside function (radius, pi, area) are local
- Calculation: π × r² = 3.14159 × 5² = 78.53975
- f-string formats the output nicely

**Key Concept:** Functions can perform calculations with local variables.

---

## Problem 6: Print Countdown

**Problem:** Create a function that prints countdown from 10 to 1, then "Go!".

**Solution:**
```python
def countdown():
    for i in range(10, 0, -1):
        print(i, end=' ')
    print("\nGo!")

countdown()
```

**Output:**
```
10 9 8 7 6 5 4 3 2 1
Go!
```

**Explanation:**
- `range(10, 0, -1)` generates 10, 9, 8, ..., 1
- `end=' '` prints numbers on same line with spaces
- `\n` in second print creates new line before "Go!"
- Function can contain loops and control structures

**Key Concept:** Functions can include loops and complex logic.

---

## Problem 7: Temperature Converter

**Problem:** Write a function that converts 25°C to Fahrenheit.

**Solution:**
```python
def celsius_to_fahrenheit():
    celsius = 25
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")

celsius_to_fahrenheit()
```

**Output:**
```
25°C is equal to 77.0°F
```

**Explanation:**
- Formula: F = (C × 9/5) + 32
- Calculation: (25 × 9/5) + 32 = 45 + 32 = 77
- Function encapsulates conversion logic

**Key Concept:** Functions are perfect for conversions and calculations.

---

## Problem 8: Prime Checker

**Problem:** Define a function that checks if 17 is prime.

**Solution:**
```python
def is_prime_number():
    number = 17
    is_prime = True

    if number < 2:
        is_prime = False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

is_prime_number()
```

**Output:**
```
17 is a prime number
```

**Explanation:**
- Prime: number > 1 with no divisors except 1 and itself
- Check divisors from 2 to √17 ≈ 4.12
- Test 2, 3, 4: none divide 17 evenly
- Therefore 17 is prime
- Using `number ** 0.5` is efficient (only check up to square root)

**Key Concept:** Functions can implement algorithms and validation logic.

---

## Problem 9: Fibonacci Sequence

**Problem:** Create a function that prints first 10 Fibonacci numbers.

**Solution:**
```python
def print_fibonacci():
    a, b = 0, 1
    count = 0

    while count < 10:
        print(a, end=' ')
        a, b = b, a + b
        count += 1

print_fibonacci()
```

**Output:**
```
0 1 1 2 3 5 8 13 21 34
```

**Explanation:**
- Start with a=0, b=1
- Print a, then update: a becomes b, b becomes a+b
- Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
- Each number is sum of previous two
- Multiple assignment `a, b = b, a + b` swaps efficiently

**Key Concept:** Functions can generate sequences and patterns.

---

## Problem 10: Pattern Printer

**Problem:** Write a function that prints a right triangle with 5 rows.

**Solution:**
```python
def print_triangle():
    for row in range(1, 6):
        for col in range(row):
            print('*', end=' ')
        print()

print_triangle()
```

**Output:**
```
*
* *
* * *
* * * *
* * * * *
```

**Explanation:**
- Outer loop: 5 rows (1 through 5)
- Inner loop: prints row number of stars
- Row 1: 1 star, Row 2: 2 stars, etc.
- `print()` after inner loop creates new line

**Key Concept:** Functions can contain nested loops for patterns.

---

## Problem 11: Even Number Counter

**Problem:** Count even numbers in range 1 to 20.

**Solution:**
```python
def count_evens():
    count = 0
    for num in range(1, 21):
        if num % 2 == 0:
            count += 1
    print(f"Count of even numbers: {count}")

count_evens()
```

**Output:**
```
Count of even numbers: 10
```

**Explanation:**
- Range 1-20 contains: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
- That's 10 even numbers
- Counter increments when `num % 2 == 0`

**Key Concept:** Functions can accumulate and report statistics.

---

## Problem 12: List Statistics

**Problem:** Print sum, average, min, and max of a list.

**Solution:**
```python
def list_stats():
    numbers = [10, 20, 30, 40, 50]
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)

    print(f"Sum: {total}")
    print(f"Average: {average}")
    print(f"Min: {minimum}")
    print(f"Max: {maximum}")

list_stats()
```

**Output:**
```
Sum: 150
Average: 30.0
Min: 10
Max: 50
```

**Explanation:**
- `sum()` adds all elements: 10+20+30+40+50 = 150
- Average: 150 / 5 = 30.0
- `min()` finds smallest: 10
- `max()` finds largest: 50
- Built-in functions make statistics easy

**Key Concept:** Functions can use built-in functions for data analysis.

---

## Problem 13: Multiplication Table

**Problem:** Print multiplication table for 7.

**Solution:**
```python
def times_table():
    number = 7
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

times_table()
```

**Output:**
```
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

**Explanation:**
- Loop from 1 to 10
- Multiply 7 by each number
- Format output for readability
- Classic function use case

**Key Concept:** Functions are ideal for repetitive calculations.

---

## Problem 14: Password Validator

**Problem:** Validate if password meets criteria.

**Solution:**
```python
def validate_password():
    password = "Secure123"

    has_length = len(password) >= 8
    has_letters = any(char.isalpha() for char in password)
    has_numbers = any(char.isdigit() for char in password)

    if has_length and has_letters and has_numbers:
        print("Password is valid")
    else:
        print("Password is invalid")

validate_password()
```

**Output:**
```
Password is valid
```

**Explanation:**
- Length check: "Secure123" has 9 characters (>= 8) ✓
- Letter check: Contains S,e,c,u,r,e ✓
- Number check: Contains 1,2,3 ✓
- All conditions met, password is valid
- `any()` checks if at least one element is True

**Key Concept:** Functions can implement validation rules.

---

## Problem 15: Grade Calculator

**Problem:** Determine letter grade for score 85.

**Solution:**
```python
def calculate_grade():
    score = 85

    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print(f"Score {score} is grade: {grade}")

calculate_grade()
```

**Output:**
```
Score 85 is grade: B
```

**Explanation:**
- 85 is not >= 90, so not A
- 85 is >= 80, so grade is B
- elif chain stops at first True condition
- Function encapsulates grading logic

**Key Concept:** Functions handle conditional logic and decision-making.

---

## Problem 16: Array Reverser

**Problem:** Reverse and print a list.

**Solution:**
```python
def reverse_list():
    original = [1, 2, 3, 4, 5]
    reversed_list = original[::-1]

    print(f"Original: {original}")
    print(f"Reversed: {reversed_list}")

reverse_list()
```

**Output:**
```
Original: [1, 2, 3, 4, 5]
Reversed: [5, 4, 3, 2, 1]
```

**Explanation:**
- `[::-1]` is slice notation for reversing
- Creates new list, doesn't modify original
- Clean, readable syntax
- Alternative: `list(reversed(original))`

**Key Concept:** Functions can manipulate data structures.

---

## Problem 17: Factorial Calculator

**Problem:** Calculate factorial of 5.

**Solution:**
```python
def factorial():
    n = 5
    result = 1

    for i in range(1, n + 1):
        result *= i

    print(f"{n}! = {result}")

factorial()
```

**Output:**
```
5! = 120
```

**Explanation:**
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- Start with result = 1
- Multiply by each number from 1 to 5
- result becomes: 1 → 1 → 2 → 6 → 24 → 120

**Key Concept:** Functions implement mathematical operations.

---

## Problem 18: Common Elements Finder

**Problem:** Find common elements between two lists.

**Solution:**
```python
def find_common():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    common = []

    for item in list1:
        if item in list2:
            common.append(item)

    print(f"Common elements: {common}")

find_common()
```

**Output:**
```
Common elements: [4, 5]
```

**Explanation:**
- Check each element of list1 against list2
- 4 is in both lists → add to common
- 5 is in both lists → add to common
- Result: [4, 5]
- Alternative: `list(set(list1) & set(list2))`

**Key Concept:** Functions can find relationships between data sets.

---

## Problem 19: String Reverser

**Problem:** Reverse a string.

**Solution:**
```python
def reverse_string():
    original = "Python"
    reversed_str = original[::-1]

    print(f"Original: {original}")
    print(f"Reversed: {reversed_str}")

reverse_string()
```

**Output:**
```
Original: Python
Reversed: nohtyP
```

**Explanation:**
- Slicing `[::-1]` works on strings too
- P-y-t-h-o-n becomes n-o-h-t-y-P
- Non-destructive operation

**Key Concept:** Functions work with various data types.

---

## Problem 20: Leap Year Checker

**Problem:** Check if 2024 is a leap year.

**Solution:**
```python
def is_leap_year():
    year = 2024

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

is_leap_year()
```

**Output:**
```
2024 is a leap year
```

**Explanation:**
- Leap year rules:
  1. Divisible by 4: 2024 % 4 == 0 ✓
  2. NOT divisible by 100 OR divisible by 400
  3. 2024 % 100 = 24 (not 0), so condition 1 is met
- Therefore 2024 is a leap year
- Complex logic encapsulated in function

**Key Concept:** Functions handle complex conditional logic.

---

## Problem 21: Vowel Counter

**Problem:** Count vowels in "Education".

**Solution:**
```python
def count_vowels():
    word = "Education"
    vowels = "aeiouAEIOU"
    count = 0

    for char in word:
        if char in vowels:
            count += 1

    print(f"Number of vowels: {count}")

count_vowels()
```

**Output:**
```
Number of vowels: 5
```

**Explanation:**
- "Education" contains: E, u, a, i, o
- That's 5 vowels
- Loop checks each character
- Case-insensitive by including both cases in vowels string

**Key Concept:** Functions process text and count patterns.

---

## Problem 22: List Duplicates

**Problem:** Find duplicate elements in a list.

**Solution:**
```python
def find_duplicates():
    numbers = [1, 2, 3, 2, 4, 5, 1]
    seen = set()
    duplicates = []

    for num in numbers:
        if num in seen:
            if num not in duplicates:
                duplicates.append(num)
        else:
            seen.add(num)

    print(f"Duplicates: {duplicates}")

find_duplicates()
```

**Output:**
```
Duplicates: [2, 1]
```

**Explanation:**
- Track seen numbers in a set
- When number already in seen, it's a duplicate
- Avoid adding same duplicate twice
- Order of finding: 2, then 1

**Key Concept:** Functions use data structures to track state.

---

## Problem 23: Perfect Number

**Problem:** Check if 28 is a perfect number.

**Solution:**
```python
def is_perfect():
    number = 28
    divisors = []

    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)

    total = sum(divisors)

    print(f"Divisors: {', '.join(map(str, divisors))}")
    print(f"Sum: {total}")

    if total == number:
        print(f"{number} is a perfect number")
    else:
        print(f"{number} is not a perfect number")

is_perfect()
```

**Output:**
```
Divisors: 1, 2, 4, 7, 14
Sum: 28
28 is a perfect number
```

**Explanation:**
- Divisors of 28: 1, 2, 4, 7, 14
- Sum: 1 + 2 + 4 + 7 + 14 = 28
- Sum equals the number, so it's perfect
- Perfect numbers are rare (6, 28, 496, 8128...)

**Key Concept:** Functions implement number theory algorithms.

---

## Problem 24: Matrix Sum

**Problem:** Calculate sum of all elements in a matrix.

**Solution:**
```python
def matrix_sum():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    total = 0
    for row in matrix:
        for element in row:
            total += element

    print(f"Matrix sum: {total}")

matrix_sum()
```

**Output:**
```
Matrix sum: 45
```

**Explanation:**
- Nested loops iterate through all elements
- Sum: 1+2+3+4+5+6+7+8+9 = 45
- Works for any size matrix

**Key Concept:** Functions handle multi-dimensional data.

---

## Problem 25: GCD Calculator

**Problem:** Find GCD of 48 and 18.

**Solution:**
```python
def gcd():
    a, b = 48, 18

    while b != 0:
        a, b = b, a % b

    print(f"GCD of 48 and 18 is: {a}")

gcd()
```

**Output:**
```
GCD of 48 and 18 is: 6
```

**Explanation:**
- Euclidean algorithm:
  - a=48, b=18: 48 % 18 = 12 → a=18, b=12
  - a=18, b=12: 18 % 12 = 6 → a=12, b=6
  - a=12, b=6: 12 % 6 = 0 → a=6, b=0
  - b=0, so GCD = 6
- Efficient algorithm, works for any pair

**Key Concept:** Functions implement classic algorithms.

---

## Problem 26: Palindrome Checker

**Problem:** Check if "madam" is a palindrome.

**Solution:**
```python
def is_palindrome():
    word = "madam"
    reversed_word = word[::-1]

    if word == reversed_word:
        print(f'"{word}" is a palindrome')
    else:
        print(f'"{word}" is not a palindrome')

is_palindrome()
```

**Output:**
```
"madam" is a palindrome
```

**Explanation:**
- "madam" reversed is "madam"
- They're equal, so it's a palindrome
- Works for any word or phrase
- Case-sensitive version shown

**Key Concept:** Functions validate text properties.

---

## Problem 27: Sum of Squares

**Problem:** Calculate sum of squares from 1 to 10.

**Solution:**
```python
def sum_of_squares():
    total = 0
    for i in range(1, 11):
        total += i ** 2

    print(f"Sum of squares from 1 to 10: {total}")

sum_of_squares()
```

**Output:**
```
Sum of squares from 1 to 10: 385
```

**Explanation:**
- 1² + 2² + 3² + ... + 10²
- 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100 = 385
- Formula: n(n+1)(2n+1)/6 = 10(11)(21)/6 = 385

**Key Concept:** Functions compute mathematical series.

---

## Problem 28: Binary Converter

**Problem:** Convert 42 to binary.

**Solution:**
```python
def to_binary():
    decimal = 42
    binary = bin(decimal)[2:]  # Remove '0b' prefix

    print(f"{decimal} in binary is: {binary}")

to_binary()
```

**Output:**
```
42 in binary is: 101010
```

**Explanation:**
- `bin()` converts to binary with '0b' prefix
- [2:] slices off '0b', keeping just digits
- 42 = 32 + 8 + 2 = 2⁵ + 2³ + 2¹ = 101010₂

**Key Concept:** Functions perform number system conversions.

---

## Problem 29: Armstrong Number

**Problem:** Check if 153 is an Armstrong number.

**Solution:**
```python
def is_armstrong():
    number = 153
    digits = [int(d) for d in str(number)]
    sum_of_cubes = sum(d ** 3 for d in digits)

    print(f"1³ + 5³ + 3³ = {sum_of_cubes}")

    if sum_of_cubes == number:
        print(f"{number} is an Armstrong number")
    else:
        print(f"{number} is not an Armstrong number")

is_armstrong()
```

**Output:**
```
1³ + 5³ + 3³ = 153
153 is an Armstrong number
```

**Explanation:**
- Extract digits: 1, 5, 3
- Cube each: 1³=1, 5³=125, 3³=27
- Sum: 1 + 125 + 27 = 153
- Equals original, so it's Armstrong
- Also called narcissistic numbers

**Key Concept:** Functions decompose numbers and check properties.

---

## Problem 30: Sort Three Numbers

**Problem:** Sort three numbers.

**Solution:**
```python
def sort_three():
    numbers = [45, 12, 67]
    sorted_numbers = sorted(numbers)

    print(f"Sorted: {', '.join(map(str, sorted_numbers))}")

sort_three()
```

**Output:**
```
Sorted: 12, 45, 67
```

**Explanation:**
- `sorted()` returns new sorted list
- Original: [45, 12, 67]
- Sorted: [12, 45, 67]
- `map(str, ...)` converts numbers to strings for joining
- `', '.join()` creates comma-separated output

**Key Concept:** Functions leverage built-in functions for clean solutions.

---

## Summary

### Key Patterns Demonstrated

1. **Simple Actions**: Functions that print or display
2. **Calculations**: Mathematical operations and formulas
3. **Validation**: Checking conditions and rules
4. **Data Processing**: Working with lists and strings
5. **Algorithms**: Classic computer science algorithms
6. **Pattern Generation**: Loops and formatting
7. **Text Analysis**: Counting, searching, validating

### Function Benefits Shown

- **Reusability**: Write once, call many times
- **Organization**: Group related code
- **Abstraction**: Hide implementation details
- **Testing**: Isolate and verify functionality
- **Maintainability**: Update in one place

### Best Practices Illustrated

- Descriptive function names
- Single responsibility
- Clear, simple logic
- Proper indentation
- Meaningful variable names
- Efficient algorithms
