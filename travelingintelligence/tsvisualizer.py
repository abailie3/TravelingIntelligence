"""
Copyright (c) 2018 Austin Bailie, All rights reserved.
"""
from typing import List, Tuple


class ProblemVisualizer(object):
    def __init__(self):
        self.target_color = 'b'
        self.origin_color = 'r'
        self.edge_color = 'k'
        pass

    def visualize_2d_solution(self, sequence: List[Tuple]):
        """
        Generates a 2d graph (matplotlib.pyplot) of the problem/solution
        :param sequence: (List[Tuple]) The sequence of points visited.
        :return: (void)
        """
        import matplotlib.pyplot as plt
        points = ProblemVisualizer.__split_tuples__(sequence)

        for i in range(1, len(points[0])):
            print(points[0][i-1:i+1])
            plt.plot(points[0][i-1:i+1], points[1][i-1:i+1], self.edge_color + '-')
        plt.plot([points[0][-1], points[0][0]], [points[1][-1], points[1][0]], self.edge_color + '-')
        plt.plot(points[0][0], points[1][0], self.target_color + 'o')
        plt.plot(points[0][1:], points[1][1:], self.origin_color + 'o')
        plt.show()

    @staticmethod
    def __split_tuples__(sequence: List[Tuple]):
        """
        Splits point sequence (ex. [(0, 1), (1, 0), ...]) into lists of the points' x and y values
            (ex. [[0, 1, ...], [1, 0, ...]])
        :param sequence: (List[Tuple]) Point sequence in form [(x0, y0, z0, ...), (x1, y1, z1, ...),...]
        :return: (List) array of dimensional values in form [[x0, x1, ...], [y0, y1, ...], [z0, z1, ...]...]
        """
        out = []
        if len(sequence) == 0:
            return out
        for i in range(len(sequence[0])):
            ar = []
            for point in sequence:
                ar.append(point[i])
            out.append(ar)
        return out
