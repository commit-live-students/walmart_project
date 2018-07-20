import pandas as pd
from unittest import TestCase
from ..build import q03_autocorrelation_plot
from inspect import getfullargspec

train_df = pd.read_csv("data/train.csv")
from greyatomlib.walmart_project.q01_preprocesssing.build import q01_preprocesssing
df = q01_preprocesssing(train_df)
df_mean = df.resample('W').mean()



class TestParam2(TestCase):
    def test_param2_args(self):

        # Input parameters tests
        args = getfullargspec(q03_autocorrelation_plot)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args[0])))

