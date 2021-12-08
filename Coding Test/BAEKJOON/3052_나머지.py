# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 21:16:19 2021

@author: 이충섭
"""

# 3052nd, 나머지 | class 1

div_num = [0 for _ in range(10)]

for idx in range(10):
    div_num[idx] = int(input()) % 42

diff_count = 10

for idx, num in enumerate(div_num):
    for i in range(idx+1, 10):
        if num == div_num[i]:
            diff_count -= 1
            break

print(diff_count)