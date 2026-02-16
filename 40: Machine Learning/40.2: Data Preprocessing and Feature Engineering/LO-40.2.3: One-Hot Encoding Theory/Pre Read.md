# One-Hot Encoding Theory

## Concept
One-Hot Encoding (OHE) is the standard method for converting **Nominal** categorical data (categories without order) into a numerical format that Machine Learning models can understand.

Instead of assigning a single number to each category (e.g., Red=1, Blue=2), which might confuse the model into thinking there is an order ($2 > 1$), OHE creates a new binary column for **each unique category**.

## Real-World Analogy: The Switchboard
Imagine a survey asking for your favorite color: Red, Green, or Blue.
* **Label Encoding:** You write "1" for Red, "2" for Green. This implies Green is "twice" as good as Red. Bad idea.
* **One-Hot Encoding:** You have a switchboard with 3 switches labeled "Is Red?", "Is Green?", "Is Blue?". You flip the specific switch to ON (1) and the others stay OFF (0).
    * Red $\rightarrow$ `[1, 0, 0]`
    * Green $\rightarrow$ `[0, 1, 0]`
    * Blue $\rightarrow$ `[0, 0, 1]`

## Visualization
!

## External Resources
* [Article: One-Hot Encoding vs Label Encoding](https://example.com/ohe-vs-label)
* [Video: Handling Categorical Data with One-Hot Encoding](https://example.com/ohe-video)
