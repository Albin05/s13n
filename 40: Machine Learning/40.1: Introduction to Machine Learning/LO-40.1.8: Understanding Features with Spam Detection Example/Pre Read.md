# Understanding Features with Spam Detection Example

## Concept
In Machine Learning, a **Feature** is an individual measurable property or characteristic of a phenomenon being observed. It is the "input" that the model actually sees.

Raw data (like an email, an image, or a sound wave) is often too complex for a computer to understand directly. We must transform this raw data into a set of numbers called **Features**.

## Real-World Example: Spam Detection
Consider an email: *"CONGRATULATIONS! You have won $1,000,000. Click here to claim."*

A machine doesn't read English. Instead, we extract specific features to help it decide if this is Spam:
1.  **Feature 1 (Word Count):** Does it contain the word "Winner"? (Yes/No $\to$ 1/0)
2.  **Feature 2 (Caps Lock):** What percentage of the text is in ALL CAPS? (e.g., 20%)
3.  **Feature 3 (Links):** How many hyperlinks are in the email? (e.g., 1)
4.  **Feature 4 (Sender):** Is the sender in your contact list? (No $\to$ 0)

The model looks at `[1, 0.2, 1, 0]` and predicts **SPAM**.

## Visualization
[Image of diagram showing raw email text being converted into a feature vector]

## External Resources
* [Article: Feature Engineering for Spam Detection](https://example.com/spam-features)
* [Video: What are Features in ML?](https://example.com/ml-features-video)
