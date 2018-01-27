"""
Copyright (c) 2018 Austin Bailie, All rights reserved.
"""
from abc import ABC, abstractmethod
from typing import Type, TypeVar

class DistanceMeasure(ABC):
    """
    Abstract class for various ways of accounting for distance.
    """
    @staticmethod
    @abstractmethod
    def distance(point1, point2) -> float:
        """
        :param point1: (tuple) Point 1 of dimension len(point1)
        :param point2: (tuple) Point 2 of dimension len(point2)
        :return: (float) distance between points.
        """
        pass

DM = TypeVar('DM', bound=DistanceMeasure)

class Euclidean(Type[DM]):
    """
    Classic Euclidean distance measure.
        Ex: For points p1 = (x1, y1) and p2 = (x2, y2).
            Distance = sqrt((x1 - x2)^2 + (y1 - y2)^2)
    """
    @staticmethod
    def distance(point1, point2) -> float:
        """
        :param point1: (tuple) Point 1 of dimension len(point1)
        :param point2: (tuple) Point 2 of dimension len(point2)
        :return: (float) distance between points.
        """
        out = 0
        for i in range(len(point1)):
            out += (point1[i] - point2[i])**2
        return out ** 0.5


class TaxiCab(Type[DM]):
    """
    Classic Taxicab distance measure.
        Ex: For points p1 = (x1, y1) and p2 = (x2, y2).
            Distance = abs(x1 - x2) + abs(y1 - y2)
    """
    @staticmethod
    def distance(point1, point2) -> float:
        """
        :param point1: (tuple) Point 1 of dimension len(point1)
        :param point2: (tuple) Point 2 of dimension len(point2)
        :return: (float) distance between points.
        """
        out = 0
        for i in range(len(point1)):
            out += abs(point1[i] - point2[i])
        return out


