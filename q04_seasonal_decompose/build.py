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



def q04_seasonal_decompose():
    "write your solution here"


