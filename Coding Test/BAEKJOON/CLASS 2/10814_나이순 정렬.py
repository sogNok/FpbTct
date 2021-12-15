# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 14:27:30 2021

@author: 이충섭
"""

# 10814th, 나이순 정렬 | class 2
import sys # int(sys.stdin.readline().r l strip())

N = int(input())


members = [list(input().split()) for _ in range(N)]

for member in sorted(members, key=lambda item: int(item[0])):
    print(member[0], member[1])

#%%
import sys # int(sys.stdin.readline().r l strip())

N = int(sys.stdin.readline())

members = [list(sys.stdin.readline().rstrip().split()) for _ in range(N)]

for member in sorted(members, key=lambda item: int(item[0])):
    print(member[0], member[1])


