# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 17:43:43 2021

@author: 이충섭
"""

# 1259th, 팰린드롬수 | class 2

while True:
    num = input()
    if num == '0':
        break
    
    former = num[:len(num)//2]
    latter = num[-1:-1-len(num)//2:-1]
    
    print('yes' if former==latter else 'no')
