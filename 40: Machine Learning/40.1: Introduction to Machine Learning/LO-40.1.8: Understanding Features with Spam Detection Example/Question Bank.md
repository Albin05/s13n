# Question Bank: Features and Spam

## Q1 (MCQ)
**Problem:** Which feature would likely have the highest correlation with an email being "Spam"?
A. The email contains the word "the".
B. The email is longer than 10 words.
C. The email contains the phrase "Wire Transfer" and comes from an unknown sender.
D. The email was sent on a Tuesday.

## Q2 (Coding)
**Problem:** Write a function `get_caps_ratio(text)` that calculates the percentage of uppercase characters in a string. This is a common feature for spam detection.
**Input:** `"HELLO world"`
**Output:** `0.45` (approx 5/11)

## Q3 (NAT)
**Problem:** You are extracting features from a batch of 50 emails. You extract 10 distinct features for each email (e.g., word count, link count, etc.). How many total numerical values are in your resulting feature matrix (Dataset)?

## Q4 (MSQ)
**Problem:** Select all valid examples of **Features** for a car price prediction model.
A. The color of the car (converted to a category).
B. The mileage (number of miles driven).
C. The age of the car (Current Year - Model Year).
D. The name of the previous owner's dog.

## Q5 (Coding)
**Problem:** You have a list of "banned words" `['win', 'free', 'money']`. Write a function `count_banned(text)` that returns the number of times any of these words appear in the input text (case-insensitive).

## Q6 (Subjective)
**Problem:** Explain the concept of "Garbage In, Garbage Out" in the context of Feature Engineering. If you choose bad features (e.g., only looking at the first letter of the email), how does that affect the model's ability to learn?
