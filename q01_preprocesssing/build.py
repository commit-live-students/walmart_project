import pandas as pd
import numpy as np


train_df = pd.read_csv("data/train.csv")

def q01_preprocesssing(df):
    "write your solution here"
    df = df.copy()
    df.Date =pd.to_datetime(df.Date,format='%Y-%m-%d')
    df['Year'] = pd.DatetimeIndex(df['Date']).year
    df['Month'] = pd.DatetimeIndex(df['Date']).month
    df['Day'] = pd.DatetimeIndex(df['Date']).day.astype('O')
    df['Store'] = df['Store'].astype('O')
    df['Dept'] = df['Dept'].astype('O')
    df.index = df['Date']
    df.drop(['Date'],axis=1,inplace=True)
    return df

