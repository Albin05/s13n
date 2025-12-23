### LO-7 Inspect Data Types (10 minutes)

### Hook (3 minutes)

**Say**: "Python needs to know what type of data it's working with. The `type()` function lets us inspect any variable's data type."

```python
age = 25
print(type(age))  # <class 'int'>

name = "Alice"
print(type(name))  # <class 'str'>
```

### Using type() Function (4 minutes)

**Say**: "Type() returns the class/type of any value. Super useful for debugging!"

```python
# Different types
x = 42              # int
y = 3.14            # float
z = "Hello"         # str
w = True            # bool

print(type(x))      # <class 'int'>
print(type(y))      # <class 'float'>
print(type(z))      # <class 'str'>
print(type(w))      # <class 'bool'>
```

**Key Use Cases**:
- Debugging unexpected behavior
- Validating user input types
- Understanding unfamiliar code
- Preventing type-related errors

**Real-World**: When building a calculator, use `type()` to ensure users enter numbers, not text!

### Practice (3 minutes)

Check types of different values:
```python
data = input("Enter something: ")
print(f"You entered: {data}")
print(f"Type: {type(data)}")  # Always 'str' from input!

# That's why we need conversion:
age = int(input("Age: "))
print(type(age))  # Now it's 'int'
```
