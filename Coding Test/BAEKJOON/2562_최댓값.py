# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:52:54 2021

@author: 이충섭
"""

# 2562th, 최댓값 | class 1

int_list = [int(input()) for _ in range(9)]

max_int = 0
idx_int = 0

for idx, num in enumerate(int_list):
    if num > max_int:
        max_int = num
        idx_int = idx

print(max_int)
print(idx_int + 1)


    