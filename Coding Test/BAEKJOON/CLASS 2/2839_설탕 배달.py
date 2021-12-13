# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 18:12:05 2021

@author: 이충섭
"""

# 2839th, 설탕 배달 | class 2

BIG_ONE = 5
SML_ONE = 3

N = int(input())
quat, remain = divmod(N, BIG_ONE) 

for x in range(quat+1):
    y, y_remain = divmod((remain + x*BIG_ONE), SML_ONE)
    if y_remain == 0:
         print(quat - x + y)
         break
else:
    print(-1)
         