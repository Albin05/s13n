
# Editorials

## Q1
### Title
Identifying Algorithms

### Problem Description
Select the item that represents an abstract procedure.

### Objective
Distinguish between the method and the result.

### Hint
An algorithm is a set of rules/instructions, not a saved state.

### Short Explanation
"Gradient Descent" is a mathematical optimization procedure (Algorithm). A file with weights is a Model.

### Detailed Explanation
* **A (Model):** Saved weights are the result of learning.
* **B (Algorithm):** Gradient Descent is the method used to update weights.
* **C (Model):** A filter that *has learned* is a model.
* **D (Prediction):** The output of a model.

---

## Q2
### Title
Class Structure Simulation

### Problem Description
Write pseudocode for the Train/Predict workflow.

### Objective
Visualize the code flow: Algo -> Model -> Prediction.

### Hint
`model = algo.train(data)`.

### Short Explanation
Instantiate, call train, capture output, call predict.

### Detailed Explanation
```python
# Instantiate the Algorithm
algo = Algorithm()

# Train to get the Model
model = algo.train([1, 2, 3])

# Use the Model to predict
result = model.predict(4)

```

---

## Q3

### Title

Counting Model Parameters

### Problem Description

Calculate total parameters generated.
Algorithm params (Hyperparameters): 2 (irrelevant to the count of *learned* params).
Learned parameters per model: 5.
Number of models: 3.

### Objective

Understand that each training run generates a unique set of parameters (a unique model).

### Hint

Each model stores its own 5 weights.

### Short Explanation

.

### Detailed Explanation

* The hyperparameters (2) are settings for the algorithm, not part of the learned model's weight count.
* Each training session produces a unique Model instance.
* Each Model contains 5 learned parameters.
* Total: .

---

## Q4

### Title

Model Properties

### Problem Description

Select true statements about the relationship.

### Objective

Clarify common misconceptions about deployment and training.

### Hint

You deploy the "brains" (Model), not the "textbook" (Algorithm).

### Short Explanation

A and C are true. B is false (we deploy the model). D is false (Data changes the Model, not the Algorithm logic).

### Detailed Explanation

* **A (True):** Algorithm = Logic. Model = Learned State.
* **B (False):** We deploy the Model (the object that knows how to predict). Deploying just the algorithm without weights is useless.
* **C (True):** Pre-trained means the heavy lifting (training) is already done.
* **D (False):** The algorithm (e.g., code for Linear Regression) stays the same regardless of data.

---

## Q5

### Title

Simple Average Model

### Problem Description

Implement `avg()` as an algorithm and store results.

### Objective

Demonstrate how one function produces different values based on input.

### Hint

`sum(data) / len(data)`.

### Short Explanation

Calculate averages for two lists and print them.

### Detailed Explanation

```python
def algorithm_avg(data):
    # The logic (Algorithm)
    return sum(data) / len(data)

# The Training
data1 = [10, 20]
data2 = [30, 40]

# The Models (Results)
model1 = algorithm_avg(data1) # 15.0
model2 = algorithm_avg(data2) # 35.0

print(f"Model 1: {model1}, Model 2: {model2}")

```

This shows that `model1` and `model2` are distinct artifacts derived from the same logic.

---

## Q6

### Title

Key Maker Analogy

### Problem Description

Map the Key Maker process to ML.

### Objective

Use an analogy to solidify the concept.

### Hint

The machine copies the pattern.

### Short Explanation

* **The Key Cutting Machine:** The **Algorithm**. It has the mechanics to cut keys but needs a pattern.
* **The Original Key:** The **Data**. It provides the pattern to learn.
* **The Blank Key:** The initialized, empty model.
* **The Cut Key:** The **Model**. It now holds the specific shape (pattern) and can be used to open the lock (Prediction).

### Detailed Explanation

* The machine (Algorithm) follows a procedure: "Trace the original and cut the blank."
* If you put in a different Original Key (Data), the machine (Algorithm) doesn't change, but the resulting Cut Key (Model) will be different.

```

```
