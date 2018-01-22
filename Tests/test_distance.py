"""
Copyright 2018, Austin Bailie, All rights reserved.
"""
import unittest
import distance
import math


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
    method to the new module and change the class within the loader.loadTestsFromTestCase(<change>) as appropriate.
    :return: (unittest.TestSuite) Test suite for this sub-test
    """
    loader = unittest.TestLoader()
    return loader.loadTestsFromTestCase(DistanceMeasureTestCase)

if __name__ == "__main__":
    unittest.main()