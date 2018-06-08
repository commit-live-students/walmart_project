import pandas as pd
from unittest import TestCase
from ..build import q04_seasonal_decompose
from inspect import getfullargspec



class TestParam2(TestCase):
    def test_param2_args(self):

        # Input parameters tests
        args = getfullargspec(q04_seasonal_decompose)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args[0])))

