# Lecture Script: The Remember-Formulate-Predict Framework

## Topic Breakdown

### 1. Why use this framework?
* **Instructor Note:** Ask students how they learned to ride a bike. Did they memorize every pebble on the road? No.
* **Why:** This framework simplifies the complex ML pipeline into intuitive human actions. It maps perfectly to the technical terms: **Data $\to$ Training $\to$ Inference**.

### 2. What are the steps?
* **Step 1: Remember (The Dataset)**
    * The machine needs examples. Just like a child needs to see many dogs to know what a "dog" is.
    * *Technical:* Collecting labeled data $(X, y)$.
* **Step 2: Formulate (The Model)**
    * The machine looks for a mathematical function $f(x)$ that connects inputs to outputs.
    * *Technical:* Finding the weights $w$ such that $y \approx wx + b$. This is the "Learning" phase.
* **Step 3: Predict (The Application)**
    * The machine takes a new input $x_{new}$ and applies the formula.
    * *Technical:* Calculating $\hat{y} = f(x_{new})$.

### 3. How does it look in code?
* **Method:** We will map Python code to these three stages.
* **Code Example:**
    ```python
    # REMEMBER (Data)
    # Past experience: Hours studied vs Marks obtained
    hours = [1, 2, 3, 4, 5]
    marks = [10, 20, 30, 40, 50]

    # FORMULATE (Training)
    # The machine figures out the rule: Marks = 10 * Hours
    def model(h):
        return 10 * h 

    # PREDICT (Inference)
    # Applying the rule to a new situation
    new_hours = 7
    prediction = model(new_hours)
    print(f"Predicted Marks: {prediction}")
    ```

* **Visual Aid:**
    

* **Demo URL:**
    [Google Playground (Simple Regression)](https://playground.tensorflow.org/) - *Show points (Remember) turning into a line (Formulate).*
