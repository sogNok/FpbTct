# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 13:36:42 2021

@author: 이충섭
"""

# 10989th, 수 정렬하기 3 | class 2
import sys # int(sys.stdin.readline().r l strip()) sys.stdout.write()

MAX_NUM = 10001
count_list = [0 for _ in range(MAX_NUM)]
N = int(input())

for _ in range(N):
    count_list[int(input())] += 1

for x in range(1, MAX_NUM):
    for _ in range(count_list[x]):
        print(x)
    
    
#%%

import sys # int(sys.stdin.readline().r l strip())

MAX_NUM = 10001
count_list = [0 for _ in range(MAX_NUM)]
N = int(sys.stdin.readline())

for _ in range(N):
    count_list[int(sys.stdin.readline())] += 1
    
for x in range(1, MAX_NUM):
    for _ in range(count_list[x]):
        sys.stdout.write(str(x) + '\n')
        
#%%
# 참조 답

import collections, itertools, sys

next(sys.stdin)
a = collections.Counter(map(int, sys.stdin))
for i in range(10001): sys.stdout.writelines(itertools.repeat(f"{i}\n", a[i]))