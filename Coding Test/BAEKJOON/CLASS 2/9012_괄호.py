# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 21:49:43 2021

@author: 이충섭
"""

# 9012th, 괄호 | class 2

import sys

T = int(sys.stdin.readline())

PS = [sys.stdin.readline() for _ in range(T)]

for ps in PS:
    count = 0
    
    for character in ps:
        if character == '(':
            count += 1
        elif character == ')':
            count -= 1
        else:
            pass
        
        if count < 0:
            print('NO')
            break
    else:
        if count == 0:
            print('YES')
        else:
            print('NO')

