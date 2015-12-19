""" 
----------------------- GAME RULES ----------------------------
1. A number is fizz if it is divisible by 3.
2. A number is buzz if it is divisible by 5.
3. A number is fizzbuzz if it is divisible by 3 and 5.

Use: py.test -s test_fizzbuzz.py
"""

from fizzbuzz import FizzBuzz

class TestFizzBuzz:

    def setup(self):
        self.fizzbuzz = FizzBuzz()
 
    def test_number_three_is_fizz(self):
        assert self.fizzbuzz.get(1) != 'fizz', "Number 1 is 1"
        assert self.fizzbuzz.get(3) == 'fizz', "Number 3 is fizz"
        assert self.fizzbuzz.get(33) == 'fizz', "Number 33 is fizz"

    def test_number_five_is_buzz(self):
        assert self.fizzbuzz.get(5) == 'buzz', "Number 5 is buzz"
        assert self.fizzbuzz.get(20) == 'buzz', "Number 20 is buzz"

    def test_number_three_and_five_is_fizzbuzz(self):
        assert self.fizzbuzz.get(15) == 'fizzbuzz', "Number 15 is fizzbuzz"
        assert self.fizzbuzz.get(30) == 'fizzbuzz', "Number 30 is fizzbuzz"