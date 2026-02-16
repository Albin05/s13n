# One-Hot Encoding Theory

## Definition
One-Hot Encoding converts a categorical variable with $N$ categories into $N$ binary (0/1) variables (columns).

## Example Transformation

**Original Dataset:**
| ID | Animal |
| :--- | :--- |
| 1 | Cat |
| 2 | Dog |
| 3 | Bird |

**One-Hot Encoded:**
| ID | Is_Cat | Is_Dog | Is_Bird |
| :--- | :--- | :--- | :--- |
| 1 | 1 | 0 | 0 |
| 2 | 0 | 1 | 0 |
| 3 | 0 | 0 | 1 |

## Key Concepts
1.  **Nominal Data Only:** Use OHE for data *without* order (Gender, City, Color). Do not use for Ordinal data (Size S/M/L) as it loses the ranking information.
2.  **Sparsity:** OHE creates a "Sparse Matrix" (mostly zeros). This can increase memory usage significantly if the cardinality (number of unique categories) is high.
3.  **Dummy Variable Trap:**
    * Occurs when independent variables are highly correlated (perfectly predictable).
    * **Rule:** If a category has $N$ unique values, we strictly only need $N-1$ binary columns to represent it.
    * *Example:* For Gender (Male/Female), we only need `Is_Male`. If `Is_Male = 0`, it is implicitly Female.

## Pros & Cons
* **Pros:** Treats all categories equally; Model interprets correctly.
* **Cons:** Increases dimensionality (Curse of Dimensionality); High memory usage for high cardinality features (e.g., Zip Codes).

## Visual Summary
!
