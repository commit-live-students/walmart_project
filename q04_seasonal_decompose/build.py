# %load q04_seasonal_decompose/build.py
import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
import sys,os
import matplotlib.pyplot as plt
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from pandas.plotting import autocorrelation_plot
from greyatomlib.walmart_project.q01_preprocesssing.build import q01_preprocesssing
plt.switch_backend('agg')

train_df = pd.read_csv("data/train.csv")
df = q01_preprocesssing(train_df)
df_mean = df.resample('W').mean()


def q04_seasonal_decompose(df):
    "write your solution here"
    s= seasonal_decompose(df.Weekly_ales,freq=30)
    a = s.plot()
    return 
