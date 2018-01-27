"""
Copyright (c) 2018 Austin Bailie, All rights reserved.
"""
import unittest

from travelingintelligence import tsvisualizer as TSV


class TSVisualizerTestCase(unittest.TestCase):

    def test_split_tuples(self):
        """
        Tests the __split_tuples__ method.
        :return: (void)
        """
        points = [(0, 0), (0, 1), (1, 0), (2, 3)]
        x = [0, 0, 1, 2]
        y = [0, 1, 0, 3]
        vis = TSV.ProblemVisualizer()
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
    method to the new module and change the class within the loader.loadTestsFromTestCase(<change>) as appropriate.
    :return: (unittest.TestSuite) Test suite for this sub-test
    """
    loader = unittest.TestLoader()
    return loader.loadTestsFromTestCase(TSVisualizerTestCase)

if __name__ == "__main__":
    unittest.main()