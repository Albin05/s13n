## Post-class Quiz: Create Custom Exception Classes

---

### Question 1
What should a custom exception class inherit from?

A) `object`
B) `Exception` or a built-in exception subclass
C) `Error`
D) `BaseException`

**Correct Answer: B**

*Explanation: Custom exceptions should inherit from `Exception` or one of its subclasses like `ValueError`, `TypeError`, etc. `BaseException` is too broad (includes `SystemExit`, `KeyboardInterrupt`).*

---

### Question 2
What is the purpose of calling `super().__init__(message)` in a custom exception?

A) To create the error message string
B) To register the exception with Python
C) To initialize the parent Exception class with the message
D) It's optional and not needed

**Correct Answer: C**

*Explanation: `super().__init__(message)` passes the message to the Exception base class, which stores it and makes it available via `str(e)` and when the exception is printed.*

---

### Question 3
What is the advantage of exception hierarchies?

A) They run faster
B) You can catch a group of related exceptions with one except block
C) They use less memory
D) Python requires them

**Correct Answer: B**

*Explanation: With a hierarchy like `AppError → DatabaseError, NetworkError`, catching `AppError` catches all subtypes. This lets you handle related errors together or separately as needed.*

---

### Question 4
Which is a valid custom exception?

A) `class MyError: pass`
B) `class MyError(Exception): pass`
C) `class MyError(str): pass`
D) `def MyError(): raise Exception()`

**Correct Answer: B**

*Explanation: Custom exceptions must be classes inheriting from Exception. Option A doesn't inherit from Exception. Option C inherits from str. Option D is a function, not a class.*

---

### Question 5
When should you create custom exceptions?

A) For every error in your code
B) When built-in exceptions don't describe your specific error well
C) Only for user-facing errors
D) Never — built-in exceptions are sufficient

**Correct Answer: B**

*Explanation: Create custom exceptions when you need to carry specific data (like account balance), when you want precise error handling (catching specific app errors), or when built-in types are too generic.*

---
