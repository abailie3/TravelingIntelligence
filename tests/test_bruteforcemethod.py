"""
Copyright (c) 2018 Austin Bailie, All rights reserved.
"""
import unittest

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
    method to the new module and change the class within the loader.loadTestsFromTestCase(<change>) as appropriate.
    :return: (unittest.TestSuite) Test suite for this sub-test
    """
    loader = unittest.TestLoader()
    return loader.loadTestsFromTestCase(BruteForceTestCase)

if __name__ == "__main__":
    unittest.main()