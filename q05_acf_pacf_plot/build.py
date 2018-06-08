import pandas as pd
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from q01_preprocesssing.build import q01_preprocesssing

train_df = pd.read_csv("data/train.csv")
df = q01_preprocesssing(train_df)

df_mean = df.resample('W').mean()

def q05_acf_pacf_plot(df):
    "write your solution here"
    series = pd.Series(df['Weekly_Sales'])
    plt.figure(figsize=(20,8))
    plt.subplot(211)
    plot_acf(series, ax=plt.gca())
    plt.subplot(212)
    plot_pacf(series, ax=plt.gca())
    plt.show()    

