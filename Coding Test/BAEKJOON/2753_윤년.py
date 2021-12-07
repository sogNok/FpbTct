# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 19:03:23 2021

@author: 이충섭
"""

# 2753th, 윤년 | class 1

year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)

        