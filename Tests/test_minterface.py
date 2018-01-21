import unittest
from MachineLibrary import minterface

class MachineLibraryTestCase(unittest.TestCase):

    def test_execute(self):
        mi = minterface.MachineInterface()
        b, l = mi.test_machine_interface()
        self.assertEqual(b, -1)
        self.assertEqual(l, [])

def suite():
    loader = unittest.TestLoader()
    return loader.loadTestsFromTestCase(MachineLibraryTestCase)

if __name__ == "__main__":
    unittest.main()