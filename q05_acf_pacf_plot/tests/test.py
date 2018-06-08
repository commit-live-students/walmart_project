import pandas as pd
from unittest import TestCase
from ..build import q05_acf_pacf_plot
from inspect import getfullargspec

class TestParam2(TestCase):
    def test_param2_args(self):

        # Input parameters tests
        args = getfullargspec(q05_acf_pacf_plot)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args[0])))

