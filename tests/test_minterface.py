"""
Copyright 2018, Austin Bailie, All rights reserved.
"""
import unittest

from travelingintelligence.machinelibrary import minterface


class MachineLibraryTestCase(unittest.TestCase):

    def test_execute(self):
        mi = minterface.MachineInterface()
        b, l = mi.test_machine_interface()
        self.assertEqual(b, -1)
        self.assertEqual(l, [])

    def test_math_(self):
        inputs = [13, 4, 4, 321, 6]
        mi = minterface.MachineInterface()
        b = mi.__math__(inputs)
        self.assertLess(b.find("("), b.find(")"))

    def test_math_doc_nvars(self):
        string = "acos(x) \n blah blah this thing acos(xalskd,asd,fas,g,)"
        string2 = "max(x, 3) \n blah blah this thing max(xalskd,asd,fas,g,)"
        string3 = "void_rage() \n blah blah this thing void_rage(xalskd,asd,fas,g,)"
        mi = minterface.MachineInterface()
        self.assertEqual(1, mi.__math_doc_nvars__(string))
        self.assertEqual(2, mi.__math_doc_nvars__(string2))
        self.assertEqual(0, mi.__math_doc_nvars__(string3))

    def test_count_commas(self):
        string = "a, b, c, dasdf223992!@@#!@, 3,"
        string2 = "x"
        mi = minterface.MachineInterface()
        self.assertEqual(5, mi.__count_commas__(string))
        self.assertEqual(0, mi.__count_commas__(string2))

"""
The below lines of code should be included in all sub-test modules.
"""


def suite():
    """
    This method must be included at the end of all sub-test modules. To use in other modules, copy this entire
    method to the new module and change the class within the loader.loadTestsFromTestCase(<change>) as appropriate.
    :return: (unittest.TestSuite) Test suite for this sub-test
    """
    loader = unittest.TestLoader()
    return loader.loadTestsFromTestCase(MachineLibraryTestCase)

if __name__ == "__main__":
    unittest.main()