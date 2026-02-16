# In-Class Quiz

## Question 1
What is the primary purpose of the "Test Set"?
A. To train the model.
B. To evaluate the model's performance on unseen data.
C. To tune the hyperparameters.
D. To provide more data for the training process.

## Question 2
If you set `random_state=42` in `train_test_split`, what happens?
A. The data is split into 42 chunks.
B. The split is random, but repeatable (you get the same random split every time).
C. The split is perfectly ordered (not random).
D. The test set size becomes 42%.

## Question 3
You have a dataset of 1000 emails, where only 10 are spam (1%). If you do a random split, you might end up with 0 spam emails in your Test set. How do you fix this?
A. Use `test_size=0.5`.
B. Use `shuffle=False`.
C. Use `stratify=y` (Stratified Split).
D. Duplicate the data.
