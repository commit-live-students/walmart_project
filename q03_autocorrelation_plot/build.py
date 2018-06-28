# %load q03_autocorrelation_plot/build.py
import pandas as pd
import sys,os
import matplotlib.pyplot as plt
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from pandas.plotting import autocorrelation_plot
from greyatomlib.walmart_project.q01_preprocesssing.build import q01_preprocesssing
plt.switch_backend('agg')
train_df = pd.read_csv("data/train.csv")
df = q01_preprocesssing(train_df)
df_mean = df.resample('W').mean()

def q03_autocorrelation_plot(df):
    "write your solution here"
    df.index = pd.to_datetime(df.index, unit='s')
    a = autocorrelation_plot(df_mean)
    return 
