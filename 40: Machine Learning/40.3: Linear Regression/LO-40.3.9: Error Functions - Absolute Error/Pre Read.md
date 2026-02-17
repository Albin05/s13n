# Error Functions - Absolute Error

## Concept
When evaluating a regression model, we need to quantify "how wrong" the predictions are. The simplest way to do this is by looking at the **Absolute Error**.

* **The Problem with Raw Difference:** If we just sum the differences ($y - \hat{y}$), positive errors (overshooting) and negative errors (undershooting) might cancel each other out, making the model look perfect when it's actually terrible.
    * Example: $+10$ error and $-10$ error sums to $0$.
* **The Solution (Absolute Value):** We take the absolute value $|y - \hat{y}|$ to ensure all errors are positive. We then average these to get the **Mean Absolute Error (MAE)**.

## Real-World Analogy: The Taxi Driver
Imagine a taxi driver charging you based on distance.
* If they drive 5km North, the meter reads 5km.
* If they drive 5km South, the meter reads 5km.
* The meter doesn't care about the *direction* (positive/negative), only the *magnitude*. This is exactly how Absolute Error works. It measures the "Manhattan Distance" or the raw effort needed to fix the mistake.

## Visualization


## External Resources
* [Article: MAE vs MSE](https://example.com/mae-vs-mse)
* [Video: Understanding Error Metrics](https://example.com/error-metrics-video)
