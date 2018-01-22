"""
Copyright 2018, Austin Bailie, All rights reserved.
"""
from abc import ABC, abstractmethod
from typing import Tuple, List

from travelingintelligence.tsproblem import TSProblem


class TSMethod(ABC):
    """
    An abstract class for the method of solving a traveling salesman problem.
    """
    @abstractmethod
    def solve(self, problem: TSProblem) -> Tuple[float, List[tuple]]:
        pass


if __name__ == "__main__":
    pass
