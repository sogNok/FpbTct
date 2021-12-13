# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 22:44:30 2021

@author: 이충섭
"""

# 1181st, 단어 정렬 | class 2

L = int(input())
str_list = sorted(set(input() for _ in range(L)), key=len)
tem_list = []

str_len = len(str_list[0])
for comp in str_list:
    if len(comp) == str_len:
        tem_list.append(comp)
    else:
        str_len = len(comp)
        for string in sorted(tem_list):
            print(string)
        tem_list = [comp]
else:
    for string in sorted(tem_list):
        print(string)
        
#%%
# 참조 답
# 멍청했음 / 스파이더가 더 멍청

import sys

L = int(sys.stdin.readline())
str_list = list(set(sys.stdin.readline().rstrip() for _ in range(L)))
str_list.sort()
str_list.sort(key=len)

print('\n'.join(str_list))