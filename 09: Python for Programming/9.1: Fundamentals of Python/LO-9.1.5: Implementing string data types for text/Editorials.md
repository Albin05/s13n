# Editorials: Implement String Data Types

## Problem 1
```python
name = "Alice Johnson"
city = "Boston"
email = "alice@example.com"

info = name + " from " + city + " (" + email + ")"
print(info)
```

## Problem 2
```python
word = "Python"
print(word.upper())    # PYTHON
print(word.lower())    # python
print(word * 3)        # PythonPythonPython
```

## Problem 3
```python
first = "Alice"
middle = "Marie"
last = "Johnson"

full_name = first + " " + middle + " " + last
print(full_name)  # Alice Marie Johnson
```

## Problem 4
```python
email = "user@example.com"

has_at = "@" in email
ends_com = email.endswith(".com")

if has_at and ends_com:
    print("Valid")
```

## Problem 5
```python
text = "Hello"
length = len(text)
border = "*" * (length + 2)

print(border)
print("*" + text + "*")
print(border)
```
