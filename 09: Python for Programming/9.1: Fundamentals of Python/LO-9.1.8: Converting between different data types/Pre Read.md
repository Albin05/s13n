# Pre-Read: Convert Between Data Types

## Why Convert Types?

User input is always a string - need to convert for math!

```python
age = input("Age: ")  # Returns string "25"
# age + 5  # Error - can't add string and int
age_int = int(age)    # Convert to int
next_year = age_int + 1  # Works!
```

### The Core Problem

Computers are very literal. To them:
- The **text** "25" (two characters: '2' and '5')
- The **number** 25 (a quantity: twenty-five)

...are completely different things stored in completely different ways!

When you type "25" in response to `input()`, the computer sees text characters. To do math, you must convert that text into an actual number.

### Simple Analogy

Think of data types like different **forms of measurement**:
- "25" (string) is like saying "twenty-five" out loud
- 25 (int) is like holding 25 physical coins
- 25.0 (float) is like a measuring cup showing 25 milliliters

All represent the same quantity, but in different "formats". To use them together, you need to convert to a common format.

**Another analogy**: File formats
- A Word document (.docx)
- A PDF file (.pdf)
- A text file (.txt)

They might contain the same text, but they're stored differently. You need conversion tools to change between them. Same with data types!

## Conversion Functions

### To Integer
```python
int("25")      # 25
int(25.9)      # 25 (truncates)
int(True)      # 1
```

### To Float
```python
float("3.14")  # 3.14
float(5)       # 5.0
```

### To String
```python
str(25)        # "25"
str(3.14)      # "3.14"
str(True)      # "True"
```

### To Boolean
```python
bool(1)        # True
bool(0)        # False
bool("text")   # True
bool("")       # False
```

## Try It
```python
age_str = "25"
age_int = int(age_str)
age_float = float(age_int)
print(type(age_float))  # <class 'float'>
```
