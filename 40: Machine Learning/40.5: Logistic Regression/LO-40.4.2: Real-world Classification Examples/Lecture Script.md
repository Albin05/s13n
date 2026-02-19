# Lecture Script: Real-world Classification Examples

## Topic: Where do we use Classification in the Industry?

### Why (Importance)
As data scientists and machine learning engineers, you are hired to solve business problems. No one pays for "a decision boundary." They pay for a system that automatically blocks spam, detects fraudulent transactions before money is lost, or diagnoses illnesses early. Understanding how to map a real-world business problem to a classification task is the first step in solving it.

### What (Concept)
Today, we look at how the abstract concept of $X$ (features) mapping to $y$ (classes) translates to the real world.
1.  **Binary Classification:** Two possible outcomes (Yes/No, 1/0).
2.  **Multi-class Classification:** More than two possible outcomes (A/B/C).

Let's look at three major industry pillars: Cybersecurity, Healthcare, and Business Operations.

### How (Method / Example)

**Example 1: Cybersecurity (Spam Detection)**
* **The Business Problem:** Users hate spam. It clogs inboxes and poses phishing risks.
* **The ML Mapping:** Binary Classification.
    * $X$ (Features): Words in the email, frequency of ALL CAPS, sender IP address.
    * $y$ (Target): 1 (Spam), 0 (Not Spam).
* **How it works:** The model learns that high frequencies of words like "Winner" and "Urgent" strongly correlate with class 1.

**Example 2: Healthcare (Disease Diagnosis)**
* **The Business Problem:** Doctors need second opinions on medical scans to avoid missing early signs of cancer.
* **The ML Mapping:** Binary Classification.
    * $X$ (Features): Tumor radius, texture, area, perimeter (extracted from biopsies).
    * $y$ (Target): 1 (Malignant/Cancerous), 0 (Benign/Safe).
* **How it works:** The model draws a boundary between safe and dangerous cell patterns. In this domain, we tune our models to avoid *False Negatives* (telling a sick patient they are healthy).

**Example 3: Business Operations (Sentiment Analysis)**
* **The Business Problem:** A company gets 10,000 product reviews a day. They need to know the general mood without reading them all.
* **The ML Mapping:** Multi-class Classification.
    * $X$ (Features): The text of the review.
    * $y$ (Target): Positive, Neutral, Negative.
* **How it works:** The model classifies the text, allowing the business to automatically flag "Negative" reviews for urgent customer support.

### URLs for Demos
* [Google Cloud Vision API Demo (Multi-class Image Classification)](https://cloud.google.com/vision)
