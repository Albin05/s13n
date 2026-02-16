# Train-Test Split

## Concept
In Machine Learning, our goal is not just to do well on the data we have, but to do well on data we *haven't seen yet* (Generalization).

To simulate this "Unseen Data," we split our available dataset into two parts:
1.  **Training Set (The Textbook):** The larger portion (usually 70-80%) used to teach the model. The model sees both the questions (Features) and the answers (Labels).
2.  **Test Set (The Final Exam):** The smaller portion (20-30%) hidden from the model during training. We use it only at the end to evaluate how well the model learned.

## Real-World Analogy: The Exam
Imagine a math teacher gives you 100 practice problems.
* **Bad Approach:** You memorize the answers to all 100 questions. If the exam has the exact same questions, you get 100%. If the exam has *new* numbers, you fail.
* **Good Approach (Train-Test Split):** You study 80 questions (Train) and hide 20 (Test). After studying, you attempt the 20 hidden questions. If you get them right, you know you actually *learned the math*, not just memorized the answers.

## Visualization
![Image of dataset split diagram showing training set and testing set proportions]

## External Resources
* [Article: Why we split data in Machine Learning](https://example.com/train-test-split)
* [Video: Scikit-Learn train_test_split explained](https://example.com/sklearn-split-video)
