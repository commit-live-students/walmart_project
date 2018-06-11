# Data loading and Preprocessing

- Time series forecasting is an important area in data mining research. Feature preprocessing techniques have significant influence on forecasting accuracy, therefore are essential in a forecasting model. 
- Although several feature preprocessing techniques have been applied in time series forecasting, there is so far no systematic research to study and compare their performance. 


## Write a function `q01_preprocesssing` that :
- Take the dataset and reformat the date column to '%Y-%m-%d'
- Create Year, Month, Day coumns and change the store, Dept column to object
- Add Date column to index and drop the date column


### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| variable | dataframe | compulsory |  | input data |



### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| variable | Dataframe for Data; CSV acceptable by sklearn | dataframe |
