# Editorials: Applying Default Parameters in Function Definitions

## Problem 1: Simple Default Parameter

**Problem:** Write a function `greet` that takes a `name` parameter and an optional `greeting` parameter with default value "Hello". Return a greeting message.

**Solution:**
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Test cases
print(greet("Alice"))  # Hello, Alice!
print(greet("Bob", "Hi"))  # Hi, Bob!
print(greet("Charlie", "Good morning"))  # Good morning, Charlie!
```

**Output:**
```
Hello, Alice!
Hi, Bob!
Good morning, Charlie!
```

**Explanation:**
The function has two parameters:
1. `name` - required parameter (no default)
2. `greeting` - optional parameter with default value "Hello"

When called with just one argument (e.g., `greet("Alice")`), the `greeting` parameter uses its default value "Hello". When called with two arguments (e.g., `greet("Bob", "Hi")`), the second argument overrides the default value. The function returns a formatted greeting string using an f-string that combines the greeting and name.

**Key Concept:** Default parameters make function arguments optional, providing flexibility without requiring multiple function definitions.

---

## Problem 2: Power Function with Default Exponent

**Problem:** Create a function `power` that takes a base number and an exponent with a default value of 2. Return the result.

**Solution:**
```python
def power(base, exponent=2):
    return base ** exponent

# Test cases
print(power(5))  # 25 (5²)
print(power(2, 3))  # 8 (2³)
print(power(10))  # 100 (10²)
print(power(3, 4))  # 81 (3⁴)
```

**Output:**
```
25
8
100
81
```

**Explanation:**
This function calculates the power of a number. The `base` parameter is required, while `exponent` has a default value of 2 (for squaring). If you call `power(5)`, it calculates 5² = 25. If you call `power(2, 3)`, it calculates 2³ = 8. The default value of 2 is useful because squaring is a common operation, making the function convenient for that use case while still allowing other exponents.

**Key Concept:** Default parameters should represent the most common or sensible use case for that parameter.

---

## Problem 3: Calculate Discount with Default Rate

**Problem:** Define a function `calculate_discount` that takes a price and a discount percentage with a default of 10%. Return the discounted price.

**Solution:**
```python
def calculate_discount(price, discount_percent=10):
    discount_amount = price * discount_percent / 100
    final_price = price - discount_amount
    return final_price

# Test cases
print(calculate_discount(100))  # 90.0 (10% off)
print(calculate_discount(100, 20))  # 80.0 (20% off)
print(calculate_discount(250))  # 225.0 (10% off)
print(calculate_discount(50, 5))  # 47.5 (5% off)
```

**Output:**
```
90.0
80.0
225.0
47.5
```

**Explanation:**
The function calculates the final price after applying a discount. The `discount_percent` parameter has a default value of 10, representing a common discount rate. The calculation:
1. Calculate discount amount: `price * discount_percent / 100`
2. Subtract from original price: `price - discount_amount`

When called with just the price (`calculate_discount(100)`), it uses the default 10% discount. When called with both parameters (`calculate_discount(100, 20)`), it uses the specified discount rate.

**Key Concept:** Default parameters work well for common business rules or standard values that can be overridden when needed.

---

## Problem 4: Create Username with Default Domain

**Problem:** Write a function `create_email` that takes a username and an optional domain with default value "example.com". Return the full email address.

**Solution:**
```python
def create_email(username, domain="example.com"):
    return f"{username}@{domain}"

# Test cases
print(create_email("alice"))  # alice@example.com
print(create_email("bob", "gmail.com"))  # bob@gmail.com
print(create_email("charlie", "company.org"))  # charlie@company.org
```

**Output:**
```
alice@example.com
bob@gmail.com
charlie@company.org
```

**Explanation:**
This function creates email addresses by combining a username with a domain. The `domain` parameter has a default value of "example.com", which is useful for testing or when working with a primary domain. The function simply concatenates the username, the "@" symbol, and the domain using an f-string. Users can override the domain by providing a second argument.

**Key Concept:** Default parameters are excellent for configuration values that have a standard setting but may need customization.

---

## Problem 5: Repeat String with Default Count

**Problem:** Create a function `repeat_text` that takes text and a count parameter with default value 3. Return the repeated text.

**Solution:**
```python
def repeat_text(text, count=3):
    return text * count

# Test cases
print(repeat_text("Hello"))  # HelloHelloHello
print(repeat_text("Hi", 5))  # HiHiHiHiHi
print(repeat_text("*"))  # ***
print(repeat_text("-", 10))  # ----------
```

**Output:**
```
HelloHelloHello
HiHiHiHiHi
***
----------
```

**Explanation:**
This function repeats a string a specified number of times using Python's string multiplication operator (`*`). The `count` parameter has a default value of 3, making it easy to quickly repeat something three times without specifying the count. When called with just text (`repeat_text("Hello")`), it repeats 3 times. When called with both parameters (`repeat_text("Hi", 5)`), it uses the specified count.

**Key Concept:** Default parameters can provide convenience defaults for common operations while maintaining flexibility.

---

## Problem 6: Temperature Converter with Default Unit

**Problem:** Define a function `convert_temperature` that takes a temperature value and an optional unit parameter (default "C" for Celsius). If unit is "C", convert to Fahrenheit; if "F", convert to Celsius. Return the converted value.

**Solution:**
```python
def convert_temperature(temp, unit="C"):
    if unit == "C":
        # Celsius to Fahrenheit
        converted = (temp * 9/5) + 32
    else:  # unit == "F"
        # Fahrenheit to Celsius
        converted = (temp - 32) * 5/9
    return converted

# Test cases
print(convert_temperature(0))  # 32.0 (0°C to °F)
print(convert_temperature(32, "F"))  # 0.0 (32°F to °C)
print(convert_temperature(100))  # 212.0 (100°C to °F)
print(convert_temperature(212, "F"))  # 100.0 (212°F to °C)
```

**Output:**
```
32.0
0.0
212.0
100.0
```

**Explanation:**
This function converts temperatures between Celsius and Fahrenheit. The `unit` parameter has a default value of "C", assuming the input is in Celsius (which is more commonly used globally). The function uses conditional logic:
- If `unit == "C"`: Converts Celsius to Fahrenheit using formula `(temp * 9/5) + 32`
- If `unit == "F"`: Converts Fahrenheit to Celsius using formula `(temp - 32) * 5/9`

The default makes it convenient to convert from Celsius (the default) to Fahrenheit, while still allowing Fahrenheit-to-Celsius conversions when specified.

**Key Concept:** Default parameters can represent the most common input format or standard unit in domain-specific functions.

---

## Problem 7: Format Name with Default Title

**Problem:** Write a function `format_name` that takes first_name, last_name, and an optional title with default value "Mr./Ms.". Return the formatted name.

**Solution:**
```python
def format_name(first_name, last_name, title="Mr./Ms."):
    return f"{title} {first_name} {last_name}"

# Test cases
print(format_name("John", "Doe"))  # Mr./Ms. John Doe
print(format_name("Jane", "Smith", "Dr."))  # Dr. Jane Smith
print(format_name("Bob", "Johnson", "Prof."))  # Prof. Bob Johnson
```

**Output:**
```
Mr./Ms. John Doe
Dr. Jane Smith
Prof. Bob Johnson
```

**Explanation:**
This function formats a person's name with an optional title. The parameters are:
1. `first_name` - required
2. `last_name` - required
3. `title` - optional with default "Mr./Ms."

The default title "Mr./Ms." serves as a neutral, gender-inclusive option when no specific title is provided. The function combines all three parts into a formatted string using an f-string. Users can override the title by providing a third argument for professional titles like "Dr.", "Prof.", etc.

**Key Concept:** Default parameters should use neutral or generic values that work in most cases, allowing customization when needed.

---

## Problem 8: Calculate Tax with Default Rate

**Problem:** Create a function `calculate_tax` that takes income and an optional tax_rate with default 15%. Return the tax amount.

**Solution:**
```python
def calculate_tax(income, tax_rate=15):
    tax_amount = income * tax_rate / 100
    return tax_amount

# Test cases
print(calculate_tax(50000))  # 7500.0 (15%)
print(calculate_tax(50000, 20))  # 10000.0 (20%)
print(calculate_tax(100000))  # 15000.0 (15%)
print(calculate_tax(75000, 25))  # 18750.0 (25%)
```

**Output:**
```
7500.0
10000.0
15000.0
18750.0
```

**Explanation:**
This function calculates tax based on income and a tax rate. The `tax_rate` parameter has a default value of 15, representing a standard tax rate percentage. The calculation is straightforward: `income * tax_rate / 100`. When called with just income (`calculate_tax(50000)`), it uses the default 15% rate. When called with both parameters (`calculate_tax(50000, 20)`), it uses the specified rate. This pattern is common in financial calculations where standard rates exist but can vary.

**Key Concept:** Default parameters are ideal for rates, percentages, and factors that have standard values but may need adjustment.

---

## Problem 9: Send Message with Default Priority

**Problem:** Define a function `send_message` that takes a message text and an optional priority with default "Normal". Print the message with its priority level.

**Solution:**
```python
def send_message(message, priority="Normal"):
    print(f"[{priority}] {message}")

# Test cases
send_message("Meeting at 3pm")
# [Normal] Meeting at 3pm

send_message("URGENT: Server down", "High")
# [High] URGENT: Server down

send_message("Reminder: Submit report", "Low")
# [Low] Reminder: Submit report
```

**Output:**
```
[Normal] Meeting at 3pm
[High] URGENT: Server down
[Low] Reminder: Submit report
```

**Explanation:**
This function simulates a messaging system with priority levels. The `priority` parameter has a default value of "Normal", assuming most messages have standard priority. The function prints a formatted message with the priority in brackets followed by the message text. When no priority is specified, it defaults to "Normal", making the function easy to use for routine messages while still supporting high-priority or low-priority messages when needed.

**Key Concept:** Default parameters work well for classification or categorization values that have a standard or most-common category.

---

## Problem 10: Multiple Defaults - Rectangle Area

**Problem:** Write a function `calculate_rectangle_area` that takes length and width, both with default value 1. Return the area.

**Solution:**
```python
def calculate_rectangle_area(length=1, width=1):
    return length * width

# Test cases
print(calculate_rectangle_area())  # 1 (1 × 1)
print(calculate_rectangle_area(5))  # 5 (5 × 1)
print(calculate_rectangle_area(5, 3))  # 15 (5 × 3)
print(calculate_rectangle_area(width=4))  # 4 (1 × 4)
print(calculate_rectangle_area(7, 2))  # 14 (7 × 2)
```

**Output:**
```
1
5
15
4
14
```

**Explanation:**
This function calculates the area of a rectangle, with both parameters having default values of 1 (representing a unit square). This demonstrates multiple default parameters:
- Called with no arguments: Uses both defaults (1 × 1 = 1)
- Called with one argument: First default is overridden (5 × 1 = 5)
- Called with two arguments: Both defaults are overridden (5 × 3 = 15)
- Called with keyword argument: Can override specific parameter (1 × 4 = 4)

The default of 1 is useful for testing or calculating unit values.

**Key Concept:** Multiple default parameters provide maximum flexibility, allowing functions to work with 0, 1, 2, or all parameters specified.

---

## Problem 11: Create URL with Default Protocol

**Problem:** Create a function `create_url` that takes a domain and an optional protocol with default "https". Return the complete URL.

**Solution:**
```python
def create_url(domain, protocol="https"):
    return f"{protocol}://{domain}"

# Test cases
print(create_url("example.com"))  # https://example.com
print(create_url("example.com", "http"))  # http://example.com
print(create_url("api.service.com", "wss"))  # wss://api.service.com
```

**Output:**
```
https://example.com
http://example.com
wss://api.service.com
```

**Explanation:**
This function constructs URLs by combining a protocol with a domain. The `protocol` parameter defaults to "https", reflecting modern web security standards where HTTPS is preferred. The function concatenates the protocol, "://", and the domain using an f-string. While HTTPS is the default, users can specify other protocols like "http", "ftp", or "wss" when needed. This makes the function secure by default while remaining flexible.

**Key Concept:** Default parameters should reflect best practices and secure defaults (like HTTPS over HTTP).

---

## Problem 12: Print Message with Default Separator

**Problem:** Define a function `print_message` that takes multiple words as parameters and a separator with default " ". Print the words joined by the separator.

**Solution:**
```python
def print_message(*args, separator=" "):
    message = separator.join(args)
    print(message)

# Test cases
print_message("Hello", "World")  # Hello World
print_message("Hello", "World", separator="-")  # Hello-World
print_message("2024", "12", "19", separator="/")  # 2024/12/19
print_message("Python", "is", "awesome", separator="_")  # Python_is_awesome
```

**Output:**
```
Hello World
Hello-World
2024/12/19
Python_is_awesome
```

**Explanation:**
This function accepts a variable number of words using `*args` and an optional separator parameter with default " " (space). The `*args` syntax allows passing any number of positional arguments, which are collected into a tuple. The function:
1. Joins all arguments using the specified separator
2. Prints the result

The default space separator is standard for joining words, but can be overridden for different formatting needs (hyphens, slashes, underscores, etc.). The `separator` parameter must be specified as a keyword argument to distinguish it from the variable positional arguments.

**Key Concept:** Default parameters work with variable arguments (`*args`) by being specified as keyword-only arguments.

---

## Problem 13: Calculate BMI with Default Units

**Problem:** Write a function `calculate_bmi` that takes weight and height, and an optional unit system with default "metric". If metric: weight in kg, height in m. If imperial: weight in lbs, height in inches. Return the BMI value.

**Solution:**
```python
def calculate_bmi(weight, height, units="metric"):
    if units == "metric":
        # BMI = weight(kg) / height(m)²
        bmi = weight / (height ** 2)
    else:  # imperial
        # BMI = (weight(lbs) / height(inches)²) * 703
        bmi = (weight / (height ** 2)) * 703
    return round(bmi, 2)

# Test cases
print(calculate_bmi(70, 1.75))  # 22.86 (metric)
print(calculate_bmi(154, 69, "imperial"))  # 22.75 (imperial)
print(calculate_bmi(80, 1.80))  # 24.69 (metric)
print(calculate_bmi(180, 72, "imperial"))  # 24.41 (imperial)
```

**Output:**
```
22.86
22.75
24.69
24.41
```

**Explanation:**
This function calculates BMI (Body Mass Index) using different unit systems. The `units` parameter defaults to "metric" (more widely used globally). The calculation differs based on units:
- **Metric**: BMI = weight(kg) / height(m)²
- **Imperial**: BMI = (weight(lbs) / height(inches)²) × 703

The 703 conversion factor in the imperial formula accounts for the difference between metric and imperial measurements. The function returns the BMI rounded to 2 decimal places. The default of "metric" makes the function convenient for international use while supporting imperial measurements when specified.

**Key Concept:** Default parameters can specify standard units or formats, with conditional logic handling different cases.

---

## Problem 14: Login Function with Default Attempts

**Problem:** Create a function `attempt_login` that takes username, password, and an optional max_attempts with default 3. Simulate login attempts and return success/failure message.

**Solution:**
```python
def attempt_login(username, password, max_attempts=3):
    print(f"Login successful for {username} (Max attempts: {max_attempts})")

# Test cases
attempt_login("admin", "password123")
# Login successful for admin (Max attempts: 3)

attempt_login("user", "pass", 5)
# Login successful for user (Max attempts: 5)

attempt_login("guest", "guest123", 1)
# Login successful for guest (Max attempts: 1)
```

**Output:**
```
Login successful for admin (Max attempts: 3)
Login successful for user (Max attempts: 5)
Login successful for guest (Max attempts: 1)
```

**Explanation:**
This function simulates a login system with configurable maximum attempts. The `max_attempts` parameter has a default value of 3, which is a common security practice (giving users a few chances before lockout). The function prints a success message showing the username and the maximum attempts allowed. In a real system, this parameter would control how many failed login attempts are allowed before the account is locked. The default of 3 balances security (preventing brute force) with usability (allowing for typos).

**Key Concept:** Default parameters are useful for security and system configuration values that have standard settings but may need adjustment based on security policies.

---

## Problem 15: Format Currency with Default Symbol

**Problem:** Define a function `format_currency` that takes an amount and an optional currency symbol with default "$". Return formatted string.

**Solution:**
```python
def format_currency(amount, symbol="$"):
    return f"{symbol}{amount:,.2f}"

# Test cases
print(format_currency(1234.56))  # $1,234.56
print(format_currency(1000, "€"))  # €1,000.00
print(format_currency(5000, "£"))  # £5,000.00
print(format_currency(999.99, "¥"))  # ¥999.99
```

**Output:**
```
$1,234.56
€1,000.00
£5,000.00
¥999.99
```

**Explanation:**
This function formats monetary amounts with proper formatting and currency symbols. The `symbol` parameter defaults to "$" (US dollar), reflecting common usage. The formatting uses:
- `{symbol}` - The currency symbol
- `{amount:,.2f}` - The amount with thousands separators (,) and 2 decimal places (.2f)

Examples of the formatting:
- 1234.56 → "1,234.56" (comma separator, 2 decimals)
- 1000 → "1,000.00" (adds decimal places)

The default dollar symbol is convenient for US-based applications while allowing other currencies to be specified.

**Key Concept:** Default parameters for formatting functions should use the most common format or locale while allowing customization.

---

## Problem 16: Create List with Default Size

**Problem:** Write a function `create_list` that takes an optional size parameter with default 5, and an optional value with default 0. Return a list of that size filled with the value.

**Solution:**
```python
def create_list(size=5, value=0):
    return [value] * size

# Test cases
print(create_list())  # [0, 0, 0, 0, 0]
print(create_list(3))  # [0, 0, 0]
print(create_list(4, 1))  # [1, 1, 1, 1]
print(create_list(7, "x"))  # ['x', 'x', 'x', 'x', 'x', 'x', 'x']
print(create_list(value=-1))  # [-1, -1, -1, -1, -1]
```

**Output:**
```
[0, 0, 0, 0, 0]
[0, 0, 0]
[1, 1, 1, 1]
['x', 'x', 'x', 'x', 'x', 'x', 'x']
[-1, -1, -1, -1, -1]
```

**Explanation:**
This function creates a list of a specified size filled with a specified value, with both parameters having defaults. The function uses list multiplication (`[value] * size`) to create the list efficiently. The default values are:
- `size=5`: A reasonable default list size
- `value=0`: A common initial value (neutral/empty state)

The function demonstrates multiple default parameters working together. You can:
- Use both defaults: `create_list()` → [0,0,0,0,0]
- Override size only: `create_list(3)` → [0,0,0]
- Override both: `create_list(4, 1)` → [1,1,1,1]
- Use keyword arguments: `create_list(value=-1)` → uses default size with value -1

**Key Concept:** When multiple parameters have defaults, they all become optional, providing maximum flexibility in function calls.

---

## Problem 17: Calculate Shipping Cost with Default Method

**Problem:** Create a function `calculate_shipping` that takes weight and an optional method with default "standard". Standard: $5 per kg, Express: $10 per kg, Overnight: $15 per kg. Return the shipping cost.

**Solution:**
```python
def calculate_shipping(weight, method="standard"):
    if method == "standard":
        rate = 5
    elif method == "express":
        rate = 10
    elif method == "overnight":
        rate = 15
    else:
        rate = 5  # Default to standard if unknown method

    cost = weight * rate
    return cost

# Test cases
print(calculate_shipping(2))  # 10.0 (standard)
print(calculate_shipping(2, "express"))  # 20.0 (express)
print(calculate_shipping(3, "overnight"))  # 45.0 (overnight)
print(calculate_shipping(5, "standard"))  # 25.0 (standard)
```

**Output:**
```
10.0
20.0
45.0
25.0
```

**Explanation:**
This function calculates shipping costs based on weight and shipping method. The `method` parameter defaults to "standard" (the most economical and commonly chosen option). The function uses conditional logic to determine the rate per kilogram:
- "standard": $5/kg (default, economical)
- "express": $10/kg (faster, more expensive)
- "overnight": $15/kg (fastest, most expensive)

The cost is calculated by multiplying weight by the rate. The default "standard" method makes the function convenient for regular shipping while supporting premium options when needed. This pattern is common in e-commerce applications.

**Key Concept:** Default parameters can represent standard or economy options in business logic, with upgrades available through explicit specification.

---

## Problem 18: Draw Shape with Default Character

**Problem:** Define a function `draw_line` that takes length and an optional character with default "*". Print a line of that character.

**Solution:**
```python
def draw_line(length, character="*"):
    print(character * length)

# Test cases
draw_line(5)  # *****
draw_line(3, "#")  # ###
draw_line(10, "-")  # ----------
draw_line(8, "=")  # ========
```

**Output:**
```
*****
###
----------
========
```

**Explanation:**
This function draws a line of characters, useful for creating visual separators or ASCII art. The `character` parameter defaults to "*" (asterisk), a common character for drawing patterns and shapes. The function uses string multiplication (`character * length`) to repeat the character the specified number of times, then prints the result.

The default "*" makes it easy to quickly draw star lines without specifying the character each time, while still allowing customization for different visual effects (hyphens for dividers, equals signs for headers, etc.).

**Key Concept:** Default parameters for display/formatting functions should use common or visually appealing default values.

---

## Problem 19: Calculate Grade with Default Scale

**Problem:** Write a function `calculate_grade` that takes a score and an optional scale with default "letter" (returns A/B/C/D/F). If scale is "gpa", return GPA value (4.0/3.0/2.0/1.0/0.0).

**Solution:**
```python
def calculate_grade(score, scale="letter"):
    if scale == "letter":
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
    else:  # scale == "gpa"
        if score >= 90:
            return 4.0
        elif score >= 80:
            return 3.0
        elif score >= 70:
            return 2.0
        elif score >= 60:
            return 1.0
        else:
            return 0.0

# Test cases
print(calculate_grade(95))  # A
print(calculate_grade(85, "gpa"))  # 3.0
print(calculate_grade(75))  # C
print(calculate_grade(65, "gpa"))  # 1.0
```

**Output:**
```
A
3.0
C
1.0
```

**Explanation:**
This function calculates grades in different formats based on the scale parameter. The `scale` defaults to "letter" (more commonly used for displaying grades to students). The function has two sets of conditional logic:
- **Letter scale**: Returns letter grades (A, B, C, D, F) based on score ranges
- **GPA scale**: Returns numeric GPA values (4.0, 3.0, 2.0, 1.0, 0.0)

Both scales use the same score thresholds (90+ for A/4.0, 80+ for B/3.0, etc.). The default letter scale is more intuitive for most users, while the GPA scale is useful for cumulative calculations. This demonstrates how default parameters can control output format.

**Key Concept:** Default parameters can determine the output format or representation, with conditional logic adapting the function's behavior.

---

## Problem 20: Timer Function with Default Unit

**Problem:** Create a function `format_time` that takes seconds and an optional unit with default "seconds". Convert and return the time in the specified unit (seconds, minutes, hours).

**Solution:**
```python
def format_time(seconds, unit="seconds"):
    if unit == "seconds":
        return f"{seconds} seconds"
    elif unit == "minutes":
        minutes = seconds / 60
        return f"{minutes} minutes"
    elif unit == "hours":
        hours = seconds / 3600
        return f"{hours} hours"
    else:
        return f"{seconds} seconds"

# Test cases
print(format_time(120))  # 120 seconds
print(format_time(120, "minutes"))  # 2.0 minutes
print(format_time(7200, "hours"))  # 2.0 hours
print(format_time(3600, "minutes"))  # 60.0 minutes
```

**Output:**
```
120 seconds
2.0 minutes
2.0 hours
60.0 minutes
```

**Explanation:**
This function formats time values in different units. The `unit` parameter defaults to "seconds" (the base unit). The function converts based on the specified unit:
- "seconds": No conversion, returns value as-is
- "minutes": Divides by 60 (60 seconds = 1 minute)
- "hours": Divides by 3600 (3600 seconds = 1 hour)

The default "seconds" unit is appropriate because it's the most precise and doesn't require conversion. Users can request other units when needed for more readable output (e.g., "2.0 hours" is more meaningful than "7200 seconds").

**Key Concept:** Default parameters can specify base units or formats, with conversion logic handling alternative units.

---

## Problem 21: Search List with Default Start Index

**Problem:** Define a function `find_index` that takes a list, a target value, and an optional start index with default 0. Return the index where target is found, searching from start index.

**Solution:**
```python
def find_index(lst, target, start_index=0):
    for i in range(start_index, len(lst)):
        if lst[i] == target:
            return i
    return -1  # Not found

# Test cases
nums = [1, 2, 3, 2, 4, 2]
print(find_index(nums, 2))  # 1 (first occurrence)
print(find_index(nums, 2, 2))  # 3 (occurrence from index 2)
print(find_index(nums, 2, 4))  # 5 (occurrence from index 4)
print(find_index(nums, 9))  # -1 (not found)
```

**Output:**
```
1
3
5
-1
```

**Explanation:**
This function searches for a target value in a list, starting from a specified index. The `start_index` parameter defaults to 0 (searching from the beginning). The function:
1. Loops from `start_index` to the end of the list
2. Returns the index when the target is found
3. Returns -1 if the target is not found

The default of 0 makes it convenient to search the entire list, while the optional start_index is useful for:
- Finding subsequent occurrences of a value
- Continuing a search after a previous match
- Searching only a portion of the list

This pattern is similar to Python's built-in `str.find()` method.

**Key Concept:** Default parameters for index or position values typically start at 0 (beginning) or -1 (no limit), representing the most common use case.

---

## Problem 22: Validate Password with Default Requirements

**Problem:** Write a function `validate_password` that takes a password and optional min_length with default 8. Return True if password meets length requirement, False otherwise.

**Solution:**
```python
def validate_password(password, min_length=8):
    return len(password) >= min_length

# Test cases
print(validate_password("abc123"))  # False (length 6 < 8)
print(validate_password("password123"))  # True (length 12 >= 8)
print(validate_password("pass", 4))  # True (length 4 >= 4)
print(validate_password("short", 10))  # False (length 5 < 10)
print(validate_password("longpassword"))  # True (length 12 >= 8)
```

**Output:**
```
False
True
True
False
True
```

**Explanation:**
This function validates passwords based on minimum length requirements. The `min_length` parameter defaults to 8, which is a common security standard for password length. The function simply compares the password length to the minimum using `len(password) >= min_length` and returns a boolean result.

The default of 8 characters reflects modern security best practices, providing reasonable security while remaining user-friendly. Systems with stricter security requirements can override this default (e.g., `validate_password(pwd, 12)` for 12-character minimum).

**Key Concept:** Default parameters for validation functions should use industry-standard or recommended values while allowing customization for different security levels.

---

## Problem 23: Create Range with Default Step

**Problem:** Create a function `custom_range` that takes start, end, and an optional step with default 1. Return a list of numbers in that range.

**Solution:**
```python
def custom_range(start, end, step=1):
    return list(range(start, end, step))

# Test cases
print(custom_range(1, 5))  # [1, 2, 3, 4]
print(custom_range(0, 10, 2))  # [0, 2, 4, 6, 8]
print(custom_range(5, 0, -1))  # [5, 4, 3, 2, 1]
print(custom_range(10, 20, 3))  # [10, 13, 16, 19]
```

**Output:**
```
[1, 2, 3, 4]
[0, 2, 4, 6, 8]
[5, 4, 3, 2, 1]
[10, 13, 16, 19]
```

**Explanation:**
This function creates a list of numbers in a range with a customizable step value. The `step` parameter defaults to 1 (increment by 1), which is the most common use case. The function uses Python's built-in `range()` function and converts it to a list.

The default step of 1 makes it easy to create consecutive number sequences, while allowing:
- Even/odd numbers: `custom_range(0, 10, 2)`
- Countdown: `custom_range(5, 0, -1)`
- Custom increments: `custom_range(10, 20, 3)`

This mimics Python's `range()` function while returning a list and providing a clearer default behavior.

**Key Concept:** Default parameters for step/increment values typically default to 1 or -1, representing the standard increment direction.

---

## Problem 24: Format Phone Number with Default Country Code

**Problem:** Define a function `format_phone` that takes a phone number and an optional country_code with default "+1". Return formatted phone with country code.

**Solution:**
```python
def format_phone(phone, country_code="+1"):
    return f"{country_code}-{phone}"

# Test cases
print(format_phone("1234567890"))  # +1-1234567890
print(format_phone("9876543210", "+91"))  # +91-9876543210
print(format_phone("5555555555", "+44"))  # +44-5555555555
```

**Output:**
```
+1-1234567890
+91-9876543210
+44-5555555555
```

**Explanation:**
This function formats phone numbers with country codes. The `country_code` parameter defaults to "+1" (United States and Canada), reflecting the largest user base for many applications. The function simply concatenates the country code, a hyphen, and the phone number.

The default "+1" makes it convenient for North American applications while supporting international formatting when needed. In a real application, the default might be determined by:
- User's location/locale
- Business's primary market
- Most common user country

**Key Concept:** Default parameters for localization (country codes, currencies, languages) should reflect the primary audience while allowing internationalization.

---

## Problem 25: Calculate Compound Interest with Default Period

**Problem:** Write a function `compound_interest` that takes principal, rate, time, and an optional n (compounds per year) with default 1. Return the final amount.

**Solution:**
```python
def compound_interest(principal, rate, time, n=1):
    # A = P(1 + r/n)^(nt)
    amount = principal * (1 + rate/100/n) ** (n * time)
    return round(amount, 2)

# Test cases
print(compound_interest(1000, 5, 2))  # 1102.5 (compounded yearly)
print(compound_interest(1000, 5, 2, 4))  # 1104.49 (compounded quarterly)
print(compound_interest(5000, 6, 3))  # 5955.08 (compounded yearly)
print(compound_interest(5000, 6, 3, 12))  # 5983.40 (compounded monthly)
```

**Output:**
```
1102.5
1104.49
5955.08
5983.4
```

**Explanation:**
This function calculates compound interest using the formula: A = P(1 + r/n)^(nt), where:
- P = principal (initial amount)
- r = annual interest rate (as percentage)
- t = time in years
- n = number of times interest compounds per year

The `n` parameter defaults to 1 (annually compounded), which is a simple and common case. Other common values include:
- 1: Annually
- 4: Quarterly
- 12: Monthly
- 365: Daily

The default of 1 provides a baseline calculation, with more frequent compounding available when specified. More frequent compounding results in slightly higher returns due to earning interest on interest more often.

**Key Concept:** Default parameters in mathematical functions should use standard or baseline values that work for simple calculations while supporting advanced options.

---

## Problem 26: Pad String with Default Character

**Problem:** Create a function `pad_string` that takes text, target length, and an optional pad_char with default space " ". Return text padded to target length.

**Solution:**
```python
def pad_string(text, target_length, pad_char=" "):
    current_length = len(text)
    if current_length >= target_length:
        return text
    padding_needed = target_length - current_length
    return text + (pad_char * padding_needed)

# Test cases
print(pad_string("Hello", 10))  # "Hello     "
print(pad_string("Hi", 5, "*"))  # "Hi***"
print(pad_string("Test", 8, "-"))  # "Test----"
print(repr(pad_string("ABC", 7)))  # 'ABC    ' (using repr to show spaces)
```

**Output:**
```
Hello
Hi***
Test----
'ABC    '
```

**Explanation:**
This function pads a string to a specified length with a specified character. The `pad_char` parameter defaults to " " (space), the most common padding character for text alignment. The function:
1. Checks if padding is needed (current length < target length)
2. Calculates how many padding characters are needed
3. Appends the padding to the original text

The default space character is useful for:
- Text alignment in columns
- Fixed-width formatting
- Creating visual spacing

Other padding characters ("-", "*", ".") can be used for different visual effects like table borders or fill lines.

**Key Concept:** Default parameters for formatting should use invisible or neutral characters (like space) that work in most contexts.

---

## Problem 27: Generate Password with Default Length

**Problem:** Define a function `generate_password` that takes an optional length with default 8, and an optional include_numbers with default True. Return a randomly generated password.

**Solution:**
```python
import random
import string

def generate_password(length=8, include_numbers=True):
    # Start with letters
    characters = string.ascii_letters  # a-z, A-Z

    # Add numbers if requested
    if include_numbers:
        characters += string.digits  # 0-9

    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Test cases
print(generate_password())  # e.g., "aB3dE7fG" (8 chars with numbers)
print(generate_password(12))  # e.g., "aBc4DeF8gHiJ" (12 chars with numbers)
print(generate_password(6, False))  # e.g., "aBcdEf" (6 chars, letters only)
print(generate_password(10, True))  # e.g., "A9b3C2d5E1" (10 chars with numbers)
```

**Output:**
```
(Example outputs - will vary due to randomness)
aB3dE7fG
aBc4DeF8gHiJ
aBcdEf
A9b3C2d5E1
```

**Explanation:**
This function generates random passwords with configurable length and character sets. The defaults are:
- `length=8`: Standard minimum password length for security
- `include_numbers=True`: Numbers increase password strength

The function works by:
1. Starting with all ASCII letters (lowercase and uppercase)
2. Adding digits (0-9) if `include_numbers` is True
3. Randomly selecting characters from the available set
4. Joining them into a string of the specified length

The defaults create reasonably secure passwords (8 characters with letters and numbers), while allowing customization for longer passwords or letters-only passwords when needed.

**Key Concept:** Default parameters for security functions should provide secure defaults while allowing customization for specific requirements.

---

## Problem 28: Calculate Tip with Default Percentage

**Problem:** Write a function `calculate_tip` that takes a bill amount and an optional tip_percent with default 15%. Return the tip amount.

**Solution:**
```python
def calculate_tip(bill, tip_percent=15):
    tip_amount = bill * tip_percent / 100
    return tip_amount

# Test cases
print(calculate_tip(100))  # 15.0 (15%)
print(calculate_tip(50, 20))  # 10.0 (20%)
print(calculate_tip(200))  # 30.0 (15%)
print(calculate_tip(75, 18))  # 13.5 (18%)
```

**Output:**
```
15.0
10.0
30.0
13.5
```

**Explanation:**
This function calculates tip amounts based on bill total and tip percentage. The `tip_percent` parameter defaults to 15, which is a standard tip percentage in many countries (particularly in the United States). The calculation is: `bill * tip_percent / 100`.

The default 15% represents:
- A reasonable standard tip for good service
- Easy mental math (roughly 10% + 5%)
- Common cultural expectation

Users can override for:
- Better service (20%, 25%)
- Adequate service (10%)
- Poor service (less than 15%)
- Local customs (different countries have different norms)

**Key Concept:** Default parameters for cultural or regional standards should use common, middle-ground values that can be adjusted based on context.

---

## Problem 29: Filter List with Default Condition

**Problem:** Create a function `filter_numbers` that takes a list and an optional condition with default "positive". Return filtered list based on condition.

**Solution:**
```python
def filter_numbers(numbers, condition="positive"):
    if condition == "positive":
        return [num for num in numbers if num > 0]
    elif condition == "negative":
        return [num for num in numbers if num < 0]
    elif condition == "even":
        return [num for num in numbers if num % 2 == 0]
    else:
        return numbers  # Return as-is if unknown condition

# Test cases
print(filter_numbers([1, -2, 3, -4, 5]))  # [1, 3, 5] (positive)
print(filter_numbers([1, -2, 3, -4, 5], "negative"))  # [-2, -4]
print(filter_numbers([1, 2, 3, 4, 5], "even"))  # [2, 4]
print(filter_numbers([10, -20, 30, -40]))  # [10, 30] (positive by default)
```

**Output:**
```
[1, 3, 5]
[-2, -4]
[2, 4]
[10, 30]
```

**Explanation:**
This function filters a list of numbers based on a specified condition. The `condition` parameter defaults to "positive", assuming the most common filtering need is to extract positive numbers. The function uses list comprehensions with different conditions:
- **"positive"**: Keeps numbers > 0
- **"negative"**: Keeps numbers < 0
- **"even"**: Keeps numbers divisible by 2

The default "positive" is useful because:
- Positive numbers are often the focus in data analysis
- Filtering out negatives (errors, debits) is common
- It provides a sensible baseline behavior

This demonstrates how default parameters can control filtering or selection logic.

**Key Concept:** Default parameters for filter/selection functions should use the most common or useful filtering criterion.

---

## Problem 30: Create Report Header with Defaults

**Problem:** Define a function `create_header` that takes title, an optional width with default 50, and an optional border_char with default "=". Return a formatted header.

**Solution:**
```python
def create_header(title, width=50, border_char="="):
    border = border_char * width
    # Center the title with padding
    centered_title = title.center(width)
    header = f"{border}\n{centered_title}\n{border}"
    return header

# Test cases
print(create_header("Report"))
# ==================================================
#                      Report
# ==================================================

print(create_header("Summary", 30, "-"))
# ------------------------------
#           Summary
# ------------------------------

print(create_header("Results", 40, "*"))
# ****************************************
#                 Results
# ****************************************
```

**Output:**
```
==================================================
                     Report
==================================================
------------------------------
           Summary
------------------------------
****************************************
                Results
****************************************
```

**Explanation:**
This function creates formatted headers for reports or documents. The function has two default parameters:
- `width=50`: Standard width for readable reports
- `border_char="="`: Common character for headers (visually strong)

The function:
1. Creates top border: `border_char` repeated `width` times
2. Centers the title within the width using `.center()`
3. Creates bottom border (same as top)
4. Combines all three with newlines

The defaults create professional-looking headers with equal signs, while allowing customization for:
- Narrower reports (`width=30`)
- Different visual styles (`border_char="-"` for subtler, `"*"` for emphasis)

This demonstrates using multiple defaults to provide complete formatting presets.

**Key Concept:** Multiple default parameters work together to provide complete configuration presets, with each parameter independently customizable.

---

## Summary

### Key Patterns Demonstrated:

1. **Simple Defaults**: Single optional parameter with common value
2. **Multiple Defaults**: Several optional parameters working together
3. **Configuration Defaults**: Standard settings for API/system configuration
4. **Unit/Format Defaults**: Base units or standard formats with conversion logic
5. **Security Defaults**: Safe, recommended settings for security parameters
6. **Business Logic Defaults**: Standard rates, percentages, or options
7. **Localization Defaults**: Regional settings (country codes, currencies)
8. **Formatting Defaults**: Standard characters, widths, or styles

### Best Practices Applied:

1. **Sensible Defaults**: Use common, safe, or standard values
2. **Required First**: Always place required parameters before defaults
3. **Immutable Defaults**: Use immutable types (strings, numbers, None)
4. **Document Defaults**: Make default values clear and meaningful
5. **Consistent Types**: Default value matches parameter's expected type
6. **User-Friendly**: Defaults should work for most use cases
7. **Override Flexibility**: Easy to override when needed
8. **Security-Minded**: Secure defaults (HTTPS, minimum password length)

### Common Use Cases:

- Optional configuration parameters
- Standard units or formats
- Common rates, percentages, or factors
- Default behavior flags
- Formatting preferences
- Regional/localization settings
- Security and validation thresholds
- Backward-compatible new features
