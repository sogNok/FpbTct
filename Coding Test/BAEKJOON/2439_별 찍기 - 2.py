# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:12:58 2021

@author: 이충섭
"""

# 2439th, 별 찍기 - 2 | class 1

counting_star = int(input())

for i in range(1, counting_star+1):
    stars = ' ' * (counting_star - i) + '*' * i
    print(stars)