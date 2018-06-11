# Test for Stationarity

- A stationary time series is one whose statistical properties such as mean, variance, autocorrelation, etc. are all constant over time. 
- Most statistical forecasting methods are based on the assumption that the time series can be rendered approximately stationary 
-  So in these we will try to plot the stationarity of Weekly_Sales column



## Write a function `q02_test_stationarity` that :
- Takes the processed Data Frame and will use the rolling window method for mean and standard deviation 
- Then with these mean and std plot a graph.
- Use adfuller() function on Weekly_Sales column (use autolag='AIC') and store it in pandas series with index
'Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'
- Use for loop to list out properly


### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| variable | dataframe | compulsory | df_mean | Weekly resampled data |
