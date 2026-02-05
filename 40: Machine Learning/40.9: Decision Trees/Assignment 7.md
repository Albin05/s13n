# ML Assignment 7

### Part A:

**Questions:**

1. Why is Logistic Regression termed as Regression and not classification?
2. What is a sigmoid function? What does it do?
3. In logistic regression, the sigmoid function is given by f(x) = 1 / (1 + e^(-z)), where z = b0 + b1*x. If the value of b0 is -3 and the value of b1 is 2, what is the predicted probability of y=1 for x=1?
4. In logistic regression, the log loss function is given by L(y, f(x)) = -(y*log(f(x)) + (1-y)*log(1-f(x))). If y=1 and the predicted probability of y=1 is 0.7, what is the value of the log loss function for this observation?
5. Calculate the RMSE and MSE for the below-given data
    
    ![Untitled](ML%20Assignment%207/Untitled.png)
    
6. Calculate the TP, FP, TN, and FN  for the below-given data. Also, calculate the sensitivity, precision, and F1 Score and draw a confusion matrix.

![Untitled](ML%20Assignment%207/Untitled%201.png)

1. Calculate the TPR, FPR, TNR, and FNR for the below table Calculate it for the different threshold values. Research the above-given terms.

![Untitled](ML%20Assignment%207/Untitled%202.png)

### **Part B:**

Dataset : 

- Training Data: [Link](https://drive.google.com/file/d/1HZyknlgIGrwPvZxuVKPR_okvEkcDrjgF/view?usp=share_link)
- Testing Data: [Link](https://drive.google.com/file/d/1SSA7Dzx4vRIb1IwRdI7Aq6IM9cLR5MFl/view?usp=share_link)

### Data Dictionary

- instant: record index
- season : season (1:winter, 2:spring, 3:summer, 4:fall)
- holiday : whether the day is a holiday or not (extracted from
- weekday: day of the week
- workingday: if the day is neither weekend nor holiday is 1, otherwise is 0.
- weathersit:
    - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
    - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
    - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
    - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
- temp: Normalized temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-8, t_max=+39 (only in hourly scale)
- atemp: Normalized feeling temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-16, t_max=+50 (only in hourly scale)
- hum: Normalized humidity. The values are divided into 100 (max)
- windspeed: Normalized wind speed. The values are divided into 67 (max)
- casual: count of casual users
- registered: count of registered users
- cnt: count of total rental bikes including both casual and registered

### Question :

Perform Exploratory Data Analysis on the given dataset and create an ML learning model to predict the count (cnt) of total rental bikes.