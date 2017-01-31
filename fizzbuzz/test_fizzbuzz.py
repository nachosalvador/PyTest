# -*- coding: utf-8 -*-

""" 
----------------------- GAME RULES ----------------------------
1. A number is fizz if it is divisible by three.
2. A number is buzz if it is divisible by five.
3. A number is fizzbuzz if it is divisible by three and five.

Use: python test_fizzbuzz.py
"""

import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.fizzbuzz = FizzBuzz()
 
    def test_no_fizzbuzz_numbers(self):
        no_fizzbuzz_numbers = [1, 19, 32]

        for number in no_fizzbuzz_numbers:
            self.assertEquals(
                self.fizzbuzz.get(number),
                number,
                'Number ' + str(number) + ' is ' + str(number)
                )

    def test_number_divisible_by_three_is_fizz(self):
        fizz_numbers = [3, 9, 33]

        for number in fizz_numbers:
            self.assertEquals(
                self.fizzbuzz.get(number),
                'fizz',
                'Number ' + str(number) + ' is "fizz"'
                )

    def test_number_divisible_by_five_is_buzz(self):
        buzz_numbers = [5, 10, 25]

        for number in buzz_numbers:
            self.assertEquals(
                self.fizzbuzz.get(number),
                'buzz',
                'Number ' + str(number) + ' is "buzz"'
                )

    def test_number_divisble_by_three_and_five_is_fizzbuzz(self):
        fizzbuzz_numbers = [15, 30, 45]

        for number in fizzbuzz_numbers:
            self.assertEquals(
                self.fizzbuzz.get(number),
                'fizzbuzz',
                'Number ' + str(number) + ' is "fizzbuzz"'
                )

if __name__ == '__main__':
    unittest.main()