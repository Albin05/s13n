
# Editorials

## Q1
### Title
Identification of Data vs Information

### Problem Description
Identify whether a barcode number `5000123` is Data or Information.

### Objective
To distinguish between raw identifiers and contextual meaning.

### Hint
Does the number tell you *what* the product is without looking it up?

### Short Explanation
The number `5000123` is a raw symbol. Without a database to map it to a product name or price, it conveys no meaning. Therefore, it is Data.

### Detailed Explanation
Data is defined as raw characters or numbers lacking context. A barcode number is simply a string of digits. It only becomes "Information" when it is processed by a system that retrieves the associated product name (e.g., "Apple") and price (e.g., "$0.50"). Since the problem specifies the number *alone*, it is Data.

---

## Q2
### Title
Extracting Information from Data (Max Value)

### Problem Description
Find the maximum value from a list of temperatures.

### Objective
Write code to process raw data into a single informative statistic.

### Hint
Use Python's built-in `max()` function or a loop.

### Short Explanation
Iterate through the list or use a built-in function to find the largest integer.

### Detailed Explanation
The raw list `[22, 25, 19, 28, 24]` is data. The "maximum temperature" is a piece of information derived from that data.
```python
def get_max_temp(temps):
    return max(temps)

```

---

## Q3

### Title

Calculating Mean Information

### Problem Description

Calculate the arithmetic mean of `{10, 20, 30, 40, 50}`.

### Objective

Perform a statistical calculation to derive information.

### Hint

Sum the numbers and divide by the count.

### Short Explanation

(10+20+30+40+50) / 5 = 150 / 5 = 30.

### Detailed Explanation

1. **Sum:** 
2. **Count:** 5
3. **Mean:** 
The value 30 is the Information representing the central tendency of the Data.

---

## Q4

### Title

Characteristics of Data and Info

### Problem Description

Select true statements about the relationship between Data and Information.

### Objective

Test conceptual understanding of definitions.

### Hint

Remember: Data -> Processing -> Information.

### Short Explanation

Options B and C are correct. Option A is reversed. Option D is false because a single number (like a credit score) can be information if it has context.

### Detailed Explanation

* **A (False):** Information comes from processing Data, not the other way around.
* **B (True):** Context turns data into information.
* **C (True):** Data is raw input.
* **D (False):** If I say "Your rank is 1", that single number is highly informative because of the context "Rank".

---

## Q5

### Title

Binary Stream Processing

### Problem Description

Process a binary list. Output "Warning" if there are more than 3 consecutive 1s, else "Normal".

### Objective

Implement logic to interpret raw binary data.

### Hint

Iterate through the list and keep a counter that resets when you see a 0.

### Short Explanation

Loop through the array, increment a counter on 1s, reset on 0s. Check if counter > 3.

### Detailed Explanation

```python
def check_status(stream):
    consecutive_ones = 0
    for bit in stream:
        if bit == 1:
            consecutive_ones += 1
            if consecutive_ones > 3:
                return "Warning"
        else:
            consecutive_ones = 0
    return "Normal"

```

Here, the raw stream is Data. The status "Warning" or "Normal" is the derived Information.

### Constraints / Edge Cases

* Empty list: Should return "Normal".
* List with all 1s: Should return "Warning" if length > 3.

---

## Q6

### Title

Data to Features in ML

### Problem Description

Explain why Data must be transformed into Information (Features) for ML.

### Objective

Connect the basic concept to Machine Learning workflows.

### Hint

Think about a picture of a cat. Can a mathematical model understand the raw pixels directly as the concept "cat" without layers of processing?

### Short Explanation

Raw data often contains noise, high dimensionality, or incompatible formats. It must be processed into "features" (Information) that correlates with the target variable.

### Detailed Explanation

In Machine Learning, a model cannot "learn" effectively from raw, unstructured data (like raw text strings or unnormalized pixel values).
**Example:** Predicting house prices.

* **Data:** A text description "Big house with garden".
* **Transformation:** We process this into numerical features (Information) like `Square_Feet=2000`, `Has_Garden=1`.
* **Reason:** The model needs these structured, meaningful inputs (Information) to perform mathematical operations and find patterns.

```

```
