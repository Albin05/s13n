# Question Bank: Override Methods

## Problem 1 (Easy)
Create a base class `Animal` with a method `speak()` that returns "Some sound". Create child classes `Dog` and `Cat` that override `speak()` to return "Woof!" and "Meow!" respectively. Test both animals.

## Problem 2 (Easy)
Create a base class `Product` with attributes `name` and `price`, and a method `display()` that prints the product details. Create a child class `DiscountedProduct` that overrides `display()` to show the original price and a 20% discount applied.

## Problem 3 (Medium)
Create a base class `Account` with attributes `account_number` and `balance`, and a method `withdraw(amount)` that subtracts from balance. Create a child class `SavingsAccount` that overrides `withdraw()` to:
- Prevent withdrawal if balance falls below minimum balance of $100
- Charge a $5 fee if withdrawing below $500
- Allow normal withdrawal otherwise

Test with various withdrawal scenarios.

## Problem 4 (Medium)
Create a base class `Media` with attributes `title` and `duration` (in minutes), and a method `play()` that prints "Playing [title]". Create child classes:
- `Song`: overrides `play()` to show "Playing song: [title] by [artist]" (add artist attribute)
- `Podcast`: overrides `play()` to show "Playing podcast: [title] - Episode [episode_number]" (add episode_number attribute)
- `Video`: overrides `play()` to show "Playing video: [title] in [resolution]" (add resolution attribute)

Create one of each and call their `play()` methods.

## Problem 5 (Hard)
Create a notification system with class hierarchy:
- Base class `Notification` with attributes `message` and `timestamp`, and methods `send()` and `format_message()`
- `EmailNotification`: overrides `send()` to include email-specific logic (to, subject), and `format_message()` to add email headers
- `SMSNotification`: overrides `send()` to include SMS logic (phone_number, character limit of 160), and `format_message()` to truncate if needed
- `PushNotification`: overrides `send()` to include push notification logic (app_name, priority), and `format_message()` to add app badge

Each child class should handle the notification differently while maintaining the same interface. Demonstrate sending all three types of notifications.
