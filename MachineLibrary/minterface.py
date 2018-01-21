import types
from distance import DistanceMeasure
from typing import Tuple, List
import math
import inspect



class MachineInterface(object):
    __tab__ = "    "
    __base_imports__ = ["from typing import Tuple, List"]
    __method_start__ = "def solve(origin, start) -> Tuple[float, List[tuple]]:\n" + __tab__ + \
                      "fout = -1.\n" + __tab__ + "lout = []\n"
    __return__ = __tab__ + "return fout, lout"

    __ASSIGNVARIABLE = 0

    def __init__(self):
        self.__method = self.__method_start__
        self.__addImports = []
        self.__lineDepth = 1
        self.__variables = ["origin", "start", "lout", "fout"]
        self.__numVar = len(self.__variables)

    def __compile__(self) -> types.FunctionType:
        code = {}
        exec(compile(self.__build_method__(), '<string>', 'exec'), code)
        return code["solve"]

    def __build_method__(self):
        out = ""
        for imp in self.__base_imports__:
            out += imp + "\n"
        return out + self.__method + "\n" + self.__return__

    def __new_var__(self, name=None, value=None):
        if name is None:
            from time import time
            name = str(int(time()*1e7))
        self.__numVar += 1
        self.__variables.append(name)

    def __math__(self, inputs: list):
        x = len(inputs)
        if x < 2:
            return None  # TODO: create error class and throw that instead
        fname, func = inspect.getmembers(math, inspect.isbuiltin)[inputs[0]]
        n_args = len(getattr(func, fname))
        print(getattr(func, fname))


    @staticmethod
    def __safe_idx__(arr_name: str, idx):
        return arr_name + "[" + str(idx) + " % len(" + arr_name + ")]"

    def test_machine_interface(self) -> Tuple[float, List]:
        b = self.__math__([1, 3, 5, 2, 5, 3, 2,15, 6,7, 5])
        return self.__compile__()(0, [])