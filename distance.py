from abc import ABC, abstractmethod

class DistanceMeasure(ABC):

    @staticmethod
    @abstractmethod
    def distance(point1, point2) -> float:
        pass

class Euclidean(DistanceMeasure):
    @staticmethod
    def distance(point1, point2):
        out = 0
        for i in range(len(point1)):
            out += (point1[i] - point2[i])**2
        return out ** 0.5
