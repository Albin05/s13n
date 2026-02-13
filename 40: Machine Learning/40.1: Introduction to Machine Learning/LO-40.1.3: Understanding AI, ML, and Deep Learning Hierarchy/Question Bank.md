# Question Bank: AI, ML, DL Hierarchy

## Q1 (MCQ)
**Problem:** If a system uses a "Random Forest" algorithm (a statistical technique) to predict house prices, which categories does it fall into?
A. AI only.
B. AI and ML.
C. AI, ML, and DL.
D. DL only.

## Q2 (Coding)
**Problem:** Create a Python class structure to represent the hierarchy.
1.  Create a base class `AI`.
2.  Create a class `ML` that inherits from `AI`.
3.  Create a class `DL` that inherits from `ML`.
4.  Instantiate a `DL` object called `chatgpt`.
5.  Use `isinstance()` to prove `chatgpt` is also an instance of `AI`.

## Q3 (NAT)
**Problem:** Consider a system $S$.
* Set $A$ contains all AI systems.
* Set $M$ contains all ML systems.
* Set $D$ contains all DL systems.
If $S$ is a Convolutional Neural Network (a DL model), how many of the sets $A, M, D$ does $S$ belong to?

## Q4 (MSQ)
**Problem:** Which of the following tasks are specifically best suited for **Deep Learning** rather than traditional Machine Learning?
A. Detecting cancer in high-resolution MRI scans.
B. Calculating the sum of a list of numbers.
C. Real-time language translation (Speech-to-Speech).
D. Predicting housing prices based on 3 simple features (size, rooms, location).

## Q5 (Coding)
**Problem:** Write a function `classify_tech(description)` that returns the *most specific* category ("DL", "ML", or "AI") based on keywords.
* If "Neural Network" or "Layers" in text -> Return "DL".
* If "Learning" or "Data" or "Statistical" in text -> Return "ML".
* If "Rule" or "If-Else" in text -> Return "AI".
* Default -> "Unknown".

## Q6 (Subjective)
**Problem:** "Deep Learning is just Machine Learning with more layers." While technically true, explain why Deep Learning is treated as a distinct revolution. Focus on "Feature Extraction" and "Data Scale".
