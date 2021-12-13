# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 15:58:46 2021

@author: 이충섭
"""

# 2775th, 부녀회장이 될테야 | class 2

T = int(input())
Test_case = [[int(input()), int(input())] for _ in range(T)]

for k, n in Test_case:
    residents = [x for x in range(1, n+1)]
    
    for _ in range(k):
        for i in range(1, n):
            residents[i] = residents[i] + residents[i-1]
            
    print(residents[-1])
