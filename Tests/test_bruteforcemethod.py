"""
Copyright 2018, Austin Bailie, All rights reserved.
"""
import unittest

import bruteforcemethod as BF
import tsproblem as tsp
from distance import Euclidean


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

def suite():
    loader = unittest.TestLoader()
    return loader.loadTestsFromTestCase(BruteForceTestCase)

if __name__ == "__main__":
    unittest.main()