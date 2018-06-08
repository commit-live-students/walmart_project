
import pandas as pd
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase

from ..build import q02_test_stationarity
from inspect import getfullargspec
'''

class TestParam2(TestCase):
    def test_param2_args(self):

        # Input parameters tests
        args = getfullargspec(q02_test_stationarity)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args[0])))
'''
