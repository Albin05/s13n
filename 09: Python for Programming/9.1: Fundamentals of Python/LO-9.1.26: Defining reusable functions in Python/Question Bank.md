### **1. Simple Greeting Function**

Define a function named `greet` that prints "Hello, World!" when called.

**Expected Output:**
```
Hello, World!
```

**Hint:** Use `def` keyword to define the function, then call it by name with parentheses.

---

---

### **2. Print Separator**

Create a function `print_separator` that prints a line of 30 dashes.

**Expected Output:**
```
------------------------------
```

**Hint:** Use `print('-' * 30)` inside the function.

---

---

### **3. Welcome Message**

Write a function `welcome` that prints a welcome message with your name.

**Expected Output:**
```
Welcome to Python Programming!
Let's learn functions together!
```

**Hint:** Function can contain multiple print statements.

---

---

### **4. Display Menu**

Create a function `show_menu` that displays a simple menu with 3 options.

**Expected Output:**
```
=== MENU ===
1. Start
2. Settings
3. Exit
```

**Hint:** Use multiple print statements with formatted strings.

---

---

### **5. Calculate Circle Area**

Define a function `circle_area` that calculates and prints the area of a circle with radius 5. Use π = 3.14159.

**Expected Output:**
```
Area: 78.53975
```

**Hint:** Formula: area = π × r²

---

---

### **6. Print Countdown**

Create a function `countdown` that prints numbers from 10 down to 1, then prints "Go!".

**Expected Output:**
```
10 9 8 7 6 5 4 3 2 1
Go!
```

**Hint:** Use a for loop with range(10, 0, -1).

---

---

### **7. Temperature Converter**

Write a function `celsius_to_fahrenheit` that converts 25°C to Fahrenheit and prints the result.

**Expected Output:**
```
25°C is equal to 77.0°F
```

**Hint:** Formula: F = (C × 9/5) + 32

---

---

### **8. Prime Checker**

Define a function `is_prime_number` that checks if 17 is prime and prints the result.

**Expected Output:**
```
17 is a prime number
```

**Hint:** Loop from 2 to √17 and check for divisors.

---

---

### **9. Fibonacci Sequence**

Create a function `print_fibonacci` that prints the first 10 Fibonacci numbers.

**Expected Output:**
```
0 1 1 2 3 5 8 13 21 34
```

**Hint:** Start with 0 and 1, then each number is sum of previous two.

---

---

### **10. Pattern Printer**

Write a function `print_triangle` that prints a right triangle with 5 rows.

**Expected Output:**
```
*
* *
* * *
* * * *
* * * * *
```

**Hint:** Use nested loops inside the function.

---

---

### **11. Even Number Counter**

Define a function `count_evens` that counts and prints how many even numbers are in the range 1 to 20.

**Expected Output:**
```
Count of even numbers: 10
```

**Hint:** Use a counter in a loop, increment when number is even.

---

---

### **12. List Statistics**

Create a function `list_stats` that prints the sum, average, min, and max of the list `[10, 20, 30, 40, 50]`.

**Expected Output:**
```
Sum: 150
Average: 30.0
Min: 10
Max: 50
```

**Hint:** Use built-in functions sum(), min(), max(), and len().

---

---

### **13. Multiplication Table**

Write a function `times_table` that prints the multiplication table for number 7 (from 7×1 to 7×10).

**Expected Output:**
```
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

**Hint:** Use a loop from 1 to 10.

---

---

### **14. Password Validator**

Define a function `validate_password` that checks if "Secure123" meets these criteria:
- At least 8 characters
- Contains both letters and numbers

Print validation result.

**Expected Output:**
```
Password is valid
```

**Hint:** Use len(), str.isalpha(), str.isdigit() methods.

---

---

### **15. Grade Calculator**

Create a function `calculate_grade` that determines the letter grade for a score of 85.

Grade scale:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Below 60: F

**Expected Output:**
```
Score 85 is grade: B
```

**Hint:** Use if-elif-else statements.

---

---

### **16. Array Reverser**

Write a function `reverse_list` that reverses and prints the list `[1, 2, 3, 4, 5]`.

**Expected Output:**
```
Original: [1, 2, 3, 4, 5]
Reversed: [5, 4, 3, 2, 1]
```

**Hint:** Use slicing `[::-1]` or the reverse() method.

---

---

### **17. Factorial Calculator**

Define a function `factorial` that calculates and prints the factorial of 5.

**Expected Output:**
```
5! = 120
```

**Hint:** Factorial of n = n × (n-1) × (n-2) × ... × 1

---

---

### **18. Common Elements Finder**

Create a function `find_common` that finds and prints common elements between two lists:
- List 1: `[1, 2, 3, 4, 5]`
- List 2: `[4, 5, 6, 7, 8]`

**Expected Output:**
```
Common elements: [4, 5]
```

**Hint:** Use a loop or set intersection.

---

---

### **19. String Reverser**

Write a function `reverse_string` that reverses and prints the string "Python".

**Expected Output:**
```
Original: Python
Reversed: nohtyP
```

**Hint:** Use slicing `[::-1]`.

---

---

### **20. Leap Year Checker**

Define a function `is_leap_year` that checks if 2024 is a leap year.

Rules:
- Divisible by 4 AND (not divisible by 100 OR divisible by 400)

**Expected Output:**
```
2024 is a leap year
```

**Hint:** Use modulo operators and logical conditions.

---

---

### **21. Vowel Counter**

Create a function `count_vowels` that counts vowels in "Education".

**Expected Output:**
```
Number of vowels: 5
```

**Hint:** Loop through string, check if char is in "aeiouAEIOU".

---

---

### **22. List Duplicates**

Write a function `find_duplicates` that finds and prints duplicate elements in `[1, 2, 3, 2, 4, 5, 1]`.

**Expected Output:**
```
Duplicates: [1, 2]
```

**Hint:** Use a set to track seen elements.

---

---

### **23. Perfect Number**

Define a function `is_perfect` that checks if 28 is a perfect number (number equals sum of its proper divisors).

**Expected Output:**
```
28 is a perfect number
Divisors: 1, 2, 4, 7, 14
Sum: 28
```

**Hint:** Find all divisors except the number itself, sum them.

---

---

### **24. Matrix Sum**

Create a function `matrix_sum` that calculates the sum of all elements in:
```python
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```

**Expected Output:**
```
Matrix sum: 45
```

**Hint:** Use nested loops.

---

---

### **25. GCD Calculator**

Write a function `gcd` that finds the greatest common divisor of 48 and 18.

**Expected Output:**
```
GCD of 48 and 18 is: 6
```

**Hint:** Use Euclidean algorithm or loop through divisors.

---

---

### **26. Palindrome Checker**

Define a function `is_palindrome` that checks if "madam" is a palindrome.

**Expected Output:**
```
"madam" is a palindrome
```

**Hint:** Compare string with its reverse.

---

---

### **27. Sum of Squares**

Create a function `sum_of_squares` that calculates sum of squares from 1 to 10.

**Expected Output:**
```
Sum of squares from 1 to 10: 385
```

**Hint:** Sum of 1² + 2² + 3² + ... + 10²

---

---

### **28. Binary Converter**

Write a function `to_binary` that converts decimal 42 to binary and prints it.

**Expected Output:**
```
42 in binary is: 101010
```

**Hint:** Use bin() function or manual conversion.

---

---

### **29. Armstrong Number**

Define a function `is_armstrong` that checks if 153 is an Armstrong number (sum of cubes of digits equals the number).

**Expected Output:**
```
153 is an Armstrong number
1³ + 5³ + 3³ = 153
```

**Hint:** Extract each digit, cube it, sum all cubes.

---

---

### **30. Sort Three Numbers**

Create a function `sort_three` that sorts and prints three numbers: 45, 12, 67.

**Expected Output:**
```
Sorted: 12, 45, 67
```

**Hint:** Use comparison and swapping or list sorting.

---

## Key Concepts

### Function Definition Syntax

```python
def function_name():
    # Function body
    # Code to execute
    pass
```

### Basic Structure

1. **def keyword**: Declares a function
2. **Function name**: Follows naming conventions (lowercase, underscores)
3. **Parentheses ()**: Required even with no parameters
4. **Colon (:)**: Marks start of function body
5. **Indentation**: Function body must be indented
6. **Function call**: Use function_name() to execute

### Naming Conventions

- Use lowercase letters
- Separate words with underscores (snake_case)
- Use descriptive names
- Start with a letter (not number)
- Avoid Python keywords

**Good names:** `calculate_area`, `print_menu`, `check_prime`
**Bad names:** `func1`, `x`, `calculateArea` (camelCase)

### Why Use Functions?

1. **Reusability**: Write once, use many times
2. **Organization**: Break code into logical blocks
3. **Readability**: Clear, named operations
4. **Maintainability**: Update in one place
5. **Testing**: Test individual components
6. **Abstraction**: Hide complex details

### Function vs No Function

**Without Function:**
```python
# Calculate area - first time
radius1 = 5
area1 = 3.14159 * radius1 * radius1
print(area1)

# Calculate area - second time
radius2 = 10
area2 = 3.14159 * radius2 * radius2
print(area2)

# Repetitive code!
```

**With Function:**
```python
def calculate_area(radius):
    return 3.14159 * radius * radius

print(calculate_area(5))
print(calculate_area(10))
# Clean, reusable!
```

### Docstrings

```python
def greet():
    """Prints a greeting message."""
    print("Hello!")

def calculate_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius: The radius of the circle

    Returns:
        The area of the circle
    """
    return 3.14159 * radius * radius
```

### Common Patterns

```python
# Simple action
def print_header():
    print("=" * 40)
    print("   Welcome to My Program")
    print("=" * 40)

# Calculation
def calculate_bmi():
    weight = 70
    height = 1.75
    bmi = weight / (height ** 2)
    print(f"BMI: {bmi:.2f}")

# Data processing
def process_list():
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    average = total / len(numbers)
    print(f"Average: {average}")

# Validation
def validate_age():
    age = 25
    if age >= 18:
        print("Adult")
    else:
        print("Minor")
```

### Best Practices

1. **Single Responsibility**: One function, one task
2. **Descriptive Names**: Name should describe what it does
3. **Keep It Short**: Ideally under 20-30 lines
4. **Add Docstrings**: Document what function does
5. **Consistent Style**: Follow PEP 8 guidelines
6. **Test Functions**: Verify they work correctly
7. **Avoid Global Variables**: Keep data inside function
8. **Group Related Functions**: Organize by functionality

### Common Mistakes

1. **Forgetting parentheses** in function call
2. **Misspelling function name**
3. **Calling before defining**
4. **Incorrect indentation**
5. **Missing colon after function name**
6. **Using reserved keywords** as function names

### Real-World Applications

1. **Web Development**: Handle requests, render pages
2. **Data Analysis**: Process datasets, calculate statistics
3. **Games**: Handle player actions, update game state
4. **Automation**: Repeat tasks, process files
5. **APIs**: Expose functionality to other programs
6. **Testing**: Unit tests for code verification
7. **GUI Applications**: Handle button clicks, events
8. **Scientific Computing**: Complex calculations, simulations

## Practice Tips

1. **Start Simple**: Begin with functions that just print
2. **Build Complexity**: Gradually add logic
3. **Test Often**: Call function to verify it works
4. **Read Error Messages**: Understand what went wrong
5. **Use Print Debugging**: Add prints to trace execution
6. **Refactor Code**: Convert repetitive code to functions
7. **Write Docstrings**: Document as you code
8. **Follow Conventions**: Consistent naming and style

---

