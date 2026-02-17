# The Linear Regression Algorithm

## Concept
We have learned the individual components: the **Model** ($y=wx+b$), the **Cost Function** (MSE), and the **Optimizer** (Gradient Descent). Now, we combine them into the full **Linear Regression Algorithm**.

The algorithm is a loop that repeatedly adjusts the line to minimize error.
1.  **Guess:** Start with a random line.
2.  **Measure:** Check how bad the line is (Cost).
3.  **Learn:** Calculate the gradient (direction to improve).
4.  **Update:** Move the line slightly (Learning Rate).
5.  **Repeat:** Do this until the line stops moving (Convergence).

## Real-World Analogy: The Archer
Imagine you are an archer trying to hit a target (The Data) with a laser pointer (The Line).
* **Step 1:** You turn on the laser. It points at the floor (Bad initialization).
* **Step 2:** You see the distance between the dot and the target (Cost).
* **Step 3:** Your brain calculates "I need to aim higher" (Gradient).
* **Step 4:** Your arm moves the laser up slightly (Update).
* **Step 5:** You repeat this micro-adjustment until the dot is on the bullseye.

## Visualization


## External Resources
* [Article: Linear Regression from Scratch](https://example.com/linreg-scratch)
* [Video: The Math of Linear Regression](https://example.com/linreg-math-video)
