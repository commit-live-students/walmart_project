import pandas as pd
import numpy as np
from pandas.plotting import autocorrelation_plot


def q03_autocorrelation_plot():
    "write your solution here"
    
    plt.figure(figsize=(16, 7))
    autocorrelation_plot(df_mean['Weekly_Sales'])

