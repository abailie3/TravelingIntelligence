"""
Copyright 2018, Austin Bailie, All rights reserved.
"""
import queue
import time
from typing import Tuple, List

from distance import DistanceMeasure
from tsmethod_abc import TSMethod, TSProblem


class BruteForce(TSMethod):
    """
    The BruteForce method tries all possible paths in the Traveling Salesman Problem and returns the shortest.
    Note: This method, while guaranteed to find the shortest path, is extremely slow (O(n!)). I would suggest
          limiting the number of points in the problem.
    """
    def __init__(self, dm: DistanceMeasure):
        """
        :param dm: (DistanceMeasure) the distance measure used to find the distance between two points.
        """
        self.distanceMeasure = dm
        self.lastRunTime = 0

    def solve(self, problem: TSProblem) -> Tuple[float, List]:
        """
        The solve method required for TSMethod instances. Algorithm documentation in class doc.
        Algorithm additionally will log the runtime and save it in self.lastRunTime.
        :param problem: (TSProblem) the traveling salesman problem.
        :return: (Tuple[float, List]) the shortest path found by the algorithm, where the first member is the
                                      length of the path, and the second member is the sequence visited (as a
                                      list of the points in order of visit).
        """
        start = time.process_time()  # for logging the algorithm run time.

        origin = problem.origin
        targets = problem.targets

        """
        While this method could theoretically be implemented using recursion, given the complexity of the algorithm
        this is impractical. As such, a priority queue is used to take an iterative approach.
        """
        p_queue = queue.PriorityQueue()

        # Add origin and all targets to queue as starting point.
        p_queue.put((origin, targets, [origin], 0))

        # Initialize minimum.
        min_len = float("inf")
        min_path = []

        # While combinations are left to try
        while not p_queue.empty():
            # Get Tuple(point, remaining targets, path to point, current path length)
            p_entry = p_queue.get()
            o1 = p_entry[0]  # point
            targets = p_entry[1]  # remaining targets
            path = p_entry[2]  # path to point
            path_len = p_entry[3]  # current path length

            if len(targets) == 0:  # if no remaining targets
                # find length from terminus to origin and add to path length
                path_len += self.distanceMeasure.distance(o1, origin)
                # if path is the shortest thus far, save path.
                if path_len < min_len:
                    min_len = path_len
                    min_path = path
            else:
                # Cue up all combinations of remaining targets, calculating the distance to the respective target
                for i in range(len(targets)):
                    p_queue.put((targets[i], BruteForce.get_rest(targets, i), path + [targets[i]],
                                 path_len + self.distanceMeasure.distance(o1, targets[i])))

        self.lastRunTime = time.process_time() - start  # Calculate run time.
        return min_len, min_path

    @staticmethod
    def get_rest(array, index):
        a = array.copy()
        a.remove(a[index])
        return a
