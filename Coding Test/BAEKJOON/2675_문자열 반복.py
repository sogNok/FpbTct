# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 14:43:16 2021

@author: 이충섭
"""

# 2675th, 문자열 반복 | class 1

TEST_NUM = int(input())

P_list = ['' for _ in range(TEST_NUM)]

for idx in range(TEST_NUM):
    R, S = input().split()
    P = ''
    for s in S:
        P += s * int(R)
    
    P_list[idx] = P

for P in P_list:
    print(P)