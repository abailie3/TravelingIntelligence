"""
Copyright (c) 2018 Austin Bailie, All rights reserved.
"""
from typing import List, Tuple
import os
import matplotlib
if os.environ.get('DISPLAY','') == '':
    matplotlib.use('Agg')
import matplotlib.pyplot as plt

class ProblemVisualizer(object):
    def __init__(self):
        self.target_color = 'b'
        self.origin_color = 'r'
        self.edge_color = 'k'

    def visualize_2d_solution(self, sequence: List[Tuple]) -> plt:
        """
        Generates a 2d graph (matplotlib.pyplot) of the problem/solution
        :param sequence: (List[Tuple]) The sequence of points visited.
        :return: (matplotlib.pyplot) The plot to show.
        """
        points = ProblemVisualizer.__split_tuples__(sequence)
        for i in range(len(points[0])):
            line = ProblemVisualizer.__line_segment__(points, i)
            plt.plot(line[0], line[1], self.edge_color + '-')
        plt.plot(points[0][0], points[1][0], self.target_color + 'o')
        plt.plot(points[0][1:], points[1][1:], self.origin_color + 'o')
        return plt

    @staticmethod
    def __line_segment__(points: List[List], idx: int) -> List[List]:
        """
        Gets the points for a line segment between the current index and the previous. If the index is 0 then the
        previous index will be the last index.
        :param points: (List[List]) The points in form [[x0, x1, ...], [y0, y1, ...], [z0, z1, ...]...]
        :param idx: (int) The index to get the line segment to.
        :return: (List[List]) The line segment in the form [[x_idx-1, x_idx], [y_idx-1, y_idx], ...]
        """
        out = []
        if idx == 0:
            for dim in points:
                out.append([dim[-1], dim[0]])
            return out
        for dim in points:
            out.append(dim[idx-1:idx+1])
        return out

    @staticmethod
    def __split_tuples__(sequence: List[Tuple]) -> List[List]:
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
