from typing import Tuple, List
import inspect
import types
import math


class MachineInterface(object):
    """
    An interface allowing AI/ML algorithms to design and execute algorithms.
    """
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
        """
        Compiles the dynamically created code, returning the function.
        :return: (FunctionType) a compiled function from the dynamically created code.
        """
        code = {}
        exec(compile(self.__build_method__(), '<string>', 'exec'), code)
        return code["solve"]

    def __build_method__(self) -> str:
        """
        This constructs the method's code to be compiled/inspected.
        :return: (str) A string of the method's code.
        """
        out = ""
        for imp in self.__base_imports__:
            out += imp + "\n"
        return out + self.__method + "\n" + self.__return__

    def __new_var__(self, name=None) -> str:
        """
        For creating and logging new variables.
        :param name: (Optional str) The name for the variable. If none a random name will be created.
        :return: (str) The name. Either the provided name or the randomly generated name.
        """
        if name is None:
            from time import time
            name = str(int(time()*1e7))
        self.__numVar += 1
        self.__variables.append(name)
        return name

    def __var_assign__(self, idx, value) -> str:
        # TODO: Add code for variable assignment
        pass

    def __math__(self, inputs: list) -> str:
        """
        This method chooses a function from the math package and creates a line of code representing its usage.
        :param inputs: (list) A list of inputs to configure the method call.
                                    inputs[0] - the index of the math function to call, if non-int then the
                                                value is truncated to an integer.
                                    inputs[1:] - the remaining indexes act as the inputs to the functions.
                                                 if the type of the index is Tuple(int) then this indicates
                                                 that a variable in the self.__variables list (at index of the
                                                 int % len(self.variables)) shall be used. Otherwise, the
                                                 value of the index shall be a static input to the function.
        :return: (str) An un-indented string of the method call.
        """
        # TODO: Find new way of indicating that a variable should be used instead of a static value.

        out = ""
        if len(inputs) < 2:
            return None  # TODO: create error and throw that instead
        fname, func = inspect.getmembers(math, inspect.isbuiltin)[inputs[0]]
        out += fname + "("
        nvars = MachineInterface.__math_doc_nvars__(func.__doc__)
        if nvars == 1:
            out += str(inputs[1]) + ","
        else:
            for i in range(1, nvars):
                print(i)
                out += str(inputs[i % len(inputs)]) + ","

        return out[:-1] + ")"
        # b = func.__doc__
        # print(dir(func))
        # print(b)
        # print(dir(b))
        # print(inspect.signature(b)

    @staticmethod
    def __math_doc_nvars__(doc: str) -> int:
        """
        This finds the number of parameters of a function from the math library by parsing the function's
        doc parameter. NOTE: This is not a great way of finding the number of parameters, but I can't find
        a better way.
        :param doc: (str) the doc string for the function.
        :return: (int) number of variables for the function.
        """
        # TODO: Find a better way.
        # TODO: Potentially log the functions away in dictionary {func_name:n_vars} for faster recall
        start = doc.find("(")+1
        end = doc.find(")")
        if end < start:
            return 0
        sub_string = doc[start:end]
        commas = MachineInterface.__count_commas__(sub_string)
        if commas == 0:
            if len(sub_string) > 0:
                return 1
            else:
                return 0
        else:
            return commas + 1


    @staticmethod
    def __count_commas__(test_str: str) -> int:
        i = test_str.find(",")
        if i == -1:
            return 0
        return 1 + MachineInterface.__count_commas__(test_str[i+1:])


    @staticmethod
    def __safe_idx__(arr_name: str, idx) -> str:
        """
        This method creates a line of code that safe indexes an array. Safe indexing here means indexing such that
        there is no possibility of indexing out of bounds (assuming the array is not of length 0).
        :param arr_name: (str) Name of the variable representing the array.
        :param idx: (int -or- float) Index of the array to grab. If float is provided it will be truncated to int.
        :return: (str) An un-indented string of the line of code.
        """
        return arr_name + "[" + str(idx) + " % len(" + arr_name + ")]"

    def test_machine_interface(self) -> Tuple[float, List]:
        """
        Just a test module for the class.
        :return:
        """
        b = self.__math__([1, 3, 5, 2, 5, 3, 2, 15, 6,7, 5])
        return self.__compile__()(0, [])