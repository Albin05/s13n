## Question Bank: Implement __init__ Constructor

---

### Q1: Basic Constructor (3 minutes, Low Difficulty)

Create a `Circle` class whose `__init__` takes `radius` and computes `self.area` and `self.circumference` during initialization. Print both for a circle of radius 5.

**Key Concepts:** __init__, computed attributes

---

### Q2: Constructor with Defaults (3 minutes, Low Difficulty)

Create a `Config` class with parameters `host` (default "localhost"), `port` (default 8080), and `debug` (default False). Demonstrate creating instances with different combinations of arguments.

**Key Concepts:** Default parameters in __init__

---

### Q3: Constructor Validation (5 minutes, Medium Difficulty)

Create a `Temperature` class whose `__init__` takes `celsius`. Raise `ValueError` if the value is below absolute zero (-273.15). Add a method `to_fahrenheit()`.

**Key Concepts:** Validation in __init__, raising exceptions

---

### Q4: Constructor with Variable Arguments (5 minutes, Medium Difficulty)

Create a `Team` class whose `__init__` takes a `name` and any number of member names using `*args`. Store members as a list. Add `add_member()` and `__len__()`.

**Key Concepts:** *args in __init__, flexible initialization

---

### Q5: Chained Initialization (7 minutes, Medium-High Difficulty)

Create a `DataFrame` class whose `__init__` accepts either a dict of lists or a list of dicts. Normalize both into a consistent internal format (dict of lists). Provide `rows()` and `columns()` methods.

**Key Concepts:** Flexible constructors, type checking

