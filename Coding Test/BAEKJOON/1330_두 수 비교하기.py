# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 12:25:44 2021

@author: 이충섭
"""

# 1330th, 두 수 비교하기 | class 1

a, b = input().split()
a, b = int(a), int(b)

print('>' if a > b else '<' if a < b else '==')