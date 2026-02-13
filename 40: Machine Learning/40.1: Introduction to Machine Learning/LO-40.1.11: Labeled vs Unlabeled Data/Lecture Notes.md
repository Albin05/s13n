# Labeled vs Unlabeled Data

## Key Definitions
* **Unlabeled Data:** Raw information containing only input variables (features).
    * *Notation:* $X$
* **Labeled Data:** Information containing input variables (features) AND a specific output variable (target/label).
    * *Notation:* $(X, y)$

## Comparison Table
| Feature | Unlabeled Data | Labeled Data |
| :--- | :--- | :--- |
| **Components** | Inputs only | Inputs + Outputs (Tags) |
| **Availability** | Abundant, cheap to collect | Scarce, expensive (requires humans) |
| **ML Type** | Unsupervised Learning | Supervised Learning |
| **Goal** | Find structure/patterns | Predict outcome/Classify |
| **Example** | Audio files | Audio files + Transcripts |

## Code Snippet: Structure
```python
# Labeled Dataset (for Supervised Learning)
dataset = [
    ([5.1, 3.5, 1.4, 0.2], "Setosa"),      # ([Features], Label)
    ([4.9, 3.0, 1.4, 0.2], "Setosa"),
    ([7.0, 3.2, 4.7, 1.4], "Versicolor")
]

# Unlabeled Dataset (for Unsupervised Learning)
dataset_raw = [
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [7.0, 3.2, 4.7, 1.4]
]
