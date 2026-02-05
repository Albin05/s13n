# DA-21-C-ML-EVALUATION-3

[Train_](https://drive.google.com/file/d/1IcIT8DrgSxNo0aLt5f8EQ-cpYWP4aweU/view?usp=sharing)

[Test_](https://docs.google.com/spreadsheets/d/1jDmGiCWXZgfZ8BoyAyxihkT7yr4sV3j4/edit?usp=sharing&ouid=101109206230394672482&rtpof=true&sd=true)

NOTE- If you face any encoding issues then simply use **encoding_errors=”ignore” or encoding=”latin-1”**

1.  Handle Noise and Null present in dataset: (don’t drop)
    
     example - Some noise may look like “ **%^9045*^&50 “ and here you have to get only first set of digits
    
2. Column **“datePostedString”** is in **dd-yy** or **mm-yy** format but we want it in **dd-mm-yy** format so here for month you have to **sum dd** and that will be your month (**example 13-2021 is the value then final optput should be like 13-4-2021, here month is sum of 1+3=4 and some where values are like dec-2020 then convert dec into its month number and also to make it a complete date add 01 at starting so final out put will be 01-12-2020**)
3. Column **level** is in text convert to number (some where it is already in number but some where it is like “One Story” or it may be like “One two story” then you have to make it 1 because you have to only check for first numerical letter only and same goes with other values ) **hint-; you can drop rows where keyword “multi” is present**
4. Current value in “Year built” is (base value**2) you have to find its base value replace with current one
5. Convert column “livingAreaValue” in single unit (1 Acre is equal to **43560 Square Feet**.)
6. Check for multi-collinearity and threshold is 70% 
7. Perform outlier analysis and drop them, perform encoding and scaling
8. Create Linear regression model and predict (”Price”)
9. Get all Related metrics
10. Create Logistic regression, decision tree (target variable “is_forAuction”)
11. Get all related metrics and compare