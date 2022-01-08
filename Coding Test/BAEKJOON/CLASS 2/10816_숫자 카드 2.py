# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 14:15:25 2021

@author: 이충섭
"""

# 10816th, 숫자 카드 2 | class 2

import sys
from bisect import bisect_left, bisect_right

M = int(sys.stdin.readline())

placed_cards = sorted(map(int, sys.stdin.readline().split()))

N = int(sys.stdin.readline())

drawn_cards = list(map(int, sys.stdin.readline().split()))

for dc in drawn_cards:
    pc_left = bisect_left(placed_cards, dc)
    pc_right = bisect_right(placed_cards, dc)
    print(pc_right - pc_left, end=' ')
    
#%%
# 참조 답
# counter 이용

from collections import Counter
N = int(input())
N_list = input().split()
M = int(input())
M_list = input().split()

C = Counter(N_list)
print(' '.join(f'{C[m]}' if m in C else '0' for m in M_list))