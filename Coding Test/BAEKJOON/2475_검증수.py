# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:21:40 2021

@author: 이충섭
"""

# 2475th, 검증수 | class 1

unique_num = input().split()
unique_num = map(int, unique_num)

pow_num = map(lambda x: x**2 , unique_num) 

pow_sum = sum(pow_num)

verification_num = pow_sum % 10

print(verification_num)