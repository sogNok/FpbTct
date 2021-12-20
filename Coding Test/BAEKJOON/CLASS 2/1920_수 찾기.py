# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 16:30:41 2021

@author: 이충섭
"""

# 1920th, 수 찾기 | class 2
A = [i for i in range(10)]

print(A[0:10])


#%%
import sys # int(sys.stdin.readline().r l strip()) sys.stdout.write()
def bi_find(x, sorted_list):
    len_list = len(sorted_list)
    
    if len_list == 1:
        if x == len_list:
            return 1
        else:
            return 0
    
    middle_point = len_list // 2
    predict_x = sorted_list[middle_point]
    
    if predict_x == x:
        return 1
    elif predict_x < x:
        return bi_find(x, sorted_list[middle_point :])
    else:
        return bi_find(x, sorted_list[: middle_point])
    
input()

A = sorted(map(int, input().split()))

input()

M = list(map(int, input().split()))

for m in M:
    print(bi_find(m, A))
    
#%%

import sys # int(sys.stdin.readline().r l strip()) sys.stdout.write()

def bi_find(x, sorted_list):
    len_list = len(sorted_list)
    
    if len_list == 1:
        if x == sorted_list[0]:
            return 1
        else:
            return 0
    
    middle_point = len_list // 2
    predict_x = sorted_list[middle_point]
    
    if predict_x <= x:
        return bi_find(x, sorted_list[middle_point :])
    else:
        return bi_find(x, sorted_list[: middle_point])
    

sys.stdin.readline()

A = sorted(map(int, sys.stdin.readline().split()))

sys.stdin.readline()

M = list(map(int, sys.stdin.readline().split()))

for m in M:
    sys.stdout.write(str(bi_find(m, A))+'\n')
    
#%%

import sys, bisect

N = int(sys.stdin.readline())

A = sorted(map(int, sys.stdin.readline().split()))

sys.stdin.readline()

M = list(map(int, sys.stdin.readline().split()))

for x in M:
    sys.stdout.write('1\n' if bisect.bisect_left(A, x) < N and bisect.bisect_right(A, x) > 0 else '0\n')