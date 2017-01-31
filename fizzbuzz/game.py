# -*- coding: utf-8 -*-

""" 
Use: python game.py
"""

from fizzbuzz import FizzBuzz

def game():
    for number in range(1, 101):
        print FizzBuzz().get(number)

if  __name__ == '__main__':
    game()