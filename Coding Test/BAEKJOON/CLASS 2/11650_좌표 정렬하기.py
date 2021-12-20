# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:28:50 2021

@author: 이충섭
"""

# 11650th, 좌표 정렬하기 | class 2
import sys # int(sys.stdin.readline().r l strip()) sys.stdout.write()

N = int(input())

locate_list = [tuple(map(int, input().split())) for _ in range(N)]

locate_list.sort()

for A, B in locate_list:
    print(A, B)
    
    
#%%
import sys

N = int(sys.stdin.readline())

locate_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

locate_list.sort()

for A, B in locate_list:
    print(A, B)
    
#%%
# 참조 답

import sys

lst = sys.stdin.readlines()[1:]
lst.sort(key=lambda x: int(x.split()[1]))
lst.sort(key=lambda x: int(x.split()[0]))
print(''.join(lst))