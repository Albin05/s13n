# Editorials

## Q1
### Title
Detecting Overfitting

### Problem Description
Identify the scenario requiring regularization.

### Objective
Interpret Training vs Test metrics.

### Hint
Large gap between Training (Good) and Test (Bad).

### Short Explanation
**Scenario C:** The model memorized the training data (99%) but failed to generalize to new data (65%). This is classic Overfitting. Regularization helps close this gap.

### Detailed Explanation
* **A:** Good model (Low bias, low variance).
* **B:** Underfitting (High bias). Needs a more complex model, not regularization.
* **C:** Overfitting (High variance). Needs regularization.
* **D:** Good model.

---

## Q2
### Title
L2 Cost Implementation

### Problem Description
Calculate penalized cost.

### Objective
Implement the math equation.

### Hint
MSE is 0 here. Calculate penalty term.

### Short Explanation
Error = 0. Penalty = $0.1 \times (10^2 + 5^2) = 0.1 \times 125 = 12.5$. Total = 12.5.

### Detailed Explanation
1.  **MSE:** $(1-1)^2 + (2-2)^2 = 0$.
2.  **Penalty:** $10^2 + 5^2 = 100 + 25 = 125$.
3.  **Lambda term:** $0.1 \times 125 = 12.5$.
4.  **Total:** $0 + 12.5 = 12.5$.

---

## Q3
### Title
L1 Cost Calculation

### Problem Description
Calculate cost: $50 + 0.5 \times 100$.

### Objective
Basic arithmetic of penalties.

### Hint
Multiply lambda by sum of weights, add to error.

### Short Explanation
$50 + (0.5 \times 100) = 50 + 50 = 100$.

### Detailed Explanation
$$J = 50 + 0.5(100) = 50 + 50 = 100$$

---

## Q4
### Title
Regularization Properties

### Problem Description
Select true statements about regularization.

### Objective
Verify conceptual understanding.

### Hint
Does it help if the model is too simple (Underfitting)? No.

### Short Explanation
A, C, and D are true. B is false (Regularization usually *increases* bias/underfitting slightly to cure overfitting).

### Detailed Explanation
* **A (True):** Adds $R(w)$.
* **B (False):** It fixes Overfitting, not Underfitting.
* **C (True):** Forces weights towards zero.
* **D (True):** Crucial for "wide" datasets (Features > Samples).

---

## Q5
### Title
Lambda Simulation

### Problem Description
Minimize $J(w) = (w-2)^2 + \lambda w^2$.

### Objective
Observe weight shrinkage.

### Hint
Analytical solution: $dJ/dw = 2(w-2) + 2\lambda w = 0 \Rightarrow w(1+\lambda) = 2 \Rightarrow w = 2/(1+\lambda)$.

### Short Explanation
Calculate optimal $w$ for different lambdas.

### Detailed Explanation
* **$\lambda=0$:** $w = 2/1 = 2$. (Matches target).
* **$\lambda=1$:** $w = 2/2 = 1$. (Shrunk).
* **$\lambda=10$:** $w = 2/11 \approx 0.18$. (Heavily shrunk towards 0).
* *Conclusion:* Higher lambda forces weights closer to 0.

---

## Q6
### Title
Bias-Variance Tradeoff

### Problem Description
Explain why we intentionally add error (bias).

### Objective
Deep theoretical understanding.

### Hint
A perfect score on practice questions doesn't guarantee a pass on the final exam.

### Short Explanation
Regularization intentionally simplifies the model. This adds **Bias** (the model might not fit the training points perfectly anymore), but it significantly reduces **Variance** (the model stops fluctuating wildly based on noise).
* **Result:** The Training Error goes up slightly, but the Test Error (Generalization Error) goes down, which is our actual goal.
