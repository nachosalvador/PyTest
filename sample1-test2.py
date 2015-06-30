# -*- coding: utf-8 -*-

import unittest
from math import factorial
 
class TestUM(unittest.TestCase):
 
    def test_factorial(self):
        self.assertEqual( factorial(3), 6)