# The Remember-Formulate-Predict Framework

## Mapping Concepts to ML Terminology

| Framework Step | ML Terminology | Description |
| :--- | :--- | :--- |
| **Remember** | **Dataset / Observations** | The raw material. The machine "remembers" the history of inputs and correct outputs. |
| **Formulate** | **Training / Fitting** | The process of creating a mathematical representation (Model) that explains the history. |
| **Predict** | **Inference / Testing** | The application of the Model to new, unseen data to generate value. |

## The "Formulate" Challenge
The core difficulty of ML lies in the **Formulate** step.
* If we just "Remember" everything, we can't handle new situations (Rote Memorization).
* We must "Formulate" a general rule (Generalization) that works on data we haven't seen yet.

## Equation Form
$$\text{Data} (x, y) \xrightarrow{\text{Formulate}} y = f(x) \xrightarrow{\text{Predict}} \hat{y} = f(x_{new})$$

## Visual Summary
