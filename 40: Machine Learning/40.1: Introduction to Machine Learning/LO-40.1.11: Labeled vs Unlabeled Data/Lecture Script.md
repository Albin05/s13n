# Lecture Script: Labeled vs Unlabeled Data

## Topic Breakdown

### 1. Why do we need to distinguish them?
* **Instructor Note:** Show two tables. One with a "Price" column (House prediction), one without. Ask students which one allows you to predict *future* prices.
* **Why:** The type of data you have dictates the *type of Machine Learning* you can perform.
    * If you have **Labels**, you do **Supervised Learning** (teaching the machine with answers).
    * If you have **No Labels**, you do **Unsupervised Learning** (asking the machine to find patterns on its own).

### 2. What is the difference?
* **Definition:**
    * **Unlabeled Data:** Input features ($X$) only. We have the questions, but not the answers. Common in raw data collection (e.g., audio recordings).
    * **Labeled Data:** Input features ($X$) + Target variable ($Y$). We have the questions *and* the answers.
* **Analogy:**
    * **Unlabeled:** A stack of practice exams with no answer key. You can group similar questions, but you can't grade yourself.
    * **Labeled:** A stack of practice exams *with* the answer key. You can learn to get the right answer.

### 3. How do we use them?
* **Method:**
    * **Labeled:** We split data into Training (Features + Labels) and Testing. The model minimizes the error between its prediction and the true Label.
    * **Unlabeled:** We feed data to algorithms (like K-Means) to group similar items (Clustering).
* **Code Example:**
    ```python
    import pandas as pd

    # UNLABELED DATA (Features only)
    # We know the size and weight, but not what fruit it is.
    data_unlabeled = pd.DataFrame({
        'weight': [150, 170, 140],
        'texture': ['smooth', 'rough', 'smooth']
    })

    # LABELED DATA (Features + Target)
    # We have the 'Fruit_Name' column which is the Label.
    data_labeled = data_unlabeled.copy()
    data_labeled['Fruit_Name'] = ['Apple', 'Orange', 'Apple']
    
    print("Labeled Data:\n", data_labeled)
    ```

* **Visual Aid:**
    

* **Demo URL:**
    [Teachable Machine: Create Labeled Data Live](https://teachablemachine.withgoogle.com/)
