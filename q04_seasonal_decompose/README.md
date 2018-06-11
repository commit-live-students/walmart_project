# Seasonal Decompose

- Time series decomposition involves thinking of a series as a combination of level, trend, seasonality, and noise components.
- Decomposition provides a useful abstract model for thinking about time series generally and for better understanding problems during time series analysis and forecasting.
- Decomposition is primarily used for time series analysis, and as an analysis tool it can be used to inform forecasting models on your problem.
- It provides a structured way of thinking about a time series forecasting problem, both generally in terms of modeling complexity and specifically in terms of how to best capture each of these components in a given model.

## Write a function `q04_seasonal_decompose` that :
- Take the dataset and with the Weekly_Sales columm apply to seasonal_decompose() function and store it to variable.
- Then with the three function trend, seasonal and residue plot a graph 


### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| variable | dataframe | compulsory |  | input data |
