### LO-9 Accept User Input (16 minutes)


### CS Theory Bite

> **Origin**: Interactive input comes from Unix's **stdin/stdout model** (1971). `input()` reads from **standard input** — the same stream whether it's a keyboard, file, or pipe.
>
> **Analogy**: `input()` is like a **waiter taking your order** — the program pauses, listens, and records what you say as a string.
>
> **Why it matters**: User input makes programs interactive — from CLI tools to form validation, input handling is essential.


### Hook (3 minutes)

**Say**: "Want to make programs that talk to users? The input() function makes programs interactive!"

```python
name = input("What's your name? ")
print(f"Hello, {name}!")
```

### Input Basics (5 minutes)

**Say**: "Input() displays a prompt, waits for user to type, then returns what they typed as a string."

```python
name = input("Enter your name: ")
print(f"Welcome, {name}!")

city = input("Where do you live? ")
print(f"{name} lives in {city}")
```

**Key Points**:
- `input()` always returns a string
- The prompt message is optional but helpful
- Program pauses until user presses Enter
- Works in terminal/console programs

### Input with Type Conversion (5 minutes)

**Say**: "Remember: input() gives strings! Convert for math."

```python
# Wrong way
age = input("Enter age: ")
# age + 1  # Error! Can't add string and number

# Right way
age = int(input("Enter age: "))
next_year = age + 1
print(f"Next year you'll be {next_year}")
```

**Common Pattern**:
```python
price = float(input("Enter price: $"))
quantity = int(input("Enter quantity: "))
total = price * quantity
print(f"Total: ${total:.2f}")
```

**Real-World**: Calculators, games, forms - all use input() to interact with users!

### Practice (3 minutes)

Build an interactive calculator:
```python
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
sum_result = num1 + num2
print(f"{num1} + {num2} = {sum_result}")
```
