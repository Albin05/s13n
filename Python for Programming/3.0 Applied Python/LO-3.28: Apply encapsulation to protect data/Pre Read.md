# Pre-Read: Apply Encapsulation

## What is Encapsulation?

Encapsulation means hiding internal details and controlling access to data:

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute (__)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(100)
# account.__balance = 999999  # Won't work! Protected
account.deposit(50)            # Use method instead
print(account.get_balance())   # 150
```

## Why Encapsulation?

1. **Data protection**: Prevent invalid modifications
2. **Control access**: Use methods to manage data
3. **Hide complexity**: Users don't need to know internals

## Public vs Private

```python
class Person:
    def __init__(self, name, ssn):
        self.name = name        # Public (no __)
        self.__ssn = ssn        # Private (__)
    
    def get_ssn(self):
        return "XXX-XX-" + self.__ssn[-4:]

person = Person("Alice", "123-45-6789")
print(person.name)           # OK - public
# print(person.__ssn)        # Error - private!
print(person.get_ssn())      # XXX-XX-6789
```
