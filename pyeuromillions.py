#!/usr/bin/python
# -*- coding: utf-8 -*-
import itertools
import sys

usage = """
pyeuromillions n1,n2...,n5,n... s1,s2,...
    The first comma separated list is for numbers. Minimun 5
    The second comma separated list is for stars. Minimun 2
"""

class PyEuromillions:
    numbers = []
    stars = []
    
    def __init__(self, numbers, stars):
        self.numbers = numbers.split(',')
        self.stars = stars.split(',')
        if ((len(self.numbers) < 5) or (len(self.stars) < 2)):
            print usage
        
    def gen_valid_combinations(self):
        valid_number_combs = itertools.combinations(self.numbers, 5)
        valid_stars_combs = itertools.combinations(self.stars,2)
        valid_combs = itertools.product(valid_number_combs, valid_stars_combs)
        return valid_combs
        
if __name__ == '__main__':
    pyeuromillions = PyEuromillions(sys.argv[1], sys.argv[2])
    valid_combs = pyeuromillions.gen_valid_combinations()
    total = 0
    for i in valid_combs:
        print i
        total += 1
    print "Total number of combinations: %s" % total    