# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 22:08:12 2021

@author: 이충섭
"""

# 10733rd, 제로 | class 2

import sys
K = int(sys.stdin.readline())

books = [int(sys.stdin.readline()) for _ in range(K)]
stack = []

for num in books:
    if num != 0:
        stack.append(num)
    else:
        stack.pop()
        
print(sum(stack))

#%%
# 참조 답
# 간단

from sys import stdin
input()
l=[]
for i in map(int, stdin):
    l.append(i) if i else l.pop()
print(sum(l))