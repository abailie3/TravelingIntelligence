"""
Copyright 2018, Austin Bailie, All rights reserved.

This is the main testing class. All tests should be added to the suite method below.
See other included test modules for notes on how to configure sub-tests.
"""
import unittest

from Tests import test_tsproblem
from Tests import test_bruteforcemethod
from Tests import test_minterface
from Tests import test_distance


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
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest='suite')