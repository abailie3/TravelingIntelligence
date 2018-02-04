"""
Copyright (c) 2018 Austin Bailie, All rights reserved.
"""
import inspect
import math
import types
from typing import Tuple, List, TypeVar, Dict
from abc import ABC

__VarCOMB__ = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]


class MachineInterface(object):
    """
    An interface allowing AI/ML algorithms to design and execute algorithms.
    """
    __tab__ = "    "  # Standard tab width for line indentation
    __base_imports__ = ["from typing import Tuple, List"]
    __method_start__ = "def solve(origin, targets) -> Tuple[float, List[tuple]]:\n" + __tab__ + \
                       "fout = -1.\n" + __tab__ + "lout = []\n"
    __return__ = __tab__ + "return fout, lout"

    __ASSIGNVARIABLE = 0

    def __init__(self):
        self.__method = self.__method_start__
        self.__addImports = []
        self.__lineDepth = 1
        self.__variables = [("origin",), ("targets", List), ("fout",), ("lout", List)]
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

    def __new_list__(self, name=None):
        return self.__new_var__(List, name)

    def __new_var__(self, var_type=None, name=None) -> str:
        """
        For creating and logging new variables.

        :param var_type: (Optional str) The name of the type of the variable.
        :param name: (Optional str) The name for the variable. If none a random name will be created.
        :return: (str) The name. Either the provided name or the randomly generated name.
        """
        if name is None:
            from time import time
            name = str(int(time()*1e7))
        self.__numVar += 1
        self.__variables.append((name, var_type))
        if var_type == List:
            return name + " = []"
        return name

    def __var_assign__(self, idx, value) -> str:
        # TODO: Add code for variable assignment
        pass

    @staticmethod
    def __math__(inputs: list) -> str:
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
        """
        Countst number of commas in the input string

        :param test_str: (str) String with commas to count
        :return: (int) Number of commas in test_str
        """
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
        # b = self.__math__([1, 3, 5, 2, 5, 3, 2, 15, 6,7, 5])
        return self.__compile__()(0, [])


class CodeElement(ABC):
    """
    Abstract class for the various code elements. (eg. ForLoop, Conditional, etc.)
    """
    __tab__ = "    "  # Standard tab width for line indentation

    def __init__(self):
        self.__car_vars__ = {}
        self.__car_var_reg__ = []
        self._int_vars_ = {}
        self._spacing_ = ""
        self._block_ = []
        self._prefix_ = ""

    @property
    def _carry_variables_(self) -> Dict:
        return self.__car_vars__

    @_carry_variables_.setter
    def _carry_variables_(self, var: Dict):
        self.__car_vars__ = var

    @property
    def _carry_register_(self) -> List[str]:
        return self.__car_var_reg__

    @_carry_register_.setter
    def _carry_register_(self, car_reg: List[str]):
        self.__car_var_reg__ = car_reg

    @property
    def internal_variables(self) -> Dict:
        return self._int_vars_

    @internal_variables.setter
    def internal_variables(self, var: Dict):
        self._int_vars_ = var

    @property
    def __spacing__(self) -> str:
        return self._spacing_

    @__spacing__.setter
    def __spacing__(self, space: str):
        self._spacing_ = space

    @property
    def __code_block__(self) -> List[str]:
        return self._block_

    @__code_block__.setter
    def __code_block__(self, new_block: List[str]):
        self._block_ = new_block

    @property
    def __prefix__(self):
        return self._prefix_

    @__prefix__.setter
    def __prefix__(self, new_prefix: str):
        self._prefix_ = new_prefix

    def _get_available_var_(self) -> str:
        for a in __VarCOMB__:
            for b in __VarCOMB__:
                for i in range(10):
                    if (a + b + str(i)) not in self._carry_variables_ and \
                                    (a + b + str(i)) not in self.internal_variables:
                        return a + b + str(i)
        return ""  # TODO: Make this throw an error instead

    def add_code(self, code_lines: List[str]) -> None:
        """
        Method for adding a block of code lines using a list of strings.

        :param code_lines: (List[str]) The block of code lines
        :return: (void)
        """
        self.__code_block__ += code_lines

    def add_code_block(self, code_block: 'CodeElement') -> None:
        """
        Method for adding a block of code lines using another code element.

        :param code_block: (CodeElement) The block of code lines
        :return: (void)
        """
        self.add_code(code_block.get_code())

    def get_code(self) -> List[str]:
        """
        To retrieve the code generated by the code element

        :return: (str) The un-indented line or block of code representing the code element.
        """
        if self.__prefix__ == "":
            out = []
        else:
            out = [self.__prefix__]

        if self.__spacing__ == "":
            return out + self.__code_block__

        for line in self.__code_block__:
            out.append(self.__spacing__ + line)
        return out


CE = TypeVar('CE', bound=CodeElement)


class GenericBlock(CodeElement):
    """
    This class is for creating a standard block of code.
    """
    def __init__(self):
        super().__init__()
        self.__prefix__ = ""
        self.__spacing__ = ""


class ForLoop(CodeElement):
    """
    This class is for creating a for loop.
    """
    def __init__(self):
        super().__init__()
        self.indexing = ""
        self.__prefix__ = "for "
        self.__spacing__ = self.__tab__

    def set_range_indexing(self, var_idx: int) -> None:
        """
        Sets the indexing method of the for loop to be based on a range of the indexing variables from 0 to some number,
        incremented by 1. It returns the following form:
            "for var0 in range(var1):"
                Where:
                    var0 - some un-used variable
                    var1 - if var_idx corresponds to a variable of type int, then var1 is this variable. Else if var_idx
                           corresponds to a list, then var1 is the length of said variable. Otherwise, this method fails

        :param var_idx: (int) The index in the carry variables of the variable to use in the "range()" interior
        :return: (void)
        """
        if len(self._carry_register_) < var_idx or len(self._carry_register_) == 0:
            return  # TODO: Throw an error
        if self._carry_variables_[self._carry_register_[var_idx]] not in [List, int, list]:
            return  # TODO: Throw an error

        # Done checking
        self.indexing = self._get_available_var_()
        self.__prefix__ += self.indexing + " in range("
        if self._carry_variables_[self._carry_register_[var_idx]] == int:
            self.__prefix__ += self._carry_register_[var_idx] + ")"
        else:
            self.__prefix__ += "len(" + self._carry_register_[var_idx] + "))"
        self.__prefix__ += ":"

    def set_member_indexing(self, var_idx: int) -> None:
        """
        Sets the indexing method of the for loop to be based on iterating through the members of some data structure.
        The data structure must be either a list, dict, or str.

        :param var_idx: (int) The index in the carry variables of the variable to iterate through
        :return: (void)
        """
        if len(self._carry_register_) < var_idx or len(self._carry_register_) == 0:
            return  # TODO: Throw an error
        if self._carry_variables_[self._carry_register_[var_idx]] not in [List, list, Dict, dict, str]:
            return  # TODO: Throw an error

        # Done checking
        self.indexing = self._get_available_var_()
        self.__prefix__ += self.indexing + " in " + self._carry_register_[var_idx]
        self.__prefix__ += ":"

if __name__ == "__main__":
    mi = MachineInterface()
