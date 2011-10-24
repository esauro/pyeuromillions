#!/usr/bin/python
# -*- coding: utf-8 -*-
import itertools
import sys
from filters import *
from generation import *
usage = """
pyeuromillions n1,n2...,n5,n... s1,s2,...
    The first comma separated list is for numbers. Minimun 5
    The second comma separated list is for stars. Minimun 2
"""
        
if __name__ == '__main__':
    pyeuromillions = PyEuromillions(sys.argv[1], sys.argv[2])
    pyeuromillions.register(even_numbers, min = 2, max = 4)
    pyeuromillions.register(odd_stars, min = 2, max = 2)
    pyeuromillions.register(high_numbers, min = 3, max = 4)
    valid_combs = pyeuromillions.gen_valid_combinations()
    total = 0
    for i in valid_combs:
        #print i
        total += 1
    print "Total number of combinations: %s" % total    
