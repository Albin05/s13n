# Lecture Script: What is Machine Learning?

## Topic Breakdown

### 1. Why do we need Machine Learning?
* **Instructor Note:** Start with a question: "How would you write a program to recognize a cat in a photo?"
* **Why:** Traditional programming scales poorly for complex, fuzzy tasks. You cannot write enough `if-else` statements to cover every angle, lighting condition, or breed of cat. We need a way to automate the creation of these rules.

### 2. What is Machine Learning?
* **Definition:** Arthur Samuel (1959) defined it as "Field of study that gives computers the ability to learn without being explicitly programmed."
* **Core Idea:** It is the science of getting computers to act without being explicitly programmed.
* **Key Components:**
    1.  **Data:** The examples to learn from.
    2.  **Model:** The mathematical engine that learns.
    3.  **Training:** The process of adjusting the model to fit the data.

### 3. How does it work?
* **Method:** We feed data into an algorithm. The algorithm looks for statistical patterns. It outputs a "Model" which can then predict new data.
* **Code Example (Conceptual):**
    Comparison of Logic.

    ```python
    # TRADITIONAL PROGRAMMING (Rule-based)
    def is_spam(email):
        if "free money" in email:
            return True
        if "click here" in email:
            return True
        return False
    
    # MACHINE LEARNING (Data-driven)
    # We don't write rules. We feed data.
    model.train(emails, labels) 
    # The model figures out that "free money" is spam 
    # based on statistics, not our hard-coded lines.
    prediction = model.predict(new_email)
    ```

* **Visual Aid:**
    

* **Demo URL:**
    [Teachable Machine (Google)](https://teachablemachine.withgoogle.com/) - *Show how easy it is to train a model with camera images.*
