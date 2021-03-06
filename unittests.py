"""
Copyright (c) 2018 Austin Bailie, All rights reserved.

This is the main testing class. All tests should be added to the suite method below.
See other included test modules for notes on how to configure sub-tests.

Tests must be imported as shown below. Note: Each test module that is added to the "tests" directory must be imported
twice as shown below. This provides support for developers with advanced testing tools and those without.
"""
from tests import test_bruteforcemethod
from tests import test_distance
from tests import test_minterface
from tests import test_tsproblem
from tests import test_tsvisualizer

from tests.test_bruteforcemethod import *
from tests.test_distance import *
from tests.test_minterface import *
from tests.test_tsproblem import *
from tests.test_tsvisualizer import *

import unittest


def suite():
    """
    Compiles all tests into a single test suite to run all at once.
    Sub tests must be imported as above and added to the test suite using suite.addTest(<test_case>.suite())
    :return: (unittest.TestSuite) Returns test suite.
    """
    suite = unittest.TestSuite()
    suite.addTest(test_tsproblem.suite())
    suite.addTest(test_bruteforcemethod.suite())
    suite.addTest(test_minterface.suite())
    suite.addTest(test_distance.suite())
    suite.addTest(test_tsvisualizer.suite())
    return suite


if __name__ == "__main__":
    unittest.main(defaultTest='suite')