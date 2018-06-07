import pandas as pd
import numpy as np
from  statsmodels.tsa.stattools import adfuller


df_mean = df.resample('W').mean()
df_mean


def q02_test_stationarity(x):
    "write your solution here"
    
    #Determing rolling statistics
    rolmean = x.rolling(window=2, center=False).mean()
    rolstd = x.rolling(window=2, center=False).std()

    #Plot rolling statistics:
    plt.figure (figsize=(17, 12))
    orig = plt.plot(x, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='green', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.grid()
    plt.xticks(rotation=90)
    plt.locator_params(nbins=60, axis = 'x')
    
    #Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    tstest = adfuller(x['Weekly_Sales'], autolag='AIC')
    tsoutput = pd.Series(tstest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in tstest[4].items():
        tsoutput['Critical Value (%s)' % key] = value
    print(tsoutput)
    

