import unittest

from Tests import test_bruteforcemethod
from Tests import test_tsproblem
from Tests import test_minterface


def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_tsproblem.suite())
    suite.addTest(test_bruteforcemethod.suite())
    suite.addTest(test_minterface.suite())

    return suite

if __name__ == "__main__":
    unittest.main(defaultTest='suite')