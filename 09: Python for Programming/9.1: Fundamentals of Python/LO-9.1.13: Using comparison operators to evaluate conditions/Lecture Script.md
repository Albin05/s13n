### LO-13 Use Comparison Operators (20 minutes)

### Hook (2 minutes)

**Say**: "Raise your hand if you're 18 or older. How did your brain just make that decision? You compared your age to 18! That's exactly what comparison operators do in Python."

### Introduction to Comparison Operators (6 minutes)

**Say**: "Comparison operators let Python ask questions and get True/False answers."

```python
age = 20
print(age >= 18)  # True
```

**Key Points**:
- Result is always True or False (boolean)
- We're asking: "Is age greater than or equal to 18?"

### Common Operators in Detail (4 minutes)

**Say**: "Double equals checks if two values are the same. VERY different from single equals!"

```python
# Single = assigns
age = 18

# Double == compares
print(age == 18)  # True
print(age == 20)  # False
```

### Real-World Application (3 minutes)

**Say**: "Let's build a simple age checker!"

```python
age = int(input("Enter your age: "))

can_vote = age >= 18
can_drive = age >= 16
is_child = age < 13

print(f"Can vote: {can_vote}")
print(f"Can drive: {can_drive}")
print(f"Is child: {is_child}")
```

### Common Mistakes (3 minutes)

**Say**: "Let me show you the #1 mistake beginners make."

```python
x = 5
if x = 5:  # SyntaxError!
    print("Five")
```

### Practice & Wrap-up (2 minutes)

```python
a = 10
b = 10
print(a == b)
print(a > b)
print(a >= b)
```

