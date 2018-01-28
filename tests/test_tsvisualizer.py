"""
Copyright (c) 2018 Austin Bailie, All rights reserved.
"""
import unittest
import numpy as np
from travelingintelligence import tsvisualizer as tsv


class TSVisualizerTestCase(unittest.TestCase):

    def test_visualize_2d_solution(self):
        """
        Tests the visualize_2d_solution method
        NOTE: This test merely tests that the method runs without error.
        :return: (void)
        """
        points = [(0, 0), (0, 1), (1, 0), (2, 3)]
        x = [0, 0, 1, 2]
        y = [0, 1, 0, 3]
        vis = tsv.ProblemVisualizer()
        vis.visualize_2d_solution(points)


    def test_line_segment(self):
        """
        Tests the __line_segment__ method.
        :return: (void)
        """
        points = [[0, 0, 1, 2], [0, 1, 0, 3]]
        segs = [[[2, 0], [3, 0]], [[0, 0], [0, 1]], [[0, 1], [1, 0]], [[1, 2], [0, 3]]]
        vis = tsv.ProblemVisualizer()
        i = 0
        # Test each line segment.
        for seg in segs:
            np.testing.assert_array_equal(seg, vis.__line_segment__(points, i))
            i += 1

    def test_split_tuples(self):
        """
        Tests the __split_tuples__ method.
        :return: (void)
        """
        points = [(0, 0), (0, 1), (1, 0), (2, 3)]
        x = [0, 0, 1, 2]
        y = [0, 1, 0, 3]
        vis = tsv.ProblemVisualizer()
        b = vis.__split_tuples__(points)
        self.assertEqual(len(b), len(points[0]))
        self.assertEqual(b[0], x)
        self.assertEqual(b[1], y)


"""
The below lines of code should be included in all sub-test modules.
"""


def suite():
    """
    This method must be included at the end of all sub-test modules. To use in other modules, copy this entire
    method to the new module and add the correct test classes to the "tests" list.
    :return: (unittest.TestSuite) Test suite for this sub-test
    """
    tests = [TSVisualizerTestCase]  # Add test classes here
    loader = unittest.TestLoader()
    full_suite = []
    for test in tests:
        test_suite = loader.loadTestsFromTestCase(test)
        full_suite.append(test_suite)
    return unittest.TestSuite(full_suite)

if __name__ == "__main__":
    unittest.main()