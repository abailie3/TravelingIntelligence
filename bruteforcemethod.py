from tsmethod_abc import TSMethod, TSProblem
from distance import DistanceMeasure
import queue
import time

class BruteForce(TSMethod):
    def __init__(self, dm: DistanceMeasure):
        self.distanceMeasure = dm
        self.lastRunTime = 0

    def solve(self, problem: TSProblem):
        start = time.process_time()
        origin = problem.origin
        targets = problem.targets
        p_queue = queue.PriorityQueue()

        # (start point, remaining targets, [sequence], length)
        p_queue.put((origin, targets, [origin], 0))

        min_len = float("inf")
        min_seq = []
        while not p_queue.empty():
            p_entry = p_queue.get()
            o1 = p_entry[0]
            targets = p_entry[1]
            seq = p_entry[2]
            seq_len = p_entry[3]

            if len(targets) == 0:
                seq_len += self.distanceMeasure.distance(o1, origin)
                if seq_len < min_len:
                    min_len = seq_len
                    min_seq = seq
            else:
                for i in range(len(targets)):
                    p_queue.put((targets[i], BruteForce.get_rest(targets, i), seq + [targets[i]],
                                 seq_len + self.distanceMeasure.distance(o1, targets[i])))
        self.lastRunTime = time.process_time() - start
        return min_len, min_seq

    @staticmethod
    def get_rest(array, index):
        a = array.copy()
        a.remove(a[index])
        return a
