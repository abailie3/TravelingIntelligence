"""
Copyright (c) 2018 Austin Bailie, All rights reserved.
"""
import unittest
import sys
import inspect

from travelingintelligence import tsproblem as tsp, bruteforcemethod as BF
from travelingintelligence.distance import Euclidean


class BruteForceTestCase(unittest.TestCase):

    def test_brute_force(self):
        points = [(0, 0), (1, 0), (0, 1), (1, 1)]
        problem = tsp.TSProblem()
        problem.setup_problem(points)
        bf = BF.BruteForce(Euclidean)
        soln_len, seq = bf.solve(problem)
        self.assertEqual(soln_len, 4)

    def test_rest(self):
        points = [1, 2, 35, 3]
        bf = BF.BruteForce(Euclidean)
        result = bf.get_rest(points, 2)
        self.assertEqual(result, [1, 2, 3])
        result = bf.get_rest(points, 0)
        self.assertEqual(result, [2, 35, 3])


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