# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 13:07:36 2021

@author: 이충섭
"""

# 2751st, 수 정렬하기 2 | class 2
import sys # int(sys.stdin.readline().r l strip())

N = int(input())
N_list = [int(input()) for _ in range(N)]

for n in sorted(N_list):
    print(n)


#%%
import sys

N = int(sys.stdin.readline())
N_list = [int(sys.stdin.readline()) for _ in range(N)]
N_list.sort()
sys.stdout.write('\n'.join(map(str, N_list)))