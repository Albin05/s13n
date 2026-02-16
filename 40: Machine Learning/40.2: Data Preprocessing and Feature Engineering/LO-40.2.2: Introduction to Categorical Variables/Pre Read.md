# Introduction to Categorical Variables

## Concept
In Machine Learning datasets, not all data is numerical. Often, we encounter **Categorical Variables**—data that represents distinct groups, classes, or labels rather than quantities.

Since Machine Learning models are essentially mathematical equations ($y = mx + c$), they cannot inherently understand text like "Red," "Blue," or "Green." We must convert these categories into numbers before training a model.

## Types of Categorical Data
1.  **Nominal:** Categories with **no intrinsic order**.
    * *Examples:* Color (Red, Blue), City (New York, Paris), Gender (Male, Female).
    * *Math:* Red < Blue is meaningless.
2.  **Ordinal:** Categories with a **clear, meaningful order**.
    * *Examples:* T-Shirt Size (S, M, L, XL), Rating (Bad, Average, Good), Education (High School, Bachelor's, Master's).
    * *Math:* Small < Medium < Large makes sense.

## Real-World Analogy: The Menu
* **Nominal:** The type of cuisine (Italian, Chinese, Mexican). You can't say "Italian is greater than Chinese."
* **Ordinal:** The spiciness level (Mild, Medium, Hot). "Hot" is definitely greater than "Mild."

## Visualization
!

## External Resources
* [Article: Handling Categorical Data in Python](https://example.com/categorical-data-python)
* [Video: Nominal vs Ordinal Variables](https://example.com/nominal-ordinal-video)
