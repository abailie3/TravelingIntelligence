"""
Copyright 2018, Austin Bailie, All rights reserved.
"""
from abc import ABC, abstractmethod
from typing import Tuple, List

from tsproblem import TSProblem


class TSMethod(ABC):
    @abstractmethod
    def solve(self, problem: TSProblem) -> Tuple[float, List[tuple]]:
        pass


if __name__ == "__main__":
    pass
