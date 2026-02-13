# Types of Machine Learning

## Topic Breakdown

### 1. Why do we have different types?
* **Instructor Note:** Ask students, "Can you teach a computer to play Chess the same way you teach it to predict house prices?"
* **Why:** Different problems have different data availability and goals.
    * If we have history (labels), we use **Supervised**.
    * If we have raw chaos (no labels), we use **Unsupervised**.
    * If we have an environment to interact with (games/robotics), we use **Reinforcement**.
    * One approach cannot solve all problems efficiently.

### 2. What are the main types?
* **Supervised Learning:**
    * *Input:* Labeled Data $(X, y)$.
    * *Task:* Map $X \to y$ (Regression or Classification).
    * *Analogy:* Classroom learning with a teacher.
* **Unsupervised Learning:**
    * *Input:* Unlabeled Data $(X)$.
    * *Task:* Find structure (Clustering, Dimensionality Reduction).
    * *Analogy:* Sorting a bucket of mixed coins by size/color without knowing their names.
* **Reinforcement Learning (RL):**
    * *Input:* State, Action, Reward.
    * *Task:* Maximize total reward over time.
    * *Analogy:* Learning to ride a bike (balance = stay up, lean too much = fall).

### 3. How do we choose the right type?
* **Method:** Look at your data and your goal.
    * *Goal:* Predict a value? $\to$ Supervised.
    * *Goal:* Group items? $\to$ Unsupervised.
    * *Goal:* Make a sequence of decisions? $\to$ RL.

* **Code Example (Pseudocode Comparison):**
    ```python
    # SUPERVISED
    model.fit(features, labels) 
    prediction = model.predict(new_data)

    # UNSUPERVISED
    model.fit(features) # No labels!
    groups = model.labels_

    # REINFORCEMENT
    while not done:
        action = agent.decide(state)
        state, reward = environment.step(action)
        agent.learn(reward)
    ```

* **Visual Aid:**
    

* **Demo URL:**
    [Visualizing K-Means (Unsupervised) vs SVM (Supervised)](https://example.com/ml-viz-demo)
