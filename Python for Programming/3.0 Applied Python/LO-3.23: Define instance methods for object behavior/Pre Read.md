# Pre-Read: Define Instance Methods

## Instance Methods

Methods are functions that belong to a class:

```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy")
my_dog.bark()  # Buddy says Woof!
```

## self Parameter

Every instance method needs `self` as first parameter:

```python
class Calculator:
    def __init__(self, value):
        self.value = value
    
    def add(self, num):
        self.value += num
    
    def show(self):
        print(f"Current value: {self.value}")

calc = Calculator(10)
calc.add(5)
calc.show()  # Current value: 15
```

## Methods Can Access Attributes

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        return self.balance

account = BankAccount(100)
account.deposit(50)
print(account.get_balance())  # 150
```
