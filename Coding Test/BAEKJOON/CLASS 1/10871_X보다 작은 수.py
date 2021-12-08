# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 23:01:52 2021

@author: 이충섭
"""

# 10871st, X보다 작은 수 | class 1

N, X = map(int, input().split())
int_list = list(map(int, input().split()))

for num in int_list:
    if num < X:
        print(num, end=' ')