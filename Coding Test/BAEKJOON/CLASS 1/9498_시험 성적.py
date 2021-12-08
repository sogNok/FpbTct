# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 21:36:32 2021

@author: 이충섭
"""

# 9498th, 시험 성적 | class 1

score = int(input())

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')