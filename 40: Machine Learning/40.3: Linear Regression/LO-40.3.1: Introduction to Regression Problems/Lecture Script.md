# Lecture Script: Introduction to Regression Problems

## Topic Breakdown

### 1. Why do we need Regression?
* **Instructor Note:** Ask students to look at the stock market or weather forecast. Do they just say "Up/Down" or do they give a number?
* **Why:** The world is quantifiable. We don't just want to know *if* it will rain (Classification); we want to know *how much* rain (Regression) to build the right drainage. We need precision.

### 2. What is a Regression Problem?
* **Definition:** A task where the target variable $y$ is continuous ($y \in \mathbb{R}$).
* **Key Characteristics:**
    * The output is a number, not a class.
    * There is an infinite number of possible outputs.
    * We measure error by "distance" (how far off was the number?), not just accuracy (right/wrong).
* **Examples:**
    * Predicting Salary based on Years of Experience.
    * Predicting Height based on Age.

### 3. How do we solve it?
* **Method:** We find a mathematical function $f(x)$ that outputs a number close to the actual $y$.
* **Code Example:**
    A simple dummy regression model.
    ```python
    # Input: Hours studied
    X = [1, 2, 3, 4, 5]
    
    # Target: Exam Score (Regression)
    y = [10, 20, 30, 40, 50]
    
    # The Model (Function)
    def simple_regression_model(hours):
        # We learned that score is roughly 10x hours
        return hours * 10
    
    prediction = simple_regression_model(6)
    print(f"Predicted Score: {prediction}") 
    # Output: 60 (A continuous number)
    ```

* **Visual Aid:**
    !

* **Demo URL:**
    [Teachable Machine (Regression Mode)](https://teachablemachine.withgoogle.com/)
