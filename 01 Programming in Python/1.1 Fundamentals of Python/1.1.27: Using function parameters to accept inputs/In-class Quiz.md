# Post-class Quiz: Using Function Parameters to Accept Inputs

## Question 1

What is the difference between a parameter and an argument?

A) They are the same thing
B) Parameter is in the function definition, argument is the value passed when calling
C) Parameter is used in Python, argument is used in other languages
D) Argument is in the function definition, parameter is the value passed when calling

**Answer: B) Parameter is in the function definition, argument is the value passed when calling**

**Explanation:** Parameters are variables listed in the function definition (placeholders), while arguments are the actual values passed to the function when it's called. For example:
```python
def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}")

greet("Alice")  # "Alice" is an argument
```
The parameter `name` is defined in the function header, and the argument "Alice" is passed when calling the function.

---

## Question 2

What will this code output?

```python
def add(x, y):
    print(x + y)

add(3, 5)
```

A) `x + y`
B) `8`
C) `35`
D) Error

**Answer: B) `8`**

**Explanation:** The function `add` takes two parameters `x` and `y`. When called with arguments 3 and 5, `x` becomes 3 and `y` becomes 5. The expression `x + y` evaluates to 3 + 5 = 8, which is then printed. Python performs mathematical addition, not string concatenation, because both values are numbers.

---

## Question 3

How many parameters does this function have?

```python
def calculate(length, width, height):
    volume = length * width * height
    print(volume)
```

A) 1
B) 2
C) 3
D) 4

**Answer: C) 3**

**Explanation:** The function `calculate` has three parameters: `length`, `width`, and `height`. Parameters are the variables listed in the parentheses of the function definition, separated by commas. The variable `volume` is not a parameter - it's a local variable created inside the function.

---

## Question 4

What happens if you call a function with fewer arguments than it has parameters?

A) Python uses default values
B) Missing parameters become None
C) TypeError is raised
D) Function runs with missing values as 0

**Answer: C) TypeError is raised**

**Explanation:** If a function expects a certain number of parameters and you call it with fewer arguments, Python raises a TypeError. For example:
```python
def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")

greet("Alice")  # TypeError: missing 1 required positional argument: 'last_name'
```
You must provide all required arguments unless the function has default parameter values (covered in a later lesson).

---

## Question 5

In this function call, what is the value of parameter `b`?

```python
def subtract(a, b):
    print(a - b)

subtract(10, 3)
```

A) 10
B) 3
C) 7
D) -7

**Answer: B) 3**

**Explanation:** Arguments are matched to parameters by position. The first argument (10) is assigned to the first parameter `a`, and the second argument (3) is assigned to the second parameter `b`. So `a` = 10 and `b` = 3. The function then calculates 10 - 3 = 7.

---

## Question 6

What will this code print?

```python
def multiply(num1, num2):
    result = num1 * num2
    print(result)

multiply(4, 5)
multiply(2, 8)
```

A) `20 16`
B) `20` on one line, `16` on the next
C) `45 28`
D) Error

**Answer: B) `20` on one line, `16` on the next**

**Explanation:** The function is called twice:
- First call: `multiply(4, 5)` → 4 × 5 = 20 (printed)
- Second call: `multiply(2, 8)` → 2 × 8 = 16 (printed)

Each `print()` statement outputs on a new line by default, so the output is:
```
20
16
```

---

## Question 7

Which is the correct way to define a function with two parameters?

A) `def my_function(param1 param2):`
B) `def my_function[param1, param2]:`
C) `def my_function(param1, param2):`
D) `def my_function{param1, param2}:`

**Answer: C) `def my_function(param1, param2):`**

**Explanation:** Parameters must be:
- Enclosed in parentheses `()` (not brackets or braces)
- Separated by commas
- Followed by a colon `:`

Option A is missing the comma, options B and D use wrong brackets. Only option C has the correct syntax.

---

## Question 8

What makes this function call incorrect?

```python
def calculate_area(length, width):
    area = length * width
    print(area)

calculate_area(5)  # Only one argument!
```

A) Wrong function name
B) Missing required argument
C) Too many arguments
D) Wrong data type

**Answer: B) Missing required argument**

**Explanation:** The function `calculate_area` expects two parameters (`length` and `width`), but the call only provides one argument (5). Python will raise a TypeError:
```
TypeError: calculate_area() missing 1 required positional argument: 'width'
```
You must provide values for all parameters unless they have default values.

---

## Question 9

Can parameters have the same name as variables outside the function?

A) No, this causes a name conflict error
B) Yes, parameters are local to the function
C) Only if the outside variable is global
D) Only if they have different data types

**Answer: B) Yes, parameters are local to the function**

**Explanation:** Parameters are local variables that only exist within the function scope. They can have the same name as variables outside the function without conflict:
```python
name = "Alice"  # Variable outside function

def greet(name):  # Parameter with same name
    print(f"Hello, {name}")

greet("Bob")  # Prints "Hello, Bob"
print(name)  # Still "Alice"
```
The parameter `name` inside the function is separate from the `name` variable outside.

---

## Question 10

What is true about parameter order?

A) Order doesn't matter
B) Arguments must match parameter positions
C) Python automatically sorts parameters alphabetically
D) You can pass arguments in any order

**Answer: B) Arguments must match parameter positions**

**Explanation:** When calling a function with positional arguments, order is crucial. The first argument goes to the first parameter, second to second, etc:
```python
def divide(numerator, denominator):
    print(numerator / denominator)

divide(10, 2)  # 10 / 2 = 5.0
divide(2, 10)  # 2 / 10 = 0.2 (different result!)
```
Swapping argument order changes which parameter receives which value, potentially changing the result completely.

---

## Question 11

What will this code output?

```python
def repeat_text(text, count):
    print(text * count)

repeat_text("Hi", 3)
```

A) `Hi 3`
B) `HiHiHi`
C) `Hi Hi Hi`
D) Error

**Answer: B) `HiHiHi`**

**Explanation:** When you multiply a string by an integer in Python, the string is repeated that many times. So `"Hi" * 3` produces `"HiHiHi"` (no spaces between repetitions). If the function were `print(text, count)` instead, it would print `Hi 3` with a space.

---

## Question 12

Which parameter name follows best practices?

A) `x`
B) `num`
C) `user_age`
D) `UserAge`

**Answer: C) `user_age`**

**Explanation:** Best practices for parameter names:
- Use descriptive names that explain what the parameter represents
- Use snake_case (lowercase with underscores)
- Avoid single letters unless in mathematical contexts
- Don't use PascalCase (reserved for class names)

`user_age` clearly describes the parameter and follows snake_case convention. `x` and `num` are too vague, and `UserAge` uses wrong capitalization.

---

## Question 13

Can parameters be different data types in the same function?

A) No, all parameters must be the same type
B) Yes, parameters can be any type
C) Only if you declare the types
D) Only numbers and strings

**Answer: B) Yes, parameters can be any type**

**Explanation:** Python is dynamically typed, so parameters can accept any data type. A function can have parameters of different types:
```python
def introduce(name, age, is_student):  # string, int, bool
    print(f"{name} is {age} years old")
    print(f"Student: {is_student}")

introduce("Alice", 25, True)
```
Here, `name` is a string, `age` is an integer, and `is_student` is a boolean.

---

## Question 14

What happens when you pass more arguments than parameters?

A) Extra arguments are ignored
B) TypeError is raised
C) Function uses only the first arguments
D) Extra arguments are stored in a list

**Answer: B) TypeError is raised**

**Explanation:** If you provide more arguments than the function has parameters, Python raises a TypeError:
```python
def add(a, b):
    print(a + b)

add(1, 2, 3)  # TypeError: add() takes 2 positional arguments but 3 were given
```
The function expects exactly 2 arguments, but 3 were provided. Later, you'll learn about *args which allows variable numbers of arguments.

---

## Question 15

What makes a function with parameters reusable?

A) It can work with different input values
B) It saves memory
C) It runs faster
D) It requires less code to write

**Answer: A) It can work with different input values**

**Explanation:** Parameters make functions reusable by allowing them to operate on different data:
```python
def square(number):
    print(number ** 2)

square(5)   # Works with 5
square(10)  # Works with 10
square(7)   # Works with 7
```
Instead of writing separate functions for each number, one parameterized function handles all cases. This is the key benefit of parameters - they make functions flexible and reusable across different contexts.

---

## Summary

### Key Concepts Tested:

1. **Parameter vs Argument**: Definition vs actual value
2. **Function Syntax**: Correct parameter definition
3. **Positional Matching**: Arguments match parameters by position
4. **Error Handling**: TypeError for wrong number of arguments
5. **Data Types**: Parameters can be any type
6. **Order Sensitivity**: Position matters for positional arguments
7. **Local Scope**: Parameters are local to the function
8. **Best Practices**: Descriptive snake_case names
9. **Reusability**: Parameters enable flexible, reusable functions
10. **Multiple Parameters**: Functions can have many parameters

### Common Patterns:

```python
# Single parameter
def greet(name):
    print(f"Hello, {name}!")

# Multiple parameters (same type)
def add(a, b):
    return a + b

# Multiple parameters (different types)
def register(username, age, email):
    print(f"User: {username}, Age: {age}, Email: {email}")

# Parameters in calculations
def circle_area(radius):
    return 3.14159 * radius ** 2

# Parameters in conditionals
def check_adult(age):
    if age >= 18:
        return "Adult"
    return "Minor"
```

### Error Scenarios:

```python
def example(a, b, c):
    pass

# Too few arguments
example(1, 2)  # TypeError: missing 1 required positional argument

# Too many arguments
example(1, 2, 3, 4)  # TypeError: takes 3 positional arguments but 4 were given

# Correct usage
example(1, 2, 3)  # Works!
```

### Best Practices:

1. **Descriptive Names**: `calculate_total()` not `calc()`
2. **Reasonable Count**: 2-4 parameters is ideal, 5+ gets complex
3. **Logical Order**: Group related parameters together
4. **Type Documentation**: Add comments explaining expected types
5. **Validation**: Check parameter values when necessary

### Quick Reference:

```python
# Definition
def function_name(parameter1, parameter2):
    # Use parameters in function body
    result = parameter1 + parameter2
    return result

# Calling
function_name(argument1, argument2)

# Example
def multiply(x, y):  # x, y are parameters
    return x * y

result = multiply(5, 3)  # 5, 3 are arguments
print(result)  # Output: 15
```

### Memory Aid:

**P**arameter = **P**laceholder in definition
**A**rgument = **A**ctual value when calling

Think: "Parameters WAIT for arguments to arrive"

---

### Real-World Analogy:

Think of a function like a coffee machine:
- **Parameters** are the settings: strength, size, milk/no milk
- **Arguments** are your choices: strong, large, with milk
- **Function body** is the process of making coffee
- **Output** is your customized coffee

Same machine (function), different settings (arguments), different results!
