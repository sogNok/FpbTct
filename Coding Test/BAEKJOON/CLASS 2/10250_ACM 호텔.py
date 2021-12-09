# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 10:40:59 2021

@author: 이충섭
"""

# 10250th, ACM 호텔 | class 2

T = int(input())

test_data = [tuple(map(int, input().split())) for _ in range(T)]

for data in test_data:
    H, W, N = data
    
    width = N // H + 1
    height = N % H
    
    if height == 0:
        height = str(H)
        width -= 1
    else:
        height = str(height)
        
    width = '0' + str(width) if width < 10 else str(width)
    
    print(height+width)

#%%

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    width = N // H + 1
    height = N % H
    
    if height == 0:
        height = str(H)
        width -= 1
    else:
        height = str(height)
        
    width = '0' + str(width) if width < 10 else str(width)
    print(height+width)
    
#%%

# clear answer

import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    h,w,n = map(int,input().split())
    print(str((n-1)%h+1) + str((n-1)//h+1).rjust(2,'0')) 