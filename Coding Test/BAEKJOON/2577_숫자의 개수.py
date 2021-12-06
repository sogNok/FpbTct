# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:58:46 2021

@author: 이충섭
"""

# 2577th, 숫자의 개수 | class 1

single_digit = [0 for _ in range(10)]

A = int(input())
B = int(input())
C = int(input())

multipli_num = A * B * C
multipli_str = str(multipli_num)

for str_num in multipli_str:
    for digit in range(10):
        if str_num == str(digit):
            single_digit[digit] += 1

for digit in single_digit:
    print(digit)