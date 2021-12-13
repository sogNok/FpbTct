# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 17:03:33 2021

@author: 이충섭
"""

# 2798th, 블랙잭 | class 2

import sys

N, M = map(int, input().split())
cards = sorted(map(int, input().split()))

max_m = 0
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_cards = cards[i] + cards[j] + cards[k]
            
            if sum_cards > M:
                break
            elif sum_cards == M:
                print(M)
                sys.exit(0)
            max_m = max(max_m, sum_cards)
            
print(max_m)
            
            