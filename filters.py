#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This module will hold filters"""
default_tens = ((0,5),
                (0,5),
                (0,5),
                (0,5),
                (0,5),
                )

def even_numbers(comb, min = 0, max = 5):
    even = 0
    for i in comb[0]:
        if (int(i) % 2) == 0:
            even +=1
    return ((even >= min) and (even <= max))

def odd_numbers(comb, min = 0, max = 5):
    odd = 0
    for i in comb[0]:
        if (int(i) % 2) != 0:
            odd += 1
    return ((odd >= min) and (odd <= max))

def even_stars(comb, min = 0, max = 2):
    even = 0
    for i in comb[1]:
        if (int(i) % 2) == 0:
            even +=1
    return ((even >= min) and (even <= max))

def odd_stars(comb, min = 0, max = 2):
    odd = 0
    for i in comb[1]:
        if (int(i) % 2) != 0:
            odd += 1
    return ((odd >= min) and (odd <= max))

def high_numbers(comb, min = 0, max = 5):
    """ A number is high if >= 25"""
    high = 0
    for i in comb[0]:
        if int(i) >= 25:
            high += 1
    return ((high >= min) and (high <= max))

def low_numbers(comb, min = 0, max = 5):
    """ A number is low if <= 25"""
    low = 0
    for i in comb[0]:
        if int(i) >= 25:
            low += 1
    return ((low >= min) and (low <= max))

def high_stars(comb, min = 0, max = 2):
    """ A number is high if >= 5"""
    high = 0
    for i in comb[1]:
        if int(i) >= 5:
            high += 1
    return ((high >= min) and (high <= max))

def low_stars(comb, min = 0, max = 2):
    """ A number is low if <= 5"""
    low = 0
    for i in comb[1]:
        if int(i) >= 5:
            low += 1
    return ((low >= min) and (low <= max))

def tens(comb, figures = default_tens):
    """This is for filtering the limits in each tens"""
    tens_count = [0, 0, 0, 0, 0]
    for i in comb[0]:
        tens_count[int(i) / 10] += 1
    for i in range(0,5):
        if ((tens_count[i] < figures[i][0]) or (tens_count[i] > figures[i][1])):
            return False 
    return True