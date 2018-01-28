"""
Copyright (c) 2018 Austin Bailie, All rights reserved.
"""
import unittest

from travelingintelligence.machinelibrary import minterface


class MachineInterfaceTestCase(unittest.TestCase):

    def test_execute(self):
        mi = minterface.MachineInterface()
        b, l = mi.test_machine_interface()
        self.assertEqual(b, -1)
        self.assertEqual(l, [])

    def test_math_(self):
        # Test for too few inputs
        mi = minterface.MachineInterface()
        self.assertIsNone(mi.__math__([1]))

        # Test for normal inputs
        inputs = [13, 4, 4, 321, 6]
        b = mi.__math__(inputs)
        self.assertLess(b.find("("), b.find(")"))

        # Now find a function with more than one input and ensure that works.
        for i in range(100):
            inputs = [i, 4, 4, 321, 6]
            b = mi.__math__(inputs)
            if mi.__math_doc_nvars__(b) > 1:
                self.assertLess(b.find("("), b.find(")"))
                break
            # Want to show an error if it doesn't find a object with more than one input.
            self.assertNotEqual(i, 99)

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

    def test_safe_idx(self):
        arr_name = "myArray"
        idx = 3
        string = "myArray[3 % len(myArray)]"
        mi = minterface.MachineInterface()
        out = mi.__safe_idx__(arr_name, idx)
        self.assertEqual(string, out)


class ForLoopTestCase(unittest.TestCase):
    def test_class_vars(self):
        fl = minterface.ForLoop()
        self.assertEqual({}, fl.carry_variables)
        self.assertEqual({}, fl.internal_variables)
        carry = {'test': 'test'}
        internal = {'int': 'int'}
        fl.carry_variables = carry
        fl.internal_variables = internal
        self.assertEqual(carry, fl.carry_variables)
        self.assertEqual(internal, fl.internal_variables)

    def test_get_code(self):
        fl = minterface.ForLoop()
        self.assertEqual(0, 0)


"""
The below lines of code should be included in all sub-test modules.
"""


def suite():
    """
    This method must be included at the end of all sub-test modules. To use in other modules, copy this entire
    method to the new module and add the correct test classes to the "tests" list.
    :return: (unittest.TestSuite) Test suite for this sub-test
    """
    tests = [MachineInterfaceTestCase, ForLoopTestCase]  # Add test classes here
    loader = unittest.TestLoader()
    full_suite = []
    for test in tests:
        test_suite = loader.loadTestsFromTestCase(test)
        full_suite.append(test_suite)
    return unittest.TestSuite(full_suite)

if __name__ == "__main__":
    unittest.main()