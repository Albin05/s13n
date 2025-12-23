# Lecture Script: LO-9 Accept User Input

## [0:00-0:02] Hook
**Say**: "Want to make programs that talk to users? That's input()!"

## [0:02-0:07] Input Basics (5 min)
```python
name = input("Name: ")
print("Hello, " + name)
```

## [0:07-0:12] Type Conversion (5 min)
**Show the problem**:
```python
age = input("Age: ")
# age + 1  # Error!
```

**Show the solution**:
```python
age = int(input("Age: "))
```

## [0:12-0:15] Practice (3 min)
Create a calculator that asks for two numbers and adds them.
