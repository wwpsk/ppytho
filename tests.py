import unittest
from lessons6 import *

class My_test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(2, 2), 4)

    def test_kwargs(self):
        self.assertEqual(adder(a=10, b=11), 21)

    def test_mixed(self):
        self.assertEqual(adder(1, a=2), 3)

    def test_diff(self):
        x = 10
        y = 0
        self.assertEqual(adder(0. -5, y, a=x), 5)

    def test_wrong_datatype(self):
        self.assertEqual(adder("5", "abc", 10), 15)

if __name__ =="__name__":
    unittest.main()