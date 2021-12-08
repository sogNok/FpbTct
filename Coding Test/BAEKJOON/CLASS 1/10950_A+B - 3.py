# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 23:07:06 2021

@author: 이충섭
"""

# 10950th, A+B - 3 | class 1

T = int(input())
test_case = [list(map(int, input().split())) for _ in range(T)]

for case in test_case:
    print(case[0] + case[1])