# Lecture Notes: Use Function Parameters

## Function Parameters

Parameters allow functions to accept input values.


---

<div align="center">

![Function machine concept - input to output](https://images.unsplash.com/photo-1581291518857-4e27b48ff24e?w=800&q=80)

*Functions are reusable blocks of code that take inputs and return outputs*

</div>

---
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
