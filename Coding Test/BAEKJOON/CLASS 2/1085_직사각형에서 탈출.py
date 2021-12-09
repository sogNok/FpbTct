# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 10:07:21 2021

@author: 이충섭
"""

# 1085th, 직사각형에서 탈출 | class 2

x, y, w, h = map(int, input().split())

min_num = min(x, w-x, y, h-y)

print(min_num)
