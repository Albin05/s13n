# Pre-Read: Applying Default Parameters in Function Definitions

## Why Default Parameters?

Functions with lots of required parameters are annoying to use. Default parameters make functions **easy to use** for common cases while staying **powerful** for complex cases!

### Simple Analogy

Think of default parameters like **ordering coffee**:
- **Required**: "I want a coffee" (must specify)
- **Defaults**: Medium size, regular milk, normal temperature (most people want this)
- **Override when needed**: "Make it large, almond milk, extra hot" (customize!)
- **Result**: Quick ordering for most, detailed control when needed

Or like **phone settings**:
- **Auto-brightness**: ON by default (works for 90% of users)
- **Override**: Turn off and set manually if you want
- **Smart design**: Common case is easy, customization available

Default parameters = **convenience with flexibility**!

## What You'll Learn
In this lesson, you'll learn how to provide default values for function parameters, making some arguments optional when calling the function.

## Why This Matters
Default parameters make functions more flexible:
- Users can provide custom values OR use sensible defaults
- Reduces the number of required arguments
- Makes functions easier to use
- Common in professional Python code

Example: `print()` has default parameter `end="\n"` (newline). You can override it: `print("Hi", end="")`

---

## What are Default Parameters?

**Default parameters** have predefined values. If the caller doesn't provide a value, the default is used.

```python
def greet(name, greeting="Hello"):  # greeting has default
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice! (uses default)
greet("Bob", "Hi")          # Hi, Bob! (overrides default)
greet("Charlie", "Hey")     # Hey, Charlie!
```

---

## Syntax

```python
def function_name(required_param, optional_param=default_value):
    # code
```

**Rules:**
1. Default parameters come AFTER required parameters
2. Can have multiple default parameters
3. Caller can override any default

---

## Simple Examples

### Example 1: Power Function

```python
def power(base, exponent=2):  # exponent defaults to 2 (square)
    return base ** exponent

print(power(5))      # 25 (5²)
print(power(5, 3))   # 125 (5³)
print(power(2, 4))   # 16 (2⁴)
```

### Example 2: Greeting with Time

```python
def greet(name, time_of_day="day"):
    if time_of_day == "morning":
        print(f"Good morning, {name}!")
    elif time_of_day == "evening":
        print(f"Good evening, {name}!")
    else:
        print(f"Good day, {name}!")

greet("Alice")                # Good day, Alice!
greet("Bob", "morning")       # Good morning, Bob!
greet("Charlie", "evening")   # Good evening, Charlie!
```

---

## Real-World Examples

### Example 1: Calculate Discount

```python
def apply_discount(price, discount=10):  # 10% default
    final_price = price * (1 - discount/100)
    return final_price

print(apply_discount(100))      # 90 (10% off)
print(apply_discount(100, 20))  # 80 (20% off)
print(apply_discount(50, 5))    # 47.5 (5% off)
```

### Example 2: Print Message with Separator

```python
def print_message(message, sep="-", length=20):
    print(sep * length)
    print(message)
    print(sep * length)

print_message("Hello")           # Uses defaults
print_message("Python", "*")     # Custom separator
print_message("Code", "=", 30)   # Custom both
```

---

## Order Matters!

**Correct:** Required parameters first, then defaults

```python
def greet(name, greeting="Hello"):  # ✓ Correct
    print(f"{greeting}, {name}")
```

**Incorrect:** Defaults before required

```python
def greet(greeting="Hello", name):  # ✗ SyntaxError!
    print(f"{greeting}, {name}")
```

---

## Multiple Defaults

```python
def create_profile(name, age=18, city="Unknown", country="USA"):
    print(f"{name}, {age}, {city}, {country}")

create_profile("Alice")                    # Alice, 18, Unknown, USA
create_profile("Bob", 25)                  # Bob, 25, Unknown, USA
create_profile("Charlie", 30, "NYC")       # Charlie, 30, NYC, USA
create_profile("David", 22, "LA", "USA")   # David, 22, LA, USA
```

---

## Try It Yourself (Before Class)

```python
def repeat_text(text, times=3, separator=" "):
    return (text + separator) * times

print(repeat_text("Hi"))
print(repeat_text("Hello", 5))
print(repeat_text("Python", 2, "-"))
```

**Questions:**
1. What does each call output?
2. Can you call it with just one argument?
3. What happens if you provide all three arguments?

---

## Key Takeaways

Before class, remember:
1. **Default parameters** - have predefined values
2. **Optional arguments** - caller can skip or override
3. **Order matters** - required first, defaults after
4. **Multiple defaults** - can have many
5. **Common pattern** - makes functions flexible

## What's Next?

In the live session, we'll:
- Write functions with multiple default parameters
- Learn about keyword arguments
- Understand when to use defaults
- Combine defaults with return values

See you in class!
