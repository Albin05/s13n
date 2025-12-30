## Post-class Quiz: Tuple Packing and Unpacking

---

### Question 1
What is the output of the following code?

```python
a, b, c = 1, 2, 3
a, b, c = c, a, b
print(a, b, c)
```

A) 1 2 3  
B) 3 1 2  
C) 2 3 1  
D) 3 2 1

**Correct Answer: B**

*Explanation: The assignment `a, b, c = c, a, b` is evaluated right-to-left. First, the right side creates a tuple (3, 1, 2) using the current values of c, a, b. Then this tuple is unpacked to a, b, c. So a=3, b=1, c=2. This is a rotation pattern.*

---

### Question 2
What will be the value of `rest` after executing this code?

```python
data = (10, 20, 30, 40, 50)
first, *rest, last = data
```

A) `[20, 30, 40]`  
B) `(20, 30, 40)`  
C) `[20, 30, 40, 50]`  
D) `20`

**Correct Answer: A**

*Explanation: The extended unpacking with * collects elements between first and last into a LIST (not a tuple). first gets 10, last gets 50, and rest gets [20, 30, 40]. The * operator always creates a list, even when unpacking from a tuple.*

---

### Question 3
Which of the following statements about tuple packing is TRUE?

A) Parentheses are required to create a tuple  
B) The comma creates the tuple, not the parentheses  
C) You cannot pack different data types together  
D) Tuple packing only works with exactly 2 values

**Correct Answer: B**

*Explanation: In Python, the comma creates the tuple, not the parentheses. `x = 1, 2, 3` creates a tuple just as `x = (1, 2, 3)` does. Parentheses are used for clarity and to resolve precedence, but aren't required for tuple creation. You can pack any number of values of any types.*

---

### Question 4
What happens when you execute this code?

```python
numbers = (1, 2, 3)
a, b = numbers
```

A) a=1, b=2 (3 is ignored)  
B) a=1, b=(2, 3)  
C) ValueError: too many values to unpack  
D) a=(1, 2), b=3

**Correct Answer: C**

*Explanation: When unpacking without the * operator, the number of variables on the left MUST exactly match the number of elements in the sequence. Here we have 2 variables (a, b) but 3 values (1, 2, 3), causing "ValueError: too many values to unpack (expected 2)". To fix this, use extended unpacking: `a, b, *_ = numbers` or `a, *b = numbers`.*

---

### Question 5
What is the output of this code?

```python
def calculate(x, y):
    return x + y, x - y, x * y

result = calculate(10, 5)
print(type(result))
print(len(result))
```

A) `<class 'list'>` and `3`  
B) `<class 'tuple'>` and `3`  
C) `<class 'tuple'>` and `1`  
D) TypeError

**Correct Answer: B**

*Explanation: When a function returns multiple values separated by commas (`return x + y, x - y, x * y`), they are automatically packed into a tuple. So `result` is a tuple containing (15, 5, 50). The type is tuple and it has 3 elements. To use the values separately, you would unpack: `sum_val, diff_val, prod_val = calculate(10, 5)`.*

---

### Bonus Question
What is the value of `middle` after this code executes?

```python
data = (1,)
first, *middle, last = data
```

A) ValueError  
B) `[]`  
C) `[1]`  
D) `()`

**Correct Answer: A**

*Explanation: This causes a ValueError because there aren't enough values to unpack. We need at least 2 values to assign to both `first` and `last`, but the tuple only has 1 element. Extended unpacking with * still requires all non-starred variables to be assigned. To handle this, the tuple needs at least as many elements as non-starred variables.*

