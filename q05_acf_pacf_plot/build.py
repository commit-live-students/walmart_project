import pandas as pd
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf


def q05_acf_pacf_plot():
    "write your solution here"
    series = pd.Series(df_mean['Weekly_Sales'])
    plt.figure(figsize=(20,8))
    plt.subplot(211)
    plot_acf(series, ax=plt.gca())
    plt.subplot(212)
    plot_pacf(series, ax=plt.gca())
    plt.show()    

