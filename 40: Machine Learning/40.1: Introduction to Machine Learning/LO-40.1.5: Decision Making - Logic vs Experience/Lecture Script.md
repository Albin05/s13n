# Lecture Script: Decision Making - Logic vs Experience

## Topic Breakdown

### 1. Why distinguish Logic from Experience?
* **Instructor Note:** Ask a student to explain *how* they catch a ball. Can they give you the physics formula? No. They do it from *experience*.
* **Why:** Traditional computers were built on **Logic** (do exactly what I say). Modern AI is built on **Experience** (do what I demonstrated). We need to know when to use which. You don't use ML to calculate taxes (use Logic); you don't use Logic to recognize faces (use ML).

### 2. What is the difference?
* **Logic (Symbolic AI):**
    * **Basis:** Deductive reasoning.
    * **Input:** Rules & Facts.
    * **Pros:** 100% explainable, verifiable.
    * **Cons:** Brittle. If a rule is missing, the system crashes.
* **Experience (Machine Learning):**
    * **Basis:** Inductive reasoning (Generalizing from examples).
    * **Input:** Data (History).
    * **Pros:** Robust. Handles noise and new scenarios.
    * **Cons:** Hard to explain ("Black Box").

### 3. How do we implement them?
* **Method:**
    * **Logic:** `if-else` chains or Switch cases.
    * **Experience:** `model.fit(data)` to minimize error.
* **Code Example:**
    Classifying a Loan Applicant.

    ```python
    # LOGIC APPROACH (Rigid rules)
    def approve_loan_logic(income, credit_score):
        if income > 50000 and credit_score > 700:
            return "Approve"
        else:
            return "Reject"
    
    # EXPERIENCE APPROACH (Weighted pattern)
    # The 'weights' are learned from thousands of past applications
    def approve_loan_ml(income, credit_score):
        # weights learned: w1=0.0002, w2=0.5, bias=-50
        score = (income * 0.0002) + (credit_score * 0.5) - 50
        return "Approve" if score > 0 else "Reject"
    ```

* **Visual Aid:**
    [Image of decision tree representing logic vs neural network representing experience]

* **Demo URL:**
    [Akinator (The Web Genie)](https://en.akinator.com/) - *Show a game that feels like magic (Experience) but is actually a sophisticated decision tree (Logic).*
  
