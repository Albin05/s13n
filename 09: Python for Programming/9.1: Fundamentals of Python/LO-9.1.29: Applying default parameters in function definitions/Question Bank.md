### **1. Simple Default Parameter**

Write a function `greet` that takes a `name` parameter and an optional `greeting` parameter with default value "Hello". Return a greeting message.

**Expected Output:**
```python
print(greet("Alice"))  # Hello, Alice!
print(greet("Bob", "Hi"))  # Hi, Bob!
```

**Hint:** Use `greeting="Hello"` as the default parameter.

---

---

### **2. Power Function with Default Exponent**

Create a function `power` that takes a base number and an exponent with a default value of 2. Return the result.

**Expected Output:**
```python
print(power(5))  # 25 (5²)
print(power(2, 3))  # 8 (2³)
print(power(10))  # 100 (10²)
```

**Hint:** Default parameter: `exponent=2`

---

---

### **3. Calculate Discount with Default Rate**

Define a function `calculate_discount` that takes a price and a discount percentage with a default of 10%. Return the discounted price.

**Expected Output:**
```python
print(calculate_discount(100))  # 90.0 (10% off)
print(calculate_discount(100, 20))  # 80.0 (20% off)
print(calculate_discount(250))  # 225.0 (10% off)
```

**Hint:** Default parameter: `discount_percent=10`

---

---

### **4. Create Username with Default Domain**

Write a function `create_email` that takes a username and an optional domain with default value "example.com". Return the full email address.

**Expected Output:**
```python
print(create_email("alice"))  # alice@example.com
print(create_email("bob", "gmail.com"))  # bob@gmail.com
```

**Hint:** Concatenate username + "@" + domain

---

---

### **5. Repeat String with Default Count**

Create a function `repeat_text` that takes text and a count parameter with default value 3. Return the repeated text.

**Expected Output:**
```python
print(repeat_text("Hello"))  # HelloHelloHello
print(repeat_text("Hi", 5))  # HiHiHiHiHi
print(repeat_text("*"))  # ***
```

**Hint:** Use string multiplication: `text * count`

---

---

### **6. Temperature Converter with Default Unit**

Define a function `convert_temperature` that takes a temperature value and an optional unit parameter (default "C" for Celsius). If unit is "C", convert to Fahrenheit; if "F", convert to Celsius. Return the converted value.

**Expected Output:**
```python
print(convert_temperature(0))  # 32.0 (0°C to °F)
print(convert_temperature(32, "F"))  # 0.0 (32°F to °C)
print(convert_temperature(100))  # 212.0 (100°C to °F)
```

**Hint:**
- C to F: `(celsius * 9/5) + 32`
- F to C: `(fahrenheit - 32) * 5/9`

---

---

### **7. Format Name with Default Title**

Write a function `format_name` that takes first_name, last_name, and an optional title with default value "Mr./Ms.". Return the formatted name.

**Expected Output:**
```python
print(format_name("John", "Doe"))  # Mr./Ms. John Doe
print(format_name("Jane", "Smith", "Dr."))  # Dr. Jane Smith
```

**Hint:** Concatenate with f-string: `f"{title} {first_name} {last_name}"`

---

---

### **8. Calculate Tax with Default Rate**

Create a function `calculate_tax` that takes income and an optional tax_rate with default 15%. Return the tax amount.

**Expected Output:**
```python
print(calculate_tax(50000))  # 7500.0 (15%)
print(calculate_tax(50000, 20))  # 10000.0 (20%)
print(calculate_tax(100000))  # 15000.0 (15%)
```

**Hint:** Tax = `income * tax_rate / 100`

---

---

### **9. Send Message with Default Priority**

Define a function `send_message` that takes a message text and an optional priority with default "Normal". Print the message with its priority level.

**Expected Output:**
```python
send_message("Meeting at 3pm")
# [Normal] Meeting at 3pm

send_message("URGENT: Server down", "High")
# [High] URGENT: Server down
```

**Hint:** Use f-string: `f"[{priority}] {message}"`

---

---

### **10. Multiple Defaults - Rectangle Area**

Write a function `calculate_rectangle_area` that takes length and width, both with default value 1. Return the area.

**Expected Output:**
```python
print(calculate_rectangle_area())  # 1 (1 × 1)
print(calculate_rectangle_area(5))  # 5 (5 × 1)
print(calculate_rectangle_area(5, 3))  # 15 (5 × 3)
```

**Hint:** Both parameters can have defaults: `length=1, width=1`

---

---

### **11. Create URL with Default Protocol**

Create a function `create_url` that takes a domain and an optional protocol with default "https". Return the complete URL.

**Expected Output:**
```python
print(create_url("example.com"))  # https://example.com
print(create_url("example.com", "http"))  # http://example.com
```

**Hint:** Concatenate: `f"{protocol}://{domain}"`

---

---

### **12. Print Message with Default Separator**

Define a function `print_message` that takes multiple words as parameters and a separator with default " ". Print the words joined by the separator.

**Expected Output:**
```python
print_message("Hello", "World")  # Hello World
print_message("Hello", "World", separator="-")  # Hello-World
print_message("2024", "12", "19", separator="/")  # 2024/12/19
```

**Hint:** Use `*args` for multiple words, then `separator.join(args)`

---

---

### **13. Calculate BMI with Default Units**

Write a function `calculate_bmi` that takes weight and height, and an optional unit system with default "metric".
- If metric: weight in kg, height in m
- If imperial: weight in lbs, height in inches

Return the BMI value.

**Expected Output:**
```python
print(calculate_bmi(70, 1.75))  # 22.86 (metric)
print(calculate_bmi(154, 69, "imperial"))  # 22.75 (imperial)
```

**Hint:**
- Metric BMI: `weight / (height ** 2)`
- Imperial BMI: `(weight / (height ** 2)) * 703`

---

---

### **14. Login Function with Default Attempts**

Create a function `attempt_login` that takes username, password, and an optional max_attempts with default 3. Simulate login attempts and return success/failure message.

**Expected Output:**
```python
attempt_login("admin", "password123")
# Login successful for admin (Max attempts: 3)

attempt_login("user", "pass", 5)
# Login successful for user (Max attempts: 5)
```

**Hint:** Print formatted message with all parameters.

---

---

### **15. Format Currency with Default Symbol**

Define a function `format_currency` that takes an amount and an optional currency symbol with default "$". Return formatted string.

**Expected Output:**
```python
print(format_currency(1234.56))  # $1,234.56
print(format_currency(1000, "€"))  # €1,000.00
print(format_currency(5000, "£"))  # £5,000.00
```

**Hint:** Use f-string with formatting: `f"{symbol}{amount:,.2f}"`

---

---

### **16. Create List with Default Size**

Write a function `create_list` that takes an optional size parameter with default 5, and an optional value with default 0. Return a list of that size filled with the value.

**Expected Output:**
```python
print(create_list())  # [0, 0, 0, 0, 0]
print(create_list(3))  # [0, 0, 0]
print(create_list(4, 1))  # [1, 1, 1, 1]
```

**Hint:** Use list multiplication: `[value] * size`

---

---

### **17. Calculate Shipping Cost with Default Method**

Create a function `calculate_shipping` that takes weight and an optional method with default "standard".
- Standard: $5 per kg
- Express: $10 per kg
- Overnight: $15 per kg

Return the shipping cost.

**Expected Output:**
```python
print(calculate_shipping(2))  # 10.0 (standard)
print(calculate_shipping(2, "express"))  # 20.0 (express)
print(calculate_shipping(3, "overnight"))  # 45.0 (overnight)
```

**Hint:** Use if-elif to determine rate based on method.

---

---

### **18. Draw Shape with Default Character**

Define a function `draw_line` that takes length and an optional character with default "*". Print a line of that character.

**Expected Output:**
```python
draw_line(5)  # *****
draw_line(3, "#")  # ###
draw_line(10, "-")  # ----------
```

**Hint:** Print `character * length`

---

---

### **19. Calculate Grade with Default Scale**

Write a function `calculate_grade` that takes a score and an optional scale with default "letter" (returns A/B/C/D/F). If scale is "gpa", return GPA value (4.0/3.0/2.0/1.0/0.0).

**Expected Output:**
```python
print(calculate_grade(95))  # A
print(calculate_grade(85, "gpa"))  # 3.0
print(calculate_grade(75))  # C
```

**Hint:** Use two sets of conditionals based on scale parameter.

---

---

### **20. Timer Function with Default Unit**

Create a function `format_time` that takes seconds and an optional unit with default "seconds". Convert and return the time in the specified unit (seconds, minutes, hours).

**Expected Output:**
```python
print(format_time(120))  # 120 seconds
print(format_time(120, "minutes"))  # 2.0 minutes
print(format_time(7200, "hours"))  # 2.0 hours
```

**Hint:**
- seconds: return as-is
- minutes: divide by 60
- hours: divide by 3600

---

---

### **21. Search List with Default Start Index**

Define a function `find_index` that takes a list, a target value, and an optional start index with default 0. Return the index where target is found, searching from start index.

**Expected Output:**
```python
nums = [1, 2, 3, 2, 4, 2]
print(find_index(nums, 2))  # 1 (first occurrence)
print(find_index(nums, 2, 2))  # 3 (occurrence from index 2)
```

**Hint:** Use loop starting from start_index to find target.

---

---

### **22. Validate Password with Default Requirements**

Write a function `validate_password` that takes a password and optional min_length with default 8. Return True if password meets length requirement, False otherwise.

**Expected Output:**
```python
print(validate_password("abc123"))  # False (length 6 < 8)
print(validate_password("password123"))  # True (length 12 >= 8)
print(validate_password("pass", 4))  # True (length 4 >= 4)
```

**Hint:** Check `len(password) >= min_length`

---

---

### **23. Create Range with Default Step**

Create a function `custom_range` that takes start, end, and an optional step with default 1. Return a list of numbers in that range.

**Expected Output:**
```python
print(custom_range(1, 5))  # [1, 2, 3, 4]
print(custom_range(0, 10, 2))  # [0, 2, 4, 6, 8]
print(custom_range(5, 0, -1))  # [5, 4, 3, 2, 1]
```

**Hint:** Use built-in `list(range(start, end, step))`

---

---

### **24. Format Phone Number with Default Country Code**

Define a function `format_phone` that takes a phone number and an optional country_code with default "+1". Return formatted phone with country code.

**Expected Output:**
```python
print(format_phone("1234567890"))  # +1-1234567890
print(format_phone("9876543210", "+91"))  # +91-9876543210
```

**Hint:** Concatenate: `f"{country_code}-{phone}"`

---

---

### **25. Calculate Compound Interest with Default Period**

Write a function `compound_interest` that takes principal, rate, time, and an optional n (compounds per year) with default 1. Return the final amount.

**Expected Output:**
```python
print(compound_interest(1000, 5, 2))  # 1102.5 (compounded yearly)
print(compound_interest(1000, 5, 2, 4))  # 1104.49 (compounded quarterly)
```

**Hint:** Formula: `principal * (1 + rate/100/n) ** (n * time)`

---

---

### **26. Pad String with Default Character**

Create a function `pad_string` that takes text, target length, and an optional pad_char with default space " ". Return text padded to target length.

**Expected Output:**
```python
print(pad_string("Hello", 10))  # "Hello     "
print(pad_string("Hi", 5, "*"))  # "Hi***"
```

**Hint:** Calculate padding needed: `target_length - len(text)`, then add `pad_char`

---

---

### **27. Generate Password with Default Length**

Define a function `generate_password` that takes an optional length with default 8, and an optional include_numbers with default True. Return a randomly generated password.

**Expected Output:**
```python
print(generate_password())  # e.g., "aB3dE7fG" (8 chars with numbers)
print(generate_password(12))  # e.g., "aBc4DeF8gHiJ" (12 chars)
print(generate_password(6, False))  # e.g., "aBcdEf" (6 chars, no numbers)
```

**Hint:** Use random.choice with string.ascii_letters and optionally string.digits

---

---

### **28. Calculate Tip with Default Percentage**

Write a function `calculate_tip` that takes a bill amount and an optional tip_percent with default 15%. Return the tip amount.

**Expected Output:**
```python
print(calculate_tip(100))  # 15.0 (15%)
print(calculate_tip(50, 20))  # 10.0 (20%)
print(calculate_tip(200))  # 30.0 (15%)
```

**Hint:** Tip = `bill * tip_percent / 100`

---

---

### **29. Filter List with Default Condition**

Create a function `filter_numbers` that takes a list and an optional condition with default "positive".
- "positive": return positive numbers
- "negative": return negative numbers
- "even": return even numbers

Return the filtered list.

**Expected Output:**
```python
print(filter_numbers([1, -2, 3, -4, 5]))  # [1, 3, 5] (positive)
print(filter_numbers([1, -2, 3, -4, 5], "negative"))  # [-2, -4]
print(filter_numbers([1, 2, 3, 4, 5], "even"))  # [2, 4]
```

**Hint:** Use list comprehension with different conditions based on parameter.

---

---

### **30. Create Report Header with Defaults**

Define a function `create_header` that takes title, an optional width with default 50, and an optional border_char with default "=". Return a formatted header.

**Expected Output:**
```python
print(create_header("Report"))
# ==================================================
#                      Report
# ==================================================

print(create_header("Summary", 30, "-"))
# ------------------------------
#           Summary
# ------------------------------
```

**Hint:** Center the title and create borders with `border_char * width`

---

## Key Concepts

### What Are Default Parameters?

Default parameters allow you to specify default values for function parameters. If the caller doesn't provide a value, the default is used.

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Use default
print(greet("Alice"))  # Hello, Alice!

# Override default
print(greet("Bob", "Hi"))  # Hi, Bob!
```

### Syntax

```python
def function_name(required_param, optional_param=default_value):
    # Function body
    pass
```

**Rules:**
1. Parameters with defaults must come AFTER parameters without defaults
2. Default value is evaluated once when function is defined
3. Can have multiple default parameters
4. Can override defaults by position or by name

### Why Use Default Parameters?

**Benefits:**
1. **Flexibility**: Function works with or without optional arguments
2. **Backward compatibility**: Add new parameters without breaking existing calls
3. **Cleaner code**: Avoid multiple function versions
4. **Common defaults**: Set sensible defaults for typical use cases
5. **Optional features**: Make advanced features optional

### Parameter Order Rules

```python
# WRONG - Default before required
def wrong(name="Guest", age):  # SyntaxError!
    pass

# RIGHT - Required before defaults
def correct(age, name="Guest"):
    pass
```

**Required parameters must come BEFORE default parameters!**

### Overriding Defaults

```python
def calculate(x, y=2, z=3):
    return x + y + z

# Use all defaults
print(calculate(1))  # 1 + 2 + 3 = 6

# Override one default
print(calculate(1, 5))  # 1 + 5 + 3 = 9

# Override both defaults
print(calculate(1, 5, 10))  # 1 + 5 + 10 = 16

# Use keyword arguments
print(calculate(1, z=10))  # 1 + 2 + 10 = 13
```

### Common Patterns

**Pattern 1: Optional Configuration**
```python
def connect_database(host, port=5432, timeout=30):
    # Use default port and timeout if not specified
    pass
```

**Pattern 2: Optional Formatting**
```python
def format_number(num, decimals=2, currency="$"):
    return f"{currency}{num:.{decimals}f}"
```

**Pattern 3: Optional Behavior**
```python
def save_file(data, backup=True):
    # Save file
    if backup:
        # Create backup
        pass
```

**Pattern 4: Multiple Defaults**
```python
def draw_rectangle(width=10, height=5, char="*"):
    for i in range(height):
        print(char * width)
```

### Mutable Default Arguments Warning

**DANGER: Don't use mutable objects as defaults!**

```python
# WRONG - Mutable default
def add_item(item, items=[]):  # BAD!
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - Unexpected!

# RIGHT - Use None and create new list
def add_item(item, items=None):  # GOOD!
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [2] - Correct!
```

**Why?** Default values are evaluated once when the function is defined, not each time it's called. Mutable objects (lists, dicts) will be shared across calls!

### Best Practices

1. **Use immutable defaults**: Strings, numbers, tuples, None
2. **Descriptive names**: Make default values obvious
3. **Sensible defaults**: Choose common, safe default values
4. **Document defaults**: Comment what the default means
5. **Don't overuse**: Too many defaults can confuse users
6. **Test both cases**: Test with and without defaults

### When to Use Default Parameters

**Use defaults when:**
- Parameter has a typical/common value
- Making parameters optional improves usability
- Adding backward-compatible features
- Configuration options with standard settings
- Optional formatting/display preferences

**Don't use defaults when:**
- Every call needs a different value
- No sensible default exists
- Value depends on other parameters
- Security-sensitive parameters (require explicit values)

### Default Values Can Be Expressions

```python
def log_message(message, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now()  # Evaluated at call time
    print(f"[{timestamp}] {message}")
```

### Real-World Applications

1. **API Functions**: Default timeout, retry attempts
2. **File Operations**: Default encoding, mode
3. **Web Requests**: Default headers, timeout
4. **Database Queries**: Default limit, offset
5. **UI Functions**: Default colors, sizes, positions
6. **Math Functions**: Default precision, rounding mode

---

