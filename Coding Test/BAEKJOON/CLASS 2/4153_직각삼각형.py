# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 10:15:54 2021

@author: 이충섭
"""

# 4153th, 직각삼각형 | class 2

while True:
    sides = sorted(map(int, input().split()))
    
    if sides == [0, 0, 0]:
        break
    
    pow_sides = [x**2 for x in sides]
    
    if pow_sides[0] + pow_sides[1] == pow_sides[2]:
        print('right')
    else:
        print('wrong')

