import pandas as pd
from unittest import TestCase
from ..build import q01_preprocesssing
from inspect import getfullargspec

train_df = pd.read_csv("data/train.csv")
df = q01_preprocesssing(train_df)

class TestParam2(TestCase):
    def test_param2_args(self):

        # Input parameters tests
        args = getfullargspec(q01_preprocesssing)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args[0])))


    def test_accuracy_values(self):
        self.assertEqual(df.shape, (421570, 7) ,"Expected shape does not match given shape")

