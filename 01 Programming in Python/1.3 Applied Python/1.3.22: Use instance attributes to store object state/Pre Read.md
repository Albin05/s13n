# Pre-Read: Use Instance Attributes

## Instance Attributes

Attributes are variables that belong to an object:

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

alice = Person("Alice", 25)
print(alice.name)  # Alice
print(alice.age)   # 25
```

## Each Object Has Its Own Attributes

```python
alice = Person("Alice", 25)
bob = Person("Bob", 30)

print(alice.name)  # Alice
print(bob.name)    # Bob
# Different values!
```

## Accessing Attributes

```python
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

my_car = Car("Toyota", 2020)

# Access attributes
print(my_car.brand)  # Toyota
print(my_car.year)   # 2020

# Modify attributes
my_car.year = 2021
print(my_car.year)   # 2021
```
