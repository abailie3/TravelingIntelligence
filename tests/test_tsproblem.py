"""
Copyright (c) 2018 Austin Bailie, All rights reserved.
"""
import unittest
import sys
import inspect

from travelingintelligence import tsproblem as tsp


class TSProblemTestCase(unittest.TestCase):
    def test_given_points(self):
        """
        Tests the TSProblem class when constructed with given points
        :return: (void)
        """

        # Test given points without an origin
        points = [(0.2, 0.1), (1, 2), (1e9, -2), (2, 4)]
        prob = tsp.TSProblem()
        prob.setup_problem(points)
        self.assertEqual(prob.targets, [(1, 2), (1e9, -2), (2, 4)])
        self.assertEqual(prob.origin, (0.2, 0.1))

        # Test given points with an origin
        prob = tsp.TSProblem()
        prob.setup_problem(points, (1, 1))
        self.assertEqual(prob.targets, points)
        self.assertEqual(prob.origin, (1, 1))

    def test_random_points(self):
        """
        Tests the TSProblem class when constructed without points.
        :return: (void)
        """

        # Create many random TSProblem's.
        prob = tsp.TSProblem()
        targets = []
        origins = []
        test_length = 10
        max_points = 10
        threshold = 0.75
        for i in range(test_length):
            prob.setup_problem(max_points=max_points)
            t = prob.targets
            o = prob.origin
            targets.append(t)
            origins.append(o)

        # See how many of the TSProblem's are matching.
        tmatches = 0
        omatches = 0
        for i in range(len(targets)):
            # Ensure that it created the correct problem sizes.
            self.assertEqual(len(targets[i]), test_length-1)
            self.assertEqual(len(targets[i][0]), 2)
            self.assertEqual(len(origins[i]), 2)
            for j in range(i+1, len(targets)):
                if origins[i] == origins[j]:
                    omatches += 1
                tm1 = 0
                for k in range(len(targets[i])):
                    if targets[i][k] == targets[j][k]:
                        tm1 += 1
                if tm1/len(targets[i]) > 0.9:
                    tmatches += 1

        # Ensure that the class is making random problems.
        self.assertLess(tmatches/test_length, threshold)
        self.assertLess(omatches/test_length, threshold)

    def test_random_dimmed_points(self):
        """
        Tests the TSProblem class when constructed without points and when specifying a point dimension.
        :return: (void)
        """
        # Create many random TSProblem's.
        prob = tsp.TSProblem()
        targets = []
        origins = []
        test_length = 10
        max_points = 10
        threshold = 0.75
        dim = 3
        for i in range(test_length):
            prob.setup_problem(max_points=max_points, dim=dim)
            t = prob.targets
            o = prob.origin
            targets.append(t)
            origins.append(o)

        # See how many of the TSProblem's are matching.
        tmatches = 0
        omatches = 0
        for i in range(len(targets)):
            # Ensure that it created the correct problem sizes.
            self.assertEqual(len(targets[i]), test_length-1)
            self.assertEqual(len(targets[i][0]), dim)
            self.assertEqual(len(origins[i]), dim)
            for j in range(i+1, len(targets)):
                if origins[i] == origins[j]:
                    omatches += 1
                tm1 = 0
                for k in range(len(targets[i])):
                    if targets[i][k] == targets[j][k]:
                        tm1 += 1
                if tm1/len(targets[i]) > 0.9:
                    tmatches += 1

        # Ensure that the class is making random problems.
        self.assertLess(tmatches/test_length, threshold)
        self.assertLess(omatches/test_length, threshold)


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