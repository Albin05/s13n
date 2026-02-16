# Introduction to Categorical Variables

## Definition
**Categorical Variable:** A variable that can take on one of a limited, and usually fixed, number of possible values, assigning each individual or other unit of observation to a particular group or nominal category.

## The Two Main Types

| Type | Definition | Order Matters? | Examples | Recommended Encoding |
| :--- | :--- | :--- | :--- | :--- |
| **Nominal** | Named categories without rank. | **No** | Dog/Cat, Yes/No, Red/Blue | One-Hot Encoding |
| **Ordinal** | Categories with a specific hierarchy. | **Yes** | Low/Med/High, 1st/2nd/3rd Place | Label/Ordinal Encoding |

## Common Pitfalls
1.  **Treating Ordinal as Nominal:** If you One-Hot Encode "Size" (S, M, L), you lose the information that L > M. The model has to relearn this relationship from scratch.
2.  **Treating Nominal as Ordinal:** If you encode "City" as Paris=1, London=2, NY=3, the model might think NY is "greater than" Paris (mathematically $3 > 1$), which is false.

## Cardinality
* **High Cardinality:** A categorical feature with many unique values (e.g., Zip Code, User ID). These are hard to handle with One-Hot Encoding as they create too many columns.
* **Low Cardinality:** Few unique values (e.g., Gender, Blood Type).

## Visual Summary
!
