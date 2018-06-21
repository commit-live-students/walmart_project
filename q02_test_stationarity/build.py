import pandas as pd
import numpy as np
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
import matplotlib.pyplot as plt
from  statsmodels.tsa.stattools import adfuller
from greyatomlib.walmart_project.q01_preprocesssing.build import q01_preprocesssing

train_df = pd.read_csv("data/train.csv")
df = q01_preprocesssing(train_df)

df_mean = df.resample('W').mean()

def q02_test_stationarity():
    "write your solution here"
    #Determing rolling statistics
    #Plot rolling statistics:    
    #Perform Dickey-Fuller test:
