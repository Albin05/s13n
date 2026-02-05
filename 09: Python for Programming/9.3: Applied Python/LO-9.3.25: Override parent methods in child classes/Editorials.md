# Editorials: Override Methods

## Problem 1
```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Test the classes
dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())
```

### Explanation
- Method overriding means redefining a parent's method in the child class
- When a child defines a method with the same name as the parent, it replaces the parent's version
- Each child class provides its own implementation of `speak()`
- The method signature (name and parameters) must match the parent's method
- This is polymorphism: same method name, different behavior based on object type
- When we call `speak()`, Python uses the version defined in the actual class of the object

## Problem 2
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product: {self.name}")
        print(f"Price: ${self.price}")

class DiscountedProduct(Product):
    def display(self):
        discount = self.price * 0.20
        final_price = self.price - discount
        print(f"Product: {self.name}")
        print(f"Original Price: ${self.price}")
        print(f"Discount (20%): ${discount:.2f}")
        print(f"Final Price: ${final_price:.2f}")

# Test the classes
regular = Product("Laptop", 1000)
discounted = DiscountedProduct("Laptop", 1000)

print("Regular Product:")
regular.display()

print("\nDiscounted Product:")
discounted.display()
```

### Explanation
- The child class completely replaces the parent's `display()` method
- `DiscountedProduct.display()` doesn't call the parent version
- The child has access to all parent attributes (`self.name`, `self.price`)
- This allows customizing behavior while maintaining the same interface
- Both classes have a `display()` method, but they work differently
- The overridden method can add new logic (calculating discount)

## Problem 3
```python
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

class SavingsAccount(Account):
    def withdraw(self, amount):
        # Check if withdrawal would go below minimum
        if self.balance - amount < 100:
            print("Cannot withdraw: Would go below minimum balance of $100")
            return

        # Charge fee if balance is below 500
        if self.balance < 500:
            print("Low balance fee: $5")
            self.balance -= 5

        # Perform withdrawal
        if amount > self.balance:
            print("Insufficient funds (including fees)")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

# Test the classes
print("Regular Account:")
account = Account("12345", 300)
account.withdraw(100)

print("\nSavings Account (balance: $300, withdraw $50):")
savings1 = SavingsAccount("67890", 300)
savings1.withdraw(50)

print("\nSavings Account (balance: $150, withdraw $60):")
savings2 = SavingsAccount("11111", 150)
savings2.withdraw(60)

print("\nSavings Account (balance: $600, withdraw $100):")
savings3 = SavingsAccount("22222", 600)
savings3.withdraw(100)
```

### Explanation
- The overridden method adds additional validation and business rules
- `SavingsAccount.withdraw()` checks minimum balance before allowing withdrawal
- It adds a fee system for low balances
- The child method is more complex than the parent's version
- This demonstrates how overriding allows specialization of behavior
- The method can have early returns to prevent further execution
- Same method interface, but with added constraints specific to savings accounts

## Problem 4
```python
class Media:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def play(self):
        print(f"Playing {self.title}")

class Song(Media):
    def __init__(self, title, duration, artist):
        self.title = title
        self.duration = duration
        self.artist = artist

    def play(self):
        print(f"Playing song: {self.title} by {self.artist}")
        print(f"Duration: {self.duration} minutes")

class Podcast(Media):
    def __init__(self, title, duration, episode_number):
        self.title = title
        self.duration = duration
        self.episode_number = episode_number

    def play(self):
        print(f"Playing podcast: {self.title} - Episode {self.episode_number}")
        print(f"Duration: {self.duration} minutes")

class Video(Media):
    def __init__(self, title, duration, resolution):
        self.title = title
        self.duration = duration
        self.resolution = resolution

    def play(self):
        print(f"Playing video: {self.title} in {self.resolution}")
        print(f"Duration: {self.duration} minutes")

# Test the classes
song = Song("Bohemian Rhapsody", 6, "Queen")
podcast = Podcast("Tech Talk", 45, 12)
video = Video("Python Tutorial", 30, "1080p")

song.play()
print()
podcast.play()
print()
video.play()

# Demonstrate polymorphism
print("\n=== Playing All Media ===")
media_list = [song, podcast, video]
for media in media_list:
    media.play()
    print()
```

### Explanation
- Each child class overrides `play()` with its own unique implementation
- All child classes add extra attributes specific to their media type
- The overridden methods use these additional attributes
- Despite different implementations, all have the same method name
- This enables polymorphism: we can treat all media objects uniformly
- The loop demonstrates calling `play()` on different types without knowing their specific class
- Each class customizes the behavior while maintaining a consistent interface

## Problem 5
```python
from datetime import datetime

class Notification:
    def __init__(self, message):
        self.message = message
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def format_message(self):
        return f"[{self.timestamp}] {self.message}"

    def send(self):
        formatted = self.format_message()
        print(f"Sending notification: {formatted}")

class EmailNotification(Notification):
    def __init__(self, message, to, subject):
        self.message = message
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.to = to
        self.subject = subject

    def format_message(self):
        header = f"To: {self.to}\nSubject: {self.subject}\n"
        body = f"Timestamp: {self.timestamp}\n\n{self.message}"
        return header + body

    def send(self):
        formatted = self.format_message()
        print("=== Sending Email ===")
        print(formatted)
        print("Email sent successfully!\n")

class SMSNotification(Notification):
    def __init__(self, message, phone_number):
        self.message = message
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.phone_number = phone_number

    def format_message(self):
        # Truncate message to 160 characters
        max_length = 160
        if len(self.message) > max_length:
            truncated = self.message[:max_length-3] + "..."
        else:
            truncated = self.message
        return f"SMS to {self.phone_number}: {truncated}"

    def send(self):
        formatted = self.format_message()
        print("=== Sending SMS ===")
        print(formatted)
        print(f"Character count: {len(self.message)}/160")
        print("SMS sent successfully!\n")

class PushNotification(Notification):
    def __init__(self, message, app_name, priority):
        self.message = message
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.app_name = app_name
        self.priority = priority

    def format_message(self):
        badge = "🔴" if self.priority == "high" else "🔵"
        return f"{badge} {self.app_name}\n{self.message}\n{self.timestamp}"

    def send(self):
        formatted = self.format_message()
        print("=== Sending Push Notification ===")
        print(formatted)
        print(f"Priority: {self.priority}")
        print("Push notification sent successfully!\n")

# Test the notification system
email = EmailNotification(
    "Your order has been shipped!",
    "customer@example.com",
    "Order Shipment Confirmation"
)

sms = SMSNotification(
    "Your verification code is 123456. This code will expire in 10 minutes. Please do not share this code with anyone for security purposes.",
    "+1234567890"
)

push = PushNotification(
    "New message from John",
    "ChatApp",
    "high"
)

# Send all notifications
email.send()
sms.send()
push.send()

# Demonstrate polymorphism
print("=== Sending All Notifications via Loop ===")
notifications = [email, sms, push]
for notification in notifications:
    notification.send()
```

### Explanation
- Both `send()` and `format_message()` are overridden in all child classes
- Each child provides notification-type-specific behavior
- `EmailNotification` adds email headers and recipient information
- `SMSNotification` enforces character limits and truncates messages
- `PushNotification` adds priority badges and app information
- All classes maintain the same interface (`send()` method)
- The datetime module is used to add timestamps
- String manipulation is used for formatting (truncation, concatenation)
- Despite different implementations, all notifications can be sent uniformly
- This demonstrates the power of polymorphism with method overriding

**Key Concepts**:
1. **Method overriding** replaces parent method implementation in child class
2. **Same signature**: overridden methods must have the same name and parameters
3. **Complete replacement**: child method completely replaces parent's version
4. **Polymorphism**: different classes can have methods with the same name but different behavior
5. **Specialization**: overriding allows child classes to customize inherited behavior
6. **Interface consistency**: maintaining the same method names enables uniform treatment of objects
