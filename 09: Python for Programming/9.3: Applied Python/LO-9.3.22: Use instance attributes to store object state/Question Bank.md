## Question Bank: Use Instance Attributes

---

### Q1: Attribute Access (3 minutes, Low Difficulty)

Create a `Profile` class with `username`, `email`, and `bio` attributes. Write a method `summary()` that returns a formatted string using all three attributes.

**Key Concepts:** Accessing instance attributes with self

---

### Q2: Mutable vs Immutable Attributes (3 minutes, Low Difficulty)

Create a `ShoppingCart` class where each instance has its own `items` list. Demonstrate that adding to one cart doesn't affect another. Explain why `items=[]` as a default parameter would be a bug.

**Key Concepts:** Mutable default argument pitfall, independent instances

---

### Q3: Attribute Modification (5 minutes, Medium Difficulty)

Create a `Counter` class with methods `increment()`, `decrement()`, `reset()`, and `value()`. The counter should not go below zero. Track the total number of increments in a separate attribute.

**Key Concepts:** Modifying attributes, guarding state

---

### Q4: Dynamic Attributes (5 minutes, Medium Difficulty)

Create a `Record` class whose `__init__` accepts `**kwargs` and sets each key-value pair as an instance attribute using `setattr`. Add a `fields()` method that returns all custom attribute names.

**Key Concepts:** setattr, dynamic attributes, __dict__

---

### Q5: Attribute Change Tracking (7 minutes, Medium-High Difficulty)

Create a `TrackedObject` class that logs every attribute change. Override `__setattr__` to append changes to a `_history` list. Provide a `get_history()` method.

**Key Concepts:** __setattr__, attribute interception

