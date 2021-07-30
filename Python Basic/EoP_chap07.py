# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 17:12:56 2021

@author: 이충섭
"""

# Chapter 07 organization

import random

MAX = 10
print(f'Generates a random number between 0~{MAX}')
number = int(input('Number of random numbers: '))

# Generate a list with elements with number and all elements is None
v = [None] * number

# Put 0~MAX random numbers into all elements
for i in range(number):
    v[i] = random.randint(0, MAX)

# Output to List
print(v)

# Output vertical bar graph to '*'
for i in range(MAX, 0 , -1):
    for j in range(0, number):
        if v[j] >= i: print('*', end='')
        else: print(' ', end='')
    print()
    
    
print('-' * number)
for i in range(number):
    print(i % 10, end='')