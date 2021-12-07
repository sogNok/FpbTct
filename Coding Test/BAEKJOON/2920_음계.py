# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 19:30:14 2021

@author: 이충섭
"""

# 2920th, 음계 | class 1

scale = list(map(int, input().split()))
ascending = [x for x in range(1, 9)]
descending = [x for x in range(8, 0, -1)]

if scale == ascending:
    print('ascending')
elif scale == descending:
    print('descending')
else:
    print('mixed')