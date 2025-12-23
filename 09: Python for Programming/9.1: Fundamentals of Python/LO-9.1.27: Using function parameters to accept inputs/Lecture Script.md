### Using Function Parameters to Accept Inputs

### Hook (3 minutes)

"Yesterday we learned functions, but they always did the SAME thing. Imagine if your calculator's 'add' button could only add 2+3 every time - not very useful!"

Today: Make functions flexible by passing data to them!

Think of a vending machine - ONE machine accepts INPUT (your selection) and gives different OUTPUT. Functions work the same way!

### Section 1: The Problem Without Parameters (4 minutes)

**Inflexible function:**
```python
def greet_alice():
    print("Hello, Alice!")

greet_alice()  # Hello, Alice!
greet_alice()  # Hello, Alice! (same every time)
```

To greet different people, we'd need many functions - impractical! **Solution: Parameters!**

### Section 2: What Are Parameters? (5 minutes)

A parameter is a variable in the function definition that acts as a placeholder for data.

**Syntax:**
```python
def function_name(parameter):
    # Use parameter here
    print(parameter)
```

**Example:**
```python
def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice")    # Hello, Alice!
greet("Bob")      # Hello, Bob!
greet("Charlie")  # Hello, Charlie!
```

**Key points:**
- Parameter is a variable name
- Gets its value when function is called
- Can be used anywhere in function body

### Section 3: Parameters vs Arguments (3 minutes)

```python
def greet(name):  # 'name' is a PARAMETER
    print(f"Hello, {name}")

greet("Alice")  # "Alice" is an ARGUMENT
```

**Remember:**
- Parameter = placeholder in definition
- Argument = actual value when calling

**Example:**
```python
def square(number):  # parameter
    print(number ** 2)

square(5)   # 5 is argument -> 25
square(10)  # 10 is argument -> 100
```

### Section 4: Multiple Parameters (5 minutes)

**Syntax:**
```python
def function_name(param1, param2, param3):
    pass
```

**Examples:**
```python
def greet_full(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet_full("Alice", "Smith")  # Hello, Alice Smith!

def add(a, b):
    print(f"{a} + {b} = {a + b}")

add(5, 3)   # 5 + 3 = 8
```

**Order matters!**
```python
def introduce(name, age):
    print(f"My name is {name} and I'm {age} years old")

introduce("Alice", 25)  # Correct
introduce(25, "Alice")  # Wrong! "My name is 25..."
```

### Section 5: Different Data Types (4 minutes)

**Strings:**
```python
def shout(message):
    print(message.upper() + "!")

shout("hello")  # HELLO!
```

**Numbers:**
```python
def print_times(text, count):
    for i in range(count):
        print(text)

print_times("Python", 3)
```

**Mixed types:**
```python
def make_sentence(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

make_sentence("Alice", 25, "New York")
```

### Section 6: Common Mistakes (3 minutes)

**Wrong number of arguments:**
```python
def add(a, b):
    print(a + b)

add(5)        # Error: missing argument
add(5, 3, 2)  # Error: too many arguments
add(5, 3)     # Correct
```

**Wrong order:**
```python
def subtract(a, b):
    print(a - b)

subtract(10, 3)  # 7
subtract(3, 10)  # -7 (different!)
```

### Section 7: Real-World Application (3 minutes)

**Validation:**
```python
def validate_username(username):
    if len(username) < 3:
        print("Username too short!")
    elif len(username) > 20:
        print("Username too long!")
    else:
        print("Username valid!")

validate_username("ab")        # Too short!
validate_username("alice123")  # Valid!
```

### Section 8: Practice (2 minutes)

Write `calculate_bmi` that takes weight and height:
```python
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    print(f"BMI: {bmi:.2f}")

calculate_bmi(70, 1.75)  # BMI: 22.86
```

### Wrap-Up (2 minutes)

**Key takeaways:**
1. Parameters = placeholders in definition
2. Arguments = actual values when calling
3. Multiple parameters = separate with commas
4. Order matters
5. Any data type can be a parameter

**Template:**
```python
def function_name(param1, param2):
    # Use parameters
    pass

function_name(value1, value2)
```
