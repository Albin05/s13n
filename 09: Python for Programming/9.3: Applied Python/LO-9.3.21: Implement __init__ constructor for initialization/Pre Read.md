# Pre-Read: Implement the __init__ Constructor

## What is __init__?

`__init__` is a special method that runs when you create an object:

```python
class Dog:
    def __init__(self, name):
        self.name = name
        print(f"Created dog named {name}")

my_dog = Dog("Buddy")  # Created dog named Buddy
print(my_dog.name)      # Buddy
```

## Why Use __init__?

1. **Initialize data**: Set up object with starting values
2. **Automatic**: Runs automatically when creating object
3. **Customization**: Each object gets different data

## The self Parameter

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Store name in THIS object
        self.age = age    # Store age in THIS object

alice = Person("Alice", 25)
bob = Person("Bob", 30)

print(alice.name)  # Alice
print(bob.name)    # Bob
```

## With and Without __init__

```python
# Without __init__
class Dog:
    pass

dog = Dog()
dog.name = "Buddy"  # Set manually

# With __init__
class Dog:
    def __init__(self, name):
        self.name = name

dog = Dog("Buddy")  # Set automatically
```
