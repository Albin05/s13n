# Lecture Notes: Use Function Parameters

## Introduction

Function parameters introduce **flexibility** and **generalization** to functions. They transform functions from **single-purpose tools** into **versatile, reusable components** that work with any data.

### Why Parameters Exist

**The rigidity problem**: Functions without parameters do one specific thing with hardcoded values. Need to greet different people? Need 100 different functions!
**Parameters solution**: One function, infinite uses. Pass different data each time.

**Historical perspective**: Early programming languages didn't have sophisticated parameter passing. FORTRAN (1954) introduced subroutine parameters, revolutionizing code reuse. Modern languages (including Python) have refined this into elegant, powerful systems.

### Real-World Analogy

Parameters are like **slots in a coffee machine**:
- **Coffee type slot**: Parameter for type (espresso, latte, cappuccino)
- **Size slot**: Parameter for size (small, medium, large)
- **Sugar slot**: Parameter for sweetness (none, 1 spoon, 2 spoons)
- **One machine**: Works with any combination of inputs!

Or like **a form**:
- **Name field**: Parameter
- **Age field**: Parameter
- **Address field**: Parameter
- **Same form**, different people fill in different values

### The Power of Abstraction

Parameters let you write **generic**, **reusable** code:
```python
# One function for ALL calculations!
def calculate(a, b, operation):
    # Works for any numbers, any operation
```

This is **parametric polymorphism** - one function, many uses through different inputs.

### Information Flow

Parameters are **inputs** to functions - the data they need to do their job:
- **Function**: A machine that processes data
- **Parameters**: The raw materials/ingredients
- **Processing**: The function's code
- **Result**: Output (we'll learn about `return` soon!)

---

<div align="center">

![Python Function Parameters and Arguments](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.1/LO-9.1.27.jpg)

*Function parameters define named input slots that receive argument values when the function is called, enabling flexible and reusable code*

</div>

---

## Function Parameters

Parameters allow functions to accept input values.


### Basic Syntax

```python
def function_name(parameter):
    # Use parameter in function body
```

## Examples

### Example 1: Single Parameter

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!
greet("Bob")    # Hello, Bob!
```

### Example 2: Multiple Parameters

```python
def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)   # 5 + 3 = 8
add_numbers(10, 20) # 10 + 20 = 30
```

### Example 3: Calculate Area

```python
def rectangle_area(length, width):
    area = length * width
    print(f"Area: {area} square units")

rectangle_area(5, 3)  # Area: 15 square units
rectangle_area(10, 4) # Area: 40 square units
```

## Parameters vs Arguments

```python
def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}")

greet("Alice")  # "Alice" is an argument
```

- **Parameter**: Variable in function definition
- **Argument**: Actual value passed when calling

## Order Matters

```python
def introduce(name, age):
    print(f"{name} is {age} years old")

introduce("Alice", 25)  # Alice is 25 years old
introduce(25, "Alice")  # 25 is Alice years old (wrong!)
```

## Key Takeaways

1. **Parameters**: Variables in function definition
2. **Arguments**: Values passed when calling
3. **Multiple parameters**: Separated by commas
4. **Order matters**: Arguments match parameters by position
5. **Flexibility**: Same function, different inputs
