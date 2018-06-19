# %load q01_preprocesssing/build.py
import pandas as pd
import numpy as np
import datetime

train_df = pd.read_csv('data/train.csv')

def q01_preprocesssing(train_df):
    'write your solution here'
    #train_df['Date'] = train_df['Date'].apply(lambda x: x.strftime('%Y-%m-%d'))
    train_df['Year'] = pd.DatetimeIndex(train_df['Date']).year
    train_df['Month'] = pd.DatetimeIndex(train_df['Date']).month
    train_df['Day'] = pd.DatetimeIndex(train_df['Date']).day
    train_df.set_index('Date')
    train_df.drop('Date',axis=1,inplace=True)
    train_df['Store']=train_df['Store'].astype('object')
    train_df['Dept']=train_df['Dept'].astype('object')
    return train_df

q01_preprocesssing(train_df)

