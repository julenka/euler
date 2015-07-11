#!/usr/bin/env python
# coding=utf-8
""" Roman Numerals

For a number written in Roman numerals to be considered valid there are basic rules which must be followed.
Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
"""
__author__ = 'julenka'
from utils import euler_roman

def solve():
    characters_saved = 0
    with open("089.txt") as input:
        for line in input:
            line = line.strip()
            value = euler_roman.from_roman(line)
            shortest = euler_roman.to_roman(value)
            characters_saved += len(line) - len(shortest)
    return characters_saved

if __name__ == '__main__':
    answer = solve()
    print answer
