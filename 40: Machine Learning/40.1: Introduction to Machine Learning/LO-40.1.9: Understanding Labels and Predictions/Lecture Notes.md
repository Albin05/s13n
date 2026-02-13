# Understanding Labels and Predictions

## Notation
* **$y$ (y):** The Label (Actual Value).
* **$\hat{y}$ (y-hat):** The Prediction (Estimated Value).

## The Relationship
$$Error = | y - \hat{y} |$$
* If $Error = 0$, the model is perfect for that example.
* Machine Learning is the process of minimizing the average Error over many examples.

## When do we have Labels?
| Phase | Do we have Features ($x$)? | Do we have Labels ($y$)? | Do we have Predictions ($\hat{y}$)? |
| :--- | :--- | :--- | :--- |
| **Training** | Yes | **Yes** | Yes (Internal) |
| **Testing** | Yes | **Yes** (Hidden) | Yes |
| **Production** | Yes | **No** | Yes |

## Types of Predictions
1.  **Classification:** Predicting a category (e.g., "Cat" vs "Dog").
    * *Comparison:* Is "Cat" == "Cat"? (Yes/No).
2.  **Regression:** Predicting a number (e.g., Price).
    * *Comparison:* How far is \$105 from \$100?

## Visual Summary
