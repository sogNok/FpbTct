# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 21:29:06 2021

@author: 이충섭
"""

# 8958th, OX퀴즈 | class 1

num_test_case = int(input())

test_case = [input() for _ in range(num_test_case)]

for idx in range(num_test_case):
    score = 0
    sequence = 0
    
    for OX in test_case[idx]:
        if OX == 'O':
            sequence += 1
        else:
            sequence = 0
        score += sequence
    
    print(score)