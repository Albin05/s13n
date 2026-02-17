## Lecture Notes: Debug Python Programs Effectively


---

## Introduction

Debugging implements **systematic error detection** - the scientific method applied to code! Before modern debugging tools, programmers used **memory dumps** (print entire memory) and **desk checking** (manually trace code on paper). Modern debugging uses **interactive inspection**, **symbolic execution**, and **automated testing** - dramatically reducing bug-finding time!

### Why Effective Debugging is Critical

**Before systematic debugging** (trial and error): Random changes, hoping bugs disappear:
```python
# Desperate debugging - changing things randomly!
# result = calculate(x, y)  # Try commenting this?
result = calculate(y, x)  # Swap parameters?
# result = calculate(x + 1, y - 1)  # Add random numbers?
# No systematic approach - wastes time!
```

**With systematic debugging** (scientific method): Form hypotheses, test, iterate:
```python
# Systematic debugging - scientific method!
print(f"Before: x={x}, y={y}, type(x)={type(x)}")
result = calculate(x, y)
print(f"After: result={result}")
# Observe, hypothesize, test!
```

**This is the scientific method** - observe, hypothesize, experiment, conclude!

### Historical Context

**The first "bug"**: Grace Hopper (1947) found a moth causing errors in Harvard Mark II computer - literally a bug! Coined the term **"debugging"** - removing bugs from hardware!

**Print debugging**: FORTRAN (1957) introduced FORMAT statements for output - enabling systematic value inspection. Still most common debugging technique today!

**Interactive debuggers**: **LISP** introduced first interactive debugger (1960s). GDB (GNU Debugger, 1986) brought symbolic debugging to C. Python's **pdb** (1992) based on GDB concepts.

**Modern tools**: **IDE debuggers** (1990s) added visual breakpoints, step-through, watch variables. **Logging frameworks** (2000s) replaced ad-hoc printing. **Assertions** (from **Eiffel**, 1986) caught invariant violations.

### Real-World Analogies

**Debugging like medical diagnosis**:
- **Symptoms**: Program behaves wrong (patient feels sick)
- **Tests**: Print statements, debugger (blood tests, X-rays)
- **Diagnosis**: Identify bug location (identify disease)
- **Treatment**: Fix bug (prescribe treatment)
- **Follow-up**: Test fix works (monitor patient)
**Doctors don't guess - they diagnose systematically!**

**Or like detective investigation**:
```python
# Crime scene: bug occurs!
def investigate_bug():
    collect_evidence()  # Print statements
    interview_witnesses()  # Check tracebacks
    form_hypothesis()  # Guess what's wrong
    test_hypothesis()  # Add assertions
    solve_case()  # Fix bug!
```

**Or like car mechanic troubleshooting**:
- **Problem**: Car won't start (program crashes)
- **Check battery**: Print values (check power)
- **Check fuel**: Assert preconditions (check fuel)
- **Check engine**: Debugger step-through (check engine)
**Mechanics use systematic diagnosis, not random part replacement!**

### The Three Error Categories

**1. Syntax Errors** (compile-time): Code won't run
- Python parser catches before execution
- Example: Missing colon, mismatched parens
- **Easy to fix** - Python tells you exactly where!

**2. Runtime Errors** (exceptions): Code crashes during execution
- Caught by Python interpreter
- Example: ZeroDivisionError, KeyError
- **Medium difficulty** - traceback shows location

**3. Logic Errors** (semantic): Code runs but produces wrong results
- **Hardest to find** - no error message!
- Requires understanding expected behavior
- Need systematic testing and debugging

---

### What Is Debugging?

Debugging is finding and fixing errors (bugs) in your code. Three types of errors:

1. **Syntax errors** — code won't run (`SyntaxError`)
2. **Runtime errors** — code crashes during execution (`TypeError`, `ValueError`, etc.)
3. **Logic errors** — code runs but gives wrong results (hardest to find)

---

### Reading Error Messages (Tracebacks)

```python
def calculate(x, y):
    return x / y

def process(data):
    return calculate(data[0], data[1])

process([10, 0])
```

```
Traceback (most recent call last):
  File "app.py", line 7, in <module>
    process([10, 0])
  File "app.py", line 5, in process
    return calculate(data[0], data[1])
  File "app.py", line 2, in calculate
    return x / y
ZeroDivisionError: division by zero
```

**Read bottom to top:**
1. Last line: the error type and message
2. Lines above: the call chain (most recent call last)
3. Each entry: file, line number, function name, and the code

---

### Print Debugging

The simplest technique — add `print()` to see values:

```python
def find_average(numbers):
    print(f"DEBUG: numbers = {numbers}")  # See input
    total = sum(numbers)
    print(f"DEBUG: total = {total}")       # See intermediate
    count = len(numbers)
    print(f"DEBUG: count = {count}")
    average = total / count
    print(f"DEBUG: average = {average}")   # See output
    return average
```

**Tips:**
- Use a prefix like `DEBUG:` so you can find and remove them later
- Print variable types too: `print(f"DEBUG: type={type(x)}, val={x}")`
- Use f-strings for readable output

---

### Using assert for Quick Checks

```python
def calculate_discount(price, percent):
    assert price >= 0, f"Price must be non-negative, got {price}"
    assert 0 <= percent <= 100, f"Percent must be 0-100, got {percent}"
    return price * (1 - percent / 100)
```

`assert` raises `AssertionError` if the condition is False. Great for catching invalid states during development.

---

### The breakpoint() Function (Python 3.7+)

Drops into an interactive debugger:

```python
def process(data):
    result = []
    for item in data:
        breakpoint()  # Pauses here — you can inspect variables
        result.append(item * 2)
    return result
```

In the debugger (`pdb`):
- `n` — next line
- `p variable` — print variable
- `c` — continue execution
- `q` — quit debugger
- `l` — list code around current line

---

### Common Debugging Strategies

**1. Binary Search (Divide and Conquer):**
If your function is long, add a print in the middle. If the output is correct there, the bug is in the second half. Repeat.

**2. Rubber Duck Debugging:**
Explain your code line by line (to a rubber duck, colleague, or yourself). Often you'll spot the error while explaining.

**3. Simplify the Input:**
If a complex input causes a bug, find the simplest input that still triggers it.

**4. Check Your Assumptions:**
```python
# You assume data is a list of ints
print(type(data), type(data[0]))
# Surprise! data[0] is a string
```

---

### Common Bug Patterns

**Off-by-one errors:**
```python
# BUG: range(5) is 0,1,2,3,4 — not 1,2,3,4,5
for i in range(5):
    print(i + 1)  # Fix: or use range(1, 6)
```

**Mutable default arguments:**
```python
# BUG: default list is shared across calls!
def add_item(item, lst=[]):
    lst.append(item)
    return lst

# Fix:
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

**Variable shadowing:**
```python
list = [1, 2, 3]  # BUG: shadows built-in list()
# Later: list("hello") → TypeError!
```

**String vs integer comparison:**
```python
age = input("Age: ")  # Returns string!
if age > 18:  # BUG: comparing string to int
    print("Adult")
# Fix: age = int(input("Age: "))
```

---

### Key Takeaways

1. Read tracebacks **bottom to top** — error type first, then trace the calls
2. `print()` debugging is simple and effective for quick checks
3. `assert` catches invalid states during development
4. `breakpoint()` drops into interactive debugger for complex issues
5. Common bugs: off-by-one, mutable defaults, type confusion, shadowing
6. Strategy: simplify input, check assumptions, binary search
