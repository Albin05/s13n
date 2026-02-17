# Cost Functions and Optimization

## Concept
In Machine Learning, training a model is essentially an **optimization problem**. We want to find the best set of parameters (weights) that make the model's predictions as accurate as possible.

This process involves two key components:
1.  **The Cost Function (Objective Function):** A mathematical formula that measures "how bad" the model is. It takes the model's predictions and the actual labels and outputs a single number (the Cost).
2.  **The Optimizer:** The algorithm (like Gradient Descent) that adjusts the parameters to minimize the Cost Function.

## Real-World Analogy: The Landscape
Imagine you are standing on a hilly landscape.
* **Location:** Your coordinates (Latitude/Longitude) are the **Parameters** (Weights).
* **Altitude:** The height above sea level is the **Cost**.
* **Goal:** You want to reach the lowest point (Sea Level / Global Minimum).
* **Cost Function:** The map that tells you the altitude for any given location.
* **Optimizer:** The strategy you use to walk downhill (e.g., "Look around and take a step in the steepest downward direction").

## Global vs. Local Minimum
* **Convex Functions:** Like a bowl. There is only one bottom (Global Minimum). Linear Regression usually uses a convex cost function (MSE).
* **Non-Convex Functions:** Like a mountain range with many valleys. You might get stuck in a small valley (Local Minimum) and think you are at the bottom, but there is a deeper valley nearby.

## Visualization
![Image of 3D surface plot showing global minimum vs local minimum]

## External Resources
* [Article: Cost Functions explained](https://example.com/cost-functions)
* [Video: Convex vs Non-Convex Optimization](https://example.com/convex-optimization-video)
