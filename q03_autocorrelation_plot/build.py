import pandas as pd
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from pandas.plotting import autocorrelation_plot
from greyatomlib.walmart_project.q01_preprocesssing.build import q01_preprocesssing

train_df = pd.read_csv("data/train.csv")
df = q01_preprocesssing(train_df)

df_mean = df.resample('W').mean()

def q03_autocorrelation_plot():
    "write your solution here"
