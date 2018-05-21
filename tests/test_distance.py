"""
Copyright (c) 2018 Austin Bailie, All rights reserved.
"""
import math
import unittest
import sys
import inspect

from travelingintelligence import distance


class DistanceMeasureTestCase(unittest.TestCase):

    def test_euclidean(self):
        p1 = [(0, 0), (0, 0), (0, 0, 0, 0)]
        p2 = [(1, 1), (2, 2), (1, 0, 0, 0)]
        answers = [math.sqrt(2), math.sqrt(8), 1]
        dm = distance.Euclidean
        for i in range(len(p1)):
            self.assertEqual(dm.distance(p1[i], p2[i]), answers[i])

    def test_taxicab(self):
        p1 = [(0, 0), (0, 0), (0, 0, 0, 0)]
        p2 = [(1, 1), (2, 2), (1, 0, 0, 0)]
        answers = [2, 4, 1]
        dm = distance.TaxiCab
        for i in range(len(p1)):
            self.assertEqual(dm.distance(p1[i], p2[i]), answers[i])


"""
The below lines of code should be included in all sub-test modules.
"""


def suite():
    """
    This method must be included at the end of all sub-test modules. To use in other modules, copy this entire
    method to the new module.
    :return: (unittest.TestSuite) Test suite for this sub-test
    """
    tests = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    loader = unittest.TestLoader()
    full_suite = []
    for test in tests:
        test_suite = loader.loadTestsFromTestCase(test[1])
        full_suite.append(test_suite)
    return unittest.TestSuite(full_suite)


if __name__ == "__main__":
    unittest.main()