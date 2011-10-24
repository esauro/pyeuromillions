#!/usr/bin/python
# -*- coding: utf-8 -*-
import itertools

class PyEuromillions:
    
    def __init__(self, numbers, stars):
        self.numbers = numbers.split(',')
        self.stars = stars.split(',')
        self.filters = []
        if ((len(self.numbers) < 5) or (len(self.stars) < 2)):
            print usage
        
    def gen_valid_combinations(self):
        valid_number_combs = itertools.combinations(self.numbers, 5)
        valid_stars_combs = itertools.combinations(self.stars,2)
        valid_combs = itertools.product(valid_number_combs, valid_stars_combs)
        for filter in self.filters:
            f = filter['function']
            args = filter['args']
            kwargs = filter['kwargs']
            valid_combs = [x for x in valid_combs if f(x, *args, **kwargs)]
        return valid_combs
    
    def register(self, function, *args, **kwargs):
        """This function will register a filter to be run when filtering combinations"""
        self.filters.append({'function': function,
                            'args': args,
                            'kwargs': kwargs})
