# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 19:19:22 2021

@author: 이충섭
"""

# 2908th, 상수 | class 1

first_Num, second_Num = input().split()

first_Num = int(first_Num[::-1])
second_Num = int(second_Num[::-1])

print(first_Num if first_Num > second_Num else second_Num)
