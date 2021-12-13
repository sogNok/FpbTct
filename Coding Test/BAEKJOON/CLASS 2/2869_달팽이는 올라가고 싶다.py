# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 18:29:26 2021

@author: 이충섭
"""

# 2869th, 달팽이는 올라가고 싶다 | class 2

A, B, V = map(int, input().split())

quat, remain = divmod(V-B, A-B)

if remain == 0:
    print(quat)
else:
    print(quat + 1)