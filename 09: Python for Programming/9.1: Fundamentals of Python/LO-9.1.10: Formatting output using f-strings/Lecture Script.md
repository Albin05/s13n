### LO-10 Format Output with F-strings (16 minutes)

### Hook (3 minutes)

**Say**: "Tired of writing `'text' + str(variable) + 'more text'`? F-strings are cleaner and faster!"

```python
# Old way (messy!)
name = "Alice"
age = 25
print("Hi " + name + ", you are " + str(age))

# F-string way (clean!)
print(f"Hi {name}, you are {age}")
```

### F-string Basics (6 minutes)

**Say**: "Put 'f' before the string, then use {variable} to insert values."

```python
name = "Alice"
age = 25
city = "NYC"

print(f"Hi {name}, age {age}, from {city}")
```

**Key Points**:
- Prefix string with `f` (f-string = formatted string)
- Use `{variable}` to embed variables
- Automatically converts types to strings
- Much cleaner than concatenation

```python
score = 95
total = 100
print(f"You scored {score} out of {total}")
```

**Real-World**: Every modern Python app uses f-strings for output!

### Expressions and Formatting (5 minutes)

**Say**: "F-strings can do calculations and format numbers!"

```python
price = 19.99
quantity = 3

# Expressions inside {}
print(f"Total: ${price * quantity}")

# Format decimals with :.2f
print(f"Price: ${price:.2f}")
print(f"Total: ${price * quantity:.2f}")

# Other examples
name = "alice"
print(f"Hello {name.upper()}")  # ALICE
```

**Formatting Options**:
- `:.2f` - Two decimal places
- `:.0f` - No decimal places
- `:,` - Add commas for thousands

### Practice (2 minutes)

Create formatted output:
```python
first = "John"
last = "Doe"
age = 30
salary = 75000.50

print(f"Name: {first} {last}")
print(f"Age: {age}")
print(f"Salary: ${salary:,.2f}")  # $75,000.50
```
