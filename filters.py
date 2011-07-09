#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This module will hold filters"""

def even_numbers(comb, min = 0, max = 5):
    even = 0
    for i in comb[0]:
        if (int(i) % 2) == 0:
            even +=1
    return ((even >= min) and (even <= max))