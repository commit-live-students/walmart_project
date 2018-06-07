import pandas as pd
from unittest import TestCase
from ..build import q02_test_stationarity
from inspect import getfullargspec

train_df = pd.read_csv("data/train.csv")
df_mean = df.resample('W').mean()
df = q02_test_stationarity(df_mean)



class TestParam2(TestCase):
    def test_param2_args(self):

        # Input parameters tests
        args = getfullargspec(q02_test_stationarity)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args[0])))
\