# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 23:50:39 2021

@author: 이충섭
"""

# 11720th, 숫자의 합 | class 1

N = int(input())
N_str = input()

sum_num = 0
for str_num in N_str:
    sum_num += int(str_num)
    
print(sum_num)