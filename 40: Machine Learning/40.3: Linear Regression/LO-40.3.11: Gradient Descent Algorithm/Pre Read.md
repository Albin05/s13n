# Gradient Descent Algorithm

## Concept
We know that Linear Regression aims to find the line that minimizes the error (MSE). But how does the computer actually *find* this line? It doesn't guess randomly. It uses an optimization algorithm called **Gradient Descent**.

Gradient Descent is an iterative method used to find the minimum value of a function (in our case, the Cost Function). It starts with a random guess and takes small steps in the direction that reduces the error the most.

## Real-World Analogy: The Hiker in the Fog
Imagine you are lost on a mountain at night with thick fog. You can't see the village at the bottom (the Global Minimum), but you want to get there.
1.  **The Method:** You feel the ground with your feet to find which way is "downhill" (The Gradient).
2.  **The Step:** You take a step in that direction.
3.  **The Loop:** You repeat this until the ground becomes flat (you reached the bottom).

## The Learning Rate ($\alpha$)
This parameter controls how big your steps are.
* **Too Small:** You take tiny baby steps. It takes forever to reach the bottom.
* **Too Big:** You take huge jumps. You might jump *over* the valley and land on the other side, missing the bottom entirely (Overshooting).

## Visualization


## External Resources
* [Article: Gradient Descent for Dummies](https://example.com/gd-dummies)
* [Video: Gradient Descent, Step-by-Step](https://example.com/gd-step-by-step)
