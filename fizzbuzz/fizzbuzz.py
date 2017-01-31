# -*- coding: utf-8 -*-

class FizzBuzz:
    """ 
    The FizzBuzz Game Class.
    """

    FIZZ = 'fizz'
    BUZZ = 'buzz'

    FIZZ_MULTIPLE = 3
    BUZZ_MULTIPLE = 5

    def get(self, number):
        """ 
        Gets the number.
        """
        return self._calculate_output(number)

    def _calculate_output(self, number):
        """ 
        Calculates the number output.
        """
        output = number
        
        if self._is_fizz(number):
            output = self.FIZZ
        
        if self._is_buzz(number):
            if isinstance(output, str):
                output += self.BUZZ
            else:
                output = self.BUZZ

        return output

    def _is_fizz(self, number):
        """ 
        Returns True if it is divisible by 3.
        """
        return number % self.FIZZ_MULTIPLE == 0

    def _is_buzz(self, number):
        """ 
        Returns True if it is divisible by 5.
        """
        return number % self.BUZZ_MULTIPLE == 0