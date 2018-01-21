"""
Copyright 2018, Austin Bailie, All rights reserved.
"""
import random


class TSProblem(object):
    """
    A class for holding a traveling salesman problem
    """
    def __init__(self):
        self.origin = ()
        self.targets = []

    def setup_problem(self, points=None, origin=None, max_points=None, dim=2, highs=(100, 100), lows=(0, 0)):
        """
        For setting up the traveling salesman problem. This can be executed in several ways.
        :param points: (list(tuple)) User supplied points, if this is left blank the method will
                       call self.__setup_random.
        :param origin: (tuple) User supplied origin, if this is left blank then self.origin will be points[0]
        :param max_points: (integer) For self.__setup_random. This corresponds to the number of randomly
                           generated points.
        :param dim: (integer) For self.__setup_random. This corresponds to the point dimension.
        :param highs: (list(integer)) For self.__setup_random. These are the max point value for each dimension.
        :param lows: (list(integer)) For self.__setup_random. These are the min point value for each dimension.
        :return: (void)
        """
        if points is None:
            self.__setup_random__(max_points,dim, highs, lows)
            return

        if origin is None:
            self.origin = points[0]
            self.targets = points[1:]
            return

        self.origin = origin
        self.targets = points

    def __setup_random__(self, max_points, dim=2, highs=(100,100), lows=(0,0)):
        """
        Method to create random TS ponints
        :param max_points: (integer) Number of points. One will be the origin.
        :param dim: (integer) This corresponds to the point dimension.
        :param highs: (list(integer)) These are the max point value for each dimension.
        :param lows: (list(integer)) These are the min point value for each dimension.
        :return:
        """
        self.targets = []
        for n in range(max_points - 1):
            point = []
            for i in range(dim):
                point.append(random.uniform(lows[i % len(lows)], highs[i % len(highs)]))
            self.targets.append(tuple(point))

        point = []
        for i in range(dim):
            point.append(random.uniform(lows[i % len(lows)], highs[i % len(highs)]))
        self.origin = tuple(point)

if __name__ == "__main__":
    pass
