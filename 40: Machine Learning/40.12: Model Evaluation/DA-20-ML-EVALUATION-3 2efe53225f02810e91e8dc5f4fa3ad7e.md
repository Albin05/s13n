# DA-20-ML-EVALUATION-3

[Train_](https://drive.google.com/file/d/1xySBgiRAFBozCfoSavQUa66K7hU7R78o/view?usp=sharing)

[Test_](https://docs.google.com/spreadsheets/d/17qdMc05ZvGbks8K627uVO-k_k5A4vBze/edit?usp=sharing&ouid=101109206230394672482&rtpof=true&sd=true)

1.  Handle Noise and Null  present in dataset: (don’t drop)
    
    Note-: Some noise may look like “ **%^9045*^&50 “ and here you have to get only first set of digits
    
2. Column “datePostedString” is in dd-yy or mm-yy format but we want it in dd-mm-yy format so here for month you have to sum dd and that will be your month (example 13-2021 is the value then final optput should be like 13-4-2021, here month is sum of 1+3=4 and some where values are like dec-2020 then convert dec into its month number and also to make it a complete date add 01 at starting so final out put will be 01-12-2020)

  3. Column level is in text convert to number (some where it is already in number but some where it   is like “One Story” or it may be like “One two story” then you have to make it 1 because you have to only check for first numerical letter only and same goes with other values ) hint-; you can drop row where keyword “multi” is present

1. Current value in “Year built” is (base value**2) you have to find its base value replace with current one
2. Convert column “livingAreaValue” in single unit (1 Acre is equal to **43560 Square Feet**.)
3. Create column zip code by combining  column “stateId”, “countyId”, “cityId”  (but there is a cache that in column “cityId” values are like 32456 then you have to get only values from first even number like from  above value 32456 you have to only get value 2456 because first even number is 2  and if value is 23334 then first even number is 2 so final output is 23334)
4. Remove redundant columns
5. Perform outlier analysis , encoding 
6. Create Linear regression model and predict (”Price”)
7. Get all Related metrics
8. Create Logistic regression, decision tree   (target variable “is_forAuction”)
9. Get all related metrics and compare 
10. 

| TV | Radio | Newspaper | Sales |
| --- | --- | --- | --- |
| 230.1 | 37.8 | 69.2 | 22.1 |
| 44.5 | 39.3 | 45.1 | 10.4 |
| 17.2 | 45.9 | 69.3 | 9.3 |
| 151.5 | 41.3 | 58.5 | 18.5 |
| 180.8 | 10.8 | 58.4 | 12.9 |
| 8.7 | 48.9 | 75.0 | 7.2 |
| ... |  |  |  |

Predict sales when TV = 15.4, Radio = 44.4, Newspaper = 66.5

Can you calculate metrics such as mean squared error (MSE) or root mean squared error (RMSE) to evaluate the model's performance?

1. 

| Passenger Class | Sex | Age | Siblings/Spouses Aboard | Parents/Children Aboard | Fare | Survived |
| --- | --- | --- | --- | --- | --- | --- |
| 3rd | Male | 22 | 1 | 0 | 7.25 | No |
| 1st | Female | 38 | 1 | 0 | 71.2833 | Yes |
| 3rd | Female | 26 | 0 | 0 | 7.925 | Yes |
| 1st | Female | 35 | 1 | 0 | 53.1 | Yes |
| 3rd | Male | 35 | 0 | 0 | 8.05 | No |
| ... |  |  |  |  |  |  |

1. Can you build a random forest classification model to predict whether a passenger survived or not based on the Passenger Class=2nd, Sex=Male, Age=29,  Siblings/Spouses Aboard=4, Parents/Children Aboard=1, Fare=55.7  ? Evaluate the performance of the model using appropriate metrics such as accuracy, precision, recall, or F1-score.

1. Can you calculate feature importance scores and rank the features accordingly?