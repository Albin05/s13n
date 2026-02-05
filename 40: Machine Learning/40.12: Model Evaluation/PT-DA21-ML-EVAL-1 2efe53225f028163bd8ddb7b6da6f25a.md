# PT-DA21-ML-EVAL-1

[Dataset-:](https://drive.google.com/file/d/12wPwGah96x2IrelrO-uPY2_DvqWoyeVp/view?usp=sharing)

Note -: You are expected to scale data before building the model.

Target to predict is “Price”

1. Handle noise and null value (do not drop them)
2. Keep only numerical values of column “Mileage”
3. Get only numerical values of column “Engine volume”
4. Convert values of column “Gear box type” as follows (”Automatic” to “0”, “Tiptronic” to “1”, “Variator” to “2”, “Manual” to “3”)
5. Convert values of column “Drive wheels” as follows (”Front” to “0”, “Rear” to “1”, “4x4” to “2”)
6. Convert Values of column “Wheel” as follows (”Left wheel” to “0”, “Right-hand drive” to “1”)
7. Convert values of column “Leather interior” as follows ( “Yes” to “1”, “No” to “0”)
8. Column “Levy” values are in form of (base_value **2) so get their original values
9. Get only year value from column “Prod. year”
10. Convert columns datatype to their respective datatype
11. Remove unnecessary columns
12. Get Name of the column which has 3rd least correlation with “Price”
13. Create a linear regression model with columns (”Price”, “Levy”, “Leather interior”, “Engine volume”, “Mileage”, “Cylinders”, “Drive wheels”, “Wheel”, “Airbags” )
14. Get metrics “MAE”, “MSE”, “RMSE”, “R2 Score”, “Adjusted R2 score”