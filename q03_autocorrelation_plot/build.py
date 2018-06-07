import pandas as pd
import numpy as np
from pandas.plotting import autocorrelation_plot
from q01_preprocesssing.build import q01_preprocesssing

train_df = pd.read_csv("data/train.csv")
df = q01_preprocesssing(train_df)

df_mean = df.resample('W').mean()

def q03_autocorrelation_plot(df):
    "write your solution here"
    
    plt.figure(figsize=(16, 7))
    autocorrelation_plot(df['Weekly_Sales'])

