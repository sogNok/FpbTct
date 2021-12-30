# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 10:08:40 2021

@author: 이충섭
"""

# 1654th, 랜선 자르기 | class 2

import sys
K, N = map(int, sys.stdin.readline().split())

Lan_cables = [int(sys.stdin.readline()) for _ in range(K)]

top = sum(Lan_cables) // N
bottom = 1
#print('top', top)
while top > bottom+1:
    length = (top + bottom) // 2
    
    count1 = 0
    count2 = 0
    for cable in Lan_cables:
        count1 += cable // length
        count2 += cable // (length+1)

    #print(length, bottom, top, count1, count2)
    if count1 > N:
        bottom = length
    elif count2 == 0 and count1 == N:
        top = length
        break
    elif count2 < N-1:
        top = length
    elif count1 == N-1:
        top = length
    elif count2 == N:
        bottom = length
    else:
        top = length
        break

count = 0
for cable in Lan_cables:
    count += cable // top

print(top if count >= N else bottom)

#%%
# 참조 답
# 깔끔, 쉬움

from sys import stdin
K, N = map(int,stdin.readline().split())
li = list(map(int,stdin.readlines()))
h, l = sum(li)//N, 1
while l <= h :
    mid = (h+l)//2
    cnt = sum([x//mid for x in li])
    if cnt < N:
        h = mid - 1
    elif cnt >= N:
        l = mid + 1
        ans = mid
print(ans)