# PT-DA-20-ML-EVALUATION-1

[Dataset](https://drive.google.com/file/d/1xKQHhRBW_-n-qUPj7rDd3HstzPx_Rzbz/view?usp=sharing)

1. Handle Null’s, Missing values and Noise
2. Column “Item_Fat_Content” has categorical values so convert them into numerical. “Low Fat” as 1, “Regular” as 2, “reg” as 3, “LF” as 4
3. Column “Outlet_Size” has categorical which needs to be converted into numerical as “Medium” as 1, “Small” as 2, “High” as 3
4. Get only  Numerical Values out of column “Outlet_Location_Type”. Example column has value like “Tier 1” then extract the numerical value 1, if it has value “Tier 2” then get numerical value 2.
5. Column “Outlet_Type”  has categorical values that needs to be converted into numerical as  “Supermarket Type1” to 1, “Supermarket Type2” to 2, “Supermarket Type3” to 3, “Grocery Store” to 4
6. By mistake value of column “Item_Outlet_Sales” are in reversed order, you need to get it back in original form. Example we have value like “831.5373 $  __” then its original order will be “__ $ 3735.138”.
7. Clean column “Item_Outlet_Sales” get only numerical values
8. Clean column “Item_Weight” get only numerical values
9. Clean column “Item_MRP” get only numerical values
10. Convert columns to respective datatypes
11. Create a Linear Regression model with help of columns “Item_Weight”, “Item_Fat_Content”, “Item_Visibility”, “Item_MRP”, “Outlet_Establishment_Year”, “Outlet_Size”, “Outlet_Location_Type”, “Outlet_Type” and Predict Item_Outlet_Sales
12. Based on a sample of houses, you have collected the following data:
    
    House area: [1200, 1500, 1800, 2000, 2200]
    Sale price: [250, 320, 390, 410, 450]
    
    Calculate the slope and intercept of the best-fit line using linear regression.