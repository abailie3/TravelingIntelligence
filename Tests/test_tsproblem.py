import unittest
import tsproblem as tsp


class TSProblemTestCase(unittest.TestCase):
    def test_given_points(self):
        points = [(0.2, 0.1), (1, 2), (1e9, -2), (2, 4)]
        prob = tsp.TSProblem()
        prob.setup_problem(points)
        self.assertEqual(prob.targets, [(1, 2), (1e9, -2), (2, 4)])
        self.assertEqual(prob.origin, (0.2, 0.1))

        prob = tsp.TSProblem()
        prob.setup_problem(points, (1, 1))
        self.assertEqual(prob.targets, points)
        self.assertEqual(prob.origin, (1, 1))

    def test_random_points(self):
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

        tmatches = 0
        omatches = 0
        for i in range(len(targets)):
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
        self.assertLess(tmatches/test_length, threshold)
        self.assertLess(omatches/test_length, threshold)

    def test_random_dimmed_points(self):
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

        tmatches = 0
        omatches = 0
        for i in range(len(targets)):
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
        self.assertLess(tmatches/test_length, threshold)
        self.assertLess(omatches/test_length, threshold)

def suite():
    loader = unittest.TestLoader()
    return loader.loadTestsFromTestCase(TSProblemTestCase)

if __name__ == "__main__":
    unittest.main()