# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 15:28:01 2021

@author: 이충섭
"""

# Chapter 09 organization

def range_of(*v):
    """ Returns the difference between maximum and minimum """
    return abs(max(v) - min(v))

print(f'range_of(1, 5)              = {range_of(1, 5)}')
print(f'range_of(1, -3, 2, 5, 4)    = {range_of(1, -3, 2, 5, 4)}')