# Pre-Read: Create Objects

## Creating Objects

An object is an instance of a class:

```python
class Book:
    pass

# Create objects (instances)
book1 = Book()
book2 = Book()
book3 = Book()
```

## Each Object is Unique

```python
class Student:
    pass

alice = Student()
bob = Student()

print(alice == bob)  # False - different objects
```

## Why Create Objects?

- Represent individual items (each student, each book)
- Store different data for each instance
- Perform actions on specific instances

## Example: Multiple Cars

```python
class Car:
    def honk(self):
        print("Beep beep!")

car1 = Car()
car2 = Car()

car1.honk()  # Beep beep!
car2.honk()  # Beep beep!
# Same behavior, different objects
```
