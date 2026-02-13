# Question Bank: Logic vs Experience

## Q1 (MCQ)
**Problem:** You are building a system to diagnose rare diseases. You have a database of symptoms and outcomes, but no doctor can explain the exact rules for diagnosis because the interactions are too complex. Which approach should you use?
A. Logic-Based (Expert System)
B. Experience-Based (Machine Learning)
C. Random Selection
D. Linear Search

## Q2 (Coding)
**Problem:** Implement a **Logic-based** decision function `get_grade(score)`.
Rules:
* Score >= 90: "A"
* Score >= 80: "B"
* Else: "C"
**Input:** `85`
**Output:** `"B"`

## Q3 (NAT)
**Problem:** A Logic-based system has 5 rules. Each rule takes 10ms to check. An Experience-based system (a neural net) takes a flat 35ms to process the input regardless of complexity. If we need to check all 5 rules, which system is faster and by how much (in ms)?

## Q4 (MSQ)
**Problem:** Which of the following statements are TRUE about **Inductive Reasoning** (The basis of Experience/ML)?
A. It guarantees the conclusion is true if the premises are true.
B. It is based on generalizing from specific observations.
C. It is susceptible to bias if the observations (data) are not representative.
D. It follows a strict top-down approach (General $\to$ Specific).

## Q5 (Coding)
**Problem:** Simulate a simple **Experience-based** learner. You have a list of past outcomes `[0, 1, 1, 1, 0, 1]`. Write a function `predict_next()` that returns the most frequent outcome (the "experience" of the majority).

## Q6 (Subjective)
**Problem:** Why is it dangerous to rely solely on **Experience-based** (ML) systems for tasks like approving loans or hiring employees? Discuss the concept of "Bias in Data" versus "Explicit Rules."
