# %load q05_acf_pacf_plot/build.py
import pandas as pd
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
import sys,os
import matplotlib.pyplot as plt
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.walmart_project.q01_preprocesssing.build import q01_preprocesssing
plt.switch_backend('agg')
train_df = pd.read_csv("data/train.csv")
df = q01_preprocesssing(train_df)

df_mean = df.resample('W').mean()

def q05_acf_pacf_plot(df):
    "write your solution here"
    a = plot_acf(df)
    b = plot_pacf(df)
    return
