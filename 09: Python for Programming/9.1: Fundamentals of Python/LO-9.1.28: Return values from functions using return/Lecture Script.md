### Return Values from Functions Using return (15 minutes)

### Hook (2 minutes)

**Say**: "Functions can send data back to the caller using the return statement. This makes functions truly reusable!"

### What is Return (5 minutes)

```python
def add(a, b):
    return a + b  # Sends back the sum

result = add(5, 3)  # result gets 8
print(result)  # 8
```

**Key Points**:
- `return` sends a value back from the function
- The function exits immediately when return executes
- Return value can be stored in a variable or used directly

### Return vs Print (5 minutes)

**Say**: "print() shows output on screen, return gives you data to use!"

```python
# With print - can't reuse
def add_print(a, b):
    print(a + b)

# With return - reusable
def add_return(a, b):
    return a + b

x = add_return(5, 3)  # x = 8
y = x + 10  # y = 18
```

### Practice (3 minutes)

Write a function that calculates area of a rectangle and returns it.
