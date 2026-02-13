# Lecture Script: AI, ML, and Deep Learning Hierarchy

## Topic Breakdown

### 1. Why the confusion?
* **Instructor Note:** Draw a big circle labeled "AI". Ask students where "ChatGPT" fits.
* **Why:** Media often calls everything "AI". As engineers, we must be precise. Using a cannon (Deep Learning) to kill a mosquito (a problem solvable by simple rules) is inefficient. We need to know which tool fits which layer.

### 2. What is the Hierarchy?
* **Artificial Intelligence (1950s):**
    * *Definition:* Human intelligence exhibited by machines.
    * *Includes:* Old chess programs that used brute force (Search trees), expert systems (If-Then rules).
* **Machine Learning (1980s):**
    * *Definition:* Algorithms that parse data, learn from it, and make a prediction.
    * *Key:* No explicit rules. The machine finds the rules.
* **Deep Learning (2010s):**
    * *Definition:* Algorithms inspired by the structure and function of the brain called artificial neural networks.
    * *Key:* Automatic feature extraction. You don't tell it "cats have pointy ears"; it figures that out from pixels.

### 3. How do they compare in code?
* **Method:** We will look at the complexity of logic.
* **Code Example:**
    ```python
    # LEVEL 1: AI (Rule-Based / Symbolic AI)
    def get_animal_ai(ears, nose):
        if ears == "pointy" and nose == "wet":
            return "Cat" # Hardcoded rule
            
    # LEVEL 2: ML (Statistical Learning)
    # Uses math (e.g., Logistic Regression) on features we extracted.
    model = LogisticRegression()
    model.fit(features, labels)
    
    # LEVEL 3: Deep Learning (Neural Networks)
    # Uses layers of neurons to find features AND classify.
    model = Sequential([
        Dense(64, activation='relu'), # Hidden Layer 1
        Dense(64, activation='relu'), # Hidden Layer 2 (The "Deep" part)
        Dense(1, activation='sigmoid')
    ])
    ```

* **Visual Aid:**
    [Image of timeline showing the evolution of AI to ML to Deep Learning]

* **Demo URL:**
    [TensorFlow Playground](https://playground.tensorflow.org/) - *Show a neural network learning.*
