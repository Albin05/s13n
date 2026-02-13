# Lecture Script: Real-world Applications of Machine Learning

## Topic Breakdown

### 1. Why is ML applied everywhere?
* **Instructor Note:** Ask students, "How many of you used Google Maps or watched a recommended video on YouTube today?"
* **Why:** Traditional algorithms cannot handle the scale and complexity of modern data. You cannot write `if-else` rules for every possible handwritten digit or every possible sentence in English. ML solves this by *learning* the rules.

### 2. What are the major application areas?
* **Computer Vision:**
    * *What:* Teaching computers to "see."
    * *Examples:* Facial recognition (FaceID), Medical Imaging (Cancer detection), Self-driving cars (Lane detection).
* **Natural Language Processing (NLP):**
    * *What:* Teaching computers to "read" and "speak."
    * *Examples:* ChatGPT, Google Translate, Siri/Alexa, Sentiment Analysis.
* **Predictive Analytics:**
    * *What:* Predicting future events based on history.
    * *Examples:* Stock market trends, Weather forecasting, Disease outbreaks.

### 3. How does a Recommendation System work?
* **Method:** It finds patterns in user behavior. "Users who liked A also liked B."
* **Code Example (Collaborative Filtering Logic):**
    ```python
    # Simple dictionary of user preferences
    # 1 means Liked, 0 means Disliked
    user_preferences = {
        'User_A': {'Movie_1': 1, 'Movie_2': 1, 'Movie_3': 0},
        'User_B': {'Movie_1': 1, 'Movie_2': 1, 'Movie_3': ?} 
    }
    
    # Logic: Since User A and User B agreed on Movie 1 and 2,
    # we predict User B will likely DISLIKE Movie 3 (following User A).
    def recommend(user_a, user_b):
        similarity = calculate_similarity(user_a, user_b)
        if similarity > 0.9:
            return user_a['Movie_3']
    ```

* **Visual Aid:**
    

* **Demo URL:**
    [Quick, Draw! (Google AI Experiment)](https://quickdraw.withgoogle.com/) - *Show how ML recognizes doodles in real-time.*
