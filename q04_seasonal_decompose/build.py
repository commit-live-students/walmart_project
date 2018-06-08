import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from pandas.plotting import autocorrelation_plot
from q01_preprocesssing.build import q01_preprocesssing

train_df = pd.read_csv("data/train.csv")
df = q01_preprocesssing(train_df)

df_mean = df.resample('W').mean()



def q04_seasonal_decompose(df):
    "write your solution here"
    decompose =  df['Weekly_Sales']
    decomposition = seasonal_decompose(decompose)


    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid
    plt.figure(figsize=(16, 7))
    plt.subplot(411)
    plt.plot(df_mean['Weekly_Sales'], label='Original')
    plt.legend(loc='best')
    plt.subplot(412)
    plt.plot(trend, label='Trend')
    plt.legend(loc='best')
    plt.subplot(413)
    plt.plot(seasonal,label='Seasonality')
    plt.legend(loc='best')
    plt.subplot(414)
    plt.plot(residual, label='Residuals')
    plt.legend(loc='best')
    plt.tight_layout()    



