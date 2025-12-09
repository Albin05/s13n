# Pre-Read: Apply Inheritance

## What is Inheritance?

Inheritance lets a class inherit attributes and methods from another class:

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

# Child class inherits from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy")
my_dog.eat()   # Inherited from Animal!
my_dog.bark()  # Defined in Dog
```

## Why Use Inheritance?

1. **Code reuse**: Don't repeat parent functionality
2. **Organization**: Group related classes
3. **Specialization**: Add specific features to child classes

## Example: Vehicles

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} starting...")

class Car(Vehicle):
    def honk(self):
        print("Beep beep!")

class Motorcycle(Vehicle):
    def wheelie(self):
        print("Doing a wheelie!")

car = Car("Toyota")
car.start()  # Inherited!
car.honk()   # Car-specific

bike = Motorcycle("Honda")
bike.start()    # Inherited!
bike.wheelie()  # Motorcycle-specific
```
