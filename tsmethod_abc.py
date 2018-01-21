from abc import ABC, abstractmethod
from tsproblem import TSProblem
from typing import Tuple, List

class TSMethod(ABC):
    @abstractmethod
    def solve(self, problem: TSProblem) -> Tuple[float, List[tuple]]:
        pass


if __name__ == "__main__":
    pass
