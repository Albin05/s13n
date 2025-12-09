# Pre-Read: Define Classes

## What is a Class?

A class is a blueprint for creating objects. Think of it as a template or recipe.

```python
class Dog:
    pass  # Empty class for now

# Create a dog object
my_dog = Dog()
```

## Why Use Classes?

1. **Organization**: Group related data and functions
2. **Reusability**: Create multiple objects from one template
3. **Real-world modeling**: Represent real-world entities

## Basic Example

```python
class Car:
    def start(self):
        print("Engine started")
    
    def stop(self):
        print("Engine stopped")

# Create and use a car
my_car = Car()
my_car.start()  # Engine started
my_car.stop()   # Engine stopped
```

## Class vs Object

- **Class**: The blueprint (Dog class)
- **Object**: The actual instance (my_dog, your_dog)

One class, many objects!

```python
class Dog:
    pass

my_dog = Dog()
your_dog = Dog()
# Same class, different objects
```
