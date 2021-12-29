# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 10:08:40 2021

@author: 이충섭
"""

# 1654th, 랜선 자르기 | class 2

import sys
K, N = map(int, sys.stdin.readline().split())

Lan_cables = [int(sys.stdin.readline()) for _ in range(K)]

s_length = sum(Lan_cables) // N
length = s_length
gap = s_length // 2

while gap:
    count = 0
    for cable in Lan_cables:
        count += cable // length
    
    if count > N:
        length -= gap
    elif count < N:
        length += gap
    else:
        break
    
    gap //= 2

for leng in range(length, s_length+1):
    count = 0
    for cable in Lan_cables:
        count += cable // leng
    if count < N:
        print(leng-1)
else:
    print(s_length)

