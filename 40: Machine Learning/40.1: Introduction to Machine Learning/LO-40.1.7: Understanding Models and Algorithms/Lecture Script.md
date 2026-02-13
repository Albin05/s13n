# Lecture Script: Understanding Models and Algorithms

## Topic Breakdown

### 1. Why distinguish them?
* **Instructor Note:** Ask students, "When you download a file to recognize faces on your phone, are you downloading the 'algorithm' or the 'model'?"
* **Why:** Engineers must communicate precisely. You "run" an algorithm to "train" a model. You "deploy" the model to production.
    * The **Algorithm** is the tool (hammer).
    * The **Model** is what you built (house).

### 2. What is the difference?
* **The Algorithm:**
    * It's the math logic (code).
    * Example: "Find the line $y = mx + c$ that minimizes error."
    * It doesn't change based on data.
* **The Model:**
    * It's the specific numbers found.
    * Example: The specific line $y = 2.5x + 10$.
    * It is unique to the dataset used.
* **Key Insight:** You can use the *same* algorithm on different datasets to create *different* models.

### 3. How do we see this in code?
* **Method:** In Python libraries (like Scikit-Learn), the Class is the Algorithm, and the Instance (after fitting) is the Model.
* **Code Example:**
    ```python
    from sklearn.linear_model import LinearRegression

    # 1. THE ALGORITHM
    # Just a set of uninitialized rules. 
    # It knows HOW to learn, but hasn't learned anything yet.
    algo = LinearRegression()

    # 2. THE DATA
    X = [[1], [2], [3]]
    y = [2, 4, 6]

    # 3. TRAINING (Running the Algorithm on Data)
    algo.fit(X, y)

    # 4. THE MODEL
    # Now 'algo' contains specific knowledge (coefficient = 2).
    # We essentially have the Model: y = 2x
    print(algo.coef_) 
    ```

* **Visual Aid:**
    

* **Demo URL:**
    [Teachable Machine](https://teachablemachine.withgoogle.com/) - *Show that the "Trainer" is the algorithm, and the "Downloadable File" is the model.*
